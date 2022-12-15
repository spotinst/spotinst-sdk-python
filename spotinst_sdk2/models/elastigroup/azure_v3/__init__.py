import json

none = "d3043820717d74d9a17694c176d39733"


# region Elastigroup
class Elastigroup:
    """
    # Arguments
    name: str
    region: str
    resource_group_name: str
    description: str
    capacity: Capacity
    strategy: Strategy
    compute: Compute
    scaling: Scaling
    health: Health
    scheduling: Scheduling
    """

    def __init__(
            self,
            name=none,
            region=none,
            resource_group_name=none,
            description=none,
            capacity=none,
            strategy=none,
            compute=none,
            scaling=none,
            health=none,
            scheduling=none):
        self.name = name
        self.region = region
        self.resource_group_name = resource_group_name
        self.description = description
        self.capacity = capacity
        self.strategy = strategy
        self.compute = compute
        self.scaling = scaling
        self.health = health
        self.scheduling = scheduling


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

# region Compute
class Compute:
    """
    # Arguments
    launch_specification: LaunchSpecification
    os: str
    preferred_zones: List[str]
    vm_sizes: VmSizes
    zones: List[str]

    """

    def __init__(
            self,
            launch_specification=none,
            os=none,
            preferred_zones=none,
            vm_sizes=none,
            zones=none,
    ):
        self.launch_specification = launch_specification
        self.os = os
        self.preferred_zones = preferred_zones
        self.vm_sizes = vm_sizes
        self.zones = zones


class LaunchSpecification:
    """
    #Arguments
    boot_diagnostics: BootDiagnostics
    custom_data: str
    data_disks: List[DataDisk]
    extensions: list[Extension]
    image: Image
    load_balancers_config: LoadBalancerConfig
    login: Login
    managed_service_identities: list[ManagedServiceIdentity]
    network: Network
    os_disk: OsDisk
    secrets: List[Secret]
    shutdown_script: str
    tags: list[Tag]
    vm_name_prefix: str
    """

    def __init__(
            self,
            boot_diagnostics=none,
            custom_data=none,
            data_disks=none,
            extensions=none,
            image=none,
            load_balancers_config=none,
            login=none,
            managed_service_identities=none,
            network=none,
            os_disk=none,
            secrets=none,
            shutdown_script=none,
            tags=none,
            vm_name_prefix=none):
        self.boot_diagnostics = boot_diagnostics
        self.custom_data = custom_data
        self.data_disks = data_disks
        self.extensions = extensions
        self.image = image
        self.load_balancers_config = load_balancers_config
        self.login = login
        self.managed_service_identities = managed_service_identities
        self.network = network
        self.os_disk = os_disk
        self.secrets = secrets
        self.shutdown_script = shutdown_script
        self.tags = tags
        self.vm_name_prefix = vm_name_prefix


class BootDiagnostics:
    """
    #Arguments
    is_enabled: bool
    storage_uri = str
    type: str
    """

    def __init__(
            self,
            is_enabled=none,
            storage_uri=none,
            type=none):
        self.is_enabled = is_enabled
        self.storage_uri = storage_uri
        self.type = type


class DataDisk:
    """
    #Arguments
    lun: int
    size_gb = int
    type: str
    """

    def __init__(
            self,
            lun=none,
            size_g_b=none,
            type=none):
        self.lun = lun
        self.size_g_b = size_g_b
        self.type = type


class Extension:
    """
    # Arguments
    api_version: str
    auto_upgrade_minor_version: bool
    minor_version_auto_upgrade: bool
    name: str
    publisher: str
    type: str
    """

    def __init__(
            self,
            api_version=none,
            auto_upgrade_minor_version=none,
            minor_version_auto_upgrade=none,
            name=none,
            publisher=none,
            type=none):
        self.api_version = api_version
        self.auto_upgrade_minor_version = auto_upgrade_minor_version
        self.minor_version_auto_upgrade = minor_version_auto_upgrade
        self.name = name
        self.publisher = publisher
        self.type = type


class Image:
    """
    # Arguments
    marketplace: Marketplace
    custom: Custom
    gallery: Gallery
    """

    def __init__(self, marketplace=none, custom=none, gallery=none):
        self.marketplace = marketplace
        self.custom = custom
        self.gallery = gallery


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
    name: str
    """

    def __init__(
            self,
            resource_group_name=none,
            name=none):
        self.resource_group_name = resource_group_name
        self.name = name


class Gallery:
    """
    # Arguments
    gallery_name: str
    image_name: str
    resource_group_name: str
    spot_account_id: str
    version: str
    """

    def __init__(
            self,
            gallery_name=none,
            image_name=none,
            resource_group_name=none,
            spot_account_id=none,
            version=none):
        self.gallery_name = gallery_name
        self.image_name = image_name
        self.resource_group_name = resource_group_name
        self.spot_account_id = spot_account_id
        self.version = version


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
    type: str
    resource_group_name: str
    application_gateway_name: str
    backend_pool_name: str
    """

    def __init__(
            self,
            balancer_id=none,
            target_set_id=none,
            auto_weight=none,
            type=none,
            resource_group_name=none,
            application_gateway_name=none,
            backend_pool_name=none):
        self.balancer_id = balancer_id
        self.target_set_id = target_set_id
        self.auto_weight = auto_weight
        self.type = type
        self.resource_group_name = resource_group_name
        self.application_gateway_name = application_gateway_name
        self.backend_pool_name = backend_pool_name


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


class Network:
    """
    # Arguments
    network_interfaces: List[NetworkInterface]
    resource_group_name: str
    virtual_network_name: str
    """

    def __init__(
            self,
            network_interfaces=none,
            virtual_network_name=none,
            resource_group_name=none):
        self.network_interfaces = network_interfaces
        self.virtual_network_name = virtual_network_name
        self.resource_group_name = resource_group_name


class NetworkInterface:
    """
    # Arguments
    additional_ip_configurations: List[AdditionalIpConfiguration]
    application_security_groups: List[ApplicationSecurityGroup]
    assign_public_ip: bool
    enable_ip_forwarding: bool
    is_primary: bool
    private_ip_addresses: List[str]
    public_ips: List[PublicIp]
    public_ip_sku: str
    security_group: SecurityGroup
    subnet_name: str
    """

    def __init__(
            self,
            additional_ip_configurations=none,
            application_security_groups=none,
            assign_public_ip=none,
            enable_ip_forwarding=none,
            is_primary=none,
            private_ip_addresses=none,
            public_ips=none,
            public_ip_sku=none,
            security_group=none,
            subnet_name=none):
        self.additional_ip_configurations = additional_ip_configurations
        self.application_security_groups = application_security_groups
        self.assign_public_ip = assign_public_ip
        self.enable_ip_forwarding = enable_ip_forwarding
        self.is_primary = is_primary
        self.private_ip_addresses = private_ip_addresses
        self.public_ips = public_ips
        self.public_ip_sku = public_ip_sku
        self.security_group = security_group
        self.subnet_name = subnet_name


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


class ApplicationSecurityGroup:
    """
    # Arguments
    name: str
    resource_group_name: str
    """

    def __init__(
            self,
            name=none,
            resource_group_name=none):
        self.name = name
        self.resource_group_name = resource_group_name


class PublicIp:
    """
    # Arguments
    name: str
    resource_group_name: str
    """

    def __init__(
            self,
            name=none,
            resource_group_name=none):
        self.name = name
        self.resource_group_name = resource_group_name


class SecurityGroup:
    """
    # Arguments
    name: str
    resource_group_name: str
    """

    def __init__(
            self,
            name=none,
            resource_group_name=none):
        self.name = name
        self.resource_group_name = resource_group_name


class OsDisk:
    """
    # Arguments
    size: int
    type: str
    """

    def __init__(
            self,
            size=none,
            type=none):
        self.size = size
        self.type = type


class Secret:
    """
    # Arguments
    source_vault: SourceVault
    vault_certificate: List[VaultCertificate]
    """

    def __init__(
            self,
            source_vault=none,
            vault_certificate=none):
        self.source_vault = source_vault
        self.vault_certificate = vault_certificate


class SourceVault:
    """
    # Arguments
    name: str
    resource_group_name: str
    """

    def __init__(
            self,
            name=none,
            resource_group_name=none):
        self.name = name
        self.resource_group_name = resource_group_name


class VaultCertificate:
    """
    # Arguments
    certificate_store: str
    certificate_url: str
    """

    def __init__(
            self,
            certificate_store=none,
            certificate_url=none):
        self.certificate_store = certificate_store
        self.certificate_url = certificate_url


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


class VmSizes:
    """
    #Arguments
    od_sizes: list[str]
    preferred_spot_sizes: list[str]
    spot_sizes: List[str]
    """

    def __init__(
            self,
            od_sizes=none,
            preferred_spot_sizes=none,
            spot_sizes=none):
        self.od_sizes = od_sizes
        self.preferred_spot_sizes = preferred_spot_sizes
        self.spot_sizes = spot_sizes


# endregion

# region Health
class Health:
    """
    #Arguments
    health_check_types: str
    auto_healing: bool
    grace_period: int
    unhealthy_duration : int
    """

    def __init__(
            self,
            health_check_types=none,
            auto_healing=none,
            grace_period=none,
            unhealthy_duration=none):
        self.health_check_types = health_check_types
        self.auto_healing = auto_healing
        self.grace_period = grace_period
        self.unhealthy_duration = unhealthy_duration


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
    is_enabled: bool
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
            is_enabled=none,
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
        self.is_enabled = is_enabled
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
    key: str
    value: str
    """

    def __init__(self, name=none, value=none):
        self.name = name
        self.value = value


class ScalingPolicyAction:
    """
    # Arguments
    type: str
    adjustment: str
    target: int
    maximum: int
    minimum: int
    """

    def __init__(
            self,
            type=none,
            adjustment=none,
            target=none,
            maximum=none,
            minimum=none):
        self.type = type
        self.adjustment = adjustment
        self.target = target
        self.maximum = maximum
        self.minimum = minimum


# endregion

# region Strategy
class Strategy:
    """
    # Arguments
    draining_timeout: int
    on_demand_count: int
    optimization_windows: List[str]
    orientation: str
    revert_to_spot: RevertToSpot
    signals: List[Signal]
    spot_percentage: int
    fallback_to_od: bool
    """

    def __init__(
            self,
            draining_timeout=none,
            on_demand_count=none,
            optimization_windows=none,
            orientation=none,
            revert_to_spot=none,
            signals=none,
            spot_percentage=none,
            fallback_to_od=none):
        self.draining_timeout = draining_timeout
        self.on_demand_count = on_demand_count
        self.optimization_windows = optimization_windows
        self.orientation = orientation
        self.revert_to_spot = revert_to_spot
        self.signals = signals
        self.spot_percentage = spot_percentage
        self.fallback_to_od = fallback_to_od


class RevertToSpot:
    """
    # Arguments
    perform_at: str
    """

    def __init__(self, perform_at=none):
        self.perform_at = perform_at


class Signal:
    """
    # Arguments
    timeout: str
    type: str
    """

    def __init__(self, timeout=none, type=none):
        self.timeout = timeout
        self.type = type


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
    frequency: str
    start_time: str
    cron_expression: str
    type: str
    scale_target_capacity: int
    scale_min_capacity: int
    scale_max_capacity: int
    batch_size_percentage: int
    grace_period: int
    adjustment: int
    adjustment_percentage: int
    target_capacity: int
    min_capacity: int
    max_capacity: int
    """

    def __init__(
            self,
            is_enabled=none,
            frequency=none,
            start_time=none,
            cron_expression=none,
            type=none,
            scale_target_capacity=none,
            scale_min_capacity=none,
            scale_max_capacity=none,
            batch_size_percentage=none,
            grace_period=none,
            adjustment=none,
            adjustment_percentage=none,
            target_capacity=none,
            min_capacity=none,
            max_capacity=none):
        self.is_enabled = is_enabled
        self.frequency = frequency
        self.start_time = start_time
        self.cron_expression = cron_expression
        self.type = type
        self.scale_target_capacity = scale_target_capacity
        self.scale_min_capacity = scale_min_capacity
        self.scale_max_capacity = scale_max_capacity
        self.batch_size_percentage = batch_size_percentage
        self.grace_period = grace_period
        self.adjustment = adjustment
        self.adjustment_percentage = adjustment_percentage
        self.target_capacity = target_capacity
        self.min_capacity = min_capacity
        self.max_capacity = max_capacity

# endregion

# Region Requests

class DetachConfiguration:
    """
    # Arguments
    draining_timeout: int
    should_decrement_target_capacity: bool
    should_terminate_vms: bool
    instances_to_detach: list[str]
    """
    def __init__(
            self,
            draining_timeout=none,
            should_decrement_target_capacity=none,
            should_terminate_vms=none,
            vms_to_detach=none):
        self.draining_timeout = draining_timeout
        self.should_decrement_target_capacity = should_decrement_target_capacity
        self.should_terminate_vms = should_terminate_vms
        self.vms_to_detach = vms_to_detach


class ElastigroupCreateRequest:
    def __init__(self, elastigroup):
        self.group = elastigroup

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class ElastigroupUpdateRequest:
    def __init__(self, elastigroup):
        self.group = elastigroup

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class ElastigroupUpdateCapacityRequest:
    def __init__(self, capacity):
        self.capacity = capacity

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class ElastigroupDetachVMsRequest:
    def __init__(self, detach_configuration):
        self.should_decrement_target_capacity = detach_configuration.should_decrement_target_capacity
        self.draining_timeout = detach_configuration.draining_timeout
        self.vms_to_detach = detach_configuration.vms_to_detach
        self.should_terminate_vms = detach_configuration.should_terminate_vms

    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=4)
# endregion
