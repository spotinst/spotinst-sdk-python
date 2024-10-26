import json
from enum import Enum
from typing import List

none = "d3043820717d74d9a17694c176d39733"


# region AutoScaler
class AggressiveScaleDown:
    """
    # Arguments
    is_enabled: bool
    """

    def __init__(self,
                 is_enabled: bool = none):
        self.is_enabled = is_enabled


class Down:
    """
    # Arguments
    evaluation_periods: int
    max_scale_down_percentage: int
    aggressive_scale_down: AggressiveScaleDown
    """

    def __init__(
            self,
            evaluation_periods: int = none,
            max_scale_down_percentage: int = none,
            aggressive_scale_down: AggressiveScaleDown = none
    ):
        self.evaluation_periods = evaluation_periods
        self.max_scale_down_percentage = max_scale_down_percentage
        self.aggressive_scale_down = aggressive_scale_down


class Headroom:
    """
    # Arguments
    cpu_per_unit: int
    gpu_per_unit: int
    memory_per_unit: int
    num_of_units: int
    """

    def __init__(
            self,
            cpu_per_unit: int = none,
            gpu_per_unit: int = none,
            memory_per_unit: int = none,
            num_of_units: int = none
    ):
        self.cpu_per_unit = cpu_per_unit
        self.gpu_per_unit = gpu_per_unit
        self.memory_per_unit = memory_per_unit
        self.num_of_units = num_of_units


class ResourceLimits:
    """
    # Arguments
    max_memory_gib: int
    max_v_cpu: int
    """

    def __init__(
            self,
            max_memory_gib: int = none,
            max_v_cpu: int = none
    ):
        self.max_memory_gib = max_memory_gib
        self.max_v_cpu = max_v_cpu


class AutoScaler:
    """
    # Arguments
    auto_headroom_percentage: int
    cooldown: int
    down: Down
    enable_automatic_and_manual_headroom: bool
    headroom: Headroom
    is_auto_config: bool
    is_enabled: bool
    resource_limits: ResourceLimits
    """

    def __init__(
            self,
            auto_headroom_percentage: int = none,
            cooldown: int = none,
            down: Down = none,
            enable_automatic_and_manual_headroom: bool = none,
            headroom: Headroom = none,
            is_auto_config: bool = none,
            is_enabled: bool = none,
            resource_limits: ResourceLimits = none
    ):
        self.auto_headroom_percentage = auto_headroom_percentage
        self.cooldown = cooldown
        self.down = down
        self.enable_automatic_and_manual_headroom = enable_automatic_and_manual_headroom
        self.headroom = headroom
        self.is_auto_config = is_auto_config
        self.is_enabled = is_enabled
        self.resource_limits = resource_limits
# endregion


# region Capacity
class Capacity:
    """
    # Arguments
    maximum: int
    minimum: int
    target: int
    """

    def __init__(
            self,
            maximum: int = none,
            minimum: int = none,
            target: int = none
    ):
        self.maximum = maximum
        self.minimum = minimum
        self.target = target
# endregion


# region Compute
class LocationType(Enum):
    regional = "regional"
    _global = "global"


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


class Scheme(Enum):
    external = "EXTERNAL"
    internal = "INTERNAL"


class BackendServices:
    """
    # Arguments
    backend_service_name: str
    location_type: LocationType
    named_ports: NamedPorts
    scheme: Scheme
    """

    def __init__(
            self,
            backend_service_name: str = none,
            location_type: LocationType = none,
            named_ports: NamedPorts = none,
            scheme: Scheme = none
    ):
        self.backend_service_name = backend_service_name
        self.location_type = location_type
        self.named_ports = named_ports
        self.scheme = scheme


class InstanceTypesFilters:
    """
    # Arguments
    exclude_families: List[str]
    include_families: List[str]
    max_memory_gi_b: float
    max_vcpu: int
    min_memory_gi_b: float
    min_vcpu: int
    """

    def __init__(self,
                 exclude_families: List[str] = none,
                 include_families: List[str] = none,
                 max_memory_gi_b: float = none,
                 max_vcpu: int = none,
                 min_memory_gi_b: float = none,
                 min_vcpu: int = none):
        self.exclude_families = exclude_families
        self.include_families = include_families
        self.max_memory_gi_b = max_memory_gi_b
        self.max_vcpu = max_vcpu
        self.min_memory_gi_b = min_memory_gi_b
        self.min_vcpu = min_vcpu


class InstanceTypes:
    """
    # Arguments
    blacklist: List[str]
    whitelist: List[str]
    filters: InstanceTypesFilters
    preferred_types: List[str]
    """

    def __init__(
            self,
            blacklist: List[str] = none,
            whitelist: List[str] = none,
            filters: InstanceTypesFilters = none,
            preferred_types: List[str] = none):
        self.blacklist = blacklist
        self.whitelist = whitelist
        self.filters = filters
        self.preferred_types = preferred_types


class Labels:
    """
    # Arguments
    key: str
    value: str
    """

    def __init__(
            self,
            key: str = none,
            value: str = none):
        self.key = key
        self.value = value


class Metadata:
    """
    # Arguments
    key: str
    value: str
    """

    def __init__(
            self,
            key: str = none,
            value: str = none):
        self.key = key
        self.value = value


class RootVolumeType(Enum):
    pd_standard = "pd-standard"
    pd_ssd = "pd-ssd"
    pd_balanced = "pd-balanced"


class ShieldedInstanceConfig:
    """
    # Arguments
    enable_integrity_monitoring: bool
    enable_secure_boot: bool
    """

    def __init__(
            self,
            enable_integrity_monitoring: bool = none,
            enable_secure_boot: bool = none):
        self.enable_integrity_monitoring = enable_integrity_monitoring
        self.enable_secure_boot = enable_secure_boot


class LaunchSpecification:
    """
    # Arguments
    ip_forwarding: bool
    labels: List[Labels]
    metadata: List[Metadata]
    min_cpu_platform: str
    root_volume_size_in_gb: int
    root_volume_type: RootVolumeType
    service_account: str
    shielded_instance_config: ShieldedInstanceConfig
    source_image: str
    tags: List[str]
    use_as_template_only: bool
    """

    def __init__(
            self,
            ip_forwarding: bool = none,
            labels: List[Labels] = none,
            metadata: List[Metadata] = none,
            min_cpu_platform: str = none,
            root_volume_size_in_gb: int = none,
            root_volume_type: RootVolumeType = none,
            service_account: str = none,
            shielded_instance_config: ShieldedInstanceConfig = none,
            source_image: str = none,
            tags: List[str] = none,
            use_as_template_only: bool = none
    ):
        self.ip_forwarding = ip_forwarding
        self.labels = labels
        self.metadata = metadata
        self.min_cpu_platform = min_cpu_platform
        self.root_volume_size_in_gb = root_volume_size_in_gb
        self.root_volume_type = root_volume_type
        self.service_account = service_account
        self.shielded_instance_config = shielded_instance_config
        self.source_image = source_image
        self.tags = tags
        self.use_as_template_only = use_as_template_only


class AccessConfigs:
    """
    # Arguments
    name: str
    type: str
    """

    def __init__(
            self,
            name: str = none,
            type: str = none
    ):
        self.name = name
        self.type = type


class AliasIpRanges:
    """
    # Arguments
    ip_cidr_range: str
    subnetwork_range_name: str
    """

    def __init__(
            self,
            ip_cidr_range: str = none,
            subnetwork_range_name: str = none
    ):
        self.ip_cidr_range = ip_cidr_range
        self.subnetwork_range_name = subnetwork_range_name


class NetworkInterfaces:
    """
    # Arguments
    access_configs: List[AccessConfigs]
    alias_ip_ranges: List[AliasIpRanges]
    network: str
    project_id: str
    """

    def __init__(
            self,
            access_configs: List[AccessConfigs] = none,
            alias_ip_ranges: List[AliasIpRanges] = none,
            network: str = none,
            project_id: str = none,
    ):
        self.access_configs = access_configs
        self.alias_ip_ranges = alias_ip_ranges
        self.network = network
        self.project_id = project_id


class Compute:
    """
    # Arguments
    availability_zones: List[str]
    backend_services: BackendServices
    instance_types: InstanceTypes
    launch_specification: LaunchSpecification
    network_interfaces: List[NetworkInterfaces]
    subnet_name: str
    """

    def __init__(
            self,
            availability_zones: List[str] = none,
            backend_services: BackendServices = none,
            instance_types: InstanceTypes = none,
            launch_specification: LaunchSpecification = none,
            network_interfaces: List[NetworkInterfaces] = none,
            subnet_name: str = none
    ):
        self.availability_zones = availability_zones
        self.backend_services = backend_services
        self.instance_types = instance_types
        self.launch_specification = launch_specification
        self.network_interfaces = network_interfaces
        self.subnet_name = subnet_name
# endregion


# region GKE
class GKE:
    """
    # Arguments
    cluster_name: str
    master_location: str
    """

    def __init__(
            self,
            cluster_name: str = none,
            master_location: str = none
    ):
        self.cluster_name = cluster_name
        self.master_location = master_location
# endregion


# region Scheduling
class ShutdownHours:
    """
    # Arguments
    is_enabled: bool
    time_windows: List[str]
    """

    def __init__(
            self,
            is_enabled: bool = none,
            time_windows: List[str] = none
    ):
        self.is_enabled = is_enabled
        self.time_windows = time_windows


class ClusterRoll:
    """
    # Arguments
    batch_min_healthy_percentage: int
    batch_size_percentage: int
    comment: str
    respect_pdb: bool
    """

    def __init__(
            self,
            batch_min_healthy_percentage: int = none,
            batch_size_percentage: int = none,
            comment: str = none,
            respect_pdb: bool = none
    ):
        self.batch_min_healthy_percentage = batch_min_healthy_percentage
        self.batch_size_percentage = batch_size_percentage
        self.comment = comment
        self.respect_pdb = respect_pdb


class Parameters:
    """
    # Arguments
    cluster_roll: ClusterRoll
    """

    def __init__(
            self,
            cluster_roll: ClusterRoll = none):
        self.cluster_roll = cluster_roll


class Tasks:
    """
    # Arguments
    cron_expression: str
    is_enabled: bool
    parameters: Parameters
    task_type: str
    """

    def __init__(
            self,
            cron_expression: str = none,
            is_enabled: bool = none,
            parameters: Parameters = none,
            task_type: str = none
    ):
        self.cron_expression = cron_expression
        self.is_enabled = is_enabled
        self.parameters = parameters
        self.task_type = task_type


class Scheduling:
    """
    # Arguments
    shutdown_hours: ShutdownHours
    tasks: List[Tasks]
    """

    def __init__(
            self,
            shutdown_hours: ShutdownHours = none,
            tasks: List[Tasks] = none):
        self.shutdown_hours = shutdown_hours
        self.tasks = tasks
# endregion


# region Security
class ContainerImage:
    """
    approved_images: List[str]
    """

    def __init__(
            self,
            approved_images: List[str] = none
    ):
        self.approved_images = approved_images


class Security:
    """
    # Arguments
    container_image: ContainerImage
    """

    def __init__(
            self,
            container_image: ContainerImage = none):
        self.container_image = container_image
# endregion


# region Strategy
class ProvisioningModel(Enum):
    spot = "SPOT"
    preemptible = "PREEMPTIBLE"


class Strategy:
    """
    # Arguments
    draining_timeout: int
    preemptible_percentage: int
    provisioning_model: ProvisioningModel
    should_utilize_commitments: bool
    """

    def __init__(
            self,
            draining_timeout: int = none,
            preemptible_percentage: int = none,
            provisioning_model: ProvisioningModel = none,
            should_utilize_commitments: bool = none
    ):
        self.draining_timeout = draining_timeout
        self.preemptible_percentage = preemptible_percentage
        self.provisioning_model = provisioning_model
        self.should_utilize_commitments = should_utilize_commitments
# endregion


# region Ocean
class Ocean:
    """
    # Arguments
    auto_scaler: AutoScaler
    capacity: Capacity
    compute: Compute
    controller_cluster_id: str
    gke: GKE
    name: str
    scheduling: Scheduling
    security: Security
    strategy: Strategy
    """

    def __init__(
            self,
            auto_scaler: AutoScaler = none,
            capacity: Capacity = none,
            compute: Compute = none,
            controller_cluster_id: str = none,
            gke: GKE = none,
            name: str = none,
            scheduling: Scheduling = none,
            security: Security = none,
            strategy: Strategy = none
    ):
        self.auto_scaler = auto_scaler
        self.capacity = capacity
        self.compute = compute
        self.controller_cluster_id = controller_cluster_id
        self.gke = gke
        self.name = name
        self.scheduling = scheduling
        self.security = security
        self.strategy = strategy
# endregion


# region OceanRequest
class OceanRequest:
    def __init__(self, ocean: Ocean):
        self.cluster = ocean

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
# endregion


# RightSizingRecommendationFilter
class Type(Enum):
    label = "label"
    annotation = "annotation"


class Operator(Enum):
    equals = "equals"
    not_equals = "notEquals"
    exists = "exists"
    does_not_exist = "doesNotExist"


class Attribute:
    """
    # Arguments
    type: Type
    key: str
    operator: Operator
    value: str
    """

    def __init__(
            self,
            type: Type = none,
            key: str = none,
            operator: Operator = none,
            value: str = none):
        self.type = type
        self.key = key
        self.operator = operator
        self.value = value


class RightSizingRecommendationFilter:
    """
    # Attribute
    namespaces: List[str]
    attribute: Attribute
    """

    def __init__(
            self,
            namespaces: List[str] = none,
            attribute: Attribute = none):
        self.namespaces = namespaces
        self.attribute = attribute


class RightSizingRecommendationRequest:
    def __init__(self, filter: RightSizingRecommendationFilter = none):
        self.filter = filter

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
# endregion


# region AggregatedClusterCosts
class AllMatch:
    """
    # Arguments
    all_match:  List[Attribute]
    """

    def __init__(
            self,
            all_match:  List[Attribute] = none):
        self.all_match = all_match


class Conditions:
    """
    # Arguments
    any_match: List[AllMatch]
    """

    def __init__(
            self,
            any_match: List[AllMatch] = none):
        self.any_match = any_match


class Scope(Enum):
    namespace = "namespace"
    resource = "resource"


class Filter:
    """
    # Arguments
    conditions: Conditions
    scope: Scope
    """

    def __init__(
            self,
            conditions: Conditions = none,
            scope: Scope = none):
        self.conditions = conditions
        self.scope = scope


class GroupBy(Enum):
    namespace = "namespace"
    namespace_label = "namespace.label.${labelKey}"
    resource_label = "resource.label.${labelKey}"
    namespace_annotation = "namespace.annotation.${annotationKey}"
    resource_annotation = "resource.annotation.${annotationKey}"


class AggregatedClusterCosts:
    """
    # Arguments
    end_time: str
    aggregated_filter: Filter
    group_by: GroupBy
    start_time: str
    """

    def __init__(
            self,
            end_time: str = none,
            aggregated_filter: Filter = none,
            group_by: GroupBy = GroupBy.namespace.value,
            start_time: str = none):
        self.end_time = end_time
        self.aggregated_filter = aggregated_filter
        self.group_by = group_by
        self.start_time = start_time


class AggregatedClusterCostRequest:
    def __init__(self, aggregated_cluster_costs: AggregatedClusterCosts = none):
        self.end_time = aggregated_cluster_costs.end_time
        self.start_time = aggregated_cluster_costs.start_time
        self.group_by = aggregated_cluster_costs.group_by
        self.filter = aggregated_cluster_costs.aggregated_filter

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
# endregion


# region VirtualNodeGroup
class AutoScale:
    """
    # Arguments
    auto_headroom_percentage: int
    headrooms: List[Headroom]
    down: Down
    """

    def __init__(
            self,
            auto_headroom_percentage: int = none,
            headrooms: List[Headroom] = none,
            down: Down = none
    ):
        self.auto_headroom_percentage = auto_headroom_percentage
        self.headrooms = headrooms
        self.down = down


class VNGResourceLimits:
    """
    # Arguments
    max_instance_count: int
    min_instance_count: int
    """

    def __init__(
            self,
            max_instance_count: int = none,
            min_instance_count: int = none
    ):
        self.max_instance_count = max_instance_count
        self.min_instance_count = min_instance_count


class Config:
    """
    Arguments
    headrooms: List[Headroom]
    """

    def __init__(self,
                 headrooms: List[Headroom] = none):
        self.headrooms = headrooms


class VNGTasks:
    """
    # Arguments
    config: Config
    cron_expression: str
    is_enabled: bool
    task_type: str
    """

    def __init__(
            self,
            config: Config = none,
            cron_expression: str = none,
            is_enabled: bool = none,
            task_type: str = none
    ):
        self.config = config
        self.cron_expression = cron_expression
        self.is_enabled = is_enabled
        self.task_type = task_type


class VNGScheduling:
    """
    # Arguments
    tasks: List[VNGTasks]
    """

    def __init__(
            self,
            tasks: List[VNGTasks]):
        self.tasks = tasks


class Storage:
    """
    # Arguments
    local_ssd_count: int
    """

    def __init__(
            self,
            local_ssd_count: int = none):
        self.local_ssd_count = local_ssd_count


class VNGStrategy:
    """
    # Arguments
    preemptible_percentage: int
    """

    def __init__(
            self,
            preemptible_percentage: int = none
    ):
        self.preemptible_percentage = preemptible_percentage


class Taints:
    """
    # Arguments
    effect: str
    key: str
    value: str
    """

    def __init__(
            self,
            effect: str = none,
            key: str = none,
            value: str = none
    ):
        self.effect = effect
        self.key = key
        self.value = value


class VirtualNodeGroup:
    """
    # Arguments
    auto_scale: AutoScale
    availability_zones: List[str]
    filters: InstanceTypesFilters
    instance_types: List[str]
    preferred_types: List[str]
    labels: List[Labels]
    metadata: List[Metadata]
    name: str
    network_interfaces: List[NetworkInterfaces]
    ocean_id: str
    resource_limits: ResourceLimits
    restrict_scale_down: bool
    root_volume_size_in_gb: int
    root_volume_type: RootVolumeType
    scheduling: Scheduling
    service_account: str
    shielded_instance_config: ShieldedInstanceConfig
    source_image: str
    storage: Storage
    strategy: VNGStrategy
    tags: List[str]
    taints: List[Taints]
    """

    def __init__(
            self,
            auto_scale: AutoScale = none,
            availability_zones: List[str] = none,
            instance_types: List[str] = none,
            filters: InstanceTypesFilters = none,
            preferred_types: List[str] = none,
            labels: List[Labels] = none,
            metadata: List[Metadata] = none,
            name: str = none,
            network_interfaces: List[NetworkInterfaces] = none,
            ocean_id: str = none,
            resource_limits: VNGResourceLimits = none,
            restrict_scale_down: bool = none,
            root_volume_size_in_gb: int = none,
            root_volume_type: RootVolumeType = none,
            scheduling: VNGScheduling = none,
            service_account: str = none,
            shielded_instance_config: ShieldedInstanceConfig = none,
            source_image: str = none,
            storage: Storage = none,
            strategy: VNGStrategy = none,
            tags: List[str] = none,
            taints: List[Taints] = none
    ):
        self.auto_scale = auto_scale
        self.availability_zones = availability_zones
        self.instance_types = instance_types
        self.filters = filters
        self.preferred_types = preferred_types
        self.labels = labels
        self.metadata = metadata
        self.name = name
        self.network_interfaces = network_interfaces
        self.ocean_id = ocean_id
        self.resource_limits = resource_limits
        self.restrict_scale_down = restrict_scale_down
        self.root_volume_size_in_gb = root_volume_size_in_gb
        self.root_volume_type = root_volume_type
        self.scheduling = scheduling
        self.service_account = service_account
        self.shielded_instance_config = shielded_instance_config
        self.source_image = source_image
        self.storage = storage
        self.strategy = strategy
        self.tags = tags
        self.taints = taints
# endregion


class VNGRequest:
    def __init__(self, vng: VirtualNodeGroup):
        self.launch_spec = vng

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class Roll:
    """
    # Arguments
    batch_min_healthy_percentage: int
    batch_size_percentage: int
    comment: str
    instance_names: List[str]
    launch_spec_ids: List[str]
    respect_pdb: bool
    """

    def __init__(
            self,
            batch_min_healthy_percentage: int = none,
            batch_size_percentage: int = none,
            comment: str = none,
            launch_spec_ids: List[str] = none,
            instance_names: List[str] = none,
            respect_pdb: bool = none):
        self.batch_min_healthy_percentage = batch_min_healthy_percentage
        self.batch_size_percentage = batch_size_percentage
        self.comment = comment
        self.instance_names = instance_names
        self.launch_spec_ids = launch_spec_ids
        self.respect_pdb = respect_pdb


class ClusterRollInitiateRequest:
    def __init__(self, roll: Roll = none):
        self.roll = roll

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class ClusterRollUpdateRequest:
    def __init__(self, status: str = none):
        self.roll = dict(status=status)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class ImportGkeClusterToOcean:
    """
    # Arguments
    auto_scaler: AutoScaler
    availability_zones: List[str]
    backend_services: List[BackendServices]
    capacity: Capacity
    controller_cluster_id: str
    instance_types: InstanceTypes
    name: str
    """

    def __init__(
            self,
            auto_scaler: AutoScaler = none,
            availability_zones: List[str] = none,
            backend_services: List[BackendServices] = none,
            capacity: Capacity = none,
            controller_cluster_id: str = none,
            instance_types: InstanceTypes = none,
            name: str = none
    ):
        self.auto_scaler = auto_scaler
        self.availability_zones = availability_zones
        self.backend_services = backend_services
        self.capacity = capacity
        self.controller_cluster_id = controller_cluster_id
        self.instance_types = instance_types
        self.name = name


class ImportGkeClusterToOceanRequest:
    def __init__(self, cluster: ImportGkeClusterToOcean = none):
        self.cluster = cluster

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class LaunchNodesRequest:
    def __init__(self, amount: int = none):
        self.launch_request = dict(amount=amount)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class DetachInstancesConfig:
    """
    # Arguments
    instances_to_detach: List[str]
    should_decrement_target_capacity: bool
    should_terminate_instances: bool
    draining_timeout: int
    """

    def __init__(
            self,
            instances_to_detach: List[str] = none,
            should_decrement_target_capacity: bool = none,
            should_terminate_instances: bool = none,
            draining_timeout: int = none):
        self.instances_to_detach = instances_to_detach
        self.should_decrement_target_capacity = should_decrement_target_capacity
        self.should_terminate_instances = should_terminate_instances
        self.draining_timeout = draining_timeout


class DetachInstancesRequest:
    def __init__(self, detach_config: DetachInstancesConfig):
        self.instances_to_detach = detach_config.instances_to_detach
        self.should_decrement_target_capacity = detach_config.should_decrement_target_capacity
        self.should_terminate_instances = detach_config.should_terminate_instances
        self.draining_timeout = detach_config.draining_timeout

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class InstanceTypesFilterRequest:
    def __init__(self, filters: InstanceTypesFilters):
        self.filters = filters

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
