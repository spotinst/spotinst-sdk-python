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

		self.client = self.session.client("mcs")
		self.mock_ok_res   = self.load_json('../test_lib/output/res_ok.json')
		self.mock_api_call = SimpleNamespace(**self.load_json('../test_lib/api_res.json'))

	@staticmethod
	def load_json(path):
		with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), path)) as group_json:
			return json.load(group_json)


# Kubernetes
class AwsInitTestMcs(AwsInitTestCase):
	@patch('requests.get')
	def testGetKubernetesClusterCost(self, mock):
		mock_kubernetes_cost_res = self.load_json('../test_lib/output/elastigroup/kubernetes_cost_res.json')

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_kubernetes_cost_res) 

		mock.return_value = self.mock_api_call

		response = self.client.get_kubernetes_cluster_cost(custer_id="jeffrey.spotinstdemo.com", from_date="2016-01-01", to_date="2018-10-12")

		self.assertEqual(len(response), len(mock_kubernetes_cost_res["response"]["items"][0]))


