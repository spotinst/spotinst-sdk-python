<h1 id="spotinst_sdk2.models.ocean.azure">spotinst_sdk2.models.ocean.azure</h1>


<h2 id="spotinst_sdk2.models.ocean.azure.Aks">Aks</h2>

```python
Aks(self,
    cluster_name: str = 'd3043820717d74d9a17694c176d39733',
    infrastructure_resource_group_name:
    str = 'd3043820717d74d9a17694c176d39733',
    region: str = 'd3043820717d74d9a17694c176d39733',
    resource_group_name: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __cluster_name__: str
- __infrastructure_resource_group_name__: str
- __region__: str
- __resource_group_name__: str

<h2 id="spotinst_sdk2.models.ocean.azure.ResourceLimits">ResourceLimits</h2>

```python
ResourceLimits(self,
               max_memory_gib: int = 'd3043820717d74d9a17694c176d39733',
               max_v_cpu: int = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __max_memory_gib__: int
- __max_v_cpu__: int

<h2 id="spotinst_sdk2.models.ocean.azure.Down">Down</h2>

```python
Down(
  self,
  max_scale_down_percentage: float = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __max_scale_down_percentage__: float

<h2 id="spotinst_sdk2.models.ocean.azure.Automatic">Automatic</h2>

```python
Automatic(self, percentage: int = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __percentage__: int

<h2 id="spotinst_sdk2.models.ocean.azure.AutoScalerHeadroom">AutoScalerHeadroom</h2>

```python
AutoScalerHeadroom(
  self, automatic: Automatic = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __automatic__: Automatic

<h2 id="spotinst_sdk2.models.ocean.azure.AutoScaler">AutoScaler</h2>

```python
AutoScaler(
  self,
  down: Down = 'd3043820717d74d9a17694c176d39733',
  headroom: AutoScalerHeadroom = 'd3043820717d74d9a17694c176d39733',
  is_enabled: bool = 'd3043820717d74d9a17694c176d39733',
  resource_limits: ResourceLimits = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __down__: Down
- __headroom__: AutoScalerHeadroom
- __is_enabled__: bool
- __resource_limits__: ResourceLimits

<h2 id="spotinst_sdk2.models.ocean.azure.ShutdownHours">ShutdownHours</h2>

```python
ShutdownHours(
  self,
  is_enabled: bool = 'd3043820717d74d9a17694c176d39733',
  time_windows: typing.List[str] = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __is_enabled__: bool
- __time_windows__: List[str]

<h2 id="spotinst_sdk2.models.ocean.azure.ClusterRoll">ClusterRoll</h2>

```python
ClusterRoll(
  self,
  batch_min_healthy_percentage: int = 'd3043820717d74d9a17694c176d39733',
  batch_size_percentage: int = 'd3043820717d74d9a17694c176d39733',
  comment: str = 'd3043820717d74d9a17694c176d39733',
  respect_pdb: bool = 'd3043820717d74d9a17694c176d39733',
  respect_restrict_scale_down: bool = 'd3043820717d74d9a17694c176d39733',
  vng_ids: typing.List[str] = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __batch_min_healthy_percentage__: int
- __batch_size_percentage__: int
- __comment__: str
- __respect_pdb__: bool
- __respect_restrict_scale_down__: bool
- __vng_ids__: List[str]

<h2 id="spotinst_sdk2.models.ocean.azure.Parameters">Parameters</h2>

```python
Parameters(self,
           cluster_roll: ClusterRoll = 'd3043820717d74d9a17694c176d39733'
           )
```

__Arguments__

- __cluster_roll__: ClusterRoll

<h2 id="spotinst_sdk2.models.ocean.azure.TaskType">TaskType</h2>

```python
TaskType(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.azure.TaskType.cluster_roll">cluster_roll</h3>


<h2 id="spotinst_sdk2.models.ocean.azure.Task">Task</h2>

```python
Task(self,
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

<h2 id="spotinst_sdk2.models.ocean.azure.Scheduling">Scheduling</h2>

```python
Scheduling(
    self,
    shutdown_hours: ShutdownHours = 'd3043820717d74d9a17694c176d39733',
    tasks:
    typing.List[spotinst_sdk2.models.ocean.azure.Task] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __shutdown_hours__: ShutdownHours
- __tasks__: List[Task]

<h2 id="spotinst_sdk2.models.ocean.azure.Health">Health</h2>

```python
Health(self, grace_period: int = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __grace_period__: int

<h2 id="spotinst_sdk2.models.ocean.azure.AutoScaleHeadroom">AutoScaleHeadroom</h2>

```python
AutoScaleHeadroom(
  self,
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

<h2 id="spotinst_sdk2.models.ocean.azure.AutoScale">AutoScale</h2>

```python
AutoScale(
    self,
    headrooms:
    typing.List[spotinst_sdk2.models.ocean.azure.AutoScaleHeadroom] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __headrooms__: List[AutoScaleHeadroom]

<h2 id="spotinst_sdk2.models.ocean.azure.NodeCountLimits">NodeCountLimits</h2>

```python
NodeCountLimits(self,
                max_count: int = 'd3043820717d74d9a17694c176d39733',
                min_count: int = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __max_count__: int
- __min_count__: int

<h2 id="spotinst_sdk2.models.ocean.azure.OsType">OsType</h2>

```python
OsType(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.azure.OsType.linux">linux</h3>


<h3 id="spotinst_sdk2.models.ocean.azure.OsType.windows">windows</h3>


<h2 id="spotinst_sdk2.models.ocean.azure.OsDiskType">OsDiskType</h2>

```python
OsDiskType(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.azure.OsDiskType.ephemereal">ephemereal</h3>


<h3 id="spotinst_sdk2.models.ocean.azure.OsDiskType.managed">managed</h3>


<h2 id="spotinst_sdk2.models.ocean.azure.OsSKU">OsSKU</h2>

```python
OsSKU(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.azure.OsSKU.azure_linux">azure_linux</h3>


<h3 id="spotinst_sdk2.models.ocean.azure.OsSKU.cbl_mariner">cbl_mariner</h3>


<h3 id="spotinst_sdk2.models.ocean.azure.OsSKU.ubuntu">ubuntu</h3>


<h3 id="spotinst_sdk2.models.ocean.azure.OsSKU.windows2019">windows2019</h3>


<h3 id="spotinst_sdk2.models.ocean.azure.OsSKU.windows2022">windows2022</h3>


<h2 id="spotinst_sdk2.models.ocean.azure.Sysctls">Sysctls</h2>

```python
Sysctls(self,
        vm_max_map_count: int = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __vm_max_map_count__: int

<h2 id="spotinst_sdk2.models.ocean.azure.LinuxOSConfig">LinuxOSConfig</h2>

```python
LinuxOSConfig(self,
              sysctls: Sysctls = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __sysctls__: Sysctls

<h2 id="spotinst_sdk2.models.ocean.azure.NodePoolProperties">NodePoolProperties</h2>

```python
NodePoolProperties(
  self,
  enable_node_public_i_p: bool = 'd3043820717d74d9a17694c176d39733',
  kubernetes_version: str = 'd3043820717d74d9a17694c176d39733',
  linux_o_s_config: LinuxOSConfig = 'd3043820717d74d9a17694c176d39733',
  max_pods_per_node: int = 'd3043820717d74d9a17694c176d39733',
  os_disk_size_g_b: int = 'd3043820717d74d9a17694c176d39733',
  os_disk_type: OsDiskType = 'd3043820717d74d9a17694c176d39733',
  os_s_k_u: OsSKU = 'd3043820717d74d9a17694c176d39733',
  os_type: OsType = 'd3043820717d74d9a17694c176d39733',
  pod_subnet_i_ds: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  vnet_subnet_i_ds: typing.List[str] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __enable_node_public_i_p__: bool
- __kubernetes_version__: str
- __linux_o_s_config__: LinuxOSConfig
- __max_pods_per_node__: int
- __os_disk_size_g_b__: int
- __os_disk_type__: OsDiskType
- __os_s_k_u__: OsSKU
- __os_type__: OsType
- __pod_subnet_i_ds__: List[str]
- __vnet_subnet_i_ds__: List[str]

<h2 id="spotinst_sdk2.models.ocean.azure.Strategy">Strategy</h2>

```python
Strategy(self,
         fallback_to_od: bool = 'd3043820717d74d9a17694c176d39733',
         spot_percentage: int = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __fallback_to_od__: bool
- __spot_percentage__: int

<h2 id="spotinst_sdk2.models.ocean.azure.Effect">Effect</h2>

```python
Effect(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.azure.Effect.no_execute">no_execute</h3>


<h3 id="spotinst_sdk2.models.ocean.azure.Effect.no_schedule">no_schedule</h3>


<h3 id="spotinst_sdk2.models.ocean.azure.Effect.prefer_no_execute">prefer_no_execute</h3>


<h3 id="spotinst_sdk2.models.ocean.azure.Effect.prefer_no_schedule">prefer_no_schedule</h3>


<h2 id="spotinst_sdk2.models.ocean.azure.Taint">Taint</h2>

```python
Taint(self,
      key: str = 'd3043820717d74d9a17694c176d39733',
      value: str = 'd3043820717d74d9a17694c176d39733',
      effect: Effect = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __key__: str
- __value__: str
- __effect__: Effect

<h2 id="spotinst_sdk2.models.ocean.azure.Architecture">Architecture</h2>

```python
Architecture(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.azure.Architecture.amd64">amd64</h3>


<h3 id="spotinst_sdk2.models.ocean.azure.Architecture.arm64">arm64</h3>


<h3 id="spotinst_sdk2.models.ocean.azure.Architecture.intel64">intel64</h3>


<h3 id="spotinst_sdk2.models.ocean.azure.Architecture.x86_64">x86_64</h3>


<h2 id="spotinst_sdk2.models.ocean.azure.AcceleratedNetworking">AcceleratedNetworking</h2>

```python
AcceleratedNetworking(cls,
                      value,
                      names=None,
                      *,
                      module,
                      qualname,
                      type,
                      start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.azure.AcceleratedNetworking.disabled">disabled</h3>


<h3 id="spotinst_sdk2.models.ocean.azure.AcceleratedNetworking.enabled">enabled</h3>


<h2 id="spotinst_sdk2.models.ocean.azure.DiskPerformance">DiskPerformance</h2>

```python
DiskPerformance(cls,
                value,
                names=None,
                *,
                module,
                qualname,
                type,
                start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.azure.DiskPerformance.premium">premium</h3>


<h3 id="spotinst_sdk2.models.ocean.azure.DiskPerformance.standard">standard</h3>


<h2 id="spotinst_sdk2.models.ocean.azure.VmType">VmType</h2>

```python
VmType(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.azure.VmType.compute_optimized">compute_optimized</h3>


<h3 id="spotinst_sdk2.models.ocean.azure.VmType.general_purpose">general_purpose</h3>


<h3 id="spotinst_sdk2.models.ocean.azure.VmType.gpu">gpu</h3>


<h3 id="spotinst_sdk2.models.ocean.azure.VmType.high_performance_compute">high_performance_compute</h3>


<h3 id="spotinst_sdk2.models.ocean.azure.VmType.memory_optimized">memory_optimized</h3>


<h3 id="spotinst_sdk2.models.ocean.azure.VmType.storage_optimized">storage_optimized</h3>


<h2 id="spotinst_sdk2.models.ocean.azure.GpuType">GpuType</h2>

```python
GpuType(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.azure.GpuType.amd_radeon_instinct_mi25">amd_radeon_instinct_mi25</h3>


<h3 id="spotinst_sdk2.models.ocean.azure.GpuType.nvidia_a10">nvidia_a10</h3>


<h3 id="spotinst_sdk2.models.ocean.azure.GpuType.nvidia_tesla_a100">nvidia_tesla_a100</h3>


<h3 id="spotinst_sdk2.models.ocean.azure.GpuType.nvidia_tesla_h100">nvidia_tesla_h100</h3>


<h3 id="spotinst_sdk2.models.ocean.azure.GpuType.nvidia_tesla_k80">nvidia_tesla_k80</h3>


<h3 id="spotinst_sdk2.models.ocean.azure.GpuType.nvidia_tesla_m60">nvidia_tesla_m60</h3>


<h3 id="spotinst_sdk2.models.ocean.azure.GpuType.nvidia_tesla_p100">nvidia_tesla_p100</h3>


<h3 id="spotinst_sdk2.models.ocean.azure.GpuType.nvidia_tesla_p40">nvidia_tesla_p40</h3>


<h3 id="spotinst_sdk2.models.ocean.azure.GpuType.nvidia_tesla_t4">nvidia_tesla_t4</h3>


<h3 id="spotinst_sdk2.models.ocean.azure.GpuType.nvidia_tesla_v100">nvidia_tesla_v100</h3>


<h2 id="spotinst_sdk2.models.ocean.azure.Filters">Filters</h2>

```python
Filters(
    self,
    accelerated_networking:
    AcceleratedNetworking = 'd3043820717d74d9a17694c176d39733',
    disk_performance: DiskPerformance = 'd3043820717d74d9a17694c176d39733',
    architectures:
    typing.List[spotinst_sdk2.models.ocean.azure.Architecture] = 'd3043820717d74d9a17694c176d39733',
    exclude_series: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
    max_memory_gi_b: float = 'd3043820717d74d9a17694c176d39733',
    max_v_cpu: int = 'd3043820717d74d9a17694c176d39733',
    min_memory_gi_b: float = 'd3043820717d74d9a17694c176d39733',
    min_v_cpu: int = 'd3043820717d74d9a17694c176d39733',
    min_gpu: float = 'd3043820717d74d9a17694c176d39733',
    max_gpu: float = 'd3043820717d74d9a17694c176d39733',
    min_data: int = 'd3043820717d74d9a17694c176d39733',
    min_n_i_cs: int = 'd3043820717d74d9a17694c176d39733',
    series: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
    vm_types:
    typing.List[spotinst_sdk2.models.ocean.azure.VmType] = 'd3043820717d74d9a17694c176d39733',
    gpu_types:
    typing.List[spotinst_sdk2.models.ocean.azure.GpuType] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __accelerated_networking__: AcceleratedNetworking
- __disk_performance__: DiskPerformance
- __architectures__: List[Architecture]
- __exclude_series__: List[str]
- __max_memory_gi_b__: float
- __max_v_cpu__: int
- __min_memory_gi_b__: float
- __min_v_cpu__: int
- __min_gpu__: float
- __max_gpu__: float
- __min_data__: int
- __min_n_i_cs__: int
- __series__: List[str]
- __vm_types__: List[VmType]
- __gpu_types__: List[GpuType]

<h2 id="spotinst_sdk2.models.ocean.azure.VmSizes">VmSizes</h2>

```python
VmSizes(self, filters: Filters = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __filters__: Filters

<h2 id="spotinst_sdk2.models.ocean.azure.VirtualNodeGroupTemplate">VirtualNodeGroupTemplate</h2>

```python
VirtualNodeGroupTemplate(
  self,
  name: str = 'd3043820717d74d9a17694c176d39733',
  ocean_id: str = 'd3043820717d74d9a17694c176d39733',
  auto_scale: AutoScale = 'd3043820717d74d9a17694c176d39733',
  availability_zones:
    typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  labels: dict = 'd3043820717d74d9a17694c176d39733',
  node_count_limits: NodeCountLimits = 'd3043820717d74d9a17694c176d39733',
  node_pool_properties:
    NodePoolProperties = 'd3043820717d74d9a17694c176d39733',
  strategy: Strategy = 'd3043820717d74d9a17694c176d39733',
  tags: dict = 'd3043820717d74d9a17694c176d39733',
  taints:
    typing.List[spotinst_sdk2.models.ocean.azure.Taint] = 'd3043820717d74d9a17694c176d39733',
  vm_sizes: VmSizes = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __ocean_id__: str
- __auto_scale__: AutoScale
- __availability_zones__: List[str]
- __labels__: dict
- __node_count_limits__: NodeCountLimits
- __node_pool_properties__: NodePoolProperties
- __strategy__: Strategy
- __tags__: dict
- __taints__: List[Taint]
- __vm_sizes__: VmSizes

<h2 id="spotinst_sdk2.models.ocean.azure.Ocean">Ocean</h2>

```python
Ocean(self,
      aks: Aks = 'd3043820717d74d9a17694c176d39733',
      auto_scaler: AutoScaler = 'd3043820717d74d9a17694c176d39733',
      controller_cluster_id: str = 'd3043820717d74d9a17694c176d39733',
      health: Health = 'd3043820717d74d9a17694c176d39733',
      name: str = 'd3043820717d74d9a17694c176d39733',
      scheduling: Scheduling = 'd3043820717d74d9a17694c176d39733',
      virtual_node_group_template:
      VirtualNodeGroupTemplate = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __aks__: Aks
- __auto_scaler__: AutoScaler
- __controller_cluster_id__: str
- __health__: Health
- __name__: str
- __scheduling__: Scheduling
- __virtual_node_group_template__: VirtualNodeGroupTemplate

<h2 id="spotinst_sdk2.models.ocean.azure.PreferredLifecycle">PreferredLifecycle</h2>

```python
PreferredLifecycle(cls,
                   value,
                   names=None,
                   *,
                   module,
                   qualname,
                   type,
                   start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.azure.PreferredLifecycle.regular">regular</h3>


<h3 id="spotinst_sdk2.models.ocean.azure.PreferredLifecycle.spot">spot</h3>


<h2 id="spotinst_sdk2.models.ocean.azure.LaunchNewNodes">LaunchNewNodes</h2>

```python
LaunchNewNodes(
  self,
  adjustment: int = 'd3043820717d74d9a17694c176d39733',
  applicable_vm_sizes:
    typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  availability_zones:
    typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  min_cores_per_node: int = 'd3043820717d74d9a17694c176d39733',
  min_memory_gi_b_per_node: float = 'd3043820717d74d9a17694c176d39733',
  ocean_id: str = 'd3043820717d74d9a17694c176d39733',
  preferred_lifecycle:
    PreferredLifecycle = 'd3043820717d74d9a17694c176d39733',
  vng_ids: typing.List[str] = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __adjustment__: int
- __applicable_vm_sizes__: List[str]
- __availability_zones__: List[str]
- __min_cores_per_node__: int
- __min_memory_gi_b_per_node__: float
- __ocean_id__: str
- __preferred_lifecycle__: PreferredLifecycle
- __vng_ids__: List[str]

<h2 id="spotinst_sdk2.models.ocean.azure.Type">Type</h2>

```python
Type(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.azure.Type.annotation">annotation</h3>


<h3 id="spotinst_sdk2.models.ocean.azure.Type.label">label</h3>


<h2 id="spotinst_sdk2.models.ocean.azure.Operator">Operator</h2>

```python
Operator(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.azure.Operator.equals">equals</h3>


<h3 id="spotinst_sdk2.models.ocean.azure.Operator.exists">exists</h3>


<h3 id="spotinst_sdk2.models.ocean.azure.Operator.not_equals">not_equals</h3>


<h3 id="spotinst_sdk2.models.ocean.azure.Operator.not_exists">not_exists</h3>


<h2 id="spotinst_sdk2.models.ocean.azure.Attribute">Attribute</h2>

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

<h2 id="spotinst_sdk2.models.ocean.azure.AllMatch">AllMatch</h2>

```python
AllMatch(
    self,
    all_match:
    typing.List[spotinst_sdk2.models.ocean.azure.Attribute] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __all_match__:  List[Attribute]

<h2 id="spotinst_sdk2.models.ocean.azure.Conditions">Conditions</h2>

```python
Conditions(
    self,
    any_match:
    typing.List[spotinst_sdk2.models.ocean.azure.AllMatch] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __any_match__: List[AllMatch]

<h2 id="spotinst_sdk2.models.ocean.azure.Scope">Scope</h2>

```python
Scope(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.azure.Scope.namespace">namespace</h3>


<h3 id="spotinst_sdk2.models.ocean.azure.Scope.resource">resource</h3>


<h2 id="spotinst_sdk2.models.ocean.azure.Filter">Filter</h2>

```python
Filter(self,
       conditions: Conditions = 'd3043820717d74d9a17694c176d39733',
       scope: Scope = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __conditions__: Conditions
- __scope__: Scope

<h2 id="spotinst_sdk2.models.ocean.azure.GroupBy">GroupBy</h2>

```python
GroupBy(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean.azure.GroupBy.namespace">namespace</h3>


<h3 id="spotinst_sdk2.models.ocean.azure.GroupBy.namespace_annotation">namespace_annotation</h3>


<h3 id="spotinst_sdk2.models.ocean.azure.GroupBy.namespace_label">namespace_label</h3>


<h3 id="spotinst_sdk2.models.ocean.azure.GroupBy.resource_annotation">resource_annotation</h3>


<h3 id="spotinst_sdk2.models.ocean.azure.GroupBy.resource_label">resource_label</h3>


<h2 id="spotinst_sdk2.models.ocean.azure.AggregatedClusterCosts">AggregatedClusterCosts</h2>

```python
AggregatedClusterCosts(
  self,
  end_time: str = 'd3043820717d74d9a17694c176d39733',
  filter: Filter = 'd3043820717d74d9a17694c176d39733',
  group_by: GroupBy = 'namespace',
  start_time: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __end_time__: str
- __filter__: Filter
- __group_by__: GroupBy
- __start_time__: str

<h2 id="spotinst_sdk2.models.ocean.azure.Roll">Roll</h2>

```python
Roll(
  self,
  comment: str = 'd3043820717d74d9a17694c176d39733',
  batch_size_percentage: int = 'd3043820717d74d9a17694c176d39733',
  batch_min_healthy_percentage: int = 'd3043820717d74d9a17694c176d39733',
  respect_pdb: bool = 'd3043820717d74d9a17694c176d39733',
  node_pool_names: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  vng_ids: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  respect_restrict_scale_down: bool = 'd3043820717d74d9a17694c176d39733',
  node_names: typing.List[str] = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __comment__: str
- __batch_size_percentage__: int
- __batch_min_healthy_percentage__: int
- __respect_pdb__: bool
- __node_pool_names__: List[str]
- __vng_ids__: List[str]
- __respect_restrict_scale_down__: bool
- __node_names__: List[str]


<h2 id="spotinst_sdk2.models.ocean.azure.Migration">Migration</h2>

```python
Migration(
  self,
  node_names: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  node_pool_names: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  batch_size_percentage: int = 'd3043820717d74d9a17694c176d39733',
  batch_min_healthy_percentage: int = 'd3043820717d74d9a17694c176d39733',
  comment: str = 'd3043820717d74d9a17694c176d39733',
  respect_pdb: bool = 'd3043820717d74d9a17694c176d39733',
  respect_restrict_scale_down: bool = 'd3043820717d74d9a17694c176d39733',
  should_evict_standalone_pods: bool = 'd3043820717d74d9a17694c176d39733',
  should_terminate_nodes: bool = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __node_names__: List[str]
- __node_pool_names__: List[str]
- __batch_size_percentage__: int
- __batch_min_healthy_percentage__: int
- __comment__: str
- __respect_pdb__: bool
- __respect_restrict_scale_down__: bool
- __should_evict_standalone_pods__: bool
- __should_terminate_nodes__: bool

<h2 id="spotinst_sdk2.models.ocean.azure.DetachNodes">DetachNodes</h2>

```python
DetachNodes(self,
            node_names_to_detach:
            typing.List[str] = 'd3043820717d74d9a17694c176d39733',
            ocean_id: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __node_names_to_detach__: List[str]
- __ocean_id__: str

