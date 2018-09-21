import os
import unittest
import json
from mock import patch

from spotinst_sdk import SpotinstClient


class SimpleNamespace:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        keys = sorted(self.__dict__)
        items = ("{}={!r}".format(k, self.__dict__[k]) for k in keys)
        return "{}({})".format(type(self).__name__, ", ".join(items))

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class AwsInitTestCase(unittest.TestCase):

	def setUp(self):
		self.client = SpotinstClient(
			auth_token='dummy-token',
			account_id='dummy-account')

		self.mock_group_json = self.load_json(path='test_lib/group.json')
		self.mock_emr = self.load_json('test_lib/emr.json')
		self.mock_stateful_json = self.load_json(path='test_lib/stateful/import_stateful.json')

		self.mock_group_response = self.load_json(path='test_lib/group_res.json')
		self.mock_statful_res = self.load_json(path='test_lib/stateful/import_stateful_res.json')
		self.mock_get_stateful_import_res = self.load_json(path='test_lib/stateful/get_import_res.json')
		self.mock_ok_res = self.load_json('test_lib/res_ok.json')
		self.mock_get_instances_res = self.load_json('test_lib/stateful/get_instances_res.json')
		self.mock_get_group_activity_res = self.load_json('test_lib/get_group_activity_res.json')
		self.mock_get_deployment_status_res = self.load_json('test_lib/get_deployment_status_res.json')

		self.mock_api_call =  SimpleNamespace(**self.load_json('test_lib/api_res.json'))


	@staticmethod
	def load_json(path):
		with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), path)) as group_json:
			return json.load(group_json)

	def decode_elastigroup(self, code):
		return json.dumps(self.mock_group_response)

	def decode_import(self, code):
		return json.dumps(self.mock_statful_res)

	def decode_get_import(self, code):
		return json.dumps(self.mock_get_stateful_import_res)

	def decoce_ok_res(self, code):
		return json.dumps(self.mock_ok_res)

	def decode_get_stateful(self,code):
		return json.dumps(self.mock_get_instances_res)

	def decode_get_group_activity(self,code):
		return json.dumps(self.mock_get_group_activity_res)

	def decode_get_deployment_status(self,code):
		return json.dumps(self.mock_get_deployment_status_res)


# Elastigroup Tests
class AwsInitTestElastigroup(AwsInitTestCase):

	@patch('requests.post')
	def testCreateElastigroup(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = self.decode_elastigroup

		mock.return_value = self.mock_api_call

		response = self.client.create_elastigroup(group=self.mock_group_json)

		self.assertEqual(len(response), len(self.mock_group_response["response"]["items"][0]))

	@patch('requests.get')
	def testGetElastigroupActivity(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = self.decode_get_group_activity

		mock.return_value = self.mock_api_call

		response = self.client.get_elastigroup_activity(group_id="sig-123456", start_date="11/05/1993")

		self.assertEqual(len(response), len(self.mock_get_group_activity_res["response"]["items"]))

	@patch('requests.get')
	def testGetDeploymentStatus(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = self.decode_get_deployment_status

		mock.return_value = self.mock_api_call

		response = self.client.get_deployment_status(group_id="sig-123456")

		self.assertEqual(len(response), len(self.mock_get_deployment_status_res["response"]["items"]))




# Stateful Tests
class AwsInitTestStateFul(AwsInitTestCase):

	@patch('requests.post')
	def testImportStatefulInstance(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = self.decode_import

		mock.return_value = self.mock_api_call

		response = self.client.import_stateful_instance(stateful_instance=self.mock_stateful_json)

		self.assertEqual(len(response), len(self.mock_statful_res["response"]["items"][0]))

	@patch('requests.get')
	def testGetStatefulImportStatus(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = self.decode_get_import

		mock.return_value = self.mock_api_call

		response = self.client.get_stateful_import_status(stateful_migration_id="smg-ed45f757")

		self.assertEqual(len(response), len(self.mock_get_stateful_import_res["response"]["items"]))

	@patch('requests.put')
	def testDeallocateStatefulInstance(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = self.decoce_ok_res

		mock.return_value = self.mock_api_call

		response = self.client.deallocate_stateful_instance(group_id="sig-1234567", stateful_instance_id="sid-1234567")

		self.assertEqual(len(response), len(self.mock_ok_res["response"]))

	@patch('requests.put')
	def testRecycleStatefulInstance(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = self.decoce_ok_res

		mock.return_value = self.mock_api_call

		response = self.client.recycle_stateful_instance(group_id="sig-1234567", stateful_instance_id="sid-1234567")

		self.assertEqual(len(response), len(self.mock_ok_res["response"]))

	@patch('requests.get')
	def testGetStatefulInstances(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = self.decode_get_stateful

		mock.return_value = self.mock_api_call

		response = self.client.get_stateful_instances(group_id="sig-1234567")

		self.assertEqual(len(response), len(self.mock_get_instances_res["response"]["items"]))

	@patch('requests.put')
	def testResumeStatefulInstance(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = self.decoce_ok_res

		mock.return_value = self.mock_api_call

		response = self.client.pause_stateful_instance(group_id="sig-1234567", stateful_instance_id="sid-1234567")

		self.assertEqual(len(response), len(self.mock_ok_res["response"]))

	@patch('requests.put')
	def testPauseStatefulInstance(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = self.decoce_ok_res

		mock.return_value = self.mock_api_call

		response = self.client.resume_stateful_instance(group_id="sig-1234567", stateful_instance_id="sid-1234567")

		self.assertEqual(len(response), len(self.mock_ok_res["response"]))








