import json

none = "d3043820717d74d9a17694c176d39733"


# region Elastigroup
class Elastigroup:

    def __init__(
            self,
            name=none,
            description=none,
            region=none,
            capacity=none,
            strategy=none,
            compute=none,
            scaling=none,
            scheduling=none,
            multai=none,
            third_parties_integration=none):
        """

        :type name: str
        :type description: str
        :type region: str
        :type capacity: Capacity
        :type strategy: Strategy
        :type compute: Compute
        :type scaling: Scaling
        :type scheduling: Scheduling
        :type multai: Multai
        :type third_parties_integration: ThirdPartyIntegrations
        """
        self.name = name
        self.description = description
        self.region = region
        self.capacity = capacity
        self.strategy = strategy
        self.scaling = scaling
        self.scheduling = scheduling
        self.multai = multai
        self.third_parties_integration = third_parties_integration
        self.compute = compute


# endregion

# region Strategy
class Strategy:

    def __init__(
            self,
            availability_vs_cost=none,
            risk=none,
            utilize_reserved_instances=none,
            fallback_to_od=none,
            on_demand_count=none,
            draining_timeout=none,
            spin_up_time=none,
            lifetime_period=none,
            signals=none,
            scaling_strategy=none,
            persistence=none,
            revert_to_spot=none):
        """

        :type availability_vs_cost: str
        :type risk: int
        :type utilize_reserved_instances: bool
        :type fallback_to_od: bool
        :type on_demand_count: int
        :type draining_timeout: int
        :type spin_up_time: int
        :type lifetime_period: int
        :type signals: list[Signal]
        :type scaling_strategy: ScalingStrategy
        :type persistence: Persistence
        :type revert_to_spot: RevertToSpot
        """
        self.risk = risk
        self.utilize_reserved_instances = utilize_reserved_instances
        self.fallback_to_od = fallback_to_od
        self.on_demand_count = on_demand_count
        self.availability_vs_cost = availability_vs_cost
        self.draining_timeout = draining_timeout
        self.spin_up_time = spin_up_time
        self.lifetime_period = lifetime_period
        self.spin_up_time = spin_up_time
        self.signals = signals
        self.scaling_strategy = scaling_strategy
        self.persistence = persistence
        self.revert_to_spot = revert_to_spot


class Signal:

    def __init__(self, name=none, timeout=none):
        """

        :type name: str
        :type timeout: int
        """
        self.name = name
        self.timeout = timeout


class ScalingStrategy:
    def __init__(self, terminate_at_end_of_billing_hour):
        """

        :type terminate_at_end_of_billing_hour: bool
        """
        self.terminate_at_end_of_billing_hour = terminate_at_end_of_billing_hour


class Persistence:
    def __init__(
            self,
            should_persist_block_devices=none,
            should_persist_root_device=none,
            should_persist_private_ip=none,
            block_devices_mode=none):
        """

        :type should_persist_block_devices: bool
        :type should_persist_root_device: bool
        :type should_persist_private_ip: bool
        :type block_devices_mode: str
        """
        self.should_persist_block_devices = should_persist_block_devices
        self.should_persist_root_device = should_persist_root_device
        self.should_persist_private_ip = should_persist_private_ip
        self.block_devices_mode = block_devices_mode


class RevertToSpot:
    def __init__(self, perform_at=none, time_windows=none):
        """

        :type perform_at: str
        :type time_windows: list[str]
        """
        self.perform_at = perform_at
        self.time_windows = time_windows


# endregion

# region Capacity
class Capacity:
    def __init__(self, minimum=none, maximum=none, target=none, unit=none):
        """

        :type minimum: int
        :type maximum: int
        :type target: int
        :type unit: str
        """
        self.minimum = minimum
        self.maximum = maximum
        self.target = target
        self.unit = unit


# endregion

# region Scaling
class Scaling:
    def __init__(self, up=none, down=none, target=none):
        """

        :type up:  list[ScalingPolicy]
        :type down: list[ScalingPolicy]
        :type target: list[TargetTrackingPolicy]
        """
        self.up = up
        self.down = down
        self.target = target


class ScalingPolicyDimension:
    def __init__(self, name=none, value=none):
        """

        :type name: str
        :type value: str
        """
        self.name = name
        self.value = value


class ScalingPolicyAction:
    def __init__(self, type=none, adjustment=none, min_target_capacity=none,
                 max_target_capacity=none, target=none,
                 minimum=none,
                 maximum=none):
        """

        :type type: str
        :type adjustment: int
        :type min_target_capacity: int
        :type max_target_capacity: int
        :type target: int
        :type minimum: int
        :type maximum: int
        """
        self.type = type
        self.adjustment = adjustment
        self.min_target_capacity = min_target_capacity
        self.max_target_capacity = max_target_capacity
        self.target = target
        self.minimum = minimum
        self.maximum = maximum


class ScalingPolicy:
    def __init__(
            self,
            namespace=none,
            metric_name=none,
            statistic=none,
            evaluation_periods=none,
            period=none,
            threshold=none,
            cooldown=none,
            action=none,
            unit=none,
            operator=none,
            dimensions=none,
            policy_name=none,
            source=none,
            extended_statistic=none):
        """

        :type namespace: str
        :type metric_name: str
        :type statistic: str
        :type evaluation_periods: int
        :type period: int
        :type threshold: float
        :type cooldown: int
        :type action: ScalingPolicyAction
        :type unit: str
        :type operator: str
        :type dimensions: list[ScalingPolicyDimension]
        :type policy_name: str
        :type source: str
        :type extended_statistic: str
        """
        self.policy_name = policy_name
        self.namespace = namespace
        self.metric_name = metric_name
        self.dimensions = dimensions
        self.statistic = statistic
        self.evaluation_periods = evaluation_periods
        self.period = period
        self.threshold = threshold
        self.cooldown = cooldown
        self.action = action
        self.unit = unit
        self.operator = operator
        self.source = source
        self.extended_statistic = extended_statistic


class TargetTrackingPolicy:
    def __init__(self, namespace=none, metric_name=none, statistic=none,
                 cooldown=none, target=none, unit=none,
                 dimensions=none, policy_name=none, source=none):
        """

        :type namespace: str
        :type metric_name: str
        :type statistic: str
        :type cooldown: int
        :type target: int
        :type unit: str
        :type dimensions: list[ScalingPolicyDimension]
        :type policy_name: str
        :type source: str
        """
        self.policy_name = policy_name
        self.namespace = namespace
        self.source = source
        self.metric_name = metric_name
        self.dimensions = dimensions
        self.statistic = statistic
        self.unit = unit
        self.cooldown = cooldown
        self.target = target


# endregion

# region Scheduling
class Scheduling:
    def __init__(self, tasks=none):
        """

        :type tasks: list[ScheduledTask]
        """
        self.tasks = tasks


class ScheduledTask:
    def __init__(
            self,
            task_type=none,
            scale_target_capacity=none,
            scale_min_capacity=none,
            scale_max_capacity=none,
            target_capacity=none,
            min_capacity=none,
            max_capacity=none,
            batch_size_percentage=none,
            grace_period=none,
            adjustment=none,
            adjustment_percentage=none,
            is_enabled=none,
            frequency=none,
            cron_expression=none,
            start_time=none):
        """

        :type task_type: str
        :type scale_target_capacity: int
        :type scale_min_capacity: int
        :type scale_max_capacity: int
        :type target_capacity: int
        :type min_capacity: int
        :type max_capacity: int
        :type batch_size_percentage: int
        :type grace_period: int
        :type adjustment: int
        :type adjustment_percentage: int
        :type is_enabled: bool
        :type frequency: str
        :type cron_expression: str
        :type start_time: str
        """
        self.is_enabled = is_enabled
        self.frequency = frequency
        self.cron_expression = cron_expression
        self.task_type = task_type
        self.scale_target_capacity = scale_target_capacity
        self.scale_min_capacity = scale_min_capacity
        self.scale_max_capacity = scale_max_capacity
        self.target_capacity = target_capacity
        self.min_capacity = min_capacity
        self.max_capacity = max_capacity
        self.batch_size_percentage = batch_size_percentage
        self.grace_period = grace_period
        self.adjustment = adjustment
        self.adjustment_percentage = adjustment_percentage
        self.start_time = start_time


# endregion

# region Multai
class Multai:
    def __init__(self, token=none, balancers=none):
        """

        :type token: str
        :type balancers: str
        """
        self.token = token
        self.balancers = balancers


class MultaiLoadBalancer:
    def __init__(
            self,
            project_id=none,
            balancer_id=none,
            target_set_id=none,
            az_awareness=none,
            auto_weight=none):
        """

        :type project_id: str
        :type balancer_id: str
        :type target_set_id: str
        :type az_awareness: bool
        :type auto_weight: bool
        """
        self.project_id = project_id
        self.balancer_id = balancer_id
        self.target_set_id = target_set_id
        self.az_awareness = az_awareness
        self.auto_weight = auto_weight


# endregion

# region ThirdPartyIntegrations
class Rancher:

    def __init__(self, access_key=none, secret_key=none, master_host=none):
        """

        :type access_key: str
        :type secret_key: str
        :type master_host: str
        """
        self.access_key = access_key
        self.secret_key = secret_key
        self.master_host = master_host


class Mesosphere:
    def __init__(self, api_server=none):
        """

        :type api_server: str
        """
        self.api_server = api_server


class ElasticBeanstalk:
    def __init__(self, environment_id=none, deployment_preferences=none):
        """

        :type environment_id: str
        :type deployment_preferences: DeploymentPreferences
        """
        self.environment_id = environment_id
        self.deployment_preferences = deployment_preferences


class DeploymentPreferences:
    def __init__(
            self,
            automatic_roll=none,
            batch_size_percentage=none,
            grace_period=none,
            strategy=none):
        """

        :type automatic_roll: bool
        :type batch_size_percentage: int
        :type grace_period: int
        :type strategy: BeanstalkDeploymentStrategy
        """
        self.automatic_roll = automatic_roll
        self.batch_size_percentage = batch_size_percentage
        self.grace_period = grace_period
        self.strategy = strategy


class BeanstalkDeploymentStrategy:
    def __init__(self, action=none, should_drain_instances=none):
        """

        :type action: str
        :type should_drain_instances: bool
        """
        self.action = action
        self.should_drain_instances = should_drain_instances


class EcsConfiguration:
    def __init__(self, cluster_name=none, auto_scale=none):
        """

        :type cluster_name: str
        :type auto_scale: EcsAutoScaleConfiguration
        """
        self.cluster_name = cluster_name
        self.auto_scale = auto_scale


class EcsAutoScaleConfiguration:
    def __init__(
            self,
            is_enabled=none,
            is_auto_config=none,
            cooldown=none,
            headroom=none,
            attributes=none,
            down=none):
        """

        :type is_enabled: bool
        :type is_auto_config:  bool
        :type cooldown: int
        :type headroom: EcsAutoScalerHeadroomConfiguration
        :type attributes: list[EcsAutoScalerAttributeConfiguration]
        :type down: EcsAutoScalerDownConfiguration
        """
        self.is_enabled = is_enabled
        self.is_auto_config = is_auto_config
        self.cooldown = cooldown
        self.headroom = headroom
        self.attributes = attributes
        self.down = down


class EcsAutoScalerHeadroomConfiguration:
    def __init__(
            self,
            cpu_per_unit=none,
            memory_per_unit=none,
            num_of_units=none):
        """

        :type cpu_per_unit: int
        :type memory_per_unit: int
        :type num_of_units: int
        """
        self.cpu_per_unit = cpu_per_unit
        self.memory_per_unit = memory_per_unit
        self.num_of_units = num_of_units


class EcsAutoScalerAttributeConfiguration:
    def __init__(self, key=none, value=none):
        """

        :type key: str
        :type value: str
        """
        self.key = key
        self.value = value


class EcsAutoScalerDownConfiguration:
    def __init__(self, evaluation_periods=none):
        """

        :type evaluation_periods: int
        """
        self.evaluation_periods = evaluation_periods


class MlbRuntimeConfiguration:
    def __init__(self, deployment_id=none):
        """

        :type deployment_id: str
        """
        self.deployment_id = deployment_id


class KubernetesConfiguration:
    def __init__(
            self,
            api_server=none,
            token=none,
            integration_mode=none,
            cluster_identifier=none,
            auto_scale=none):
        """

        :type api_server: str
        :type token: str
        :type integration_mode: str
        :type cluster_identifier: str
        :type auto_scale: KubernetesAutoScalerConfiguration
        """
        self.api_server = api_server
        self.token = token
        self.integration_mode = integration_mode
        self.cluster_identifier = cluster_identifier
        self.auto_scale = auto_scale


class KubernetesAutoScalerConfiguration:
    def __init__(
            self,
            is_enabled=none,
            is_auto_config=none,
            cooldown=none,
            headroom=none,
            labels=none,
            down=none):
        """

        :type is_enabled: bool
        :type is_auto_config: bool
        :type cooldown: int
        :type headroom: KubernetesAutoScalerHeadroomConfiguration
        :type labels: KubernetesAutoScalerLabelsConfiguration
        :type down: KubernetesAutoScalerDownConfiguration
        """
        self.is_enabled = is_enabled
        self.is_auto_config = is_auto_config
        self.cooldown = cooldown
        self.headroom = headroom
        self.labels = labels
        self.down = down


class KubernetesAutoScalerHeadroomConfiguration:
    def __init__(
            self,
            cpu_per_unit=none,
            memory_per_unit=none,
            num_of_units=none):
        """

        :type cpu_per_unit: int
        :type memory_per_unit: int
        :type num_of_units: int
        """
        self.cpu_per_unit = cpu_per_unit
        self.memory_per_unit = memory_per_unit
        self.num_of_units = num_of_units


class KubernetesAutoScalerLabelsConfiguration:
    def __init__(self, key=none, value=none):
        """

        :type key: str
        :type value: str
        """
        self.key = key
        self.value = value


class KubernetesAutoScalerDownConfiguration:
    def __init__(self, evaluation_periods=none):
        """

        :type evaluation_periods: int
        """
        self.evaluation_periods = evaluation_periods


class RightScaleConfiguration:
    def __init__(self, account_id=none, refresh_token=none, region=none):
        """

        :type account_id: str
        :type refresh_token: str
        :type region: str
        """
        self.account_id = account_id
        self.refresh_token = refresh_token
        self.region = region


class OpsWorksConfiguration:
    def __init__(self, layer_id=none, stack_type=none):
        """

        :type layer_id: str
        :type stack_type: str
        """
        self.layer_id = layer_id
        self.stack_type = stack_type


class ChefConfiguration:
    def __init__(
            self,
            chef_server=none,
            organization=none,
            user=none,
            pem_key=none,
            chef_version=none):
        """

        :type chef_server: str
        :type organization: str
        :type user: str
        :type pem_key: str
        :type chef_version: str
        """
        self.chef_server = chef_server
        self.organization = organization
        self.user = user
        self.pem_key = pem_key
        self.chef_version = chef_version


class CodeDeployConfiguration:
    def __init__(
            self,
            deployment_groups=none,
            clean_up_on_failure=none,
            terminate_instance_on_failure=none):
        """

        :type deployment_groups: list[CodeDeployDeploymentGroupsConfiguration]
        :type clean_up_on_failure: bool
        :type terminate_instance_on_failure: bool
        """
        self.deployment_groups = deployment_groups
        self.clean_up_on_failure = clean_up_on_failure
        self.terminate_instance_on_failure = terminate_instance_on_failure


class CodeDeployDeploymentGroupsConfiguration:
    def __init__(self, application_name=none, deployment_group_name=none):
        """

        :type application_name: str
        :type deployment_group_name: str
        """
        self.application_name = application_name
        self.deployment_group_name = deployment_group_name


class NomadConfiguration:
    def __init__(
            self,
            master_host=none,
            master_port=none,
            acl_token=none,
            auto_scale=none):
        """

        :type master_host: str
        :type master_port: int
        :type acl_token: str
        :type auto_scale: NomadAutoScalerConfiguration
        """
        self.master_host = master_host
        self.master_port = master_port
        self.acl_token = acl_token
        self.auto_scale = auto_scale


class NomadAutoScalerConfiguration:
    def __init__(
            self,
            is_enabled=none,
            cooldown=none,
            headroom=none,
            constraints=none,
            down=none):
        """

        :type is_enabled: bool
        :type cooldown: int
        :type headroom: NomadAutoScalerHeadroomConfiguration
        :type constraints: list[NomadAutoScalerConstraintsConfiguration]
        :type down: NomadAutoScalerDownConfiguration
        """
        self.is_enabled = is_enabled
        self.cooldown = cooldown
        self.headroom = headroom
        self.constraints = constraints
        self.down = down


class NomadAutoScalerHeadroomConfiguration:
    def __init__(
            self,
            cpu_per_unit=none,
            memory_per_unit=none,
            num_of_units=none):
        """

        :type cpu_per_unit: int
        :type memory_per_unit: int
        :type num_of_units: int
        """
        self.cpu_per_unit = cpu_per_unit
        self.memory_per_unit = memory_per_unit
        self.num_of_units = num_of_units


class NomadAutoScalerConstraintsConfiguration:
    def __init__(self, key=none, value=none):
        """

        :type key: str
        :type value: str
        """
        self.key = key
        self.value = value


class NomadAutoScalerDownConfiguration:
    def __init__(self, evaluation_periods=none):
        """

        :type evaluation_periods: int
        """
        self.evaluation_periods = evaluation_periods


class DockerSwarmConfiguration:
    def __init__(self, master_host=none, master_port=none, auto_scale=none):
        """

        :type master_host: str
        :type master_port: int
        :type auto_scale: DockerSwarmAutoScalerConfiguration
        """
        self.master_host = master_host
        self.master_port = master_port
        self.auto_scale = auto_scale


class DockerSwarmAutoScalerConfiguration:
    def __init__(
            self,
            is_enabled=none,
            cooldown=none,
            headroom=none,
            down=none):
        """

        :type is_enabled: bool
        :type cooldown: int
        :type headroom: DockerSwarmAutoScalerHeadroomConfiguration
        :type down: DockerSwarmAutoScalerDownConfiguration
        """
        self.is_enabled = is_enabled
        self.cooldown = cooldown
        self.headroom = headroom
        self.down = down


class DockerSwarmAutoScalerHeadroomConfiguration:
    def __init__(
            self,
            cpu_per_unit=none,
            memory_per_unit=none,
            num_of_units=none):
        """

        :type cpu_per_unit: int
        :type memory_per_unit:
        :type num_of_units: int
        """
        self.cpu_per_unit = cpu_per_unit
        self.memory_per_unit = memory_per_unit
        self.num_of_units = num_of_units


class DockerSwarmAutoScalerDownConfiguration:
    def __init__(self, evaluation_periods=none):
        """

        :type evaluation_periods: int
        """
        self.evaluation_periods = evaluation_periods


class Route53Configuration:
    def __init__(self, domains=none):
        """

        :type domains: list[Route53DomainsConfiguration]
        """
        self.domains = domains


class Route53DomainsConfiguration:
    def __init__(self, hosted_zone_id=none, record_sets=none):
        """

        :type hosted_zone_id: str
        :type record_sets: list[Route53RecordSetsConfiguration]
        """
        self.hosted_zone_id = hosted_zone_id
        self.record_sets = record_sets


class Route53RecordSetsConfiguration:
    def __init__(self, name=none, use_public_ip=none):
        """

        :type name: str
        :type use_public_ip: bool
        """
        self.name = name
        self.use_public_ip = use_public_ip


class ThirdPartyIntegrations:
    def __init__(
            self,
            rancher=none,
            mesosphere=none,
            elastic_beanstalk=none,
            ecs=none,
            kubernetes=none,
            right_scale=none,
            ops_works=none,
            chef=none,
            mlb_runtime=none,
            code_deploy=none,
            nomad=none,
            docker_swarm=none,
            route53=none):
        """

        :type rancher: Rancher
        :type mesosphere: Mesosphere
        :type elastic_beanstalk: ElasticBeanstalk
        :type ecs: EcsConfiguration
        :type kubernetes: KubernetesConfiguration
        :type right_scale: RightScaleConfiguration
        :type ops_works: OpsWorksConfiguration
        :type chef: ChefConfiguration
        :type mlb_runtime: MlbRuntimeConfiguration
        :type code_deploy: CodeDeployConfiguration
        :type nomad: NomadConfiguration
        :type docker_swarm: DockerSwarmConfiguration
        :type route53: Route53Configuration
        """
        self.rancher = rancher
        self.mesosphere = mesosphere
        self.elastic_beanstalk = elastic_beanstalk
        self.ecs = ecs
        self.kubernetes = kubernetes
        self.right_scale = right_scale
        self.ops_works = ops_works
        self.chef = chef
        self.mlb_runtime = mlb_runtime
        self.code_deploy = code_deploy
        self.nomad = nomad
        self.docker_swarm = docker_swarm
        self.route53 = route53


# endregion

# region Compute
class Compute:
    def __init__(
            self,
            launch_specification=none,
            instance_types=none,
            product=none,
            availability_zones=none,
            elastic_ips=none,
            private_ips=none,
            subnet_ids=none,
            preferred_availability_zones=none):
        """

        :type launch_specification: LaunchSpecification
        :type instance_types: InstanceTypes
        :type product: str
        :type availability_zones: list[AvailabilityZone]
        :type elastic_ips: list[str]
        :type private_ips: list[str]
        :type subnet_ids: list[str]
        :type preferred_availability_zones: list[str]
        """
        self.elastic_ips = elastic_ips
        self.private_ips = private_ips
        self.subnet_ids = subnet_ids
        self.instance_types = instance_types
        self.availability_zones = availability_zones
        self.product = product
        self.launch_specification = launch_specification
        self.preferred_availability_zones = preferred_availability_zones


class AvailabilityZone:
    def __init__(
            self,
            name=none,
            subnet_id=none,
            subnet_ids=none,
            placement_group_name=none):
        """

        :type name:
        :type subnet_id:
        :type subnet_ids:
        :type placement_group_name:
        """
        self.name = name
        self.subnet_id = subnet_id
        self.subnet_ids = subnet_ids
        self.placement_group_name = placement_group_name


class InstanceTypes:
    def __init__(
            self,
            ondemand=none,
            spot=none,
            weights=none,
            preferred_spot=none):
        """

        :type ondemand: str
        :type spot: list[str]
        :type weights: list[Weight]
        :type preferred_spot: list[str]
        """
        self.ondemand = ondemand
        self.spot = spot
        self.weights = weights
        self.preferred_spot = preferred_spot


class Weight:
    def __init__(self, instance_type=none, weighted_capacity=none):
        """

        :type instance_type: str
        :type weighted_capacity: int
        """
        self.instance_type = instance_type
        self.weighted_capacity = weighted_capacity


class LaunchSpecification:
    def __init__(
            self,
            security_group_ids=none,
            image_id=none,
            monitoring=none,
            health_check_type=none,
            load_balancers_config=none,
            health_check_grace_period=none,
            health_check_unhealthy_duration_before_replacement=none,
            ebs_optimized=none,
            tenancy=none,
            iam_role=none,
            key_pair=none,
            user_data=none,
            shutdown_script=none,
            block_device_mappings=none,
            network_interfaces=none,
            tags=none):
        """

        :type security_group_ids: list[str]
        :type image_id: str
        :type monitoring: bool
        :type health_check_type: str
        :type load_balancers_config:  LoadBalancersConfig
        :type health_check_grace_period: int
        :type health_check_unhealthy_duration_before_replacement: int
        :type ebs_optimized: bool
        :type tenancy: str
        :type iam_role: list[IamRole]
        :type key_pair: str
        :type user_data: str
        :type shutdown_script: str
        :type block_device_mappings: list[BlockDeviceMapping]
        :type network_interfaces: list[NetworkInterface]
        :type tags: list[Tag]
        """
        self.load_balancers_config = load_balancers_config
        self.health_check_type = health_check_type
        self.health_check_grace_period = health_check_grace_period
        self.health_check_unhealthy_duration_before_replacement = health_check_unhealthy_duration_before_replacement
        self.security_group_ids = security_group_ids
        self.monitoring = monitoring
        self.ebs_optimized = ebs_optimized
        self.image_id = image_id
        self.tenancy = tenancy
        self.iam_role = iam_role
        self.key_pair = key_pair
        self.user_data = user_data
        self.shutdown_script = shutdown_script
        self.block_device_mappings = block_device_mappings
        self.network_interfaces = network_interfaces
        self.tags = tags


class LoadBalancersConfig:
    def __init__(self, load_balancers=none):
        """

        :type load_balancers: list[LoadBalancer]
        """
        self.load_balancers = load_balancers


class LoadBalancer:
    def __init__(
            self,
            type=none,
            arn=none,
            name=none,
            target_set_id=none,
            balancer_id=none,
            auto_weight=none,
            az_awareness=none):
        """

        :type type: str
        :type arn: str
        :type name: str
        :type target_set_id: str
        :type balancer_id: str
        :type auto_weight: bool
        :type az_awareness: bool

        """
        self.type = type
        self.arn = arn
        self.name = name
        self.target_set_id = target_set_id
        self.balancer_id = balancer_id
        self.auto_weight = auto_weight
        self.az_awareness = az_awareness


class IamRole:
    def __init__(self, name=none, arn=none):
        """

        :type name: str
        :type arn: str
        """
        self.name = name
        self.arn = arn


class BlockDeviceMapping:
    def __init__(
            self,
            device_name=none,
            ebs=none,
            no_device=none,
            virtual_name=none):
        """

        :type device_name: str
        :type ebs: list[EBS]
        :type no_device: bool
        :type virtual_name: str
        """
        self.device_name = device_name
        self.ebs = ebs
        self.no_device = no_device
        self.virtual_name = virtual_name


class EBS:
    def __init__(
            self,
            delete_on_termination=none,
            encrypted=none,
            iops=none,
            snapshot_id=none,
            volume_size=none,
            volume_type=none,
            kms_key_id=none):
        """

        :type delete_on_termination: bool
        :type encrypted: bool
        :type iops: int
        :type snapshot_id: str
        :type volume_size: int
        :type volume_type: str
        :type kms_key_id: str
        """
        self.delete_on_termination = delete_on_termination
        self.encrypted = encrypted
        self.iops = iops
        self.snapshot_id = snapshot_id
        self.volume_size = volume_size
        self.volume_type = volume_type
        self.kms_key_id = kms_key_id


class Tag:
    def __init__(self, tag_key=none, tag_value=none):
        """

        :type tag_key: str
        :type tag_value: str
        """
        self.tag_key = tag_key
        self.tag_value = tag_value


class NetworkInterface:
    def __init__(
            self,
            delete_on_termination=none,
            device_index=none,
            description=none,
            secondary_private_ip_address_count=none,
            associate_public_ip_address=none,
            groups=none,
            network_interface_id=none,
            private_ip_address=none,
            private_ip_addresses=none,
            subnet_id=none,
            associate_ipv6_address=none):
        """

        :type delete_on_termination: bool
        :type device_index: int
        :type description: str
        :type secondary_private_ip_address_count: int
        :type associate_public_ip_address: bool
        :type groups: list[str]
        :type network_interface_id: str
        :type private_ip_address: str
        :type private_ip_addresses: PrivateIpAddress
        :type subnet_id: str
        :type associate_ipv6_address: str
        """
        self.description = description
        self.device_index = device_index
        self.secondary_private_ip_address_count = secondary_private_ip_address_count
        self.associate_public_ip_address = associate_public_ip_address
        self.delete_on_termination = delete_on_termination
        self.groups = groups
        self.network_interface_id = network_interface_id
        self.private_ip_address = private_ip_address
        self.private_ip_addresses = private_ip_addresses
        self.subnet_id = subnet_id
        self.associate_ipv6_address = associate_ipv6_address


class PrivateIpAddress:
    def __init__(self, private_ip_address=none, primary=none):
        """

        :type private_ip_address: str
        :type primary: bool
        """
        self.private_ip_address = private_ip_address
        self.primary = primary


# endregion

class Roll:
    def __init__(
            self,
            batch_size_percentage=none,
            grace_period=none,
            health_check_type=none,
            strategy=none):
        self.batch_size_percentage = batch_size_percentage
        self.grace_period = grace_period
        self.health_check_type = health_check_type
        self.strategy = strategy


class DetachConfiguration:
    def __init__(
            self,
            instances_to_detach=none,
            should_terminate_instances=none,
            draining_timeout=none,
            should_decrement_target_capacity=none):
        self.instances_to_detach = instances_to_detach
        self.should_terminate_instances = should_terminate_instances
        self.draining_timeout = draining_timeout
        self.should_decrement_target_capacity = should_decrement_target_capacity


class StatefulDeallocation:
    def __init__(
            self,
            should_delete_images=none,
            should_delete_network_interfaces=none,
            should_delete_volumes=none,
            should_delete_snapshots=none):
        self.should_delete_images = should_delete_images
        self.should_delete_network_interfaces = should_delete_network_interfaces
        self.should_delete_volumes = should_delete_volumes
        self.should_delete_snapshots = should_delete_snapshots


class ElastigroupCreationRequest:
    def __init__(self, elastigroup):
        self.group = elastigroup

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class ElastigroupDeletionRequest:
    def __init__(self, stateful_deallocation):
        self.stateful_deallocation = stateful_deallocation

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class ElastigroupUpdateRequest:
    def __init__(self, elastigroup):
        self.group = elastigroup

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class ElastigroupRollRequest:
    def __init__(self, group_roll):
        self.batch_size_percentage = group_roll.batch_size_percentage
        self.grace_period = group_roll.grace_period
        self.health_check_type = group_roll.health_check_type
        self.strategy = group_roll.strategy

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class ElastigroupDetachInstancesRequest:
    def __init__(self, detach_configuration):
        self.should_decrement_target_capacity = detach_configuration.should_decrement_target_capacity
        self.draining_timeout = detach_configuration.draining_timeout
        self.instances_to_detach = detach_configuration.instances_to_detach
        self.should_terminate_instances = detach_configuration.should_terminate_instances

    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=4)
