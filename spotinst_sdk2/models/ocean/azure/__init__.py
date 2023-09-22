import json
from enum import Enum
from typing import List

none = "d3043820717d74d9a17694c176d39733"

class OceanAKS:
    '''
    # Arguments
    cluster_name: str
    infrastructure_resource_group_name: str
    region: str
    resource_group_name: str
    '''
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
        self.max_memory_gib=max_memory_gib
        self.max_v_cpu=max_v_cpu

class Down:
    """
    # Arguments
    max_scale_down_percentage: int
    """
    def __init__(
            self,
            max_scale_down_percentage: int = none):
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
    '''
    # Arguments
    down: Down
    headroom: AutoScalerHeadroom
    is_enabled: bool
    resource_limits: ResourceLimits
    '''
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

class ShutdownHours:
    '''
    # Arguments
    is_enabled: bool
    time_windows: List[str]
    '''
    def __init__(
            self,
            is_enabled: bool = none,
            time_windows: List[str] = none):
        self.is_enabled = is_enabled
        self.time_windows = time_windows

class Scheduling:
    '''
    # Arguments
    shutdown_hours: ShutdownHours
    '''
    def __init__(
            self,
            shutdown_hours: ShutdownHours = none):
        self.shutdown_hours = shutdown_hours

class Health:
    '''
    # Arguments
    grace_period: int
    '''
    def __init__(
            self,
            grace_period: int = none):
        self.grace_period = grace_period

class AutoScaleHeadroom:
    '''
    # Arguments
    cpu_per_unit: int
    gpu_per_unit: int
    memory_per_unit: int
    num_of_units: int
    '''
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
    '''
    # Arguments
    headrooms: List[AutoScaleHeadroom]
    '''
    def __init__(
            self,
            headrooms: List[AutoScaleHeadroom] = none):
        self.headrooms = headrooms                

class Labels:
    '''
    # Arguments
    key: str
    '''
    def __init__(
            self,
            key: str = none):
        self.key = key  

class NodeCountLimits:
    '''
    # Arguments
    max_count: int
    min_count: int
    '''
    def __init__(
            self,
            max_count: int = none,
            min_count: int = none):
        self.max_count = max_count
        self.min_count = min_count

class OsType(Enum):
    linux="Linux"
    windows="Windows"         

class OsDiskType(Enum):
    managed="Managed"
    ephemereal="Ephemereal"        

class OsSKU(Enum):
    ubuntu="Ubuntu"
    azure_linux="AzureLinux"
    cbl_mariner="CBLMariner"
    windows2019="Windows2019"
    windows2022="Windows2022"

class NodePoolProperties:
    '''
    # Arguments
    enable_node_public_ip: bool
    kubernetes_version: str
    max_pods_per_node: int
    os_disk_size_gB: int
    os_disk_type: OsDiskType
    os_sKU: OsSKU
    os_type: OsType
    '''
    def __init__(
            self,
            enable_node_public_ip: bool = none,
            kubernetes_version: str = none,
            max_pods_per_node: int = none,
            os_disk_size_gB: int = none,
            os_disk_type: OsDiskType = none,
            os_sKU: OsSKU = none,
            os_type: OsType = none):
        self.enable_node_public_ip = enable_node_public_ip
        self.kubernetes_version = kubernetes_version
        self.max_pods_per_node = max_pods_per_node
        self.os_disk_size_gB = os_disk_size_gB
        self.os_disk_type =   os_disk_type
        self.os_sKU = os_sKU
        self.os_type = os_type  

class Strategy:
    '''
    # Arguments
    fallback_to_oD: bool
    spot_percentage: int
    '''

    def __init__(
            self,
            fallback_to_oD: bool = none,
            spot_percentage: int = none):
        self.fallback_to_oD = fallback_to_oD
        self.spot_percentage = spot_percentage

class Tags:
    '''
    # Arguments
    key: str
    value: str
    '''
    def __init__(
            self,
            key: str = none,
            value:str = none):
        self.key = key
        self.value = value                  

class Effect(Enum):
    no_schedule="NoSchedule"
    prefer_no_schedule="PreferNoSchedule"
    no_execute="NoExecute"
    prefer_no_execute="PreferNoExecute"

class Taints:
    '''
    # Arguments
    key: str
    value: str
    effect: Effect
    '''
    def __init__(
            self,
            key: str = none,
            value:str = none,
            effect:Effect = none):
        self.key = key
        self.value = value
        self.effect = effect

class Architectures(Enum):
    x86_64="X86_64" 
    intel64="INTEL64" 
    amd64="AMD64" 
    arm64="ARM64"

class AcceleratedNetworking(Enum):
    enabled="Enabled"
    disabled="Disabled"

class DiskPerformance(Enum):
    standard="Standard"
    premium="Premium"

class VmTypes(Enum):
    general_purpose="generalPurpose" 
    memory_optimized="memoryOptimized" 
    compute_optimized="computeOptimized" 
    high_performance_compute="highPerformanceCompute" 
    storage_optimized="storageOptimized"
    gpu="GPU"                                

class Filters:
    '''
    # Arguments
    accelerated_networking: AcceleratedNetworking
    disk_performance: DiskPerformance
    architectures: List[Architectures]
    exclude_series: List[str]
    max_memory_giB: float
    max_vCpu: int
    min_memory_giB: float
    min_vCpu: int
    min_gpu: int
    max_gpu: int
    min_data: int
    min_nICs: int
    series: List[str]
    vm_types: List[VmTypes]
    '''
    def __init__(
            self,
            accelerated_networking: AcceleratedNetworking = none,
            disk_performance: DiskPerformance = none,
            architectures: List[Architectures] = none,
            exclude_series: List[str] = none,
            max_memory_giB: float = none,
            max_vCpu: int = none,
            min_memory_giB: float = none,
            min_vCpu: int = none,
            min_gpu: int = none,
            max_gpu: int = none,
            min_data: int = none,
            min_nICs: int = none,
            series: List[str] = none,
            vm_types: List[VmTypes] = none):
        self.accelerated_networking=accelerated_networking
        self.disk_performance=disk_performance
        self.architectures = architectures
        self.exclude_series = exclude_series
        self.max_memory_giB = max_memory_giB
        self.max_vCpu = max_vCpu
        self.min_memory_giB = min_memory_giB
        self.min_vCpu = min_vCpu
        self.min_gpu = min_gpu
        self.max_gpu = max_gpu
        self.min_data=min_data
        self.min_nICs=min_nICs
        self.series = series
        self.vm_types = vm_types

class VmSizes:
    '''
    # Arguments
    filters: Filters
    '''
    def __init__(
            self,
            filters: Filters = none):
        self.filters = filters         

class VirtualNodeGroupTemplate:
    '''
    # Arguments
    name: str
    ocean_id: str 
    auto_scale: AutoScale
    availabilty_zones: List[str]
    labels: Labels
    node_count_limits: NodeCountLimits
    node_pool_properties: NodePoolProperties
    strategy: Strategy
    tags: Tags
    taints: Taints
    vm_sizes: VmSizes
    '''

    def __init__(
            self,
            name: str = none,
            ocean_id: str = none,
            auto_scale: AutoScale = none,
            availabilty_zones: List[str] = none,
            labels: Labels = none,
            node_count_limits: NodeCountLimits = none,
            node_pool_properties: NodePoolProperties = none,
            strategy: Strategy = none,
            tags: Tags = none,
            taints: Taints = none,
            vm_sizes: VmSizes = none):
        self.name=name
        self.ocean_id=ocean_id
        self.auto_scale=auto_scale
        self.availability_zones=availabilty_zones
        self.labels=labels
        self.node_count_limits=node_count_limits
        self.node_pool_properties=node_pool_properties
        self.strategy=strategy
        self.tags=tags
        self.taints=taints
        self.vm_sizes=vm_sizes              
       
class Ocean:
    '''
    # Arguments 
    aks: OceanAKS
    auto_scaler: AutoScaler
    controller_cluster_id: str
    health: Health
    name: str
    scheduling: Scheduling
    virtual_node_group_template: VirtualNodeGroupTemplate
    '''

    def __init__(
            self,
            aks: OceanAKS = none,
            auto_scaler: AutoScaler = none,
            controller_cluster_id: str = none,
            health: Health = none,
            name: str = none,
            scheduling: Scheduling = none,
            virtual_node_group_template: VirtualNodeGroupTemplate = none):
        self.aks=aks
        self.auto_scaler=auto_scaler
        self.controller_cluster_id=controller_cluster_id
        self.health=health
        self.name=name
        self.scheduling=scheduling
        self.virtual_node_group_template=virtual_node_group_template

class LaunchNewNodes:
    '''
    # Arguments
    adjustment: int
    applicable_vm_sizes: List[str]
    availability_zones: List[str]
    min_cores_per_node: int
    min_memory_giB_per_node: float
    ocean_id: str
    preferred_lifecycle: str
    vngIds: List[str]
    '''
    def __init__(
            self,
            adjustment: int = none,
            applicable_vm_sizes: List[str] = none,
            availability_zones: List[str] = none,
            min_cores_per_node: int = none,
            min_memory_giB_per_node: float = none,
            ocean_id: str = none,
            preferred_lifecycle: str = none,
            vngIds: List[str] = none):
        self.adjustment=adjustment
        self.applicable_vm_sizes=applicable_vm_sizes
        self.availability_zones=availability_zones
        self.min_cores_per_node=min_cores_per_node
        self.min_memory_giB_per_node=min_memory_giB_per_node
        self.ocean_id=ocean_id
        self.preferred_lifecycle=preferred_lifecycle
        self.vngIds=vngIds

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
class LaunchNewNodesRequest:
    def __init__(self, launch_new_nodes: LaunchNewNodes):
        self.adjustment=launch_new_nodes.adjustment
        self.applicable_vm_sizes=launch_new_nodes.applicable_vm_sizes
        self.availability_zones=launch_new_nodes.availability_zones
        self.min_cores_per_node=launch_new_nodes.min_cores_per_node
        self.min_memory_giB_per_node=launch_new_nodes.min_memory_giB_per_node
        self.ocean_id=launch_new_nodes.ocean_id
        self.preferred_lifecycle=launch_new_nodes.preferred_lifecycle
        self.vngIds=launch_new_nodes.vngIds

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
# endregion

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

class AllMatch:
    """
    # Arguments
    all_matches:  List[Attribute]
    """
    def __init__(
            self,
            all_matches:  List[Attribute] = none):
        self.all_matches = all_matches


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
            conditions: Conditions = none):
        self.conditions = conditions


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