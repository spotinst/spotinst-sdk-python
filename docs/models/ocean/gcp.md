<h1 id="spotinst_sdk2.models.ocean.gcp">spotinst_sdk2.models.ocean.gcp</h1>


<h2 id="spotinst_sdk2.models.ocean.gcp.AggressiveScaleDown">AggressiveScaleDown</h2>

```python
AggressiveScaleDown(self,
                    is_enabled: bool = 'd3043820717d74d9a17694c176d39733'
                    )
```

__Arguments__

- __is_enabled__: bool

<h2 id="spotinst_sdk2.models.ocean.gcp.Down">Down</h2>

```python
Down(self,
     evaluation_periods: int = 'd3043820717d74d9a17694c176d39733',
     max_scale_down_percentage: int = 'd3043820717d74d9a17694c176d39733',
     aggressive_scale_down:
     AggressiveScaleDown = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __evaluation_periods__: int
- __max_scale_down_percentage__: int
- __aggressive_scale_down__: AggressiveScaleDown

<h2 id="spotinst_sdk2.models.ocean.gcp.Headroom">Headroom</h2>

```python
Headroom(self,
         cpu_per_unit: int = 'd3043820717d74d9a17694c176d39733',
         gpu_per_unit: int = 'd3043820717d74d9a17694c176d39733',
         memory_per_unit: int = 'd3043820717d74d9a17694c176d39733',
         num_of_units: int = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __cpu_per_unit__: int
- __gpu_per_unit__: int
- __memory_per_unit__: int
- __num_of_units__: int

<h2 id="spotinst_sdk2.models.ocean.gcp.ResourceLimits">ResourceLimits</h2>

```python
ResourceLimits(self,
               max_memory_gib: int = 'd3043820717d74d9a17694c176d39733',
               max_v_cpu: int = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __max_memory_gib__: int
- __max_v_cpu__: int

<h2 id="spotinst_sdk2.models.ocean.gcp.AutoScaler">AutoScaler</h2>

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
  resource_limits: ResourceLimits = 'd3043820717d74d9a17694c176d39733')
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

<h2 id="spotinst_sdk2.models.ocean.gcp.Capacity">Capacity</h2>

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

<h2 id="spotinst_sdk2.models.ocean.gcp.LocationType">LocationType</h2>

```python
LocationType(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.gcp.LocationType.regional">regional</h3>


<h2 id="spotinst_sdk2.models.ocean.gcp.NamedPorts">NamedPorts</h2>

```python
NamedPorts(self,
           name: str = 'd3043820717d74d9a17694c176d39733',
           ports: typing.List[int] = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __ports__: List[int]

<h2 id="spotinst_sdk2.models.ocean.gcp.Scheme">Scheme</h2>

```python
Scheme(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.gcp.Scheme.external">external</h3>


<h3 id="spotinst_sdk2.models.ocean.gcp.Scheme.internal">internal</h3>


<h2 id="spotinst_sdk2.models.ocean.gcp.BackendServices">BackendServices</h2>

```python
BackendServices(
  self,
  backend_service_name: str = 'd3043820717d74d9a17694c176d39733',
  location_type: LocationType = 'd3043820717d74d9a17694c176d39733',
  named_ports: NamedPorts = 'd3043820717d74d9a17694c176d39733',
  scheme: Scheme = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __backend_service_name__: str
- __location_type__: LocationType
- __named_ports__: NamedPorts
- __scheme__: Scheme

<h2 id="spotinst_sdk2.models.ocean.gcp.InstanceTypes">InstanceTypes</h2>

```python
InstanceTypes(
  self,
  blacklist: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  whitelist: typing.List[str] = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __blacklist__: List[str]
- __whitelist__: List[str]

<h2 id="spotinst_sdk2.models.ocean.gcp.Labels">Labels</h2>

```python
Labels(self,
       key: str = 'd3043820717d74d9a17694c176d39733',
       value: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __key__: str
- __value__: str

<h2 id="spotinst_sdk2.models.ocean.gcp.Metadata">Metadata</h2>

```python
Metadata(self,
         key: str = 'd3043820717d74d9a17694c176d39733',
         value: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __key__: str
- __value__: str

<h2 id="spotinst_sdk2.models.ocean.gcp.RootVolumeType">RootVolumeType</h2>

```python
RootVolumeType(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.gcp.RootVolumeType.pd_ssd">pd_ssd</h3>


<h3 id="spotinst_sdk2.models.ocean.gcp.RootVolumeType.pd_standard">pd_standard</h3>


<h2 id="spotinst_sdk2.models.ocean.gcp.ShieldedInstanceConfig">ShieldedInstanceConfig</h2>

```python
ShieldedInstanceConfig(
  self,
  enable_integrity_monitoring: bool = 'd3043820717d74d9a17694c176d39733',
  enable_secure_boot: bool = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __enable_integrity_monitoring__: bool
- __enable_secure_boot__: bool

<h2 id="spotinst_sdk2.models.ocean.gcp.LaunchSpecification">LaunchSpecification</h2>

```python
LaunchSpecification(
  self,
  ip_forwarding: bool = 'd3043820717d74d9a17694c176d39733',
  labels:
    typing.List[spotinst_sdk2.models.ocean.gcp.Labels] = 'd3043820717d74d9a17694c176d39733',
  metadata:
    typing.List[spotinst_sdk2.models.ocean.gcp.Metadata] = 'd3043820717d74d9a17694c176d39733',
  min_cpu_platform: str = 'd3043820717d74d9a17694c176d39733',
  root_volume_size_in_gb: int = 'd3043820717d74d9a17694c176d39733',
  root_volume_type: RootVolumeType = 'd3043820717d74d9a17694c176d39733',
  service_account: str = 'd3043820717d74d9a17694c176d39733',
  shielded_instance_config:
    ShieldedInstanceConfig = 'd3043820717d74d9a17694c176d39733',
  source_image: str = 'd3043820717d74d9a17694c176d39733',
  tags: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  use_as_template_only: bool = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __ip_forwarding__: bool
- __labels__: List[Labels]
- __metadata__: List[Metadata]
- __min_cpu_platform__: str
- __root_volume_size_in_gb__: int
- __root_volume_type__: RootVolumeType
- __service_account__: str
- __shielded_instance_config__: ShieldedInstanceConfig
- __source_image__: str
- __tags__: List[str]
- __use_as_template_only__: bool

<h2 id="spotinst_sdk2.models.ocean.gcp.AccessConfigs">AccessConfigs</h2>

```python
AccessConfigs(self,
              name: str = 'd3043820717d74d9a17694c176d39733',
              type: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __type__: str

<h2 id="spotinst_sdk2.models.ocean.gcp.AliasIpRanges">AliasIpRanges</h2>

```python
AliasIpRanges(
  self,
  ip_cidr_range: str = 'd3043820717d74d9a17694c176d39733',
  subnetwork_range_name: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __ip_cidr_range__: str
- __subnetwork_range_name__: str

<h2 id="spotinst_sdk2.models.ocean.gcp.NetworkInterfaces">NetworkInterfaces</h2>

```python
NetworkInterfaces(
  self,
  access_configs:
    typing.List[spotinst_sdk2.models.ocean.gcp.AccessConfigs] = 'd3043820717d74d9a17694c176d39733',
  alias_ip_ranges:
    typing.List[spotinst_sdk2.models.ocean.gcp.AliasIpRanges] = 'd3043820717d74d9a17694c176d39733',
  network: str = 'd3043820717d74d9a17694c176d39733',
  project_id: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __access_configs__: List[AccessConfigs]
- __alias_ip_ranges__: List[AliasIpRanges]
- __network__: str
- __project_id__: str

<h2 id="spotinst_sdk2.models.ocean.gcp.Compute">Compute</h2>

```python
Compute(
  self,
  availability_zones:
    typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  backend_services: BackendServices = 'd3043820717d74d9a17694c176d39733',
  instance_types: InstanceTypes = 'd3043820717d74d9a17694c176d39733',
  launch_specification:
    LaunchSpecification = 'd3043820717d74d9a17694c176d39733',
  network_interfaces:
    typing.List[spotinst_sdk2.models.ocean.gcp.NetworkInterfaces] = 'd3043820717d74d9a17694c176d39733',
  subnet_name: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __availability_zones__: List[str]
- __backend_services__: BackendServices
- __instance_types__: InstanceTypes
- __launch_specification__: LaunchSpecification
- __network_interfaces__: List[NetworkInterfaces]
- __subnet_name__: str

<h2 id="spotinst_sdk2.models.ocean.gcp.GKE">GKE</h2>

```python
GKE(self,
    cluster_name: str = 'd3043820717d74d9a17694c176d39733',
    master_location: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __cluster_name__: str
- __master_location__: str

<h2 id="spotinst_sdk2.models.ocean.gcp.ShutdownHours">ShutdownHours</h2>

```python
ShutdownHours(
  self,
  is_enabled: bool = 'd3043820717d74d9a17694c176d39733',
  time_windows: typing.List[str] = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __is_enabled__: bool
- __time_windows__: List[str]

<h2 id="spotinst_sdk2.models.ocean.gcp.ClusterRoll">ClusterRoll</h2>

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

<h2 id="spotinst_sdk2.models.ocean.gcp.Parameters">Parameters</h2>

```python
Parameters(self,
           cluster_roll: ClusterRoll = 'd3043820717d74d9a17694c176d39733'
           )
```

__Arguments__

- __cluster_roll__: ClusterRoll

<h2 id="spotinst_sdk2.models.ocean.gcp.Tasks">Tasks</h2>

```python
Tasks(self,
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

<h2 id="spotinst_sdk2.models.ocean.gcp.Scheduling">Scheduling</h2>

```python
Scheduling(
    self,
    shutdown_hours: ShutdownHours = 'd3043820717d74d9a17694c176d39733',
    tasks:
    typing.List[spotinst_sdk2.models.ocean.gcp.Tasks] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __shutdown_hours__: ShutdownHours
- __tasks__: List[Tasks]

<h2 id="spotinst_sdk2.models.ocean.gcp.ContainerImage">ContainerImage</h2>

```python
ContainerImage(
  self,
  approved_images: typing.List[str] = 'd3043820717d74d9a17694c176d39733'
)
```

approved_images: List[str]

<h2 id="spotinst_sdk2.models.ocean.gcp.Security">Security</h2>

```python
Security(
  self,
  container_image: ContainerImage = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __container_image__: ContainerImage

<h2 id="spotinst_sdk2.models.ocean.gcp.ProvisioningModel">ProvisioningModel</h2>

```python
ProvisioningModel(cls,
                  value,
                  names=None,
                  *,
                  module,
                  qualname,
                  type,
                  start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.gcp.ProvisioningModel.preemptible">preemptible</h3>


<h3 id="spotinst_sdk2.models.ocean.gcp.ProvisioningModel.spot">spot</h3>


<h2 id="spotinst_sdk2.models.ocean.gcp.Strategy">Strategy</h2>

```python
Strategy(
    self,
    draining_timeout: int = 'd3043820717d74d9a17694c176d39733',
    preemptible_percentage: int = 'd3043820717d74d9a17694c176d39733',
    provisioning_model: ProvisioningModel = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __draining_timeout__: int
- __preemptible_percentage__: int
- __provisioning_model__: ProvisioningModel

<h2 id="spotinst_sdk2.models.ocean.gcp.Ocean">Ocean</h2>

```python
Ocean(self,
      auto_scaler: AutoScaler = 'd3043820717d74d9a17694c176d39733',
      capacity: Capacity = 'd3043820717d74d9a17694c176d39733',
      compute: Compute = 'd3043820717d74d9a17694c176d39733',
      controller_cluster_id: str = 'd3043820717d74d9a17694c176d39733',
      gke: GKE = 'd3043820717d74d9a17694c176d39733',
      name: str = 'd3043820717d74d9a17694c176d39733',
      scheduling: Scheduling = 'd3043820717d74d9a17694c176d39733',
      security: Security = 'd3043820717d74d9a17694c176d39733',
      strategy: Strategy = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __auto_scaler__: AutoScaler
- __capacity__: Capacity
- __compute__: Compute
- __controller_cluster_id__: str
- __gke__: GKE
- __name__: str
- __scheduling__: Scheduling
- __security__: Security
- __strategy__: Strategy

<h2 id="spotinst_sdk2.models.ocean.gcp.Type">Type</h2>

```python
Type(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.gcp.Type.annotation">annotation</h3>


<h3 id="spotinst_sdk2.models.ocean.gcp.Type.label">label</h3>


<h2 id="spotinst_sdk2.models.ocean.gcp.Operator">Operator</h2>

```python
Operator(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.gcp.Operator.does_not_exist">does_not_exist</h3>


<h3 id="spotinst_sdk2.models.ocean.gcp.Operator.equals">equals</h3>


<h3 id="spotinst_sdk2.models.ocean.gcp.Operator.exists">exists</h3>


<h3 id="spotinst_sdk2.models.ocean.gcp.Operator.not_equals">not_equals</h3>


<h2 id="spotinst_sdk2.models.ocean.gcp.Attribute">Attribute</h2>

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

<h2 id="spotinst_sdk2.models.ocean.gcp.RightSizingRecommendationFilter">RightSizingRecommendationFilter</h2>

```python
RightSizingRecommendationFilter(
  self,
  namespaces: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  attribute: Attribute = 'd3043820717d74d9a17694c176d39733')
```

__Attribute__

namespaces: List[str]
attribute: Attribute

<h2 id="spotinst_sdk2.models.ocean.gcp.AllMatch">AllMatch</h2>

```python
AllMatch(
    self,
    all_match:
    typing.List[spotinst_sdk2.models.ocean.gcp.Attribute] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __all_match__:  List[Attribute]

<h2 id="spotinst_sdk2.models.ocean.gcp.Conditions">Conditions</h2>

```python
Conditions(
    self,
    any_match:
    typing.List[spotinst_sdk2.models.ocean.gcp.AllMatch] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __any_match__: List[AllMatch]

<h2 id="spotinst_sdk2.models.ocean.gcp.Scope">Scope</h2>

```python
Scope(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.gcp.Scope.namespace">namespace</h3>


<h3 id="spotinst_sdk2.models.ocean.gcp.Scope.resource">resource</h3>


<h2 id="spotinst_sdk2.models.ocean.gcp.Filter">Filter</h2>

```python
Filter(self,
       conditions: Conditions = 'd3043820717d74d9a17694c176d39733',
       scope: Scope = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __conditions__: Conditions
- __scope__: Scope

<h2 id="spotinst_sdk2.models.ocean.gcp.GroupBy">GroupBy</h2>

```python
GroupBy(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.gcp.GroupBy.namespace">namespace</h3>


<h3 id="spotinst_sdk2.models.ocean.gcp.GroupBy.namespace_annotation">namespace_annotation</h3>


<h3 id="spotinst_sdk2.models.ocean.gcp.GroupBy.namespace_label">namespace_label</h3>


<h3 id="spotinst_sdk2.models.ocean.gcp.GroupBy.resource_annotation">resource_annotation</h3>


<h3 id="spotinst_sdk2.models.ocean.gcp.GroupBy.resource_label">resource_label</h3>


<h2 id="spotinst_sdk2.models.ocean.gcp.AggregatedClusterCosts">AggregatedClusterCosts</h2>

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

<h2 id="spotinst_sdk2.models.ocean.gcp.AutoScale">AutoScale</h2>

```python
AutoScale(
  self,
  auto_headroom_percentage: int = 'd3043820717d74d9a17694c176d39733',
  headrooms:
    typing.List[spotinst_sdk2.models.ocean.gcp.Headroom] = 'd3043820717d74d9a17694c176d39733',
  down: Down = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __auto_headroom_percentage__: int
- __headrooms__: List[Headroom]
- __down__: Down

<h2 id="spotinst_sdk2.models.ocean.gcp.VNGResourceLimits">VNGResourceLimits</h2>

```python
VNGResourceLimits(
  self,
  max_instance_count: int = 'd3043820717d74d9a17694c176d39733',
  min_instance_count: int = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __max_instance_count__: int
- __min_instance_count__: int

<h2 id="spotinst_sdk2.models.ocean.gcp.Config">Config</h2>

```python
Config(
    self,
    headrooms:
    typing.List[spotinst_sdk2.models.ocean.gcp.Headroom] = 'd3043820717d74d9a17694c176d39733'
)
```

Arguments
headrooms: List[Headroom]

<h2 id="spotinst_sdk2.models.ocean.gcp.VNGTasks">VNGTasks</h2>

```python
VNGTasks(self,
         config: Config = 'd3043820717d74d9a17694c176d39733',
         cron_expression: str = 'd3043820717d74d9a17694c176d39733',
         is_enabled: bool = 'd3043820717d74d9a17694c176d39733',
         task_type: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __config__: Config
- __cron_expression__: str
- __is_enabled__: bool
- __task_type__: str

<h2 id="spotinst_sdk2.models.ocean.gcp.VNGScheduling">VNGScheduling</h2>

```python
VNGScheduling(
  self, tasks: typing.List[spotinst_sdk2.models.ocean.gcp.VNGTasks])
```

__Arguments__

- __tasks__: List[VNGTasks]

<h2 id="spotinst_sdk2.models.ocean.gcp.Storage">Storage</h2>

```python
Storage(self, local_ssd_count: int = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __local_ssd_count__: int

<h2 id="spotinst_sdk2.models.ocean.gcp.VNGStrategy">VNGStrategy</h2>

```python
VNGStrategy(
  self,
  preemptible_percentage: int = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __preemptible_percentage__: int

<h2 id="spotinst_sdk2.models.ocean.gcp.Taints">Taints</h2>

```python
Taints(self,
       effect: str = 'd3043820717d74d9a17694c176d39733',
       key: str = 'd3043820717d74d9a17694c176d39733',
       value: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __effect__: str
- __key__: str
- __value__: str

<h2 id="spotinst_sdk2.models.ocean.gcp.VirtualNodeGroup">VirtualNodeGroup</h2>

```python
VirtualNodeGroup(
    self,
    auto_scale: AutoScale = 'd3043820717d74d9a17694c176d39733',
    availability_zones: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
    instance_types: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
    labels:
    typing.List[spotinst_sdk2.models.ocean.gcp.Labels] = 'd3043820717d74d9a17694c176d39733',
    metadata:
    typing.List[spotinst_sdk2.models.ocean.gcp.Metadata] = 'd3043820717d74d9a17694c176d39733',
    name: str = 'd3043820717d74d9a17694c176d39733',
    network_interfaces:
    typing.List[spotinst_sdk2.models.ocean.gcp.NetworkInterfaces] = 'd3043820717d74d9a17694c176d39733',
    ocean_id: str = 'd3043820717d74d9a17694c176d39733',
    resource_limits: VNGResourceLimits = 'd3043820717d74d9a17694c176d39733',
    restrict_scale_down: bool = 'd3043820717d74d9a17694c176d39733',
    root_volume_size_in_gb: int = 'd3043820717d74d9a17694c176d39733',
    root_volume_type: str = 'd3043820717d74d9a17694c176d39733',
    scheduling: VNGScheduling = 'd3043820717d74d9a17694c176d39733',
    service_account: str = 'd3043820717d74d9a17694c176d39733',
    shielded_instance_config:
    ShieldedInstanceConfig = 'd3043820717d74d9a17694c176d39733',
    source_image: str = 'd3043820717d74d9a17694c176d39733',
    storage: Storage = 'd3043820717d74d9a17694c176d39733',
    strategy: VNGStrategy = 'd3043820717d74d9a17694c176d39733',
    tags: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
    taints:
    typing.List[spotinst_sdk2.models.ocean.gcp.Taints] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __auto_scale__: AutoScale
- __availability_zones__: List[str]
- __instance_types__: List[str]
- __labels__: List[Labels]
- __metadata__: List[Metadata]
- __name__: str
- __network_interfaces__: List[NetworkInterfaces]
- __ocean_id__: str
- __resource_limits__: ResourceLimits
- __restrict_scale_down__: bool
- __root_volume_size_in_gb__: int
- __root_volume_type__: str
- __scheduling__: Scheduling
- __service_account__: str
- __shielded_instance_config__: ShieldedInstanceConfig
- __source_image__: str
- __storage__: Storage
- __strategy__: VNGStrategy
- __tags__: List[str]
- __taints__: List[Taints]

<h2 id="spotinst_sdk2.models.ocean.gcp.Roll">Roll</h2>

```python
Roll(
  self,
  batch_min_healthy_percentage: int = 'd3043820717d74d9a17694c176d39733',
  batch_size_percentage: int = 'd3043820717d74d9a17694c176d39733',
  comment: str = 'd3043820717d74d9a17694c176d39733',
  launch_spec_ids: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  instance_ids: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  respect_pdb: bool = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __batch_min_healthy_percentage__: int
- __batch_size_percentage__: int
- __comment__: str
- __instance_names__: List[str]
- __launch_spec_ids__: List[str]
- __respect_pdb__: bool

<h2 id="spotinst_sdk2.models.ocean.gcp.ImportGkeClusterToOcean">ImportGkeClusterToOcean</h2>

```python
ImportGkeClusterToOcean(
  self,
  auto_scaler: AutoScaler = 'd3043820717d74d9a17694c176d39733',
  availability_zones:
    typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  backend_services:
    typing.List[spotinst_sdk2.models.ocean.gcp.BackendServices] = 'd3043820717d74d9a17694c176d39733',
  capacity: Capacity = 'd3043820717d74d9a17694c176d39733',
  controller_cluster_id: str = 'd3043820717d74d9a17694c176d39733',
  instance_types: InstanceTypes = 'd3043820717d74d9a17694c176d39733',
  name: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __auto_scaler__: AutoScaler
- __availability_zones__: List[str]
- __backend_services__: List[BackendServices]
- __capacity__: Capacity
- __controller_cluster_id__: str
- __instance_types__: InstanceTypes
- __name__: str

