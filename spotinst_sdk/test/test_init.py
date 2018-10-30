import os
import unittest
import json
from mock import patch

from spotinst_sdk import SpotinstClient
from spotinst_sdk.aws_elastigroup import *


class SimpleNamespace:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        keys = sorted(self.__dict__)
        items = ("{}={!r}".format(k, self.__dict__[k]) for k in keys)
        return "{}({})".format(type(self).__name__, ", ".join(items))

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class AwsInitTestCase(unittest.TestCase):

	def setUp(self):
		self.client = SpotinstClient(
			auth_token='dummy-token',
			account_id='dummy-account')

		self.mock_ok_res   = self.load_json('test_lib/output/res_ok.json')

		self.mock_api_call = SimpleNamespace(**self.load_json('test_lib/api_res.json'))


	@staticmethod
	def load_json(path):
		with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), path)) as group_json:
			return json.load(group_json)






# Elastigroup Tests
class AwsInitTestElastigroup(AwsInitTestCase):

	@patch('requests.post')
	def testCreateElastigroup(self, mock):
		mock_group_response = self.load_json('test_lib/output/group_res.json')
		mock_group_json = self.load_json('test_lib/input/group.json')

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_group_response)

		mock.return_value = self.mock_api_call

		response = self.client.create_elastigroup(group=mock_group_json)

		self.assertEqual(len(response), len(mock_group_response["response"]["items"][0]))

	@patch('requests.put')
	def testUpdateElastigroup(self, mock):
		mock_group_response = self.load_json('test_lib/output/group_res.json')
		mock_group_json = self.load_json('test_lib/input/group.json')

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_group_response)

		mock.return_value = self.mock_api_call

		response = self.client.update_elastigroup(group_update=mock_group_json, group_id="sig-123456")

		self.assertEqual(len(response), len(mock_group_response["response"]["items"][0]))

	@patch('requests.get')
	def testGetElastigroupActivity(self, mock):
		mock_get_group_activity_res    = self.load_json('test_lib/output/get_group_activity_res.json')

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_group_activity_res)

		mock.return_value = self.mock_api_call

		response = self.client.get_elastigroup_activity(group_id="sig-123456", start_date="11/05/1993")

		self.assertEqual(len(response), len(mock_get_group_activity_res["response"]["items"]))





# Stateful Tests
class AwsInitTestStateFul(AwsInitTestCase):

	@patch('requests.post')
	def testImportStatefulInstance(self, mock):
		mock_statful_res = self.load_json('test_lib/stateful/import_stateful_res.json')
		mock_stateful_json             = self.load_json('test_lib/stateful/import_stateful.json')

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_statful_res) 

		mock.return_value = self.mock_api_call

		response = self.client.import_stateful_instance(stateful_instance=mock_stateful_json)

		self.assertEqual(len(response), len(mock_statful_res["response"]["items"][0]))

	@patch('requests.get')
	def testGetStatefulImportStatus(self, mock):
		mock_get_stateful_import_res = self.load_json('test_lib/stateful/get_import_res.json')

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_stateful_import_res) 

		mock.return_value = self.mock_api_call

		response = self.client.get_stateful_import_status(stateful_migration_id="smg-ed45f757")

		self.assertEqual(len(response), len(mock_get_stateful_import_res["response"]["items"]))

	@patch('requests.put')
	def testDeallocateStatefulInstance(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 

		mock.return_value = self.mock_api_call

		response = self.client.deallocate_stateful_instance(group_id="sig-1234567", stateful_instance_id="sid-1234567")

		self.assertEqual(len(response), len(self.mock_ok_res["response"]))

	@patch('requests.put')
	def testRecycleStatefulInstance(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 

		mock.return_value = self.mock_api_call

		response = self.client.recycle_stateful_instance(group_id="sig-1234567", stateful_instance_id="sid-1234567")

		self.assertEqual(len(response), len(self.mock_ok_res["response"]))

	@patch('requests.get')
	def testGetStatefulInstances(self, mock):
		mock_get_instances_res = self.load_json('test_lib/stateful/get_instances_res.json')

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_instances_res)

		mock.return_value = self.mock_api_call

		response = self.client.get_stateful_instances(group_id="sig-1234567")

		self.assertEqual(len(response), len(mock_get_instances_res["response"]["items"]))

	@patch('requests.put')
	def testResumeStatefulInstance(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 

		mock.return_value = self.mock_api_call

		response = self.client.pause_stateful_instance(group_id="sig-1234567", stateful_instance_id="sid-1234567")

		self.assertEqual(len(response), len(self.mock_ok_res["response"]))

	@patch('requests.put')
	def testPauseStatefulInstance(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 

		mock.return_value = self.mock_api_call

		response = self.client.resume_stateful_instance(group_id="sig-1234567", stateful_instance_id="sid-1234567")

		self.assertEqual(len(response), len(self.mock_ok_res["response"]))




# Kubernetes
class AwsInitTestKubernetes(AwsInitTestCase):
	@patch('requests.get')
	def testGetKubernetesClusterCost(self, mock):
		mock_kubernetes_cost_res = self.load_json('test_lib/output/kubernetes_cost_res.json')

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_kubernetes_cost_res) 

		mock.return_value = self.mock_api_call

		response = self.client.get_kubernetes_cluster_cost(custer_id="jeffrey.spotinstdemo.com", from_date="2016-01-01", to_date="2018-10-12")

		self.assertEqual(len(response), len(mock_kubernetes_cost_res["response"]["items"][0]))




# Blue Green Deployment
class AWSInitTestBGDeployment(AwsInitTestCase):
	@patch('requests.post')
	def testCreateBDDeployment(self, mock):
		mock_bg_deployment = self.load_json('test_lib/input/bg_deployment.json')

		mock_bg_deployment_res= self.load_json('test_lib/output/bg_deployment_res.json')

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_bg_deployment_res) 

		mock.return_value = self.mock_api_call

		response = self.client.create_blue_green_deployment(group_id="sig-123456", blue_green_deployment=mock_bg_deployment)

		self.assertEqual(len(response), len(mock_bg_deployment_res["response"]["items"][0]))

	@patch('requests.get')
	def testGetBDDeployments(self, mock):
		mock_get_bg_res = self.load_json('test_lib/output/get_bg_status.json')

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_bg_res) 

		mock.return_value = self.mock_api_call

		response = self.client.get_blue_green_deployment(group_id="sig-123456")

		self.assertEqual(len(response), len(mock_get_bg_res["response"]["items"][0]))

	@patch('requests.put')
	def testStopBDDeployment(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 

		mock.return_value = self.mock_api_call

		response = self.client.stop_blue_green_deployment(group_id="sig-1234", deployment_id="cdbg-611a38d3")

		self.assertEqual(len(response), len(self.mock_ok_res["response"]))





# Test Deployment Action
class AWSInitTestDeployment(AwsInitTestCase):
	@patch('requests.get')
	def testGetAllGroupDeployment(self, mock):
		mock_get_deployment_status_res = self.load_json('test_lib/output/get_deployment_status_res.json')

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_deployment_status_res) 

		mock.return_value = self.mock_api_call

		response = self.client.get_all_group_deployment(group_id="sig-123456")

		self.assertEqual(len(response), len(mock_get_deployment_status_res["response"]["items"]))

	@patch('requests.put')
	def testRollGroup(self, mock):
		mock_roll_group_res = self.load_json('test_lib/output/roll_group_res.json')


		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_roll_group_res) 

		mock.return_value = self.mock_api_call

		response = self.client.roll_group(group_id="sig-123456", group_roll=Roll(batch_size_percentage=50, grace_period=150, health_check_type="EC2", strategy=dict(action="REPLACE_SERVER")))

		self.assertEqual(len(response), len(mock_roll_group_res["response"]))

	@patch('requests.get')
	def testGetDeploymentStatus(self, mock):
		mock_roll_status_res = self.load_json('test_lib/output/roll_status_res.json')

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

	@patch('requests.post')
	def testCreateDeploymentAction(self, mock):
		mock_deployment_action_res = self.load_json('test_lib/output/deployment_action_res.json')
		mock_deployment_action         = self.load_json('test_lib/input/deployment_action.json')

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_deployment_action_res) 

		mock.return_value = self.mock_api_call

		response = self.client.create_deployment_action(group_id="sig-123456", roll_id="sbgd-4ea64d71", deployment_action=mock_deployment_action)

		self.assertEqual(len(response), len(mock_deployment_action_res["response"]["items"]))




# Test Instance
class AWSInitTestInstance(AwsInitTestCase):
	@patch('requests.get')
	def testGetInstanceTypeByRegion(self, mock):
		mock_instance_region = self.load_json('test_lib/output/instance_region.json')

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_instance_region) 

		mock.return_value = self.mock_api_call

		response = self.client.get_instance_type_by_region(region="us-east-2")

		self.assertEqual(len(response), len(mock_instance_region["response"]["items"]))	

	@patch('requests.post')
	def testLockInstance(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 

		mock.return_value = self.mock_api_call

		response = self.client.lock_instance(instance_id="i-123456", lock_time=23)

		self.assertEqual(len(response), len(self.mock_ok_res["response"]["status"]))	

	@patch('requests.post')
	def testUnlockInstance(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 

		mock.return_value = self.mock_api_call

		response = self.client.unlock_instance(instance_id="i-123456")

		self.assertEqual(len(response), len(self.mock_ok_res["response"]["status"]))	

	@patch('requests.post')
	def testEnterInstanceStandby(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 

		mock.return_value = self.mock_api_call

		response = self.client.enter_instance_standby(instance_id="i-123456")

		self.assertEqual(len(response), len(self.mock_ok_res["response"]["status"]))	
	
	@patch('requests.post')
	def testEnterInstanceStandby(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 

		mock.return_value = self.mock_api_call

		response = self.client.exit_instance_standby(instance_id="i-123456")

		self.assertEqual(len(response), len(self.mock_ok_res["response"]["status"]))	
	
	@patch('requests.get')
	def getInstanceStatus(self, mock):
		mock_instance_status_res = self.load_json("test_lib/output/instance_status_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_instance_status_res) 

		mock.return_value = self.mock_api_call

		response = self.client.get_instance_status(instance_id="i-123456")

		self.assertEqual(len(response), len(mock_instance_status_res["response"]["items"][0]))	

	@patch('requests.get')
	def testGetInstanceHealthiness(self, mock):
		mock_instance_healthiness_res = self.load_json("test_lib/output/instance_healthiness_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_instance_healthiness_res) 

		mock.return_value = self.mock_api_call

		response = self.client.get_instance_healthiness(group_id="sig-12345")

		self.assertEqual(len(response), len(mock_instance_healthiness_res["response"]["items"][0]))	

	@patch('requests.post')
	def testCreateInstanceSignal(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 

		mock.return_value = self.mock_api_call

		response = self.client.create_instance_signal(instance_id="i-123456", signal="TEST")

		self.assertEqual(len(response), len(self.mock_ok_res["response"]["status"]))	





# Test cost and savings
class AWSInitTestCostAndSavings(AwsInitTestCase):
	@patch('requests.get')
	def testGetCostPerAccount(self, mock):
		mock_cost_per_account_res = self.load_json("test_lib/output/cost_per_account_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_cost_per_account_res) 

		mock.return_value = self.mock_api_call

		response = self.client.get_cost_per_account(to_date="", from_date="")

		self.assertEqual(len(response), len(mock_cost_per_account_res["response"]["items"]))

	@patch('requests.get')
	def testGetCostPerElastigroup(self, mock):
		mock_cost_per_group_res = self.load_json("test_lib/output/cost_per_group_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_cost_per_group_res) 

		mock.return_value = self.mock_api_call

		response = self.client.get_cost_per_elastigroup(group_id="sig-123456", to_date="2016-01-01", from_date="2018-10-15")

		self.assertEqual(len(response), len(mock_cost_per_group_res["response"]["items"]))

	@patch('requests.get')
	def testGroupDetailedCost(self, mock):
		mock_detailed_cost_per_group_res = self.load_json("test_lib/output/detailed_cost_per_group_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_detailed_cost_per_group_res) 

		mock.return_value = self.mock_api_call

		response = self.client.get_group_detailed_cost(group_id="sig-123456", to_date="2016-01-01", from_date="2018-10-15")

		self.assertEqual(len(response), len(mock_detailed_cost_per_group_res["response"]["items"]))

	@patch('requests.get')
	def testGetPotentialSaving(self, mock):
		mock_potential_saving_res= self.load_json("test_lib/output/potential_saving_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_potential_saving_res) 

		mock.return_value = self.mock_api_call

		response = self.client.get_potential_savings()

		self.assertEqual(len(response), len(mock_potential_saving_res["response"]["items"]))

	@patch('requests.get')
	def testGetInstancePotentialSaving(self, mock):
		mock_instance_potential_saving_res= self.load_json("test_lib/output/instance_potential_saving_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_instance_potential_saving_res) 

		mock.return_value = self.mock_api_call

		response = self.client.get_instance_potential_savings(instance_ids=["i-08674ba9a","i-08674ba9a"], region="us-west-2")

		self.assertEqual(len(response), len(mock_instance_potential_saving_res["response"]["items"]))





# Test Scaling Policy
class AWSInitTestScalingPolicy(AwsInitTestCase):
	@patch('requests.post')
	def testSuspendScalingPolicies(self, mock):
		mock_suspend_scaling_res = self.load_json("test_lib/output/suspend_scaling_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_suspend_scaling_res) 

		mock.return_value = self.mock_api_call

		response = self.client.suspend_scaling_policies(group_id="sig-12345", policy_name="TEST")

		self.assertEqual(len(response), len(mock_suspend_scaling_res["response"]["items"][0]))

	@patch('requests.get')
	def testListSuspendedScalingPolicies(self, mock):
		mock_list_suspended_res = self.load_json("test_lib/output/list_suspended_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_list_suspended_res) 

		mock.return_value = self.mock_api_call

		response = self.client.list_suspended_scaling_policies(group_id="sig-12345")

		self.assertEqual(len(response), len(mock_list_suspended_res["response"]["items"]))

	@patch('requests.post')
	def testResumeSuspendedScalingPolicy(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 

		mock.return_value = self.mock_api_call

		response = self.client.resume_suspended_scaling_policies(group_id="sig-123456", policy_name="TEST")

		self.assertEqual(len(response), len(self.mock_ok_res["response"]["status"]))





# Test Processes
class AWSInitTestProcesses(AwsInitTestCase):
	@patch('requests.get')
	def testListSuspendedPocress(self, mock):
		mock_list_process_res = self.load_json("test_lib/output/list_process_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_list_process_res) 

		mock.return_value = self.mock_api_call

		response = self.client.list_suspended_process(group_id="sig-123456")

		self.assertEqual(len(response), len(mock_list_process_res["response"]["items"]))

	@patch('requests.post')
	def testSuspendProcess(self, mock):
		mock_suspended_process_res = self.load_json("test_lib/output/suspended_process_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_suspended_process_res) 

		mock.return_value = self.mock_api_call

		response = self.client.suspend_process(group_id="sig-12345", processes="TEST", suspensions="TEST")

		self.assertEqual(len(response), len(mock_suspended_process_res["response"]["items"]))

	@patch('requests.delete')
	def testRemoveSuspendedProcess(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 

		mock.return_value = self.mock_api_call

		response = self.client.remove_suspended_process(group_id="sig-12345", processes="TEST")

		self.assertEqual(response, True)






# Test Beanstalk
class AWSInitTestBeanstalk(AwsInitTestCase):
	@patch('requests.get')
	def testImportBeanstalk(self, mock):
		mock_beanstalk_import_res = self.load_json("test_lib/output/beanstalk_import_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_beanstalk_import_res) 

		mock.return_value = self.mock_api_call

		response = self.client.beanstalk_import(region="us-west-2", env_id=None, env_name=None)

		self.assertEqual(len(response), len(mock_beanstalk_import_res["response"]["items"][0]))

	@patch('requests.put')
	def testReimportBeanstalk(self, mock):
		mock_beanstalk_reimport_res = self.load_json("test_lib/output/beanstalk_reimport_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_beanstalk_reimport_res) 

		mock.return_value = self.mock_api_call

		response = self.client.beanstalk_reimport(group_id="sig-12345")

		self.assertEqual(len(response), len(mock_beanstalk_reimport_res["response"]["items"][0]))





# Test ASG
class AWSInitTestASG(AwsInitTestCase):
	@patch('requests.post')
	def testImportASG(self, mock):
		mock_import_asg_res = self.load_json("test_lib/output/import_asg_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_import_asg_res) 

		mock.return_value = self.mock_api_call

		response = self.client.import_asg(region="us-west-2", asg_name="Test", asg="Test")

		self.assertEqual(len(response), len(mock_import_asg_res["response"]["items"][0]))





# Test Activity Events
class AWSInitTestASG(AwsInitTestCase):
	@patch('requests.get')
	def testGetActivityEvents(self, mock):
		mock_activity_events_res = self.load_json("test_lib/output/activity_events_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_activity_events_res) 

		mock.return_value = self.mock_api_call

		response = self.client.get_activity_events(group_id="sig-1234", from_date="2016-01-01")

		self.assertEqual(len(response), len(mock_activity_events_res["response"]["items"][0]))





# Test AMI Backup
class AWSInitTestASG(AwsInitTestCase):
	@patch('requests.post')
	def testAmiBackup(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 

		mock.return_value = self.mock_api_call

		response = self.client.ami_backup(group_id="sig-12345")

		self.assertEqual(len(response), len(self.mock_ok_res["response"]["status"]))




# Test Org and Account
class AWSInitTestOrgAndAcct(AwsInitTestCase):
	@patch('requests.post')
	def testCreateOrganization(self, mock):
		mock_create_org_res = self.load_json("test_lib/output/create_org_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_create_org_res) 

		mock.return_value = self.mock_api_call

		response = self.client.create_organization(org_name="test")

		self.assertEqual(len(response), len(mock_create_org_res["response"]["items"][0]))

	@patch('requests.delete')
	def testDeleteOrganization(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 

		mock.return_value = self.mock_api_call

		response = self.client.delete_organization(org_id=123456)

		self.assertEqual(response, True)

	@patch('requests.post')
	def testSetCloudCredentials(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 

		mock.return_value = self.mock_api_call

		response = self.client.set_cloud_credentials(iam_role="arn", external_id="test")

		self.assertEqual(len(response), len(self.mock_ok_res["response"]["status"]))

	@patch('requests.post')
	def testCreateAccount(self, mock):
		mock_create_account_res = self.load_json("test_lib/output/create_account_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_create_account_res) 

		mock.return_value = self.mock_api_call

		response = self.client.create_account(account_name="test")

		self.assertEqual(len(response), len(mock_create_account_res["response"]["items"][0]))


	@patch('requests.get')
	def testGetAccounts(self, mock):
		mock_get_accounts_res = self.load_json("test_lib/output/get_accounts_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_accounts_res) 

		mock.return_value = self.mock_api_call

		response = self.client.get_accounts()

		self.assertEqual(len(response), len(mock_get_accounts_res["response"]["items"]))

	@patch('requests.delete')
	def testDeleteAccount(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 

		mock.return_value = self.mock_api_call

		response = self.client.delete_account(account_name="test")

		self.assertEqual(response, True)

	@patch('requests.post')
	def testCreateUser(self, mock):
		mock_create_user_res = self.load_json("test_lib/output/create_user_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_create_user_res) 

		mock.return_value = self.mock_api_call

		response = self.client.create_user(first_name="jane", last_name="doe", email="jd@mail.com", password="12345", role="test")

		self.assertEqual(len(response), len(mock_create_user_res["response"]["items"][0]))

	@patch('requests.post')
	def testAddExsistingUser(self, mock): 
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 

		mock.return_value = self.mock_api_call

		response = self.client.add_exsisting_user(user_email="test", role="test")

		self.assertEqual(len(response), len(self.mock_ok_res["response"]["status"]))

	@patch('requests.put')
	def testUpdateUserRole(self, mock): 
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 

		mock.return_value = self.mock_api_call

		response = self.client.update_user_role(user_email="test", role="test")

		self.assertEqual(len(response), len(self.mock_ok_res["response"]["status"]))

	@patch('requests.delete')
	def testDetachUser(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps() 

		mock.return_value = self.mock_api_call

		response = self.client.detach_user(user_email="test")

		self.assertEqual(response, True)

	@patch('requests.get')
	def testGetUser(self, mock):
		mock_get_user_res = self.load_json("test_lib/output/get_user_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_user_res) 

		mock.return_value = self.mock_api_call

		response = self.client.get_user(user_email="test")

		self.assertEqual(len(response), len(mock_get_user_res["response"]["items"]))

	@patch('requests.post')
	def testAssignUserToAccounts(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 

		mock.return_value = self.mock_api_call

		response = self.client.assign_user_to_account(mappings=[])

		self.assertEqual(len(response), len(self.mock_ok_res["response"]["status"]))





# Testing EMR
class AWSInitTestEMR(AwsInitTestCase):
	@patch('requests.post')
	def testCreateEMR(self, mock):
		mock_create_emr_res = self.load_json("test_lib/output/emr/create_emr_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_create_emr_res) 

		mock.return_value = self.mock_api_call

		response = self.client.create_emr(emr={})

		self.assertEqual(len(response), len(mock_create_emr_res["response"]["items"][0]))

	@patch('requests.put')
	def testUpdateEMR(self, mock):
		mock_update_emr_res = self.load_json("test_lib/output/emr/create_emr_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_update_emr_res) 

		mock.return_value = self.mock_api_call

		response = self.client.update_emr(emr_id="sigi-123456", emr={})

		self.assertEqual(len(response), len(mock_update_emr_res["response"]["items"][0]))

	@patch('requests.get')
	def testGetAllEMR(self, mock):
		mock_get_all_emr_res = self.load_json("test_lib/output/emr/get_all_emr_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_all_emr_res) 

		mock.return_value = self.mock_api_call

		response = self.client.get_all_emr()

		self.assertEqual(len(response), len(mock_get_all_emr_res["response"]["items"]))

	@patch('requests.get')
	def testGetEMR(self, mock):
		mock_get_emr_res = self.load_json("test_lib/output/emr/get_emr_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_emr_res) 

		mock.return_value = self.mock_api_call

		response = self.client.get_emr(emr_id="sigi-123456")

		self.assertEqual(len(response), len(mock_get_emr_res["response"]["items"][0]))

	@patch('requests.get')
	def testGetEMRInstances(self, mock):
		mock_get_emr_instances_res = self.load_json("test_lib/output/emr/get_emr_instances_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_emr_instances_res) 

		mock.return_value = self.mock_api_call

		response = self.client.get_emr_instances(emr_id="sigi-123456")

		self.assertEqual(len(response), len(mock_get_emr_instances_res["response"]["items"]))

	@patch('requests.get')
	def testGetEMRCluster(self, mock):
		mock_get_emr_cluster_res = self.load_json("test_lib/output/emr/get_emr_cluster_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_emr_cluster_res) 

		mock.return_value = self.mock_api_call

		response = self.client.get_emr_cluster(emr_id="sigi-123456")

		self.assertEqual(len(response), len(mock_get_emr_cluster_res["response"]["items"][0]))

	@patch('requests.get')
	def testGetEMRCost(self, mock):
		mock_get_emr_cost_res = self.load_json("test_lib/output/emr/get_emr_cost_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_emr_cost_res) 

		mock.return_value = self.mock_api_call

		response = self.client.get_emr_cost(emr_id="sigi-123456")

		self.assertEqual(len(response), len(mock_get_emr_cost_res["response"]["items"][0]))

	@patch('requests.delete')
	def testDeleteEMR(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps() 

		mock.return_value = self.mock_api_call

		response = self.client.delete_emr(emr_id="sigi-123456")

		self.assertEqual(response, True)

	@patch('requests.put')
	def testScaleEMRUp(self, mock):
		mock_scale_up_emr_res = self.load_json("test_lib/output/emr/scale_up_emr_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_scale_up_emr_res) 

		mock.return_value = self.mock_api_call

		response = self.client.scale_up_emr(emr_id="sigi-123456", adjustment=1)

		self.assertEqual(len(response), len(mock_scale_up_emr_res["response"]["items"][0]))

	@patch('requests.put')
	def testScaleEMRDown(self, mock):
		mock_scale_down_emr_res = self.load_json("test_lib/output/emr/scale_down_emr_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_scale_down_emr_res) 

		mock.return_value = self.mock_api_call

		response = self.client.scale_down_emr(emr_id="sigi-123456", adjustment=1)

		self.assertEqual(len(response), len(mock_scale_down_emr_res["response"]["items"][0]))





# Test MLB
class AWSInitTestMLB(AwsInitTestCase):
	@patch('requests.get')
	def testGetAllMLBRuntime(self, mock):
		mock_get_all_mlb_runtime = self.load_json("test_lib/output/mlb/get_all_runtime.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_all_mlb_runtime) 

		mock.return_value = self.mock_api_call

		response = self.client.get_all_mlb_runtime()

		self.assertEqual(len(response), len(mock_get_all_mlb_runtime["response"]["items"]))

	@patch('requests.get')
	def testGetMLBRuntime(self, mock):
		mock_get_mlb_runtime = self.load_json("test_lib/output/mlb/get_runtime.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_mlb_runtime) 

		mock.return_value = self.mock_api_call

		response = self.client.get_mlb_runtime(runtime_id="rid-123456")

		self.assertEqual(len(response), len(mock_get_mlb_runtime["response"]["items"][0]))

	@patch('requests.put')
	def testDeregisterMLBRuntime(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 

		mock.return_value = self.mock_api_call

		response = self.client.deregister_mlb_runtime(runtime_id="rid-123456")

		self.assertEqual(len(response), len(self.mock_ok_res["response"]["status"]))

	@patch('requests.delete')
	def testDeleteMLBRuntime(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 

		mock.return_value = self.mock_api_call

		response = self.client.delete_mlb_runtime(runtime_id="rid-123456")

		self.assertEqual(response, True)

	@patch('requests.post')
	def testCreateMLBDeployment(self, mock):
		mock_create_mlb_deployment_res = self.load_json("test_lib/output/mlb/create_deployment_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_create_mlb_deployment_res) 

		mock.return_value = self.mock_api_call

		response = self.client.create_mlb_deployment(deployment_name="test")

		self.assertEqual(len(response), len(mock_create_mlb_deployment_res["response"]["items"][0]))

	@patch('requests.put')
	def testUpdateMLBDeployment(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 

		mock.return_value = self.mock_api_call

		response = self.client.update_mlb_deployment(deployment_id="did-123456", deployment_name="test")

		self.assertEqual(len(response), len(self.mock_ok_res["response"]["status"]))

	@patch('requests.get')
	def testGetMLBDeployment(self, mock):
		mock_get_mlb_deployment_res = self.load_json("test_lib/output/mlb/get_deployment_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_mlb_deployment_res) 

		mock.return_value = self.mock_api_call

		response = self.client.get_mlb_deployment(deployment_id="did-123456")

		self.assertEqual(len(response), len(mock_get_mlb_deployment_res["response"]["items"][0]))

	@patch('requests.get')
	def testGetAllMLBDeployment(self, mock):
		mock_get_all_mlb_deployment_res = self.load_json("test_lib/output/mlb/get_all_deployment_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_all_mlb_deployment_res) 

		mock.return_value = self.mock_api_call

		response = self.client.get_all_mlb_deployment()

		self.assertEqual(len(response), len(mock_get_all_mlb_deployment_res["response"]["items"]))

	@patch('requests.delete')
	def testDeleteMLBDeployment(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 

		mock.return_value = self.mock_api_call

		response = self.client.delete_mlb_deployment(deployment_id="did-123456")

		self.assertEqual(response, True)

	@patch('requests.post')
	def testCreateMLBBalancer(self, mock):
		mock_create_mlb_balancer_res = self.load_json("test_lib/output/mlb/create_balancer_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_create_mlb_balancer_res) 

		mock.return_value = self.mock_api_call

		response = self.client.create_mlb_balancer(balancer={})

		self.assertEqual(len(response), len(mock_create_mlb_balancer_res["response"]["items"][0]))

	@patch('requests.put')
	def testUpdateMLBBalancer(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 

		mock.return_value = self.mock_api_call

		response = self.client.update_mlb_balancer(balancer_id="bid-12345", balancer={})

		self.assertEqual(len(response), len(self.mock_ok_res["response"]["status"]))

	@patch('requests.get')
	def testGetMLBBalancer(self, mock):
		mock_get_mlb_balancer_res = self.load_json("test_lib/output/mlb/get_balancer_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_mlb_balancer_res) 

		mock.return_value = self.mock_api_call

		response = self.client.get_mlb_balancer(balancer_id="bid-12345")

		self.assertEqual(len(response), len(mock_get_mlb_balancer_res["response"]["items"][0]))

	@patch('requests.get')
	def testGetAllMLBBalancer(self, mock):
		mock_get_all_mlb_balancer_res = self.load_json("test_lib/output/mlb/get_all_balancer_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_all_mlb_balancer_res) 

		mock.return_value = self.mock_api_call

		response = self.client.get_all_mlb_balancer()

		self.assertEqual(len(response), len(mock_get_all_mlb_balancer_res["response"]["items"]))

	@patch('requests.delete')
	def testDeleteMLBBalancer(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 

		mock.return_value = self.mock_api_call

		response = self.client.delete_mlb_balancer(balancer_id="bid-12345")

		self.assertEqual(response, True)

	@patch('requests.post')
	def testCreateMLBTargetSet(self, mock):
		mock_create_mlb_target_set_res = self.load_json("test_lib/output/mlb/create_target_set_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_create_mlb_target_set_res) 

		mock.return_value = self.mock_api_call

		response = self.client.create_mlb_target_set(target_set={})

		self.assertEqual(len(response), len(mock_create_mlb_target_set_res["response"]["items"][0]))

	@patch('requests.put')
	def testUpdateMLBTargetSet(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 

		mock.return_value = self.mock_api_call

		response = self.client.update_mlb_target_set(target_set_id="ts-12345", target_set={})

		self.assertEqual(len(response), len(self.mock_ok_res["response"]["status"]))

	@patch('requests.get')
	def testGetMLBTargetSet(self, mock):
		mock_get_mlb_target_set_res = self.load_json("test_lib/output/mlb/get_target_set_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_mlb_target_set_res) 

		mock.return_value = self.mock_api_call

		response = self.client.get_mlb_target_set(target_set_id="ts-12345")

		self.assertEqual(len(response), len(mock_get_mlb_target_set_res["response"]["items"][0]))

	@patch('requests.get')
	def testGetAllMLBTargetSet(self, mock):
		mock_get_all_mlb_target_set_res = self.load_json("test_lib/output/mlb/get_all_target_set_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_all_mlb_target_set_res) 

		mock.return_value = self.mock_api_call

		response = self.client.get_all_mlb_target_set()

		self.assertEqual(len(response), len(mock_get_all_mlb_target_set_res["response"]["items"]))

	@patch('requests.delete')
	def testDeleteMLBTargetSet(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 

		mock.return_value = self.mock_api_call

		response = self.client.delete_mlb_target_set(target_set_id="ts-12345")

		self.assertEqual(response, True)

	@patch('requests.put')
	def testRegisterMLBTargets(self, mock):
		mock_register_target_res = self.load_json("test_lib/output/mlb/register_target_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_register_target_res) 

		mock.return_value = self.mock_api_call

		response = self.client.register_mlb_targets(target_set_id="ts-12345", targets=[])

		self.assertEqual(len(response), len(mock_register_target_res["response"]["items"]))

	@patch('requests.put')
	def testDegristerMLBTargets(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 

		mock.return_value = self.mock_api_call

		response = self.client.deregister_mlb_targets(target_set_id="ts-12345", targets=[])

		self.assertEqual(len(response), len(self.mock_ok_res["response"]["status"]))

	@patch('requests.post')
	def testCreateMLBTarget(self, mock):
		mock_create_mlb_target_res = self.load_json("test_lib/output/mlb/create_target_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_create_mlb_target_res) 

		mock.return_value = self.mock_api_call

		response = self.client.create_mlb_target(target={})

		self.assertEqual(len(response), len(mock_create_mlb_target_res["response"]["items"][0]))

	@patch('requests.put')
	def testUpdateMLBTarget(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 

		mock.return_value = self.mock_api_call

		response = self.client.update_mlb_target(target_id="t-12345", target={})

		self.assertEqual(len(response), len(self.mock_ok_res["response"]["status"]))

	@patch('requests.get')
	def testGetMLBTarget(self, mock):
		mock_get_mlb_target_res = self.load_json("test_lib/output/mlb/get_target_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_mlb_target_res) 

		mock.return_value = self.mock_api_call

		response = self.client.get_mlb_target(target_id="t-12345")

		self.assertEqual(len(response), len(mock_get_mlb_target_res["response"]["items"][0]))

	@patch('requests.get')
	def testGetAllMLBTarget(self, mock):
		mock_get_all_mlb_target_res = self.load_json("test_lib/output/mlb/get_all_target_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_all_mlb_target_res) 

		mock.return_value = self.mock_api_call

		response = self.client.get_all_mlb_target()

		self.assertEqual(len(response), len(mock_get_all_mlb_target_res["response"]["items"]))

	@patch('requests.delete')
	def testDeleteMLBTarget(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 

		mock.return_value = self.mock_api_call

		response = self.client.delete_mlb_target(target_id="t-12345")

		self.assertEqual(response, True)

	@patch('requests.post')
	def testCreateMLBListener(self, mock):
		mock_create_mlb_listener = self.load_json("test_lib/output/mlb/listener.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_create_mlb_listener) 

		mock.return_value = self.mock_api_call

		response = self.client.create_mlb_listener(listener={})

		self.assertEqual(len(response), len(mock_create_mlb_listener["response"]["items"][0]))

	@patch('requests.put')
	def testUpdateMLBListener(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 

		mock.return_value = self.mock_api_call

		response = self.client.update_mlb_listener(listener_id="ls-12345",listener={})

		self.assertEqual(len(response), len(self.mock_ok_res["response"]["status"]))

	@patch('requests.get')
	def testGetMLBListener(self, mock):
		mock_get_mlb_listener = self.load_json("test_lib/output/mlb/listener.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_mlb_listener) 

		mock.return_value = self.mock_api_call

		response = self.client.get_mlb_listener(listener_id="ls-12345")

		self.assertEqual(len(response), len(mock_get_mlb_listener["response"]["items"][0]))

	@patch('requests.get')
	def testGetAllMLBListener(self, mock):
		mock_get_all_mlb_listner = self.load_json("test_lib/output/mlb/listener.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_all_mlb_listner) 

		mock.return_value = self.mock_api_call

		response = self.client.get_all_mlb_listener()

		self.assertEqual(len(response), len(mock_get_all_mlb_listner["response"]["items"]))

	@patch('requests.delete')
	def testDeleteMLBListener(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 

		mock.return_value = self.mock_api_call

		response = self.client.delete_mlb_listener(listener_id="ls-12345")

		self.assertEqual(response, True)

	@patch('requests.post')
	def testCreateMLBMiddleware(self, mock):
		mock_create_mlb_middleware = self.load_json("test_lib/output/mlb/middleware.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_create_mlb_middleware) 

		mock.return_value = self.mock_api_call

		response = self.client.create_mlb_middleware(middleware={})

		self.assertEqual(len(response), len(mock_create_mlb_middleware["response"]["items"][0]))

	@patch('requests.put')
	def testUpdateMLBMiddleware(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 

		mock.return_value = self.mock_api_call

		response = self.client.update_mlb_middleware(middleware_id="mw-12345",middleware={})

		self.assertEqual(len(response), len(self.mock_ok_res["response"]["status"]))

	@patch('requests.get')
	def testGetMLBMiddleware(self, mock):
		mock_get_mlb_middleware = self.load_json("test_lib/output/mlb/middleware.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_mlb_middleware) 

		mock.return_value = self.mock_api_call

		response = self.client.get_mlb_middleware(middleware_id="mw-12345")

		self.assertEqual(len(response), len(mock_get_mlb_middleware["response"]["items"][0]))

	@patch('requests.get')
	def testGetAllMLBMiddleware(self, mock):
		mock_get_all_mlb_middleware = self.load_json("test_lib/output/mlb/middleware.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_all_mlb_middleware) 

		mock.return_value = self.mock_api_call

		response = self.client.get_all_mlb_middleware()

		self.assertEqual(len(response), len(mock_get_all_mlb_middleware["response"]["items"]))

	@patch('requests.delete')
	def testDeleteMLBMiddleware(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 

		mock.return_value = self.mock_api_call

		response = self.client.delete_mlb_middleware(middleware_id="mw-12345")

		self.assertEqual(response, True)

	@patch('requests.post')
	def testCreateMLBRoutingRule(self, mock):
		mock_create_mlb_routing_rule = self.load_json("test_lib/output/mlb/routing_rule.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_create_mlb_routing_rule) 

		mock.return_value = self.mock_api_call

		response = self.client.create_mlb_routing_rule(routing_rule={})

		self.assertEqual(len(response), len(mock_create_mlb_routing_rule["response"]["items"][0]))

	@patch('requests.put')
	def testUpdateMLBRoutingRule(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 

		mock.return_value = self.mock_api_call

		response = self.client.update_mlb_routing_rule(routing_rule_id="rr-12345",routing_rule={})

		self.assertEqual(len(response), len(self.mock_ok_res["response"]["status"]))

	@patch('requests.get')
	def testGetMLBRoutingRule(self, mock):
		mock_get_mlb_routing_rule = self.load_json("test_lib/output/mlb/routing_rule.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_mlb_routing_rule) 

		mock.return_value = self.mock_api_call

		response = self.client.get_mlb_routing_rule(routing_rule_id="rr-12345")

		self.assertEqual(len(response), len(mock_get_mlb_routing_rule["response"]["items"][0]))

	@patch('requests.get')
	def testGetAllMLBRoutingRule(self, mock):
		mock_get_all_mlb_routing_rule = self.load_json("test_lib/output/mlb/routing_rule.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_all_mlb_routing_rule) 

		mock.return_value = self.mock_api_call

		response = self.client.get_all_mlb_routing_rule()

		self.assertEqual(len(response), len(mock_get_all_mlb_routing_rule["response"]["items"]))

	@patch('requests.delete')
	def testDeleteRoutingRule(self, mock):
		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(self.mock_ok_res) 

		mock.return_value = self.mock_api_call

		response = self.client.delete_mlb_routing_rule(routing_rule_id="rr-12345")

		self.assertEqual(response, True)




