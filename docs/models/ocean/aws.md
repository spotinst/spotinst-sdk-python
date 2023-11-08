<h1 id="spotinst_sdk2.models.ocean.aws">spotinst_sdk2.models.ocean.aws</h1>


<h2 id="spotinst_sdk2.models.ocean.aws.ResourceLimits">ResourceLimits</h2>

```python
ResourceLimits(self,
               max_memory_gib: int = 'd3043820717d74d9a17694c176d39733',
               max_v_cpu: int = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __max_memory_gib__: int
- __max_v_cpu__: int

<h2 id="spotinst_sdk2.models.ocean.aws.Down">Down</h2>

```python
Down(
  self,
  max_scale_down_percentage: int = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __max_scale_down_percentage__: int

<h2 id="spotinst_sdk2.models.ocean.aws.Headroom">Headroom</h2>

```python
Headroom(self,
         cpu_per_unit: int = 'd3043820717d74d9a17694c176d39733',
         memory_per_unit: int = 'd3043820717d74d9a17694c176d39733',
         gpu_per_unit: int = 'd3043820717d74d9a17694c176d39733',
         num_of_units: int = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __cpu_per_unit__: int
- __memory_per_unit__: int
- __gpu_per_unit__: int
- __num_of_units__: int

<h2 id="spotinst_sdk2.models.ocean.aws.AutoScaler">AutoScaler</h2>

```python
AutoScaler(
    self,
    is_enabled: bool = 'd3043820717d74d9a17694c176d39733',
    cooldown: int = 'd3043820717d74d9a17694c176d39733',
    resource_limits: ResourceLimits = 'd3043820717d74d9a17694c176d39733',
    down: Down = 'd3043820717d74d9a17694c176d39733',
    headroom: Headroom = 'd3043820717d74d9a17694c176d39733',
    is_auto_config: bool = 'd3043820717d74d9a17694c176d39733',
    auto_headroom_percentage: int = 'd3043820717d74d9a17694c176d39733',
    enable_automatic_and_manual_headroom:
    bool = 'd3043820717d74d9a17694c176d39733',
    extended_resource_definitions:
    typing.List[str] = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __is_enabled__: bool
- __cooldown__: int
- __resource_limits__: ResourceLimits
- __down__: Down
- __headroom__: Headroom
- __is_auto_config__: bool
- __auto_headroom_percentage__: int
- __enable_automatic_and_manual_headroom__: bool
- __extended_resource_definitions__: List[str]

<h2 id="spotinst_sdk2.models.ocean.aws.Capacity">Capacity</h2>

```python
Capacity(self,
         minimum: int = 'd3043820717d74d9a17694c176d39733',
         maximum: int = 'd3043820717d74d9a17694c176d39733',
         target: int = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __minimum__: int
- __maximum__: int
- __target__: int

<h2 id="spotinst_sdk2.models.ocean.aws.AvailabilityVsCost">AvailabilityVsCost</h2>

```python
AvailabilityVsCost(cls,
                   value,
                   names=None,
                   *,
                   module,
                   qualname,
                   type,
                   start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.aws.AvailabilityVsCost.balanced">balanced</h3>


<h3 id="spotinst_sdk2.models.ocean.aws.AvailabilityVsCost.cheapest">cheapest</h3>


<h3 id="spotinst_sdk2.models.ocean.aws.AvailabilityVsCost.cost_oriented">cost_oriented</h3>


<h2 id="spotinst_sdk2.models.ocean.aws.ClusterOrientation">ClusterOrientation</h2>

```python
ClusterOrientation(
    self,
    availability_vs_cost:
    AvailabilityVsCost = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __availability_vs_cost__: AvailabilityVsCost

<h2 id="spotinst_sdk2.models.ocean.aws.SpreadNodesBy">SpreadNodesBy</h2>

```python
SpreadNodesBy(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.aws.SpreadNodesBy.count">count</h3>


<h3 id="spotinst_sdk2.models.ocean.aws.SpreadNodesBy.vcpu">vcpu</h3>


<h2 id="spotinst_sdk2.models.ocean.aws.Strategy">Strategy</h2>

```python
Strategy(
  self,
  utilize_reserved_instances: bool = 'd3043820717d74d9a17694c176d39733',
  fallback_to_od: bool = 'd3043820717d74d9a17694c176d39733',
  spot_percentage: int = 'd3043820717d74d9a17694c176d39733',
  grace_period: int = 'd3043820717d74d9a17694c176d39733',
  draining_timeout: int = 'd3043820717d74d9a17694c176d39733',
  utilize_commitments: bool = 'd3043820717d74d9a17694c176d39733',
  cluster_orientation:
    ClusterOrientation = 'd3043820717d74d9a17694c176d39733',
  spread_nodes_by: SpreadNodesBy = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __utilize_reserved_instances__: bool
- __fallback_to_od__: bool
- __spot_percentage__: int
- __grace_period__: int
- __draining_timeout__: int
- __utilize_commitments__: bool
- __cluster_orientation__: ClusterOrientation
- __spread_nodes_by__: SpreadNodesBy

<h2 id="spotinst_sdk2.models.ocean.aws.ClusterRoll">ClusterRoll</h2>

```python
ClusterRoll(
  self,
  batch_min_healthy_percentage: int = 'd3043820717d74d9a17694c176d39733',
  batch_size_percentage: int = 'd3043820717d74d9a17694c176d39733',
  comment: str = 'd3043820717d74d9a17694c176d39733',
  respect_pdb: bool = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __batch_min_healthy_percentage__: int
- __batch_size_percentage__: int
- __comment__: str
- __respect_pdb__: bool

<h2 id="spotinst_sdk2.models.ocean.aws.Parameters">Parameters</h2>

```python
Parameters(self,
           cluster_roll: ClusterRoll = 'd3043820717d74d9a17694c176d39733'
           )
```

__Arguments__

- __cluster_roll__: ClusterRoll

<h2 id="spotinst_sdk2.models.ocean.aws.TaskType">TaskType</h2>

```python
TaskType(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.aws.TaskType.cluster_roll">cluster_roll</h3>


<h2 id="spotinst_sdk2.models.ocean.aws.Tasks">Tasks</h2>

```python
Tasks(self,
      cron_expression: str = 'd3043820717d74d9a17694c176d39733',
      is_enabled: bool = 'd3043820717d74d9a17694c176d39733',
      parameters: Parameters = 'd3043820717d74d9a17694c176d39733',
      task_type: TaskType = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __cron_expression__: str
- __is_enabled__: bool
- __parameters__: Parameters
- __task_type__: TaskType

<h2 id="spotinst_sdk2.models.ocean.aws.ShutdownHours">ShutdownHours</h2>

```python
ShutdownHours(
  self,
  is_enabled: bool = 'd3043820717d74d9a17694c176d39733',
  time_windows: typing.List[str] = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __is_enabled__: bool
- __time_windows__: List[str]

<h2 id="spotinst_sdk2.models.ocean.aws.Scheduling">Scheduling</h2>

```python
Scheduling(
  self,
  tasks:
    typing.List[spotinst_sdk2.models.ocean.aws.Tasks] = 'd3043820717d74d9a17694c176d39733',
  shutdown_hours: ShutdownHours = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __tasks__: List[Tasks]
- __shutdown_hours__: ShutdownHours

<h2 id="spotinst_sdk2.models.ocean.aws.ContainerImage">ContainerImage</h2>

```python
ContainerImage(
  self,
  approved_images: typing.List[str] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __approved_images__: List[str]

<h2 id="spotinst_sdk2.models.ocean.aws.Security">Security</h2>

```python
Security(
  self,
  container_image: ContainerImage = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __container_image__: ContainerImage

<h2 id="spotinst_sdk2.models.ocean.aws.Architectures">Architectures</h2>

```python
Architectures(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.aws.Architectures.arm64">arm64</h3>


<h3 id="spotinst_sdk2.models.ocean.aws.Architectures.i386">i386</h3>


<h3 id="spotinst_sdk2.models.ocean.aws.Architectures.x86_64">x86_64</h3>


<h2 id="spotinst_sdk2.models.ocean.aws.Categories">Categories</h2>

```python
Categories(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.aws.Categories.accelerated_computing">accelerated_computing</h3>


<h3 id="spotinst_sdk2.models.ocean.aws.Categories.compute_optimized">compute_optimized</h3>


<h3 id="spotinst_sdk2.models.ocean.aws.Categories.general_purpose">general_purpose</h3>


<h3 id="spotinst_sdk2.models.ocean.aws.Categories.memory_optimized">memory_optimized</h3>


<h3 id="spotinst_sdk2.models.ocean.aws.Categories.storage_optimized">storage_optimized</h3>


<h2 id="spotinst_sdk2.models.ocean.aws.DiskTypes">DiskTypes</h2>

```python
DiskTypes(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.aws.DiskTypes.ebs">ebs</h3>


<h3 id="spotinst_sdk2.models.ocean.aws.DiskTypes.hdd">hdd</h3>


<h3 id="spotinst_sdk2.models.ocean.aws.DiskTypes.nvme">nvme</h3>


<h3 id="spotinst_sdk2.models.ocean.aws.DiskTypes.ssd">ssd</h3>


<h2 id="spotinst_sdk2.models.ocean.aws.Hypervisor">Hypervisor</h2>

```python
Hypervisor(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.aws.Hypervisor.nitro">nitro</h3>


<h3 id="spotinst_sdk2.models.ocean.aws.Hypervisor.xen">xen</h3>


<h2 id="spotinst_sdk2.models.ocean.aws.RootDeviceTypes">RootDeviceTypes</h2>

```python
RootDeviceTypes(cls,
                value,
                names=None,
                *,
                module,
                qualname,
                type,
                start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.aws.RootDeviceTypes.ebs">ebs</h3>


<h3 id="spotinst_sdk2.models.ocean.aws.RootDeviceTypes.instance_store">instance_store</h3>


<h2 id="spotinst_sdk2.models.ocean.aws.VirtualizationTypes">VirtualizationTypes</h2>

```python
VirtualizationTypes(cls,
                    value,
                    names=None,
                    *,
                    module,
                    qualname,
                    type,
                    start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.aws.VirtualizationTypes.hvm">hvm</h3>


<h3 id="spotinst_sdk2.models.ocean.aws.VirtualizationTypes.paravirtual">paravirtual</h3>


<h2 id="spotinst_sdk2.models.ocean.aws.InstanceTypesFilters">InstanceTypesFilters</h2>

```python
InstanceTypesFilters(
    self,
    architectures:
    typing.List[spotinst_sdk2.models.ocean.aws.Architectures] = 'd3043820717d74d9a17694c176d39733',
    categories:
    typing.List[spotinst_sdk2.models.ocean.aws.Categories] = 'd3043820717d74d9a17694c176d39733',
    disk_types:
    typing.List[spotinst_sdk2.models.ocean.aws.DiskTypes] = 'd3043820717d74d9a17694c176d39733',
    exclude_families: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
    exclude_metal: bool = 'd3043820717d74d9a17694c176d39733',
    hypervisor:
    typing.List[spotinst_sdk2.models.ocean.aws.Hypervisor] = 'd3043820717d74d9a17694c176d39733',
    include_families: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
    is_ena_supported: bool = 'd3043820717d74d9a17694c176d39733',
    max_gpu: int = 'd3043820717d74d9a17694c176d39733',
    max_memory_gi_b: float = 'd3043820717d74d9a17694c176d39733',
    max_network_performance: int = 'd3043820717d74d9a17694c176d39733',
    max_vcpu: int = 'd3043820717d74d9a17694c176d39733',
    min_enis: int = 'd3043820717d74d9a17694c176d39733',
    min_gpu: int = 'd3043820717d74d9a17694c176d39733',
    min_memory_gi_b: float = 'd3043820717d74d9a17694c176d39733',
    min_network_performance: int = 'd3043820717d74d9a17694c176d39733',
    min_vcpu: int = 'd3043820717d74d9a17694c176d39733',
    root_device_types:
    typing.List[spotinst_sdk2.models.ocean.aws.RootDeviceTypes] = 'd3043820717d74d9a17694c176d39733',
    virtualization_types:
    typing.List[spotinst_sdk2.models.ocean.aws.VirtualizationTypes] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __architectures__: List[Architectures]
- __categories__: List[Categories]
- __disk_types__: List[DiskTypes]
- __exclude_families__: List[str]
- __exclude_metal__: bool
- __hypervisor__: List[Hypervisor]
- __include_families__: List[str]
- __is_ena_supported__: bool
- __max_gpu__: int
- __max_memory_gi_b__: float
- __max_network_performance__: int
- __max_vcpu__: int
- __min_enis__: int
- __min_gpu__: int
- __min_memory_gi_b__: float
- __min_network_performance__: int
- __min_vcpu__: int
- __root_device_types__: List[RootDeviceTypes]
- __virtualization_types__: List[VirtualizationTypes]

<h2 id="spotinst_sdk2.models.ocean.aws.InstanceTypes">InstanceTypes</h2>

```python
InstanceTypes(
  self,
  blacklist: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  whitelist: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  filters: InstanceTypesFilters = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __blacklist__: List[str]
- __whitelist__: List[str]
- __filters__: InstanceTypesFilters

<h2 id="spotinst_sdk2.models.ocean.aws.DynamicVolumeSize">DynamicVolumeSize</h2>

```python
DynamicVolumeSize(
  self,
  base_size: int = 'd3043820717d74d9a17694c176d39733',
  resource: str = 'd3043820717d74d9a17694c176d39733',
  size_per_resource_unit: int = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __base_size__: int
- __resource__: str
- __size_per_resource_unit__: int

<h2 id="spotinst_sdk2.models.ocean.aws.EBS">EBS</h2>

```python
EBS(
    self,
    throughput: int = 'd3043820717d74d9a17694c176d39733',
    delete_on_termination: bool = 'd3043820717d74d9a17694c176d39733',
    encrypted: bool = 'd3043820717d74d9a17694c176d39733',
    iops: int = 'd3043820717d74d9a17694c176d39733',
    kms_key_id: str = 'd3043820717d74d9a17694c176d39733',
    snapshot_id: str = 'd3043820717d74d9a17694c176d39733',
    volume_type: str = 'd3043820717d74d9a17694c176d39733',
    volume_size: int = 'd3043820717d74d9a17694c176d39733',
    dynamic_volume_size: DynamicVolumeSize = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __throughput__: int
- __delete_on_termination__: bool
- __encrypted__: bool
- __iops__: int
- __kms_key_id__: str
- __snapshot_id__:  str
- __volume_type__: str
- __volume_size__: int
- __dynamic_volume_size__: DynamicVolumeSize

<h2 id="spotinst_sdk2.models.ocean.aws.BlockDeviceMappings">BlockDeviceMappings</h2>

```python
BlockDeviceMappings(
  self,
  device_name: str = 'd3043820717d74d9a17694c176d39733',
  ebs: EBS = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __device_name__: str
- __ebs__: EBS

<h2 id="spotinst_sdk2.models.ocean.aws.IamInstanceProfile">IamInstanceProfile</h2>

```python
IamInstanceProfile(self,
                   name: str = 'd3043820717d74d9a17694c176d39733',
                   arn: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __arn__: str

<h2 id="spotinst_sdk2.models.ocean.aws.HttpEndpoint">HttpEndpoint</h2>

```python
HttpEndpoint(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.aws.HttpEndpoint.disabled">disabled</h3>


<h3 id="spotinst_sdk2.models.ocean.aws.HttpEndpoint.enabled">enabled</h3>


<h2 id="spotinst_sdk2.models.ocean.aws.HttpTokens">HttpTokens</h2>

```python
HttpTokens(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.aws.HttpTokens.optional">optional</h3>


<h3 id="spotinst_sdk2.models.ocean.aws.HttpTokens.required">required</h3>


<h2 id="spotinst_sdk2.models.ocean.aws.InstanceMetadataOptions">InstanceMetadataOptions</h2>

```python
InstanceMetadataOptions(
  self,
  http_endpoint: HttpEndpoint = 'd3043820717d74d9a17694c176d39733',
  http_put_response_hop_limit: int = 'd3043820717d74d9a17694c176d39733',
  http_tokens: HttpTokens = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __http_endpoint__: HttpEndpoint
- __http_put_response_hop_limit__: int
- __http_tokens__: HttpTokens

<h2 id="spotinst_sdk2.models.ocean.aws.LoadBalancerType">LoadBalancerType</h2>

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
<h3 id="spotinst_sdk2.models.ocean.aws.LoadBalancerType.classic">classic</h3>


<h3 id="spotinst_sdk2.models.ocean.aws.LoadBalancerType.target_group">target_group</h3>


<h2 id="spotinst_sdk2.models.ocean.aws.LoadBalancer">LoadBalancer</h2>

```python
LoadBalancer(
  self,
  arn: str = 'd3043820717d74d9a17694c176d39733',
  name: str = 'd3043820717d74d9a17694c176d39733',
  type: LoadBalancerType = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __arn__: str
- __name__: str
- __type__: str

<h2 id="spotinst_sdk2.models.ocean.aws.Tags">Tags</h2>

```python
Tags(self,
     tag_key: str = 'd3043820717d74d9a17694c176d39733',
     tag_value: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __tag_key__: str
- __tag_value__: str

<h2 id="spotinst_sdk2.models.ocean.aws.Volumes">Volumes</h2>

```python
Volumes(self, should_tag: bool = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __should_tag__: str

<h2 id="spotinst_sdk2.models.ocean.aws.ResourceTagSpecification">ResourceTagSpecification</h2>

```python
ResourceTagSpecification(
  self, volumes: Volumes = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __volumes__: Volumes

<h2 id="spotinst_sdk2.models.ocean.aws.LaunchSpecifications">LaunchSpecifications</h2>

```python
LaunchSpecifications(
  self,
  associate_ipv6_address: bool = 'd3043820717d74d9a17694c176d39733',
  associate_public_ip_address: bool = 'd3043820717d74d9a17694c176d39733',
  block_device_mappings:
    typing.List[spotinst_sdk2.models.ocean.aws.BlockDeviceMappings] = 'd3043820717d74d9a17694c176d39733',
  ebs_optimized: bool = 'd3043820717d74d9a17694c176d39733',
  iam_instance_profile:
    IamInstanceProfile = 'd3043820717d74d9a17694c176d39733',
  image_id: str = 'd3043820717d74d9a17694c176d39733',
  instance_metadata_options:
    InstanceMetadataOptions = 'd3043820717d74d9a17694c176d39733',
  key_pair: str = 'd3043820717d74d9a17694c176d39733',
  load_balancers:
    typing.List[spotinst_sdk2.models.ocean.aws.LoadBalancer] = 'd3043820717d74d9a17694c176d39733',
  monitoring: bool = 'd3043820717d74d9a17694c176d39733',
  resource_tag_specification:
    ResourceTagSpecification = 'd3043820717d74d9a17694c176d39733',
  root_volume_size: int = 'd3043820717d74d9a17694c176d39733',
  security_group_ids:
    typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  tags:
    typing.List[spotinst_sdk2.models.ocean.aws.Tags] = 'd3043820717d74d9a17694c176d39733',
  use_as_template_only: bool = 'd3043820717d74d9a17694c176d39733',
  user_data: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __associate_ipv6_address__: bool
- __associate_public_ip_address__: bool
- __block_device_mappings__: List[BlockDeviceMappings]
- __ebs_optimized__: bool
- __iam_instance_profile__: IamInstanceProfile
- __image_id__: str
- __instance_metadata_options__: InstanceMetadataOptions
- __key_pair__: str
- __load_balancers__: List[LoadBalancers]
- __monitoring__: bool
- __resource_tag_specification__: ResourceTagSpecification
- __root_volume_size__: int
- __security_group_ids__: List[str]
- __tags__: List[Tags]
- __use_as_template_only__: bool
- __user_data__: str

<h2 id="spotinst_sdk2.models.ocean.aws.Compute">Compute</h2>

```python
Compute(
    self,
    subnet_ids: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
    instance_types: InstanceTypes = 'd3043820717d74d9a17694c176d39733',
    launch_specification:
    LaunchSpecifications = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __subnet_ids__: List[str]
- __instance_types__: InstanceTypes
- __launch_specification__: LaunchSpecification

<h2 id="spotinst_sdk2.models.ocean.aws.S3">S3</h2>

```python
S3(self, id: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __id__: str

<h2 id="spotinst_sdk2.models.ocean.aws.Export">Export</h2>

```python
Export(self, s3: S3 = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __s3__: S3

<h2 id="spotinst_sdk2.models.ocean.aws.Logging">Logging</h2>

```python
Logging(self, export: Export = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __export__: Export

<h2 id="spotinst_sdk2.models.ocean.aws.Ocean">Ocean</h2>

```python
Ocean(self,
      name: str = 'd3043820717d74d9a17694c176d39733',
      controller_cluster_id: str = 'd3043820717d74d9a17694c176d39733',
      region: str = 'd3043820717d74d9a17694c176d39733',
      auto_scaler: AutoScaler = 'd3043820717d74d9a17694c176d39733',
      capacity: Capacity = 'd3043820717d74d9a17694c176d39733',
      strategy: Strategy = 'd3043820717d74d9a17694c176d39733',
      scheduling: Scheduling = 'd3043820717d74d9a17694c176d39733',
      security: Security = 'd3043820717d74d9a17694c176d39733',
      compute: Compute = 'd3043820717d74d9a17694c176d39733',
      logging: Logging = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __controller_cluster_id__: str
- __region__: str
- __auto_scaler__: AutoScaler
- __capacity__: Capacity
- __strategy__: Strategy
- __scheduling__: Scheduling
- __security__: Security
- __compute__: Compute
- __logging__: Logging

<h2 id="spotinst_sdk2.models.ocean.aws.Type">Type</h2>

```python
Type(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.aws.Type.annotation">annotation</h3>


<h3 id="spotinst_sdk2.models.ocean.aws.Type.label">label</h3>


<h2 id="spotinst_sdk2.models.ocean.aws.Operator">Operator</h2>

```python
Operator(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.aws.Operator.does_not_exist">does_not_exist</h3>


<h3 id="spotinst_sdk2.models.ocean.aws.Operator.equals">equals</h3>


<h3 id="spotinst_sdk2.models.ocean.aws.Operator.exists">exists</h3>


<h3 id="spotinst_sdk2.models.ocean.aws.Operator.not_equals">not_equals</h3>


<h2 id="spotinst_sdk2.models.ocean.aws.Attribute">Attribute</h2>

```python
Attribute(self,
          type: Type = 'd3043820717d74d9a17694c176d39733',
          key: str = 'd3043820717d74d9a17694c176d39733',
          operator: Operator = 'd3043820717d74d9a17694c176d39733',
          value: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __type__: Type
- __key__: str
- __operator__: Operator
- __value__: str

<h2 id="spotinst_sdk2.models.ocean.aws.RightSizingRecommendationFilter">RightSizingRecommendationFilter</h2>

```python
RightSizingRecommendationFilter(
  self,
  namespaces: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  attribute: Attribute = 'd3043820717d74d9a17694c176d39733')
```

__Attribute__

namespaces: List[str]
attribute: Attribute

<h2 id="spotinst_sdk2.models.ocean.aws.AllMatch">AllMatch</h2>

```python
AllMatch(
    self,
    all_matches:
    typing.List[spotinst_sdk2.models.ocean.aws.Attribute] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __all_matches__:  List[Attribute]

<h2 id="spotinst_sdk2.models.ocean.aws.Conditions">Conditions</h2>

```python
Conditions(
    self,
    any_match:
    typing.List[spotinst_sdk2.models.ocean.aws.AllMatch] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __any_match__: List[AllMatch]

<h2 id="spotinst_sdk2.models.ocean.aws.Scope">Scope</h2>

```python
Scope(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.aws.Scope.namespace">namespace</h3>


<h3 id="spotinst_sdk2.models.ocean.aws.Scope.resource">resource</h3>


<h2 id="spotinst_sdk2.models.ocean.aws.Filter">Filter</h2>

```python
Filter(self,
       conditions: Conditions = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __conditions__: Conditions
- __scope__: Scope

<h2 id="spotinst_sdk2.models.ocean.aws.GroupBy">GroupBy</h2>

```python
GroupBy(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.aws.GroupBy.namespace">namespace</h3>


<h3 id="spotinst_sdk2.models.ocean.aws.GroupBy.namespace_annotation">namespace_annotation</h3>


<h3 id="spotinst_sdk2.models.ocean.aws.GroupBy.namespace_label">namespace_label</h3>


<h3 id="spotinst_sdk2.models.ocean.aws.GroupBy.resource_annotation">resource_annotation</h3>


<h3 id="spotinst_sdk2.models.ocean.aws.GroupBy.resource_label">resource_label</h3>


<h2 id="spotinst_sdk2.models.ocean.aws.AggregatedClusterCosts">AggregatedClusterCosts</h2>

```python
AggregatedClusterCosts(
  self,
  end_time: str = 'd3043820717d74d9a17694c176d39733',
  aggregated_filter: Filter = 'd3043820717d74d9a17694c176d39733',
  group_by: GroupBy = 'namespace',
  start_time: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __end_time__: str
- __aggregated_filter__: Filter
- __group_by__: GroupBy
- __start_time__: str

<h2 id="spotinst_sdk2.models.ocean.aws.Roll">Roll</h2>

```python
Roll(
  self,
  batch_min_healthy_percentage: int = 'd3043820717d74d9a17694c176d39733',
  batch_size_percentage: int = 'd3043820717d74d9a17694c176d39733',
  comment: str = 'd3043820717d74d9a17694c176d39733',
  disable_launch_spec_auto_scaling:
    bool = 'd3043820717d74d9a17694c176d39733',
  launch_spec_ids: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  instance_ids: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  respect_pdb: bool = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __batch_min_healthy_percentage__: int
- __batch_size_percentage__: int
- __comment__: str
- __disable_launch_spec_auto_scaling__: bool
- __instance_ids__: List[str]
- __launch_spec_ids__: List[str]
- __respect_pdb__: bool

<h2 id="spotinst_sdk2.models.ocean.aws.AutoScaleDown">AutoScaleDown</h2>

```python
AutoScaleDown(
  self,
  max_scale_down_percentage: float = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __max_scale_down_percentage__: double

<h2 id="spotinst_sdk2.models.ocean.aws.AutoScale">AutoScale</h2>

```python
AutoScale(
    self,
    auto_headroom_percentage: int = 'd3043820717d74d9a17694c176d39733',
    down: AutoScaleDown = 'd3043820717d74d9a17694c176d39733',
    headrooms:
    typing.List[spotinst_sdk2.models.ocean.aws.Headroom] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __auto_headroom_percentage__: int
- __down__: class(AutoScaleDown)
- __headrooms__: List[Headroom]

<h2 id="spotinst_sdk2.models.ocean.aws.TagSelector">TagSelector</h2>

```python
TagSelector(self,
            tag_key: str = 'd3043820717d74d9a17694c176d39733',
            tag_value: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __tag_key__: str
- __tag_value__: str

<h2 id="spotinst_sdk2.models.ocean.aws.ElasticIpPool">ElasticIpPool</h2>

```python
ElasticIpPool(
  self, tag_selector: TagSelector = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __tag_selector__: TagSelector

<h2 id="spotinst_sdk2.models.ocean.aws.ImageId">ImageId</h2>

```python
ImageId(self, id: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __id__: str = none

<h2 id="spotinst_sdk2.models.ocean.aws.Labels">Labels</h2>

```python
Labels(self,
       key: str = 'd3043820717d74d9a17694c176d39733',
       value: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __key__: str
- __value__: str

<h2 id="spotinst_sdk2.models.ocean.aws.VNGResourceLimits">VNGResourceLimits</h2>

```python
VNGResourceLimits(
  self,
  max_instance_count: int = 'd3043820717d74d9a17694c176d39733',
  min_instance_count: int = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __max_instance_count__: int
- __min_instance_count__: int

<h2 id="spotinst_sdk2.models.ocean.aws.Config">Config</h2>

```python
Config(
    self,
    headrooms:
    typing.List[spotinst_sdk2.models.ocean.aws.Headroom] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __headrooms__: List[Headroom]

<h2 id="spotinst_sdk2.models.ocean.aws.VNGSchedulingTaskType">VNGSchedulingTaskType</h2>

```python
VNGSchedulingTaskType(cls,
                      value,
                      names=None,
                      *,
                      module,
                      qualname,
                      type,
                      start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.aws.VNGSchedulingTaskType.manual_headroom_update">manual_headroom_update</h3>


<h2 id="spotinst_sdk2.models.ocean.aws.VNGSchedulingTasks">VNGSchedulingTasks</h2>

```python
VNGSchedulingTasks(
  self,
  cron_expression: str = 'd3043820717d74d9a17694c176d39733',
  is_enabled: bool = 'd3043820717d74d9a17694c176d39733',
  config: Config = 'd3043820717d74d9a17694c176d39733',
  task_type: VNGSchedulingTaskType = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __cron_expression__: str
- __is_enabled__: bool
- __parameters__: Parameters
- __task_type__: TaskType

<h2 id="spotinst_sdk2.models.ocean.aws.VNGSchedulingShutdownHours">VNGSchedulingShutdownHours</h2>

```python
VNGSchedulingShutdownHours(
  self,
  is_enabled: bool = 'd3043820717d74d9a17694c176d39733',
  time_windows: typing.List[str] = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __is_enabled__: bool
- __time_windows__: List[str]

<h2 id="spotinst_sdk2.models.ocean.aws.VNGScheduling">VNGScheduling</h2>

```python
VNGScheduling(
    self,
    tasks:
    typing.List[spotinst_sdk2.models.ocean.aws.VNGSchedulingTasks] = 'd3043820717d74d9a17694c176d39733',
    shutdown_hours:
    VNGSchedulingShutdownHours = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __tasks__: List[VNGSchedulingTasks]
- __shutdown_hours__: VNGSchedulingShutdownHours

<h2 id="spotinst_sdk2.models.ocean.aws.VNGStrategy">VNGStrategy</h2>

```python
VNGStrategy(self,
            spot_percentage: int = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __spot_percentage__: int

<h2 id="spotinst_sdk2.models.ocean.aws.Taints">Taints</h2>

```python
Taints(self,
       effect: str = 'd3043820717d74d9a17694c176d39733',
       key: str = 'd3043820717d74d9a17694c176d39733',
       value: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __tag_key__: str
- __tag_value__: str

<h2 id="spotinst_sdk2.models.ocean.aws.VirtualNodeGroup">VirtualNodeGroup</h2>

```python
VirtualNodeGroup(
  self,
  associate_public_ip_address: bool = 'd3043820717d74d9a17694c176d39733',
  auto_scale: AutoScale = 'd3043820717d74d9a17694c176d39733',
  block_device_mappings:
    typing.List[spotinst_sdk2.models.ocean.aws.BlockDeviceMappings] = 'd3043820717d74d9a17694c176d39733',
  elastic_ip_pool: ElasticIpPool = 'd3043820717d74d9a17694c176d39733',
  iam_instance_profile:
    IamInstanceProfile = 'd3043820717d74d9a17694c176d39733',
  image_id: str = 'd3043820717d74d9a17694c176d39733',
  images:
    typing.List[spotinst_sdk2.models.ocean.aws.ImageId] = 'd3043820717d74d9a17694c176d39733',
  instance_metadata_options:
    InstanceMetadataOptions = 'd3043820717d74d9a17694c176d39733',
  instance_types: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  instance_types_filters:
    InstanceTypesFilters = 'd3043820717d74d9a17694c176d39733',
  labels:
    typing.List[spotinst_sdk2.models.ocean.aws.Labels] = 'd3043820717d74d9a17694c176d39733',
  name: str = 'd3043820717d74d9a17694c176d39733',
  ocean_id: str = 'd3043820717d74d9a17694c176d39733',
  preferred_spot_types:
    typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  resource_limits: VNGResourceLimits = 'd3043820717d74d9a17694c176d39733',
  restrict_scale_down: bool = 'd3043820717d74d9a17694c176d39733',
  root_volume_size: int = 'd3043820717d74d9a17694c176d39733',
  scheduling: VNGScheduling = 'd3043820717d74d9a17694c176d39733',
  strategy: VNGStrategy = 'd3043820717d74d9a17694c176d39733',
  security_group_ids:
    typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  subnet_ids: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  tags:
    typing.List[spotinst_sdk2.models.ocean.aws.Tags] = 'd3043820717d74d9a17694c176d39733',
  taints:
    typing.List[spotinst_sdk2.models.ocean.aws.Taints] = 'd3043820717d74d9a17694c176d39733',
  user_data: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __associate_public_ip_address__: bool
- __auto_scale__: AutoScale
- __block_device_mappings__: List[BlockDeviceMappings]
- __elastic_ip_pool__: ElasticIpPool
- __iam_instance_profile__: IamInstanceProfile
- __image_id__: str
- __images__: List[ImageId]
- __instance_metadata_options__: InstanceMetadataOptions
- __instance_types __: List[str]
- __instance_types_filters__: InstanceTypesFilters
- __labels__: List[Labels]
- __name__: str
- __ocean_id__: str
- __preferred_spot_types__: List[str]
- __resource_limits__: VNGResourceLimits
- __restrict_scale_down__: bool
- __root_volume_size__: int
- __scheduling__: VNGScheduling
- __strategy__: VNGStrategy
- __security_group_ids__: List[str]
- __subnet_ids__: List[str]
- __taints__: List[Taints]
- __user_data__: str

<h2 id="spotinst_sdk2.models.ocean.aws.Migration">Migration</h2>

```python
Migration(
  self,
  batch_size_percentage: int = 'd3043820717d74d9a17694c176d39733',
  force_pod_eviction_on_pdb_failure:
    bool = 'd3043820717d74d9a17694c176d39733',
  instance_ids: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  should_evict_stand_alone_pods:
    bool = 'd3043820717d74d9a17694c176d39733',
  should_terminate_drained_nodes:
    bool = 'd3043820717d74d9a17694c176d39733',
  state: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __batch_size_percentage__: int
- __force_pod_eviction_on_pdb_failure__: bool
- __instance_ids__: List[str]
- __should_evict_stand_alone_pods__: bool
- __should_terminate_drained_nodes__: bool
- __state__: str

<h2 id="spotinst_sdk2.models.ocean.aws.DetachInstances">DetachInstances</h2>

```python
DetachInstances(
  self,
  instances_to_detach:
    typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  should_decrement_target_capacity:
    bool = 'd3043820717d74d9a17694c176d39733',
  should_terminate_instances: bool = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __instances_to_detach__: List[str]
- __should_decrement_target_capacity__: bool
- __should_terminate_instances__: bool

<h2 id="spotinst_sdk2.models.ocean.aws.ImportASGToOceanCluster">ImportASGToOceanCluster</h2>

```python
ImportASGToOceanCluster(
  self,
  instance_types: typing.List[str] = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __instance_types__: List[str]

<h2 id="spotinst_sdk2.models.ocean.aws.ImportASGToOceanVNG">ImportASGToOceanVNG</h2>

```python
ImportASGToOceanVNG(
    self,
    name: str = 'd3043820717d74d9a17694c176d39733',
    labels:
    typing.List[spotinst_sdk2.models.ocean.aws.Labels] = 'd3043820717d74d9a17694c176d39733',
    taints:
    typing.List[spotinst_sdk2.models.ocean.aws.Taints] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __labels__: List[Labels]
- __name__: str
- __taints__: List[Taints]

<h2 id="spotinst_sdk2.models.ocean.aws.ImportEKSNodeGroupToOceanVNG">ImportEKSNodeGroupToOceanVNG</h2>

```python
ImportEKSNodeGroupToOceanVNG(
    self,
    name: str = 'd3043820717d74d9a17694c176d39733',
    labels:
    typing.List[spotinst_sdk2.models.ocean.aws.Labels] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __labels__: List[Labels]
- __name__: str

<h2 id="spotinst_sdk2.models.ocean.aws.ExtendedResourceDefinition">ExtendedResourceDefinition</h2>

```python
ExtendedResourceDefinition(
  self,
  mapping: dict = 'd3043820717d74d9a17694c176d39733',
  name: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __mapping__: dict
- __name__: str

