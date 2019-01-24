<h1 id="spotinst_sdk.spotinst_emr.EMR">EMR</h1>

```python
EMR(self, name='d3043820717d74d9a17694c176d39733', description='d3043820717d74d9a17694c176d39733', region='d3043820717d74d9a17694c176d39733', strategy='d3043820717d74d9a17694c176d39733', compute='d3043820717d74d9a17694c176d39733', cluster='d3043820717d74d9a17694c176d39733', scaling='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __decription__: str
- __region__: str
- __strategy__: Strategy
- __compute__: Compute
- __cluster__: Cluster
- __scaling__: Scaling

<h1 id="spotinst_sdk.spotinst_emr.Strategy">Strategy</h1>

```python
Strategy(self, wrapping='d3043820717d74d9a17694c176d39733', cloning='d3043820717d74d9a17694c176d39733', new='d3043820717d74d9a17694c176d39733', provisioning_timeout='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __wrapping__: Wrapping
- __cloning__: Cloning
- __new__: Newing
- __provisioning_timeout__: ProvisioningTimeout

<h1 id="spotinst_sdk.spotinst_emr.Wrapping">Wrapping</h1>

```python
Wrapping(self, source_cluster_id)
```

__Arguments__

- __source_cluster_id__: str

<h1 id="spotinst_sdk.spotinst_emr.Cloning">Cloning</h1>

```python
Cloning(self, origin_cluster_id='d3043820717d74d9a17694c176d39733', include_steps='d3043820717d74d9a17694c176d39733', number_of_retries='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __origin_cluster_id__: str
- __include_steps__: bool
- __number_of_retries__: int

<h1 id="spotinst_sdk.spotinst_emr.ProvisioningTimeout">ProvisioningTimeout</h1>

```python
ProvisioningTimeout(self, timeout='d3043820717d74d9a17694c176d39733', timeout_action='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __timeout__: int
:- __tpye timeout_action__: str

<h1 id="spotinst_sdk.spotinst_emr.Compute">Compute</h1>

```python
Compute(self, ebs_root_volume_size='d3043820717d74d9a17694c176d39733', availability_zones='d3043820717d74d9a17694c176d39733', bootstrap_actions='d3043820717d74d9a17694c176d39733', steps='d3043820717d74d9a17694c176d39733', instance_groups='d3043820717d74d9a17694c176d39733', configurations='d3043820717d74d9a17694c176d39733', emr_managed_master_security_group='d3043820717d74d9a17694c176d39733', emr_managed_slave_security_group='d3043820717d74d9a17694c176d39733', additional_master_security_groups='d3043820717d74d9a17694c176d39733', service_access_security_group='d3043820717d74d9a17694c176d39733', custom_ami_id='d3043820717d74d9a17694c176d39733', repo_upgrade_on_boot='d3043820717d74d9a17694c176d39733', additional_slave_security_groups='d3043820717d74d9a17694c176d39733', ec2_key_name='d3043820717d74d9a17694c176d39733', applications='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __ebs_root_volume_size__: int
- __availability_zones__: List[AvailabilityZone]
- __bootstrap_actions__: BootstrapActions
- __steps__: Steps
- __instance_groups__: InstanceGroups
- __configurations__: Configurations
- __emr_managed_master_security_group__: str
- __emr_managed_slave_security_group__: str
- __additional_master_security_groups__: List[str]
- __service_access_security_group__: str
- __custom_ami_id__: str
- __repo_upgrade_on_boot__: str
- __additional_slave_security_groups__: List[str]
- __ec2_key_name__: str
- __applications__: List[Application]

<h1 id="spotinst_sdk.spotinst_emr.AvailabilityZone">AvailabilityZone</h1>

```python
AvailabilityZone(self, name='d3043820717d74d9a17694c176d39733', subnetId='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __subnetId__: str

<h1 id="spotinst_sdk.spotinst_emr.BootstrapActions">BootstrapActions</h1>

```python
BootstrapActions(self, file='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __file__: File

<h1 id="spotinst_sdk.spotinst_emr.File">File</h1>

```python
File(self, bucket='d3043820717d74d9a17694c176d39733', key='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __bucket__: str
- __key__: str

<h1 id="spotinst_sdk.spotinst_emr.Steps">Steps</h1>

```python
Steps(self, file='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __file__: File

<h1 id="spotinst_sdk.spotinst_emr.InstanceGroups">InstanceGroups</h1>

```python
InstanceGroups(self, master_group='d3043820717d74d9a17694c176d39733', core_group='d3043820717d74d9a17694c176d39733', task_group='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __master_group__: MasterGroup
- __core_group__: CoreGroup
- __task_group__: TaskGroup

<h1 id="spotinst_sdk.spotinst_emr.MasterGroup">MasterGroup</h1>

```python
MasterGroup(self, instance_types='d3043820717d74d9a17694c176d39733', target='d3043820717d74d9a17694c176d39733', life_cycle='d3043820717d74d9a17694c176d39733', configurations='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __instance_types__: List[str]
- __target__: int
- __life_cycle__: str
- __configurations__: Configurations

<h1 id="spotinst_sdk.spotinst_emr.CoreGroup">CoreGroup</h1>

```python
CoreGroup(self, instance_types='d3043820717d74d9a17694c176d39733', target='d3043820717d74d9a17694c176d39733', life_cycle='d3043820717d74d9a17694c176d39733', ebs_configuration='d3043820717d74d9a17694c176d39733', configurations='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __instance_types__: List[str]
- __target__: int
- __life_cycle__: str
- __ebs_configuration__: EbsConfiguration
- __configurations__: Configurations

<h1 id="spotinst_sdk.spotinst_emr.TaskGroup">TaskGroup</h1>

```python
TaskGroup(self, instance_types='d3043820717d74d9a17694c176d39733', capacity='d3043820717d74d9a17694c176d39733', life_cycle='d3043820717d74d9a17694c176d39733', ebs_configuration='d3043820717d74d9a17694c176d39733', configurations='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __instance_types__: List[str]
- __capacity__: Capacity
- __life_cycle__: str
- __ebs_configuration__: EbsConfiguration
- __configurations__: Configurations

<h1 id="spotinst_sdk.spotinst_emr.Capacity">Capacity</h1>

```python
Capacity(self, target='d3043820717d74d9a17694c176d39733', minimum='d3043820717d74d9a17694c176d39733', maximum='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __target__: int
- __minimum__: int
- __maximum__: int

<h1 id="spotinst_sdk.spotinst_emr.EbsConfiguration">EbsConfiguration</h1>

```python
EbsConfiguration(self, ebs_block_device_configs='d3043820717d74d9a17694c176d39733', ebs_optimized='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __ebs_block_device_configs__: List[SingleEbsConfig]
- __ebs_optimized__: bool

<h1 id="spotinst_sdk.spotinst_emr.SingleEbsConfig">SingleEbsConfig</h1>

```python
SingleEbsConfig(self, volume_specification='d3043820717d74d9a17694c176d39733', volumes_per_instance='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __volume_specification__: VolumeSpecification
- __volumes_per_instance__: int

<h1 id="spotinst_sdk.spotinst_emr.VolumeSpecification">VolumeSpecification</h1>

```python
VolumeSpecification(self, volume_type='d3043820717d74d9a17694c176d39733', size_in_gb='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __volume_type__: str
- __size_in_GB__: int

<h1 id="spotinst_sdk.spotinst_emr.Configurations">Configurations</h1>

```python
Configurations(self, file='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __file__: File

<h1 id="spotinst_sdk.spotinst_emr.Scaling">Scaling</h1>

```python
Scaling(self, up='d3043820717d74d9a17694c176d39733', down='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __up__: List[Metric]
- __down__: List[Metric]

<h1 id="spotinst_sdk.spotinst_emr.Metric">Metric</h1>

```python
Metric(self, metric_name='d3043820717d74d9a17694c176d39733', statistic='d3043820717d74d9a17694c176d39733', unit='d3043820717d74d9a17694c176d39733', threshold='d3043820717d74d9a17694c176d39733', adjustment='d3043820717d74d9a17694c176d39733', namespace='d3043820717d74d9a17694c176d39733', period='d3043820717d74d9a17694c176d39733', evaluation_periods='d3043820717d74d9a17694c176d39733', action='d3043820717d74d9a17694c176d39733', cooldown='d3043820717d74d9a17694c176d39733', dimensions='d3043820717d74d9a17694c176d39733', operator='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __metric_name__: str
- __statistic__: str
- __unit__: str
- __threshold__: int
- __adjustment__: int
- __namespace__: str
- __period__: int
- __evaluation_periods__: int
- __action__: Action
- __cooldown__: int
- __dimensions__: List[Dimension]
- __operator__: str

<h1 id="spotinst_sdk.spotinst_emr.Action">Action</h1>

```python
Action(self, type='d3043820717d74d9a17694c176d39733', adjustment='d3043820717d74d9a17694c176d39733', min_target_capacity='d3043820717d74d9a17694c176d39733', target='d3043820717d74d9a17694c176d39733', minimum='d3043820717d74d9a17694c176d39733', maximum='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __type__: str
- __adjustment__: int
- __min_target_capacity__: int
- __target__: int
- __minimum__: int
- __maximum__: int

<h1 id="spotinst_sdk.spotinst_emr.Dimension">Dimension</h1>

```python
Dimension(self, name='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str

