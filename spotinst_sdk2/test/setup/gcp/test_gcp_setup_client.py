import os
import unittest
import json
from mock import patch

from spotinst_sdk2 import SpotinstSession
from spotinst_sdk2.models.setup.gcp import *

class SimpleNamespace:
	def __init__(self, **kwargs):
		self.__dict__.update(kwargs)

class GcpInitTestCase(unittest.TestCase):
	def setUp(self):
		self.session = SpotinstSession(
			auth_token='dummy-token',
			account_id='dummy-account')
		
		self.client = self.session.client("setup_gcp")
		
		self.mock_ok_res   = self.load_json('../../test_lib/output/res_ok.json')
		
		self.mock_api_call = SimpleNamespace(**self.load_json('../../test_lib/api_res.json'))
		
	@staticmethod
	def load_json(path):
		with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), path)) as group_json:
			return json.load(group_json)

class GcpInitTestSetupCredentials(GcpInitTestCase):
	@patch('requests.post')
	def testSetCloudCredentials(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 
		
		mock.return_value = self.mock_api_call
		
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
		
		response = self.client.set_credentials(credentials=gcp_credentials)
		
		self.assertEqual(len(response), len(self.mock_ok_res["response"]["status"]))
		
	@patch('requests.post')
	def testValidateCredentials(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 
		
		mock.return_value = self.mock_api_call
		
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
			
		response = self.client.validate_credentials(credentials=gcp_credentials)
		
		self.assertEqual(len(response), len(self.mock_ok_res["response"]["status"]))