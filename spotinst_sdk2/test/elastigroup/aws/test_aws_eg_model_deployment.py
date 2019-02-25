import os
import unittest

from spotinst_sdk2 import SpotinstSession
from spotinst_sdk2.models.elastigroup.aws.deployment import *


class AwsElastigroupTestCase(unittest.TestCase):

    def setUp(self):
        self.session = SpotinstSession(
            auth_token='dummy-token',
            account_id='dummy-account')

        self.mock_group_json = self.load_group_json()

        self.client = self.session.client("elastigroup_aws")

    def create_formatted_deployment_request(self, deployment):
        group_request = BlueGreenDeploymentRequest(deployment)
        excluded_group_dict = self.client.exclude_missing(
            json.loads(group_request.toJSON()))
        formatted_group_dict = self.client.convert_json(
            excluded_group_dict, self.client.underscore_to_camel)
        return formatted_group_dict

    @staticmethod
    def load_group_json():
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../test_lib/input/elastigroup/bg_deployment.json')) as group_json:
            return json.load(group_json)


# region B/G Deployment
class AwsElastigroupTestBGDeployment(AwsElastigroupTestCase):
    def runTest(self):
        tags = [Tag(tag_key="key", tag_value="value")]
        deployment_groups = [DeploymentGroup(application_name="appTest",deployment_group_name="deploymentGroupTest")]

        bgd = BlueGreenDeployment(
            timeout=20,
            tags=tags,
            deployment_groups=deployment_groups
        )

        formatted_group_dict = self.create_formatted_deployment_request(bgd)

        actual_request_json = formatted_group_dict
        expected_request_json = self.mock_group_json

        self.assertDictEqual(actual_request_json, expected_request_json)



