import json
from enum import Enum
from typing import List

none = "d3043820717d74d9a17694c176d39733"


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


class AgressiveScaleDown:
    """
    # Arguments
    is_enabled: bool
    """

    def __init__(
            self,
            is_enabled: bool = none):
        self.is_enabled = is_enabled


class Down:
    """
    # Arguments
    aggressive_scale_down: AgressiveScaleDown
    max_scale_down_percentage: int
    """

    def __init__(
            self,
            max_scale_down_percentage: int = none,
            aggressive_scale_down: AgressiveScaleDown = none):
        self.max_scale_down_percentage = max_scale_down_percentage
        self.aggressive_scale_down = aggressive_scale_down


class Headroom:
    """
    # Arguments
    cpu_per_unit: int
    memory_per_unit: int
    gpu_per_unit: int
    num_of_units: int
    """

    def __init__(
            self,
            cpu_per_unit: int = none,
            memory_per_unit: int = none,
            gpu_per_unit: int = none,
            num_of_units: int = none):
        self.cpu_per_unit = cpu_per_unit
        self.memory_per_unit = memory_per_unit
        self.gpu_per_unit = gpu_per_unit
        self.num_of_units = num_of_units


class AutoScaler:
    """
    # Arguments
    is_enabled: bool
    cooldown: int
    resource_limits: ResourceLimits
    down: Down
    headroom: Headroom
    is_auto_config: bool
    auto_headroom_percentage: int
    enable_automatic_and_manual_headroom: bool
    extended_resource_definitions: List[str]
    """

    def __init__(
            self,
            is_enabled: bool = none,
            cooldown: int = none,
            resource_limits: ResourceLimits = none,
            down: Down = none,
            headroom: Headroom = none,
            is_auto_config: bool = none,
            auto_headroom_percentage: int = none,
            enable_automatic_and_manual_headroom: bool = none,
            extended_resource_definitions: List[str] = none):
        self.is_enabled = is_enabled
        self.cooldown = cooldown
        self.resource_limits = resource_limits
        self.down = down
        self.headroom = headroom
        self.is_auto_config = is_auto_config
        self.auto_headroom_percentage = auto_headroom_percentage
        self.enable_automatic_and_manual_headroom = enable_automatic_and_manual_headroom
        self.extended_resource_definitions = extended_resource_definitions
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
            minimum: int = none,
            maximum: int = none,
            target: int = none):
        self.minimum = minimum
        self.maximum = maximum
        self.target = target
# endregion


# region Strategy
class AvailabilityVsCost(Enum):
    cost_oriented = "costOriented"
    balanced = "balanced"
    cheapest = "cheapest"


class ClusterOrientation:
    """
    # Arguments
    availability_vs_cost: AvailabilityVsCost
    """

    def __init__(
            self,
            availability_vs_cost: AvailabilityVsCost = none):
        self.availability_vs_cost = availability_vs_cost


class SpreadNodesBy(Enum):
    vcpu = "vcpu"
    count = "count"


class Strategy:
    """
    # Arguments
    utilize_reserved_instances: bool
    fallback_to_od: bool
    spot_percentage: int
    grace_period: int
    draining_timeout: int
    utilize_commitments: bool
    cluster_orientation: ClusterOrientation
    spread_nodes_by: SpreadNodesBy
    """

    def __init__(
            self,
            utilize_reserved_instances: bool = none,
            fallback_to_od: bool = none,
            spot_percentage: int = none,
            grace_period: int = none,
            draining_timeout: int = none,
            utilize_commitments: bool = none,
            cluster_orientation: ClusterOrientation = none,
            spread_nodes_by: SpreadNodesBy = none):
        self.utilize_reserved_instances = utilize_reserved_instances
        self.fallback_to_od = fallback_to_od
        self.spot_percentage = spot_percentage
        self.grace_period = grace_period
        self.draining_timeout = draining_timeout
        self.utilize_commitments = utilize_commitments
        self.cluster_orientation = cluster_orientation
        self.spread_nodes_by = spread_nodes_by
# endregion


# region Scheduling
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
            respect_pdb: bool = none):
        self.batch_min_healthy_percentage = batch_min_healthy_percentage
        self.batch_size_percentage = batch_size_percentage
        self.comment = comment
        self.respect_pdb = respect_pdb


class AmiAutoUpdate:
    """
    # Arguments
    patch: bool
    minor_version: bool
    apply_roll: bool
    cluster_roll: ClusterRoll
    """

    def __init__(
            self,
            patch: bool = none,
            minor_version: bool = none,
            apply_roll: bool = none,
            cluster_roll: ClusterRoll = none):
        self.patch = patch
        self.minor_version = minor_version
        self.apply_roll = apply_roll
        self.cluster_roll = cluster_roll


class Parameters:
    """
    # Arguments
    cluster_roll: ClusterRoll
    ami_auto_update: AmiAutoUpdate
    """

    def __init__(
            self,
            ami_auto_update: AmiAutoUpdate = none,
            cluster_roll: ClusterRoll = none):
        self.cluster_roll = cluster_roll
        self.ami_auto_update = ami_auto_update


class TaskType(Enum):
    cluster_roll = "clusterRoll"
    ami_auto_update = "amiAutoUpdate"


class Tasks:
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


class Scheduling:
    """
    # Arguments
    tasks: List[Tasks]
    shutdown_hours: ShutdownHours
    """

    def __init__(
            self,
            tasks: List[Tasks] = none,
            shutdown_hours: ShutdownHours = none):
        self.tasks = tasks
        self.shutdown_hours = shutdown_hours
# endregion


# region Security
class ContainerImage:
    """
    # Arguments
    approved_images: List[str]
    """

    def __init__(
            self,
            approved_images: List[str] = none):
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


# region Compute
# region InstanceTypes
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
    # Arguments
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

    def __init__(
            self,
            architectures: List[Architectures] = none,
            categories: List[Categories] = none,
            disk_types: List[DiskTypes] = none,
            exclude_families: List[str] = none,
            exclude_metal: bool = none,
            hypervisor: List[Hypervisor] = none,
            include_families: List[str] = none,
            is_ena_supported: bool = none,
            max_gpu: int = none,
            max_memory_gi_b: float = none,
            max_network_performance: int = none,
            max_vcpu: int = none,
            min_enis: int = none,
            min_gpu: int = none,
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
        self.max_gpu = max_gpu
        self.max_memory_gi_b = max_memory_gi_b
        self.max_network_performance = max_network_performance
        self.max_vcpu = max_vcpu
        self.min_enis = min_enis
        self.min_gpu = min_gpu
        self.min_memory_gi_b = min_memory_gi_b
        self.min_network_performance = min_network_performance
        self.min_vcpu = min_vcpu
        self.root_device_types = root_device_types
        self.virtualization_types = virtualization_types


class InstanceTypes:
    """
    # Arguments
    blacklist: List[str]
    whitelist: List[str]
    filters: InstanceTypesFilters
    """

    def __init__(
            self,
            blacklist: List[str] = none,
            whitelist: List[str] = none,
            filters: InstanceTypesFilters = none):
        self.blacklist = blacklist
        self.whitelist = whitelist
        self.filters = filters
# endregion


# region LaunchSpecification
class DynamicVolumeSize:
    """
    # Arguments
    base_size: int
    resource: str
    size_per_resource_unit: int
    """

    def __init__(
            self,
            base_size: int = none,
            resource: str = none,
            size_per_resource_unit: int = none):
        self.base_size = base_size
        self.resource = resource
        self.size_per_resource_unit = size_per_resource_unit


class EBS:
    """
    # Arguments
    throughput: int
    delete_on_termination: bool
    encrypted: bool
    iops: int
    kms_key_id: str
    snapshot_id:  str
    volume_type: str
    volume_size: int
    dynamic_volume_size: DynamicVolumeSize
    """

    def __init__(
            self,
            throughput: int = none,
            delete_on_termination: bool = none,
            encrypted: bool = none,
            iops: int = none,
            kms_key_id: str = none,
            snapshot_id: str = none,
            volume_type: str = none,
            volume_size: int = none,
            dynamic_volume_size: DynamicVolumeSize = none):
        self.throughput = throughput
        self.delete_on_termination = delete_on_termination
        self.encrypted = encrypted
        self.iops = iops
        self.kms_key_id = kms_key_id
        self.snapshot_id = snapshot_id
        self.volume_type = volume_type
        self.volume_size = volume_size
        self.dynamic_volume_size = dynamic_volume_size


class BlockDeviceMappings:
    """
    # Arguments
    device_name: str
    ebs: EBS
    """

    def __init__(
            self,
            device_name: str = none,
            ebs: EBS = none):
        self.device_name = device_name
        self.ebs = ebs


class IamInstanceProfile:
    """
    # Arguments
    name: str
    arn: str
    """

    def __init__(
            self,
            name: str = none,
            arn: str = none):
        self.name = name
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

    def __init__(
            self,
            http_endpoint: HttpEndpoint = none,
            http_put_response_hop_limit: int = none,
            http_tokens: HttpTokens = none):
        self.http_endpoint = http_endpoint
        self.http_put_response_hop_limit = http_put_response_hop_limit
        self.http_tokens = http_tokens


class LoadBalancerType(Enum):
    classic = "CLASSIC"
    target_group = "TARGET_GROUP"


class LoadBalancer:
    """
    # Arguments
    arn: str
    name: str
    type: str
    """

    def __init__(
            self,
            arn: str = none,
            name: str = none,
            type: LoadBalancerType = none):
        self.arn = arn
        self.name = name
        self.type = type


class Tags:
    """
    # Arguments
    tag_key: str
    tag_value: str
    """

    def __init__(
            self,
            tag_key: str = none,
            tag_value: str = none):
        self.tag_key = tag_key
        self.tag_value = tag_value


class Volumes:
    """
    # Arguments
    should_tag: str
    """

    def __init__(
            self,
            should_tag: bool = none):
        self.should_tag = should_tag


class ResourceTagSpecification:
    """
    # Arguments
    volumes: Volumes
    """

    def __init__(
            self,
            volumes: Volumes = none):
        self.volumes = volumes


class LaunchSpecifications:
    """
    # Arguments
    associate_ipv6_address: bool
    associate_public_ip_address: bool
    block_device_mappings: List[BlockDeviceMappings]
    ebs_optimized: bool
    iam_instance_profile: IamInstanceProfile
    image_id: str
    instance_metadata_options: InstanceMetadataOptions
    key_pair: str
    load_balancers: List[LoadBalancers]
    monitoring: bool
    resource_tag_specification: ResourceTagSpecification
    root_volume_size: int
    security_group_ids: List[str]
    tags: List[Tags]
    use_as_template_only: bool
    user_data: str
    """

    def __init__(
            self,
            associate_ipv6_address: bool = none,
            associate_public_ip_address: bool = none,
            block_device_mappings: List[BlockDeviceMappings] = none,
            ebs_optimized: bool = none,
            iam_instance_profile: IamInstanceProfile = none,
            image_id: str = none,
            instance_metadata_options: InstanceMetadataOptions = none,
            key_pair: str = none,
            load_balancers: List[LoadBalancer] = none,
            monitoring: bool = none,
            resource_tag_specification: ResourceTagSpecification = none,
            root_volume_size: int = none,
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
        self.key_pair = key_pair
        self.load_balancers = load_balancers
        self.monitoring = monitoring
        self.resource_tag_specification = resource_tag_specification
        self.root_volume_size = root_volume_size
        self.security_group_ids = security_group_ids
        self.tags = tags
        self.use_as_template_only = use_as_template_only
        self.user_data = user_data
# endregion


class Compute:
    """
    # Arguments
    subnet_ids: List[str]
    instance_types: InstanceTypes
    launch_specification: LaunchSpecification
    """

    def __init__(
            self,
            subnet_ids: List[str] = none,
            instance_types: InstanceTypes = none,
            launch_specification: LaunchSpecifications = none):
        self.subnet_ids = subnet_ids
        self.instance_types = instance_types
        self.launch_specification = launch_specification
# endregion


# region Logging
class S3:
    """
    # Arguments
    id: str
    """

    def __init__(
            self,
            id: str = none):
        self.id = id


class Export:
    """
    # Arguments
    s3: S3
    """

    def __init__(
            self,
            s3: S3 = none):
        self.s3 = s3


class Logging:
    """
    # Arguments
    export: Export
    """

    def __init__(
            self,
            export: Export = none):
        self.export = export
# endregion


# region Ocean
class Ocean:
    """
    # Arguments
    name: str
    controller_cluster_id: str
    region: str
    auto_scaler: AutoScaler
    capacity: Capacity
    strategy: Strategy
    scheduling: Scheduling
    security: Security
    compute: Compute
    logging: Logging
    """

    def __init__(
            self,
            name: str = none,
            controller_cluster_id: str = none,
            region: str = none,
            auto_scaler: AutoScaler = none,
            capacity: Capacity = none,
            strategy: Strategy = none,
            scheduling: Scheduling = none,
            security: Security = none,
            compute: Compute = none,
            logging: Logging = none):
        self.name = name
        self.controller_cluster_id = controller_cluster_id
        self.region = region
        self.auto_scaler = auto_scaler
        self.capacity = capacity
        self.strategy = strategy
        self.scheduling = scheduling
        self.security = security
        self.compute = compute
        self.security = logging
# endregion


# region OceanRequest
class OceanRequest:
    def __init__(self, ocean: Ocean):
        self.cluster = ocean

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


class Roll:
    """
    # Arguments
    batch_min_healthy_percentage: int
    batch_size_percentage: int
    comment: str
    disable_launch_spec_auto_scaling: bool
    instance_ids: List[str]
    launch_spec_ids: List[str]
    respect_pdb: bool
    """

    def __init__(
            self,
            batch_min_healthy_percentage: int = none,
            batch_size_percentage: int = none,
            comment: str = none,
            disable_launch_spec_auto_scaling: bool = none,
            launch_spec_ids: List[str] = none,
            instance_ids: List[str] = none,
            respect_pdb: bool = none):
        self.batch_min_healthy_percentage = batch_min_healthy_percentage
        self.batch_size_percentage = batch_size_percentage
        self.comment = comment
        self.disable_launch_spec_auto_scaling = disable_launch_spec_auto_scaling
        self.instance_ids = instance_ids
        self.launch_spec_ids = launch_spec_ids
        self.respect_pdb = respect_pdb

# region VirtualNodeGroup


class AutoScaleDown:
    """
    # Arguments
    max_scale_down_percentage: float
    """

    def __init__(
            self,
            max_scale_down_percentage: float = none):
        self.max_scale_down_percentage = max_scale_down_percentage


class AutoScale:
    """
    # Arguments
    auto_headroom_percentage: int
    down: class(AutoScaleDown)
    headrooms: List[Headroom]
    """

    def __init__(
            self,
            auto_headroom_percentage: int = none,
            down: AutoScaleDown = none,
            headrooms: List[Headroom] = none):
        self.auto_headroom_percentage = auto_headroom_percentage
        self.down = down
        self.headrooms = headrooms


class TagSelector:
    """
    # Arguments
    tag_key: str
    tag_value: str
    """

    def __init__(
            self,
            tag_key: str = none,
            tag_value: str = none):
        self.tag_key = tag_key
        self.tag_value = tag_value


class ElasticIpPool:
    """
    # Arguments
    tag_selector: TagSelector
    """

    def __init__(
            self,
            tag_selector: TagSelector = none):
        self.tag_selector = tag_selector


class ImageId:
    """
    # Arguments
    id: str = none
    """

    def __init__(
            self,
            id: str = none):
        self.id = id


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


class VNGResourceLimits:
    """
    # Arguments
    max_instance_count: int
    min_instance_count: int
    """

    def __init__(
            self,
            max_instance_count: int = none,
            min_instance_count: int = none):
        self.max_instance_count = max_instance_count
        self.min_instance_count = min_instance_count


class Config:
    """
    # Arguments
    headrooms: List[Headroom]
    """

    def __init__(
            self,
            headrooms: List[Headroom] = none):
        self.headrooms = headrooms


class VNGSchedulingTaskType(Enum):
    manual_headroom_update = "manualHeadroomUpdate"


class VNGSchedulingTasks:
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
            config: Config = none,
            task_type: VNGSchedulingTaskType = none):
        self.cron_expression = cron_expression
        self.is_enabled = is_enabled
        self.config = config
        self.task_type = task_type


class VNGSchedulingShutdownHours:
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


class VNGScheduling:
    """
    # Arguments
    tasks: List[VNGSchedulingTasks]
    shutdown_hours: VNGSchedulingShutdownHours
    """

    def __init__(
            self,
            tasks: List[VNGSchedulingTasks] = none,
            shutdown_hours: VNGSchedulingShutdownHours = none):
        self.tasks = tasks
        self.shutdown_hours = shutdown_hours


class VNGStrategy:
    """
    # Arguments
    spot_percentage: int
    """

    def __init__(
            self,
            spot_percentage: int = none):
        self.spot_percentage = spot_percentage


class Taints:
    """
    # Arguments
    tag_key: str
    tag_value: str
    """

    def __init__(
            self,
            effect: str = none,
            key: str = none,
            value: str = none):
        self.effect = effect
        self.key = key
        self.value = value


class VirtualNodeGroup:
    """
    # Arguments
    associate_public_ip_address: bool
    auto_scale: AutoScale
    block_device_mappings: List[BlockDeviceMappings]
    elastic_ip_pool: ElasticIpPool
    iam_instance_profile: IamInstanceProfile
    image_id: str
    images: List[ImageId]
    instance_metadata_options: InstanceMetadataOptions
    instance_types : List[str]
    instance_types_filters: InstanceTypesFilters
    labels: List[Labels]
    name: str
    ocean_id: str
    preferred_spot_types: List[str]
    resource_limits: VNGResourceLimits
    restrict_scale_down: bool
    root_volume_size: int
    scheduling: VNGScheduling
    strategy: VNGStrategy
    security_group_ids: List[str]
    subnet_ids: List[str]
    taints: List[Taints]
    user_data: str
    """

    def __init__(
            self,
            associate_public_ip_address: bool = none,
            auto_scale: AutoScale = none,
            block_device_mappings: List[BlockDeviceMappings] = none,
            elastic_ip_pool: ElasticIpPool = none,
            iam_instance_profile: IamInstanceProfile = none,
            image_id: str = none,
            images: List[ImageId] = none,
            instance_metadata_options: InstanceMetadataOptions = none,
            instance_types: List[str] = none,
            instance_types_filters: InstanceTypesFilters = none,
            labels: List[Labels] = none,
            name: str = none,
            ocean_id: str = none,
            preferred_spot_types: List[str] = none,
            resource_limits: VNGResourceLimits = none,
            restrict_scale_down: bool = none,
            root_volume_size: int = none,
            scheduling: VNGScheduling = none,
            strategy: VNGStrategy = none,
            security_group_ids: List[str] = none,
            subnet_ids: List[str] = none,
            tags: List[Tags] = none,
            taints: List[Taints] = none,
            user_data: str = none):
        self.associate_public_ip_address = associate_public_ip_address
        self.auto_scale = auto_scale
        self.block_device_mappings = block_device_mappings
        self.elastic_ip_pool = elastic_ip_pool
        self.iam_instance_profile = iam_instance_profile
        self.image_id = image_id
        self.images = images
        self.instance_metadata_options = instance_metadata_options
        self.instance_types = instance_types
        self.instance_types_filters = instance_types_filters
        self.labels = labels
        self.name = name
        self.ocean_id = ocean_id
        self.preferred_spot_types = preferred_spot_types
        self.resource_limits = resource_limits
        self.restrict_scale_down = restrict_scale_down
        self.root_volume_size = root_volume_size
        self.scheduling = scheduling
        self.strategy = strategy
        self.security_group_ids = security_group_ids
        self.subnet_ids = subnet_ids
        self.tags = tags
        self.taints = taints
        self.user_data = user_data
# endregion


# region Migration
class Migration:
    """
    # Arguments
    batch_size_percentage: int
    force_pod_eviction_on_pdb_failure: bool
    instance_ids: List[str]
    should_evict_stand_alone_pods: bool
    should_terminate_drained_nodes: bool
    state: str
    """

    def __init__(
            self,
            batch_size_percentage: int = none,
            force_pod_eviction_on_pdb_failure: bool = none,
            instance_ids: List[str] = none,
            should_evict_stand_alone_pods: bool = none,
            should_terminate_drained_nodes: bool = none,
            state: str = none):
        self.batch_size_percentage = batch_size_percentage
        self.force_pod_eviction_on_pdb_failure = force_pod_eviction_on_pdb_failure
        self.instance_ids = instance_ids
        self.should_evict_stand_alone_pods = should_evict_stand_alone_pods
        self.should_terminate_drained_nodes = should_terminate_drained_nodes
        self.state = state
# endregion


# region DetachInstances
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
# endregion

# region ImportASGToOcean


class ImportASGToOceanCluster:
    """
    # Arguments
    instance_types: List[str]
    """

    def __init__(
            self,
            instance_types: List[str] = none):
        self.instance_types = instance_types
# endregion


# region ImportASGToOceanVNG
class ImportASGToOceanVNG:
    """
    # Arguments
    labels: List[Labels]
    name: str
    taints: List[Taints]
    """

    def __init__(
            self,
            name: str = none,
            labels: List[Labels] = none,
            taints: List[Taints] = none):
        self.name = name
        self.labels = labels
        self.taints = taints
# endregion


# region ImportEKSNodeGroupToOceanVNG
class ImportEKSNodeGroupToOceanVNG:
    """
    # Arguments
    labels: List[Labels]
    name: str
    """

    def __init__(
            self,
            name: str = none,
            labels: List[Labels] = none):
        self.name = name
        self.labels = labels
# endregion


# region ExtendedResourceDefinition
class ExtendedResourceDefinition:
    """
    # Arguments
    mapping: dict
    name: str
    """

    def __init__(
            self,
            mapping: dict = none,
            name: str = none):
        self.mapping = mapping
        self.name = name
# endregion


class VNGRequest:
    def __init__(self, vng: VirtualNodeGroup):
        self.launch_spec = vng

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class ImportASGToOceanClusterRequest:
    def __init__(self, cluster: ImportASGToOceanCluster):
        self.cluster = cluster

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class ImportASGToOceanVNGRequest:
    def __init__(self, launch_spec: ImportASGToOceanVNG):
        self.launch_spec = launch_spec

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class ImportEKSNodeGroupToOceanVNGRequest:
    def __init__(self, launch_spec: ImportEKSNodeGroupToOceanVNG):
        self.launch_spec = launch_spec

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class DetachInstancesRequest:
    def __init__(self, detachInstances: DetachInstances):
        self.instances_to_detach = detachInstances.instances_to_detach
        self.should_decrement_target_capacity = detachInstances.should_decrement_target_capacity
        self.should_terminate_instances = detachInstances.should_terminate_instances

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class LoadBalancersRequest:
    def __init__(self, load_balancers: List[LoadBalancer]):
        self.load_balancers = load_balancers

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


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


class InstanceTypesFilterSimulationRequest:
    def __init__(self, instance_type_filter: InstanceTypesFilters = none):
        self.filters = instance_type_filter

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class LaunchNodesRequest:
    def __init__(self, amount: int = none):
        self.launch_request = dict(amount=amount)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class MigrationRequest:
    def __init__(self, migration: Migration):
        self.migration = migration

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class ExtendedResourceDefinitionRequest:
    def __init__(self, extended_resource_defintion: ExtendedResourceDefinition):
        self.extended_resource_defintion = extended_resource_defintion

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class InstanceTypesFilterSimulationRequestForVNG:
    def __init__(self, instance_types_filters: InstanceTypesFilters = none):
        self.instance_types_filters = instance_types_filters

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
