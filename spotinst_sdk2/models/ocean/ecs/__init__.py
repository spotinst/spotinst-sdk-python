import json
from enum import Enum
from typing import List

none = "d3043820717d74d9a17694c176d39733"


class Down:
    """
    # Arguments
    evaluation_periods: int
    maxScale_down_percentage: int
    """
    def __init__(self,
                 evaluation_periods: int = none,
                 maxScale_down_percentage: int = none):
        self.evaluation_periods = evaluation_periods
        self.maxScale_down_percentage = maxScale_down_percentage


class Headroom:
    """
    # Arguments
    cpu_per_unit: int
    memory_per_unit: int
    num_of_units: int
    """
    def __init__(self,
                 cpu_per_unit: int = none,
                 memory_per_unit: int = none,
                 num_of_units: int = none):
        self.cpu_per_unit = cpu_per_unit
        self.memory_per_unit = memory_per_unit
        self.num_of_units = num_of_units


class ResourceLimits:
    """
    # Arguments
    max_memory_gib: int
    max_vcpu: int
    """
    def __init__(self,
                 max_memory_gib: int = none,
                 max_vcpu: int = none):
        self.max_memory_gib = max_memory_gib
        self.max_vcpu = max_vcpu


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
    should_scale_down_non_service_tasks: bool
    """
    def __init__(self,
                 auto_headroom_percentage: int = none,
                 cooldown: int = none,
                 down: Down = none,
                 enable_automatic_and_manual_headroom: bool = none,
                 headroom: Headroom = none,
                 is_auto_config: bool = none,
                 is_enabled: bool = none,
                 resource_limits: ResourceLimits = none,
                 should_scale_down_non_service_tasks: bool = none):
        self.auto_headroom_percentage = auto_headroom_percentage
        self.cooldown = cooldown
        self.down = down
        self.enable_automatic_and_manual_headroom = enable_automatic_and_manual_headroom
        self.headroom = headroom
        self.is_auto_config = is_auto_config
        self.is_enabled = is_enabled
        self.resource_limits = resource_limits
        self.should_scale_down_non_service_tasks = should_scale_down_non_service_tasks


class Unit(Enum):
    weight = "weight"
    instance = "instance"


class Capacity:
    """
    # Arguments
    maximum: int
    minimum: int
    target: int
    unit: Unit
    """
    def __init__(self,
                 maximum: int = none,
                 minimum: int = none,
                 target: int = none,
                 unit: Unit = none):
        self.maximum = maximum
        self.minimum = minimum
        self.target = target
        self.unit = unit


class Architectures(Enum):
    i386 = "i386"
    x86_64 = "x86_64"
    arm64 = "arm64"


class Categories(Enum):
    accelerated_computing = "Accelerated_computing"
    compute_optimized = "Compute_optimized"
    general_purpose = "General_purpose"
    memory_optimized = "Memory_optimized"
    storage_optimized = "Storage_optimized"


class DiskTypes(Enum):
    nvme = "NVMe"
    ebs = "EBS"
    ssd = "SSD"
    hdd = "HDD"


class Hypervisor(Enum):
    nitro = "nitro"
    xen = "xen"


class RootDeviceTypes(Enum):
    ebs = "ebs"
    instance_store = "instance-store"


class VirtualizationTypes(Enum):
    hvm = "hvm"
    paravirtual = "paravirtual"


class InstanceTypesFilters:
    """
    architectures: List[Architectures]
    categories: List[Categories]
    disk_types: List[DiskTypes]
    exclude_families: List[str]
    exclude_metal: bool
    hypervisor: List[Hypervisor]
    include_families: List[str]
    is_ena_supported: bool
    max_gpu: int
    max_memory_gi_b: float
    max_network_performance: int
    max_vcpu: int
    min_enis: int
    min_gpu: int
    min_memory_gi_b: float
    min_network_performance: int
    min_vcpu: int
    root_device_types: List[RootDeviceTypes]
    virtualization_types: List[VirtualizationTypes]
    """
    def __init__(self,
                 architectures: List[Architectures] = none,
                 categories: List[Categories] = none,
                 disk_types: List[DiskTypes] = none,
                 exclude_families: List[str] = none,
                 exclude_metal: bool = none,
                 hypervisor: List[Hypervisor] = none,
                 include_families: List[str] = none,
                 is_ena_supported: bool = none,
                 max_gpu: int = none,
                 min_memory_gi_b: float = none,
                 min_network_performance: int = none,
                 min_vcpu: int = none,
                 root_device_types: List[RootDeviceTypes] = none,
                 virtualization_types: List[VirtualizationTypes] = none):
        self.architectures = architectures
        self.categories = categories
        self.disk_types = disk_types
        self.exclude_families = exclude_families
        self.exclude_metal = exclude_metal
        self.hypervisor = hypervisor
        self.include_families = include_families
        self.is_ena_supported = is_ena_supported
        self.max_gpu= max_gpu
        self.min_memory_gi_b = min_memory_gi_b
        self.min_network_performance = min_network_performance
        self.min_vcpu = min_vcpu
        self.root_device_types = root_device_types
        self.virtualization_types = virtualization_types


class InstanceTypes:
    """
    # Arguments
    blacklist: List[str]
    filters: InstanceTypesFilters
    whitelist: List[str]
    """
    def __init__(self,
                 blacklist: List[str] = none,
                 filters: InstanceTypesFilters = none,
                 whitelist: List[str] = none):
        self.blacklist = blacklist
        self.filters = filters
        self.whitelist = whitelist


class DynamicVolumeSize:
    """
    # Arguments
    base_size: int
    resource: str
    size_per_resource_unit: int
    """
    def __init__(self,
                 base_size: int = none,
                 resource: str = none,
                 size_per_resource_unit: int = none):
        self.base_size = base_size
        self.resource = resource
        self.size_per_resource_unit = size_per_resource_unit


class EBS:
    """
    # Arguments
    delete_on_termination: bool
    dynamic_volume_size: DynamicVolumeSize
    encrypted: bool
    iops: int
    kms_key_id: str
    snapshot_id: str
    throughput: int
    volume_size: int
    volume_type: str
    """
    def __init__(self,
                 delete_on_termination: bool = none,
                 dynamic_volume_size: DynamicVolumeSize = none,
                 encrypted: bool = none,
                 iops: int = none,
                 kms_key_id: str = none,
                 snapshot_id: str = none,
                 throughput: int = none,
                 volume_size: int = none,
                 volume_type: str = none):
        self.delete_on_termination = delete_on_termination
        self.dynamic_volume_size = dynamic_volume_size
        self.encrypted = encrypted
        self.iops = iops
        self.kms_key_id = kms_key_id
        self.snapshot_id = snapshot_id
        self.throughput = throughput
        self.volume_size = volume_size
        self.volume_type = volume_type


class BlockDeviceMappings:
    """
    # Arguments
    device_name: str
    ebs: EBS
    """
    def __init__(self,
                 device_name: str = none,
                 ebs: EBS = none):
        self.device_name = device_name
        self.ebs = ebs


class IamInstanceProfile:
    """
    # Arguments
    arn: str
    """
    def __init__(self,
                 arn: str = none):
        self.arn = arn


class HttpEndpoint(Enum):
    disabled = "disabled"
    enabled = "enabled"


class HttpTokens(Enum):
    optional = "optional"
    required = "required"


class InstanceMetadataOptions:
    """
    # Arguments
    http_endpoint: HttpEndpoint
    http_put_response_hop_limit: int
    http_tokens: HttpTokens
    """
    def __init__(self,
                 http_endpoint: HttpEndpoint = none,
                 http_put_response_hop_limit: int = none,
                 http_tokens: HttpTokens = none):
        self.http_endpoint = http_endpoint
        self.http_put_response_hop_limit = http_put_response_hop_limit
        self.http_tokens = http_tokens


class Tags:
    """
    # Arguments
    tag_key: str
    tag_value: str
    """
    def __init__(self,
                 tag_key: str = none,
                 tag_value: str = none):
        self.tag_key = tag_key
        self.tag_value = tag_value


class LaunchSpecification:
    """
    # Arguments
    associate_ipv6_address: bool
    associate_public_ip_address: bool
    block_device_mappings: List[BlockDeviceMappings]
    ebs_optimized: bool
    iam_instance_profile: IamInstanceProfile
    image_id: str
    instance_metadata_options: InstanceMetadataOptions
    monitoring: bool
    security_group_ids: List[str]
    tags: List[Tags]
    use_as_template_only: bool
    user_data: str
    """
    def __init__(self,
                 associate_ipv6_address: bool = none,
                 associate_public_ip_address: bool = none,
                 block_device_mappings: List[BlockDeviceMappings] = none,
                 ebs_optimized: bool = none,
                 iam_instance_profile: IamInstanceProfile = none,
                 image_id: str = none,
                 instance_metadata_options: InstanceMetadataOptions = none,
                 monitoring: bool = none,
                 security_group_ids: List[str] = none,
                 tags: List[Tags] = none,
                 use_as_template_only: bool = none,
                 user_data: str = none):
        self.associate_ipv6_address = associate_ipv6_address
        self.associate_public_ip_address = associate_public_ip_address
        self.block_device_mappings = block_device_mappings
        self.ebs_optimized = ebs_optimized
        self.iam_instance_profile = iam_instance_profile
        self.image_id = image_id
        self.instance_metadata_options = instance_metadata_options
        self.monitoring = monitoring
        self.security_group_ids = security_group_ids
        self.tags = tags
        self.use_as_template_only = use_as_template_only
        self.user_data = user_data


class OptimizeImages:
    """
    # Arguments
    perform_at: str
    should_optimize_ecs_ami: bool
    time_windows: List[str]
    """
    def __init__(self,
                 perform_at: str = none,
                 should_optimize_ecs_ami: bool = none,
                 time_windows: List[str] = none):
        self.perform_at = perform_at
        self.should_optimize_ecs_ami = should_optimize_ecs_ami
        self.time_windows = time_windows


class Compute:
    """
    # Arguments
    instance_types: InstanceTypes
    launch_specification: LaunchSpecification
    optimize_images: OptimizeImages
    subnet_ids: List[str]
    """
    def __init__(self,
                 instance_types: InstanceTypes = none,
                 launch_specification: LaunchSpecification = none,
                 optimize_images: OptimizeImages = none,
                 subnet_ids: List[str] = none):
        self.instance_types = instance_types
        self.launch_specification = launch_specification
        self.optimize_images = optimize_images
        self.subnet_ids = subnet_ids


class S3:
    """
    # Arguments
    id: str
    """
    def __init__(self,
                 id: str = none):
        self.id = id


class Export:
    """
    # Arguments
    s3: S3
    """
    def __init__(self,
                 s3: S3 = none):
        self.s3 = s3


class Logging:
    """
    # Arguments
    export: Export
    """
    def __init__(self,
                 export: Export = none):
        self.export = export


class ShutdownHours:
    """
    # Arguments
    is_enabled: bool
    time_windows: List[str]
    """
    def __init__(self,
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
    """
    def __init__(self,
                 batch_min_healthy_percentage: int = none,
                 batch_size_percentage: int = none,
                 comment: str = none):
        self.batch_min_healthy_percentage = batch_min_healthy_percentage
        self.batch_size_percentage = batch_size_percentage
        self.comment = comment


class Parameters:
    """
    # Arguments
    cluster_roll: ClusterRoll
    """
    def __init__(self,
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
    def __init__(self,
                 cron_expression: str = none,
                 is_enabled: bool = none,
                 parameters: Parameters = none,
                 task_type: str = none):
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
    def __init__(self,
                 shutdown_hours: ShutdownHours = none,
                 tasks: List[Tasks] = none):
        self.shutdown_hours = shutdown_hours
        self.tasks = tasks


class AvailabilityVsCost(Enum):
    cost_oriented = "CostOriented"
    balanced = "balanced"


class ClusterOrientation:
    """
    # Arguments
    availability_vs_cost: AvailabilityVsCost
    """
    def __init__(self,
                 availability_vs_cost: AvailabilityVsCost = none):
        self.availability_vs_cost = availability_vs_cost


class Strategy:
    """
    # Arguments
    cluster_orientation: ClusterOrientation
    draining_timeout: int
    fallback_to_od: bool
    spot_percentage: int
    utilize_commitments: bool
    utilize_reserved_instances: bool
    """
    def __init__(self,
                 cluster_orientation: ClusterOrientation = none,
                 draining_timeout: int = none,
                 fallback_to_od: bool = none,
                 spot_percentage: int = none,
                 utilize_commitments: bool = none,
                 utilize_reserved_instances: bool = none):
        self.cluster_orientation = cluster_orientation
        self.draining_timeout = draining_timeout
        self.fallback_to_od = fallback_to_od
        self.spot_percentage = spot_percentage
        self.utilize_commitments = utilize_commitments
        self.utilize_reserved_instances = utilize_reserved_instances


class Ocean:
    """
    # Arguments
    auto_scaler: AutoScaler
    capacity: Capacity
    cluster_name: str
    compute: Compute
    logging: Logging
    name: str
    region: str
    scheduling: Scheduling
    strategy: Strategy
    """
    def __init__(self,
                 auto_scaler: AutoScaler = none,
                 capacity: Capacity = none,
                 cluster_name: str = none,
                 compute: Compute = none,
                 logging: Logging = none,
                 name: str = none,
                 region: str = none,
                 scheduling: Scheduling = none,
                 strategy: Strategy = none):
        self.auto_scaler = auto_scaler
        self.capacity = capacity
        self.cluster_name = cluster_name
        self.compute = compute
        self.logging = logging
        self.name = name
        self.region = region
        self.scheduling = scheduling
        self.strategy = strategy


class OceanRequest:
    def __init__(self, ocean: Ocean):
        self.cluster = ocean

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class ImportCluster:
    """
    # Arguments
    instance_id: str
    name: str
    region: str
    """
    def __init__(self,
                 instance_id: str = none,
                 name: str = none,
                 region: str = none):
        self.instance_id = instance_id
        self.name = name
        self.region = region


class ImportClusterRequest:
    def __init__(self, import_cluster: ImportCluster):
        self.region = import_cluster.region
        self.name = import_cluster.name
        self.instance_id = import_cluster.instance_id

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class InstanceTypesFilterRequest:
    def __init__(self, filters: InstanceTypesFilters):
        self.filters = filters

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class Roll:
    """
    # Arguments
    batch_min_healthy_percentage: int
    batch_size_percentage: int
    comment: str
    instance_ids: List[str]
    launch_spec_ids: List[str]
    """

    def __init__(
            self,
            batch_min_healthy_percentage: int = none,
            batch_size_percentage: int = none,
            comment: str = none,
            launch_spec_ids: List[str] = none,
            instance_ids: List[str] = none):
        self.batch_min_healthy_percentage = batch_min_healthy_percentage
        self.batch_size_percentage = batch_size_percentage
        self.comment = comment
        self.instance_ids = instance_ids
        self.launch_spec_ids = launch_spec_ids


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


class DetachInstances:
    """
    # Arguments
    instances_to_detach: List[str]
    should_decrement_target_capacity: bool
    should_terminate_instances: bool
    """

    def __init__(
            self,
            instances_to_detach: List[str] = none,
            should_decrement_target_capacity: bool = none,
            should_terminate_instances: bool = none):
        self.instances_to_detach = instances_to_detach
        self.should_decrement_target_capacity = should_decrement_target_capacity
        self.should_terminate_instances = should_terminate_instances


class DetachInstancesRequest:
    def __init__(self, detachInstances: DetachInstances):
        self.instances_to_detach = detachInstances.instances_to_detach
        self.should_decrement_target_capacity = detachInstances.should_decrement_target_capacity
        self.should_terminate_instances = detachInstances.should_terminate_instances

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class Attributes:
    """
    # Arguments
    key: str
    value: str
    """
    def __init__(self,
                 key: str = none,
                 value: str = none):
        self.key = key
        self.value = value


class AutoScale:
    """
    # Arguments
    headrooms: List[Headrooms]
    """
    def __init__(self,
                 headrooms: List[Headroom] = none):
        self.headrooms = headrooms


class Images:
    """
    # Arguments
    id: str
    """
    def __init__(self,
                 id: str = none):
        self.id = id


class VngTasks:
    """
    # Arguments
    config: List[Headroom]
    cron_expression: str
    is_enabled: bool
    task_type: str
    """
    def __init__(self,
                 config: List[Headroom] = none,
                 cron_expression: str = none,
                 is_enabled: bool = none,
                 task_type: str = none):
        self.config = config
        self.cron_expression = cron_expression
        self.is_enabled = is_enabled
        self.task_type = task_type


class VngScheduling:
    """
    # Arguments
    tasks: List[VngTasks]
    """
    def __init__(self,
                 tasks: List[VngTasks]):
        self.tasks = tasks


class VirtualNodeGroup:
    """
    # Arguments
    attributes: List[Attributes]
    auto_scale: AutoScale
    block_device_mappings: List[BlockDeviceMappings]
    iam_instance_profile: List[str]
    image_id: str
    images: List[Images]
    instance_metadata_options: InstanceMetadataOptions
    instance_types: List[str]
    name: str
    ocean_id: str
    preferred_spot_types: List[str]
    restrict_scale_down: bool
    scheduling: VngScheduling
    security_group_ids: List[str]
    strategy: Strategy
    subnet_ids: List[str]
    tags: List[Tags]
    user_data: str
    """
    def __init__(self,
                 attributes: List[Attributes] = none,
                 auto_scale: AutoScale = none,
                 block_device_mappings: List[BlockDeviceMappings] = none,
                 iam_instance_profile: List[str] = none,
                 image_id: str = none,
                 images: List[Images] = none,
                 instance_metadata_options: InstanceMetadataOptions = none,
                 instance_types: List[str] = none,
                 name: str = none,
                 ocean_id: str = none,
                 preferred_spot_types: List[str] = none,
                 restrict_scale_down: bool = none,
                 scheduling: VngScheduling = none,
                 security_group_ids: List[str] = none,
                 strategy: Strategy = none,
                 subnet_ids: List[str] = none,
                 tags: List[Tags] = none,
                 user_data: str = none):
        self.attributes = attributes
        self.auto_scale = auto_scale
        self.block_device_mappings = block_device_mappings
        self.iam_instance_profile = iam_instance_profile
        self.image_id = image_id
        self.images = images
        self.instance_metadata_options = instance_metadata_options
        self.instance_types = instance_types
        self.name = name
        self.ocean_id = ocean_id
        self.preferred_spot_types = preferred_spot_types
        self.restrict_scale_down = restrict_scale_down
        self.scheduling = scheduling
        self.security_group_ids = security_group_ids
        self.strategy = strategy
        self.subnet_ids = subnet_ids
        self.tags = tags
        self.user_data = user_data


class VNGRequest:
    def __init__(self, vng: VirtualNodeGroup):
        self.launch_spec = vng

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class ImportFargateToExistingOceanCluster:
    """
    # Arguments
    services: List[str]
    simple_new_service_names: bool
    """
    def __init__(self,
                 services: List[str] = none,
                 simple_new_service_names: bool = none):
        self.services = services
        self.simple_new_service_names = simple_new_service_names


class ImportFargateToExistingOceanClusterRequest:
    def __init__(self, import_fargate_to_cluster: ImportFargateToExistingOceanCluster):
        self.services = import_fargate_to_cluster.services
        self.simple_new_service_names = import_fargate_to_cluster.simple_new_service_names

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class ImportFargateToNewOceanCluster:
    """
    # Arguments
    ecs_cluster_name: str
    key_pair: str
    ocean_cluster_name: str
    region: str
    services: List[str]
    tags: List[Tags]
    """
    def __int__(self,
                ecs_cluster_name: str = none,
                key_pair: str = none,
                ocean_cluster_name: str = none,
                region: str = none,
                services: List[str] = none,
                tags: List[Tags] = none):
        self.ecs_cluster_name = ecs_cluster_name
        self.key_pair = key_pair
        self.ocean_cluster_name = ocean_cluster_name
        self.region = region
        self.services = services
        self.tags = tags


class Operator(Enum):
    equals = "equals"
    not_equals = "notEquals"
    exists = "exists"
    does_not_exist = "doesNotExist"


class Attribute:
    """
    # Arguments
    key: str
    operator: Operator
    value: str
    """

    def __init__(
            self,
            key: str = none,
            operator: Operator = none,
            value: str = none):
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


class Filter:
    """
    # Arguments
    conditions: Conditions
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


class LaunchInstancesRequest:
    def __init__(self, amount: int = none):
        self.launch_request = dict(amount=amount)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
