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

		self.client = self.session.client("ocean_aws")
		self.mock_ok_res   = self.load_json('../test_lib/output/res_ok.json')
		self.mock_api_call = SimpleNamespace(**self.load_json('../test_lib/api_res.json'))


	@staticmethod
	def load_json(path):
		with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), path)) as group_json:
			return json.load(group_json)


# Ocean Tests
class AwsInitTestOcean(AwsInitTestCase):

	@patch('requests.post')
	def testCreateOcean(self, mock):
		mock_cluster_response = self.load_json('../test_lib/output/ocean/ocean_cluster_res.json')
		mock_cluster_json = self.load_json('../test_lib/input/ocean/ocean_cluster.json')

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_cluster_response)

		mock.return_value = self.mock_api_call

		response = self.client.create_ocean_cluster(ocean=mock_cluster_json)

		self.assertEqual(len(response), len(mock_cluster_response["response"]["items"][0]))

	@patch('requests.put')
	def testUpdateOcean(self, mock):
		mock_cluster_response = self.load_json('../test_lib/output/ocean/ocean_cluster_res.json')
		mock_cluster_json = self.load_json('../test_lib/input/ocean/ocean_cluster.json')

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_cluster_response)

		mock.return_value = self.mock_api_call

		response = self.client.update_ocean_cluster(ocean=mock_cluster_json, ocean_id="o-123456")

		self.assertEqual(len(response), len(mock_cluster_response["response"]["items"][0]))

	@patch('requests.get')
	def testGetAllOcean(self, mock):
		mock_get_ocean_clusters_res    = self.load_json('../test_lib/output/ocean/get_ocean_clusters_res.json')

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_ocean_clusters_res)

		mock.return_value = self.mock_api_call

		response = self.client.get_all_ocean_cluster()

		self.assertEqual(len(response), len(mock_get_ocean_clusters_res["response"]["items"]))

	@patch('requests.get')
	def testGetOcean(self, mock):
		mock_get_ocean_clusters_res    = self.load_json('../test_lib/output/ocean/get_ocean_clusters_res.json')

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_ocean_clusters_res)

		mock.return_value = self.mock_api_call

		response = self.client.get_ocean_cluster(ocean_id="o-123456")

		self.assertEqual(len(response), len(mock_get_ocean_clusters_res["response"]["items"][0]))

	@patch('requests.delete')
	def testDeleteOcean(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 

		mock.return_value = self.mock_api_call

		response = self.client.delete_ocean_cluster(ocean_id="o-12345")

		self.assertEqual(response, True)


