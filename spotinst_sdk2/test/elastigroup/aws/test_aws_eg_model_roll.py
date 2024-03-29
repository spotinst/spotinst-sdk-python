import os
import unittest

from spotinst_sdk2 import SpotinstSession
from spotinst_sdk2.models.elastigroup.aws import *

class AwsElastigroupRollTestCase(unittest.TestCase):

    def setUp(self):
        self.session = SpotinstSession(
            auth_token='dummy-token',
            account_id='dummy-account')

        self.client = self.session.client("elastigroup_aws")

        self.mock_group_roll_json = self.load_group_roll_json()

    def create_formatted_group_roll_request(self, group_roll):
        group_roll_request = ElastigroupRollRequest(group_roll=group_roll)
        excluded_group_roll_dict = self.client.exclude_missing(
            json.loads(group_roll_request.toJSON()))
        formatted_group_roll_dict = self.client.convert_json(
            excluded_group_roll_dict, self.client.underscore_to_camel)
        return formatted_group_roll_dict

    @staticmethod
    def load_group_roll_json():
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../test_lib/input/elastigroup/aws_group_roll.json')) as group_roll_json:
            return json.load(group_roll_json)


# region Roll
class AwsElastigroupRollTest(AwsElastigroupRollTestCase):
    def runTest(self):
        on_failure = OnFailure(action_type="DETACH_OLD", should_handle_all_batches=True, batch_num=2, draining_timeout=300, should_decrement_target_capacity=False)
        strategy = RollStrategy(action="REPLACE_SERVER", should_drain_instances=True, batch_min_healthy_percentage=100, on_failure=on_failure)
        roll = Roll(grace_period=500, batch_size_percentage="20", health_check_type="NONE", strategy=strategy)

        formatted_group_roll_dict = self.create_formatted_group_roll_request(roll)

        self.assertDictEqual(formatted_group_roll_dict, self.mock_group_roll_json)
# endregion