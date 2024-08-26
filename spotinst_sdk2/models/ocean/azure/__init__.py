import json
from enum import Enum
from typing import List

none = "d3043820717d74d9a17694c176d39733"


# region Aks
class Aks:
    """
    # Arguments
    cluster_name: str
    infrastructure_resource_group_name: str
    region: str
    resource_group_name: str
    """

    def __init__(
            self,
            cluster_name: str = none,
            infrastructure_resource_group_name: str = none,
            region: str = none,
            resource_group_name: str = none):
        self.cluster_name = cluster_name
        self.infrastructure_resource_group_name = infrastructure_resource_group_name
        self.region = region
        self.resource_group_name = resource_group_name
# endregion

# region AutoScaler


class ResourceLimits:
    """
    # Arguments
    max_memory_gib: int
    max_v_cpu: int
    """

    def __init__(
            self,
            max_memory_gib: int = none,
            max_v_cpu: int = none):
        self.max_memory_gib = max_memory_gib
        self.max_v_cpu = max_v_cpu


class Down:
    """
    # Arguments
    max_scale_down_percentage: float
    """

    def __init__(
            self,
            max_scale_down_percentage: float = none):
        self.max_scale_down_percentage = max_scale_down_percentage


class Automatic:
    """
    # Arguments
    percentage: int
    """

    def __init__(
            self,
            percentage: int = none):
        self.percentage = percentage


class AutoScalerHeadroom:
    """
    # Arguments
    automatic: Automatic
    """

    def __init__(
            self,
            automatic: Automatic = none):
        self.automatic = automatic


class AutoScaler:
    """
    # Arguments
    down: Down
    headroom: AutoScalerHeadroom
    is_enabled: bool
    resource_limits: ResourceLimits
    """

    def __init__(
            self,
            down: Down = none,
            headroom: AutoScalerHeadroom = none,
            is_enabled: bool = none,
            resource_limits: ResourceLimits = none):
        self.down = down
        self.headroom = headroom
        self.is_enabled = is_enabled
        self.resource_limits = resource_limits
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
            time_windows: List[str] = none):
        self.is_enabled = is_enabled
        self.time_windows = time_windows

class SuspensionHours:
    """
    # Arguments
    is_enabled: bool
    time_windows: List[str]
    """

    def __init__(
            self,
            is_enabled: bool = none,
            time_windows: List[str] = none):
        self.is_enabled = is_enabled
        self.time_windows = time_windows        


class ClusterRoll:
    """
    # Arguments
    batch_min_healthy_percentage: int
    batch_size_percentage: int
    comment: str
    respect_pdb: bool
    respect_restrict_scale_down: bool
    vng_ids: List[str]
    """

    def __init__(
            self,
            batch_min_healthy_percentage: int = none,
            batch_size_percentage: int = none,
            comment: str = none,
            respect_pdb: bool = none,
            respect_restrict_scale_down: bool = none,
            vng_ids: List[str] = none):
        self.batch_min_healthy_percentage = batch_min_healthy_percentage
        self.batch_size_percentage = batch_size_percentage
        self.comment = comment
        self.respect_pdb = respect_pdb
        self.respect_restrict_scale_down = respect_restrict_scale_down
        self.vng_ids = vng_ids


class Parameters:
    """
    # Arguments
    cluster_roll: ClusterRoll
    """

    def __init__(
            self,
            cluster_roll: ClusterRoll = none):
        self.cluster_roll = cluster_roll


class TaskType(Enum):
    cluster_roll = "clusterRoll"


class Task:
    """
    # Arguments
    cron_expression: str
    is_enabled: bool
    parameters: Parameters
    task_type: TaskType
    """

    def __init__(
            self,
            cron_expression: str = none,
            is_enabled: bool = none,
            parameters: Parameters = none,
            task_type: TaskType = none):
        self.cron_expression = cron_expression
        self.is_enabled = is_enabled
        self.parameters = parameters
        self.task_type = task_type


class Scheduling:
    """
    # Arguments
    shutdown_hours: ShutdownHours
    tasks: List[Task]
    """

    def __init__(
            self,
            shutdown_hours: ShutdownHours = none,
            suspension_hours : SuspensionHours = none,
            tasks: List[Task] = none):
        self.shutdown_hours = shutdown_hours
        self.suspension_hours = suspension_hours
        self.tasks = tasks
# endregion

# region Health


class Health:
    """
    # Arguments
    grace_period: int
    """

    def __init__(
            self,
            grace_period: int = none):
        self.grace_period = grace_period
 # endregion

# region VirtualNodeGroupTemplate

# region AutoScale


class AutoScaleHeadroom:
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
            num_of_units: int = none):
        self.cpu_per_unit = cpu_per_unit
        self.gpu_per_unit = gpu_per_unit
        self.memory_per_unit = memory_per_unit
        self.num_of_units = num_of_units


class AutoScale:
    """
    # Arguments
    headrooms: List[AutoScaleHeadroom]
    """

    def __init__(
            self,
            headrooms: List[AutoScaleHeadroom] = none):
        self.headrooms = headrooms
# endregion

# region NodeCountLimits


class NodeCountLimits:
    """
    # Arguments
    max_count: int
    min_count: int
    """

    def __init__(
            self,
            max_count: int = none,
            min_count: int = none):
        self.max_count = max_count
        self.min_count = min_count
# endregion

# region NodePoolProperties


class OsType(Enum):
    linux = "Linux"
    windows = "Windows"


class OsDiskType(Enum):
    managed = "Managed"
    ephemereal = "Ephemereal"


class OsSKU(Enum):
    ubuntu = "Ubuntu"
    azure_linux = "AzureLinux"
    cbl_mariner = "CBLMariner"
    windows2019 = "Windows2019"
    windows2022 = "Windows2022"


class Sysctls:
    """
    # Arguments
    vm_max_map_count: int
    """

    def __init__(
            self,
            vm_max_map_count: int = none):
        self.vm_max_map_count = vm_max_map_count


class LinuxOSConfig:
    """
    # Arguments
    sysctls: Sysctls
    """

    def __init__(
            self,
            sysctls: Sysctls = none):
        self.sysctls = sysctls


class NodePoolProperties:
    """
    # Arguments
    enable_node_public_i_p: bool
    kubernetes_version: str
    linux_o_s_config: LinuxOSConfig
    max_pods_per_node: int
    os_disk_size_g_b: int
    os_disk_type: OsDiskType
    os_s_k_u: OsSKU
    os_type: OsType
    pod_subnet_i_ds: List[str]
    vnet_subnet_i_ds: List[str]
    """

    def __init__(
            self,
            enable_node_public_i_p: bool = none,
            kubernetes_version: str = none,
            linux_o_s_config: LinuxOSConfig = none,
            max_pods_per_node: int = none,
            os_disk_size_g_b: int = none,
            os_disk_type: OsDiskType = none,
            os_s_k_u: OsSKU = none,
            os_type: OsType = none,
            pod_subnet_i_ds: List[str] = none,
            vnet_subnet_i_ds: List[str] = none):
        self.enable_node_public_i_p = enable_node_public_i_p
        self.kubernetes_version = kubernetes_version
        self.linux_o_s_config = linux_o_s_config
        self.max_pods_per_node = max_pods_per_node
        self.os_disk_size_g_b = os_disk_size_g_b
        self.os_disk_type = os_disk_type
        self.os_s_k_u = os_s_k_u
        self.os_type = os_type
        self.pod_subnet_i_ds = pod_subnet_i_ds
        self.vnet_subnet_i_ds = vnet_subnet_i_ds
# endregion

# region Strategy


class Strategy:
    """
    # Arguments
    fallback_to_od: bool
    spot_percentage: int
    """

    def __init__(
            self,
            fallback_to_od: bool = none,
            spot_percentage: int = none):
        self.fallback_to_od = fallback_to_od
        self.spot_percentage = spot_percentage
# endregion

# region Taint


class Effect(Enum):
    no_schedule = "NoSchedule"
    prefer_no_schedule = "PreferNoSchedule"
    no_execute = "NoExecute"
    prefer_no_execute = "PreferNoExecute"


class Taint:
    """
    # Arguments
    key: str
    value: str
    effect: Effect
    """

    def __init__(
            self,
            key: str = none,
            value: str = none,
            effect: Effect = none):
        self.key = key
        self.value = value
        self.effect = effect
# endregion

# region VmSizes


class Architecture(Enum):
    x86_64 = "X86_64"
    intel64 = "INTEL64"
    amd64 = "AMD64"
    arm64 = "ARM64"


class AcceleratedNetworking(Enum):
    enabled = "Enabled"
    disabled = "Disabled"


class DiskPerformance(Enum):
    standard = "Standard"
    premium = "Premium"


class VmType(Enum):
    general_purpose = "generalPurpose"
    memory_optimized = "memoryOptimized"
    compute_optimized = "computeOptimized"
    high_performance_compute = "highPerformanceCompute"
    storage_optimized = "storageOptimized"
    gpu = "GPU"


class GpuType(Enum):
    nvidia_tesla_v100 = "nvidia-tesla-v100"
    amd_radeon_instinct_mi25 = "amd-radeon-instinct-mi25"
    nvidia_a10 = "nvidia-a10"
    nvidia_tesla_a100 = "nvidia-tesla-a100"
    nvidia_tesla_k80 = "nvidia-tesla-k80"
    nvidia_tesla_m60 = "nvidia-tesla-m60"
    nvidia_tesla_p100 = "nvidia-tesla-p100"
    nvidia_tesla_p40 = "nvidia-tesla-p40"
    nvidia_tesla_t4 = "nvidia-tesla-t4"
    nvidia_tesla_h100 = "nvidia-tesla-h100"


class Filters:
    """
    # Arguments
    accelerated_networking: AcceleratedNetworking
    disk_performance: DiskPerformance
    architectures: List[Architecture]
    exclude_series: List[str]
    max_memory_gi_b: float
    max_v_cpu: int
    min_memory_gi_b: float
    min_v_cpu: int
    min_gpu: float
    max_gpu: float
    min_data: int
    min_n_i_cs: int
    series: List[str]
    vm_types: List[VmType]
    gpu_types: List[GpuType]
    """

    def __init__(
            self,
            accelerated_networking: AcceleratedNetworking = none,
            disk_performance: DiskPerformance = none,
            architectures: List[Architecture] = none,
            exclude_series: List[str] = none,
            max_memory_gi_b: float = none,
            max_v_cpu: int = none,
            min_memory_gi_b: float = none,
            min_v_cpu: int = none,
            min_gpu: float = none,
            max_gpu: float = none,
            min_data: int = none,
            min_n_i_cs: int = none,
            series: List[str] = none,
            vm_types: List[VmType] = none,
            gpu_types: List[GpuType] = none):
        self.accelerated_networking = accelerated_networking
        self.disk_performance = disk_performance
        self.architectures = architectures
        self.exclude_series = exclude_series
        self.max_memory_gi_b = max_memory_gi_b
        self.max_v_cpu = max_v_cpu
        self.min_memory_gi_b = min_memory_gi_b
        self.min_v_cpu = min_v_cpu
        self.min_gpu = min_gpu
        self.max_gpu = max_gpu
        self.min_data = min_data
        self.min_n_i_cs = min_n_i_cs
        self.series = series
        self.vm_types = vm_types
        self.gpu_types = gpu_types


class VmSizes:
    """
    # Arguments
    filters: Filters
    """

    def __init__(
            self,
            filters: Filters = none):
        self.filters = filters
# endregion


class VirtualNodeGroupTemplate:
    """
    # Arguments
    name: str
    ocean_id: str 
    auto_scale: AutoScale
    availability_zones: List[str]
    labels: dict
    node_count_limits: NodeCountLimits
    node_pool_properties: NodePoolProperties
    strategy: Strategy
    tags: dict
    taints: List[Taint]
    vm_sizes: VmSizes
    """

    def __init__(
            self,
            name: str = none,
            ocean_id: str = none,
            auto_scale: AutoScale = none,
            availability_zones: List[str] = none,
            labels: dict = none,
            node_count_limits: NodeCountLimits = none,
            node_pool_properties: NodePoolProperties = none,
            strategy: Strategy = none,
            tags: dict = none,
            taints: List[Taint] = none,
            vm_sizes: VmSizes = none):
        self.name = name
        self.ocean_id = ocean_id
        self.auto_scale = auto_scale
        self.availability_zones = availability_zones
        self.labels = labels
        self.node_count_limits = node_count_limits
        self.node_pool_properties = node_pool_properties
        self.strategy = strategy
        self.tags = tags
        self.taints = taints
        self.vm_sizes = vm_sizes

# endregion

# region Ocean


class Ocean:
    """
    # Arguments 
    aks: Aks
    auto_scaler: AutoScaler
    controller_cluster_id: str
    health: Health
    name: str
    scheduling: Scheduling
    virtual_node_group_template: VirtualNodeGroupTemplate
    """

    def __init__(
            self,
            aks: Aks = none,
            auto_scaler: AutoScaler = none,
            controller_cluster_id: str = none,
            health: Health = none,
            name: str = none,
            scheduling: Scheduling = none,
            virtual_node_group_template: VirtualNodeGroupTemplate = none):
        self.aks = aks
        self.auto_scaler = auto_scaler
        self.controller_cluster_id = controller_cluster_id
        self.health = health
        self.name = name
        self.scheduling = scheduling
        self.virtual_node_group_template = virtual_node_group_template
# endregion

# region OceanRequest


class OceanRequest:
    def __init__(self, ocean: Ocean):
        self.cluster = ocean

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
# endregion

# region VNGRequest


class VNGRequest:
    def __init__(self, vng: VirtualNodeGroupTemplate):
        self.virtual_node_group = vng

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
# endregion

# region LaunchNewNodesRequest


class PreferredLifecycle(Enum):
    spot = "Spot"
    regular = "Regular"


class LaunchNewNodes:
    """
    # Arguments
    adjustment: int
    applicable_vm_sizes: List[str]
    availability_zones: List[str]
    min_cores_per_node: int
    min_memory_gi_b_per_node: float
    ocean_id: str
    preferred_lifecycle: PreferredLifecycle
    vng_ids: List[str]
    """

    def __init__(
            self,
            adjustment: int = none,
            applicable_vm_sizes: List[str] = none,
            availability_zones: List[str] = none,
            min_cores_per_node: int = none,
            min_memory_gi_b_per_node: float = none,
            ocean_id: str = none,
            preferred_lifecycle: PreferredLifecycle = none,
            vng_ids: List[str] = none):
        self.adjustment = adjustment
        self.applicable_vm_sizes = applicable_vm_sizes
        self.availability_zones = availability_zones
        self.min_cores_per_node = min_cores_per_node
        self.min_memory_gi_b_per_node = min_memory_gi_b_per_node
        self.ocean_id = ocean_id
        self.preferred_lifecycle = preferred_lifecycle
        self.vng_ids = vng_ids


class LaunchNewNodesRequest:
    def __init__(self, launch_new_nodes: LaunchNewNodes):
        self.adjustment = launch_new_nodes.adjustment
        self.applicable_vm_sizes = launch_new_nodes.applicable_vm_sizes
        self.availability_zones = launch_new_nodes.availability_zones
        self.min_cores_per_node = launch_new_nodes.min_cores_per_node
        self.min_memory_gi_b_per_node = launch_new_nodes.min_memory_gi_b_per_node
        self.ocean_id = launch_new_nodes.ocean_id
        self.preferred_lifecycle = launch_new_nodes.preferred_lifecycle
        self.vng_ids = launch_new_nodes.vng_ids

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
# endregion

# region AggregatedClusterCosts


class Type(Enum):
    label = "label"
    annotation = "annotation"


class Operator(Enum):
    equals = "equals"
    not_equals = "notEquals"
    exists = "exists"
    not_exists = "notExists"


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
    filter: Filter
    group_by: GroupBy
    start_time: str
    """

    def __init__(
            self,
            end_time: str = none,
            filter: Filter = none,
            group_by: GroupBy = GroupBy.namespace.value,
            start_time: str = none):
        self.end_time = end_time
        self.filter = filter
        self.group_by = group_by
        self.start_time = start_time


class AggregatedClusterCostRequest:
    def __init__(self, aggregated_cluster_costs: AggregatedClusterCosts = none):
        self.end_time = aggregated_cluster_costs.end_time
        self.start_time = aggregated_cluster_costs.start_time
        self.group_by = aggregated_cluster_costs.group_by
        self.filter = aggregated_cluster_costs.filter

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
# endregion


class Roll:
    """
    # Arguments
    comment: str
    batch_size_percentage: int
    batch_min_healthy_percentage: int
    respect_pdb: bool
    node_pool_names: List[str]
    vng_ids: List[str]
    respect_restrict_scale_down: bool
    node_names: List[str]

    """

    def __init__(
            self,
            comment: str = none,
            batch_size_percentage: int = none,
            batch_min_healthy_percentage: int = none,
            respect_pdb: bool = none,
            node_pool_names: List[str] = none,
            vng_ids: List[str] = none,
            respect_restrict_scale_down: bool = none,
            node_names: List[str] = none):
        self.comment = comment
        self.batch_size_percentage = batch_size_percentage
        self.batch_min_healthy_percentage = batch_min_healthy_percentage
        self.respect_pdb = respect_pdb
        self.node_pool_names = node_pool_names
        self.vng_ids = vng_ids
        self.respect_restrict_scale_down = respect_restrict_scale_down
        self.node_names = node_names


class ClusterRollInitiateRequest:
    def __init__(self, roll: Roll = none):
        self.comment = roll.comment
        self.batch_size_percentage = roll.batch_size_percentage
        self.batch_min_healthy_percentage = roll.batch_min_healthy_percentage
        self.respect_pdb = roll.respect_pdb
        self.node_pool_names = roll.node_pool_names
        self.vng_ids = roll.vng_ids
        self.respect_restrict_scale_down = roll.respect_restrict_scale_down
        self.node_names = roll.node_names

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

# region Migration


class Migration:
    """
    # Arguments
    node_names: List[str]
    node_pool_names: List[str]
    batch_size_percentage: int
    batch_min_healthy_percentage: int
    comment: str
    respect_pdb: bool
    respect_restrict_scale_down: bool
    should_evict_standalone_pods: bool
    should_terminate_nodes: bool
    """

    def __init__(
            self,
            node_names: List[str] = none,
            node_pool_names: List[str] = none,
            batch_size_percentage: int = none,
            batch_min_healthy_percentage: int = none,
            comment: str = none,
            respect_pdb: bool = none,
            respect_restrict_scale_down: bool = none,
            should_evict_standalone_pods: bool = none,
            should_terminate_nodes: bool = none,
    ):
        self.node_names = node_names
        self.node_pool_names = node_pool_names
        self.batch_size_percentage = batch_size_percentage
        self.batch_min_healthy_percentage = batch_min_healthy_percentage
        self.comment = comment
        self.respect_pdb = respect_pdb
        self.respect_restrict_scale_down = respect_restrict_scale_down
        self.should_evict_standalone_pods = should_evict_standalone_pods
        self.should_terminate_nodes = should_terminate_nodes


class MigrationRequest:
    def __init__(self, migration: Migration):
        self.node_names = migration.node_names
        self.node_pool_names = migration.node_pool_names
        self.batch_size_percentage = migration.batch_size_percentage
        self.batch_min_healthy_percentage = migration.batch_min_healthy_percentage
        self.comment = migration.comment
        self.respect_pdb = migration.respect_pdb
        self.respect_restrict_scale_down = migration.respect_restrict_scale_down
        self.should_evict_standalone_pods = migration.should_evict_standalone_pods
        self.should_terminate_nodes = migration.should_terminate_nodes

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
# endregion


class DetachNodes:
    """
    # Arguments
    node_names_to_detach: List[str]
    ocean_id: str
    """
    def __init__(self,
                 node_names_to_detach: List[str] = none,
                 ocean_id: str = none):
        self.node_names_to_detach = node_names_to_detach
        self.ocean_id = ocean_id


class DetachNodesRequest:
    def __init__(self, detach_nodes_obj: DetachNodes):
        self.node_names_to_detach = detach_nodes_obj.node_names_to_detach
        self.ocean_id = detach_nodes_obj.ocean_id

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class RightSizingFilter:
    """
    # Arguments
    attribute: Attribute
    namespaces: List[str]
    """
    def __init__(self,
                 attribute: Attribute = none,
                 namespaces: List[str] = none):
        self.attribute = attribute
        self.namespaces = namespaces


class FetchRightSizingRequest:
    def __init__(self, filter: RightSizingFilter):
        self.filter = filter

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
