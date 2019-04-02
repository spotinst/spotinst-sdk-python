import json

none = "d3043820717d74d9a17694c176d39733"


# region Elastigroup
class Elastigroup:
    """
    # Arguments
    name: str
    region: str
    resource_group_name: str
    capacity: Capacity
    strategy: Strategy
    compute: Compute
    scaling: Scaling
    scheduling: Scheduling
    third_parties_integration: ThirdPartiesIntegration
    """
    def __init__(
            self,
            name=none,
            region=none,
            resource_group_name=none,
            capacity=none,
            strategy=none,
            compute=none,
            scaling=none,
            scheduling=none,
            third_parties_integration=none):

        self.name = name
        self.region = region
        self.resource_group_name = resource_group_name
        self.capacity = capacity
        self.strategy = strategy
        self.compute = compute
        self.scaling = scaling
        self.scheduling = scheduling
        self.third_parties_integration = third_parties_integration
# endregion

# region Capacity
class Capacity:
    """
    # Arguments
    minimum: int
    maximum: int
    target: int
    """
    def __init__(
            self,
            minimum=none,
            maximum=none,
            target=none):

        self.minimum = minimum
        self.maximum = maximum
        self.target = target
# endregion


# region Strategy
class Strategy:
    """
    # Arugments
    low_priority_percentage: int
    on_demand_count: int
    draining_timeout: int
    """
    def __init__(
            self,
            low_priority_percentage=none,
            on_demand_count=none,
            draining_timeout=none):

        self.low_priority_percentage = low_priority_percentage
        self.on_demand_count = on_demand_count
        self.draining_timeout = draining_timeout
# endregion

# region Compute
class Compute:
    """
    # Arguments
    vm_sizes: VmSizes
    product: str
    health: Health
    launch_specification: LaunchSpecification
    """
    def __init__(
            self,
            vm_sizes=none,
            product=none,
            health=none,
            launch_specification=none):

        self.vm_sizes = vm_sizes
        self.product = product
        self.health = health
        self.launch_specification = launch_specification

class VmSizes:
    """
    #Arguments
    od_sizes: list[str]
    low_priority_sizes: list[str]
    """
    def __init__(
            self,
            od_sizes=none,
            low_priority_sizes=none):

        self.od_sizes = od_sizes
        self.low_priority_sizes = low_priority_sizes

class Health:
    """
    #Arguments
    health_check_type: str
    auto_healing: bool
    grace_period: int
    """
    def __init__(
            self,
            health_check_type=none,
            auto_healing=none,
            grace_period=none):

        self.health_check_type = health_check_type
        self.auto_healing = auto_healing
        self.grace_period = grace_period

class LaunchSpecification:
    """
    #Arguments
    image: Image
    network: Network
    login: Login
    user_data: str
    shutdown_script: str
    custom_data: str
    load_balancers_config: LoadBalancerConfig
    tags: list[Tag]
    extensions: list[Extension]
    managed_service_identities: list[ManagedServiceIdentity]
    """
    def __init__(
            self,
            image=none,
            network=none,
            login=none,
            user_data=none,
            shutdown_script=none,
            custom_data=none,
            load_balancers_config=none,
            tags=none,
            extensions=none,
            managed_service_identities=none):

        self.image = image
        self.network = network
        self.login = login
        self.user_data = user_data
        self.shutdown_script = shutdown_script
        self.custom_data = custom_data
        self.load_balancers_config = load_balancers_config
        self.tags = tags
        self.extensions = extensions
        self.managed_service_identities = managed_service_identities

class Image:
    """
    # Arguments
    marketplace: Marketplace
    custom: Custom
    """
    def __init__(self, marketplace=none, custom=none):

        self.marketplace = marketplace
        self.custom = custom

class Marketplace:
    """
    # Arguments
    publisher: str
    offer: str
    sku: str
    version: str
    """
    def __init__(
            self,
            publisher=none,
            offer=none,
            sku=none,
            version=none):

        self.publisher = publisher
        self.offer = offer
        self.sku = sku
        self.version = version

class Custom:
    """
    # Arguments
    resource_group_name: str
    image_name: str
    """
    def __init__(
            self,
            resource_group_name=none,
            image_name=none):

        self.resource_group_name = resource_group_name
        self.image_name = image_name

class Network:
    """
    # Arguments
    virtual_network_name: str
    subnet_name: str
    resource_group_name: str
    assign_public_ip: bool
    additional_ip_configurations: list[AdditionalIpConfiguration]
    """
    def __init__(
            self,
            virtual_network_name=none,
            subnet_name=none,
            resource_group_name=none,
            assign_public_ip=none,
            additional_ip_configurations=none):

        self.virtual_network_name = virtual_network_name
        self.subnet_name = subnet_name
        self.resource_group_name = resource_group_name
        self.assign_public_ip = assign_public_ip
        self.additional_ip_configurations = additional_ip_configurations

class AdditionalIpConfiguration:
    """
    # Arguments
    name: str
    private_ip_address_version: str
    """
    def __init__(
            self,
            name=none,
            private_ip_address_version=none): 

        self.name = name
        self.private_ip_address_version = private_ip_address_version

class Login:
    """
    # Arguments
    ssh_public_key: str
    user_name: str
    password: str
    """
    def __init__(
            self,
            ssh_public_key=none,
            user_name=none,
            password=none):

        self.ssh_public_key = ssh_public_key
        self.user_name = user_name
        self.password = password

class LoadBalancerConfig:
    """
    # Arguments
    load_balancers: list[LoadBalancer]
    """
    def __init__(self, load_balancers=none):
        self.load_balancers = load_balancers

class LoadBalancer:
    """
    # Arguments
    balancer_id: str
    target_set_id: str
    auto_weight: bool
    resource_group_name: str
    application_gateway_name: str
    backend_pool_name: str
    balancer_type: str
    """
    def __init__(
            self,
            balancer_id=none,
            target_set_id=none,
            auto_weight=none,
            resource_group_name=none,
            application_gateway_name=none,
            backend_pool_name=none,
            balancer_type=none):

        self.balancer_id = balancer_id
        self.target_set_id = target_set_id
        self.auto_weight = auto_weight
        self.resource_group_name = resource_group_name
        self.application_gateway_name = application_gateway_name
        self.backend_pool_name = backend_pool_name
        self.type = balancer_type

class Tag:
    """
    # Arguments
    tag_key: str
    tag_value: str
    """
    def __init__(
            self,
            tag_key=none,
            tag_value=none):

        self.tag_key = tag_key
        self.tag_value = tag_value

class Extension:
    """
    # Arguments
    auto_upgrade_minor_version: bool
    name: str
    publisher: str
    extension_type: str
    type_handler_version: str
    protected_settings: ProtectedSettings
    """
    def __init__(
            self,
            auto_upgrade_minor_version=none,
            name=none,
            publisher=none,
            extension_type=none,
            type_handler_version=none,
            protected_settings=none):

        self.auto_upgrade_minor_version = auto_upgrade_minor_version
        self.name = name
        self.publisher = publisher
        self.type = extension_type
        self.type_handler_version = type_handler_version
        self.protected_settings = protected_settings

class ProtectedSettings:
    """
    # Arguments
    command_to_execute: str
    """
    def __init__(self, command_to_execute=none):
        self.command_to_execute = command_to_execute

class ManagedServiceIdentity:
    """
    # Arguments
    resource_group_name: str
    name: str
    """
    def __init__(
            self,
            resource_group_name=none,
            name=none):

        self.resource_group_name = resource_group_name
        self.name = name

# endregion


# region Scaling
class Scaling:
    """
    # Arguments
    up:  list[ScalingPolicy]
    down: list[ScalingPolicy]
    """
    def __init__(self, up=none, down=none):

        self.up = up
        self.down = down

class ScalingPolicy:
    """
    # Arguments
    policy_name: str
    namespace: str
    metric_name: str
    dimensions: list[ScalingPolicyDimension]
    statistic: str
    unit: str
    threshold: float
    adjustment: int
    min_target_capacity: int
    period: int
    evaluation_periods: int
    cooldown: int
    action: ScalingPolicyAction
    operator: str
    """
    def __init__(
            self,
            policy_name=none,
            namespace=none,
            metric_name=none,
            dimensions=none,
            statistic=none,
            unit=none,
            threshold=none,
            adjustment=none,
            min_target_capacity=none,
            period=none,
            evaluation_periods=none,
            cooldown=none,
            action=none,
            operator=none):

        self.policy_name = policy_name
        self.namespace = namespace
        self.metric_name = metric_name
        self.dimensions = dimensions
        self.statistic = statistic
        self.unit = unit
        self.threshold = threshold
        self.adjustment = adjustment
        self.min_target_capacity = min_target_capacity
        self.period = period
        self.evaluation_periods = evaluation_periods
        self.cooldown = cooldown
        self.action = action
        self.operator = operator

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
    scaling_type: str
    adjustment: int
    min_target_capacity: int
    target: int
    maximum: int
    minimum: int
    """
    def __init__(
            self,
            scaling_type=none,
            adjustment=none,
            min_target_capacity=none,
            target=none,
            maximum=none,
            minimum=none):

        self.type = scaling_type
        self.adjustment = adjustment
        self.min_target_capacity = min_target_capacity
        self.target = target
        self.maximum = maximum
        self.minimum = minimum
# endregion


# region Scheduling
class Scheduling:
    """
    # Arguments
    tasks: list[SchedulingTask]
    """
    def __init__(self, tasks=none):
        self.tasks = tasks

class SchedulingTask:
    """
    # Arguments
    is_enabled: bool
    cron_expression: str
    task_type: str
    scale_target_capacity: int
    scale_min_capacity: int
    scale_max_capacity: int
    batch_size_percentage: int
    grace_period: int
    adjustment: int
    adjustment_percentage: int
    """
    def __init__(
            self,
            is_enabled=none,
            cron_expression=none,
            task_type=none,
            scale_target_capacity=none,
            scale_min_capacity=none,
            scale_max_capacity=none,
            batch_size_percentage=none,
            grace_period=none,
            adjustment=none,
            adjustment_percentage=none):

        self.is_enabled = is_enabled
        self.cron_expression = cron_expression
        self.task_type = task_type
        self.scale_target_capacity = scale_target_capacity
        self.scale_min_capacity = scale_min_capacity
        self.scale_max_capacity = scale_max_capacity
        self.batch_size_percentage = batch_size_percentage
        self.grace_period = grace_period
        self.adjustment = adjustment
        self.adjustment_percentage = adjustment_percentage

# endregion


# region Third Parties Integration
class ThirdPartiesIntegration:
    """
    # Arguments
    mlb_runtime: MlbRuntime
    kubernetes: Kubernetes
    hpc_grid_engine: HpcGridEngine
    """
    def __init__(self, mlb_runtime=none, kubernetes=none, hpc_grid_engine=none):
        self.mlb_runtime = mlb_runtime
        self.kubernetes = kubernetes
        self.hpc_grid_engine = hpc_grid_engine

class MlbRuntime:
    """
    # Arguments
    deployment_id: str
    """
    def __init__(self, deployment_id=none):
        self.deployment_id = deployment_id

class Kubernetes:
    """
    # Arguments
    cluster_identifier: str
    """
    def __init__(self, cluster_identifier=none):
        self.cluster_identifier = cluster_identifier

class HpcGridEngine:
    """
    # Arguments
    cluster_id: str
    queues: List[str]
    """
    def __init__(self, cluster_id=none, queues=none):
        self.cluster_id = cluster_id
        self.queues = queues

class ElastigroupCreationRequest:
    def __init__(self, elastigroup):
        self.group = elastigroup

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
# endregion


# Deployment
class RollGroup:
    """
    # Arguments
    batch_size_percentage: int
    grace_period: int
    health_check_type: str
    """
    def __init__(
            self,
            batch_size_percentage=none,
            grace_period=none,
            health_check_type=none):

        self.batch_size_percentage = batch_size_percentage
        self.grace_period = grace_period
        self.health_check_type = health_check_type

class ElastigroupRollRequest:
    def __init__(self, group_roll):
        self.batch_size_percentage = group_roll.batch_size_percentage
        self.grace_period = group_roll.grace_period
        self.health_check_type = group_roll.health_check_type

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
# endregion


# Detach Instances
class DetachConfiguration:
    """
    # Arguments
    instances_to_detach: list[str]
    draining_timeout: int
    should_decrement_target_capacity: bool
    """
    def __init__(
            self,
            instances_to_detach=none,
            draining_timeout=none,
            should_decrement_target_capacity=none):
        self.instances_to_detach = instances_to_detach
        self.draining_timeout = draining_timeout
        self.should_decrement_target_capacity = should_decrement_target_capacity

class ElastigroupDetachInstancesRequest:
    def __init__(self, detach_configuration):
        self.should_decrement_target_capacity = detach_configuration.should_decrement_target_capacity
        self.draining_timeout = detach_configuration.draining_timeout
        self.instances_to_detach = detach_configuration.instances_to_detach

    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=4)
# endregion
