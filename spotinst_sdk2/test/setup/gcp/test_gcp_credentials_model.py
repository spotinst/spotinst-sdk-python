import os
import unittest

from spotinst_sdk2 import SpotinstSession
from spotinst_sdk2.models.setup.gcp import *

class GcpSetupTestCase(unittest.TestCase):
    
    def setUp(self):
        self.session = SpotinstSession(
            auth_token='dummy-token',
            account_id='dummy-account')
            
        self.client = self.session.client("setup_azure")
        
        self.mock_group_json = self.load_group_json()
        
    def create_formatted_credentials_request(self, credentials):
        credentials_request = GcpSetCredentialsRequest(credentials)
        excluded_credentials_dict = self.client.exclude_missing(
            json.loads(credentials_request.to_json()))
        return excluded_credentials_dict
        
    @staticmethod
    def load_group_json():
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../test_lib/input/setup/gcp_credentials.json')) as credentials_json:
            return json.load(credentials_json)


class GcpSetupTestCredentials(GcpSetupTestCase):
    def runTest(self):
        service_account = ServiceAccount(
			type="type",
			project_id="project_id",
			private_key_id="private_key_id",
			private_key="private_key",
			client_email="client_email",
			client_id="client_id",
			auth_uri="auth_uri",
			token_uri="token_uri",
			auth_provider_x509_cert_url="auth_provider_x509_cert_url",
			client_x509_cert_url="client_x509_cert_url")
            
        gcp_credentials = GcpCredentials(serviceAccount=service_account)

        actual_request_json = self.create_formatted_credentials_request(gcp_credentials)
        expected_request_json = self.mock_group_json

        self.assertDictEqual(actual_request_json, expected_request_json)