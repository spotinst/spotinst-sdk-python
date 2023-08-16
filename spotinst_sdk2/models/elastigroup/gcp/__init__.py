import json
from enum import Enum
from typing import List

none = "d3043820717d74d9a17694c176d39733"


# region Capacity
class Capacity:
    """
    # Arguments
    minimum: int
    maximum: int
    target: int
    unit: str
    """

    def __init__(self,
                 minimum: int = none,
                 maximum: int = none,
                 target: int = none,
                 unit: str = none):
        self.minimum = minimum
        self.maximum = maximum
        self.target = target
        self.unit = unit


# endregion


# region Strategy
class RevertToPreemptible:
    """
    # Arguments
    perform_at: str
    """

    def __init__(self,
                 perform_at: str = none):
        self.perform_at = perform_at


class ProvisioningModel(Enum):
    spot = 'SPOT'
    preemptible = 'PREEMPTIBLE'


class Strategy:
    """
    # Arguments
    preemptible_percentage: int
    on_demand_count: int
    draining_timeout: int
    fallback_to_od: bool
    optimization_windows: List[str]
    provisioning_model: ProvisioningModel
    revert_to_preemptible: RevertToPreemptible
    """

    def __init__(
            self,
            preemptible_percentage: int = none,
            on_demand_count: int = none,
            draining_timeout: int = none,
            fallback_to_od: bool = none,
            optimization_windows: List[str] = none,
            provisioning_model: ProvisioningModel = none,
            revert_to_preemptible: RevertToPreemptible = none):
        self.preemptible_percentage = preemptible_percentage
        self.on_demand_count = on_demand_count
        self.draining_timeout = draining_timeout
        self.fallback_to_od = fallback_to_od
        self.optimization_windows = optimization_windows
        self.provisioning_model = provisioning_model
        self.revert_to_preemptible = revert_to_preemptible


# endregion


# region Scaling
class ScalingPolicyAction:
    """
    # Arguments
    scaling_type: str
    adjustment: int
    """

    def __init__(self,
                 scaling_type: str = none,
                 adjustment: int = none):
        self.type = scaling_type
        self.adjustment = adjustment


class ScalingPolicyDimension:
    """
    # Arguments
    name: str
    value: str
    """

    def __init__(self, name=none, value=none):
        self.name = name
        self.value = value


class ScalingPolicy:
    """
    # Arguments
    action: ScalingPolicyAction
    cooldown: int
    dimensions: List[ScalingPolicyDimension]
    evaluation_periods: int
    metric_name: str
    namespace: str
    operator: str
    period: int
    policy_name: str
    source: str
    statistic: str
    threshold: int
    unit: str
    """

    def __init__(
            self,
            action: ScalingPolicyAction = none,
            cooldown: int = none,
            dimensions: List[ScalingPolicyDimension] = none,
            evaluation_periods: int = none,
            metric_name: str = none,
            namespace: str = none,
            operator: str = none,
            period: int = none,
            policy_name: str = none,
            source: str = none,
            statistic: str = none,
            threshold: int = none,
            unit: str = none):
        self.source = source
        self.policy_name = policy_name
        self.namespace = namespace
        self.metric_name = metric_name
        self.dimensions = dimensions
        self.statistic = statistic
        self.unit = unit
        self.threshold = threshold
        self.period = period
        self.evaluation_periods = evaluation_periods
        self.cooldown = cooldown
        self.action = action
        self.operator = operator


class Scaling:
    """
    # Arguments
    up:  List[ScalingPolicy]
    down: List[ScalingPolicy]
    """

    def __init__(self,
                 up: List[ScalingPolicy] = none,
                 down: List[ScalingPolicy] = none):
        self.up = up
        self.down = down


# endregion


# region ThirdPartiesIntegration
class DockerSwarmConfiguration:
    """
    # Arguments
    master_host: str
    master_port: int
    """

    def __init__(self,
                 master_host: str = none,
                 master_port: int = none):
        self.master_host = master_host
        self.master_port = master_port


class Down:
    """
    # Arguments
    evaluation_periods: int
    """

    def __init__(self, evaluation_periods: int = none):
        self.evaluation_periods = evaluation_periods


class Headroom:
    """
    # Arguments
    cpu_per_unit: int
    memory_per_unit: int
    num_of_units: int
    """

    def __init__(
            self,
            cpu_per_unit: int = none,
            memory_per_unit: int = none,
            num_of_units: int = none):
        self.cpu_per_unit = cpu_per_unit
        self.memory_per_unit = memory_per_unit
        self.num_of_units = num_of_units


class AutoScale:
    """
    # Arguments
    is_enabled: bool
    is_auto_config: bool
    cooldown: int
    headroom: Headroom
    down: Down
    """

    def __init__(
            self,
            is_enabled: bool = none,
            is_auto_config: bool = none,
            cooldown: int = none,
            headroom: Headroom = none,
            down: Down = none):
        self.is_enabled = is_enabled
        self.is_auto_config = is_auto_config
        self.cooldown = cooldown
        self.headroom = headroom
        self.down = down


class GKE:
    """
    # Arguments
    auto_update: bool
    auto_scale: AutoScale
    cluster_identifier: str
    location: str
    """

    def __init__(
            self,
            auto_update: bool = none,
            auto_scale: AutoScale = none,
            cluster_identifier: str = none,
            location: str = none):
        self.auto_update = auto_update
        self.auto_scale = auto_scale
        self.cluster_identifier = cluster_identifier
        self.location = location


class ThirdPartiesIntegration:
    """
    # Arguments
    docker_swarm: DockerSwarmConfiguration
    gke : GKE
    """

    def __init__(
            self,
            docker_swarm: DockerSwarmConfiguration = none,
            gke: GKE = none):
        self.docker_swarm = docker_swarm
        self.gke = gke


# endregion


# region Compute
class Metadata:
    """
    # Arguments
    key: str
    value: str
    """

    def __init__(self, key: str = none, value: str = none):
        self.key = key
        self.value = value


class NamedPorts:
    """
    # Arguments
    name: str
    ports: List[int]
    """

    def __init__(
            self,
            name: str = none,
            ports: List[int] = none):
        self.name = name
        self.ports = ports


class BackendServices:
    """
    # Arguments
    backend_service_name: str
    location_type: str
    scheme: str
    named_ports: NamedPorts
    """

    def __init__(
            self,
            backend_service_name: str = none,
            location_type: str = none,
            scheme: str = none,
            named_ports: NamedPorts = none):
        self.backend_service_name = backend_service_name
        self.location_type = location_type
        self.scheme = scheme
        self.named_ports = named_ports


class BackendServiceConfig:
    """
    # Arguments
    backend_services: List[BackendServices]
    """

    def __init__(self, backend_services: List[BackendServices] = none):
        self.backend_services = backend_services


class InitializeParams:
    """
    # Arguments
    disk_size_gb: int
    disk_type: str
    source_image: str
    """

    def __init__(
            self,
            disk_size_gb: int = none,
            disk_type: str = none,
            source_image: str = none):
        self.disk_size_gb = disk_size_gb
        self.disk_type = disk_type
        self.source_image = source_image


class Disk:
    """
    # Arguments
    auto_delete: bool
    boot: bool
    device_name: str
    initialize_params: InitializeParams
    interface: str
    mode: str
    source: str
    disk_type: str
    """

    def __init__(
            self,
            auto_delete: bool = none,
            boot: bool = none,
            device_name: str = none,
            initialize_params: InitializeParams = none,
            interface: str = none,
            mode: str = none,
            source: str = none,
            disk_type: str = none):
        self.auto_delete = auto_delete
        self.boot = boot
        self.device_name = device_name
        self.initialize_params = initialize_params
        self.interface = interface
        self.mode = mode
        self.source = source
        self.type = disk_type


class NetworkInterface:
    """
    # Arguments
    network: str
    project_id: str
    """

    def __init__(
            self,
            network: str = none,
            project_id: str = none):
        self.network = network
        self.project_id = project_id


class LaunchSpecification:
    """
    # Arguments
    metadata: List[Metadata]
    tags: List[str]
    backend_service_config: BackendServiceConfig
    startup_script: str
    disks: List[Disk]
    network_interfaces: List[NetworkInterface]
    ip_forwarding: bool
    shutdown_script: str
    min_cpu_platform: str
    instance_name_prefix: str
    """

    def __init__(
            self,
            metadata: List[Metadata] = none,
            tags: List[str] = none,
            backend_service_config: BackendServiceConfig = none,
            startup_script: str = none,
            disks: List[Disk] = none,
            network_interfaces: List[NetworkInterface] = none,
            ip_forwarding: bool = none,
            shutdown_script: str = none,
            min_cpu_platform: str = none,
            instance_name_prefix: str = none):
        self.metadata = metadata
        self.tags = tags
        self.backend_service_config = backend_service_config
        self.startup_script = startup_script
        self.disks = disks
        self.network_interfaces = network_interfaces
        self.ip_forwarding = ip_forwarding
        self.shutdown_script = shutdown_script
        self.min_cpu_platform = min_cpu_platform
        self.instance_name_prefix = instance_name_prefix


class CustomInstanceTypes:
    """
    # Arguments
    v_cPU: int
    memory_giB: int
    """

    def __init__(
            self,
            v_cPU: int = none,
            memory_giB: int = none):
        self.v_cPU = v_cPU
        self.memory_giB = memory_giB


class PreferredPreemtible:
    """
    # Arguments
    custom: CustomInstanceTypes
    preemptible: List[str]
    """

    def __init__(self,
                 custom: CustomInstanceTypes = none,
                 preemptible: List[str] = none):
        self.custom = custom
        self.preemptible = preemptible


class InstanceTypes:
    """
    # Arguments
    ondemand: str
    preemptible: List[str]
    custom: CustomInstanceTypes
    preferred: PreferredPreemtible
    """

    def __init__(
            self,
            ondemand: str = none,
            preemptible: List[str] = none,
            custom: CustomInstanceTypes = none,
            preferred: PreferredPreemtible = none):
        self.ondemand = ondemand
        self.preemptible = preemptible
        self.custom = custom
        self.preferred = preferred


class Gpu:
    """
    # Arguments
    gpu_type: str
    count: int
    """

    def __init__(
            self,
            gpu_type: str = none,
            count: int = none):
        self.type = gpu_type
        self.count = count


class Health:
    """
    # Arguments
    grace_period: str
    auto_healing: bool
    health_check_type: str
    unhealthy_duration: int
    """

    def __init__(
            self,
            grace_period: str = none,
            auto_healing: bool = none,
            health_check_type: str = none,
            unhealthy_duration: int = none):
        self.grace_period = grace_period
        self.auto_healing = auto_healing
        self.health_check_type = health_check_type
        self.unhealthy_duration = unhealthy_duration


class Subnet:
    """
    # Arguments
    region: str
    subnet_names: List[str]
    """

    def __init__(
            self,
            region: str = none,
            subnet_names: List[str] = none):
        self.region = region
        self.subnet_names = subnet_names


class Compute:
    """
    # Arguments
    launch_specification: LaunchSpecification
    instance_types: InstanceTypes
    gpu: Gpu
    health: Health
    availability_zones: List[str]
    subnets: List[Subnet]
    preferred_availability_zones: List[str]
    """

    def __init__(
            self,
            launch_specification: LaunchSpecification = none,
            instance_types: InstanceTypes = none,
            gpu: Gpu = none,
            health: Health = none,
            availability_zones: List[str] = none,
            subnets: List[Subnet] = none,
            preferred_availability_zones: List[str] = none):
        self.launch_specification = launch_specification
        self.instance_types = instance_types
        self.gpu = gpu
        self.health = health
        self.availability_zones = availability_zones
        self.subnets = subnets
        self.preferred_availability_zones = preferred_availability_zones


# endregion


# region Scheduling
class Tasks:
    """
    # Arguments
    cron_expression: str
    is_enabled: bool
    max_capacity: int
    min_capacity: int
    target_capacity: int
    task_type: str
    """

    def __init__(self,
                 cron_expression: str = none,
                 is_enabled: bool = none,
                 max_capacity: int = none,
                 min_capacity: int = none,
                 target_capacity: int = none,
                 task_type: str = none):
        self.cron_expression = cron_expression
        self.is_enabled = is_enabled
        self.max_capacity = max_capacity
        self.min_capacity = min_capacity
        self.target_capacity = target_capacity
        self.task_type = task_type


class Scheduling:
    """
    # Arguments
    tasks: List[Tasks]
    """

    def __init__(self,
                 tasks: List[Tasks] = none):
        self.tasks = tasks
# endregion


# region Elastigroup
class Elastigroup:
    """
    # Arguments
    name: str
    description: str
    capacity: Capacity
    strategy: Strategy
    scaling: Scaling
    third_parties_integration: ThirdPartiesIntegration
    compute: Compute
    scheduling: Scheduling
    """

    def __init__(
            self,
            name: str = none,
            description: str = none,
            capacity: Capacity = none,
            strategy: Strategy = none,
            scaling: Scaling = none,
            third_parties_integration: ThirdPartiesIntegration = none,
            compute: Compute = none,
            scheduling: Scheduling = none):
        self.name = name
        self.description = description
        self.capacity = capacity
        self.strategy = strategy
        self.scaling = scaling
        self.third_parties_integration = third_parties_integration
        self.compute = compute
        self.scheduling = scheduling


class ElastigroupCreationRequest:
    def __init__(self, elastigroup: Elastigroup):
        self.group = elastigroup

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class ElastigroupUpdateRequest:
    def __init__(self, elastigroup: Elastigroup):
        self.group = elastigroup

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


# endregion


# region Deployment
class RollGroup:
    """
    # Arguments
    batch_size_percentage: int
    grace_period: int
    """

    def __init__(
            self,
            batch_size_percentage: int = none,
            grace_period: int = none):
        self.batch_size_percentage = batch_size_percentage
        self.grace_period = grace_period


class ElastigroupRollRequest:
    def __init__(self, group_roll: RollGroup):
        self.batch_size_percentage = group_roll.batch_size_percentage
        self.grace_period = group_roll.grace_period

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
# endregion


# region Detach Instance
class DetachConfiguration:
    """
    # Arguments
    instances_to_detach: List[str]
    should_terminate_instances: bool
    draining_timeout: int
    should_decrement_target_capacity: bool
    """

    def __init__(
            self,
            instances_to_detach: List[str] = none,
            should_terminate_instances: bool = none,
            draining_timeout: int = none,
            should_decrement_target_capacity: bool = none):
        self.instances_to_detach = instances_to_detach
        self.should_terminate_instances = should_terminate_instances
        self.draining_timeout = draining_timeout
        self.should_decrement_target_capacity = should_decrement_target_capacity


class ElastigroupDetachInstancesRequest:
    def __init__(self, detach_configuration: DetachConfiguration):
        self.should_decrement_target_capacity = detach_configuration.should_decrement_target_capacity
        self.draining_timeout = detach_configuration.draining_timeout
        self.instances_to_detach = detach_configuration.instances_to_detach
        self.should_terminate_instances = detach_configuration.should_terminate_instances

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
# endregion
