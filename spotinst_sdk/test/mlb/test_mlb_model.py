import os
import unittest

from spotinst_sdk import SpotinstSession
from spotinst_sdk.models.mlb import *

class SpotinstEMRTestCase(unittest.TestCase):

    def setUp(self):
        self.session = SpotinstSession(
            auth_token='dummy-token',
            account_id='act-1234567')
        self.client = self.session.client("functions")

        self.mock_balancer_json = self.load_json("../test_lib/input/mlb/balancer.json")
        self.mock_target_set_json = self.load_json("../test_lib/input/mlb/target_set.json")
        self.mock_target_json = self.load_json("../test_lib/input/mlb/target.json")
        self.mock_targets_json = self.load_json("../test_lib/input/mlb/targets.json")
        self.mock_listener_json = self.load_json("../test_lib/input/mlb/listener.json")
        self.mock_middleware_json = self.load_json("../test_lib/input/mlb/middleware.json")
        self.mock_routing_rule_json = self.load_json("../test_lib/input/mlb/routing_rule.json")


    def create_formatted_balancer_request(self, balancer):
        balancer = BalancerRequest(balancer)

        excluded_balancer_dict = self.client.exclude_missing(
            json.loads(balancer.toJSON()))

        formatted_balancer_dict = self.client.convert_json(
            excluded_balancer_dict, self.client.underscore_to_camel)

        return formatted_balancer_dict

    def create_formatted_target_set_request(self, target_set):
        target_set = TargetSetRequest(target_set)

        excluded_target_set_dict = self.client.exclude_missing(
            json.loads(target_set.toJSON()))

        formatted_target_set_dict = self.client.convert_json(
            excluded_target_set_dict, self.client.underscore_to_camel)

        return formatted_target_set_dict

    def create_formatted_target_request(self, target):
        target = TargetRequest(target)

        excluded_target_dict = self.client.exclude_missing(
            json.loads(target.toJSON()))

        formatted_target_dict = self.client.convert_json(
            excluded_target_dict, self.client.underscore_to_camel)

        return formatted_target_dict

    def create_formatted_targets_request(self, targets):
        targets = TargetsRequest(targets)

        excluded_targets_dict = self.client.exclude_missing(
            json.loads(targets.toJSON()))

        formatted_targets_dict = self.client.convert_json(
            excluded_targets_dict, self.client.underscore_to_camel)

        return formatted_targets_dict

    def create_formatted_middleware_request(self, middleware):
        middleware = MiddlewareRequest(middleware)

        excluded_middleware_dict = self.client.exclude_missing(
            json.loads(middleware.toJSON()))

        formatted_middleware_dict = self.client.convert_json(
            excluded_middleware_dict, self.client.underscore_to_camel)

        return formatted_middleware_dict

    def create_formatted_routing_rule_request(self, routing_rule):
        routing_rule = RoutingRuleRequest(routing_rule)

        excluded_routing_rule_dict = self.client.exclude_missing(
            json.loads(routing_rule.toJSON()))

        formatted_routing_rule_dict = self.client.convert_json(
            excluded_routing_rule_dict, self.client.underscore_to_camel)

        return formatted_routing_rule_dict

    def create_formatted_listener_request(self, listener):
        listener = ListenerRequest(listener)

        excluded_listener_dict = self.client.exclude_missing(
            json.loads(listener.toJSON()))

        formatted_listener_dict = self.client.convert_json(
            excluded_listener_dict, self.client.underscore_to_camel)

        return formatted_listener_dict



    @staticmethod
    def load_json(input_file):
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), input_file)) as output_json:
            return json.load(output_json)

class SpotinstBalancerCreate(SpotinstEMRTestCase):
	def runTest(self):

		balancer = Balancer(
			name="bestLoadBalancerInTheWorld",
			timeouts=Timeout(idle=60,draining=300),
			tags=[Tag(key="Environment",value="Production")])

		formatted = self.create_formatted_balancer_request(balancer)
		expected = self.mock_balancer_json

		self.assertDictEqual(formatted, expected)

class SpotinstTargetSetCreate(SpotinstEMRTestCase):
	def runTest(self):

		target_set = TargetSet(
			name="targetSet1",
			balancer_id="lb-5470a9fb",
			deployment_id="de-12345",
			protocol="HTTP",
			weight=1,
			config=Config(rate_limiter=RateLimiter(requests_per_second=10)),
			integrations=Integrations(ecs=[ECS(target_group_arn="arn:aws:elasticloadbalancing:us-east-1:12345:targetgroup/MyTargetGroup/12345",
												target_group_name="MyTargetGroup",
												region="us-east-1",
												service_name="11",
												cluster_name="22")]),
			health_check=HealthCheck(interval=10,
									 path="/healthCheck",
									 port=80,
									 protocol="HTTP",
									 timeout=5,
									 healthy_threshold_count=2,
									 unhealthy_threshold_count=3),
			tags=[Tag(key="Environment",value="Production")])


		formatted = self.create_formatted_target_set_request(target_set)
		expected = self.mock_target_set_json

		self.assertDictEqual(formatted, expected)

class SpotinstTargetCreate(SpotinstEMRTestCase):
	def runTest(self):

		target = Target(
			name="target1",
			balancer_id="lb-12345",
			target_set_id="ts-12345",
			host="10.0.0.2",
			port=8080,
			weight=1,
			tags=[Tag(key="Environment",value="Production")])

		formatted = self.create_formatted_target_request(target)
		expected = self.mock_target_json

		self.assertDictEqual(formatted, expected)

class SpotinstTargetsCreate(SpotinstEMRTestCase):
	def runTest(self):

		targets = [
			Target(
				name="target 1",
				host="10.0.0.2",
				port=1337,
				weight=1,
				tags=[Tag(key="Environment",value="Production")]), 
			Target(
				name="target 2",
				host="10.0.0.2",
				port=1337,
				weight=10,
				tags=[Tag(key="Environment",value="Production")])]

		formatted = self.create_formatted_targets_request(targets)
		expected = self.mock_targets_json

		self.assertDictEqual(formatted, expected)

class SpotinstMiddlewareCreate(SpotinstEMRTestCase):
	def runTest(self):

		conditions = [
			Condition(
				type="HTTP_REQUEST_IP",
				values=[
					"1.2.3.4",
					"1.2.3.5"
				]
				)
			]

		spec = Spec(
			action="ALLOW",
			conditions=conditions)

		middleware = Middleware(
			balancer_id="lb-6acf2ff362ac",
			type="ACL",
			priority=1,
			spec=spec,
			tags=[Tag(key="Environment",value="Production")])

		formatted = self.create_formatted_middleware_request(middleware)
		expected = self.mock_middleware_json

		self.assertDictEqual(formatted, expected)

class SpotinstListenerCreate(SpotinstEMRTestCase):
	def runTest(self):

		tls_config = TLSConfig(
			min_version="TLS10",
			max_version="TLS12",
			session_tickets_disabled=True,
			prefer_server_cipher_suites=True,
			cipher_suites=[
				"TLS_RSA_WITH_AES_256_CBC_SHA",
				"TLS_RSA_WITH_AES_128_CBC_SHA256"
			],
			insecure_skip_verify=False,
			certificate_ids=[
				"ce-12345",
				"ce-67890"
			])

		listener = Listener(
			balancer_id="lb-5470a9fb",
			protocol="HTTPS",
			port="443",
			tls_config=tls_config,
			tags=[Tag(key="Environment",value="Production")])

		formatted = self.create_formatted_listener_request(listener)
		expected = self.mock_listener_json

		self.assertDictEqual(formatted, expected)

class SpotinstRountingRuleCreate(SpotinstEMRTestCase):
	def runTest(self):

		routing_rule = RoutingRule(
			balancer_id="lb-12345",
			route="PathRegexp(`/`)",
			target_set_ids=[
				"ts-12345",
				"ts-67890"
			],
			middleware_ids=[
				"mw-23456",
				"mw-7890"
			],
			listener_id="ls-12345",
			priority=2,
			tags=[Tag(key="Environment",value="Production")]
			)

		formatted = self.create_formatted_routing_rule_request(routing_rule)
		expected = self.mock_routing_rule_json

		self.assertDictEqual(formatted, expected)









