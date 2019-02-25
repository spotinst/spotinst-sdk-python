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

		self.client = self.session.client("subscription")
		self.mock_ok_res   = self.load_json('../test_lib/output/res_ok.json')
		self.mock_api_call = SimpleNamespace(**self.load_json('../test_lib/api_res.json'))


	@staticmethod
	def load_json(path):
		with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), path)) as group_json:
			return json.load(group_json)


# Subscription Tests
class AwsInitTestSubscription(AwsInitTestCase):

	@patch('requests.post')
	def testCreateSubscription(self, mock):
		mock_subscription_response = self.load_json('../test_lib/output/event/subscription_res.json')
		mock_subscription_json = self.load_json('../test_lib/input/event/subscription.json')

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_subscription_response)

		mock.return_value = self.mock_api_call

		response = self.client.create_event_subscription(subscription=mock_subscription_json)

		self.assertEqual(len(response), len(mock_subscription_response["response"]["items"][0]))

	@patch('requests.put')
	def testUpdateSubscription(self, mock):
		mock_subscription_response = self.load_json('../test_lib/output/event/subscription_res.json')
		mock_subscription_json = self.load_json('../test_lib/input/event/subscription.json')

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_subscription_response)

		mock.return_value = self.mock_api_call

		response = self.client.update_event_subscription(subscription=mock_subscription_json, subscription_id="sis-123456")

		self.assertEqual(len(response), len(mock_subscription_response["response"]))

	@patch('requests.get')
	def testGetAllSubscription(self, mock):
		mock_get_subscription_res    = self.load_json('../test_lib/output/event/get_subscription_res.json')

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_subscription_res)

		mock.return_value = self.mock_api_call

		response = self.client.get_all_event_subscription()

		self.assertEqual(len(response), len(mock_get_subscription_res["response"]["items"]))

	@patch('requests.get')
	def testGetSubscription(self, mock):
		mock_get_subscription_res    = self.load_json('../test_lib/output/event/get_subscription_res.json')

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_subscription_res)

		mock.return_value = self.mock_api_call

		response = self.client.get_event_subscription(subscription_id="sis-123456")

		self.assertEqual(len(response), len(mock_get_subscription_res["response"]["items"][0]))

	@patch('requests.delete')
	def testDeleteSubscription(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 

		mock.return_value = self.mock_api_call

		response = self.client.delete_event_subscription(subscription_id="sis-12345")

		self.assertEqual(response, True)

