<h1 id="spotinst_sdk2.models.elastigroup.gcp">spotinst_sdk2.models.elastigroup.gcp</h1>


<h2 id="spotinst_sdk2.models.elastigroup.gcp.Elastigroup">Elastigroup</h2>

```python
Elastigroup(self, name='d3043820717d74d9a17694c176d39733', description='d3043820717d74d9a17694c176d39733', capacity='d3043820717d74d9a17694c176d39733', strategy='d3043820717d74d9a17694c176d39733', scaling='d3043820717d74d9a17694c176d39733', third_parties_integration='d3043820717d74d9a17694c176d39733', compute='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __description__: str
- __capacity__: Capacity
- __strategy__: Strategy
- __scaling__: Scaling
- __third_parties_integration__: ThirdPartiesIntegration
- __compute__: Compute

<h2 id="spotinst_sdk2.models.elastigroup.gcp.Capacity">Capacity</h2>

```python
Capacity(self, minimum='d3043820717d74d9a17694c176d39733', maximum='d3043820717d74d9a17694c176d39733', target='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __minimum__: int
- __maximum__: int
- __target__: int

<h2 id="spotinst_sdk2.models.elastigroup.gcp.Strategy">Strategy</h2>

```python
Strategy(self, preemptible_percentage='d3043820717d74d9a17694c176d39733', on_demand_count='d3043820717d74d9a17694c176d39733', draining_timeout='d3043820717d74d9a17694c176d39733', fallback_to_od='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __preemptible_percentage__: int
- __on_demand_count__: int
- __draining_timeout__: int
- __fallback_to_od__: bool

<h2 id="spotinst_sdk2.models.elastigroup.gcp.Scaling">Scaling</h2>

```python
Scaling(self, up='d3043820717d74d9a17694c176d39733', down='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __up__:  list[ScalingPolicy]
- __down__: list[ScalingPolicy]

<h2 id="spotinst_sdk2.models.elastigroup.gcp.ScalingPolicy">ScalingPolicy</h2>

```python
ScalingPolicy(self, source='d3043820717d74d9a17694c176d39733', policy_name='d3043820717d74d9a17694c176d39733', namespace='d3043820717d74d9a17694c176d39733', metric_name='d3043820717d74d9a17694c176d39733', dimensions='d3043820717d74d9a17694c176d39733', statistic='d3043820717d74d9a17694c176d39733', unit='d3043820717d74d9a17694c176d39733', threshold='d3043820717d74d9a17694c176d39733', period='d3043820717d74d9a17694c176d39733', evaluation_periods='d3043820717d74d9a17694c176d39733', cooldown='d3043820717d74d9a17694c176d39733', action='d3043820717d74d9a17694c176d39733', operator='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __source__: str
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

<h2 id="spotinst_sdk2.models.elastigroup.gcp.ScalingPolicyDimension">ScalingPolicyDimension</h2>

```python
ScalingPolicyDimension(self, name='d3043820717d74d9a17694c176d39733', value='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __value__: str

<h2 id="spotinst_sdk2.models.elastigroup.gcp.ScalingPolicyAction">ScalingPolicyAction</h2>

```python
ScalingPolicyAction(self, scaling_type='d3043820717d74d9a17694c176d39733', adjustment='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __type__: str
- __adjustment__: int

<h2 id="spotinst_sdk2.models.elastigroup.gcp.ThirdPartiesIntegration">ThirdPartiesIntegration</h2>

```python
ThirdPartiesIntegration(self, docker_swarm='d3043820717d74d9a17694c176d39733', gke='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __docker_swarm__: DockerSwarmConfiguration
- __gke __: GKE

<h2 id="spotinst_sdk2.models.elastigroup.gcp.DockerSwarmConfiguration">DockerSwarmConfiguration</h2>

```python
DockerSwarmConfiguration(self, master_host='d3043820717d74d9a17694c176d39733', master_port='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __master_host__: str
- __master_port__: int

<h2 id="spotinst_sdk2.models.elastigroup.gcp.GKE">GKE</h2>

```python
GKE(self, auto_update='d3043820717d74d9a17694c176d39733', auto_scale='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __auto_update__: bool
- __auto_scale__: AutoScale

<h2 id="spotinst_sdk2.models.elastigroup.gcp.AutoScale">AutoScale</h2>

```python
AutoScale(self, is_enabled='d3043820717d74d9a17694c176d39733', is_auto_config='d3043820717d74d9a17694c176d39733', cooldown='d3043820717d74d9a17694c176d39733', headroom='d3043820717d74d9a17694c176d39733', labels='d3043820717d74d9a17694c176d39733', down='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __is_enabled__: bool
- __is_auto_config__: bool
- __cooldown__: int
- __headroom__: Headroom
- __labels__: list[Label]
- __down__: Down

<h2 id="spotinst_sdk2.models.elastigroup.gcp.Headroom">Headroom</h2>

```python
Headroom(self, cpu_per_unit='d3043820717d74d9a17694c176d39733', memory_per_unit='d3043820717d74d9a17694c176d39733', num_of_units='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __cpu_per_unit__: int
- __memory_per_unit__: int
- __num_of_units__: int

<h2 id="spotinst_sdk2.models.elastigroup.gcp.Down">Down</h2>

```python
Down(self, evaluation_periods='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __evaluation_periods__: int

<h2 id="spotinst_sdk2.models.elastigroup.gcp.Compute">Compute</h2>

```python
Compute(self, launch_specification='d3043820717d74d9a17694c176d39733', instance_types='d3043820717d74d9a17694c176d39733', gpu='d3043820717d74d9a17694c176d39733', health='d3043820717d74d9a17694c176d39733', availability_zones='d3043820717d74d9a17694c176d39733', subnets='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __launch_specification__: LaunchSpecification
- __instance_types__: InstanceTypes
- __gpu__: Gpu
- __health__: Health
- __availability_zones__: list[str]
- __subnets__: list[Subnet]

<h2 id="spotinst_sdk2.models.elastigroup.gcp.LaunchSpecification">LaunchSpecification</h2>

```python
LaunchSpecification(self, labels='d3043820717d74d9a17694c176d39733', metadata='d3043820717d74d9a17694c176d39733', tags='d3043820717d74d9a17694c176d39733', backend_service_config='d3043820717d74d9a17694c176d39733', startup_script='d3043820717d74d9a17694c176d39733', disks='d3043820717d74d9a17694c176d39733', network_interfaces='d3043820717d74d9a17694c176d39733', service_account='d3043820717d74d9a17694c176d39733', ip_forwarding='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __labels__: list[Label]
- __metadata__: list[MetaData]
- __tags__: List[str]
- __backend_service_config__: BackendServiceConfig
- __startup_script__: str
- __disks__: list[Disk]
- __network_interfaces__: list[NetworkInterface]
- __service_account__: str
- __ip_forwarding__: bool

<h2 id="spotinst_sdk2.models.elastigroup.gcp.Label">Label</h2>

```python
Label(self, key='d3043820717d74d9a17694c176d39733', value='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __key__: str
- __value__: str

<h2 id="spotinst_sdk2.models.elastigroup.gcp.Metadata">Metadata</h2>

```python
Metadata(self, key='d3043820717d74d9a17694c176d39733', value='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __key__: str
- __value__: str

<h2 id="spotinst_sdk2.models.elastigroup.gcp.BackendServiceConfig">BackendServiceConfig</h2>

```python
BackendServiceConfig(self, backend_services='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __backend_services__: [BackendServices]

<h2 id="spotinst_sdk2.models.elastigroup.gcp.BackendServices">BackendServices</h2>

```python
BackendServices(self, backend_service_name='d3043820717d74d9a17694c176d39733', location_type='d3043820717d74d9a17694c176d39733', scheme='d3043820717d74d9a17694c176d39733', named_ports='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __backend_service_name__: str
- __location_type__: str
- __scheme__: str
- __named_ports__: NamedPorts

<h2 id="spotinst_sdk2.models.elastigroup.gcp.NamedPorts">NamedPorts</h2>

```python
NamedPorts(self, name='d3043820717d74d9a17694c176d39733', ports='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __ports__: list[int]

<h2 id="spotinst_sdk2.models.elastigroup.gcp.Disk">Disk</h2>

```python
Disk(self, auto_delete='d3043820717d74d9a17694c176d39733', boot='d3043820717d74d9a17694c176d39733', device_name='d3043820717d74d9a17694c176d39733', initialize_params='d3043820717d74d9a17694c176d39733', interface='d3043820717d74d9a17694c176d39733', mode='d3043820717d74d9a17694c176d39733', source='d3043820717d74d9a17694c176d39733', disk_type='d3043820717d74d9a17694c176d39733')
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

<h2 id="spotinst_sdk2.models.elastigroup.gcp.InitializeParams">InitializeParams</h2>

```python
InitializeParams(self, disk_size_gb='d3043820717d74d9a17694c176d39733', disk_type='d3043820717d74d9a17694c176d39733', source_image='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __disk_size_gb__: int
- __disk_type__: str
- __source_image__: str

<h2 id="spotinst_sdk2.models.elastigroup.gcp.NetworkInterface">NetworkInterface</h2>

```python
NetworkInterface(self, network='d3043820717d74d9a17694c176d39733', access_configs='d3043820717d74d9a17694c176d39733', alias_ip_ranges='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __network__: str
- __access_configs__: list[AccessConfig]
- __alias_ip_ranges__: list[AliasIpRange]

<h2 id="spotinst_sdk2.models.elastigroup.gcp.AccessConfig">AccessConfig</h2>

```python
AccessConfig(self, name='d3043820717d74d9a17694c176d39733', access_type='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __access_type__: str

<h2 id="spotinst_sdk2.models.elastigroup.gcp.AliasIpRange">AliasIpRange</h2>

```python
AliasIpRange(self, ip_cidr_range='d3043820717d74d9a17694c176d39733', subnetwork_range_name='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __ip_cidr_range__: str
- __subnetwork_range_name__: str

<h2 id="spotinst_sdk2.models.elastigroup.gcp.InstanceTypes">InstanceTypes</h2>

```python
InstanceTypes(self, ondemand='d3043820717d74d9a17694c176d39733', preemptible='d3043820717d74d9a17694c176d39733', custom='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __ondemand__: str
- __preemptible__: list[str]
- __custom__: list[CustomInstanceTypes]

<h2 id="spotinst_sdk2.models.elastigroup.gcp.CustomInstanceTypes">CustomInstanceTypes</h2>

```python
CustomInstanceTypes(self, v_cpu='d3043820717d74d9a17694c176d39733', memory_gib='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __v_cpu__: int
- __memory_gib__: int

<h2 id="spotinst_sdk2.models.elastigroup.gcp.Gpu">Gpu</h2>

```python
Gpu(self, gpu_type='d3043820717d74d9a17694c176d39733', count='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __type__: str
- __count__: int

<h2 id="spotinst_sdk2.models.elastigroup.gcp.Health">Health</h2>

```python
Health(self, grace_period='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __grace_period__: int

<h2 id="spotinst_sdk2.models.elastigroup.gcp.Subnet">Subnet</h2>

```python
Subnet(self, region='d3043820717d74d9a17694c176d39733', subnet_names='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __region__: str
- __subnet_names__: list[str]

<h2 id="spotinst_sdk2.models.elastigroup.gcp.RollGroup">RollGroup</h2>

```python
RollGroup(self, batch_size_percentage='d3043820717d74d9a17694c176d39733', grace_period='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __batch_size_percentage__: int
- __grace_period__: int

<h2 id="spotinst_sdk2.models.elastigroup.gcp.DetachConfiguration">DetachConfiguration</h2>

```python
DetachConfiguration(self, instances_to_detach='d3043820717d74d9a17694c176d39733', should_terminate_instances='d3043820717d74d9a17694c176d39733', draining_timeout='d3043820717d74d9a17694c176d39733', should_decrement_target_capacity='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __instances_to_detach__: list[str]
- __should_terminate_instances__: bool
- __draining_timeout__: int
- __should_decrement_target_capacity__: bool

<h1 id="spotinst_sdk2.models.elastigroup.gcp.gke">spotinst_sdk2.models.elastigroup.gcp.gke</h1>


<h2 id="spotinst_sdk2.models.elastigroup.gcp.gke.GKE">GKE</h2>

```python
GKE(self, name='d3043820717d74d9a17694c176d39733', preemptible_percentage='d3043820717d74d9a17694c176d39733', capacity='d3043820717d74d9a17694c176d39733', instance_types='d3043820717d74d9a17694c176d39733', availability_zones='d3043820717d74d9a17694c176d39733', node_image='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __preemptible_percentage__: int
- __capacity__: Capacity
- __instance_types__: InstanceTypes
- __availability_zones__: list[str]
- __node_image__: str

<h2 id="spotinst_sdk2.models.elastigroup.gcp.gke.Capacity">Capacity</h2>

```python
Capacity(self, minimum='d3043820717d74d9a17694c176d39733', maximum='d3043820717d74d9a17694c176d39733', target='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __minimum__: int
- __maximum__: int
- __target__: int

<h2 id="spotinst_sdk2.models.elastigroup.gcp.gke.InstanceTypes">InstanceTypes</h2>

```python
InstanceTypes(self, ondemand='d3043820717d74d9a17694c176d39733', preemptible='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __ondemand__: str
- __preemptible__: list[str]

