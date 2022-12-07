import json

none = "d3043820717d74d9a17694c176d39733"


# region Elastigroup
class Elastigroup:
    """
    # Arguments
    name: str
    description: str
    region: str
    capacity: Capacity
    strategy: Strategy
    compute: Compute
    scaling: Scaling
    scheduling: Scheduling
    multai: Multai
    third_parties_integration: ThirdPartyIntegrations
    """
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
    """
    # Arguments
    availability_vs_cost: str
    risk: int
    utilize_commitments: bool
    utilize_reserved_instances: bool
    fallback_to_od: bool
    on_demand_count: int
    draining_timeout: int
    spin_up_time: int
    lifetime_period: int
    signals: list[Signal]
    scaling_strategy: ScalingStrategy
    persistence: Persistence
    revert_to_spot: RevertToSpot
    """
    def __init__(
            self,
            availability_vs_cost=none,
            risk=none,
            utilize_commitments=none,
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

        self.risk = risk
        self.utilize_commitments = utilize_commitments
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
    """
    # Arguments
    name: str
    timeout: int
    """
    def __init__(self, name=none, timeout=none):

        self.name = name
        self.timeout = timeout


class ScalingStrategy:
    """
    # Arguments
    terminate_at_end_of_billing_hour: bool
    terminationPolicy: str
    """
    def __init__(self, terminate_at_end_of_billing_hour=none, terminationPolicy=none):

        self.terminate_at_end_of_billing_hour = terminate_at_end_of_billing_hour
        self.terminationPolicy = terminationPolicy


class Persistence:
    """
    # Arguments
    should_persist_block_devices: bool
    should_persist_root_device: bool
    should_persist_private_ip: bool
    block_devices_mode: str
    """
    def __init__(
            self,
            should_persist_block_devices=none,
            should_persist_root_device=none,
            should_persist_private_ip=none,
            block_devices_mode=none):

        self.should_persist_block_devices = should_persist_block_devices
        self.should_persist_root_device = should_persist_root_device
        self.should_persist_private_ip = should_persist_private_ip
        self.block_devices_mode = block_devices_mode


class RevertToSpot:
    """
    # Arguments
    perform_at: str
    time_windows: list[str]
    """
    def __init__(self, perform_at=none, time_windows=none):

        self.perform_at = perform_at
        self.time_windows = time_windows


# endregion

# region Capacity
class Capacity:
    """
    # Arguments
    minimum: int
    maximum: int
    target: int
    unit: str
    """
    def __init__(self, minimum=none, maximum=none, target=none, unit=none):

        self.minimum = minimum
        self.maximum = maximum
        self.target = target
        self.unit = unit


# endregion

# region Scaling
class Scaling:
    """
    # Arguments
    up:  list[ScalingPolicy]
    down: list[ScalingPolicy]
    target: list[TargetTrackingPolicy]
    multiple_metrics: MultipleMetrics
    """
    def __init__(self, up=none, down=none, target=none, multiple_metrics=none):

        self.up = up
        self.down = down
        self.target = target
        self.multiple_metrics = multiple_metrics


class ScalingPolicyDimension:
    """
    # Arguments
    name: str
    value: str
    """
    def __init__(self, name=none, value=none):

        self.name = name
        self.value = value


class ScalingPolicyAction:
    """
    # Arguments
    type: str
    adjustment: int
    min_target_capacity: int
    max_target_capacity: int
    target: int
    minimum: int
    maximum: int
    """
    def __init__(self, type=none, adjustment=none, min_target_capacity=none,
                 max_target_capacity=none, target=none,
                 minimum=none,
                 maximum=none):

        self.type = type
        self.adjustment = adjustment
        self.min_target_capacity = min_target_capacity
        self.max_target_capacity = max_target_capacity
        self.target = target
        self.minimum = minimum
        self.maximum = maximum


class ScalingPolicyStepAdjustment:
    """
    # Arguments
    action: ScalingPolicyAction
    threshold: int
    """
    def __init__(self, action=none, threshold=none):

        self.action = action
        self.threshold = threshold


class ScalingPolicy:
    """
    # Arguments
    namespace: str
    metric_name: str
    statistic: str
    evaluation_periods: int
    period: int
    threshold: float
    cooldown: int
    action: ScalingPolicyAction
    unit: str
    operator: str
    dimensions: list[ScalingPolicyDimension]
    policy_name: str
    source: str
    extended_statistic: str
    step_adjustments: list[ScalingPolicyStepAdjustment]
    min_target_capacity: int
    max_target_capacity: int
    should_resume_stateful: bool
    is_enabled: bool
    """
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
            extended_statistic=none,
            step_adjustments=none,
            min_target_capacity=none,
            max_target_capacity=none,
            should_resume_stateful=none,
            is_enabled=none):

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
        self.step_adjustments = step_adjustments
        self.min_target_capacity = min_target_capacity
        self.max_target_capacity = max_target_capacity
        self.should_resume_stateful = should_resume_stateful
        self.is_enabled = is_enabled


class TargetTrackingPolicy:
    """
    # Arguments
    namespace: str
    metric_name: str
    statistic: str
    cooldown: int
    target: int
    unit: str
    dimensions: list[ScalingPolicyDimension]
    policy_name: str
    source: str
    """
    def __init__(self, namespace=none, metric_name=none, statistic=none,
                 cooldown=none, target=none, unit=none,
                 dimensions=none, policy_name=none, source=none):

        self.policy_name = policy_name
        self.namespace = namespace
        self.source = source
        self.metric_name = metric_name
        self.dimensions = dimensions
        self.statistic = statistic
        self.unit = unit
        self.cooldown = cooldown
        self.target = target


class ScalingPolicyMetric:
    """
    # Arguments
    name: str
    metric_name: str
    name_space: str
    statistic: str
    unit: str
    dimensions: list[ScalingPolicyDimension]
    extended_statistic: str
    """
    def __init__(
            self,
            name=none,
            namespace=none,
            metric_name=none,
            statistic=none,
            unit=none,
            dimensions=none,
            extended_statistic=none):

        self.name = name
        self.namespace = namespace
        self.metric_name = metric_name
        self.dimensions = dimensions
        self.statistic = statistic
        self.unit = unit
        self.extended_statistic = extended_statistic


class MetricExpression:
    """
    # Arguments
    name: str
    expression: str
    """
    def __init__(self, name=none, expression=none):

        self.name = name
        self.expression = expression


class MultipleMetrics:
    """
    # Arguments
    metrics: list[ScalingPolicyMetric]
    expressions: list[MetricExpression]
    """
    def __init__(self, metrics=none, expressions=none):

        self.metrics = metrics
        self.expressions = expressions

# endregion

# region Scheduling
class Scheduling:
    """
    # Arguments
    tasks: list[ScheduledTask]
    """
    def __init__(self, tasks=none):

        self.tasks = tasks


class ScheduledTask:
    """
    # Arguments
    task_type: str
    scale_target_capacity: int
    scale_min_capacity: int
    scale_max_capacity: int
    target_capacity: int
    min_capacity: int
    max_capacity: int
    batch_size_percentage: int
    grace_period: int
    adjustment: int
    adjustment_percentage: int
    is_enabled: bool
    frequency: str
    cron_expression: str
    start_time: str
    """
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
    """
    # Arguments
    token: str
    balancers: str
    """
    def __init__(self, token=none, balancers=none):

        self.token = token
        self.balancers = balancers


class MultaiLoadBalancer:
    """
    # Arguments
    project_id: str
    balancer_id: str
    target_set_id: str
    az_awareness: bool
    auto_weight: bool
    """
    def __init__(
            self,
            project_id=none,
            balancer_id=none,
            target_set_id=none,
            az_awareness=none,
            auto_weight=none):

        self.project_id = project_id
        self.balancer_id = balancer_id
        self.target_set_id = target_set_id
        self.az_awareness = az_awareness
        self.auto_weight = auto_weight


# endregion

# region ThirdPartyIntegrations
class Rancher:
    """
    # Arguments
    access_key: str
    secret_key: str
    master_host: str
    version: str
    """
    def __init__(self, access_key=none, secret_key=none, master_host=none, version=none):

        self.access_key = access_key
        self.secret_key = secret_key
        self.master_host = master_host
        self.version = version


class Mesosphere:
    """
    # Arguments
    api_server: str
    """
    def __init__(self, api_server=none):

        self.api_server = api_server


class ElasticBeanstalk:
    """
    # Arguments
    environment_id: str
    managed_actions: ManagedActions
    deployment_preferences: DeploymentPreferences
    """
    def __init__(self, environment_id=none, managed_actions=none, deployment_preferences=none):

        self.environment_id = environment_id
        self.managed_actions = managed_actions
        self.deployment_preferences = deployment_preferences


class ManagedActions:
    """
    # Arguments
    platform_update: PlatformUpdate
    """
    def __init__(self, platform_update=none):

        self.platform_update = platform_update


class PlatformUpdate:
    """
    # Arguments
    perform_at: str
    time_window: str
    update_level: str
    """
    def __init__(
        self,
        perform_at=none,
        time_window=none,
        update_level=none):

        self.perform_at = perform_at
        self.time_window = time_window
        self.update_level = update_level


class DeploymentPreferences:
    """
    # Arguments
    automatic_roll: bool
    batch_size_percentage: int
    grace_period: int
    strategy: BeanstalkDeploymentStrategy
    """
    def __init__(
            self,
            automatic_roll=none,
            batch_size_percentage=none,
            grace_period=none,
            strategy=none):

        self.automatic_roll = automatic_roll
        self.batch_size_percentage = batch_size_percentage
        self.grace_period = grace_period
        self.strategy = strategy


class BeanstalkDeploymentStrategy:
    """
    # Arguments
    action: str
    should_drain_instances: bool
    """
    def __init__(self, action=none, should_drain_instances=none):

        self.action = action
        self.should_drain_instances = should_drain_instances


class EcsConfiguration:
    """
    # Arguments
    cluster_name: str
    auto_scale: EcsAutoScaleConfiguration
    """
    def __init__(self, cluster_name=none, auto_scale=none):

        self.cluster_name = cluster_name
        self.auto_scale = auto_scale


class EcsAutoScaleConfiguration:
    """
    # Arguments
    is_enabled: bool
    is_auto_config:  bool
    cooldown: int
    headroom: EcsAutoScalerHeadroomConfiguration
    attributes: list[EcsAutoScalerAttributeConfiguration]
    down: EcsAutoScalerDownConfiguration
    """
    def __init__(
            self,
            is_enabled=none,
            is_auto_config=none,
            cooldown=none,
            headroom=none,
            attributes=none,
            down=none):

        self.is_enabled = is_enabled
        self.is_auto_config = is_auto_config
        self.cooldown = cooldown
        self.headroom = headroom
        self.attributes = attributes
        self.down = down


class EcsAutoScalerHeadroomConfiguration:
    """
    # Arguments
    cpu_per_unit: int
    memory_per_unit: int
    num_of_units: int
    """
    def __init__(
            self,
            cpu_per_unit=none,
            memory_per_unit=none,
            num_of_units=none):

        self.cpu_per_unit = cpu_per_unit
        self.memory_per_unit = memory_per_unit
        self.num_of_units = num_of_units


class EcsAutoScalerAttributeConfiguration:
    """
    # Arguments
    key: str
    value: str
    """
    def __init__(self, key=none, value=none):

        self.key = key
        self.value = value


class EcsAutoScalerDownConfiguration:
    """
    # Arguments
    evaluation_periods: int
    """
    def __init__(self, evaluation_periods=none):

        self.evaluation_periods = evaluation_periods


class MlbRuntimeConfiguration:
    """
    # Arguments
    deployment_id: str
    """
    def __init__(self, deployment_id=none):

        self.deployment_id = deployment_id


class KubernetesConfiguration:
    """
    # Arguments
    api_server: str
    token: str
    integration_mode: str
    cluster_identifier: str
    auto_scale: KubernetesAutoScalerConfiguration
    """
    def __init__(
            self,
            api_server=none,
            token=none,
            integration_mode=none,
            cluster_identifier=none,
            auto_scale=none):

        self.api_server = api_server
        self.token = token
        self.integration_mode = integration_mode
        self.cluster_identifier = cluster_identifier
        self.auto_scale = auto_scale


class KubernetesAutoScalerConfiguration:
    """
    # Arguments
    is_enabled: bool
    is_auto_config: bool
    cooldown: int
    headroom: KubernetesAutoScalerHeadroomConfiguration
    labels: KubernetesAutoScalerLabelsConfiguration
    down: KubernetesAutoScalerDownConfiguration
    """
    def __init__(
            self,
            is_enabled=none,
            is_auto_config=none,
            cooldown=none,
            headroom=none,
            labels=none,
            down=none):

        self.is_enabled = is_enabled
        self.is_auto_config = is_auto_config
        self.cooldown = cooldown
        self.headroom = headroom
        self.labels = labels
        self.down = down


class KubernetesAutoScalerHeadroomConfiguration:
    """
    # Arguments
    cpu_per_unit: int
    memory_per_unit: int
    num_of_units: int
    """
    def __init__(
            self,
            cpu_per_unit=none,
            memory_per_unit=none,
            num_of_units=none):

        self.cpu_per_unit = cpu_per_unit
        self.memory_per_unit = memory_per_unit
        self.num_of_units = num_of_units


class KubernetesAutoScalerLabelsConfiguration:
    """
    # Arguments
    key: str
    value: str
    """
    def __init__(self, key=none, value=none):

        self.key = key
        self.value = value


class KubernetesAutoScalerDownConfiguration:
    """
    # Arguments
    evaluation_periods: int
    """
    def __init__(self, evaluation_periods=none):
        self.evaluation_periods = evaluation_periods


class RightScaleConfiguration:
    """
    # Arguments
    account_id: str
    refresh_token: str
    region: str
    """
    def __init__(self, account_id=none, refresh_token=none, region=none):

        self.account_id = account_id
        self.refresh_token = refresh_token
        self.region = region


class OpsWorksConfiguration:
    """
    # Arguments
    layer_id: str
    stack_type: str
    """
    def __init__(self, layer_id=none, stack_type=none):

        self.layer_id = layer_id
        self.stack_type = stack_type


class ChefConfiguration:
    """
    # Arguments
    chef_server: str
    organization: str
    user: str
    pem_key: str
    chef_version: str
    """
    def __init__(
            self,
            chef_server=none,
            organization=none,
            user=none,
            pem_key=none,
            chef_version=none):

        self.chef_server = chef_server
        self.organization = organization
        self.user = user
        self.pem_key = pem_key
        self.chef_version = chef_version


class CodeDeployConfiguration:
    """
    # Arguments
    deployment_groups: list[CodeDeployDeploymentGroupsConfiguration]
    clean_up_on_failure: bool
    terminate_instance_on_failure: bool
    """
    def __init__(
            self,
            deployment_groups=none,
            clean_up_on_failure=none,
            terminate_instance_on_failure=none):

        self.deployment_groups = deployment_groups
        self.clean_up_on_failure = clean_up_on_failure
        self.terminate_instance_on_failure = terminate_instance_on_failure


class CodeDeployDeploymentGroupsConfiguration:
    """
    # Arguments
    application_name: str
    deployment_group_name: str
    """
    def __init__(self, application_name=none, deployment_group_name=none):

        self.application_name = application_name
        self.deployment_group_name = deployment_group_name


class NomadConfiguration:
    """
    # Arguments
    master_host: str
    master_port: int
    acl_token: str
    auto_scale: NomadAutoScalerConfiguration
    """
    def __init__(
            self,
            master_host=none,
            master_port=none,
            acl_token=none,
            auto_scale=none):

        self.master_host = master_host
        self.master_port = master_port
        self.acl_token = acl_token
        self.auto_scale = auto_scale


class NomadAutoScalerConfiguration:
    """
    # Arguments
    is_enabled: bool
    cooldown: int
    headroom: NomadAutoScalerHeadroomConfiguration
    constraints: list[NomadAutoScalerConstraintsConfiguration]
    down: NomadAutoScalerDownConfiguration
    """
    def __init__(
            self,
            is_enabled=none,
            cooldown=none,
            headroom=none,
            constraints=none,
            down=none):

        self.is_enabled = is_enabled
        self.cooldown = cooldown
        self.headroom = headroom
        self.constraints = constraints
        self.down = down


class NomadAutoScalerHeadroomConfiguration:
    """
    # Arguments
    cpu_per_unit: int
    memory_per_unit: int
    num_of_units: int
    """
    def __init__(
            self,
            cpu_per_unit=none,
            memory_per_unit=none,
            num_of_units=none):

        self.cpu_per_unit = cpu_per_unit
        self.memory_per_unit = memory_per_unit
        self.num_of_units = num_of_units


class NomadAutoScalerConstraintsConfiguration:
    """
    # Arguments
    key: str
    value: str
    """
    def __init__(self, key=none, value=none):

        self.key = key
        self.value = value


class NomadAutoScalerDownConfiguration:
    """
    # Arguments
    evaluation_periods: int
    """
    def __init__(self, evaluation_periods=none):

        self.evaluation_periods = evaluation_periods


class DockerSwarmConfiguration:
    """
    # Arguments
    master_host: str
    master_port: int
    auto_scale: DockerSwarmAutoScalerConfiguration
    """
    def __init__(self, master_host=none, master_port=none, auto_scale=none):

        self.master_host = master_host
        self.master_port = master_port
        self.auto_scale = auto_scale


class DockerSwarmAutoScalerConfiguration:
    """
    # Arguments
    is_enabled: bool
    cooldown: int
    headroom: DockerSwarmAutoScalerHeadroomConfiguration
    down: DockerSwarmAutoScalerDownConfiguration
    """
    def __init__(
            self,
            is_enabled=none,
            cooldown=none,
            headroom=none,
            down=none):

        self.is_enabled = is_enabled
        self.cooldown = cooldown
        self.headroom = headroom
        self.down = down


class DockerSwarmAutoScalerHeadroomConfiguration:
    """
    # Arguments
    cpu_per_unit: int
    memory_per_unit:
    num_of_units: int
    """
    def __init__(
            self,
            cpu_per_unit=none,
            memory_per_unit=none,
            num_of_units=none):

        self.cpu_per_unit = cpu_per_unit
        self.memory_per_unit = memory_per_unit
        self.num_of_units = num_of_units


class DockerSwarmAutoScalerDownConfiguration:
    """
    # Arguments
    evaluation_periods: int
    """
    def __init__(self, evaluation_periods=none):

        self.evaluation_periods = evaluation_periods


class Route53Configuration:
    """
    # Arguments
    domains: list[Route53DomainsConfiguration]
    """
    def __init__(self, domains=none):

        self.domains = domains


class Route53DomainsConfiguration:
    """
    # Arguments
    hosted_zone_id: str
    record_sets: list[Route53RecordSetsConfiguration]
    """
    def __init__(self, hosted_zone_id=none, record_sets=none):

        self.hosted_zone_id = hosted_zone_id
        self.record_sets = record_sets


class Route53RecordSetsConfiguration:
    """
    # Arguments
    name: str
    use_public_ip: bool
    """
    def __init__(self, name=none, use_public_ip=none):

        self.name = name
        self.use_public_ip = use_public_ip


class ThirdPartyIntegrations:
    """
    # Arguments
    rancher: Rancher
    mesosphere: Mesosphere
    elastic_beanstalk: ElasticBeanstalk
    ecs: EcsConfiguration
    kubernetes: KubernetesConfiguration
    right_scale: RightScaleConfiguration
    ops_works: OpsWorksConfiguration
    chef: ChefConfiguration
    mlb_runtime: MlbRuntimeConfiguration
    code_deploy: CodeDeployConfiguration
    nomad: NomadConfiguration
    docker_swarm: DockerSwarmConfiguration
    route53: Route53Configuration
    """
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
    """
    # Arguments
    launch_specification: LaunchSpecification
    instance_types: InstanceTypes
    product: str
    availability_zones: list[AvailabilityZone]
    elastic_ips: list[str]
    private_ips: list[str]
    subnet_ids: list[str]
    preferred_availability_zones: list[str]
    """
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

        self.elastic_ips = elastic_ips
        self.private_ips = private_ips
        self.subnet_ids = subnet_ids
        self.instance_types = instance_types
        self.availability_zones = availability_zones
        self.product = product
        self.launch_specification = launch_specification
        self.preferred_availability_zones = preferred_availability_zones


class AvailabilityZone:
    """
    # Aerguments
    name:
    subnet_id:
    subnet_ids:
    placement_group_name:
    """
    def __init__(
            self,
            name=none,
            subnet_id=none,
            subnet_ids=none,
            placement_group_name=none):

        self.name = name
        self.subnet_id = subnet_id
        self.subnet_ids = subnet_ids
        self.placement_group_name = placement_group_name


class InstanceTypes:
    """
    # Arguments
    ondemand: str
    spot: list[str]
    weights: list[Weight]
    preferred_spot: list[str]
    """
    def __init__(
            self,
            ondemand=none,
            spot=none,
            weights=none,
            preferred_spot=none):

        self.ondemand = ondemand
        self.spot = spot
        self.weights = weights
        self.preferred_spot = preferred_spot


class Weight:
    """
    # Arguments
    instance_type: str
    weighted_capacity: int
    """
    def __init__(self, instance_type=none, weighted_capacity=none):

        self.instance_type = instance_type
        self.weighted_capacity = weighted_capacity


class TagSpecification:
    """
    # Arguments
    should_tag: bool
    """
    def __init__(self, should_tag: bool = none):
        self.should_tag = should_tag


class ResourceTagSpecification:
    """
    # Arguments
    volumes: TagSpecification
    snapshots: TagSpecification
    enis: TagSpecification
    amis: TagSpecification
    """
    def __init__(self, volumes: TagSpecification = none, snapshots: TagSpecification = none, enis: TagSpecification = none,
                 amis: TagSpecification = none):
        self.volumes = volumes
        self.snapshots = snapshots
        self.enis = enis
        self.amis = amis


class LaunchSpecification:
    """
    # Arguments
    security_group_ids: list[str]
    credit_specification: CreditSpecification
    image_id: str
    images: list[Image]
    monitoring: bool
    health_check_type: str
    load_balancers_config:  LoadBalancersConfig
    health_check_grace_period: int
    health_check_unhealthy_duration_before_replacement: int
    ebs_optimized: bool
    tenancy: str
    iam_role: IamRole
    key_pair: str
    user_data: str
    shutdown_script: str
    block_device_mappings: list[BlockDeviceMapping]
    network_interfaces: list[NetworkInterface]
    tags: list[Tag]
    resource_tag_specification: ResourceTagSpecification
    """
    def __init__(
            self,
            security_group_ids=none,
            image_id=none,
            images=none,
            monitoring=none,
            credit_specification=none,
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
            tags=none,
            resource_tag_specification=none):

        self.load_balancers_config = load_balancers_config
        self.health_check_type = health_check_type
        self.health_check_grace_period = health_check_grace_period
        self.health_check_unhealthy_duration_before_replacement = health_check_unhealthy_duration_before_replacement
        self.security_group_ids = security_group_ids
        self.monitoring = monitoring
        self.credit_specification = credit_specification
        self.ebs_optimized = ebs_optimized
        self.image_id = image_id
        self.images = images
        self.tenancy = tenancy
        self.iam_role = iam_role
        self.key_pair = key_pair
        self.user_data = user_data
        self.shutdown_script = shutdown_script
        self.block_device_mappings = block_device_mappings
        self.network_interfaces = network_interfaces
        self.tags = tags
        self.resource_tag_specification = resource_tag_specification


class CreditSpecification:
    """
    # Arguments
    cpu_credits: str
    """ 
    def __init__(
        self,
        cpu_credits=none):

        self.cpu_credits = cpu_credits


class Image:
    """
    # Arguments
    id: str
    """
    def __init__(
        self,
        id=none):

        self.id = id


class LoadBalancersConfig:
    """
    # Arguments
    load_balancers: list[LoadBalancer]
    """
    def __init__(self, load_balancers=none):

        self.load_balancers = load_balancers


class LoadBalancer:
    """
    # Arguments
    type: str
    arn: str
    name: str
    target_set_id: str
    balancer_id: str
    auto_weight: bool
    az_awareness: bool
    """
    def __init__(
            self,
            type=none,
            arn=none,
            name=none,
            target_set_id=none,
            balancer_id=none,
            auto_weight=none,
            az_awareness=none):

        self.type = type
        self.arn = arn
        self.name = name
        self.target_set_id = target_set_id
        self.balancer_id = balancer_id
        self.auto_weight = auto_weight
        self.az_awareness = az_awareness


class IamRole:
    """
    # Arguments
    name: str
    arn: str
    """
    def __init__(self, name=none, arn=none):

        self.name = name
        self.arn = arn


class BlockDeviceMapping:
    """
    # Arguments
    device_name: str
    ebs: list[EBS]
    no_device: bool
    virtual_name: str
    """
    def __init__(
            self,
            device_name=none,
            ebs=none,
            no_device=none,
            virtual_name=none):

        self.device_name = device_name
        self.ebs = ebs
        self.no_device = no_device
        self.virtual_name = virtual_name


class EBS:
    """
    # Arguments
    delete_on_termination: bool
    encrypted: bool
    iops: int
    snapshot_id: str
    volume_size: int
    volume_type: str
    kms_key_id: str
    dynamic_volume_size: DynamicVolumeSize
    throughput: int
    """
    def __init__(
            self,
            delete_on_termination=none,
            encrypted=none,
            iops=none,
            snapshot_id=none,
            volume_size=none,
            volume_type=none,
            kms_key_id=none,
            dynamic_volume_size=none,
            throughput=none):

        self.delete_on_termination = delete_on_termination
        self.encrypted = encrypted
        self.iops = iops
        self.snapshot_id = snapshot_id
        self.volume_size = volume_size
        self.volume_type = volume_type
        self.kms_key_id = kms_key_id
        self.dynamic_volume_size = dynamic_volume_size
        self.throughput = throughput

class DynamicVolumeSize:
    """
    # Arguments
    base_size: int
    resource: str
    size_per_resource_unit: int
    """
    def __init__(
            self,
            base_size=none,
            resource=none,
            size_per_resource_unit=none):

        self.base_size=base_size
        self.resource=resource
        self.size_per_resource_unit=size_per_resource_unit


class Tag:
    """
    # Arguments
    tag_key: str
    tag_value: str
    """
    def __init__(self, tag_key=none, tag_value=none):

        self.tag_key = tag_key
        self.tag_value = tag_value


class NetworkInterface:
    """
    # Arguments
    delete_on_termination: bool
    device_index: int
    description: str
    secondary_private_ip_address_count: int
    associate_public_ip_address: bool
    groups: list[str]
    network_interface_id: str
    private_ip_address: str
    private_ip_addresses: PrivateIpAddress
    subnet_id: str
    associate_ipv6_address: str
    """
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
    """
    # Arguments
    private_ip_address: str
    primary: bool
    """
    def __init__(self, private_ip_address=none, primary=none):

        self.private_ip_address = private_ip_address
        self.primary = primary


# endregion

class Roll:
    """
    # Arguments
    batch_size_percentage: str
    grace_period: xstr
    health_check_type: str
    strategy: RollStrategy
    """
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


class RollStrategy:
    """
    # Arguments
    action: str,
    should_drain_instances: bool,
    batch_min_healthy_percentage: int,
    on_failure: OnFailure
    """
    def __init__(
            self,
            action=none,
            should_drain_instances=none,
            batch_min_healthy_percentage=none,
            on_failure=none):
        self.action = action
        self.should_drain_instances = should_drain_instances
        self.batch_min_healthy_percentage = batch_min_healthy_percentage
        self.on_failure = on_failure


class OnFailure:
    """
    # Arguments
    action_type: str
    should_handle_all_batches: bool
    batch_num: int
    draining_timeout: int
    should_decrement_target_capacity: bool
    """
    def __init__(
            self,
            action_type=none,
            should_handle_all_batches=none,
            batch_num=none,
            draining_timeout=none,
            should_decrement_target_capacity=none):
        self.action_type = action_type
        self.should_handle_all_batches = should_handle_all_batches
        self.batch_num = batch_num
        self.draining_timeout = draining_timeout
        self.should_decrement_target_capacity = should_decrement_target_capacity


class DetachConfiguration:
    """
    # Arguments
    instances_to_detach: list[str]
    should_terminate_instances: bool
    draining_timeout: int
    should_decrement_target_capacity: bool
    """
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
    """
    # Arguments
    should_delete_images: bool
    should_delete_network_interfaces: bool
    should_delete_volumes: bool
    should_delete_snapshots: bool
    """
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
