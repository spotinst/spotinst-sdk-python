import unittest

from spotinst_sdk2 import SpotinstSession

class SpotinstSessionTestCase(unittest.TestCase):

    def setUp(self):
        self.session = SpotinstSession(
            auth_token='dummy-token',
            account_id='act-1234567')

        self.client = self.session.client("elastigroup_aws")



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

# endregion
