<h1 id="spotinst_sdk2.models.elastigroup.gcp">spotinst_sdk2.models.elastigroup.gcp</h1>


<h2 id="spotinst_sdk2.models.elastigroup.gcp.Capacity">Capacity</h2>

```python
Capacity(self,
         minimum: int = 'd3043820717d74d9a17694c176d39733',
         maximum: int = 'd3043820717d74d9a17694c176d39733',
         target: int = 'd3043820717d74d9a17694c176d39733',
         unit: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __minimum__: int
- __maximum__: int
- __target__: int
- __unit__: str

<h2 id="spotinst_sdk2.models.elastigroup.gcp.RevertToPreemptible">RevertToPreemptible</h2>

```python
RevertToPreemptible(self,
                    perform_at: str = 'd3043820717d74d9a17694c176d39733'
                    )
```

__Arguments__

- __perform_at__: str

<h2 id="spotinst_sdk2.models.elastigroup.gcp.ProvisioningModel">ProvisioningModel</h2>

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
<h3 id="spotinst_sdk2.models.elastigroup.gcp.ProvisioningModel.preemptible">preemptible</h3>


<h3 id="spotinst_sdk2.models.elastigroup.gcp.ProvisioningModel.spot">spot</h3>


<h2 id="spotinst_sdk2.models.elastigroup.gcp.Strategy">Strategy</h2>

```python
Strategy(
    self,
    preemptible_percentage: int = 'd3043820717d74d9a17694c176d39733',
    on_demand_count: int = 'd3043820717d74d9a17694c176d39733',
    draining_timeout: int = 'd3043820717d74d9a17694c176d39733',
    fallback_to_od: bool = 'd3043820717d74d9a17694c176d39733',
    optimization_windows: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
    provisioning_model: ProvisioningModel = 'd3043820717d74d9a17694c176d39733',
    revert_to_preemptible:
    RevertToPreemptible = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __preemptible_percentage__: int
- __on_demand_count__: int
- __draining_timeout__: int
- __fallback_to_od__: bool
- __optimization_windows__: List[str]
- __provisioning_model__: ProvisioningModel
- __revert_to_preemptible__: RevertToPreemptible

<h2 id="spotinst_sdk2.models.elastigroup.gcp.ScalingPolicyAction">ScalingPolicyAction</h2>

```python
ScalingPolicyAction(
  self,
  scaling_type: str = 'd3043820717d74d9a17694c176d39733',
  adjustment: int = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __scaling_type__: str
- __adjustment__: int

<h2 id="spotinst_sdk2.models.elastigroup.gcp.ScalingPolicyDimension">ScalingPolicyDimension</h2>

```python
ScalingPolicyDimension(self,
                       name='d3043820717d74d9a17694c176d39733',
                       value='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __value__: str

<h2 id="spotinst_sdk2.models.elastigroup.gcp.ScalingPolicy">ScalingPolicy</h2>

```python
ScalingPolicy(
  self,
  action: ScalingPolicyAction = 'd3043820717d74d9a17694c176d39733',
  cooldown: int = 'd3043820717d74d9a17694c176d39733',
  dimensions: list = 'd3043820717d74d9a17694c176d39733',
  evaluation_periods: int = 'd3043820717d74d9a17694c176d39733',
  metric_name: str = 'd3043820717d74d9a17694c176d39733',
  namespace: str = 'd3043820717d74d9a17694c176d39733',
  operator: str = 'd3043820717d74d9a17694c176d39733',
  period: int = 'd3043820717d74d9a17694c176d39733',
  policy_name: str = 'd3043820717d74d9a17694c176d39733',
  source: str = 'd3043820717d74d9a17694c176d39733',
  statistic: str = 'd3043820717d74d9a17694c176d39733',
  threshold: int = 'd3043820717d74d9a17694c176d39733',
  unit: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __action__: ScalingPolicyAction
- __cooldown__: int
- __dimensions__: list[ScalingPolicyDimension]
- __evaluation_periods__: int
- __metric_name__: str
- __namespace__: str
- __operator__: str
- __period__: int
- __policy_name__: str
- __source__: str
- __statistic__: str
- __threshold__: int
- __unit__: str

<h2 id="spotinst_sdk2.models.elastigroup.gcp.Scaling">Scaling</h2>

```python
Scaling(
    self,
    up:
    typing.List[spotinst_sdk2.models.elastigroup.gcp.ScalingPolicy] = 'd3043820717d74d9a17694c176d39733',
    down:
    typing.List[spotinst_sdk2.models.elastigroup.gcp.ScalingPolicy] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __up__:  list[ScalingPolicy]
- __down__: list[ScalingPolicy]

<h2 id="spotinst_sdk2.models.elastigroup.gcp.DockerSwarmConfiguration">DockerSwarmConfiguration</h2>

```python
DockerSwarmConfiguration(
  self,
  master_host: str = 'd3043820717d74d9a17694c176d39733',
  master_port: int = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __master_host__: str
- __master_port__: int

<h2 id="spotinst_sdk2.models.elastigroup.gcp.Down">Down</h2>

```python
Down(self, evaluation_periods: int = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __evaluation_periods__: int

<h2 id="spotinst_sdk2.models.elastigroup.gcp.Headroom">Headroom</h2>

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

<h2 id="spotinst_sdk2.models.elastigroup.gcp.AutoScale">AutoScale</h2>

```python
AutoScale(self,
          is_enabled: bool = 'd3043820717d74d9a17694c176d39733',
          is_auto_config: bool = 'd3043820717d74d9a17694c176d39733',
          cooldown: int = 'd3043820717d74d9a17694c176d39733',
          headroom: Headroom = 'd3043820717d74d9a17694c176d39733',
          down: Down = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __is_enabled__: bool
- __is_auto_config__: bool
- __cooldown__: int
- __headroom__: Headroom
- __down__: Down

<h2 id="spotinst_sdk2.models.elastigroup.gcp.GKE">GKE</h2>

```python
GKE(self,
    auto_update: bool = 'd3043820717d74d9a17694c176d39733',
    auto_scale: AutoScale = 'd3043820717d74d9a17694c176d39733',
    cluster_identifier: str = 'd3043820717d74d9a17694c176d39733',
    location: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __auto_update__: bool
- __auto_scale__: AutoScale
- __cluster_identifier__: str
- __location__: str

<h2 id="spotinst_sdk2.models.elastigroup.gcp.ThirdPartiesIntegration">ThirdPartiesIntegration</h2>

```python
ThirdPartiesIntegration(
  self,
  docker_swarm:
    DockerSwarmConfiguration = 'd3043820717d74d9a17694c176d39733',
  gke: GKE = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __docker_swarm__: DockerSwarmConfiguration
- __gke __: GKE

<h2 id="spotinst_sdk2.models.elastigroup.gcp.Metadata">Metadata</h2>

```python
Metadata(self,
         key: str = 'd3043820717d74d9a17694c176d39733',
         value: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __key__: str
- __value__: str

<h2 id="spotinst_sdk2.models.elastigroup.gcp.NamedPorts">NamedPorts</h2>

```python
NamedPorts(self,
           name: str = 'd3043820717d74d9a17694c176d39733',
           ports: list = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __ports__: list[int]

<h2 id="spotinst_sdk2.models.elastigroup.gcp.BackendServices">BackendServices</h2>

```python
BackendServices(
  self,
  backend_service_name: str = 'd3043820717d74d9a17694c176d39733',
  location_type: str = 'd3043820717d74d9a17694c176d39733',
  scheme: str = 'd3043820717d74d9a17694c176d39733',
  named_ports: NamedPorts = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __backend_service_name__: str
- __location_type__: str
- __scheme__: str
- __named_ports__: NamedPorts

<h2 id="spotinst_sdk2.models.elastigroup.gcp.BackendServiceConfig">BackendServiceConfig</h2>

```python
BackendServiceConfig(
  self, backend_services: list = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __backend_services__: list[BackendServices]

<h2 id="spotinst_sdk2.models.elastigroup.gcp.InitializeParams">InitializeParams</h2>

```python
InitializeParams(self,
                 disk_size_gb: int = 'd3043820717d74d9a17694c176d39733',
                 disk_type: str = 'd3043820717d74d9a17694c176d39733',
                 source_image: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __disk_size_gb__: int
- __disk_type__: str
- __source_image__: str

<h2 id="spotinst_sdk2.models.elastigroup.gcp.Disk">Disk</h2>

```python
Disk(self,
     auto_delete: bool = 'd3043820717d74d9a17694c176d39733',
     boot: bool = 'd3043820717d74d9a17694c176d39733',
     device_name: str = 'd3043820717d74d9a17694c176d39733',
     initialize_params:
     InitializeParams = 'd3043820717d74d9a17694c176d39733',
     interface: str = 'd3043820717d74d9a17694c176d39733',
     mode: str = 'd3043820717d74d9a17694c176d39733',
     source: str = 'd3043820717d74d9a17694c176d39733',
     disk_type: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __auto_delete__: bool
- __boot__: bool
- __device_name__: str
- __initialize_params__: InitializeParams
- __interface__: str
- __mode__: str
- __source__: str
- __disk_type__: str

<h2 id="spotinst_sdk2.models.elastigroup.gcp.NetworkInterface">NetworkInterface</h2>

```python
NetworkInterface(self,
                 network: str = 'd3043820717d74d9a17694c176d39733',
                 project_id: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __network__: str
- __project_id__: str

<h2 id="spotinst_sdk2.models.elastigroup.gcp.LaunchSpecification">LaunchSpecification</h2>

```python
LaunchSpecification(
  self,
  metadata: list = 'd3043820717d74d9a17694c176d39733',
  tags: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  backend_service_config:
    BackendServiceConfig = 'd3043820717d74d9a17694c176d39733',
  startup_script: str = 'd3043820717d74d9a17694c176d39733',
  disks: list = 'd3043820717d74d9a17694c176d39733',
  network_interfaces: list = 'd3043820717d74d9a17694c176d39733',
  ip_forwarding: bool = 'd3043820717d74d9a17694c176d39733',
  shutdown_script: str = 'd3043820717d74d9a17694c176d39733',
  min_cpu_platform: str = 'd3043820717d74d9a17694c176d39733',
  instance_name_prefix: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __metadata__: list[Metadata]
- __tags__: List[str]
- __backend_service_config__: BackendServiceConfig
- __startup_script__: str
- __disks__: list[Disk]
- __network_interfaces__: list[NetworkInterface]
- __ip_forwarding__: bool
- __shutdown_script__: str
- __min_cpu_platform__: str
- __instance_name_prefix__: str

<h2 id="spotinst_sdk2.models.elastigroup.gcp.CustomInstanceTypes">CustomInstanceTypes</h2>

```python
CustomInstanceTypes(
  self,
  v_cPU: int = 'd3043820717d74d9a17694c176d39733',
  memory_giB: int = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __v_cPU__: int
- __memory_giB__: int

<h2 id="spotinst_sdk2.models.elastigroup.gcp.PreferredPreemtible">PreferredPreemtible</h2>

```python
PreferredPreemtible(
  self,
  custom: CustomInstanceTypes = 'd3043820717d74d9a17694c176d39733',
  preemptible: list = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __custom__: CustomInstanceTypes
- __preemptible__: list[str]

<h2 id="spotinst_sdk2.models.elastigroup.gcp.InstanceTypes">InstanceTypes</h2>

```python
InstanceTypes(
  self,
  ondemand: str = 'd3043820717d74d9a17694c176d39733',
  preemptible: list = 'd3043820717d74d9a17694c176d39733',
  custom: CustomInstanceTypes = 'd3043820717d74d9a17694c176d39733',
  preferred: PreferredPreemtible = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __ondemand__: str
- __preemptible__: list[str]
- __custom__: CustomInstanceTypes
- __preferred__: PreferredPreemtible

<h2 id="spotinst_sdk2.models.elastigroup.gcp.Gpu">Gpu</h2>

```python
Gpu(self,
    gpu_type: str = 'd3043820717d74d9a17694c176d39733',
    count: int = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __gpu_type__: str
- __count__: int

<h2 id="spotinst_sdk2.models.elastigroup.gcp.Health">Health</h2>

```python
Health(self,
       grace_period: str = 'd3043820717d74d9a17694c176d39733',
       auto_healing: bool = 'd3043820717d74d9a17694c176d39733',
       health_check_type: str = 'd3043820717d74d9a17694c176d39733',
       unhealthy_duration: int = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __grace_period__: str
- __auto_healing__: bool
- __health_check_type__: str
- __unhealthy_duration__: int

<h2 id="spotinst_sdk2.models.elastigroup.gcp.Subnet">Subnet</h2>

```python
Subnet(self,
       region='d3043820717d74d9a17694c176d39733',
       subnet_names='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __region__: str
- __subnet_names__: list[str]

<h2 id="spotinst_sdk2.models.elastigroup.gcp.Compute">Compute</h2>

```python
Compute(
  self,
  launch_specification:
    LaunchSpecification = 'd3043820717d74d9a17694c176d39733',
  instance_types: InstanceTypes = 'd3043820717d74d9a17694c176d39733',
  gpu: Gpu = 'd3043820717d74d9a17694c176d39733',
  health: Health = 'd3043820717d74d9a17694c176d39733',
  availability_zones: list = 'd3043820717d74d9a17694c176d39733',
  subnets: list = 'd3043820717d74d9a17694c176d39733',
  preferred_availability_zones: list = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __launch_specification__: LaunchSpecification
- __instance_types__: InstanceTypes
- __gpu__: Gpu
- __health__: Health
- __availability_zones__: list[str]
- __subnets__: list[Subnet]
- __preferred_availability_zones__: list[str]

<h2 id="spotinst_sdk2.models.elastigroup.gcp.Tasks">Tasks</h2>

```python
Tasks(self,
      cron_expression: str = 'd3043820717d74d9a17694c176d39733',
      is_enabled: bool = 'd3043820717d74d9a17694c176d39733',
      max_capacity: int = 'd3043820717d74d9a17694c176d39733',
      min_capacity: int = 'd3043820717d74d9a17694c176d39733',
      target_capacity: int = 'd3043820717d74d9a17694c176d39733',
      task_type: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __cron_expression__: str
- __is_enabled__: bool
- __max_capacity__: int
- __min_capacity__: int
- __target_capacity__: int
- __task_type__: str

<h2 id="spotinst_sdk2.models.elastigroup.gcp.Scheduling">Scheduling</h2>

```python
Scheduling(self, tasks: list = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __tasks__: list[Tasks]

<h2 id="spotinst_sdk2.models.elastigroup.gcp.Elastigroup">Elastigroup</h2>

```python
Elastigroup(self,
            name: str = 'd3043820717d74d9a17694c176d39733',
            description: str = 'd3043820717d74d9a17694c176d39733',
            capacity: Capacity = 'd3043820717d74d9a17694c176d39733',
            strategy: Strategy = 'd3043820717d74d9a17694c176d39733',
            scaling: Scaling = 'd3043820717d74d9a17694c176d39733',
            third_parties_integration:
            ThirdPartiesIntegration = 'd3043820717d74d9a17694c176d39733',
            compute: Compute = 'd3043820717d74d9a17694c176d39733',
            scheduling: Scheduling = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __description__: str
- __capacity__: Capacity
- __strategy__: Strategy
- __scaling__: Scaling
- __third_parties_integration__: ThirdPartiesIntegration
- __compute__: Compute
- __scheduling__: Scheduling

<h2 id="spotinst_sdk2.models.elastigroup.gcp.RollGroup">RollGroup</h2>

```python
RollGroup(
  self,
  batch_size_percentage: int = 'd3043820717d74d9a17694c176d39733',
  grace_period: int = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __batch_size_percentage__: int
- __grace_period__: int

<h2 id="spotinst_sdk2.models.elastigroup.gcp.DetachConfiguration">DetachConfiguration</h2>

```python
DetachConfiguration(
    self,
    instances_to_detach: list = 'd3043820717d74d9a17694c176d39733',
    should_terminate_instances: bool = 'd3043820717d74d9a17694c176d39733',
    draining_timeout: int = 'd3043820717d74d9a17694c176d39733',
    should_decrement_target_capacity: bool = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __instances_to_detach__: list[str]
- __should_terminate_instances__: bool
- __draining_timeout__: int
- __should_decrement_target_capacity__: bool

<h1 id="spotinst_sdk2.models.elastigroup.gcp.gke">spotinst_sdk2.models.elastigroup.gcp.gke</h1>


<h2 id="spotinst_sdk2.models.elastigroup.gcp.gke.Capacity">Capacity</h2>

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

<h2 id="spotinst_sdk2.models.elastigroup.gcp.gke.InstanceTypes">InstanceTypes</h2>

```python
InstanceTypes(self,
              ondemand: str = 'd3043820717d74d9a17694c176d39733',
              preemptible: list = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __ondemand__: str
- __preemptible__: list[str]

<h2 id="spotinst_sdk2.models.elastigroup.gcp.gke.GKEImportConfig">GKEImportConfig</h2>

```python
GKEImportConfig(
  self,
  name: str = 'd3043820717d74d9a17694c176d39733',
  preemptible_percentage: int = 'd3043820717d74d9a17694c176d39733',
  capacity: Capacity = 'd3043820717d74d9a17694c176d39733',
  instance_types: InstanceTypes = 'd3043820717d74d9a17694c176d39733',
  availability_zones: list = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __preemptible_percentage__: int
- __capacity__: Capacity
- __instance_types__: InstanceTypes
- __availability_zones__: list[str]

