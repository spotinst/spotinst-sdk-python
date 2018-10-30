import unittest

from spotinst_sdk import SpotinstClient
from spotinst_sdk.aws_elastigroup import *


class SpotinstClientTestCase(unittest.TestCase):

    def setUp(self):
        self.client = SpotinstClient(
            auth_token='dummy-token',
            account_id='act-1234567')


# region Internal Methods
class SpotinstClientExcludeMissingTest(SpotinstClientTestCase):
    def runTest(self):
        dummy_obj = {
            "valid_key": "valid_value",
            "null_key": None,
            "ignored_key": none}
        expected_obj = {"valid_key": "valid_value", "null_key": None}
        actual_obj = self.client.exclude_missing(dummy_obj)
        self.assertDictEqual(actual_obj, expected_obj)


class SpotinstClientConvertJsonToCamelCaseTest(SpotinstClientTestCase):
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

# endregion
