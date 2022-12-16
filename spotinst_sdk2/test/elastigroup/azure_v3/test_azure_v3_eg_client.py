import os
import unittest
import json
from mock import patch

from spotinst_sdk2 import SpotinstSession
from spotinst_sdk2.models.elastigroup.azure_v3 import *


class SimpleNamespace:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class AzureV3InitTestCase(unittest.TestCase):

    def setUp(self):
        self.session = SpotinstSession(
            auth_token='dummy-token',
            account_id='dummy-account')

        self.client = self.session.client("elastigroup_azure_v3")

        self.mock_ok_res = self.load_json('../../test_lib/output/res_ok.json')

        self.mock_api_call = SimpleNamespace(**self.load_json('../../test_lib/api_res.json'))

    @staticmethod
    def load_json(path):
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), path)) as group_json:
            return json.load(group_json)


# Elastigroup Tests
class AzureV3InitTestElastigroup(AzureV3InitTestCase):

    @patch('requests.post')
    def testCreateElastigroup(self, mock):
        mock_group_response = self.load_json('../../test_lib/output/elastigroup/group_res.json')
        mock_group_json = self.load_json('../../test_lib/input/elastigroup/azure_v3_group.json')

        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(mock_group_response)

        mock.return_value = self.mock_api_call

        response = self.client.create_elastigroup(group=mock_group_json)

        self.assertEqual(len(response), len(mock_group_response["response"]["items"][0]))

    @patch('requests.put')
    def testUpdateElastigroup(self, mock):
        mock_group_response = self.load_json('../../test_lib/output/elastigroup/group_res.json')
        mock_group_json = self.load_json('../../test_lib/input/elastigroup/azure_v3_group.json')

        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(mock_group_response)

        mock.return_value = self.mock_api_call

        response = self.client.update_elastigroup(group_update=mock_group_json, group_id="sig-123456")

        self.assertEqual(len(response), len(mock_group_response["response"]["items"][0]))

    @patch('requests.delete')
    def testDeleteElastigroup(self, mock):
        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res)

        mock.return_value = self.mock_api_call

        response = self.client.delete_elastigroup(group_id="sig-12345")

        self.assertEqual(response, True)

    @patch('requests.get')
    def testGetElastigroup(self, mock):
        mock_get_group_res = self.load_json('../../test_lib/output/elastigroup/get_group_res.json')

        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_group_res)

        mock.return_value = self.mock_api_call

        response = self.client.get_elastigroup(group_id="sig-123456")

        self.assertEqual(len(response), len(mock_get_group_res["response"]["items"][0]))

    @patch('requests.get')
    def testGetElastigroups(self, mock):
        mock_get_group_res = self.load_json('../../test_lib/output/elastigroup/get_group_res.json')

        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_group_res)

        mock.return_value = self.mock_api_call

        response = self.client.get_elastigroups()

        self.assertEqual(len(response), len(mock_get_group_res["response"]["items"]))

    @patch('requests.put')
    def testScaleGroupUp(self, mock):
        mock_group_scale_response = self.load_json('../../test_lib/output/elastigroup/group_scale_res.json')

        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(mock_group_scale_response)

        mock.return_value = self.mock_api_call

        response = self.client.scale_elastigroup_up(group_id="sig-123456", adjustment=1)

        self.assertEqual(len(response), len(mock_group_scale_response["response"]["items"]))

    @patch('requests.put')
    def testScaleGroupDown(self, mock):
        mock_group_scale_response = self.load_json('../../test_lib/output/elastigroup/group_scale_res.json')

        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(mock_group_scale_response)

        mock.return_value = self.mock_api_call

        response = self.client.scale_elastigroup_down(group_id="sig-123456", adjustment=1)

        self.assertEqual(len(response), len(mock_group_scale_response["response"]["items"]))
