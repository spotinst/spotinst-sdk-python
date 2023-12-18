<h1 id="spotinst_sdk2.models.stateful_node">spotinst_sdk2.models.stateful_node</h1>


<h2 id="spotinst_sdk2.models.stateful_node.PersistenceMode">PersistenceMode</h2>

```python
PersistenceMode(cls,
                value,
                names=None,
                *,
                module,
                qualname,
                type,
                start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.stateful_node.PersistenceMode.on_launch">on_launch</h3>


<h3 id="spotinst_sdk2.models.stateful_node.PersistenceMode.reattach">reattach</h3>


<h2 id="spotinst_sdk2.models.stateful_node.Persistence">Persistence</h2>

```python
Persistence(
  self,
  data_disks_persistence_mode:
    PersistenceMode = 'd3043820717d74d9a17694c176d39733',
  os_disk_persistence_mode:
    PersistenceMode = 'd3043820717d74d9a17694c176d39733',
  should_persist_data_disks: bool = 'd3043820717d74d9a17694c176d39733',
  should_persist_network: bool = 'd3043820717d74d9a17694c176d39733',
  should_persist_os_disk: bool = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __data_disks_persistence_mode__: PersistenceMode
- __os_disk_persistence_mode__: PersistenceMode
- __should_persist_data_disks__: bool
- __should_persist_network__: bool
- __should_persist_os_disk__: bool

<h2 id="spotinst_sdk2.models.stateful_node.HealthCheckTypes">HealthCheckTypes</h2>

```python
HealthCheckTypes(cls,
                 value,
                 names=None,
                 *,
                 module,
                 qualname,
                 type,
                 start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.stateful_node.HealthCheckTypes.application_gateway">application_gateway</h3>


<h3 id="spotinst_sdk2.models.stateful_node.HealthCheckTypes.vm_state">vm_state</h3>


<h2 id="spotinst_sdk2.models.stateful_node.Health">Health</h2>

```python
Health(
  self,
  health_check_types:
    typing.List[spotinst_sdk2.models.stateful_node.HealthCheckTypes] = 'd3043820717d74d9a17694c176d39733',
  auto_healing: bool = 'd3043820717d74d9a17694c176d39733',
  grace_period: int = 'd3043820717d74d9a17694c176d39733',
  unhealthy_duration: int = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __health_check_types__: List[HealthCheckTypes]
- __auto_healing__: bool
- __grace_period__: int
- __unhealthy_duration__: int

<h2 id="spotinst_sdk2.models.stateful_node.SchedulingTaskType">SchedulingTaskType</h2>

```python
SchedulingTaskType(cls,
                   value,
                   names=None,
                   *,
                   module,
                   qualname,
                   type,
                   start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.stateful_node.SchedulingTaskType.pause">pause</h3>


<h3 id="spotinst_sdk2.models.stateful_node.SchedulingTaskType.recycle">recycle</h3>


<h3 id="spotinst_sdk2.models.stateful_node.SchedulingTaskType.resume">resume</h3>


<h2 id="spotinst_sdk2.models.stateful_node.SchedulingTask">SchedulingTask</h2>

```python
SchedulingTask(
  self,
  is_enabled: bool = 'd3043820717d74d9a17694c176d39733',
  cron_expression: str = 'd3043820717d74d9a17694c176d39733',
  type: SchedulingTaskType = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __is_enabled__: bool
- __cron_expression__: str
- __type__: SchedulingTaskType

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

<h2 id="spotinst_sdk2.models.stateful_node.PerformAt">PerformAt</h2>

```python
PerformAt(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.stateful_node.PerformAt.always">always</h3>


<h3 id="spotinst_sdk2.models.stateful_node.PerformAt.never">never</h3>


<h3 id="spotinst_sdk2.models.stateful_node.PerformAt.time_window">time_window</h3>


<h2 id="spotinst_sdk2.models.stateful_node.RevertToSpot">RevertToSpot</h2>

```python
RevertToSpot(self,
             perform_at: PerformAt = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __perform_at__: PerformAt

<h2 id="spotinst_sdk2.models.stateful_node.SignalType">SignalType</h2>

```python
SignalType(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.stateful_node.SignalType.vm_ready">vm_ready</h3>


<h3 id="spotinst_sdk2.models.stateful_node.SignalType.vm_ready_to_shutdown">vm_ready_to_shutdown</h3>


<h2 id="spotinst_sdk2.models.stateful_node.Signal">Signal</h2>

```python
Signal(self,
       timeout: int = 'd3043820717d74d9a17694c176d39733',
       type: SignalType = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __timeout__: int
- __type__: SignalType

<h2 id="spotinst_sdk2.models.stateful_node.CapacityReservationGroups">CapacityReservationGroups</h2>

```python
CapacityReservationGroups(
  self,
  name: str = 'd3043820717d74d9a17694c176d39733',
  resource_group_name: str = 'd3043820717d74d9a17694c176d39733',
  should_prioritize: bool = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __resource_group_name__: str
- __should_prioritize__: bool

<h2 id="spotinst_sdk2.models.stateful_node.UtilizationStrategy">UtilizationStrategy</h2>

```python
UtilizationStrategy(cls,
                    value,
                    names=None,
                    *,
                    module,
                    qualname,
                    type,
                    start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.stateful_node.UtilizationStrategy.utilize_over_od">utilize_over_od</h3>


<h3 id="spotinst_sdk2.models.stateful_node.UtilizationStrategy.utilize_over_spot">utilize_over_spot</h3>


<h2 id="spotinst_sdk2.models.stateful_node.CapacityReservation">CapacityReservation</h2>

```python
CapacityReservation(
    self,
    capacity_reservation_groups:
    typing.List[spotinst_sdk2.models.stateful_node.CapacityReservationGroups] = 'd3043820717d74d9a17694c176d39733',
    should_utilize: bool = 'd3043820717d74d9a17694c176d39733',
    utilization_strategy:
    UtilizationStrategy = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __capacity_reservation_groups__: List[CapacityReservationGroups]
- __should_utilize__: bool
- __utilization_strategy__: UtilizationStrategy

<h2 id="spotinst_sdk2.models.stateful_node.PreferredLifeCycle">PreferredLifeCycle</h2>

```python
PreferredLifeCycle(cls,
                   value,
                   names=None,
                   *,
                   module,
                   qualname,
                   type,
                   start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.stateful_node.PreferredLifeCycle.od">od</h3>


<h3 id="spotinst_sdk2.models.stateful_node.PreferredLifeCycle.spot">spot</h3>


<h2 id="spotinst_sdk2.models.stateful_node.Strategy">Strategy</h2>

```python
Strategy(
    self,
    availability_vs_cost: int = 'd3043820717d74d9a17694c176d39733',
    capacity_reservation:
    CapacityReservation = 'd3043820717d74d9a17694c176d39733',
    draining_timeout: int = 'd3043820717d74d9a17694c176d39733',
    fallback_to_od: bool = 'd3043820717d74d9a17694c176d39733',
    od_windows: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
    optimization_windows: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
    preferred_lifecycle:
    PreferredLifeCycle = 'd3043820717d74d9a17694c176d39733',
    revert_to_spot: RevertToSpot = 'd3043820717d74d9a17694c176d39733',
    signals:
    typing.List[spotinst_sdk2.models.stateful_node.Signal] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __availability_vs_cost__: int
- __capacity_reservation__: CapacityReservation
- __draining_timeout__: int
- __fallback_to_od__: bool
- __od_windows__: List[str]
- __optimization_windows__: List[str]
- __preferred_lifecycle__: PreferredLifeCycle
- __revert_to_spot__: RevertToSpot
- __signals__: List[Signal]

<h2 id="spotinst_sdk2.models.stateful_node.StorageType">StorageType</h2>

```python
StorageType(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.stateful_node.StorageType.managed">managed</h3>


<h3 id="spotinst_sdk2.models.stateful_node.StorageType.unmanaged">unmanaged</h3>


<h2 id="spotinst_sdk2.models.stateful_node.BootDiagnostics">BootDiagnostics</h2>

```python
BootDiagnostics(self,
                is_enabled: bool = 'd3043820717d74d9a17694c176d39733',
                storage_uri: str = 'd3043820717d74d9a17694c176d39733',
                type: StorageType = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __is_enabled__: bool
storage_uri = str
- __type__: StorageType

<h2 id="spotinst_sdk2.models.stateful_node.DataDiskType">DataDiskType</h2>

```python
DataDiskType(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.stateful_node.DataDiskType.premium_lrs">premium_lrs</h3>


<h3 id="spotinst_sdk2.models.stateful_node.DataDiskType.standard_lrs">standard_lrs</h3>


<h3 id="spotinst_sdk2.models.stateful_node.DataDiskType.standard_ssd_lrs">standard_ssd_lrs</h3>


<h3 id="spotinst_sdk2.models.stateful_node.DataDiskType.ultra_ssd_lrs">ultra_ssd_lrs</h3>


<h2 id="spotinst_sdk2.models.stateful_node.DataDisk">DataDisk</h2>

```python
DataDisk(self,
         lun: int = 'd3043820717d74d9a17694c176d39733',
         size_g_b: int = 'd3043820717d74d9a17694c176d39733',
         type: DataDiskType = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __lun__: int
size_g_b = int
- __type__: DataDiskType

<h2 id="spotinst_sdk2.models.stateful_node.Extension">Extension</h2>

```python
Extension(
  self,
  api_version: str = 'd3043820717d74d9a17694c176d39733',
  minor_version_auto_upgrade: bool = 'd3043820717d74d9a17694c176d39733',
  name: str = 'd3043820717d74d9a17694c176d39733',
  protected_settings='d3043820717d74d9a17694c176d39733',
  public_settings='d3043820717d74d9a17694c176d39733',
  publisher: str = 'd3043820717d74d9a17694c176d39733',
  type: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __api_version__: str
- __minor_version_auto_upgrade__: bool
- __name__: str
- __protected_settings__: ProtectedSettings
- __public_settings__: PublicSettings
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

<h2 id="spotinst_sdk2.models.stateful_node.LoadBalancerType">LoadBalancerType</h2>

```python
LoadBalancerType(cls,
                 value,
                 names=None,
                 *,
                 module,
                 qualname,
                 type,
                 start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.stateful_node.LoadBalancerType.application_gateway">application_gateway</h3>


<h3 id="spotinst_sdk2.models.stateful_node.LoadBalancerType.load_balancer">load_balancer</h3>


<h2 id="spotinst_sdk2.models.stateful_node.LoadBalancer">LoadBalancer</h2>

```python
LoadBalancer(
  self,
  backend_pool_names:
    typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  load_balancer_sku: str = 'd3043820717d74d9a17694c176d39733',
  name: str = 'd3043820717d74d9a17694c176d39733',
  resource_group_name: str = 'd3043820717d74d9a17694c176d39733',
  type: LoadBalancerType = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __backend_pool_names__: List[str]
- __load_balancer_sku__: str
- __name__: str
- __resource_group_name__: str
- __type__: LoadBalancerType

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

<h2 id="spotinst_sdk2.models.stateful_node.PrivateIpAddressVersion">PrivateIpAddressVersion</h2>

```python
PrivateIpAddressVersion(cls,
                        value,
                        names=None,
                        *,
                        module,
                        qualname,
                        type,
                        start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.stateful_node.PrivateIpAddressVersion.ipv4">ipv4</h3>


<h3 id="spotinst_sdk2.models.stateful_node.PrivateIpAddressVersion.ipv6">ipv6</h3>


<h2 id="spotinst_sdk2.models.stateful_node.AdditionalIpConfiguration">AdditionalIpConfiguration</h2>

```python
AdditionalIpConfiguration(
    self,
    name: str = 'd3043820717d74d9a17694c176d39733',
    private_ip_address_version:
    PrivateIpAddressVersion = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __private_ip_address_version__: PrivateIpAddressVersion

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

<h2 id="spotinst_sdk2.models.stateful_node.PublicIpSku">PublicIpSku</h2>

```python
PublicIpSku(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.stateful_node.PublicIpSku.basic">basic</h3>


<h3 id="spotinst_sdk2.models.stateful_node.PublicIpSku.standard">standard</h3>


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
  network_security_group:
    NetworkSecurityGroup = 'd3043820717d74d9a17694c176d39733',
  private_ip_addresses:
    typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  public_ips:
    typing.List[spotinst_sdk2.models.stateful_node.PublicIp] = 'd3043820717d74d9a17694c176d39733',
  public_ip_sku: PublicIpSku = 'd3043820717d74d9a17694c176d39733',
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
       type: DataDiskType = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __size_g_b__: int
- __type__: DataDiskType

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

<h2 id="spotinst_sdk2.models.stateful_node.ProximityPlacementGroups">ProximityPlacementGroups</h2>

```python
ProximityPlacementGroups(
  self,
  name: str = 'd3043820717d74d9a17694c176d39733',
  resource_group_name: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __resource_group_name__: str

<h2 id="spotinst_sdk2.models.stateful_node.SecurityType">SecurityType</h2>

```python
SecurityType(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.stateful_node.SecurityType.standard">standard</h3>


<h3 id="spotinst_sdk2.models.stateful_node.SecurityType.trusted_launch">trusted_launch</h3>


<h2 id="spotinst_sdk2.models.stateful_node.Security">Security</h2>

```python
Security(
  self,
  secure_boot_enabled: bool = 'd3043820717d74d9a17694c176d39733',
  security_type: SecurityType = 'd3043820717d74d9a17694c176d39733',
  v_tpm_enabled: bool = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __secure_boot_enabled__: bool
- __security_type__: SecurityType
- __v_tpm_enabled__: bool

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
  proximity_placement_groups:
    typing.List[spotinst_sdk2.models.stateful_node.ProximityPlacementGroups] = 'd3043820717d74d9a17694c176d39733',
  secrets:
    typing.List[spotinst_sdk2.models.stateful_node.Secret] = 'd3043820717d74d9a17694c176d39733',
  security: Security = 'd3043820717d74d9a17694c176d39733',
  shutdown_script: str = 'd3043820717d74d9a17694c176d39733',
  tags:
    typing.List[spotinst_sdk2.models.stateful_node.Tag] = 'd3043820717d74d9a17694c176d39733',
  user_data: str = 'd3043820717d74d9a17694c176d39733',
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
- __proximity_placement_groups__: List[ProximityPlacementGroups]
- __secrets__: List[Secret]
- __security__: Security
- __shutdown_script__: str
- __tags__: List[Tag]
- __user_data__: str
- __vm_name__: str
- __vm_name_prefix__: str

<h2 id="spotinst_sdk2.models.stateful_node.OsType">OsType</h2>

```python
OsType(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.stateful_node.OsType.linux">linux</h3>


<h3 id="spotinst_sdk2.models.stateful_node.OsType.windows">windows</h3>


<h2 id="spotinst_sdk2.models.stateful_node.Compute">Compute</h2>

```python
Compute(self,
        launch_specification:
        LaunchSpecification = 'd3043820717d74d9a17694c176d39733',
        os: OsType = 'd3043820717d74d9a17694c176d39733',
        preferred_zone: str = 'd3043820717d74d9a17694c176d39733',
        vm_sizes: VmSizes = 'd3043820717d74d9a17694c176d39733',
        zones: typing.List[str] = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __launch_specification__: LaunchSpecification
- __os__: OsType
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

