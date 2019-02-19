import os
import unittest
import json
from mock import patch

from spotinst_sdk import SpotinstSession

class SimpleNamespace:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

class AwsInitTestCase(unittest.TestCase):

	def setUp(self):
		self.session = SpotinstSession(
			auth_token='dummy-token',
			account_id='dummy-account')

		self.client = self.session.client("mlb")
		self.mock_ok_res   = self.load_json('../test_lib/output/res_ok.json')
		self.mock_api_call = SimpleNamespace(**self.load_json('../test_lib/api_res.json'))


	@staticmethod
	def load_json(path):
		with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), path)) as group_json:
			return json.load(group_json)


# Test MLB
class AWSInitTestMLB(AwsInitTestCase):
	@patch('requests.get')
	def testGetAllMLBRuntime(self, mock):
		mock_get_all_mlb_runtime = self.load_json("../test_lib/output/mlb/get_all_runtime.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_all_mlb_runtime) 

		mock.return_value = self.mock_api_call

		response = self.client.get_all_mlb_runtime()

		self.assertEqual(len(response), len(mock_get_all_mlb_runtime["response"]["items"]))

	@patch('requests.get')
	def testGetMLBRuntime(self, mock):
		mock_get_mlb_runtime = self.load_json("../test_lib/output/mlb/get_runtime.json")

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
		mock_create_mlb_deployment_res = self.load_json("../test_lib/output/mlb/create_deployment_res.json")

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
		mock_get_mlb_deployment_res = self.load_json("../test_lib/output/mlb/get_deployment_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_mlb_deployment_res) 

		mock.return_value = self.mock_api_call

		response = self.client.get_mlb_deployment(deployment_id="did-123456")

		self.assertEqual(len(response), len(mock_get_mlb_deployment_res["response"]["items"][0]))

	@patch('requests.get')
	def testGetAllMLBDeployment(self, mock):
		mock_get_all_mlb_deployment_res = self.load_json("../test_lib/output/mlb/get_all_deployment_res.json")

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
		mock_create_mlb_balancer_res = self.load_json("../test_lib/output/mlb/create_balancer_res.json")

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
		mock_get_mlb_balancer_res = self.load_json("../test_lib/output/mlb/get_balancer_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_mlb_balancer_res) 

		mock.return_value = self.mock_api_call

		response = self.client.get_mlb_balancer(balancer_id="bid-12345")

		self.assertEqual(len(response), len(mock_get_mlb_balancer_res["response"]["items"][0]))

	@patch('requests.get')
	def testGetAllMLBBalancer(self, mock):
		mock_get_all_mlb_balancer_res = self.load_json("../test_lib/output/mlb/get_all_balancer_res.json")

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
		mock_create_mlb_target_set_res = self.load_json("../test_lib/output/mlb/create_target_set_res.json")

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
		mock_get_mlb_target_set_res = self.load_json("../test_lib/output/mlb/get_target_set_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_mlb_target_set_res) 

		mock.return_value = self.mock_api_call

		response = self.client.get_mlb_target_set(target_set_id="ts-12345")

		self.assertEqual(len(response), len(mock_get_mlb_target_set_res["response"]["items"][0]))

	@patch('requests.get')
	def testGetAllMLBTargetSet(self, mock):
		mock_get_all_mlb_target_set_res = self.load_json("../test_lib/output/mlb/get_all_target_set_res.json")

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
		mock_register_target_res = self.load_json("../test_lib/output/mlb/register_target_res.json")

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
		mock_create_mlb_target_res = self.load_json("../test_lib/output/mlb/create_target_res.json")

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
		mock_get_mlb_target_res = self.load_json("../test_lib/output/mlb/get_target_res.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_mlb_target_res) 

		mock.return_value = self.mock_api_call

		response = self.client.get_mlb_target(target_id="t-12345")

		self.assertEqual(len(response), len(mock_get_mlb_target_res["response"]["items"][0]))

	@patch('requests.get')
	def testGetAllMLBTarget(self, mock):
		mock_get_all_mlb_target_res = self.load_json("../test_lib/output/mlb/get_all_target_res.json")

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
		mock_create_mlb_listener = self.load_json("../test_lib/output/mlb/listener.json")

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
		mock_get_mlb_listener = self.load_json("../test_lib/output/mlb/listener.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_mlb_listener) 

		mock.return_value = self.mock_api_call

		response = self.client.get_mlb_listener(listener_id="ls-12345")

		self.assertEqual(len(response), len(mock_get_mlb_listener["response"]["items"][0]))

	@patch('requests.get')
	def testGetAllMLBListener(self, mock):
		mock_get_all_mlb_listner = self.load_json("../test_lib/output/mlb/listener.json")

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
		mock_create_mlb_middleware = self.load_json("../test_lib/output/mlb/middleware.json")

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
		mock_get_mlb_middleware = self.load_json("../test_lib/output/mlb/middleware.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_mlb_middleware) 

		mock.return_value = self.mock_api_call

		response = self.client.get_mlb_middleware(middleware_id="mw-12345")

		self.assertEqual(len(response), len(mock_get_mlb_middleware["response"]["items"][0]))

	@patch('requests.get')
	def testGetAllMLBMiddleware(self, mock):
		mock_get_all_mlb_middleware = self.load_json("../test_lib/output/mlb/middleware.json")

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
		mock_create_mlb_routing_rule = self.load_json("../test_lib/output/mlb/routing_rule.json")

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
		mock_get_mlb_routing_rule = self.load_json("../test_lib/output/mlb/routing_rule.json")

		self.mock_api_call.content = SimpleNamespace(**self.mock_api_call.content)
		self.mock_api_call.content.decode = lambda code: json.dumps(mock_get_mlb_routing_rule) 

		mock.return_value = self.mock_api_call

		response = self.client.get_mlb_routing_rule(routing_rule_id="rr-12345")

		self.assertEqual(len(response), len(mock_get_mlb_routing_rule["response"]["items"][0]))

	@patch('requests.get')
	def testGetAllMLBRoutingRule(self, mock):
		mock_get_all_mlb_routing_rule = self.load_json("../test_lib/output/mlb/routing_rule.json")

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


