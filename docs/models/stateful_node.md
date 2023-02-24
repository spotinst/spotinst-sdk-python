<h1 id="spotinst_sdk2.models.stateful_node">spotinst_sdk2.models.stateful_node</h1>


<h2 id="spotinst_sdk2.models.stateful_node.Persistence">Persistence</h2>

```python
Persistence(
  self,
  data_disks_persistence_mode: str = 'd3043820717d74d9a17694c176d39733',
  os_disk_persistence_mode: str = 'd3043820717d74d9a17694c176d39733',
  should_persist_data_disks: bool = 'd3043820717d74d9a17694c176d39733',
  should_persist_network: bool = 'd3043820717d74d9a17694c176d39733',
  should_persist_os_disk: bool = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __data_disks_persistence_mode__: str
- __os_disk_persistence_mode__: str
- __should_persist_data_disks__: bool
- __should_persist_network__: bool
- __should_persist_os_disk__: bool

<h2 id="spotinst_sdk2.models.stateful_node.Health">Health</h2>

```python
Health(self,
       health_check_types: str = 'd3043820717d74d9a17694c176d39733',
       auto_healing: bool = 'd3043820717d74d9a17694c176d39733',
       grace_period: int = 'd3043820717d74d9a17694c176d39733',
       unhealthy_duration: int = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __health_check_types__: str
- __auto_healing__: bool
- __grace_period__: int
- __unhealthy_duration __: int

<h2 id="spotinst_sdk2.models.stateful_node.SchedulingTask">SchedulingTask</h2>

```python
SchedulingTask(self,
               is_enabled: bool = 'd3043820717d74d9a17694c176d39733',
               cron_expression: str = 'd3043820717d74d9a17694c176d39733',
               type: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __is_enabled__: bool
- __cron_expression__: str
- __type__: str

<h2 id="spotinst_sdk2.models.stateful_node.Scheduling">Scheduling</h2>

```python
Scheduling(
    self,
    tasks:
    typing.List[spotinst_sdk2.models.stateful_node.SchedulingTask] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __tasks__: List[SchedulingTask]

<h2 id="spotinst_sdk2.models.stateful_node.RevertToSpot">RevertToSpot</h2>

```python
RevertToSpot(self, perform_at: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __perform_at__: str

<h2 id="spotinst_sdk2.models.stateful_node.Signal">Signal</h2>

```python
Signal(self,
       timeout: int = 'd3043820717d74d9a17694c176d39733',
       type: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __timeout__: int
- __type__: str

<h2 id="spotinst_sdk2.models.stateful_node.Strategy">Strategy</h2>

```python
Strategy(
    self,
    draining_timeout: int = 'd3043820717d74d9a17694c176d39733',
    fallback_to_od: bool = 'd3043820717d74d9a17694c176d39733',
    od_windows: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
    optimization_windows: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
    preferred_lifecycle: str = 'd3043820717d74d9a17694c176d39733',
    revert_to_spot: RevertToSpot = 'd3043820717d74d9a17694c176d39733',
    signals:
    typing.List[spotinst_sdk2.models.stateful_node.Signal] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __draining_timeout__: int
- __fallback_to_od__: bool
- __od_windows__: List[str]
- __optimization_windows__: List[str]
- __preferred_lifecycle__: str
- __revert_to_spot__: RevertToSpot
- __signals__: List[Signal]

<h2 id="spotinst_sdk2.models.stateful_node.BootDiagnostics">BootDiagnostics</h2>

```python
BootDiagnostics(self,
                is_enabled: bool = 'd3043820717d74d9a17694c176d39733',
                storage_uri: str = 'd3043820717d74d9a17694c176d39733',
                type: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __is_enabled__: bool
storage_uri = str
- __type__: str

<h2 id="spotinst_sdk2.models.stateful_node.DataDisk">DataDisk</h2>

```python
DataDisk(self,
         lun: int = 'd3043820717d74d9a17694c176d39733',
         size_g_b: int = 'd3043820717d74d9a17694c176d39733',
         type: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __lun__: int
size_gb = int
- __type__: str

<h2 id="spotinst_sdk2.models.stateful_node.Extension">Extension</h2>

```python
Extension(
  self,
  api_version: str = 'd3043820717d74d9a17694c176d39733',
  minor_version_auto_upgrade: bool = 'd3043820717d74d9a17694c176d39733',
  name: str = 'd3043820717d74d9a17694c176d39733',
  publisher: str = 'd3043820717d74d9a17694c176d39733',
  type: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __api_version__: str
- __minor_version_auto_upgrade__: bool
- __name__: str
- __publisher__: str
- __type__: str

<h2 id="spotinst_sdk2.models.stateful_node.Marketplace">Marketplace</h2>

```python
Marketplace(self,
            publisher: str = 'd3043820717d74d9a17694c176d39733',
            offer: str = 'd3043820717d74d9a17694c176d39733',
            sku: str = 'd3043820717d74d9a17694c176d39733',
            version: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __publisher__: str
- __offer__: str
- __sku__: str
- __version__: str

<h2 id="spotinst_sdk2.models.stateful_node.Custom">Custom</h2>

```python
Custom(self,
       resource_group_name: str = 'd3043820717d74d9a17694c176d39733',
       name: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __resource_group_name__: str
- __name__: str

<h2 id="spotinst_sdk2.models.stateful_node.Gallery">Gallery</h2>

```python
Gallery(self,
        gallery_name: str = 'd3043820717d74d9a17694c176d39733',
        image_name: str = 'd3043820717d74d9a17694c176d39733',
        resource_group_name: str = 'd3043820717d74d9a17694c176d39733',
        spot_account_id: str = 'd3043820717d74d9a17694c176d39733',
        version_name: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __gallery_name__: str
- __image_name__: str
- __resource_group_name__: str
- __spot_account_id__: str
- __version_name__: str

<h2 id="spotinst_sdk2.models.stateful_node.Image">Image</h2>

```python
Image(self,
      marketplace: Marketplace = 'd3043820717d74d9a17694c176d39733',
      custom: Custom = 'd3043820717d74d9a17694c176d39733',
      gallery: Gallery = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __marketplace__: Marketplace
- __custom__: Custom
- __gallery__: Gallery

<h2 id="spotinst_sdk2.models.stateful_node.LoadBalancer">LoadBalancer</h2>

```python
LoadBalancer(
  self,
  backend_pool_names:
    typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  load_balancer_sku: str = 'd3043820717d74d9a17694c176d39733',
  name: str = 'd3043820717d74d9a17694c176d39733',
  resource_group_name: str = 'd3043820717d74d9a17694c176d39733',
  type: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __backend_pool_names__: List[str]
- __load_balancer_sku__: str
- __name__: str
- __resource_group_name__: str
- __type__: str

<h2 id="spotinst_sdk2.models.stateful_node.LoadBalancerConfig">LoadBalancerConfig</h2>

```python
LoadBalancerConfig(
    self,
    load_balancers:
    typing.List[spotinst_sdk2.models.stateful_node.LoadBalancer] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __load_balancers__: List[LoadBalancer]

<h2 id="spotinst_sdk2.models.stateful_node.Login">Login</h2>

```python
Login(self,
      ssh_public_key: str = 'd3043820717d74d9a17694c176d39733',
      user_name: str = 'd3043820717d74d9a17694c176d39733',
      password: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __ssh_public_key__: str
- __user_name__: str
- __password__: str

<h2 id="spotinst_sdk2.models.stateful_node.ManagedServiceIdentity">ManagedServiceIdentity</h2>

```python
ManagedServiceIdentity(
  self,
  resource_group_name: str = 'd3043820717d74d9a17694c176d39733',
  name: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __resource_group_name__: str
- __name__: str

<h2 id="spotinst_sdk2.models.stateful_node.AdditionalIpConfiguration">AdditionalIpConfiguration</h2>

```python
AdditionalIpConfiguration(
  self,
  name: str = 'd3043820717d74d9a17694c176d39733',
  private_ip_address_version: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __private_ip_address_version__: str

<h2 id="spotinst_sdk2.models.stateful_node.ApplicationSecurityGroup">ApplicationSecurityGroup</h2>

```python
ApplicationSecurityGroup(
  self,
  name: str = 'd3043820717d74d9a17694c176d39733',
  resource_group_name: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __resource_group_name__: str

<h2 id="spotinst_sdk2.models.stateful_node.NetworkSecurityGroup">NetworkSecurityGroup</h2>

```python
NetworkSecurityGroup(
  self,
  name: str = 'd3043820717d74d9a17694c176d39733',
  resource_group_name: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __resource_group_name__: str

<h2 id="spotinst_sdk2.models.stateful_node.PublicIp">PublicIp</h2>

```python
PublicIp(self,
         name: str = 'd3043820717d74d9a17694c176d39733',
         resource_group_name: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __resource_group_name__: str

<h2 id="spotinst_sdk2.models.stateful_node.NetworkInterface">NetworkInterface</h2>

```python
NetworkInterface(
  self,
  additional_ip_configurations:
    typing.List[spotinst_sdk2.models.stateful_node.AdditionalIpConfiguration] = 'd3043820717d74d9a17694c176d39733',
  application_security_groups:
    typing.List[spotinst_sdk2.models.stateful_node.ApplicationSecurityGroup] = 'd3043820717d74d9a17694c176d39733',
  assign_public_ip: bool = 'd3043820717d74d9a17694c176d39733',
  enable_ip_forwarding: bool = 'd3043820717d74d9a17694c176d39733',
  is_primary: bool = 'd3043820717d74d9a17694c176d39733',
  network_security_group='d3043820717d74d9a17694c176d39733',
  private_ip_addresses:
    typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  public_ips:
    typing.List[spotinst_sdk2.models.stateful_node.PublicIp] = 'd3043820717d74d9a17694c176d39733',
  public_ip_sku: str = 'd3043820717d74d9a17694c176d39733',
  subnet_name: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __additional_ip_configurations__: List[AdditionalIpConfiguration]
- __application_security_groups__: List[ApplicationSecurityGroup]
- __assign_public_ip__: bool
- __enable_ip_forwarding__: bool
- __is_primary__: bool
- __network_security_group__: NetworkSecurityGroup
- __private_ip_addresses__: List[str]
- __public_ips__: List[PublicIp]
- __public_ip_sku__: str
- __subnet_name__: str

<h2 id="spotinst_sdk2.models.stateful_node.Network">Network</h2>

```python
Network(
  self,
  network_interfaces:
    typing.List[spotinst_sdk2.models.stateful_node.NetworkInterface] = 'd3043820717d74d9a17694c176d39733',
  virtual_network_name: str = 'd3043820717d74d9a17694c176d39733',
  resource_group_name: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __network_interfaces__: List[NetworkInterface]
- __resource_group_name__: str
- __virtual_network_name__: str

<h2 id="spotinst_sdk2.models.stateful_node.OsDisk">OsDisk</h2>

```python
OsDisk(self,
       size_g_b: int = 'd3043820717d74d9a17694c176d39733',
       type: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __size_g_b__: int
- __type__: str

<h2 id="spotinst_sdk2.models.stateful_node.SourceVault">SourceVault</h2>

```python
SourceVault(
  self,
  name: str = 'd3043820717d74d9a17694c176d39733',
  resource_group_name: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __resource_group_name__: str

<h2 id="spotinst_sdk2.models.stateful_node.VaultCertificate">VaultCertificate</h2>

```python
VaultCertificate(
  self,
  certificate_store: str = 'd3043820717d74d9a17694c176d39733',
  certificate_url: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __certificate_store__: str
- __certificate_url__: str

<h2 id="spotinst_sdk2.models.stateful_node.Secret">Secret</h2>

```python
Secret(
    self,
    source_vault: SourceVault = 'd3043820717d74d9a17694c176d39733',
    vault_certificates:
    typing.List[spotinst_sdk2.models.stateful_node.VaultCertificate] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __source_vault__: SourceVault
- __vault_certificates__: List[VaultCertificate]

<h2 id="spotinst_sdk2.models.stateful_node.Tag">Tag</h2>

```python
Tag(self,
    tag_key: str = 'd3043820717d74d9a17694c176d39733',
    tag_value: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __tag_key__: str
- __tag_value__: str

<h2 id="spotinst_sdk2.models.stateful_node.VmSizes">VmSizes</h2>

```python
VmSizes(
  self,
  od_sizes: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  preferred_spot_sizes:
    typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  spot_sizes: typing.List[str] = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __od_sizes__: List[str]
- __preferred_spot_sizes__: List[str]
- __spot_sizes__: List[str]

<h2 id="spotinst_sdk2.models.stateful_node.LaunchSpecification">LaunchSpecification</h2>

```python
LaunchSpecification(
  self,
  boot_diagnostics: BootDiagnostics = 'd3043820717d74d9a17694c176d39733',
  custom_data: str = 'd3043820717d74d9a17694c176d39733',
  data_disks:
    typing.List[spotinst_sdk2.models.stateful_node.DataDisk] = 'd3043820717d74d9a17694c176d39733',
  extensions:
    typing.List[spotinst_sdk2.models.stateful_node.Extension] = 'd3043820717d74d9a17694c176d39733',
  image: Image = 'd3043820717d74d9a17694c176d39733',
  license_type: str = 'd3043820717d74d9a17694c176d39733',
  load_balancers_config:
    LoadBalancerConfig = 'd3043820717d74d9a17694c176d39733',
  login: Login = 'd3043820717d74d9a17694c176d39733',
  managed_service_identities:
    typing.List[spotinst_sdk2.models.stateful_node.ManagedServiceIdentity] = 'd3043820717d74d9a17694c176d39733',
  network: Network = 'd3043820717d74d9a17694c176d39733',
  os_disk: OsDisk = 'd3043820717d74d9a17694c176d39733',
  secrets:
    typing.List[spotinst_sdk2.models.stateful_node.Secret] = 'd3043820717d74d9a17694c176d39733',
  shutdown_script: str = 'd3043820717d74d9a17694c176d39733',
  tags:
    typing.List[spotinst_sdk2.models.stateful_node.Tag] = 'd3043820717d74d9a17694c176d39733',
  vm_name: str = 'd3043820717d74d9a17694c176d39733',
  vm_name_prefix: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __boot_diagnostics__: BootDiagnostics
- __custom_data__: str
- __data_disks__: List[DataDisk]
- __extensions__: List[Extension]
- __image__: Image
- __license_type__: str
- __load_balancers_config__: LoadBalancerConfig
- __login__: Login
- __managed_service_identities__: List[ManagedServiceIdentity]
- __network__: Network
- __os_disk__: OsDisk
- __secrets__: List[Secret]
- __shutdown_script__: str
- __tags__: List[Tag]
- __vm_name__: str
- __vm_name_prefix__: str

<h2 id="spotinst_sdk2.models.stateful_node.Compute">Compute</h2>

```python
Compute(self,
        launch_specification:
        LaunchSpecification = 'd3043820717d74d9a17694c176d39733',
        os: str = 'd3043820717d74d9a17694c176d39733',
        preferred_zone: str = 'd3043820717d74d9a17694c176d39733',
        vm_sizes: VmSizes = 'd3043820717d74d9a17694c176d39733',
        zones: typing.List[str] = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __launch_specification__: LaunchSpecification
- __os__: str
- __preferred_zone__: str
- __vm_sizes__: VmSizes
- __zones__: List[str]

<h2 id="spotinst_sdk2.models.stateful_node.StatefulNode">StatefulNode</h2>

```python
StatefulNode(
  self,
  compute: Compute = 'd3043820717d74d9a17694c176d39733',
  description: str = 'd3043820717d74d9a17694c176d39733',
  health: Health = 'd3043820717d74d9a17694c176d39733',
  name: str = 'd3043820717d74d9a17694c176d39733',
  persistence: Persistence = 'd3043820717d74d9a17694c176d39733',
  region: str = 'd3043820717d74d9a17694c176d39733',
  resource_group_name: str = 'd3043820717d74d9a17694c176d39733',
  scheduling: Scheduling = 'd3043820717d74d9a17694c176d39733',
  strategy: Strategy = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __compute__: Compute
- __description__: str
- __health__: Health
- __name__: str
- __persistence__: Persistence
- __region__: str
- __resource_group_name__: str
- __scheduling__: Scheduling
- __strategy__: Strategy

