import unittest

from spotinst_sdk import SpotinstClient
from spotinst_sdk.aws_elastigroup import *


class AwsElastigroupTestCase(unittest.TestCase):

    def setUp(self):
        self.client = SpotinstClient(auth_token='dummy-token', account_id='act-1234567')
        self.mock_group_json = self.load_group_json()

    def create_formatted_group_request(self, group):
        group_request = ElastigroupCreationRequest(group)
        excluded_group_dict = self.client.exclude_missing(json.loads(group_request.toJSON()))
        formatted_group_dict = self.client.convert_json(excluded_group_dict, self.client.underscore_to_camel)
        return formatted_group_dict

    @staticmethod
    def load_group_json():
        with open('group.json') as group_json:
            return json.load(group_json)


class AwsElastigroupExcludeMissingTest(AwsElastigroupTestCase):
    def runTest(self):
        dummy_obj = {"valid_key": "valid_value", "null_key": None, "ignored_key": none}
        expected_obj = {"valid_key": "valid_value", "null_key": None}
        actual_obj = self.client.exclude_missing(dummy_obj)
        self.assertDictEqual(actual_obj, expected_obj)


class AwsElastigroupTestEcsIntegration(AwsElastigroupTestCase):
    def runTest(self):
        ecs_auto_scale_down = EcsAutoScalerDownConfiguration(evaluation_periods=3)
        ecs_auto_scale_attribute = EcsAutoScalerAttributeConfiguration(key='the_key',
                                                                       value='the_value')
        ecs_auto_scale_headroom = EcsAutoScalerHeadroomConfiguration(cpu_per_unit=4096,
                                                                     memory_per_unit=4096,
                                                                     num_of_units=30)
        ecs_auto_scale = EcsAutoScaleConfiguration(is_enabled=True, is_auto_config=False,
                                                   cooldown=900,
                                                   headroom=ecs_auto_scale_headroom,
                                                   down=ecs_auto_scale_down,
                                                   attributes=[ecs_auto_scale_attribute])
        ecs = EcsConfiguration(cluster_name='test-ecs', auto_scale=ecs_auto_scale)
        third_party_integrations = ThirdPartyIntegrations(ecs=ecs)

        group = Elastigroup(third_parties_integration=third_party_integrations)

        formatted_group_dict = self.create_formatted_group_request(group)

        actual_request_json = formatted_group_dict['group']['thirdPartiesIntegration']['ecs']
        expected_request_json = self.mock_group_json['group']['thirdPartiesIntegration']['ecs']

        self.assertDictEqual(actual_request_json, expected_request_json)


class AwsElastigroupTestKubernetesIntegration(AwsElastigroupTestCase):
    def runTest(self):
        kubernetes_auto_scale_down = KubernetesAutoScalerDownConfiguration(
            evaluation_periods=5)
        kubernetes_auto_scale_headroom = KubernetesAutoScalerHeadroomConfiguration(
            cpu_per_unit=2000, memory_per_unit=4000, num_of_units=2)
        kubernetes_auto_scale = EcsAutoScaleConfiguration(is_enabled=True, cooldown=300,
                                                          headroom=kubernetes_auto_scale_headroom,
                                                          down=kubernetes_auto_scale_down,
                                                          is_auto_config=False)
        kubernetes = KubernetesConfiguration(integration_mode='pod',
                                             cluster_identifier='test-k8s',
                                             auto_scale=kubernetes_auto_scale)
        third_party_integrations = ThirdPartyIntegrations(kubernetes=kubernetes)

        group = Elastigroup(third_parties_integration=third_party_integrations)
        formatted_group_dict = self.create_formatted_group_request(group)

        actual_request_json = formatted_group_dict['group']['thirdPartiesIntegration']['kubernetes']
        expected_request_json = self.mock_group_json['group']['thirdPartiesIntegration']['kubernetes']

        self.assertDictEqual(actual_request_json, expected_request_json)


class AwsElastigroupTestNomadIntegration(AwsElastigroupTestCase):
    def runTest(self):
        nomad_down = NomadAutoScalerDownConfiguration(evaluation_periods=3)
        nomad_constraints = NomadAutoScalerConstraintsConfiguration(
            key='${node.class}', value='value')
        nomad_scale_headroom = NomadAutoScalerHeadroomConfiguration(cpu_per_unit=10,
                                                                    memory_per_unit=1000,
                                                                    num_of_units=2)
        nomad_auto_scale = NomadAutoScalerConfiguration(is_enabled=True, cooldown=180,
                                                        headroom=nomad_scale_headroom,
                                                        constraints=[nomad_constraints],
                                                        down=nomad_down)
        nomad = NomadConfiguration(master_host="https://master.host.com", master_port=443,
                                   acl_token='123', auto_scale=nomad_auto_scale)
        third_party_integrations = ThirdPartyIntegrations(nomad=nomad)

        group = Elastigroup(third_parties_integration=third_party_integrations)
        formatted_group_dict = self.create_formatted_group_request(group)

        actual_request_json = formatted_group_dict['group']['thirdPartiesIntegration']['nomad']
        expected_request_json = self.mock_group_json['group']['thirdPartiesIntegration']['nomad']

        self.assertDictEqual(actual_request_json, expected_request_json)


class AwsElastigroupTestDockerSwarmIntegration(AwsElastigroupTestCase):
    def runTest(self):
        docker_swarm_down = DockerSwarmAutoScalerDownConfiguration(evaluation_periods=4)
        docker_swarm_headroom = DockerSwarmAutoScalerHeadroomConfiguration(cpu_per_unit=1000000000,
                                                                           memory_per_unit=800000000, num_of_units=3)
        docker_swarm_auto_scale = DockerSwarmAutoScalerConfiguration(is_enabled=True, cooldown=300,
                                                                     headroom=docker_swarm_headroom,
                                                                     down=docker_swarm_down)
        docker_swarm = DockerSwarmConfiguration(master_host='10.10.10.10', master_port=1234,
                                                auto_scale=docker_swarm_auto_scale)
        third_party_integrations = ThirdPartyIntegrations(docker_swarm=docker_swarm)

        group = Elastigroup(third_parties_integration=third_party_integrations)
        formatted_group_dict = self.create_formatted_group_request(group)

        actual_request_json = formatted_group_dict['group']['thirdPartiesIntegration']['dockerSwarm']
        expected_request_json = self.mock_group_json['group']['thirdPartiesIntegration']['dockerSwarm']

        self.assertDictEqual(actual_request_json, expected_request_json)


class AwsElastigroupTestCodeDeployIntegration(AwsElastigroupTestCase):
    def runTest(self):
        code_deploy_deployment_groups = CodeDeployDeploymentGroupsConfiguration(application_name='test-app',
                                                                                deployment_group_name='test-grp')
        code_deploy = CodeDeployConfiguration(clean_up_on_failure=False, terminate_instance_on_failure=False,
                                              deployment_groups=[code_deploy_deployment_groups])
        third_party_integrations = ThirdPartyIntegrations(code_deploy=code_deploy)

        group = Elastigroup(third_parties_integration=third_party_integrations)
        formatted_group_dict = self.create_formatted_group_request(group)

        actual_request_json = formatted_group_dict['group']['thirdPartiesIntegration']['codeDeploy']
        expected_request_json = self.mock_group_json['group']['thirdPartiesIntegration']['codeDeploy']

        self.assertDictEqual(actual_request_json, expected_request_json)


class AwsElastigroupTestRoute53Integration(AwsElastigroupTestCase):
    def runTest(self):
        route53_record_set = Route53RecordSetsConfiguration(use_public_ip=True, name='test-domain.com')
        route53_domains = Route53DomainsConfiguration(hosted_zone_id='Z3UFMBCGJMYLUT', record_sets=[route53_record_set])
        route53 = Route53Configuration(domains=[route53_domains])
        third_party_integrations = ThirdPartyIntegrations(route53=route53)

        group = Elastigroup(third_parties_integration=third_party_integrations)
        formatted_group_dict = self.create_formatted_group_request(group)

        actual_request_json = formatted_group_dict['group']['thirdPartiesIntegration']['route53']
        expected_request_json = self.mock_group_json['group']['thirdPartiesIntegration']['route53']

        self.assertDictEqual(actual_request_json, expected_request_json)
