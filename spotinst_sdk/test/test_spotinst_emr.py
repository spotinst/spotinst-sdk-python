import os
import unittest

from spotinst_sdk import SpotinstClient
from spotinst_sdk.spotinst_emr import *

class SpotinstEMRTestCase(unittest.TestCase):

    def setUp(self):
        self.client = SpotinstClient(
            auth_token='dummy-token',
            account_id='act-1234567')
        self.mock_emr_json = self.load_emr_json()


    def create_formatted_emr_request(self, emr):
        emr_request = EMRCreationRequest(emr)

        excluded_emr_dict = self.client.exclude_missing(
            json.loads(emr_request.toJSON()))

        formatted_emr_dict = self.client.convert_json(
            excluded_emr_dict, self.client.underscore_to_camel)

        return formatted_emr_dict

    @staticmethod
    def load_emr_json():
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib/emr.json')) as emr_json:
            return json.load(emr_json)

class SpotinstEMRCreate(SpotinstEMRTestCase):
	def runTest(self):
		################ Scaling ################

		action = Action(		
			type="adjustment",
			adjustment=2,
			min_target_capacity=1,
			target=5,
			minimum=0,
			maximum=10)

		dimension = Dimension(name="test_dim")

		up = Metric(		
			metric_name="metric_name",
			statistic="average",
			unit="percent",
			threshold=100,
			adjustment=2,
			namespace="AWS/ElasticMapReduce",
			period=300,
			evaluation_periods=1,
			cooldown=600,
			dimensions=[dimension],
			operator="gte")

		down = Metric(		
			metric_name="metric_name",
			statistic="average",
			unit="percent",
			threshold=100,
			adjustment=2,
			namespace="AWS/ElasticMapReduce",
			period=300,
			evaluation_periods=1,
			cooldown=600,
			dimensions=[dimension],
			operator="gte")

		scaling = Scaling(up=[up], down=[down])

		################ Copmute ################

		c_file = File(bucket="test_bucket", key="test_key")

		configurations = Configurations(file=c_file)


		volume_specification = VolumeSpecification(volume_type="gp2", size_in_gb=4)

		ebs_config = SingleEbsConfig(volume_specification=volume_specification, volumes_per_instance=1)

		ebs_configuration = EbsConfiguration(ebs_block_device_configs=[ebs_config], ebs_optimized=True)

		capacity = Capacity(target=1, maximum=1, minimum=1)


		master_group = MasterGroup(instance_types=["m1.medium", "c3.xlarge", "m3.xlarge"], target=1, life_cycle="SPOT")

		core_group = CoreGroup(instance_types=["m1.medium", "c3.xlarge", "m3.xlarge"], target=1, life_cycle="SPOT", ebs_configuration=ebs_configuration)

		task_group = TaskGroup(instance_types=["m1.medium", "c3.xlarge", "m3.xlarge"], capacity=capacity, life_cycle="SPOT", ebs_configuration=ebs_configuration)

		instance_groups = InstanceGroups(master_group=master_group, core_group=core_group, task_group=task_group)


		s_file = File(bucket="test_bucket", key="test_key")

		steps = Steps(file=s_file)


		ba_file = File(bucket="test_bucket", key="test_key")

		bootstrap_actions = BootstrapActions(file=ba_file)


		compute = Compute(ebs_root_volume_size=4, availability_zones=[{"name": "us-west-2a","subnetId": "subnet-3b5b3601"}], bootstrap_actions=bootstrap_actions, steps=steps, instance_groups=instance_groups, configurations=configurations)

		################ Strategy ################

		cloning = Cloning(origin_cluster_id="123456789", include_steps=False)

		provisioning_timeout = ProvisioningTimeout(timeout=600, timeout_action="terminate")

		strategy = Strategy(cloning=cloning, provisioning_timeout=provisioning_timeout)

		name = "SDK-Test"

		description = "This was created with the SDK"

		region = "us-west-2"

		emr = EMR(name=name, description=description, region=region, strategy=strategy, compute=compute, scaling=scaling)

		formatted_emr = self.create_formatted_emr_request(emr)
		expected_emr = self.mock_emr_json

		self.assertDictEqual(formatted_emr, expected_emr)



