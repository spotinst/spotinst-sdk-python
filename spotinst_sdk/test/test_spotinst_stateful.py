import os
import unittest

from spotinst_sdk import SpotinstClient
from spotinst_sdk.spotinst_stateful import *

class SpotinstEMRTestCase(unittest.TestCase):

    def setUp(self):
        self.client = SpotinstClient(
            auth_token='dummy-token',
            account_id='act-1234567')
        self.mock_stateful_json = self.load_stateful_json()


    def create_formatted_import_stateful(self, stateful_instance):
        stateful_instance = StatefulImportRequest(stateful_instance)

        excluded_stateful_dict = self.client.exclude_missing(
            json.loads(stateful_instance.toJSON()))

        formatted_stateful_dict = self.client.convert_json(
            excluded_stateful_dict, self.client.underscore_to_camel)

        return formatted_stateful_dict

    @staticmethod
    def load_stateful_json():
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test_lib/stateful/import_stateful.json')) as stateful_json:
            return json.load(stateful_json)

class SpotinstImportStateful(SpotinstEMRTestCase):
	def runTest(self):

		availability_zones= AvailabilityZone(name="us-west-2a",subnet_ids=["subnet-79da021e"])

		stateful_instance = StatefulInstance(
			should_keep_private_ip=False , 
			original_instance_id="i-08807e080f8c3e681" , 
			name="Test" , 
			product="Linux/UNIX" , 
			spot_instance_types=["m1.medium", "c3.xlarge", "m3.xlarge"] ,
			region="us-west-2" ,
			availability_zones=[availability_zones])

		formatted_stateful = self.create_formatted_import_stateful(stateful_instance)
		expected_stateful = self.mock_stateful_json

		self.assertDictEqual(formatted_stateful, expected_stateful)



