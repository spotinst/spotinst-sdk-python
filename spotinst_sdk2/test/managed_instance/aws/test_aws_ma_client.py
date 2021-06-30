import os
import unittest
import json
from mock import patch

from spotinst_sdk2 import SpotinstSession
from spotinst_sdk2.models.managed_instance.aws import *


class SimpleNamespace:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class ManagedInstanceInitTestCase(unittest.TestCase):

    def setUp(self):
        self.session = SpotinstSession(
            auth_token='dummy-token',
            account_id='dummy-account')

        self.client = self.session.client("managed_instance_aws")
        self.mock_ok_res = self.load_json('../../test_lib/output/res_ok.json')
        self.mock_api_call = SimpleNamespace(**self.load_json('../../test_lib/api_res.json'))

    @staticmethod
    def load_json(path):
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), path)) as ma_json:
            return json.load(ma_json)


# Managed Instance Tests
class TestAwsManagedInstanceInit(ManagedInstanceInitTestCase):

    @patch('requests.post')
    def test_create_managed_instance(self, mock):
        mock_ma_request = self.load_json('../../test_lib/output/managed_instance/aws_managed_instance.json')
        mock_ma_json = self.load_json('../../test_lib/input/managed_instance/aws_managed_instance.json')

        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(mock_ma_request)

        mock.return_value = self.mock_api_call

        response = self.client.create_managed_instance(managed_instance=mock_ma_json)

        self.assertEqual(len(response), len(mock_ma_request["response"]["items"][0]))

    @patch('requests.put')
    def test_update_managed_instance(self, mock):
        mock_ma_request = self.load_json('../../test_lib/output/managed_instance/aws_managed_instance.json')
        mock_ma_json = self.load_json('../../test_lib/input/managed_instance/aws_managed_instance.json')

        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(mock_ma_request)

        mock.return_value = self.mock_api_call

        response = self.client.update_managed_instance(managed_instance_id="mi-12312",
                                                       managed_instance_update=mock_ma_json)

        self.assertEqual(len(response), len(mock_ma_request["response"]["items"][0]))

    @patch('requests.get')
    def test_get_managed_instance(self, mock):
        mock_get_ma_res = self.load_json('../../test_lib/output/managed_instance/get_managed_instance_res.json')

        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_ma_res)

        mock.return_value = self.mock_api_call

        response = self.client.get_managed_instance(managed_instance_id="mi-123456")

        self.assertEqual(len(response), len(mock_get_ma_res["response"]["items"][0]))

    @patch('requests.get')
    def test_get_managed_instances(self, mock):
        mock_get_ma_res = self.load_json('../../test_lib/output/managed_instance/get_managed_instance_res.json')

        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_ma_res)

        mock.return_value = self.mock_api_call

        response = self.client.get_managed_instances()

        self.assertEqual(len(response), len(mock_get_ma_res["response"]["items"]))

    @patch('requests.delete')
    def test_delete_managed_instances(self, mock):
        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res)

        mock.return_value = self.mock_api_call

        response = self.client.delete_managed_instance(managed_instance_id="mi-12345")

        self.assertEqual(response, True)

    @patch('requests.put')
    def test_pause_managed_instances(self, mock):
        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res)

        mock.return_value = self.mock_api_call

        response = self.client.pause_managed_instance(managed_instance_id="mi-1234567")
        self.assertEqual(len(response), len(self.mock_ok_res["response"]["status"]))

    @patch('requests.put')
    def test_resume_managed_instances(self, mock):
        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res)

        mock.return_value = self.mock_api_call

        response = self.client.resume_managed_instance(managed_instance_id="mi-1234567")
        self.assertEqual(len(response), len(self.mock_ok_res["response"]["status"]))

    @patch('requests.put')
    def test_recycle_managed_instances(self, mock):
        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res)

        mock.return_value = self.mock_api_call

        response = self.client.recycle_managed_instance(managed_instance_id="mi-1234567")
        self.assertEqual(len(response), len(self.mock_ok_res["response"]["status"]))