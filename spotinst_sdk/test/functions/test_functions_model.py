import os
import unittest

from spotinst_sdk import SpotinstSession
from spotinst_sdk.models.functions import *

class AwsASGTestCase(unittest.TestCase):
    def setUp(self):
        self.session = SpotinstSession(
            auth_token='dummy-token',

            account_id='dummy-account')
        self.mock_app_json = self.load_json("../test_lib/input/function/app.json")
        self.mock_env_json = self.load_json("../test_lib/input/function/env.json")
        self.client = self.session.client("functions")

    def create_formatted_application_request(self, app):
        group_request = ApplicationCreationRequest(app)
        excluded_group_dict = self.client.exclude_missing(
            json.loads(group_request.toJSON()))
        formatted_group_dict = self.client.convert_json(
            excluded_group_dict, self.client.underscore_to_camel)
        return formatted_group_dict

    def create_formatted_environment_request(self, env):
        group_request = EnvironmentCreationRequest(env)
        excluded_group_dict = self.client.exclude_missing(
            json.loads(group_request.toJSON()))
        formatted_group_dict = self.client.convert_json(
            excluded_group_dict, self.client.underscore_to_camel)
        return formatted_group_dict

    @staticmethod
    def load_json(input_path):
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), input_path)) as group_json:
            return json.load(group_json)


# region Func tests
class AwsCreateApplicationTest(AwsASGTestCase):
    def runTest(self):
        application = Application(name="my application name")

        formatted_asg_dict = self.create_formatted_application_request(application)

        formatted = formatted_asg_dict
        expected = self.mock_app_json

        self.assertDictEqual(formatted, expected)

class AwsCreateEvnironmentTest(AwsASGTestCase):
    def runTest(self):
        environment = Environment(
        	name="testing", 
        	application_id="app-5470a9fb", 
        	providers=[
				"azure"
			], 
        	locations=[
				"us-east",
				"eu-west"
			])

        formatted_asg_dict = self.create_formatted_environment_request(environment)

        formatted = formatted_asg_dict
        expected = self.mock_env_json

        self.assertDictEqual(formatted, expected)
