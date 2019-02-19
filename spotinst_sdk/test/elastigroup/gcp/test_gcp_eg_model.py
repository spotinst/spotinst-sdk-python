import os
import unittest

from spotinst_sdk import SpotinstSession
from spotinst_sdk.models.elastigroup.gcp import *

class GcpElastigroupTestCase(unittest.TestCase):

    def setUp(self):
        self.session = SpotinstSession(
            auth_token='dummy-token',
            account_id='dummy-account')

        self.client = self.session.client("elastigroup_gcp")

        self.mock_group_json = self.load_group_json()

    def create_formatted_group_request(self, group):
        group_request = ElastigroupCreationRequest(group)
        excluded_group_dict = self.client.exclude_missing(
            json.loads(group_request.toJSON()))
        formatted_group_dict = self.client.convert_json(
            excluded_group_dict, self.client.underscore_to_camel)
        return formatted_group_dict

    @staticmethod
    def load_group_json():
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../test_lib/input/elastigroup/gcp_group.json')) as group_json:
            return json.load(group_json)

# region Elastigroup
class GcpElastigroupTest(GcpElastigroupTestCase):
    def runTest(self):
        ###################### Capacity ######################
        capacity = Capacity(minimum=0, maximum=0, target=0)

        ###################### Strategy ######################
        strategy = Strategy(
          preemptible_percentage=100,
          on_demand_count=0,
          draining_timeout=0,
          fallback_to_od=False)

        ####################### Scaling ######################
        dim = ScalingPolicyDimension(name="name", value="value")

        action = ScalingPolicyAction(scaling_type="adjustment", adjustment=0)

        up = ScalingPolicy(
          source="spectrum",
            policy_name="policy_name",
            namespace="namespace",
            metric_name="metric_name",
            dimensions=[dim],
            statistic="average",
            unit="seconds",
            threshold=0,
            period=60,
            evaluation_periods=1,
            cooldown=0,
            action=action,
            operator="gte")

        down = ScalingPolicy(
          source="spectrum",
            policy_name="policy_name",
            namespace="namespace",
            metric_name="metric_name",
            dimensions=[dim],
            statistic="average",
            unit="seconds",
            threshold=0,
            period=60,
            evaluation_periods=1,
            cooldown=0,
            action=action,
            operator="gte")

        scaling = Scaling(up=[up], down=[down])

        ############## ThirdPartiesIntegration ##############
        docker_swarm = DockerSwarmConfiguration(master_host="master_host", master_port=1)

        third_parties_integration = ThirdPartiesIntegration(docker_swarm=docker_swarm)

        ###################### Compute ######################
        subnet = Subnet(region="us-west2", subnet_names=["subnet_names"])

        health = Health(grace_period=0)

        gpu = Gpu(gpu_type="nvidia-tesla-v100", count=1)

        custom = CustomInstanceTypes(v_cpu=1, memory_gib=1)

        instance_types = InstanceTypes(ondemand="ondemand", preemptible=["preemptible"], custom=[custom])

        label = Label(key="key", value="value")

        metadata = Metadata(key="key", value="value")

        named_ports = NamedPorts(name="name", ports=[1,2,3])

        backend_services = BackendServices(
            backend_service_name="backend_service_name",
            location_type="regional",
            scheme="EXTERNAL",
            named_ports=named_ports)

        backend_service_config = BackendServiceConfig(backend_services=[backend_services])

        initialize_params = InitializeParams(            
          disk_size_gb=1,
            disk_type="disk_type",
            source_image="source_image")

        disk = Disk(           
          auto_delete=False,
            boot=False,
            device_name="device_name",
            initialize_params=initialize_params,
            interface="SCSI",
            mode="READ_WRITE",
            source="source",
            disk_type="disk_type")

        access_configs = AccessConfig(name="name", access_type="ONE_TO_ONE_NAT")

        alias_ip_ranges = AliasIpRange(ip_cidr_range="ip_cidr_range", subnetwork_range_name="subnetwork_range_name")

        network_interfaces = NetworkInterface(            
          network="network",
            access_configs=[access_configs],
            alias_ip_ranges=[alias_ip_ranges])

        launch_specification = LaunchSpecification(
            labels=[label],
            metadata=[metadata],
            tags=["tags"],
            backend_service_config=backend_service_config,
            startup_script="startup_script",
            disks=[disk],
            network_interfaces=[network_interfaces],
            service_account="service_account",
            ip_forwarding=False)

        compute = Compute(
          launch_specification=launch_specification,
            instance_types=instance_types,
            gpu=gpu,
            health=health,
            availability_zones=["us-west2-a"],
            subnets=[subnet])

        #################### Elastigroup ####################
        elastigroup = Elastigroup(
          name="name", 
          description="description", 
          capacity=capacity, 
          strategy=strategy, 
          scaling=scaling, 
          third_parties_integration=third_parties_integration, 
          compute=compute)

        formatted_group_dict = self.create_formatted_group_request(elastigroup)

        self.assertDictEqual(formatted_group_dict, self.mock_group_json)

