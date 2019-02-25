import os
import unittest

from spotinst_sdk2 import SpotinstSession
from spotinst_sdk2.models.ocean.aws import *

class SpotinstOceanTestCase(unittest.TestCase):

    def setUp(self):
        self.session = SpotinstSession(
            auth_token='dummy-token',
            account_id='act-1234567')

        self.mock_ocean_json = self.load_ocean_json()
        self.client = self.session.client("ocean_aws")


    def create_formatted_ocean(self, ocean):
        ocean_request = OceanRequest(ocean)

        excluded_ocean_dict = self.client.exclude_missing(
            json.loads(ocean_request.toJSON()))

        formatted_ocean_dict = self.client.convert_json(
            excluded_ocean_dict, self.client.underscore_to_camel)

        return formatted_ocean_dict

    @staticmethod
    def load_ocean_json():
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../test_lib/input/ocean/ocean_cluster.json')) as cluster_json:
            return json.load(cluster_json)

class SpotinstOceanCluster(SpotinstOceanTestCase):
	def runTest(self):
		################ Compute ################

		single_tag = Tag(tag_key="testing", tag_value="tags")

		launch_specification = LaunchSpecifications(security_group_ids=["sg-8cfb40f6"],
		 image_id="ami-1178f169", key_pair="Noam-key", tags=[single_tag])

		instance_types = InstanceTypes(whitelist=["c4.8xlarge"])

		compute = Compute(instance_types=instance_types, subnet_ids=["subnet-1ba25052"], launch_specification=launch_specification)

		################ Strategy ################

		strategy = Strategy(utilize_reserved_instances=False, fallback_to_od=True, spot_percentage=100)

		################ Capacity ################

		capacity = Capacity(minimum=0, maximum=0, target=0)

		################ AutoScaler ################

		down = Down(evaluation_periods=3)

		headroom = Headroom(cpu_per_unit=2000, memory_per_unit=0, num_of_units=4)

		resource_limits = ResourceLimits(max_memory_gib=1500, max_vCpu=750)

		auto_scaler = AutoScaler(is_enabled=True, cooldown=180, resource_limits=resource_limits, down=down, 
			headroom=headroom, is_auto_config=True)

		################ Test ################

		region = "us-west-2"

		controller_cluster_id = "ocean.k8s"

		name = "Ocean SDK Test"

		ocean = Ocean(name=name, controller_cluster_id=controller_cluster_id, region=region, 
			auto_scaler=auto_scaler, capacity=capacity, strategy=strategy, compute=compute)

		formatted_ocean = self.create_formatted_ocean(ocean)
		expected_ocean = self.mock_ocean_json

		self.assertDictEqual(formatted_ocean, expected_ocean)
