import os
import unittest

from spotinst_sdk2 import SpotinstSession
from spotinst_sdk2.models.setup.azure import *

class AzureSetupTestCase(unittest.TestCase):
    
    def setUp(self):
        self.session = SpotinstSession(
            auth_token='dummy-token',
            account_id='dummy-account')
            
        self.client = self.session.client("setup_azure")
        
        self.mock_group_json = self.load_group_json()
        
    def create_formatted_credentials_request(self, credentials):
        credentials_request = AzureSetCredentialsRequest(credentials)
        excluded_credentials_dict = self.client.exclude_missing(
            json.loads(credentials_request.to_json()))
        formatted_group_dict = self.client.convert_json(
            excluded_credentials_dict, self.client.underscore_to_camel)
        return formatted_group_dict
        
    @staticmethod
    def load_group_json():
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../test_lib/input/setup/azure_credentials.json')) as credentials_json:
            return json.load(credentials_json)


class AzureSetupTestCredentials(AzureSetupTestCase):
    def runTest(self):
        azure_credentials = AzureCredentials(
			client_id="client_id",
			client_secret="client_secret",
			tenant_id="tenant_id",
			subscription_id="subscription_id")

        actual_request_json = self.create_formatted_credentials_request(azure_credentials)
        expected_request_json = self.mock_group_json

        self.assertDictEqual(actual_request_json, expected_request_json)