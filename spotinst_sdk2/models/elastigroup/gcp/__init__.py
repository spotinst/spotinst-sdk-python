import json

none = "d3043820717d74d9a17694c176d39733"


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
    """
    def __init__(
            self,
            name=none,
            description=none,
            capacity=none,
            strategy=none,
            scaling=none,
            third_parties_integration=none,
            compute=none):

        self.name = name
        self.description = description
        self.capacity = capacity
        self.strategy = strategy
        self.scaling = scaling
        self.third_parties_integration = third_parties_integration
        self.compute = compute

# endregion

# region Capacity
class Capacity:
    """
    # Arguments
    minimum: int
    maximum: int
    target: int
    """
    def __init__(self, minimum=none, maximum=none, target=none):

        self.minimum = minimum
        self.maximum = maximum
        self.target = target
# endregion


# region Strategy
class Strategy:
    """
    # Arguments
    preemptible_percentage: int
    on_demand_count: int
    draining_timeout: int
    fallback_to_od: bool
    """
    def __init__(
            self,
            preemptible_percentage=none,
            on_demand_count=none,
            draining_timeout=none,
            fallback_to_od=none):

            self.preemptible_percentage = preemptible_percentage
            self.on_demand_count = on_demand_count
            self.draining_timeout = draining_timeout
            self.fallback_to_od = fallback_to_od
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
    source: str
    policy_name: str
    namespace: str
    metric_name: str
    dimensions: list[ScalingPolicyDimension]
    statistic: str
    unit: str
    threshold: float
    period: int
    evaluation_periods: int
    cooldown: int
    action: ScalingPolicyAction
    operator: str
    """
    def __init__(
            self,
            source=none,
            policy_name=none,
            namespace=none,
            metric_name=none,
            dimensions=none,
            statistic=none,
            unit=none,
            threshold=none,
            period=none,
            evaluation_periods=none,
            cooldown=none,
            action=none,
            operator=none):

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
    """
    def __init__(self, scaling_type=none, adjustment=none):

        self.type = scaling_type
        self.adjustment = adjustment
# endregion


# region ThirdPartiesIntegration
class ThirdPartiesIntegration:
    """
    # Arguments
    docker_swarm: DockerSwarmConfiguration
    gke : GKE
    """
    def __init__(
            self,
            docker_swarm=none,
            gke=none):

        self.docker_swarm = docker_swarm
        self.gke = gke

class DockerSwarmConfiguration:
    """
    # Arguments
    master_host: str
    master_port: int
    """
    def __init__(self, master_host=none, master_port=none):

        self.master_host = master_host
        self.master_port = master_port

class GKE:
    """
    # Arguments
    auto_update: bool
    auto_scale: AutoScale
    """
    def __init__(
            self,
            auto_update=none,
            auto_scale=none):

        self.auto_update = auto_update
        self.auto_scale = auto_scale

class AutoScale:
    """
    # Arguments
    is_enabled: bool
    is_auto_config: bool
    cooldown: int
    headroom: Headroom
    labels: list[Label]
    down: Down
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

class Headroom:
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

class Down:
    """
    # Arguments
    evaluation_periods: int
    """
    def __init__(self, evaluation_periods=none):
        self.evaluation_periods = evaluation_periods


# endregion


# region Compute
class Compute:
    """
    # Arguments
    launch_specification: LaunchSpecification
    instance_types: InstanceTypes
    gpu: Gpu
    health: Health
    availability_zones: list[str]
    subnets: list[Subnet]
    """
    def __init__(
            self,
            launch_specification=none,
            instance_types=none,
            gpu=none,
            health=none,
            availability_zones=none,
            subnets=none):

        self.launch_specification = launch_specification
        self.instance_types = instance_types
        self.gpu = gpu
        self.health = health
        self.availability_zones = availability_zones
        self.subnets = subnets

class LaunchSpecification:
    """
    # Arguments
    labels: list[Label]
    metadata: list[MetaData]
    tags: List[str]
    backend_service_config: BackendServiceConfig
    startup_script: str
    disks: list[Disk]
    network_interfaces: list[NetworkInterface]
    service_account: str
    ip_forwarding: bool
    """
    def __init__(
            self,
            labels=none,
            metadata=none,
            tags=none,
            backend_service_config=none,
            startup_script=none,
            disks=none,
            network_interfaces=none,
            service_account=none,
            ip_forwarding=none):

        self.labels = labels
        self.metadata = metadata 
        self.tags = tags 
        self.backend_service_config = backend_service_config
        self.startup_script = startup_script
        self.disks = disks
        self.network_interfaces = network_interfaces
        self.service_account = service_account
        self.ip_forwarding = ip_forwarding

class Label:
    """
    # Arguments
    key: str
    value: str
    """
    def __init__(self, key=none, value=none):

        self.key = key
        self.value = value

class Metadata:
    """
    # Arguments
    key: str
    value: str
    """
    def __init__(self, key=none, value=none):

        self.key = key
        self.value = value

class BackendServiceConfig:
    """
    # Arguments
    backend_services: [BackendServices]
    """
    def __init__(self, backend_services=none):
        self.backend_services = backend_services

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
            backend_service_name=none,
            location_type=none,
            scheme=none,
            named_ports=none):

        self.backend_service_name = backend_service_name
        self.location_type = location_type
        self.scheme = scheme
        self.named_ports = named_ports

class NamedPorts:
    """
    # Arguments
    name: str
    ports: list[int]
    """
    def __init__(
            self,
            name=none,
            ports=none):

        self.name = name
        self.ports = ports

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
            auto_delete=none,
            boot=none,
            device_name=none,
            initialize_params=none,
            interface=none,
            mode=none,
            source=none,
            disk_type=none):

        self.auto_delete = auto_delete
        self.boot = boot
        self.device_name = device_name
        self.initialize_params = initialize_params
        self.interface = interface
        self.mode = mode
        self.source = source
        self.type = disk_type

class InitializeParams:
    """
    # Arguments
    disk_size_gb: int
    disk_type: str
    source_image: str
    """

    def __init__(
            self,
            disk_size_gb=none,
            disk_type=none,
            source_image=none):

        self.disk_size_gb = disk_size_gb
        self.disk_type = disk_type
        self.source_image = source_image

class NetworkInterface: 
    """
    # Arguments
    network: str
    access_configs: list[AccessConfig]
    alias_ip_ranges: list[AliasIpRange]
    """
    def __init__(
            self,
            network=none,
            access_configs=none,
            alias_ip_ranges=none):

        self.network = network
        self.access_configs = access_configs
        self.alias_ip_ranges = alias_ip_ranges

class AccessConfig:
    """
    # Arguments
    name: str
    access_type: str
    """
    def __init__(
            self,
            name=none,
            access_type=none):

        self.name = name
        self.type = access_type

class AliasIpRange:
    """
    # Arguments
    ip_cidr_range: str
    subnetwork_range_name: str
    """
    def __init__(
            self,
            ip_cidr_range=none,
            subnetwork_range_name=none):

        self.ip_cidr_range = ip_cidr_range
        self.subnetwork_range_name = subnetwork_range_name

class InstanceTypes:
    """
    # Arguments
    ondemand: str
    preemptible: list[str]
    custom: list[CustomInstanceTypes]
    """
    def __init__(
            self,
            ondemand=none,
            preemptible=none,
            custom=none):

        self.ondemand = ondemand
        self.preemptible = preemptible
        self.custom = custom

class CustomInstanceTypes:
    """
    # Arguments
    v_cpu: int
    memory_gib: int
    """
    def __init__(
            self,
            v_cpu=none,
            memory_gib=none):

        self.v_cPU = v_cpu
        self.memory_giB = memory_gib

class Gpu:
    """
    # Arguments
    gpu_type: str
    count: int
    """
    def __init__(
            self,
            gpu_type=none,
            count=none):
        self.type = gpu_type
        self.count = count

class Health:
    """
    # Arguments
    grace_period: int
    """
    def __init__(
            self,
            grace_period=none):
        self.grace_period = grace_period

class Subnet:
    """
    # Arguments
    region: str
    subnet_names: list[str]
    """
    def __init__(
            self,
            region=none,
            subnet_names=none):

        self.region = region
        self.subnet_names = subnet_names

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
    """
    def __init__(
            self,
            batch_size_percentage=none,
            grace_period=none):

        self.batch_size_percentage = batch_size_percentage
        self.grace_period = grace_period

class ElastigroupRollRequest:
    def __init__(self, group_roll):
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

class ElastigroupDetachInstancesRequest:
    def __init__(self, detach_configuration):
        self.should_decrement_target_capacity = detach_configuration.should_decrement_target_capacity
        self.draining_timeout = detach_configuration.draining_timeout
        self.instances_to_detach = detach_configuration.instances_to_detach
        self.should_terminate_instances = detach_configuration.should_terminate_instances

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
# endregion


