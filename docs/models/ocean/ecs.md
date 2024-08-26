<h1 id="spotinst_sdk2.models.ocean.ecs">spotinst_sdk2.models.ocean.ecs</h1>


<h2 id="spotinst_sdk2.models.ocean.ecs.Down">Down</h2>

```python
Down(
  self,
  evaluation_periods: int = 'd3043820717d74d9a17694c176d39733',
  max_scale_down_percentage: int = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __evaluation_periods__: int
- __max_scale_down_percentage__: int

<h2 id="spotinst_sdk2.models.ocean.ecs.Headroom">Headroom</h2>

```python
Headroom(self,
         cpu_per_unit: int = 'd3043820717d74d9a17694c176d39733',
         memory_per_unit: int = 'd3043820717d74d9a17694c176d39733',
         num_of_units: int = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __cpu_per_unit__: int
- __memory_per_unit__: int
- __num_of_units__: int

<h2 id="spotinst_sdk2.models.ocean.ecs.ResourceLimits">ResourceLimits</h2>

```python
ResourceLimits(self,
               max_memory_gib: int = 'd3043820717d74d9a17694c176d39733',
               max_v_cpu: int = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __max_memory_gib__: int
- __max_v_cpu__: int

<h2 id="spotinst_sdk2.models.ocean.ecs.AutoScaler">AutoScaler</h2>

```python
AutoScaler(
    self,
    auto_headroom_percentage: int = 'd3043820717d74d9a17694c176d39733',
    cooldown: int = 'd3043820717d74d9a17694c176d39733',
    down: Down = 'd3043820717d74d9a17694c176d39733',
    enable_automatic_and_manual_headroom:
    bool = 'd3043820717d74d9a17694c176d39733',
    headroom: Headroom = 'd3043820717d74d9a17694c176d39733',
    is_auto_config: bool = 'd3043820717d74d9a17694c176d39733',
    is_enabled: bool = 'd3043820717d74d9a17694c176d39733',
    resource_limits: ResourceLimits = 'd3043820717d74d9a17694c176d39733',
    should_scale_down_non_service_tasks:
    bool = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __auto_headroom_percentage__: int
- __cooldown__: int
- __down__: Down
- __enable_automatic_and_manual_headroom__: bool
- __headroom__: Headroom
- __is_auto_config__: bool
- __is_enabled__: bool
- __resource_limits__: ResourceLimits
- __should_scale_down_non_service_tasks__: bool

<h2 id="spotinst_sdk2.models.ocean.ecs.Capacity">Capacity</h2>

```python
Capacity(self,
         maximum: int = 'd3043820717d74d9a17694c176d39733',
         minimum: int = 'd3043820717d74d9a17694c176d39733',
         target: int = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __maximum__: int
- __minimum__: int
- __target__: int

<h2 id="spotinst_sdk2.models.ocean.ecs.Architecture">Architecture</h2>

```python
Architecture(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.ecs.Architecture.arm64">arm64</h3>


<h3 id="spotinst_sdk2.models.ocean.ecs.Architecture.i386">i386</h3>


<h3 id="spotinst_sdk2.models.ocean.ecs.Architecture.x86_64">x86_64</h3>


<h2 id="spotinst_sdk2.models.ocean.ecs.Category">Category</h2>

```python
Category(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.ecs.Category.accelerated_computing">accelerated_computing</h3>


<h3 id="spotinst_sdk2.models.ocean.ecs.Category.compute_optimized">compute_optimized</h3>


<h3 id="spotinst_sdk2.models.ocean.ecs.Category.general_purpose">general_purpose</h3>


<h3 id="spotinst_sdk2.models.ocean.ecs.Category.memory_optimized">memory_optimized</h3>


<h3 id="spotinst_sdk2.models.ocean.ecs.Category.storage_optimized">storage_optimized</h3>


<h2 id="spotinst_sdk2.models.ocean.ecs.DiskType">DiskType</h2>

```python
DiskType(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.ecs.DiskType.ebs">ebs</h3>


<h3 id="spotinst_sdk2.models.ocean.ecs.DiskType.hdd">hdd</h3>


<h3 id="spotinst_sdk2.models.ocean.ecs.DiskType.nvme">nvme</h3>


<h3 id="spotinst_sdk2.models.ocean.ecs.DiskType.ssd">ssd</h3>


<h2 id="spotinst_sdk2.models.ocean.ecs.Hypervisor">Hypervisor</h2>

```python
Hypervisor(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.ecs.Hypervisor.nitro">nitro</h3>


<h3 id="spotinst_sdk2.models.ocean.ecs.Hypervisor.xen">xen</h3>


<h2 id="spotinst_sdk2.models.ocean.ecs.RootDeviceType">RootDeviceType</h2>

```python
RootDeviceType(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.ecs.RootDeviceType.ebs">ebs</h3>


<h3 id="spotinst_sdk2.models.ocean.ecs.RootDeviceType.instance_store">instance_store</h3>


<h2 id="spotinst_sdk2.models.ocean.ecs.VirtualizationType">VirtualizationType</h2>

```python
VirtualizationType(cls,
                   value,
                   names=None,
                   *,
                   module,
                   qualname,
                   type,
                   start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.ecs.VirtualizationType.hvm">hvm</h3>


<h3 id="spotinst_sdk2.models.ocean.ecs.VirtualizationType.paravirtual">paravirtual</h3>


<h2 id="spotinst_sdk2.models.ocean.ecs.InstanceTypesFilters">InstanceTypesFilters</h2>

```python
InstanceTypesFilters(
  self,
  min_vcpu: int = 'd3043820717d74d9a17694c176d39733',
  max_vcpu: int = 'd3043820717d74d9a17694c176d39733',
  min_memory_gi_b: float = 'd3043820717d74d9a17694c176d39733',
  max_memory_gi_b: float = 'd3043820717d74d9a17694c176d39733',
  min_gpu: int = 'd3043820717d74d9a17694c176d39733',
  max_gpu: int = 'd3043820717d74d9a17694c176d39733',
  include_families: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  exclude_families: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  exclude_metal: bool = 'd3043820717d74d9a17694c176d39733',
  is_ena_supported: bool = 'd3043820717d74d9a17694c176d39733',
  architectures:
    typing.List[spotinst_sdk2.models.ocean.ecs.Architecture] = 'd3043820717d74d9a17694c176d39733',
  virtualization_types:
    typing.List[spotinst_sdk2.models.ocean.ecs.VirtualizationType] = 'd3043820717d74d9a17694c176d39733',
  categories:
    typing.List[spotinst_sdk2.models.ocean.ecs.Category] = 'd3043820717d74d9a17694c176d39733',
  min_enis: int = 'd3043820717d74d9a17694c176d39733',
  disk_types:
    typing.List[spotinst_sdk2.models.ocean.ecs.DiskType] = 'd3043820717d74d9a17694c176d39733',
  hypervisor:
    typing.List[spotinst_sdk2.models.ocean.ecs.Hypervisor] = 'd3043820717d74d9a17694c176d39733',
  root_device_types:
    typing.List[spotinst_sdk2.models.ocean.ecs.RootDeviceType] = 'd3043820717d74d9a17694c176d39733',
  min_network_performance: int = 'd3043820717d74d9a17694c176d39733',
  max_network_performance: int = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __min_vcpu__: int
- __max_vcpu__: int
- __min_memory_gi_b__: float
- __max_memory_gi_b__: float
- __min_gpu__: int
- __max_gpu__: int
- __include_families__: List[str]
- __exclude_families__: List[str]
- __exclude_metal__: bool
- __is_ena_supported__: bool
- __architectures__: List[Architecture]
- __virtualization_types__: List[VirtualizationType]
- __categories__: List[Category]
- __min_enis__: int
- __disk_types__: List[DiskType]
- __hypervisor__: List[Hypervisor]
- __root_device_types__: List[RootDeviceType]
- __min_network_performance__: int
- __max_network_performance__: int

<h2 id="spotinst_sdk2.models.ocean.ecs.InstanceTypes">InstanceTypes</h2>

```python
InstanceTypes(
  self,
  blacklist: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  filters: InstanceTypesFilters = 'd3043820717d74d9a17694c176d39733',
  whitelist: typing.List[str] = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __blacklist__: List[str]
- __filters__: InstanceTypesFilters
- __whitelist__: List[str]

<h2 id="spotinst_sdk2.models.ocean.ecs.DynamicVolumeSize">DynamicVolumeSize</h2>

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

<h2 id="spotinst_sdk2.models.ocean.ecs.EBS">EBS</h2>

```python
EBS(self,
    delete_on_termination: bool = 'd3043820717d74d9a17694c176d39733',
    dynamic_volume_size:
    DynamicVolumeSize = 'd3043820717d74d9a17694c176d39733',
    encrypted: bool = 'd3043820717d74d9a17694c176d39733',
    iops: int = 'd3043820717d74d9a17694c176d39733',
    kms_key_id: str = 'd3043820717d74d9a17694c176d39733',
    snapshot_id: str = 'd3043820717d74d9a17694c176d39733',
    throughput: int = 'd3043820717d74d9a17694c176d39733',
    volume_size: int = 'd3043820717d74d9a17694c176d39733',
    volume_type: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __delete_on_termination__: bool
- __dynamic_volume_size__: DynamicVolumeSize
- __encrypted__: bool
- __iops__: int
- __kms_key_id__: str
- __snapshot_id__: str
- __throughput__: int
- __volume_size__: int
- __volume_type__: str

<h2 id="spotinst_sdk2.models.ocean.ecs.BlockDeviceMapping">BlockDeviceMapping</h2>

```python
BlockDeviceMapping(self,
                   device_name: str = 'd3043820717d74d9a17694c176d39733',
                   ebs: EBS = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __device_name__: str
- __ebs__: EBS

<h2 id="spotinst_sdk2.models.ocean.ecs.IamInstanceProfile">IamInstanceProfile</h2>

```python
IamInstanceProfile(self, arn: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __arn__: str

<h2 id="spotinst_sdk2.models.ocean.ecs.HttpEndpoint">HttpEndpoint</h2>

```python
HttpEndpoint(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.ecs.HttpEndpoint.disabled">disabled</h3>


<h3 id="spotinst_sdk2.models.ocean.ecs.HttpEndpoint.enabled">enabled</h3>


<h2 id="spotinst_sdk2.models.ocean.ecs.HttpTokens">HttpTokens</h2>

```python
HttpTokens(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.ecs.HttpTokens.optional">optional</h3>


<h3 id="spotinst_sdk2.models.ocean.ecs.HttpTokens.required">required</h3>


<h2 id="spotinst_sdk2.models.ocean.ecs.InstanceMetadataOptions">InstanceMetadataOptions</h2>

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

<h2 id="spotinst_sdk2.models.ocean.ecs.Tag">Tag</h2>

```python
Tag(self,
    tag_key: str = 'd3043820717d74d9a17694c176d39733',
    tag_value: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __tag_key__: str
- __tag_value__: str

<h2 id="spotinst_sdk2.models.ocean.ecs.LaunchSpecification">LaunchSpecification</h2>

```python
LaunchSpecification(
  self,
  associate_ipv6_address: bool = 'd3043820717d74d9a17694c176d39733',
  associate_public_ip_address: bool = 'd3043820717d74d9a17694c176d39733',
  block_device_mappings:
    typing.List[spotinst_sdk2.models.ocean.ecs.BlockDeviceMapping] = 'd3043820717d74d9a17694c176d39733',
  ebs_optimized: bool = 'd3043820717d74d9a17694c176d39733',
  iam_instance_profile:
    IamInstanceProfile = 'd3043820717d74d9a17694c176d39733',
  image_id: str = 'd3043820717d74d9a17694c176d39733',
  instance_metadata_options:
    InstanceMetadataOptions = 'd3043820717d74d9a17694c176d39733',
  monitoring: bool = 'd3043820717d74d9a17694c176d39733',
  security_group_ids:
    typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  tags:
    typing.List[spotinst_sdk2.models.ocean.ecs.Tag] = 'd3043820717d74d9a17694c176d39733',
  use_as_template_only: bool = 'd3043820717d74d9a17694c176d39733',
  user_data: str = 'd3043820717d74d9a17694c176d39733',
  key_pair: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __associate_ipv6_address__: bool
- __associate_public_ip_address__: bool
- __block_device_mappings__: List[BlockDeviceMapping]
- __ebs_optimized__: bool
- __iam_instance_profile__: IamInstanceProfile
- __image_id__: str
- __instance_metadata_options__: InstanceMetadataOptions
- __monitoring__: bool
- __security_group_ids__: List[str]
- __tags__: List[Tag]
- __use_as_template_only__: bool
- __user_data__: str
- __key_pair__: str

<h2 id="spotinst_sdk2.models.ocean.ecs.OptimizeImages">OptimizeImages</h2>

```python
OptimizeImages(
  self,
  perform_at: str = 'd3043820717d74d9a17694c176d39733',
  should_optimize_ecs_ami: bool = 'd3043820717d74d9a17694c176d39733',
  time_windows: typing.List[str] = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __perform_at__: str
- __should_optimize_ecs_ami__: bool
- __time_windows__: List[str]

<h2 id="spotinst_sdk2.models.ocean.ecs.Compute">Compute</h2>

```python
Compute(
  self,
  instance_types: InstanceTypes = 'd3043820717d74d9a17694c176d39733',
  launch_specification:
    LaunchSpecification = 'd3043820717d74d9a17694c176d39733',
  optimize_images: OptimizeImages = 'd3043820717d74d9a17694c176d39733',
  subnet_ids: typing.List[str] = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __instance_types__: InstanceTypes
- __launch_specification__: LaunchSpecification
- __optimize_images__: OptimizeImages
- __subnet_ids__: List[str]

<h2 id="spotinst_sdk2.models.ocean.ecs.S3Bucket">S3Bucket</h2>

```python
S3Bucket(self, id: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __id__: str

<h2 id="spotinst_sdk2.models.ocean.ecs.LoggingConfiguration">LoggingConfiguration</h2>

```python
LoggingConfiguration(self,
                     s3: S3Bucket = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __s3__: S3Bucket

<h2 id="spotinst_sdk2.models.ocean.ecs.Logging">Logging</h2>

```python
Logging(
  self,
  export: LoggingConfiguration = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __export__: LoggingConfiguration

<h2 id="spotinst_sdk2.models.ocean.ecs.ShutdownHours">ShutdownHours</h2>

```python
ShutdownHours(
  self,
  is_enabled: bool = 'd3043820717d74d9a17694c176d39733',
  time_windows: typing.List[str] = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __is_enabled__: bool
- __time_windows__: List[str]

<h2 id="spotinst_sdk2.models.ocean.ecs.ClusterRoll">ClusterRoll</h2>

```python
ClusterRoll(
  self,
  batch_min_healthy_percentage: int = 'd3043820717d74d9a17694c176d39733',
  batch_size_percentage: int = 'd3043820717d74d9a17694c176d39733',
  comment: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __batch_min_healthy_percentage__: int
- __batch_size_percentage__: int
- __comment__: str

<h2 id="spotinst_sdk2.models.ocean.ecs.Parameters">Parameters</h2>

```python
Parameters(self,
           cluster_roll: ClusterRoll = 'd3043820717d74d9a17694c176d39733'
           )
```

__Arguments__

- __cluster_roll__: ClusterRoll

<h2 id="spotinst_sdk2.models.ocean.ecs.SchedulingTask">SchedulingTask</h2>

```python
SchedulingTask(
  self,
  cron_expression: str = 'd3043820717d74d9a17694c176d39733',
  is_enabled: bool = 'd3043820717d74d9a17694c176d39733',
  parameters: Parameters = 'd3043820717d74d9a17694c176d39733',
  task_type: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __cron_expression__: str
- __is_enabled__: bool
- __parameters__: Parameters
- __task_type__: str

<h2 id="spotinst_sdk2.models.ocean.ecs.Scheduling">Scheduling</h2>

```python
Scheduling(
    self,
    shutdown_hours: ShutdownHours = 'd3043820717d74d9a17694c176d39733',
    tasks:
    typing.List[spotinst_sdk2.models.ocean.ecs.SchedulingTask] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __shutdown_hours__: ShutdownHours
- __tasks__: List[SchedulingTask]

<h2 id="spotinst_sdk2.models.ocean.ecs.AvailabilityVsCost">AvailabilityVsCost</h2>

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
<h3 id="spotinst_sdk2.models.ocean.ecs.AvailabilityVsCost.balanced">balanced</h3>


<h3 id="spotinst_sdk2.models.ocean.ecs.AvailabilityVsCost.cheapest">cheapest</h3>


<h3 id="spotinst_sdk2.models.ocean.ecs.AvailabilityVsCost.cost_oriented">cost_oriented</h3>


<h2 id="spotinst_sdk2.models.ocean.ecs.ClusterOrientation">ClusterOrientation</h2>

```python
ClusterOrientation(
    self,
    availability_vs_cost:
    AvailabilityVsCost = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __availability_vs_cost__: AvailabilityVsCost

<h2 id="spotinst_sdk2.models.ocean.ecs.Strategy">Strategy</h2>

```python
Strategy(
  self,
  cluster_orientation:
    ClusterOrientation = 'd3043820717d74d9a17694c176d39733',
  draining_timeout: int = 'd3043820717d74d9a17694c176d39733',
  fallback_to_od: bool = 'd3043820717d74d9a17694c176d39733',
  spot_percentage: int = 'd3043820717d74d9a17694c176d39733',
  utilize_commitments: bool = 'd3043820717d74d9a17694c176d39733',
  utilize_reserved_instances: bool = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __cluster_orientation__: ClusterOrientation
- __draining_timeout__: int
- __fallback_to_od__: bool
- __spot_percentage__: int
- __utilize_commitments__: bool
- __utilize_reserved_instances__: bool

<h2 id="spotinst_sdk2.models.ocean.ecs.Ocean">Ocean</h2>

```python
Ocean(self,
      auto_scaler: AutoScaler = 'd3043820717d74d9a17694c176d39733',
      capacity: Capacity = 'd3043820717d74d9a17694c176d39733',
      cluster_name: str = 'd3043820717d74d9a17694c176d39733',
      compute: Compute = 'd3043820717d74d9a17694c176d39733',
      logging: Logging = 'd3043820717d74d9a17694c176d39733',
      name: str = 'd3043820717d74d9a17694c176d39733',
      region: str = 'd3043820717d74d9a17694c176d39733',
      scheduling: Scheduling = 'd3043820717d74d9a17694c176d39733',
      strategy: Strategy = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __auto_scaler__: AutoScaler
- __capacity__: Capacity
- __cluster_name__: str
- __compute__: Compute
- __logging__: Logging
- __name__: str
- __region__: str
- __scheduling__: Scheduling
- __strategy__: Strategy

<h2 id="spotinst_sdk2.models.ocean.ecs.ImportClusterConfig">ImportClusterConfig</h2>

```python
ImportClusterConfig(
  self,
  instance_id: str = 'd3043820717d74d9a17694c176d39733',
  name: str = 'd3043820717d74d9a17694c176d39733',
  region: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __instance_id__: str
- __name__: str
- __region__: str

<h2 id="spotinst_sdk2.models.ocean.ecs.RollConfig">RollConfig</h2>

```python
RollConfig(
  self,
  batch_min_healthy_percentage: int = 'd3043820717d74d9a17694c176d39733',
  batch_size_percentage: int = 'd3043820717d74d9a17694c176d39733',
  comment: str = 'd3043820717d74d9a17694c176d39733',
  launch_spec_ids: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  instance_ids: typing.List[str] = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __batch_min_healthy_percentage__: int
- __batch_size_percentage__: int
- __comment__: str
- __instance_ids__: List[str]
- __launch_spec_ids__: List[str]

<h2 id="spotinst_sdk2.models.ocean.ecs.DetachInstancesConfig">DetachInstancesConfig</h2>

```python
DetachInstancesConfig(
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

<h2 id="spotinst_sdk2.models.ocean.ecs.Attribute">Attribute</h2>

```python
Attribute(self,
          key: str = 'd3043820717d74d9a17694c176d39733',
          value: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __key__: str
- __value__: str

<h2 id="spotinst_sdk2.models.ocean.ecs.AutoScale">AutoScale</h2>

```python
AutoScale(
    self,
    headrooms:
    typing.List[spotinst_sdk2.models.ocean.ecs.Headroom] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __headrooms__: List[Headrooms]

<h2 id="spotinst_sdk2.models.ocean.ecs.Image">Image</h2>

```python
Image(self, id: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __id__: str

<h2 id="spotinst_sdk2.models.ocean.ecs.VngTask">VngTask</h2>

```python
VngTask(
  self,
  config:
    typing.List[spotinst_sdk2.models.ocean.ecs.Headroom] = 'd3043820717d74d9a17694c176d39733',
  cron_expression: str = 'd3043820717d74d9a17694c176d39733',
  is_enabled: bool = 'd3043820717d74d9a17694c176d39733',
  task_type: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __config__: List[Headroom]
- __cron_expression__: str
- __is_enabled__: bool
- __task_type__: str

<h2 id="spotinst_sdk2.models.ocean.ecs.VngScheduling">VngScheduling</h2>

```python
VngScheduling(
  self, tasks: typing.List[spotinst_sdk2.models.ocean.ecs.VngTask])
```

__Arguments__

- __tasks__: List[VngTask]

<h2 id="spotinst_sdk2.models.ocean.ecs.VirtualNodeGroup">VirtualNodeGroup</h2>

```python
VirtualNodeGroup(
  self,
  attributes:
    typing.List[spotinst_sdk2.models.ocean.ecs.Attribute] = 'd3043820717d74d9a17694c176d39733',
  auto_scale: AutoScale = 'd3043820717d74d9a17694c176d39733',
  block_device_mappings:
    typing.List[spotinst_sdk2.models.ocean.ecs.BlockDeviceMapping] = 'd3043820717d74d9a17694c176d39733',
  iam_instance_profile:
    IamInstanceProfile = 'd3043820717d74d9a17694c176d39733',
  image_id: str = 'd3043820717d74d9a17694c176d39733',
  images:
    typing.List[spotinst_sdk2.models.ocean.ecs.Image] = 'd3043820717d74d9a17694c176d39733',
  instance_metadata_options:
    InstanceMetadataOptions = 'd3043820717d74d9a17694c176d39733',
  instance_types: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  name: str = 'd3043820717d74d9a17694c176d39733',
  ocean_id: str = 'd3043820717d74d9a17694c176d39733',
  preferred_spot_types:
    typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  restrict_scale_down: bool = 'd3043820717d74d9a17694c176d39733',
  scheduling: VngScheduling = 'd3043820717d74d9a17694c176d39733',
  security_group_ids:
    typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  strategy: Strategy = 'd3043820717d74d9a17694c176d39733',
  subnet_ids: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  tags:
    typing.List[spotinst_sdk2.models.ocean.ecs.Tag] = 'd3043820717d74d9a17694c176d39733',
  user_data: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __attributes__: List[Attribute]
- __auto_scale__: AutoScale
- __block_device_mappings__: List[BlockDeviceMapping]
- __iam_instance_profile__: IamInstanceProfile
- __image_id__: str
- __images__: List[Image]
- __instance_metadata_options__: InstanceMetadataOptions
- __instance_types__: List[str]
- __name__: str
- __ocean_id__: str
- __preferred_spot_types__: List[str]
- __restrict_scale_down__: bool
- __scheduling__: VngScheduling
- __security_group_ids__: List[str]
- __strategy__: Strategy
- __subnet_ids__: List[str]
- __tags__: List[Tag]
- __user_data__: str

<h2 id="spotinst_sdk2.models.ocean.ecs.ImportFargateToExistingOceanCluster">ImportFargateToExistingOceanCluster</h2>

```python
ImportFargateToExistingOceanCluster(
  self,
  services: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  simple_new_service_names: bool = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __services__: List[str]
- __simple_new_service_names__: bool

<h2 id="spotinst_sdk2.models.ocean.ecs.ImportFargateToNewOceanCluster">ImportFargateToNewOceanCluster</h2>

```python
ImportFargateToNewOceanCluster(
    self,
    ecs_cluster_name: str = 'd3043820717d74d9a17694c176d39733',
    key_pair: str = 'd3043820717d74d9a17694c176d39733',
    ocean_cluster_name: str = 'd3043820717d74d9a17694c176d39733',
    region: str = 'd3043820717d74d9a17694c176d39733',
    services: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
    tags:
    typing.List[spotinst_sdk2.models.ocean.ecs.Tag] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __ecs_cluster_name__: str
- __key_pair__: str
- __ocean_cluster_name__: str
- __region__: str
- __services__: List[str]
- __tags__: List[Tag]

