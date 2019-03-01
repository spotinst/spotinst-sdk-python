import os
import unittest

from spotinst_sdk2 import SpotinstSession
from spotinst_sdk2.models.elastigroup.azure import *

class GcpElastigroupTestCase(unittest.TestCase):

    def setUp(self):
        self.session = SpotinstSession(
            auth_token='dummy-token',
            account_id='dummy-account')

        self.client = self.session.client("elastigroup_azure")

        self.mock_group_json = self.load_group_json()

    def create_formatted_group_request(self, group):
        group_request = ElastigroupCreationRequest(group)
        excluded_group_dict = self.client.exclude_missing(
            json.loads(group_request.toJSON()))
        formatted_group_dict = self.client.convert_json(
            excluded_group_dict, self.client.underscore_to_camel)
        return formatted_group_dict

    @staticmethod
    def load_group_json():
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../test_lib/input/elastigroup/azure_group.json')) as group_json:
            return json.load(group_json)

# region Elastigroup
class GcpElastigroupTest(GcpElastigroupTestCase):
    def runTest(self):
        ############################# Capacity #############################
        capacity = Capacity(minimum=0, maximum=0, target=0)

        ############################# Strategy #############################
        strategy = Strategy(            
            low_priority_percentage=0,
            on_demand_count=0,
            draining_timeout=0)

        ############################# Compute ##############################
        managed_service_identity = ManagedServiceIdentity(resource_group_name="resource_group_name", name="name")

        protected_settings = ProtectedSettings(command_to_execute="command_to_execute")

        extension = Extension(
            auto_upgrade_minor_version=False,
            name="none",
            publisher="publisher",
            extension_type="extension_type",
            type_handler_version="type_handler_version",
            protected_settings=protected_settings)

        tag = Tag(tag_key="tag_key", tag_value="tag_value")

        load_balancer = LoadBalancer(
            balancer_id="balancer_id",
            target_set_id="target_set_id",
            auto_weight=False,
            resource_group_name="resource_group_name",
            application_gateway_name="application_gateway_name",
            backend_pool_name="backend_pool_name",
            balancer_type="type")

        load_balancers_config = LoadBalancerConfig(load_balancers=[load_balancer])

        login = Login(
            ssh_public_key="ssh_public_key",
            user_name="user_name",
            password="password")

        additional_ip_configuration = AdditionalIpConfiguration(name="name", private_ip_address_version="private_ip_address_version")

        network = Network(
            virtual_network_name="virtual_network_name",
            subnet_name="subnet_name",
            resource_group_name="resource_group_name",
            assign_public_ip=False,
            additional_ip_configurations=[additional_ip_configuration])

        custom = Custom(
            resource_group_name="resource_group_name",
            image_name="image_name")

        marketplace = Marketplace(
            publisher="publisher",
            offer="offer",
            sku="sku",
            version="version")

        image = Image(marketplace=marketplace, custom=custom)

        launch_specification = LaunchSpecification(
            image=image,
            network=network,
            login=login,
            user_data="user_data",
            shutdown_script="shutdown_script",
            custom_data="custom_data",
            load_balancers_config=load_balancers_config,
            tags=[tag],
            extensions=[extension],
            managed_service_identities=[managed_service_identity])

        health = Health(
            health_check_type="health_check_type",
            auto_healing=False,
            grace_period=0)

        vm_sizes = VmSizes(
            od_sizes=["od_sizes"],
            low_priority_sizes=["low_priority_sizes"])

        compute = Compute(
            vm_sizes=vm_sizes,
            product="product",
            health=health,
            launch_specification=launch_specification)

        ############################## Scaling #############################
        action = ScalingPolicyAction(
            scaling_type="scaling_type",
            adjustment=0,
            min_target_capacity=0,
            target=0,
            maximum=0,
            minimum=0)

        dimensions = ScalingPolicyDimension(name="name", value="value")

        scaling_policy = ScalingPolicy(
            policy_name="policy_name",
            namespace="namespace",
            metric_name="metric_name",
            dimensions=[dimensions],
            statistic="statistic",
            unit="unit",
            threshold=0,
            adjustment=0,
            min_target_capacity=0,
            period=0,
            evaluation_periods=0,
            cooldown=0,
            action=action,
            operator=0)

        scaling = Scaling(up=[scaling_policy], down=[scaling_policy])

        ############################# Scheduling ############################

        task = SchedulingTask(
            is_enabled=False,
            cron_expression="cron_expression",
            task_type="task_type",
            scale_target_capacity=0,
            scale_min_capacity=0,
            scale_max_capacity=0,
            batch_size_percentage=0,
            grace_period=0,
            adjustment=0,
            adjustment_percentage=0)

        scheduling = Scheduling(tasks=[task])

        #################### Third Parties Integrations #####################

        mlb_runtime = MlbRuntime(deployment_id="deployment_id")

        kubernetes = Kubernetes(cluster_identifier="cluster_identifier")

        third_parties_integration = ThirdPartiesIntegration(mlb_runtime=mlb_runtime, kubernetes=kubernetes)

        ###################### Elastigroup Operations #######################

        elastigroup = Elastigroup(
            name="name",
            region="region",
            resource_group_name="resource_group_name",
            capacity=capacity,
            strategy=strategy,
            compute=compute,
            scaling=scaling,
            scheduling=scheduling,
            third_parties_integration=third_parties_integration)


        formatted_group_dict = self.create_formatted_group_request(elastigroup)

        self.assertDictEqual(formatted_group_dict, self.mock_group_json)

