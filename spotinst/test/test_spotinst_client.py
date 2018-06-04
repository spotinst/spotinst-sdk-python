import unittest

from spotinst import SpotinstClient, aws_elastigroup


class AwsElastigroupTestCase(unittest.TestCase):
    def setUp(self):
        self.client = SpotinstClient(auth_token='dummy-token', account_id='act-1234567')


class AwsElastigroupExcludeMissingTest(AwsElastigroupTestCase):
    def runTest(self):
        dummy_obj = {"valid_key": "valid_value", "null_key": None, "ignored_key": aws_elastigroup.none}
        expected_obj = {"valid_key": "valid_value", "null_key": None}
        actual_obj = self.client.exclude_missing(dummy_obj)
        self.assertDictEqual(actual_obj, expected_obj)
