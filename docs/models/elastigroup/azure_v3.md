<h1 id="spotinst_sdk2.models.elastigroup.azure_v3">spotinst_sdk2.models.elastigroup.azure_v3</h1>


<h2 id="spotinst_sdk2.models.elastigroup.azure_v3.Elastigroup">Elastigroup</h2>

```python
Elastigroup(self,
            name='d3043820717d74d9a17694c176d39733',
            region='d3043820717d74d9a17694c176d39733',
            resource_group_name='d3043820717d74d9a17694c176d39733',
            description='d3043820717d74d9a17694c176d39733',
            capacity='d3043820717d74d9a17694c176d39733',
            strategy='d3043820717d74d9a17694c176d39733',
            compute='d3043820717d74d9a17694c176d39733',
            scaling='d3043820717d74d9a17694c176d39733',
            health='d3043820717d74d9a17694c176d39733',
            scheduling='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __region__: str
- __resource_group_name__: str
- __description__: str
- __capacity__: Capacity
- __strategy__: Strategy
- __compute__: Compute
- __scaling__: Scaling
- __health__: Health
- __scheduling__: Scheduling

<h2 id="spotinst_sdk2.models.elastigroup.azure_v3.Capacity">Capacity</h2>

```python
Capacity(self,
         minimum='d3043820717d74d9a17694c176d39733',
         maximum='d3043820717d74d9a17694c176d39733',
         target='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __minimum__: int
- __maximum__: int
- __target__: int

<h2 id="spotinst_sdk2.models.elastigroup.azure_v3.Compute">Compute</h2>

```python
Compute(self,
        launch_specification='d3043820717d74d9a17694c176d39733',
        os='d3043820717d74d9a17694c176d39733',
        preferred_zones='d3043820717d74d9a17694c176d39733',
        vm_sizes='d3043820717d74d9a17694c176d39733',
        zones='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __launch_specification__: LaunchSpecification
- __os__: str
- __preferred_zones__: List[str]
- __vm_sizes__: VmSizes
- __zones__: List[str]


<h2 id="spotinst_sdk2.models.elastigroup.azure_v3.LaunchSpecification">LaunchSpecification</h2>

```python
LaunchSpecification(
  self,
  boot_diagnostics='d3043820717d74d9a17694c176d39733',
  custom_data='d3043820717d74d9a17694c176d39733',
  data_disks='d3043820717d74d9a17694c176d39733',
  extensions='d3043820717d74d9a17694c176d39733',
  image='d3043820717d74d9a17694c176d39733',
  load_balancers_config='d3043820717d74d9a17694c176d39733',
  login='d3043820717d74d9a17694c176d39733',
  managed_service_identities='d3043820717d74d9a17694c176d39733',
  network='d3043820717d74d9a17694c176d39733',
  os_disk='d3043820717d74d9a17694c176d39733',
  secrets='d3043820717d74d9a17694c176d39733',
  shutdown_script='d3043820717d74d9a17694c176d39733',
  tags='d3043820717d74d9a17694c176d39733',
  vm_name_prefix='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __boot_diagnostics__: BootDiagnostics
- __custom_data__: str
- __data_disks__: List[DataDisk]
- __extensions__: list[Extension]
- __image__: Image
- __load_balancers_config__: LoadBalancerConfig
- __login__: Login
- __managed_service_identities__: list[ManagedServiceIdentity]
- __network__: Network
- __os_disk__: OsDisk
- __secrets__: List[Secret]
- __shutdown_script__: str
- __tags__: list[Tag]
- __vm_name_prefix__: str

<h2 id="spotinst_sdk2.models.elastigroup.azure_v3.BootDiagnostics">BootDiagnostics</h2>

```python
BootDiagnostics(self,
                is_enabled='d3043820717d74d9a17694c176d39733',
                storage_uri='d3043820717d74d9a17694c176d39733',
                type='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __is_enabled__: bool
storage_uri = str
- __type__: str

<h2 id="spotinst_sdk2.models.elastigroup.azure_v3.DataDisk">DataDisk</h2>

```python
DataDisk(self,
         lun='d3043820717d74d9a17694c176d39733',
         size_g_b='d3043820717d74d9a17694c176d39733',
         type='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __lun__: int
size_gb = int
- __type__: str

<h2 id="spotinst_sdk2.models.elastigroup.azure_v3.Extension">Extension</h2>

```python
Extension(self,
          api_version='d3043820717d74d9a17694c176d39733',
          auto_upgrade_minor_version='d3043820717d74d9a17694c176d39733',
          minor_version_auto_upgrade='d3043820717d74d9a17694c176d39733',
          name='d3043820717d74d9a17694c176d39733',
          publisher='d3043820717d74d9a17694c176d39733',
          type='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __api_version__: str
- __auto_upgrade_minor_version__: bool
- __minor_version_auto_upgrade__: bool
- __name__: str
- __publisher__: str
- __type__: str

<h2 id="spotinst_sdk2.models.elastigroup.azure_v3.Image">Image</h2>

```python
Image(self,
      marketplace='d3043820717d74d9a17694c176d39733',
      custom='d3043820717d74d9a17694c176d39733',
      gallery='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __marketplace__: Marketplace
- __custom__: Custom
- __gallery__: Gallery

<h2 id="spotinst_sdk2.models.elastigroup.azure_v3.Marketplace">Marketplace</h2>

```python
Marketplace(self,
            publisher='d3043820717d74d9a17694c176d39733',
            offer='d3043820717d74d9a17694c176d39733',
            sku='d3043820717d74d9a17694c176d39733',
            version='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __publisher__: str
- __offer__: str
- __sku__: str
- __version__: str

<h2 id="spotinst_sdk2.models.elastigroup.azure_v3.Custom">Custom</h2>

```python
Custom(self,
       resource_group_name='d3043820717d74d9a17694c176d39733',
       name='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __resource_group_name__: str
- __name__: str

<h2 id="spotinst_sdk2.models.elastigroup.azure_v3.Gallery">Gallery</h2>

```python
Gallery(self,
        gallery_name='d3043820717d74d9a17694c176d39733',
        image_name='d3043820717d74d9a17694c176d39733',
        resource_group_name='d3043820717d74d9a17694c176d39733',
        spot_account_id='d3043820717d74d9a17694c176d39733',
        version='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __gallery_name__: str
- __image_name__: str
- __resource_group_name__: str
- __spot_account_id__: str
- __version__: str

<h2 id="spotinst_sdk2.models.elastigroup.azure_v3.LoadBalancerConfig">LoadBalancerConfig</h2>

```python
LoadBalancerConfig(self,
                   load_balancers='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __load_balancers__: list[LoadBalancer]

<h2 id="spotinst_sdk2.models.elastigroup.azure_v3.LoadBalancer">LoadBalancer</h2>

```python
LoadBalancer(self,
             balancer_id='d3043820717d74d9a17694c176d39733',
             target_set_id='d3043820717d74d9a17694c176d39733',
             auto_weight='d3043820717d74d9a17694c176d39733',
             type='d3043820717d74d9a17694c176d39733',
             resource_group_name='d3043820717d74d9a17694c176d39733',
             application_gateway_name='d3043820717d74d9a17694c176d39733',
             backend_pool_name='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __balancer_id__: str
- __target_set_id__: str
- __auto_weight__: bool
- __type__: str
- __resource_group_name__: str
- __application_gateway_name__: str
- __backend_pool_name__: str

<h2 id="spotinst_sdk2.models.elastigroup.azure_v3.Login">Login</h2>

```python
Login(self,
      ssh_public_key='d3043820717d74d9a17694c176d39733',
      user_name='d3043820717d74d9a17694c176d39733',
      password='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __ssh_public_key__: str
- __user_name__: str
- __password__: str

<h2 id="spotinst_sdk2.models.elastigroup.azure_v3.ManagedServiceIdentity">ManagedServiceIdentity</h2>

```python
ManagedServiceIdentity(
  self,
  resource_group_name='d3043820717d74d9a17694c176d39733',
  name='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __resource_group_name__: str
- __name__: str

<h2 id="spotinst_sdk2.models.elastigroup.azure_v3.Network">Network</h2>

```python
Network(self,
        network_interfaces='d3043820717d74d9a17694c176d39733',
        virtual_network_name='d3043820717d74d9a17694c176d39733',
        resource_group_name='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __network_interfaces__: List[NetworkInterface]
- __resource_group_name__: str
- __virtual_network_name__: str

<h2 id="spotinst_sdk2.models.elastigroup.azure_v3.NetworkInterface">NetworkInterface</h2>

```python
NetworkInterface(
  self,
  additional_ip_configurations='d3043820717d74d9a17694c176d39733',
  application_security_groups='d3043820717d74d9a17694c176d39733',
  assign_public_ip='d3043820717d74d9a17694c176d39733',
  enable_ip_forwarding='d3043820717d74d9a17694c176d39733',
  is_primary='d3043820717d74d9a17694c176d39733',
  private_ip_addresses='d3043820717d74d9a17694c176d39733',
  public_ips='d3043820717d74d9a17694c176d39733',
  public_ip_sku='d3043820717d74d9a17694c176d39733',
  security_group='d3043820717d74d9a17694c176d39733',
  subnet_name='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __additional_ip_configurations__: List[AdditionalIpConfiguration]
- __application_security_groups__: List[ApplicationSecurityGroup]
- __assign_public_ip__: bool
- __enable_ip_forwarding__: bool
- __is_primary__: bool
- __private_ip_addresses__: List[str]
- __public_ips__: List[PublicIp]
- __public_ip_sku__: str
- __security_group__: SecurityGroup
- __subnet_name__: str

<h2 id="spotinst_sdk2.models.elastigroup.azure_v3.AdditionalIpConfiguration">AdditionalIpConfiguration</h2>

```python
AdditionalIpConfiguration(
  self,
  name='d3043820717d74d9a17694c176d39733',
  private_ip_address_version='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __private_ip_address_version__: str

<h2 id="spotinst_sdk2.models.elastigroup.azure_v3.ApplicationSecurityGroup">ApplicationSecurityGroup</h2>

```python
ApplicationSecurityGroup(
  self,
  name='d3043820717d74d9a17694c176d39733',
  resource_group_name='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __resource_group_name__: str

<h2 id="spotinst_sdk2.models.elastigroup.azure_v3.PublicIp">PublicIp</h2>

```python
PublicIp(self,
         name='d3043820717d74d9a17694c176d39733',
         resource_group_name='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __resource_group_name__: str

<h2 id="spotinst_sdk2.models.elastigroup.azure_v3.SecurityGroup">SecurityGroup</h2>

```python
SecurityGroup(self,
              name='d3043820717d74d9a17694c176d39733',
              resource_group_name='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __resource_group_name__: str

<h2 id="spotinst_sdk2.models.elastigroup.azure_v3.OsDisk">OsDisk</h2>

```python
OsDisk(self,
       size='d3043820717d74d9a17694c176d39733',
       type='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __size__: int
- __type__: str

<h2 id="spotinst_sdk2.models.elastigroup.azure_v3.Secret">Secret</h2>

```python
Secret(self,
       source_vault='d3043820717d74d9a17694c176d39733',
       vault_certificates='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __source_vault__: SourceVault
- __vault_certificates__: List[VaultCertificate]

<h2 id="spotinst_sdk2.models.elastigroup.azure_v3.SourceVault">SourceVault</h2>

```python
SourceVault(self,
            name='d3043820717d74d9a17694c176d39733',
            resource_group_name='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __resource_group_name__: str

<h2 id="spotinst_sdk2.models.elastigroup.azure_v3.VaultCertificate">VaultCertificate</h2>

```python
VaultCertificate(self,
                 certificate_store='d3043820717d74d9a17694c176d39733',
                 certificate_url='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __certificate_store__: str
- __certificate_url__: str

<h2 id="spotinst_sdk2.models.elastigroup.azure_v3.Tag">Tag</h2>

```python
Tag(self,
    tag_key='d3043820717d74d9a17694c176d39733',
    tag_value='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __tag_key__: str
- __tag_value__: str

<h2 id="spotinst_sdk2.models.elastigroup.azure_v3.VmSizes">VmSizes</h2>

```python
VmSizes(self,
        od_sizes='d3043820717d74d9a17694c176d39733',
        preferred_spot_sizes='d3043820717d74d9a17694c176d39733',
        spot_sizes='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __od_sizes__: list[str]
- __preferred_spot_sizes__: list[str]
- __spot_sizes__: List[str]

<h2 id="spotinst_sdk2.models.elastigroup.azure_v3.Health">Health</h2>

```python
Health(self,
       health_check_types='d3043820717d74d9a17694c176d39733',
       auto_healing='d3043820717d74d9a17694c176d39733',
       grace_period='d3043820717d74d9a17694c176d39733',
       unhealthy_duration='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __health_check_types__: list[str]
- __auto_healing__: bool
- __grace_period__: int
- __unhealthy_duration__: int

<h2 id="spotinst_sdk2.models.elastigroup.azure_v3.Scaling">Scaling</h2>

```python
Scaling(self,
        up='d3043820717d74d9a17694c176d39733',
        down='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __up__:  list[ScalingPolicy]
- __down__: list[ScalingPolicy]

<h2 id="spotinst_sdk2.models.elastigroup.azure_v3.ScalingPolicy">ScalingPolicy</h2>

```python
ScalingPolicy(self,
              is_enabled='d3043820717d74d9a17694c176d39733',
              policy_name='d3043820717d74d9a17694c176d39733',
              namespace='d3043820717d74d9a17694c176d39733',
              metric_name='d3043820717d74d9a17694c176d39733',
              dimensions='d3043820717d74d9a17694c176d39733',
              statistic='d3043820717d74d9a17694c176d39733',
              unit='d3043820717d74d9a17694c176d39733',
              threshold='d3043820717d74d9a17694c176d39733',
              period='d3043820717d74d9a17694c176d39733',
              evaluation_periods='d3043820717d74d9a17694c176d39733',
              cooldown='d3043820717d74d9a17694c176d39733',
              action='d3043820717d74d9a17694c176d39733',
              operator='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __is_enabled__: bool
- __policy_name__: str
- __namespace__: str
- __metric_name__: str
- __dimensions__: list[ScalingPolicyDimension]
- __statistic__: str
- __unit__: str
- __threshold__: float
- __period__: int
- __evaluation_periods__: int
- __cooldown__: int
- __action__: ScalingPolicyAction
- __operator__: str

<h2 id="spotinst_sdk2.models.elastigroup.azure_v3.ScalingPolicyDimension">ScalingPolicyDimension</h2>

```python
ScalingPolicyDimension(self,
                       name='d3043820717d74d9a17694c176d39733',
                       value='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __key__: str
- __value__: str

<h2 id="spotinst_sdk2.models.elastigroup.azure_v3.ScalingPolicyAction">ScalingPolicyAction</h2>

```python
ScalingPolicyAction(self,
                    type='d3043820717d74d9a17694c176d39733',
                    adjustment='d3043820717d74d9a17694c176d39733',
                    target='d3043820717d74d9a17694c176d39733',
                    maximum='d3043820717d74d9a17694c176d39733',
                    minimum='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __type__: str
- __adjustment__: str
- __target__: int
- __maximum__: int
- __minimum__: int

<h2 id="spotinst_sdk2.models.elastigroup.azure_v3.Strategy">Strategy</h2>

```python
Strategy(self,
         draining_timeout='d3043820717d74d9a17694c176d39733',
         on_demand_count='d3043820717d74d9a17694c176d39733',
         optimization_windows='d3043820717d74d9a17694c176d39733',
         orientation='d3043820717d74d9a17694c176d39733',
         revert_to_spot='d3043820717d74d9a17694c176d39733',
         signals='d3043820717d74d9a17694c176d39733',
         spot_percentage='d3043820717d74d9a17694c176d39733',
         fallback_to_od='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __draining_timeout__: int
- __on_demand_count__: int
- __optimization_windows__: List[str]
- __orientation__: str
- __revert_to_spot__: RevertToSpot
- __signals__: List[Signal]
- __spot_percentage__: int
- __fallback_to_od__: bool

<h2 id="spotinst_sdk2.models.elastigroup.azure_v3.RevertToSpot">RevertToSpot</h2>

```python
RevertToSpot(self, perform_at='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __perform_at__: str

<h2 id="spotinst_sdk2.models.elastigroup.azure_v3.Signal">Signal</h2>

```python
Signal(self,
       timeout='d3043820717d74d9a17694c176d39733',
       type='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __timeout__: str
- __type__: str

<h2 id="spotinst_sdk2.models.elastigroup.azure_v3.Scheduling">Scheduling</h2>

```python
Scheduling(self, tasks='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __tasks__: list[SchedulingTask]

<h2 id="spotinst_sdk2.models.elastigroup.azure_v3.SchedulingTask">SchedulingTask</h2>

```python
SchedulingTask(self,
               is_enabled='d3043820717d74d9a17694c176d39733',
               frequency='d3043820717d74d9a17694c176d39733',
               start_time='d3043820717d74d9a17694c176d39733',
               cron_expression='d3043820717d74d9a17694c176d39733',
               type='d3043820717d74d9a17694c176d39733',
               scale_target_capacity='d3043820717d74d9a17694c176d39733',
               scale_min_capacity='d3043820717d74d9a17694c176d39733',
               scale_max_capacity='d3043820717d74d9a17694c176d39733',
               batch_size_percentage='d3043820717d74d9a17694c176d39733',
               grace_period='d3043820717d74d9a17694c176d39733',
               adjustment='d3043820717d74d9a17694c176d39733',
               adjustment_percentage='d3043820717d74d9a17694c176d39733',
               target_capacity='d3043820717d74d9a17694c176d39733',
               min_capacity='d3043820717d74d9a17694c176d39733',
               max_capacity='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __is_enabled__: bool
- __frequency__: str
- __start_time__: str
- __cron_expression__: str
- __type__: str
- __scale_target_capacity__: int
- __scale_min_capacity__: int
- __scale_max_capacity__: int
- __batch_size_percentage__: int
- __grace_period__: int
- __adjustment__: int
- __adjustment_percentage__: int
- __target_capacity__: int
- __min_capacity__: int
- __max_capacity__: int

<h2 id="spotinst_sdk2.models.elastigroup.azure_v3.DetachConfiguration">DetachConfiguration</h2>

```python
DetachConfiguration(
  self,
  draining_timeout='d3043820717d74d9a17694c176d39733',
  should_decrement_target_capacity='d3043820717d74d9a17694c176d39733',
  should_terminate_vms='d3043820717d74d9a17694c176d39733',
  vms_to_detach='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __draining_timeout__: int
- __should_decrement_target_capacity__: bool
- __should_terminate_vms__: bool
- __instances_to_detach__: list[str]

<h2 id="spotinst_sdk2.models.elastigroup.azure_v3.DeploymentConfiguration">DeploymentConfiguration</h2>

```python
DeploymentConfiguration(
  self,
  batch_min_healthy_percentage='d3043820717d74d9a17694c176d39733',
  batch_size_percentage='d3043820717d74d9a17694c176d39733',
  draining_timeout='d3043820717d74d9a17694c176d39733',
  grace_period='d3043820717d74d9a17694c176d39733',
  health_check_types='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __batch_min_healthy_percentage__: int
- __batch_size_percentage__: int
- __draining_timeout__: int
- __grace_period__: int
- __health_check_types__: list[str]

<h2 id="spotinst_sdk2.models.elastigroup.azure_v3.Process">Process</h2>

```python
Process(self,
        name='d3043820717d74d9a17694c176d39733',
        ttl_in_minutes='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __ttl_in_minutes__: int

