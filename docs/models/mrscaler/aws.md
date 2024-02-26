<h1 id="spotinst_sdk2.models.mrscaler.aws">spotinst_sdk2.models.mrscaler.aws</h1>


<h2 id="spotinst_sdk2.models.mrscaler.aws.Cluster">Cluster</h2>

```python
Cluster(
  self,
  visible_to_all_users: bool = 'd3043820717d74d9a17694c176d39733',
  termination_protected: bool = 'd3043820717d74d9a17694c176d39733',
  keep_job_flow_alive_when_no_steps:
    bool = 'd3043820717d74d9a17694c176d39733',
  log_uri: str = 'd3043820717d74d9a17694c176d39733',
  additional_info: str = 'd3043820717d74d9a17694c176d39733',
  job_flow_role: str = 'd3043820717d74d9a17694c176d39733',
  service_role: str = 'd3043820717d74d9a17694c176d39733',
  security_configuration: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __visible_to_all_users__: Boolean
- __termination_protected__: Boolean
- __keep_job_flow_alive_when_no_steps__: Boolean
- __log_uri__: str
- __additional_info__: str
- __job_flow_role__: str
- __service_role__: str
- __security_configuration__: str

<h2 id="spotinst_sdk2.models.mrscaler.aws.Wrapping">Wrapping</h2>

```python
Wrapping(self,
         source_cluster_id: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __source_cluster_id__: str

<h2 id="spotinst_sdk2.models.mrscaler.aws.Cloning">Cloning</h2>

```python
Cloning(self,
        origin_cluster_id: str = 'd3043820717d74d9a17694c176d39733',
        include_steps: bool = 'd3043820717d74d9a17694c176d39733',
        number_of_retries: int = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __origin_cluster_id__: str
- __include_steps__: bool
- __number_of_retries__: int

<h2 id="spotinst_sdk2.models.mrscaler.aws.New">New</h2>

```python
New(self,
    release_label: str = 'd3043820717d74d9a17694c176d39733',
    number_of_retries: int = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __release_label__: str
- __number_of_retries__: int

<h2 id="spotinst_sdk2.models.mrscaler.aws.ProvisioningTimeout">ProvisioningTimeout</h2>

```python
ProvisioningTimeout(
  self,
  timeout: int = 'd3043820717d74d9a17694c176d39733',
  timeout_action: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __timeout__: int
- __timeout_action__: str

<h2 id="spotinst_sdk2.models.mrscaler.aws.Strategy">Strategy</h2>

```python
Strategy(self,
         wrapping: Wrapping = 'd3043820717d74d9a17694c176d39733',
         cloning: Cloning = 'd3043820717d74d9a17694c176d39733',
         new: New = 'd3043820717d74d9a17694c176d39733',
         provisioning_timeout:
         ProvisioningTimeout = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __wrapping__: Wrapping
- __cloning__: Cloning
- __new__: New
- __provisioning_timeout__: ProvisioningTimeout

<h2 id="spotinst_sdk2.models.mrscaler.aws.Application">Application</h2>

```python
Application(self,
            name: str = 'd3043820717d74d9a17694c176d39733',
            args: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
            version: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __args__: List[str]
- __version__: str

<h2 id="spotinst_sdk2.models.mrscaler.aws.AvailabilityZone">AvailabilityZone</h2>

```python
AvailabilityZone(self,
                 name: str = 'd3043820717d74d9a17694c176d39733',
                 subnet_id: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __subnetId__: str

<h2 id="spotinst_sdk2.models.mrscaler.aws.File">File</h2>

```python
File(self,
     bucket: str = 'd3043820717d74d9a17694c176d39733',
     key: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __bucket__: str
- __key__: str

<h2 id="spotinst_sdk2.models.mrscaler.aws.ScriptBootstrapAction">ScriptBootstrapAction</h2>

```python
ScriptBootstrapAction(
  self,
  args: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  path: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __args__: List[str]
- __path__: str

<h2 id="spotinst_sdk2.models.mrscaler.aws.JsonConfiguration">JsonConfiguration</h2>

```python
JsonConfiguration(
    self,
    name: str = 'd3043820717d74d9a17694c176d39733',
    script_bootstrap_action:
    ScriptBootstrapAction = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __script_bootstrap_action__: ScriptBootstrapAction

<h2 id="spotinst_sdk2.models.mrscaler.aws.BootstrapActions">BootstrapActions</h2>

```python
BootstrapActions(
    self,
    file: File = 'd3043820717d74d9a17694c176d39733',
    json_configuration:
    typing.List[spotinst_sdk2.models.mrscaler.aws.JsonConfiguration] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __file__: File
- __json_configuration__: List[JsonConfiguration]

<h2 id="spotinst_sdk2.models.mrscaler.aws.Configurations">Configurations</h2>

```python
Configurations(self, file: File = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __file__: File

<h2 id="spotinst_sdk2.models.mrscaler.aws.DynamicVolumeSize">DynamicVolumeSize</h2>

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

<h2 id="spotinst_sdk2.models.mrscaler.aws.VolumeSpecification">VolumeSpecification</h2>

```python
VolumeSpecification(
    self,
    volume_type: str = 'd3043820717d74d9a17694c176d39733',
    size_in_g_b: int = 'd3043820717d74d9a17694c176d39733',
    iops: int = 'd3043820717d74d9a17694c176d39733',
    dynamic_volume_size: DynamicVolumeSize = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __volume_type__: str
- __size_in_g_b__: int
- __iops__: int
- __dynamic_volume_size__: DynamicVolumeSize

<h2 id="spotinst_sdk2.models.mrscaler.aws.SingleEbsConfig">SingleEbsConfig</h2>

```python
SingleEbsConfig(
  self,
  volume_specification:
    VolumeSpecification = 'd3043820717d74d9a17694c176d39733',
  volumes_per_instance: int = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __volume_specification__: VolumeSpecification
- __volumes_per_instance__: int

<h2 id="spotinst_sdk2.models.mrscaler.aws.EbsConfiguration">EbsConfiguration</h2>

```python
EbsConfiguration(
    self,
    ebs_optimized: bool = 'd3043820717d74d9a17694c176d39733',
    ebs_block_device_configs:
    typing.List[spotinst_sdk2.models.mrscaler.aws.SingleEbsConfig] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __ebs_optimized__: bool
- __ebs_block_device_configs__: List[SingleEbsConfig]

<h2 id="spotinst_sdk2.models.mrscaler.aws.Capacity">Capacity</h2>

```python
Capacity(self,
         target: int = 'd3043820717d74d9a17694c176d39733',
         minimum: int = 'd3043820717d74d9a17694c176d39733',
         maximum: int = 'd3043820717d74d9a17694c176d39733',
         unit: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __target__: int
- __minimum__: int
- __maximum__: int
- __unit__: str

<h2 id="spotinst_sdk2.models.mrscaler.aws.MasterGroup">MasterGroup</h2>

```python
MasterGroup(
  self,
  instance_types: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  target: int = 'd3043820717d74d9a17694c176d39733',
  life_cycle: str = 'd3043820717d74d9a17694c176d39733',
  ebs_configuration:
    EbsConfiguration = 'd3043820717d74d9a17694c176d39733',
  configurations: Configurations = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __instance_types__: List[str]
- __target__: int
- __life_cycle__: str
- __ebs_configuration__: EbsConfiguration
- __configurations__: Configurations

<h2 id="spotinst_sdk2.models.mrscaler.aws.CoreGroup">CoreGroup</h2>

```python
CoreGroup(
  self,
  instance_types: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  target: int = 'd3043820717d74d9a17694c176d39733',
  capacity: Capacity = 'd3043820717d74d9a17694c176d39733',
  life_cycle: str = 'd3043820717d74d9a17694c176d39733',
  ebs_configuration:
    EbsConfiguration = 'd3043820717d74d9a17694c176d39733',
  configurations: Configurations = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __instance_types__: List[str]
- __target__: int
- __capacity__: Capacity
- __life_cycle__: str
- __ebs_configuration__: EbsConfiguration
- __configurations__: Configurations

<h2 id="spotinst_sdk2.models.mrscaler.aws.TaskGroup">TaskGroup</h2>

```python
TaskGroup(
  self,
  instance_types: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  capacity: Capacity = 'd3043820717d74d9a17694c176d39733',
  life_cycle: str = 'd3043820717d74d9a17694c176d39733',
  ebs_configuration:
    EbsConfiguration = 'd3043820717d74d9a17694c176d39733',
  configurations: Configurations = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __instance_types__: List[str]
- __capacity__: Capacity
- __life_cycle__: str
- __ebs_configuration__: EbsConfiguration
- __configurations__: Configurations

<h2 id="spotinst_sdk2.models.mrscaler.aws.InstanceGroups">InstanceGroups</h2>

```python
InstanceGroups(
  self,
  master_group: MasterGroup = 'd3043820717d74d9a17694c176d39733',
  core_group: CoreGroup = 'd3043820717d74d9a17694c176d39733',
  task_group: TaskGroup = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __master_group__: MasterGroup
- __core_group__: CoreGroup
- __task_group__: TaskGroup

<h2 id="spotinst_sdk2.models.mrscaler.aws.InstanceWeight">InstanceWeight</h2>

```python
InstanceWeight(
  self,
  instance_type: str = 'd3043820717d74d9a17694c176d39733',
  weighted_capacity: int = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __instance_type__: str
- __weighted_capacity__: int

<h2 id="spotinst_sdk2.models.mrscaler.aws.Steps">Steps</h2>

```python
Steps(self, file='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __file__: File

<h2 id="spotinst_sdk2.models.mrscaler.aws.Tag">Tag</h2>

```python
Tag(self,
    tag_key: str = 'd3043820717d74d9a17694c176d39733',
    tag_value: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __tag_key__: str
- __tag_value__: str

<h2 id="spotinst_sdk2.models.mrscaler.aws.Compute">Compute</h2>

```python
Compute(
    self,
    additional_master_security_groups:
    typing.List[str] = 'd3043820717d74d9a17694c176d39733',
    additional_slave_security_groups:
    typing.List[str] = 'd3043820717d74d9a17694c176d39733',
    applications:
    typing.List[spotinst_sdk2.models.mrscaler.aws.Application] = 'd3043820717d74d9a17694c176d39733',
    availability_zones:
    typing.List[spotinst_sdk2.models.mrscaler.aws.AvailabilityZone] = 'd3043820717d74d9a17694c176d39733',
    bootstrap_actions: BootstrapActions = 'd3043820717d74d9a17694c176d39733',
    configurations: Configurations = 'd3043820717d74d9a17694c176d39733',
    custom_ami_id: str = 'd3043820717d74d9a17694c176d39733',
    ebs_root_volume_size: int = 'd3043820717d74d9a17694c176d39733',
    ec2_key_name: str = 'd3043820717d74d9a17694c176d39733',
    emr_managed_master_security_group: str = 'd3043820717d74d9a17694c176d39733',
    emr_managed_slave_security_group: str = 'd3043820717d74d9a17694c176d39733',
    instance_groups: InstanceGroups = 'd3043820717d74d9a17694c176d39733',
    instance_weights:
    typing.List[spotinst_sdk2.models.mrscaler.aws.InstanceWeight] = 'd3043820717d74d9a17694c176d39733',
    repo_upgrade_on_boot: str = 'd3043820717d74d9a17694c176d39733',
    service_access_security_group: str = 'd3043820717d74d9a17694c176d39733',
    steps: Steps = 'd3043820717d74d9a17694c176d39733',
    tags:
    typing.List[spotinst_sdk2.models.mrscaler.aws.Tag] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __additional_master_security_groups__: List[str]
- __additional_slave_security_groups__: List[str]
- __applications__: List[Application]
- __availability_zones__: List[AvailabilityZone]
- __bootstrap_actions__: BootstrapActions
- __configurations__: Configurations
- __custom_ami_id__: str
- __ebs_root_volume_size__: int
- __ec2_key_name__: str
- __emr_managed_master_security_group__: str
- __emr_managed_slave_security_group__: str
- __instance_groups__: InstanceGroups
- __instance_weights__: List[InstanceWeight]
- __repo_upgrade_on_boot__: str
- __service_access_security_group__: str
- __steps__: Steps
- __tags__: List[Tag]

<h2 id="spotinst_sdk2.models.mrscaler.aws.Task">Task</h2>

```python
Task(self,
     is_enabled: bool = 'd3043820717d74d9a17694c176d39733',
     instance_group_type: str = 'd3043820717d74d9a17694c176d39733',
     task_type: str = 'd3043820717d74d9a17694c176d39733',
     cron_expression: str = 'd3043820717d74d9a17694c176d39733',
     target_capacity: int = 'd3043820717d74d9a17694c176d39733',
     min_capacity: int = 'd3043820717d74d9a17694c176d39733',
     max_capacity: int = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __is_enabled__: bool
- __instance_group_type__: str
- __task_type__: str
- __cron_expression__: str
- __target_capacity__: int
- __min_capacity__: int
- __max_capacity__: int

<h2 id="spotinst_sdk2.models.mrscaler.aws.Scheduling">Scheduling</h2>

```python
Scheduling(
    self,
    tasks:
    typing.List[spotinst_sdk2.models.mrscaler.aws.Task] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __tasks__: List[Task]

<h2 id="spotinst_sdk2.models.mrscaler.aws.Action">Action</h2>

```python
Action(self,
       type: str = 'd3043820717d74d9a17694c176d39733',
       adjustment: int = 'd3043820717d74d9a17694c176d39733',
       min_target_capacity: int = 'd3043820717d74d9a17694c176d39733',
       target: int = 'd3043820717d74d9a17694c176d39733',
       minimum: int = 'd3043820717d74d9a17694c176d39733',
       maximum: int = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __type__: str
- __adjustment__: int
- __min_target_capacity__: int
- __target__: int
- __minimum__: int
- __maximum__: int

<h2 id="spotinst_sdk2.models.mrscaler.aws.Dimension">Dimension</h2>

```python
Dimension(self,
          name: str = 'd3043820717d74d9a17694c176d39733',
          value: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __value__: str

<h2 id="spotinst_sdk2.models.mrscaler.aws.Metric">Metric</h2>

```python
Metric(
  self,
  policy_name: str = 'd3043820717d74d9a17694c176d39733',
  metric_name: str = 'd3043820717d74d9a17694c176d39733',
  statistic: str = 'd3043820717d74d9a17694c176d39733',
  unit: str = 'd3043820717d74d9a17694c176d39733',
  threshold: int = 'd3043820717d74d9a17694c176d39733',
  adjustment: int = 'd3043820717d74d9a17694c176d39733',
  namespace: str = 'd3043820717d74d9a17694c176d39733',
  min_target_capacity: int = 'd3043820717d74d9a17694c176d39733',
  period: int = 'd3043820717d74d9a17694c176d39733',
  evaluation_periods: int = 'd3043820717d74d9a17694c176d39733',
  action: Action = 'd3043820717d74d9a17694c176d39733',
  cooldown: int = 'd3043820717d74d9a17694c176d39733',
  dimensions:
    typing.List[spotinst_sdk2.models.mrscaler.aws.Dimension] = 'd3043820717d74d9a17694c176d39733',
  operator: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __policy_name__: str
- __metric_name__: str
- __statistic__: str
- __unit__: str
- __threshold__: int
- __adjustment__: int
- __namespace__: str
- __min_target_capacity__: int
- __period__: int
- __evaluation_periods__: int
- __action__: Action
- __cooldown__: int
- __dimensions__: List[Dimension]
- __operator__: str

<h2 id="spotinst_sdk2.models.mrscaler.aws.Scaling">Scaling</h2>

```python
Scaling(
    self,
    up:
    typing.List[spotinst_sdk2.models.mrscaler.aws.Metric] = 'd3043820717d74d9a17694c176d39733',
    down:
    typing.List[spotinst_sdk2.models.mrscaler.aws.Metric] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __up__: List[Metric]
- __down__: List[Metric]

<h2 id="spotinst_sdk2.models.mrscaler.aws.Statement">Statement</h2>

```python
Statement(self,
          metric_name: str = 'd3043820717d74d9a17694c176d39733',
          statistic: str = 'd3043820717d74d9a17694c176d39733',
          unit: str = 'd3043820717d74d9a17694c176d39733',
          threshold: int = 'd3043820717d74d9a17694c176d39733',
          evaluation_periods: int = 'd3043820717d74d9a17694c176d39733',
          namespace: str = 'd3043820717d74d9a17694c176d39733',
          period: int = 'd3043820717d74d9a17694c176d39733',
          operator: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __metric_name__: str
- __statistic__: str
- __unit__: str
- __threshold__: int
- __namespace__: str
- __period__: int
- __evaluation_periods__: int
- __operator__: str

<h2 id="spotinst_sdk2.models.mrscaler.aws.TerminationPolicy">TerminationPolicy</h2>

```python
TerminationPolicy(
    self,
    statements:
    typing.List[spotinst_sdk2.models.mrscaler.aws.Statement] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __statements__: List[Statement]

<h2 id="spotinst_sdk2.models.mrscaler.aws.EMR">EMR</h2>

```python
EMR(
    self,
    name: str = 'd3043820717d74d9a17694c176d39733',
    description: str = 'd3043820717d74d9a17694c176d39733',
    region: str = 'd3043820717d74d9a17694c176d39733',
    strategy: Strategy = 'd3043820717d74d9a17694c176d39733',
    compute: Compute = 'd3043820717d74d9a17694c176d39733',
    cluster: Cluster = 'd3043820717d74d9a17694c176d39733',
    scheduling: Scheduling = 'd3043820717d74d9a17694c176d39733',
    scaling: Scaling = 'd3043820717d74d9a17694c176d39733',
    termination_policies:
    typing.List[spotinst_sdk2.models.mrscaler.aws.TerminationPolicy] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __name__: str
- __decription__: str
- __region__: str
- __strategy__: Strategy
- __compute__: Compute
- __cluster__: Cluster
- __scheduling__: Scheduling
- __scaling__: Scaling
- __termination_policies__: List[TerminationPolicy]

