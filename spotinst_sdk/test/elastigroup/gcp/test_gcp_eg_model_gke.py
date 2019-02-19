import os
import unittest

from spotinst_sdk import SpotinstSession
from spotinst_sdk.models.elastigroup.gcp.gke import *

class GcpGKETestCase(unittest.TestCase):
    def setUp(self):
        self.session = SpotinstSession(
            auth_token='dummy-token',
            account_id='dummy-account')

        self.mock_gke_json = self.load_asg_json()

        self.client = self.session.client("elastigroup_gcp")

    def create_formatted_gke_request(self, asg):
        group_request = ImportGKERequest(asg)
        excluded_group_dict = self.client.exclude_missing(
            json.loads(group_request.toJSON()))
        formatted_group_dict = self.client.convert_json(
            excluded_group_dict, self.client.underscore_to_camel)
        return formatted_group_dict

    @staticmethod
    def load_asg_json():
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../test_lib/input/elastigroup/import_gke.json')) as group_json:
            return json.load(group_json)


# region B/G Deployment
class AwsImportASGTest(GcpGKETestCase):
    def runTest(self):

        instance_types = InstanceTypes(ondemand="test", preemptible=["test"])

        capacity = Capacity(minimum=0, maximum=0, target=0)

        gke = GKE(
            preemptible_percentage=0,
            capacity=capacity,
            instance_types=instance_types,
            availability_zones=["test"],
            node_image="test")

        formatted_asg_dict = self.create_formatted_gke_request(gke)

        formatted = formatted_asg_dict
        expected = self.mock_gke_json

        self.assertDictEqual(formatted, expected)



