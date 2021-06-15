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
            
        self.client = self.session.client("setup_aws")
        
        self.mock_ok_res   = self.load_json('../../test_lib/output/res_ok.json')
        
        self.mock_api_call = SimpleNamespace(**self.load_json('../../test_lib/api_res.json'))
        
        
    @staticmethod
    def load_json(path):
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), path)) as group_json:
            return json.load(group_json)



# Test Org and Account
class AWSInitTestSetupCredentials(AwsInitTestCase):
    @patch('requests.post')
    def testSetCloudCredentials(self, mock):
        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 
        
        mock.return_value = self.mock_api_call
        
        response = self.client.set_credentials(iam_role="arn")
        
        self.assertEqual(len(response), len(self.mock_ok_res["response"]["status"]))
        
    @patch('requests.post')
    def testCreateAwsExternalId(self, mock):
        mock_create_aws_external_id_res = self.load_json("../../test_lib/output/admin/create_aws_external_id_res.json")
        
        self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
        self.mock_api_call.content.decode = lambda code: json.dumps(mock_create_aws_external_id_res) 
        
        mock.return_value = self.mock_api_call
        
        response = self.client.create_external_id()
        
        self.assertEqual(len(response), len(mock_create_aws_external_id_res["response"]["items"][0]))