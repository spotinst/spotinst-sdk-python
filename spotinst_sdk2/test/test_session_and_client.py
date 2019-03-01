import unittest
import os
import json
import yaml
from mock import patch, mock_open

from spotinst_sdk2 import SpotinstSession
from spotinst_sdk2.client import SpotinstClientException

class SimpleNamespace:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

class SpotinstSessionTestCase(unittest.TestCase):
    def setUp(self):
        with patch("spotinst_sdk2.session.open", mock_open(read_data=yaml.dump(dict()))):
            try:
                SpotinstSession()
            except SpotinstClientException as e:
                pass
        
        self.session = SpotinstSession(
            auth_token='dummy-token',
            account_id='act-1234567')

        self.client = self.session.client("elastigroup_aws")

        self.mock_fail_res   = self.load_json('./test_lib/output/res_fail.json')
        self.mock_api_call = SimpleNamespace(**self.load_json('./test_lib/api_fail_res.json'))

    @staticmethod
    def load_json(path):
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), path)) as group_json:
            return json.load(group_json)  


# region Internal Methods
class SpotinstClientExcludeMissingTest(SpotinstSessionTestCase):
    def runTest(self):
        dummy_obj = {
            "valid_key": "valid_value",
            "null_key": None,
            "ignored_key": None}
        expected_obj = {'valid_key': 'valid_value', 'null_key': None, 'ignored_key': None}
        actual_obj = self.client.exclude_missing(dummy_obj)
        self.assertDictEqual(actual_obj, expected_obj)


class SpotinstClientConvertJsonToCamelCaseTest(SpotinstSessionTestCase):
    def runTest(self):
        test_obj = {
            'group': {
                'compute': {
                    'preferred_availability_zones': [
                        'a',
                        'b',
                        'c']}}}
        actual_obj = self.client.convert_json(
            test_obj, self.client.underscore_to_camel)
        expected_obj = {
            'group': {
                'compute': {
                    'preferredAvailabilityZones': [
                        'a',
                        'b',
                        'c']}}}
        self.assertDictEqual(actual_obj, expected_obj)

class SpotinstClientExpectedErrors(SpotinstSessionTestCase):
    @patch('requests.get')
    def testFailSendGet(self, mock):
        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_fail_res)

        mock.return_value = self.mock_api_call
        try:
            response = self.client.send_get(url="test", entity_name="test")
        except SpotinstClientException as e:
            pass

    @patch('requests.delete')
    def testFailSendDelete(self, mock):
        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_fail_res)

        mock.return_value = self.mock_api_call
        try:
            response = self.client.send_delete(url="test", entity_name="test")
        except SpotinstClientException as e:
            pass

    @patch('requests.delete')
    def testFailSendDeleteWithBody(self, mock):
        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_fail_res)

        mock.return_value = self.mock_api_call
        try:
            response = self.client.send_delete_with_body(url="test", entity_name="test", body="test")
        except SpotinstClientException as e:
            pass

    @patch('requests.post')
    def testFailSendPost(self, mock):
        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_fail_res)

        mock.return_value = self.mock_api_call
        try:
            response = self.client.send_post(url="test", entity_name="test")
        except SpotinstClientException as e:
            pass

    @patch('requests.put')
    def testFailSendPut(self, mock):
        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_fail_res)

        mock.return_value = self.mock_api_call
        try:
            response = self.client.send_put(url="test", entity_name="test")
        except SpotinstClientException as e:
            pass

    @patch('requests.put')
    def testFailSendPutWithParams(self, mock):
        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_fail_res)

        mock.return_value = self.mock_api_call
        try:
            response = self.client.send_put_with_params(url="test", entity_name="test", body="test", user_query_params=dict(test="test"))
        except SpotinstClientException as e:
            pass


# endregion
