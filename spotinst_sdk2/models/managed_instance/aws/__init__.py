import json
from typing import List

none = "d3043820717d74d9a17694c176d39733"


class Persistence:
    """
    # Arguments
    persist_root_device: bool
    persist_block_devices: bool
    block_devices_mode: str
    persist_private_ip: bool
    """
    def __init__(self, persist_root_device: bool = none, persist_block_devices: bool = none,
                 block_devices_mode: str = none, persist_private_ip: bool = none):
        self.persist_root_device = persist_root_device
        self.persist_block_devices = persist_block_devices
        self.block_devices_mode = block_devices_mode
        self.persist_private_ip = persist_private_ip


class HealthCheck:
    """
    # Arguments
    type: bool
    auto_healing: bool
    grace_period: int
    unhealthy_duration: int
    """
    def __init__(self, type: str = none, auto_healing: bool = none, grace_period: int = none,
                 unhealthy_duration: int = none):
        self.type = type
        self.auto_healing = auto_healing
        self.grace_period = grace_period
        self.unhealthy_duration = unhealthy_duration


class Task:
    """
    # Arguments
    task_type: str
    start_time: str
    cron_expression: str
    is_enabled: bool
    frequency: str
    """
    def __init__(self, task_type: str = none, start_time: str = none, cron_expression: str = none,
                 is_enabled: bool = none, frequency: str = none):
        self.is_enabled = is_enabled
        self.frequency = frequency
        self.start_time = start_time
        self.cron_expression = cron_expression
        self.task_type = task_type


class Scheduling:
    """
    # Arguments
    tasks: list[Task]
    """
    def __init__(self, tasks: List[Task] = none):
        self.tasks = tasks


class RevertToSpot:
    """
    # Arguments
    perform_at: str
    """
    def __init__(self, perform_at: str = none):
        self.perform_at = perform_at


class Strategy:
    """
    # Arguments
    life_cycle: str
    orientation: str
    draining_timeout: int
    fallback_to_od: bool
    utilize_reserved_instances: bool
    utilize_commitments: bool
    optimization_windows: list[str]
    revert_to_spot: RevertToSpot
    minimum_instance_lifetime: int
    """
    def __init__(self, life_cycle: str = none, orientation: str = none, draining_timeout: int = none,
                 fallback_to_od: bool = none,
                 utilize_reserved_instances: bool = none, utilize_commitments: bool = none,
                 optimization_windows: List[str] = none,
                 revert_to_spot: RevertToSpot = none, minimum_instance_lifetime: int = none):
        self.life_cycle = life_cycle
        self.orientation = orientation
        self.draining_timeout = draining_timeout
        self.fallback_to_od = fallback_to_od
        self.utilize_reserved_instances = utilize_reserved_instances
        self.utilize_commitments = utilize_commitments
        self.optimization_windows = optimization_windows
        self.revert_to_spot = revert_to_spot
        self.minimum_instance_lifetime = minimum_instance_lifetime


class EBS:
    """
    # Arguments
    delete_on_termination: bool
    encrypted: bool
    iops: int
    throughput: float
    volume_size: int
    volume_type: str
    kms_key_id: str
    snapshot_id: str
    """
    def __init__(self, delete_on_termination: bool = none, encrypted: bool = none, iops: int = none,
                 throughput: float = none,
                 kms_key_id: str = none,
                 snapshot_id: str = none,
                 volume_size: int = none,
                 volume_type: str = none):
        self.delete_on_termination = delete_on_termination
        self.encrypted = encrypted
        self.iops = iops
        self.throughput = throughput
        self.volume_size = volume_size
        self.volume_type = volume_type
        self.kms_key_id = kms_key_id
        self.snapshot_id = snapshot_id


class BlockDeviceMapping:
    """
    # Arguments
    device_name: str
    ebs: EBS
    no_device: str
    virtual_name: str
    """
    def __init__(self, device_name: str = none, ebs: EBS = none, no_device: str = none, virtual_name: str = none):
        self.device_name = device_name
        self.ebs = ebs
        self.no_device = no_device
        self.virtual_name = virtual_name


class CreditSpecification:
    """
    # Arguments
    cpu_credits: str
    """
    def __init__(self, cpu_credits: str = none):
        self.cpu_credits = cpu_credits


class IamRole:
    """
    # Arguments
    name: str
    arn: str
    """
    def __init__(self, name: str = none, arn: str = none):
        self.name = name
        self.arn = arn


class InstanceTypes:
    """
    # Arguments
    preferred_type: str
    types: list[str]
    """
    def __init__(self, preferred_type: str = none, types: List[str] = none):
        self.preferred_type = preferred_type
        self.types = types


class NetworkInterface:
    """
    # Arguments
    device_index: int
    associate_public_ip_address: bool
    associate_ipv6_address: bool
    """
    def __init__(self, device_index: int = none, associate_public_ip_address: bool = none,
                 associate_ipv6_address: bool = none):
        self.device_index = device_index
        self.associate_public_ip_address = associate_public_ip_address
        self.associate_ipv6_address = associate_ipv6_address


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


class Tag:
    """
    # Arguments
    tag_key: str
    tag_value: str
    """
    def __init__(self, tag_key: str = none, tag_value: str = none):
        self.tag_key = tag_key
        self.tag_value = tag_value


class LaunchSpecification:
    """
    # Arguments
    instance_types: InstanceTypes
    ebs_optimized: bool
    monitoring: bool
    tenancy: str
    iam_role: IamRole
    security_group_ids: list[str]
    image_id: str
    key_pair: str
    tags: list[Tag]
    resource_tag_specification: ResourceTagSpecification
    user_data: str
    shutdown_script: str
    credit_specification: CreditSpecification
    network_interfaces: list[NetworkInterface]
    block_device_mappings: list[BlockDeviceMapping]
    """
    def __init__(self, instance_types: InstanceTypes = none, ebs_optimized: bool = none, monitoring: bool = none,
                 tenancy: str = none,
                 iam_role: IamRole = none, security_group_ids: List[str] = none, image_id: str = none,
                 key_pair: str = none, tags: List[Tag] = none,
                 resource_tag_specification: ResourceTagSpecification = none, user_data: str = none,
                 shutdown_script: str = none,
                 credit_specification: CreditSpecification = none, network_interfaces: List[NetworkInterface] = none,
                 block_device_mappings: List[BlockDeviceMapping] = none):
        self.instance_types = instance_types
        self.ebs_optimized = ebs_optimized
        self.monitoring = monitoring
        self.tenancy = tenancy
        self.iam_role = iam_role
        self.security_group_ids = security_group_ids
        self.image_id = image_id
        self.key_pair = key_pair
        self.tags = tags
        self.resource_tag_specification = resource_tag_specification
        self.user_data = user_data
        self.shutdown_script = shutdown_script
        self.block_device_mappings = block_device_mappings
        self.credit_specification = credit_specification
        self.network_interfaces = network_interfaces


class Compute:
    """
    # Arguments
    subnet_ids: list[str]
    vpc_id: str
    elastic_ip: str
    private_ip: str
    product: str
    launch_specification: LaunchSpecification
    """
    def __init__(self, subnet_ids: List[str] = none, vpc_id: str = none, elastic_ip: str = none, private_ip: str = none,
                 product: str = none,
                 launch_specification: LaunchSpecification = none):
        self.subnet_ids = subnet_ids
        self.vpc_id = vpc_id
        self.elastic_ip = elastic_ip
        self.private_ip = private_ip
        self.product = product
        self.launch_specification = launch_specification


class Route53RecordSetConfiguration:
    """
    # Arguments
    name: str
    use_public_ip: bool
    use_public_dns: bool
    """
    def __init__(self, name: str = none, use_public_ip: bool = none, use_public_dns: bool = none):
        self.name = name
        self.use_public_ip = use_public_ip
        self.use_public_dns = use_public_dns


class Route53DomainConfiguration:
    """
    # Arguments
    hosted_zone_id: str
    spotinst_account_id: str
    record_set_type: str
    record_sets: list[Route53RecordSetConfiguration]
    """
    def __init__(self, hosted_zone_id: str = none, spotinst_account_id: str = none, record_set_type: str = none,
                 record_sets: List[Route53RecordSetConfiguration] = none):
        self.hosted_zone_id = hosted_zone_id
        self.spotinst_account_id = spotinst_account_id
        self.record_set_type = record_set_type
        self.record_sets = record_sets


class Route53Configuration:
    """
    # Arguments
    domains: list[Route53DomainsConfiguration]
    """
    def __init__(self, domains: List[Route53DomainConfiguration] = none):
        self.domains = domains


class LoadBalancer:
    """
    # Arguments
    name: str
    arn: str
    type: str
    balancer_id: str
    target_set_id: str
    az_awareness: bool
    auto_weight: bool
    """
    def __init__(self, name: str = none, arn: str = none, type: str = none, balancer_id: str = none,
                 target_set_id: str = none, az_awareness: bool = none,
                 auto_weight: bool = none):
        self.name = name
        self.arn = arn
        self.type = type
        self.balancer_id = balancer_id
        self.target_set_id = target_set_id
        self.az_awareness = az_awareness
        self.auto_weight = auto_weight


class LoadBalancersConfiguration:
    """
    # Arguments
    load_balancers: list[LoadBalancer]
    """

    def __init__(self, load_balancers: List[LoadBalancer] = none):
        self.load_balancers = load_balancers


class IntegrationsConfig:
    """
    # Arguments
    route53: Route53Configuration
    load_balancers_config: LoadBalancersConfiguration
    """

    def __init__(self, route53: Route53Configuration = none, load_balancers_config: LoadBalancersConfiguration = none):
        self.route53 = route53
        self.load_balancers_config = load_balancers_config


class ManagedInstance:
    """
    # Arguments
    name: str
    description: str
    region: str
    strategy: Strategy
    persistence: Persistence
    health_check: HealthCheck
    scheduling: Scheduling
    compute: Compute
    integrations: IntegrationsConfig
    """

    def __init__(self, name: str = none, description: str = none, region: str = none,
                 strategy: Strategy = none,
                 persistence: Persistence = none, health_check: HealthCheck = none, scheduling: Scheduling = none,
                 compute: Compute = none, integrations: IntegrationsConfig = none):
        self.name = name
        self.description = description
        self.region = region
        self.strategy = strategy
        self.persistence = persistence
        self.health_check = health_check
        self.compute = compute
        self.scheduling = scheduling
        self.integrations = integrations


# region Client Requests
class ManagedInstanceCreationRequest:
    def __init__(self, managed_instance: ManagedInstance):
        self.managed_instance = managed_instance

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class DeallocationConfig:
    def __init__(self, deallocate_network_interfaces: bool = none,
                 deallocate_volumes: bool = none, deallocate_snapshots: bool = none, deallocate_amis: bool = none,
                 should_terminate_instance: bool = none):
        self.deallocate_network_interfaces = deallocate_network_interfaces
        self.deallocate_volumes = deallocate_volumes
        self.deallocate_snapshots = deallocate_snapshots
        self.deallocate_amis = deallocate_amis
        self.should_terminate_instance = should_terminate_instance

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class AmiBackup:
    def __init__(self, should_delete_images: bool = none):
        self.should_delete_images = should_delete_images

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class ManagedInstanceDeletionRequest:
    def __init__(self, deallocation_config: DeallocationConfig = none, ami_backup: AmiBackup = none):
        self.deallocation_config = deallocation_config
        self.ami_backup = ami_backup

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class ManagedInstanceUpdateRequest:
    def __init__(self, managed_instance: ManagedInstance):
        self.managed_instance = managed_instance

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
# endregion
