import os
import unittest

from spotinst_sdk2 import SpotinstSession
from spotinst_sdk2.models.managed_instance.aws import *


class SimpleNamespace:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class AwsManagedInstanceTestCase(unittest.TestCase):

    def setUp(self):
        self.session = SpotinstSession(
            auth_token='dummy-token',
            account_id='dummy-account')

        self.client = self.session.client("managed_instance_aws")
        self.mock_mi_json = self.load_json()

    def create_formatted_mi_request(self, managed_instance):
        group_request = ManagedInstanceCreationRequest(managed_instance)
        excluded_group_dict = self.client.exclude_missing(
            json.loads(group_request.toJSON()))
        formatted_group_dict = self.client.convert_json(
            excluded_group_dict, self.client.underscore_to_camel)
        return formatted_group_dict

    @staticmethod
    def load_json():
        file_path = '../../test_lib/input/managed_instance/aws_managed_instance.json'
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), file_path)) as ma_json:
            return json.load(ma_json)


class TestAwsManagedInstancePersistRootDevice(AwsManagedInstanceTestCase):
    def runTest(self):
        persistence_obj = Persistence(True, False, "onLaunch", False)
        mi_obj = ManagedInstance(persistence=persistence_obj)
        formatted_mi_request = self.create_formatted_mi_request(mi_obj)

        actual_request_persist_root = formatted_mi_request['managedInstance']['persistence']['persistRootDevice']
        expected_request_persist_root = self.mock_mi_json['managedInstance']['persistence']['persistRootDevice']

        self.assertEqual(actual_request_persist_root, True)
        self.assertEqual(actual_request_persist_root, expected_request_persist_root)


class TestAwsManagedInstancePersistence(AwsManagedInstanceTestCase):
    def runTest(self):
        persistence_obj = Persistence(True, True, "onLaunch")
        mi_obj = ManagedInstance(persistence=persistence_obj)
        formatted_mi_request = self.create_formatted_mi_request(mi_obj)

        actual_request_json = formatted_mi_request['managedInstance']['persistence']
        expected_request_json = self.mock_mi_json['managedInstance']['persistence']

        self.assertDictEqual(actual_request_json, expected_request_json)


class TestAwsManagedInstanceIntegrationsRoute53DomainsConfiguration(AwsManagedInstanceTestCase):
    def runTest(self):
        recordset_config = Route53RecordSetConfiguration(name="someName", use_public_ip=True, use_public_dns=True)
        route_53_domains_config = Route53DomainConfiguration(hosted_zone_id="123", spotinst_account_id="foo",
                                                             record_set_type="bar", record_sets=[recordset_config])
        route_53_config = Route53Configuration(domains=[route_53_domains_config])
        integrations_config = IntegrationsConfig(route53=route_53_config)
        mi_obj = ManagedInstance(integrations=integrations_config)

        formatted_mi_request = self.create_formatted_mi_request(mi_obj)

        actual_request_json = formatted_mi_request['managedInstance']['integrations']["route53"]["domains"][0]
        expected_request_json = self.mock_mi_json['managedInstance']['integrations']["route53"]["domains"][0]

        self.assertDictEqual(actual_request_json, expected_request_json)


class TestAwsManagedInstanceIntegrationsLoadBalancersConfiguration(AwsManagedInstanceTestCase):
    def runTest(self):
        lb = LoadBalancer(name="name", arn="arn", type="MULTAI_TARGET_SET", balancer_id="lb-1ee2e3q",
                          target_set_id="ts-3eq", az_awareness=True, auto_weight=True)
        lbs_config = LoadBalancersConfiguration(load_balancers=[lb])
        integrations_config = IntegrationsConfig(load_balancers_config=lbs_config)
        mi_obj = ManagedInstance(integrations=integrations_config)

        formatted_mi_request = self.create_formatted_mi_request(mi_obj)

        actual_request_json = formatted_mi_request['managedInstance']['integrations']["loadBalancersConfig"]
        expected_request_json = self.mock_mi_json['managedInstance']['integrations']["loadBalancersConfig"]

        self.assertDictEqual(actual_request_json, expected_request_json)


class TestAwsManagedInstanceComputeLaunchSpecification(AwsManagedInstanceTestCase):
    def runTest(self):
        # block_device_mappings
        ebs = EBS(delete_on_termination=True, iops=0, throughput=125, volume_type="gp2", volume_size=12)
        block_device_mappings = [BlockDeviceMapping(device_name="/dev/xvdcz", ebs=ebs)]
        # network_interfaces
        network_interfaces = [
            NetworkInterface(device_index=0, associate_ipv6_address=True, associate_public_ip_address=True)]
        # credit_specification
        credit_specification = CreditSpecification(cpu_credits="unlimited")
        # shutdown_script & user_data
        shutdown_script = "dXNlcmJhc2g2NGVuY29kZWQ="
        user_data = "dXNlcmJhc2g2NGVuY29kZWQ="
        # resource_tag_specification
        resource_tag_spec = ResourceTagSpecification(volumes=TagSpecification(should_tag=False),
                                                     snapshots=TagSpecification(should_tag=True),
                                                     enis=TagSpecification(should_tag=False),
                                                     amis=TagSpecification(should_tag=True))
        # tags
        tags = [Tag(tag_key="Creator", tag_value="test1@spot.io")]
        # key_pair & image_id
        key_pair = "labs-oregon"
        image_id = "ami-01e24be29428c15b2"
        # security_group_ids
        security_group_ids = ["sg-0dfc2c8760df6fec7"]
        # iam_role
        iam_role = IamRole(name="name", arn="arn")
        # tenancy
        tenancy = "default"
        # monitoring
        monitoring = False
        # ebs_optimized
        ebs_optimized = False
        # instance_types
        instance_types = InstanceTypes(preferred_type="t2.micro", types=["t2.micro"])

        launch_spec = LaunchSpecification(block_device_mappings=block_device_mappings,
                                          network_interfaces=network_interfaces,
                                          credit_specification=credit_specification, shutdown_script=shutdown_script,
                                          user_data=user_data, resource_tag_specification=resource_tag_spec, tags=tags,
                                          key_pair=key_pair, image_id=image_id, security_group_ids=security_group_ids,
                                          iam_role=iam_role, tenancy=tenancy, monitoring=monitoring,
                                          ebs_optimized=ebs_optimized, instance_types=instance_types
                                          )
        mi_obj = ManagedInstance(compute=Compute(launch_specification=launch_spec))

        formatted_mi_request = self.create_formatted_mi_request(mi_obj)

        actual_request_json = formatted_mi_request['managedInstance']['compute']["launchSpecification"]
        expected_request_json = self.mock_mi_json['managedInstance']['compute']["launchSpecification"]

        self.assertDictEqual(actual_request_json, expected_request_json)
