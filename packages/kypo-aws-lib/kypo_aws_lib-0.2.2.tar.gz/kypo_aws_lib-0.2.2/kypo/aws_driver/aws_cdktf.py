import os
from typing import List
from kypo.cloud_commons import TopologyInstance, SecurityGroups, MAN_NAME, MAN_NET_NAME
from kypo.cloud_commons.topology_elements import Host, Link, Node, Router
from kypo_aws_commons.security_groups.construct import SecurityGroupsConstruct

from constructs import Construct
from cdktf import App, TerraformStack, LocalBackend

from cdktf_cdktf_provider_aws.provider import AwsProvider
from cdktf_cdktf_provider_aws.vpc import Vpc
from cdktf_cdktf_provider_aws.data_aws_vpc import DataAwsVpc
from cdktf_cdktf_provider_aws.subnet import Subnet
from cdktf_cdktf_provider_aws.data_aws_subnet import DataAwsSubnet
from cdktf_cdktf_provider_aws.instance import Instance, InstanceNetworkInterface
from cdktf_cdktf_provider_aws.network_interface import NetworkInterface
from cdktf_cdktf_provider_aws.route_table import RouteTable, RouteTableRoute
from cdktf_cdktf_provider_aws.route_table_association import RouteTableAssociation
from cdktf_cdktf_provider_aws.data_aws_security_group import DataAwsSecurityGroup


CDKTF_OUTPU_DIR = '/tmp'
CDKTF_STACK_NAME = 'sandbox'
CDKTF_TEMPLATE_FILE_NAME = 'cdk.tf.json'
CDKTF_OUTPUT_FILE = f'{CDKTF_OUTPU_DIR}/stacks/{CDKTF_STACK_NAME}/{CDKTF_TEMPLATE_FILE_NAME}'
CONFIG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config')
CONFIG_SECURITY_GROUPS = os.path.join(CONFIG_DIR, 'security_groups.yaml')
HOST_ROUTING_SCRIPT = '''#!/bin/bash
ip r del default
ip r add default via {}
'''


class AwsNetwork:

    def __init__(self, stack: TerraformStack, topology_instance: TopologyInstance,
                 availability_zone: str, resource_prefix: str):
        _name = f'{resource_prefix}-'
        network_name = _name + 'network-{}'
        self.networks = {net.name:
                         Vpc(stack, network_name.format(net.name), cidr_block=net.cidr,
                             tags={'Name': network_name.format(net.name)})
                         for net in topology_instance.get_networks()}

        base_net = DataAwsVpc(stack, 'base-net', tags={'Name': 'Base Net'})

        self.security_groups = {SecurityGroups.SANDBOX_ACCESS.value:
                                DataAwsSecurityGroup(stack, 'data-sg', vpc_id=base_net.id,
                                                     name='kypo-sandbox-access-sg')}

        for net_name, vpc in self.networks.items():
            sec_group_cons = SecurityGroupsConstruct.from_file(stack, net_name, vpc.id,
                                                               CONFIG_SECURITY_GROUPS)
            self.security_groups[net_name] = sec_group_cons.aws_groups_dict

        subnet_name = _name + 'subnet-{}'
        self.subnets = {net_name:
                        Subnet(stack, subnet_name.format(net_name), vpc_id=vpc.id,
                               cidr_block=vpc.cidr_block,
                               map_public_ip_on_launch=False,
                               availability_zone=availability_zone,
                               tags={'Name': subnet_name.format(net_name)})
                        for net_name, vpc in self.networks.items()}


class KypoInstance:

    def __init__(self, stack: TerraformStack, node: Host, link_name: str,
                 key_pair_ssh,  # TODO type, and windows certs??
                 subnet_id: str,
                 security_group_ids: List[str],
                 resource_prefix: str,
                 user_data: str = '',
                 ):
        self._prefixed_name = resource_prefix + '-{}'
        self.stack = stack
        net_int = NetworkInterface(stack, self._prefixed_name.format(link_name),
                                   subnet_id=subnet_id,
                                   security_groups=security_group_ids,
                                   source_dest_check=False)

        self.instance = Instance(stack, self._prefixed_name.format(node.name),
                                 ami=node.base_box.image,
                                 instance_type=node.flavor,
                                 key_name=key_pair_ssh,
                                 network_interface=[InstanceNetworkInterface(
                                     device_index=0,
                                     network_interface_id=net_int.id
                                 )],
                                 user_data=user_data,
                                 tags={'Name': self._prefixed_name.format(node.name)})

    def add_network_interface(self, link: Link, subnet_id: str, security_group_ids: List[str]):
        net_int = NetworkInterface(self.stack, self._prefixed_name.format(link.name),
                                   subnet_id=subnet_id,
                                   security_groups=security_group_ids,
                                   source_dest_check=False,
                                   private_ips=[link.ip] if link.ip else None)

        instance_interfaces = self.instance.network_interface_input
        instance_interfaces.append(InstanceNetworkInterface(
            device_index=len(instance_interfaces),
            network_interface_id=net_int.id
        ))
        self.instance.put_network_interface(instance_interfaces)

        return net_int


class AwsStack(TerraformStack):  # Possibly create a cdktf interface (or abstract class)

    def __init__(self, scope: Construct, id: str, topology_instance: TopologyInstance,
                 region: str, access_key: str, secret_key: str, availability_zone: str,
                 key_pair_name_ssh, key_pair_name_cert, resource_prefix: str):
        super().__init__(scope, id)
        LocalBackend(self, path='terraform.tfstate')
        AwsProvider(self, 'aws', region=region, access_key=access_key,
                    secret_key=secret_key)

        self.topology_instance = topology_instance
        self.key_pair_name_ssh = key_pair_name_ssh
        self.resource_prefix = resource_prefix
        self.aws_networks = AwsNetwork(self, topology_instance, availability_zone, resource_prefix)
        man = topology_instance.get_node(MAN_NAME)
        base_sb = DataAwsSubnet(self, 'base-sb',
                                tags={'Name': 'Base Subnet'})  # TODO: read name of subnet from TRC
        man_instance = KypoInstance(self, man, 'man-out-port', key_pair_name_ssh, base_sb.id,
                                    [self.aws_networks.security_groups[SecurityGroups.SANDBOX_ACCESS.value].id],
                                    resource_prefix)

        self.wan = topology_instance.get_network('wan')
        man_wan_link = topology_instance.get_link_between_node_and_network(man, self.wan)
        self.add_instance_link(man_instance, man_wan_link)

        self.man_net = topology_instance.get_network(MAN_NET_NAME)
        man_man_net_link = topology_instance.get_link_between_node_and_network(man, self.man_net)
        self.add_instance_link(man_instance, man_man_net_link)

        for router in topology_instance.get_routers():
            self.create_router(router)

        for host_network in topology_instance.get_hosts_networks():
            for link in topology_instance.get_network_links(host_network, topology_instance.get_hosts()):
                self.create_host(link)

    def create_kypo_instance(self, node: Node, link: Link, user_data: str = ''):
        """
        Create KypoInstance for generic node (Router/Host).
        From the link the node and corresponding network can be read.
        """
        subnet = self.aws_networks.subnets[link.network.name]
        security_group = self.aws_networks.security_groups[link.network.name][link.security_group].id

        return KypoInstance(self, node, link.name, self.key_pair_name_ssh, subnet.id,
                            [security_group], self.resource_prefix, user_data)

    def add_instance_link(self, instance: KypoInstance, link: Link):
        """
        Add Network Interface to Kypo instance.
        """
        subnet = self.aws_networks.subnets[link.network.name]
        security_group = self.aws_networks.security_groups[link.network.name][link.security_group].id
        return instance.add_network_interface(link, subnet.id, [security_group])

    def create_host(self, link: Link):
        """
        Create Host Kypo instance.
        Created instance is first connected to the host network (connection with router),
        secondly connected to the MAN network.
        """
        host = self.topology_instance.get_node(link.node.name)
        host_network = self.topology_instance.get_network(link.network.name)
        default_ip = self.topology_instance.get_network_default_gateway_link(host_network)
        user_data = HOST_ROUTING_SCRIPT.format(default_ip.ip)
        host_instance = self.create_kypo_instance(host, link, user_data)

        man_net_link = self.topology_instance.get_link_between_node_and_network(host, self.man_net)
        self.add_instance_link(host_instance, man_net_link)

    def create_router(self, router: Router):
        """
        Create Router Kypo instance.
        Created instance is first connected to the WAN network. Then, the connections to the host
        networks are made. Finally, the router is conneted to the MAN network.
        """
        wan_link = self.topology_instance.get_link_between_node_and_network(router, self.wan)
        router_instance = self.create_kypo_instance(router, wan_link)

        for link in self.topology_instance.get_node_links(router,
                                                          self.topology_instance.get_hosts_networks()):
            router_interface = self.add_instance_link(router_instance, link)
            subnet = self.aws_networks.subnets[link.network.name]
            vpc = self.aws_networks.networks[link.network.name]
            def_route = RouteTable(self, '{}-default-route'.format(link.network.name),
                                   vpc_id=vpc.id,
                                   route=[
                                       RouteTableRoute(cidr_block='0.0.0.0/0',
                                                       network_interface_id=router_interface.id)
                                       ]
                                   )
            RouteTableAssociation(self, '{}-def-router-assoc'.format(link.network.name),
                                  subnet_id=subnet.id,
                                  route_table_id=def_route.id)

        man_net_link = self.topology_instance.get_link_between_node_and_network(router, self.man_net)
        self.add_instance_link(router_instance, man_net_link)


def read_template():
    with open(CDKTF_OUTPUT_FILE) as file:
        return file.read()


def cdktf_create_template(topology_instance: TopologyInstance, region: str, access_key: str,
                          secret_key: str, availability_zone: str,
                          key_pair_name_ssh: str = 'kypo-dummy-ssh-key-pair',
                          key_pair_name_cert: str = 'kypo-dummy-cert-key-pair',
                          resource_prefix: str = 'stack-name'):
    app = App(outdir=CDKTF_OUTPU_DIR, skip_validation=True)
    AwsStack(app, CDKTF_STACK_NAME, topology_instance, region, access_key, secret_key,
             availability_zone, key_pair_name_ssh, key_pair_name_cert, resource_prefix)
    app.synth()
    return read_template()
