import os
import unittest
import json
from mock import patch

from spotinst_sdk2 import SpotinstSession

class SimpleNamespace:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

class NotificationCenterTestCase(unittest.TestCase):
    def setUp(self):
        self.session = SpotinstSession(
            auth_token="dummy-token",
            account_id="dummy-account"
        )
        self.client = self.session.client("notification_center")
        self.mock_ok_res = self.load_json("../test_lib/output/res_ok.json")
        self.mock_api_call = SimpleNamespace(**self.load_json("../test_lib/api_res.json"))

    @staticmethod
    def load_json(path):
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), path)) as json_file:
            return json.load(json_file)

# Test Notification Center Methods
class TestNotificationCenterClient(NotificationCenterTestCase):
    @patch("requests.get")
    def test_get_account_resources(self, mock):
        mock_get_account_resources_res = self.load_json("../test_lib/output/notification_center/get_resources_res.json")

        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_account_resources_res)

        mock.return_value = self.mock_api_call

        response = self.client.get_account_resources(account_id="act-b116740d")

        self.assertEqual(len(response), len(mock_get_account_resources_res["response"]["items"]))

    @patch("requests.get")
    def test_get_aggregated_events(self, mock):
        mock_get_aggregated_events_res = self.load_json("../test_lib/output/notification_center/get_aggregated_events_res.json")

        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_aggregated_events_res)

        mock.return_value = self.mock_api_call

        response = self.client.get_aggregated_events(account_id="act-b116740d")

        self.assertEqual(len(response), len(mock_get_aggregated_events_res["response"]["items"]))

    @patch("requests.get")
    def test_get_all_notification_policies(self, mock):
        mock_get_all_notification_policies_res = self.load_json("../test_lib/output/notification_center/get_all_notification_policies_res.json")

        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_all_notification_policies_res)

        mock.return_value = self.mock_api_call

        response = self.client.get_all_notification_policies()

        self.assertEqual(len(response), len(mock_get_all_notification_policies_res["response"]["items"]))