import os
import unittest
import json
from mock import patch

from spotinst_sdk import SpotinstSession

class SimpleNamespace:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

class AwsInitTestCase(unittest.TestCase):

	def setUp(self):
		self.session = SpotinstSession(
			auth_token='dummy-token',
			account_id='dummy-account')

		self.client = self.session.client("mrScaler_aws")
		self.mock_ok_res   = self.load_json('../test_lib/output/res_ok.json')
		self.mock_api_call = SimpleNamespace(**self.load_json('../test_lib/api_res.json'))


	@staticmethod
	def load_json(path):
		with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), path)) as group_json:
			return json.load(group_json)


# Testing EMR
class AWSInitTestEMR(AwsInitTestCase):
	@patch('requests.post')
	def testCreateEMR(self, mock):
		mock_create_emr_res = self.load_json("../test_lib/output/emr/create_emr_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_create_emr_res) 

		mock.return_value = self.mock_api_call

		response = self.client.create_emr(emr={})

		self.assertEqual(len(response), len(mock_create_emr_res["response"]["items"][0]))

	@patch('requests.put')
	def testUpdateEMR(self, mock):
		mock_update_emr_res = self.load_json("../test_lib/output/emr/create_emr_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_update_emr_res) 

		mock.return_value = self.mock_api_call

		response = self.client.update_emr(emr_id="sigi-123456", emr={})

		self.assertEqual(len(response), len(mock_update_emr_res["response"]["items"][0]))

	@patch('requests.get')
	def testGetAllEMR(self, mock):
		mock_get_all_emr_res = self.load_json("../test_lib/output/emr/get_all_emr_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_all_emr_res) 

		mock.return_value = self.mock_api_call

		response = self.client.get_all_emr()

		self.assertEqual(len(response), len(mock_get_all_emr_res["response"]["items"]))

	@patch('requests.get')
	def testGetEMR(self, mock):
		mock_get_emr_res = self.load_json("../test_lib/output/emr/get_emr_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_emr_res) 

		mock.return_value = self.mock_api_call

		response = self.client.get_emr(emr_id="sigi-123456")

		self.assertEqual(len(response), len(mock_get_emr_res["response"]["items"][0]))

	@patch('requests.get')
	def testGetEMRInstances(self, mock):
		mock_get_emr_instances_res = self.load_json("../test_lib/output/emr/get_emr_instances_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_emr_instances_res) 

		mock.return_value = self.mock_api_call

		response = self.client.get_emr_instances(emr_id="sigi-123456")

		self.assertEqual(len(response), len(mock_get_emr_instances_res["response"]["items"]))

	@patch('requests.get')
	def testGetEMRCluster(self, mock):
		mock_get_emr_cluster_res = self.load_json("../test_lib/output/emr/get_emr_cluster_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_emr_cluster_res) 

		mock.return_value = self.mock_api_call

		response = self.client.get_emr_cluster(emr_id="sigi-123456")

		self.assertEqual(len(response), len(mock_get_emr_cluster_res["response"]["items"][0]))

	@patch('requests.get')
	def testGetEMRCost(self, mock):
		mock_get_emr_cost_res = self.load_json("../test_lib/output/emr/get_emr_cost_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_emr_cost_res) 

		mock.return_value = self.mock_api_call

		response = self.client.get_emr_cost(emr_id="sigi-123456")

		self.assertEqual(len(response), len(mock_get_emr_cost_res["response"]["items"][0]))

	@patch('requests.delete')
	def testDeleteEMR(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps() 

		mock.return_value = self.mock_api_call

		response = self.client.delete_emr(emr_id="sigi-123456")

		self.assertEqual(response, True)

	@patch('requests.put')
	def testScaleEMRUp(self, mock):
		mock_scale_up_emr_res = self.load_json("../test_lib/output/emr/scale_up_emr_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_scale_up_emr_res) 

		mock.return_value = self.mock_api_call

		response = self.client.scale_up_emr(emr_id="sigi-123456", adjustment=1)

		self.assertEqual(len(response), len(mock_scale_up_emr_res["response"]["items"][0]))

	@patch('requests.put')
	def testScaleEMRDown(self, mock):
		mock_scale_down_emr_res = self.load_json("../test_lib/output/emr/scale_down_emr_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_scale_down_emr_res) 

		mock.return_value = self.mock_api_call

		response = self.client.scale_down_emr(emr_id="sigi-123456", adjustment=1)

		self.assertEqual(len(response), len(mock_scale_down_emr_res["response"]["items"][0]))

