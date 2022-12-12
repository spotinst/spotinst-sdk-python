import os
import unittest

from spotinst_sdk2 import SpotinstSession
from spotinst_sdk2.models.elastigroup.azure_v3 import *

class AzureV3ElastigroupTestCase(unittest.TestCase):

    def setUp(self):
        self.session = SpotinstSession(
            auth_token='dummy-token',
            account_id='dummy-account')

        self.client = self.session.client("elastigroup_azure_v3")

        self.mock_group_json = self.load_group_json()

    def create_formatted_group_request(self, group):
        group_request = ElastigroupCreateRequest(group)
        excluded_group_dict = self.client.exclude_missing(
            json.loads(group_request.toJSON()))
        formatted_group_dict = self.client.convert_json(
            excluded_group_dict, self.client.underscore_to_camel)
        return formatted_group_dict

    @staticmethod
    def load_group_json():
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../test_lib/input/elastigroup/azure_v3_group.json')) as group_json:
            return json.load(group_json)

# region Elastigroup
class AzureV3ElastigroupTest(AzureV3ElastigroupTestCase):
    def runTest(self):
        ############################# Capacity #############################
        capacity = Capacity(minimum=0, maximum=10, target=5)

        ############################# Compute ##############################

        # Boot Diagnostics
        boot_diagnostics = BootDiagnostics(is_enabled=True, type="managed")

        data_disks = [DataDisk(lun=0, size_gb=8, type='Standard_LRS'),
                      DataDisk(lun=1, size_gb=32, type='StandardSSD_LRS')]

        os_disk = OsDisk(size=8, type='Standard_LRS')

        marketplace = Marketplace(publisher="Canonical", version="latest", sku="18.04-LTS", offer="UbuntuServer")

        image = Image(marketplace=marketplace)

        # Network Interfaces
        interface = NetworkInterface(is_primary=True, assign_public_ip=False, subnet_name="Automation-PrivateSubnet",
                                     enable_ip_forwarding=True)
        network_interfaces = [interface]

        # Network
        network = Network(network_interfaces=network_interfaces, virtual_network_name='Automation-VirtualNetwork',
                          resource_group_name='AutomationResourceGroup')

        # Login
        login = Login(user_name="ubuntu",
                      ssh_public_key="ssh-rsa dummy key")

        # Tags
        tag_creator = Tag(tag_key="Creator", tag_value="Spotinst-Python-SDK")
        tag_name = Tag(tag_key="Name", tag_value="Spotinst-Elastigroup-Instance")
        tags = [tag_creator, tag_name]

        # Launch Specification
        launch_spec = LaunchSpecification(boot_diagnostics=boot_diagnostics, image=image, login=login, network=network,
                                          tags=tags, os_disk=os_disk, custom_data="TXkgQ3VzdG9tIERhdGE=",
                                          shutdown_script="TXkgU2h1dGRvd24gU2NyaXB0", data_disks = data_disks)

        # VmSizes
        vm_sizes = VmSizes(od_sizes=['standard_a1_v2', 'standard_a2_v2'],
                           spot_sizes=['standard_a1_v2', 'standard_a2_v2'],
                           preferred_spot_sizes=['standard_a1_v2'])

        # Compute
        compute = Compute(launch_specification=launch_spec, os='Linux', vm_sizes=vm_sizes)

        ############################# Strategy ##############################
        strategy = Strategy(draining_timeout=240, spot_percentage=100, orientation='cost', fallback_to_od=True)

        ############################# Health ################################
        health = Health(health_check_types=["vmState"], auto_healing=True, grace_period=350, unhealthy_duration=300)

        ############################# Scaling ###############################
        # Scaling Policy Action
        scaling_policy_action = ScalingPolicyAction(type="adjustment", adjustment="2")

        # Scaling Policy
        scaling_policy = ScalingPolicy(is_enabled=True, policy_name="cpuScaleUp", namespace="Microsoft.Compute",
                                       metric_name="Percentage CPU", statistic="average", unit="percent", threshold=60,
                                       period=300, evaluation_periods=3, cooldown=600, action=scaling_policy_action,
                                       operator="gt")
        up = [scaling_policy]

        # Scaling
        scaling = Scaling(up=up)

        ############################# Scheduling #############################
        # Scheduling Task
        scheduling_task_1 = SchedulingTask(is_enabled=True, cron_expression="* * * 1 *", type="deployment",
                                           batch_size_percentage=10, grace_period=200)

        scheduling_task_2 = SchedulingTask(is_enabled=True, cron_expression="*/2 * * * *", type="scaleUp",
                                           adjustment=2)

        # Scheduling
        scheduling = Scheduling(tasks=[scheduling_task_1, scheduling_task_2])

        # Elastigroup
        group = Elastigroup(name='Python-Test', region='eastus', resource_group_name='AutomationResourceGroup',
                            capacity=capacity, strategy=strategy, compute=compute, scheduling=scheduling, health=health,
                            scaling=scaling)

        formatted_group_dict = self.create_formatted_group_request(group)

        print(formatted_group_dict)
        print(self.mock_group_json)

        self.assertDictEqual(formatted_group_dict, self.mock_group_json)

