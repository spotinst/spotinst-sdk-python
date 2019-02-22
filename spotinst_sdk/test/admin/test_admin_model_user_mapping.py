import os
import unittest

from spotinst_sdk import SpotinstSession
from spotinst_sdk.models.admin.user_mapping import *


class AwsElastigroupTestCase(unittest.TestCase):

    def setUp(self):
        self.session = SpotinstSession(
            auth_token='dummy-token',
            account_id='dummy-account')

        self.client = self.session.client("admin")
        self.mock_mapping_json = self.load_mapping_json()

    def create_formatted_mapping_request(self, mappings):
        group_request = UserMappingRequest(mappings)
        excluded_group_dict = self.client.exclude_missing(
            json.loads(group_request.toJSON()))
        formatted_group_dict = self.client.convert_json(
            excluded_group_dict, self.client.underscore_to_camel)
        return formatted_group_dict

    @staticmethod
    def load_mapping_json():
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../test_lib/input/admin/user_mapping.json')) as group_json:
            return json.load(group_json)


# region User Mapping
class AwsAdminUserMappingTest(AwsElastigroupTestCase):
    def runTest(self):
        mappings = [
            UserMapping(
                user_email="test@spotinst.ocom",
                account_id="act-123abc",
                role="editor"
            ),
            UserMapping(
                user_email="test2@spotinst.com",
                account_id="act-123abc",
                role="viewer"
            )
        ]


        formatted_mapping_dict = self.create_formatted_mapping_request(mappings)

        actual_request_json = formatted_mapping_dict
        expected_request_json = self.mock_mapping_json

        self.assertDictEqual(actual_request_json, expected_request_json)



