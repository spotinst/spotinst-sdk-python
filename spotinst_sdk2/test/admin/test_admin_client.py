import os
import unittest
import json
from mock import patch

from spotinst_sdk2 import SpotinstSession

class SimpleNamespace:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

class AwsInitTestCase(unittest.TestCase):

	def setUp(self):
		self.session = SpotinstSession(
			auth_token='dummy-token',
			account_id='dummy-account')

		self.client = self.session.client("admin")

		self.mock_ok_res   = self.load_json('../test_lib/output/res_ok.json')

		self.mock_api_call = SimpleNamespace(**self.load_json('../test_lib/api_res.json'))


	@staticmethod
	def load_json(path):
		with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), path)) as group_json:
			return json.load(group_json)



# Test Org and Account
class AWSInitTestOrgAndAcct(AwsInitTestCase):
	@patch('requests.post')
	def testCreateOrganization(self, mock):
		mock_create_org_res = self.load_json("../test_lib/output/admin/create_org_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_create_org_res) 

		mock.return_value = self.mock_api_call

		response = self.client.create_organization(org_name="test")

		self.assertEqual(len(response), len(mock_create_org_res["response"]["items"][0]))

	@patch('requests.delete')
	def testDeleteOrganization(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 

		mock.return_value = self.mock_api_call

		response = self.client.delete_organization(org_id=123456)

		self.assertEqual(response, True)

	@patch('requests.post')
	def testSetCloudCredentials(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 

		mock.return_value = self.mock_api_call

		response = self.client.set_cloud_credentials(iam_role="arn")

		self.assertEqual(len(response), len(self.mock_ok_res["response"]["status"]))

	@patch('requests.post')
	def testCreateAwsExternalId(self, mock):
		mock_create_aws_external_id_res = self.load_json("../test_lib/output/admin/create_aws_external_id_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_create_aws_external_id_res) 

		mock.return_value = self.mock_api_call

		response = self.client.create_aws_external_id()

		self.assertEqual(len(response), len(mock_create_aws_external_id_res["response"]["items"][0]))

	@patch('requests.post')
	def testCreateAccount(self, mock):
		mock_create_account_res = self.load_json("../test_lib/output/admin/create_account_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_create_account_res) 

		mock.return_value = self.mock_api_call

		response = self.client.create_account(account_name="test")

		self.assertEqual(len(response), len(mock_create_account_res["response"]["items"][0]))


	@patch('requests.get')
	def testGetAccounts(self, mock):
		mock_get_accounts_res = self.load_json("../test_lib/output/admin/get_accounts_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_accounts_res) 

		mock.return_value = self.mock_api_call

		response = self.client.get_accounts()

		self.assertEqual(len(response), len(mock_get_accounts_res["response"]["items"]))

	@patch('requests.delete')
	def testDeleteAccount(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 

		mock.return_value = self.mock_api_call

		response = self.client.delete_account(account_name="test")

		self.assertEqual(response, True)

	@patch('requests.post')
	def testCreateUser(self, mock):
		mock_create_user_res = self.load_json("../test_lib/output/admin/create_user_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_create_user_res) 

		mock.return_value = self.mock_api_call

		response = self.client.create_user(first_name="jane", last_name="doe", email="jd@mail.com", password="12345", role="test")

		self.assertEqual(len(response), len(mock_create_user_res["response"]["items"][0]))

	@patch('requests.post')
	def testAddExsistingUser(self, mock): 
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 

		mock.return_value = self.mock_api_call

		response = self.client.add_exsisting_user(user_email="test", role="test")

		self.assertEqual(len(response), len(self.mock_ok_res["response"]["status"]))

	@patch('requests.put')
	def testUpdateUserRole(self, mock): 
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 

		mock.return_value = self.mock_api_call

		response = self.client.update_user_role(user_email="test", role="test")

		self.assertEqual(len(response), len(self.mock_ok_res["response"]["status"]))

	@patch('requests.delete')
	def testDetachUser(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps() 

		mock.return_value = self.mock_api_call

		response = self.client.detach_user(user_email="test")

		self.assertEqual(response, True)

	@patch('requests.get')
	def testGetUser(self, mock):
		mock_get_user_res = self.load_json("../test_lib/output/admin/get_user_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_user_res) 

		mock.return_value = self.mock_api_call

		response = self.client.get_user(user_email="test")

		self.assertEqual(len(response), len(mock_get_user_res["response"]["items"]))

	@patch('requests.post')
	def testAssignUserToAccounts(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 

		mock.return_value = self.mock_api_call

		response = self.client.assign_user_to_account(mappings=[])

		self.assertEqual(len(response), len(self.mock_ok_res["response"]["status"]))


