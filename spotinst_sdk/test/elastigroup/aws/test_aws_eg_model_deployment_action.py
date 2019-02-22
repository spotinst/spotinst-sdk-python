import os
import unittest

from spotinst_sdk import SpotinstSession
from spotinst_sdk.models.elastigroup.aws.deployment_action import *


class AwsElastigroupTestCase(unittest.TestCase):

    def setUp(self):
        self.session = SpotinstSession(
            auth_token='dummy-token',
            account_id='dummy-account')

        self.mock_group_json = self.load_group_json()
        self.client = self.session.client("elastigroup_aws")

    def create_formatted_deployment_request(self, deployment):
        group_request = DeploymentActionRequest(deployment)
        excluded_group_dict = self.client.exclude_missing(
            json.loads(group_request.toJSON()))
        formatted_group_dict = self.client.convert_json(
            excluded_group_dict, self.client.underscore_to_camel)
        return formatted_group_dict

    @staticmethod
    def load_group_json():
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../test_lib/input/elastigroup/deployment_action.json')) as group_json:
            return json.load(group_json)


# region B/G Deployment
class AwsElastigroupTestDeploymentAction(AwsElastigroupTestCase):
    def runTest(self):

        da = DeploymentAction(
            action_type="DETACH_NEW",
            should_handle_all_batches=True,
            draining_timeout=60,
            should_decrement_target_capacity=False
        )

        formatted_group_dict = self.create_formatted_deployment_request(da)

        actual_request_json = formatted_group_dict
        expected_request_json = self.mock_group_json

        self.assertDictEqual(actual_request_json, expected_request_json)



