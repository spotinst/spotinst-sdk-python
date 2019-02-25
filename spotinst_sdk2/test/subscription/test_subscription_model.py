import os
import unittest

from spotinst_sdk2 import SpotinstSession
from spotinst_sdk2.models.subscription import *

class SpotinstSubscriptionTestCase(unittest.TestCase):

    def setUp(self):
        self.session = SpotinstSession(
            auth_token='dummy-token',
            account_id='act-1234567')

        self.mock_event_subscription_json = self.load_json(path='../test_lib/input/event/subscription.json')
        self.client = self.session.client("subscription")

    def create_formatted_event_subscription_request(self, subscription):
        subscription_request = SubscriptionRequest(subscription)

        excluded_subscription_dict = self.client.exclude_missing(
            json.loads(subscription_request.toJSON()))

        formatted_subscription_dict = self.client.convert_json(
            excluded_subscription_dict, self.client.underscore_to_camel)

        return formatted_subscription_dict

    @staticmethod
    def load_json(path):
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), path)) as subscription_json:
            return json.load(subscription_json)

class SpotinstEventSubscriptionCreate(SpotinstSubscriptionTestCase):
	def runTest(self):
		subscription = Subscription(
			resource_id="sig-885c4f64",
			protocol="web",
			endpoint="https://webhook.com",
			event_type="GROUP_UPDATED",
			event_format=" { \"subject\" : \"%s\", \"message\" : \"%s\" }"
		)

		formatted_subscription = self.create_formatted_event_subscription_request(subscription)
		expected_subscription = self.mock_event_subscription_json

		self.assertDictEqual(formatted_subscription, expected_subscription)
