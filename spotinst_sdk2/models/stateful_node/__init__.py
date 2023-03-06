import json
from typing import List

none = "d3043820717d74d9a17694c176d39733"

# region Persistence

class Persistence:
    """
    # Arguments
    data_disks_persistence_mode: str
    os_disk_persistence_mode: str
    should_persist_data_disks: bool
    should_persist_network: bool
    should_persist_os_disk: bool
    """

    def __init__(self, data_disks_persistence_mode: str = none, os_disk_persistence_mode: str = none,
                 should_persist_data_disks: bool = none, should_persist_network: bool = none,
                 should_persist_os_disk: bool = none):
        self.data_disks_persistence_mode = data_disks_persistence_mode
        self.os_disk_persistence_mode = os_disk_persistence_mode
        self.should_persist_data_disks = should_persist_data_disks
        self.should_persist_network = should_persist_network
        self.should_persist_os_disk = should_persist_os_disk

# endregion


# region Health

class Health:
    """
    # Arguments
    health_check_types: List[str]
    auto_healing: bool
    grace_period: int
    unhealthy_duration: int
    """

    def __init__(
            self,
            health_check_types: List[str] = none,
            auto_healing: bool = none,
            grace_period: int = none,
            unhealthy_duration: int = none):
        self.health_check_types = health_check_types
        self.auto_healing = auto_healing
        self.grace_period = grace_period
        self.unhealthy_duration = unhealthy_duration

# endregion


# region Scheduling

class SchedulingTask:
    """
    # Arguments
    is_enabled: bool
    cron_expression: str
    type: str
    """

    def __init__(
            self,
            is_enabled: bool = none,
            cron_expression: str = none,
            type: str = none):
        self.is_enabled = is_enabled
        self.cron_expression = cron_expression
        self.type = type
        
class Scheduling:
    """
    # Arguments
    tasks: List[SchedulingTask]
    """

    def __init__(self, tasks: List[SchedulingTask] = none):
        self.tasks = tasks

# endregion


# region Strategy

class RevertToSpot:
    """
    # Arguments
    perform_at: str
    """

    def __init__(self, perform_at: str = none):
        self.perform_at = perform_at


class Signal:
    """
    # Arguments
    timeout: int
    type: str
    """

    def __init__(self, timeout: int = none, type: str = none):
        self.timeout = timeout
        self.type = type

class Strategy:
    """
    # Arguments
    draining_timeout: int
    fallback_to_od: bool
    od_windows: List[str]
    optimization_windows: List[str]
    preferred_lifecycle: str
    revert_to_spot: RevertToSpot
    signals: List[Signal]
    """

    def __init__(
            self,
            draining_timeout: int = none,
            fallback_to_od: bool = none,
            od_windows: List[str] = none,
            optimization_windows: List[str] = none,
            preferred_lifecycle: str = none,
            revert_to_spot: RevertToSpot =none,
            signals: List[Signal] = none):
        self.draining_timeout = draining_timeout
        self.fallback_to_od = fallback_to_od
        self.od_windows = od_windows
        self.optimization_windows = optimization_windows
        self.preferred_lifecycle = preferred_lifecycle
        self.revert_to_spot = revert_to_spot
        self.signals = signals

# endregion


# region Compute

class BootDiagnostics:
    """
    # Arguments
    is_enabled: bool
    storage_uri = str
    type: str
    """

    def __init__(
            self,
            is_enabled: bool = none,
            storage_uri: str = none,
            type: str = none):
        self.is_enabled = is_enabled
        self.storage_uri = storage_uri
        self.type = type


class DataDisk:
    """
    # Arguments
    lun: int
    size_gb = int
    type: str
    """

    def __init__(
            self,
            lun: int = none,
            size_g_b: int = none,
            type: str = none):
        self.lun = lun
        self.size_g_b = size_g_b
        self.type = type


class Extension:
    """
    # Arguments
    api_version: str
    minor_version_auto_upgrade: bool
    name: str
    publisher: str
    type: str
    """

    def __init__(
            self,
            api_version: str = none,
            minor_version_auto_upgrade: bool = none,
            name: str = none,
            publisher: str = none,
            type: str = none):
        self.api_version = api_version
        self.minor_version_auto_upgrade = minor_version_auto_upgrade
        self.name = name
        self.publisher = publisher
        self.type = type


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
            publisher: str = none,
            offer: str = none,
            sku: str = none,
            version: str = none):
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
            resource_group_name: str = none,
            name: str = none):
        self.resource_group_name = resource_group_name
        self.name = name


class Gallery:
    """
    # Arguments
    gallery_name: str
    image_name: str
    resource_group_name: str
    spot_account_id: str
    version_name: str
    """

    def __init__(
            self,
            gallery_name: str = none,
            image_name: str = none,
            resource_group_name: str = none,
            spot_account_id: str = none,
            version_name: str = none):
        self.gallery_name = gallery_name
        self.image_name = image_name
        self.resource_group_name = resource_group_name
        self.spot_account_id = spot_account_id
        self.version_name = version_name


class Image:
    """
    # Arguments
    marketplace: Marketplace
    custom: Custom
    gallery: Gallery
    """

    def __init__(self, marketplace: Marketplace = none, custom: Custom = none, gallery: Gallery = none):
        self.marketplace = marketplace
        self.custom = custom
        self.gallery = gallery


class LoadBalancer:
    """
    # Arguments
    backend_pool_names: List[str]
    load_balancer_sku: str
    name: str
    resource_group_name: str
    type: str
    """

    def __init__(
            self,
            backend_pool_names: List[str] = none,
            load_balancer_sku: str = none,
            name: str = none,
            resource_group_name: str = none,
            type: str = none):
        self.backend_pool_names = backend_pool_names
        self.load_balancer_sku = load_balancer_sku
        self.name = name
        self.resource_group_name = resource_group_name
        self.type = type


class LoadBalancerConfig:
    """
    # Arguments
    load_balancers: List[LoadBalancer]
    """

    def __init__(self, load_balancers: List[LoadBalancer] = none):
        self.load_balancers = load_balancers


class Login:
    """
    # Arguments
    ssh_public_key: str
    user_name: str
    password: str
    """

    def __init__(
            self,
            ssh_public_key: str = none,
            user_name: str = none,
            password: str = none):
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
            resource_group_name: str = none,
            name: str = none):
        self.resource_group_name = resource_group_name
        self.name = name


class AdditionalIpConfiguration:
    """
    # Arguments
    name: str
    private_ip_address_version: str
    """

    def __init__(
            self,
            name: str = none,
            private_ip_address_version: str = none):
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
            name: str = none,
            resource_group_name: str = none):
        self.name = name
        self.resource_group_name = resource_group_name


class NetworkSecurityGroup:
    """
    # Arguments
    name: str
    resource_group_name: str
    """

    def __init__(
            self,
            name: str = none,
            resource_group_name: str = none):
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
            name: str = none,
            resource_group_name: str = none):
        self.name = name
        self.resource_group_name = resource_group_name


class NetworkInterface:
    """
    # Arguments
    additional_ip_configurations: List[AdditionalIpConfiguration]
    application_security_groups: List[ApplicationSecurityGroup]
    assign_public_ip: bool
    enable_ip_forwarding: bool
    is_primary: bool
    network_security_group: NetworkSecurityGroup
    private_ip_addresses: List[str]
    public_ips: List[PublicIp]
    public_ip_sku: str
    subnet_name: str
    """

    def __init__(
            self,
            additional_ip_configurations: List[AdditionalIpConfiguration] = none,
            application_security_groups: List[ApplicationSecurityGroup] = none,
            assign_public_ip: bool = none,
            enable_ip_forwarding: bool = none,
            is_primary: bool = none,
            network_security_group=none,
            private_ip_addresses: List[str] = none,
            public_ips: List[PublicIp] = none,
            public_ip_sku: str = none,
            subnet_name: str = none):
        self.additional_ip_configurations = additional_ip_configurations
        self.application_security_groups = application_security_groups
        self.assign_public_ip = assign_public_ip
        self.enable_ip_forwarding = enable_ip_forwarding
        self.is_primary = is_primary
        self.network_security_group = network_security_group
        self.private_ip_addresses = private_ip_addresses
        self.public_ips = public_ips
        self.public_ip_sku = public_ip_sku
        self.subnet_name = subnet_name


class Network:
    """
    # Arguments
    network_interfaces: List[NetworkInterface]
    resource_group_name: str
    virtual_network_name: str
    """

    def __init__(
            self,
            network_interfaces: List[NetworkInterface] = none,
            virtual_network_name: str = none,
            resource_group_name: str = none):
        self.network_interfaces = network_interfaces
        self.virtual_network_name = virtual_network_name
        self.resource_group_name = resource_group_name


class OsDisk:
    """
    # Arguments
    size_g_b: int
    type: str
    """

    def __init__(
            self,
            size_g_b: int = none,
            type: str = none):
        self.size_g_b = size_g_b
        self.type = type


class SourceVault:
    """
    # Arguments
    name: str
    resource_group_name: str
    """

    def __init__(
            self,
            name: str = none,
            resource_group_name: str = none):
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
            certificate_store: str = none,
            certificate_url: str = none):
        self.certificate_store = certificate_store
        self.certificate_url = certificate_url


class Secret:
    """
    # Arguments
    source_vault: SourceVault
    vault_certificates: List[VaultCertificate]
    """

    def __init__(
            self,
            source_vault: SourceVault = none,
            vault_certificates: List[VaultCertificate] = none):
        self.source_vault = source_vault
        self.vault_certificates = vault_certificates


class Tag:
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


class VmSizes:
    """
    # Arguments
    od_sizes: List[str]
    preferred_spot_sizes: List[str]
    spot_sizes: List[str]
    """

    def __init__(
            self,
            od_sizes: List[str] = none,
            preferred_spot_sizes: List[str] = none,
            spot_sizes: List[str] = none):
        self.od_sizes = od_sizes
        self.preferred_spot_sizes = preferred_spot_sizes
        self.spot_sizes = spot_sizes


class LaunchSpecification:
    """
    # Arguments
    boot_diagnostics: BootDiagnostics
    custom_data: str
    data_disks: List[DataDisk]
    extensions: List[Extension]
    image: Image
    license_type: str
    load_balancers_config: LoadBalancerConfig
    login: Login
    managed_service_identities: List[ManagedServiceIdentity]
    network: Network
    os_disk: OsDisk
    secrets: List[Secret]
    shutdown_script: str
    tags: List[Tag]
    vm_name: str
    vm_name_prefix: str
    """

    def __init__(
            self,
            boot_diagnostics: BootDiagnostics = none,
            custom_data: str = none,
            data_disks: List[DataDisk] = none,
            extensions: List[Extension] = none,
            image: Image = none,
            license_type: str = none,
            load_balancers_config: LoadBalancerConfig = none,
            login: Login = none,
            managed_service_identities: List[ManagedServiceIdentity] = none,
            network: Network = none,
            os_disk: OsDisk = none,
            secrets: List[Secret] = none,
            shutdown_script: str = none,
            tags: List[Tag] = none,
            vm_name: str = none,
            vm_name_prefix: str = none):
        self.boot_diagnostics = boot_diagnostics
        self.custom_data = custom_data
        self.data_disks = data_disks
        self.extensions = extensions
        self.image = image
        self.license_type = license_type
        self.load_balancers_config = load_balancers_config
        self.login = login
        self.managed_service_identities = managed_service_identities
        self.network = network
        self.os_disk = os_disk
        self.secrets = secrets
        self.shutdown_script = shutdown_script
        self.tags = tags
        self.vm_name = vm_name
        self.vm_name_prefix = vm_name_prefix


class Compute:
    """
    # Arguments
    launch_specification: LaunchSpecification
    os: str
    preferred_zone: str
    vm_sizes: VmSizes
    zones: List[str]
    """

    def __init__(
            self,
            launch_specification: LaunchSpecification = none,
            os: str = none,
            preferred_zone: str = none,
            vm_sizes: VmSizes = none,
            zones: List[str] = none):
        self.launch_specification = launch_specification
        self.os = os
        self.preferred_zone = preferred_zone
        self.vm_sizes = vm_sizes
        self.zones = zones

# endregion

# region StatefulNode

class StatefulNode:
    """
    # Arguments
    compute: Compute
    description: str
    health: Health    
    name: str
    persistence: Persistence
    region: str
    resource_group_name: str
    scheduling: Scheduling
    strategy: Strategy
    """

    def __init__(
            self,
            compute: Compute =none,
            description: str = none,
            health: Health =none,
            name: str = none,
            persistence: Persistence =none,
            region: str = none,
            resource_group_name: str = none,
            scheduling: Scheduling =none,
            strategy: Strategy =none):
        self.compute = compute
        self.description = description
        self.health = health
        self.name = name
        self.persistence = persistence
        self.region = region
        self.resource_group_name = resource_group_name
        self.scheduling = scheduling
        self.strategy = strategy

# endregion


# region Client Requests
class CreateStatefulNodeRequest:
    def __init__(self, stateful_node: StatefulNode):
        self.stateful_node = stateful_node

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class UpdateStatefulNodeRequest:
    def __init__(self, stateful_node: StatefulNode):
        self.stateful_node = stateful_node

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class Deallocate:
    def __init__(
            self,
            should_deallocate: bool = none,
            ttl_in_hours: int = none):
        self.should_deallocate = should_deallocate
        self.ttl_in_hours = ttl_in_hours

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class DeallocationConfig:
    def __init__(self,
                 disk_deallocation_config: Deallocate = none,
                 network_deallocation_config: Deallocate = none,
                 public_ip_deallocation_config: Deallocate = none,
                 snapshot_deallocation_config: Deallocate = none,
                 should_terminate_vm: bool = none):
        self.disk_deallocation_config = disk_deallocation_config
        self.network_deallocation_config = network_deallocation_config
        self.public_ip_deallocation_config = public_ip_deallocation_config
        self.snapshot_deallocation_config = snapshot_deallocation_config
        self.should_terminate_vm = should_terminate_vm

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class DeleteStatefulNodeRequest:
    def __init__(self, deallocation_config: DeallocationConfig = none):
        self.deallocation_config = deallocation_config

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class ImportVmConfiguration:
    def __init__(self,
                 draining_timeout: int = none,
                 node: StatefulNode = none,
                 original_vm_name: str = none,
                 resource_group_name: str = none,
                 resource_retention_time: int = none):
        self.draining_timeout = draining_timeout
        self.node = node
        self.original_vm_name = original_vm_name
        self.resource_group_name = resource_group_name
        self.resource_retention_time = resource_retention_time

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class ImportVmToStatefulNodeRequest:
    def __init__(self, import_vm_configuration: ImportVmConfiguration = none):
        self.stateful_node_import = import_vm_configuration

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class AttachDataDiskConfiguration:
    def __init__(
            self,
            data_disk_name: str = none,
            data_disk_resource_group_name: str = none,
            lun: int = none,
            size_g_b: int = none,
            storage_account_type: str = none,
            zone: str = none):
        self.data_disk_name = data_disk_name
        self.data_disk_resource_group_name = data_disk_resource_group_name
        self.lun = lun
        self.size_g_b = size_g_b
        self.storage_account_type = storage_account_type
        self.zone = zone


class AttachDataDiskToStatefulNodeRequest:
    def __init__(self, attach_data_disk_configuration: AttachDataDiskConfiguration = none):
        self.data_disk_name = attach_data_disk_configuration.data_disk_name
        self.data_disk_resource_group_name = attach_data_disk_configuration.data_disk_resource_group_name
        self.lun = attach_data_disk_configuration.lun
        self.size_g_b = attach_data_disk_configuration.size_g_b
        self.storage_account_type = attach_data_disk_configuration.storage_account_type
        self.zone = attach_data_disk_configuration.zone

    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=4)


class DetachDataDiskConfiguration:
    def __init__(
            self,
            data_disk_name: str = none,
            data_disk_resource_group_name: str = none,
            should_deallocate: bool = none,
            ttl_in_hours: int = none):
        self.data_disk_name = data_disk_name
        self.data_disk_resource_group_name = data_disk_resource_group_name
        self.should_deallocate = should_deallocate
        self.ttl_in_hours = ttl_in_hours


class DetachDataDiskFromStatefulNodeRequest:
    def __init__(self, detach_data_disk_configuration: DetachDataDiskConfiguration = none):
        self.data_disk_name = detach_data_disk_configuration.data_disk_name
        self.data_disk_resource_group_name = detach_data_disk_configuration.data_disk_resource_group_name
        self.should_deallocate = detach_data_disk_configuration.should_deallocate
        self.ttl_in_hours = detach_data_disk_configuration.ttl_in_hours

    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=4)

# endregion
