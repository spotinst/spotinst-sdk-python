import os
import unittest

from spotinst_sdk2 import SpotinstSession
from spotinst_sdk2.models.elastigroup.aws.asg import *

class AwsASGTestCase(unittest.TestCase):
    def setUp(self):
        self.session = SpotinstSession(
            auth_token='dummy-token',
            account_id='dummy-account')

        self.mock_asg_json = self.load_asg_json()

        self.client = self.session.client("elastigroup_aws")

    def create_formatted_asg_request(self, asg):
        group_request = ImportASGRequest(asg)
        excluded_group_dict = self.client.exclude_missing(
            json.loads(group_request.toJSON()))
        formatted_group_dict = self.client.convert_json(
            excluded_group_dict, self.client.underscore_to_camel)
        return formatted_group_dict

    @staticmethod
    def load_asg_json():
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../test_lib/input/elastigroup/import_asg.json')) as group_json:
            return json.load(group_json)


# region B/G Deployment
class AwsImportASGTest(AwsASGTestCase):
    def runTest(self):
        asg = ASG(
            product="Linux/UNIX",
            spot_instance_types=[
                "c3.large",
                "m4.large"
            ],
            name="My Group")


        formatted_asg_dict = self.create_formatted_asg_request(asg)

        formatted = formatted_asg_dict
        expected = self.mock_asg_json

        self.assertDictEqual(formatted, expected)



