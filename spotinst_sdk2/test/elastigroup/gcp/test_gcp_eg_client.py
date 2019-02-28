import os
import unittest
import json
from mock import patch

from spotinst_sdk2 import SpotinstSession
from spotinst_sdk2.models.elastigroup.gcp import *

class SimpleNamespace:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

class GcpInitTestCase(unittest.TestCase):

	def setUp(self):
		self.session = SpotinstSession(
			auth_token='dummy-token',
			account_id='dummy-account')

		self.client = self.session.client("elastigroup_gcp")

		self.mock_ok_res   = self.load_json('../../test_lib/output/res_ok.json')

		self.mock_api_call = SimpleNamespace(**self.load_json('../../test_lib/api_res.json'))


	@staticmethod
	def load_json(path):
		with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), path)) as group_json:
			return json.load(group_json)



# Elastigroup Tests
class GCPInitTestElastigroup(GcpInitTestCase):

	@patch('requests.post')
	def testCreateElastigroup(self, mock):
		mock_group_response = self.load_json('../../test_lib/output/elastigroup/group_res.json')
		mock_group_json = self.load_json('../../test_lib/input/elastigroup/gcp_group.json')

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_group_response)

		mock.return_value = self.mock_api_call

		response = self.client.create_elastigroup(group=mock_group_json)

		self.assertEqual(len(response), len(mock_group_response["response"]["items"][0]))

	@patch('requests.put')
	def testUpdateElastigroup(self, mock):
		mock_group_response = self.load_json('../../test_lib/output/elastigroup/group_res.json')
		mock_group_json = self.load_json('../../test_lib/input/elastigroup/gcp_group.json')

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
		mock_get_group_res    = self.load_json('../../test_lib/output/elastigroup/get_group_res.json')

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_group_res)

		mock.return_value = self.mock_api_call

		response = self.client.get_elastigroup(group_id="sig-123456")

		self.assertEqual(len(response), len(mock_get_group_res["response"]["items"][0]))

	@patch('requests.get')
	def testGetElastigroups(self, mock):
		mock_get_group_res    = self.load_json('../../test_lib/output/elastigroup/get_group_res.json')

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

	@patch('requests.get')
	def testGetElastigroupActiveInstances(self, mock):
		mock_get_group_active_res    = self.load_json('../../test_lib/output/elastigroup/get_group_active_res.json')

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_group_active_res)

		mock.return_value = self.mock_api_call

		response = self.client.get_elastigroup_active_instances(group_id="sig-123456")

		self.assertEqual(len(response), len(mock_get_group_active_res["response"]["items"]))

	@patch('requests.put')
	def testDetachElastigroupInstances(self, mock):	
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res)

		mock.return_value = self.mock_api_call

		response = self.client.detach_elastigroup_instances(group_id="sig-123456", detach_configuration=DetachConfiguration(
			instances_to_detach="test", 
			draining_timeout="test",
			should_decrement_target_capacity="test"))

		self.assertEqual(response, self.mock_ok_res['response']['status'])

	@patch('requests.get')
	def testGetElastigroupActivity(self, mock):
		mock_get_group_activity_res    = self.load_json('../../test_lib/output/elastigroup/get_group_activity_res.json')

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_group_activity_res)

		mock.return_value = self.mock_api_call

		response = self.client.get_elastigroup_activity(group_id="sig-123456", start_date="11/05/1993")

		self.assertEqual(len(response), len(mock_get_group_activity_res["response"]["items"]))

	@patch('requests.get')
	def testGetCostPerElastigroup(self, mock):
		mock_cost_per_group_res = self.load_json("../../test_lib/output/elastigroup/cost_per_group_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_cost_per_group_res) 

		mock.return_value = self.mock_api_call

		response = self.client.get_cost_per_elastigroup(group_id="sig-123456", to_date="2016-01-01", from_date="2018-10-15")

		self.assertEqual(len(response), len(mock_cost_per_group_res["response"]["items"]))



# Test Deployment Action
class GCPInitTestDeployment(GcpInitTestCase):
	@patch('requests.get')
	def testGetAllGroupDeployment(self, mock):
		mock_get_deployment_status_res = self.load_json('../../test_lib/output/elastigroup/get_deployment_status_res.json')

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_deployment_status_res) 

		mock.return_value = self.mock_api_call

		response = self.client.get_all_group_deployment(group_id="sig-123456")

		self.assertEqual(len(response), len(mock_get_deployment_status_res["response"]["items"]))

	@patch('requests.put')
	def testRollGroup(self, mock):
		mock_roll_group_res = self.load_json('../../test_lib/output/elastigroup/roll_group_res.json')

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_roll_group_res) 

		mock.return_value = self.mock_api_call

		response = self.client.roll_group(group_id="sig-123456", group_roll=RollGroup(batch_size_percentage=50, grace_period=150))

		self.assertEqual(len(response), len(mock_roll_group_res["response"]))

	@patch('requests.get')
	def testGetDeploymentStatus(self, mock):
		mock_roll_status_res = self.load_json('../../test_lib/output/elastigroup/roll_status_res.json')

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_roll_status_res) 

		mock.return_value = self.mock_api_call

		response = self.client.get_deployment_status(group_id="sig-12345", roll_id="sbgd-4ea64d71")

		self.assertEqual(len(response), len(mock_roll_status_res["response"]["items"]))

	@patch('requests.put')
	def testStopDeployment(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 

		mock.return_value = self.mock_api_call

		response = self.client.stop_deployment(group_id="sig-12345", roll_id="sbgd-4ea64d71")

		self.assertEqual(len(response), len(self.mock_ok_res["response"]))




# Test GKE
class GCPInitTestGKE(GcpInitTestCase):
	@patch('requests.post')
	def testImportGKE(self, mock):
		mock_import_gke_res = self.load_json("../../test_lib/output/elastigroup/import_gke_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_import_gke_res) 

		mock.return_value = self.mock_api_call

		response = self.client.import_gke(location="location", gke_id="test", gke="test")

		self.assertEqual(len(response), len(mock_import_gke_res["response"]["items"][0]))
