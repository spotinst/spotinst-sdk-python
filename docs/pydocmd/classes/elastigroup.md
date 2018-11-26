<h1 id="spotinst_sdk.aws_elastigroup.Elastigroup">Elastigroup</h1>

```python
Elastigroup(self, name='d3043820717d74d9a17694c176d39733', description='d3043820717d74d9a17694c176d39733', region='d3043820717d74d9a17694c176d39733', capacity='d3043820717d74d9a17694c176d39733', strategy='d3043820717d74d9a17694c176d39733', compute='d3043820717d74d9a17694c176d39733', scaling='d3043820717d74d9a17694c176d39733', scheduling='d3043820717d74d9a17694c176d39733', multai='d3043820717d74d9a17694c176d39733', third_parties_integration='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __description__: str
- __region__: str
- __capacity__: Capacity
- __strategy__: Strategy
- __compute__: Compute
- __scaling__: Scaling
- __scheduling__: Scheduling
- __multai__: Multai
- __third_parties_integration__: ThirdPartyIntegrations

<h1 id="spotinst_sdk.aws_elastigroup.Strategy">Strategy</h1>

```python
Strategy(self, availability_vs_cost='d3043820717d74d9a17694c176d39733', risk='d3043820717d74d9a17694c176d39733', utilize_reserved_instances='d3043820717d74d9a17694c176d39733', fallback_to_od='d3043820717d74d9a17694c176d39733', on_demand_count='d3043820717d74d9a17694c176d39733', draining_timeout='d3043820717d74d9a17694c176d39733', spin_up_time='d3043820717d74d9a17694c176d39733', lifetime_period='d3043820717d74d9a17694c176d39733', signals='d3043820717d74d9a17694c176d39733', scaling_strategy='d3043820717d74d9a17694c176d39733', persistence='d3043820717d74d9a17694c176d39733', revert_to_spot='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __availability_vs_cost__: str
- __risk__: int
- __utilize_reserved_instances__: bool
- __fallback_to_od__: bool
- __on_demand_count__: int
- __draining_timeout__: int
- __spin_up_time__: int
- __lifetime_period__: int
- __signals__: list[Signal]
- __scaling_strategy__: ScalingStrategy
- __persistence__: Persistence
- __revert_to_spot__: RevertToSpot

<h1 id="spotinst_sdk.aws_elastigroup.Signal">Signal</h1>

```python
Signal(self, name='d3043820717d74d9a17694c176d39733', timeout='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __timeout__: int

<h1 id="spotinst_sdk.aws_elastigroup.ScalingStrategy">ScalingStrategy</h1>

```python
ScalingStrategy(self, terminate_at_end_of_billing_hour)
```

__Arguments__

- __terminate_at_end_of_billing_hour__: bool

<h1 id="spotinst_sdk.aws_elastigroup.Persistence">Persistence</h1>

```python
Persistence(self, should_persist_block_devices='d3043820717d74d9a17694c176d39733', should_persist_root_device='d3043820717d74d9a17694c176d39733', should_persist_private_ip='d3043820717d74d9a17694c176d39733', block_devices_mode='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __should_persist_block_devices__: bool
- __should_persist_root_device__: bool
- __should_persist_private_ip__: bool
- __block_devices_mode__: str

<h1 id="spotinst_sdk.aws_elastigroup.RevertToSpot">RevertToSpot</h1>

```python
RevertToSpot(self, perform_at='d3043820717d74d9a17694c176d39733', time_windows='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __perform_at__: str
- __time_windows__: list[str]

<h1 id="spotinst_sdk.aws_elastigroup.Capacity">Capacity</h1>

```python
Capacity(self, minimum='d3043820717d74d9a17694c176d39733', maximum='d3043820717d74d9a17694c176d39733', target='d3043820717d74d9a17694c176d39733', unit='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __minimum__: int
- __maximum__: int
- __target__: int
- __unit__: str

<h1 id="spotinst_sdk.aws_elastigroup.Scaling">Scaling</h1>

```python
Scaling(self, up='d3043820717d74d9a17694c176d39733', down='d3043820717d74d9a17694c176d39733', target='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __up__:  list[ScalingPolicy]
- __down__: list[ScalingPolicy]
- __target__: list[TargetTrackingPolicy]

<h1 id="spotinst_sdk.aws_elastigroup.ScalingPolicyDimension">ScalingPolicyDimension</h1>

```python
ScalingPolicyDimension(self, name='d3043820717d74d9a17694c176d39733', value='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __value__: str

<h1 id="spotinst_sdk.aws_elastigroup.ScalingPolicyAction">ScalingPolicyAction</h1>

```python
ScalingPolicyAction(self, type='d3043820717d74d9a17694c176d39733', adjustment='d3043820717d74d9a17694c176d39733', min_target_capacity='d3043820717d74d9a17694c176d39733', max_target_capacity='d3043820717d74d9a17694c176d39733', target='d3043820717d74d9a17694c176d39733', minimum='d3043820717d74d9a17694c176d39733', maximum='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __type__: str
- __adjustment__: int
- __min_target_capacity__: int
- __max_target_capacity__: int
- __target__: int
- __minimum__: int
- __maximum__: int

<h1 id="spotinst_sdk.aws_elastigroup.ScalingPolicy">ScalingPolicy</h1>

```python
ScalingPolicy(self, namespace='d3043820717d74d9a17694c176d39733', metric_name='d3043820717d74d9a17694c176d39733', statistic='d3043820717d74d9a17694c176d39733', evaluation_periods='d3043820717d74d9a17694c176d39733', period='d3043820717d74d9a17694c176d39733', threshold='d3043820717d74d9a17694c176d39733', cooldown='d3043820717d74d9a17694c176d39733', action='d3043820717d74d9a17694c176d39733', unit='d3043820717d74d9a17694c176d39733', operator='d3043820717d74d9a17694c176d39733', dimensions='d3043820717d74d9a17694c176d39733', policy_name='d3043820717d74d9a17694c176d39733', source='d3043820717d74d9a17694c176d39733', extended_statistic='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __namespace__: str
- __metric_name__: str
- __statistic__: str
- __evaluation_periods__: int
- __period__: int
- __threshold__: float
- __cooldown__: int
- __action__: ScalingPolicyAction
- __unit__: str
- __operator__: str
- __dimensions__: list[ScalingPolicyDimension]
- __policy_name__: str
- __source__: str
- __extended_statistic__: str

<h1 id="spotinst_sdk.aws_elastigroup.TargetTrackingPolicy">TargetTrackingPolicy</h1>

```python
TargetTrackingPolicy(self, namespace='d3043820717d74d9a17694c176d39733', metric_name='d3043820717d74d9a17694c176d39733', statistic='d3043820717d74d9a17694c176d39733', cooldown='d3043820717d74d9a17694c176d39733', target='d3043820717d74d9a17694c176d39733', unit='d3043820717d74d9a17694c176d39733', dimensions='d3043820717d74d9a17694c176d39733', policy_name='d3043820717d74d9a17694c176d39733', source='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __namespace__: str
- __metric_name__: str
- __statistic__: str
- __cooldown__: int
- __target__: int
- __unit__: str
- __dimensions__: list[ScalingPolicyDimension]
- __policy_name__: str
- __source__: str

<h1 id="spotinst_sdk.aws_elastigroup.Scheduling">Scheduling</h1>

```python
Scheduling(self, tasks='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __tasks__: list[ScheduledTask]

<h1 id="spotinst_sdk.aws_elastigroup.ScheduledTask">ScheduledTask</h1>

```python
ScheduledTask(self, task_type='d3043820717d74d9a17694c176d39733', scale_target_capacity='d3043820717d74d9a17694c176d39733', scale_min_capacity='d3043820717d74d9a17694c176d39733', scale_max_capacity='d3043820717d74d9a17694c176d39733', target_capacity='d3043820717d74d9a17694c176d39733', min_capacity='d3043820717d74d9a17694c176d39733', max_capacity='d3043820717d74d9a17694c176d39733', batch_size_percentage='d3043820717d74d9a17694c176d39733', grace_period='d3043820717d74d9a17694c176d39733', adjustment='d3043820717d74d9a17694c176d39733', adjustment_percentage='d3043820717d74d9a17694c176d39733', is_enabled='d3043820717d74d9a17694c176d39733', frequency='d3043820717d74d9a17694c176d39733', cron_expression='d3043820717d74d9a17694c176d39733', start_time='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __task_type__: str
- __scale_target_capacity__: int
- __scale_min_capacity__: int
- __scale_max_capacity__: int
- __target_capacity__: int
- __min_capacity__: int
- __max_capacity__: int
- __batch_size_percentage__: int
- __grace_period__: int
- __adjustment__: int
- __adjustment_percentage__: int
- __is_enabled__: bool
- __frequency__: str
- __cron_expression__: str
- __start_time__: str

<h1 id="spotinst_sdk.aws_elastigroup.Multai">Multai</h1>

```python
Multai(self, token='d3043820717d74d9a17694c176d39733', balancers='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __token__: str
- __balancers__: str

<h1 id="spotinst_sdk.aws_elastigroup.MultaiLoadBalancer">MultaiLoadBalancer</h1>

```python
MultaiLoadBalancer(self, project_id='d3043820717d74d9a17694c176d39733', balancer_id='d3043820717d74d9a17694c176d39733', target_set_id='d3043820717d74d9a17694c176d39733', az_awareness='d3043820717d74d9a17694c176d39733', auto_weight='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __project_id__: str
- __balancer_id__: str
- __target_set_id__: str
- __az_awareness__: bool
- __auto_weight__: bool

<h1 id="spotinst_sdk.aws_elastigroup.Rancher">Rancher</h1>

```python
Rancher(self, access_key='d3043820717d74d9a17694c176d39733', secret_key='d3043820717d74d9a17694c176d39733', master_host='d3043820717d74d9a17694c176d39733', version='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __access_key__: str
- __secret_key__: str
- __master_host__: str
- __version__: str

<h1 id="spotinst_sdk.aws_elastigroup.Mesosphere">Mesosphere</h1>

```python
Mesosphere(self, api_server='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __api_server__: str

<h1 id="spotinst_sdk.aws_elastigroup.ElasticBeanstalk">ElasticBeanstalk</h1>

```python
ElasticBeanstalk(self, environment_id='d3043820717d74d9a17694c176d39733', deployment_preferences='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __environment_id__: str
- __deployment_preferences__: DeploymentPreferences

<h1 id="spotinst_sdk.aws_elastigroup.DeploymentPreferences">DeploymentPreferences</h1>

```python
DeploymentPreferences(self, automatic_roll='d3043820717d74d9a17694c176d39733', batch_size_percentage='d3043820717d74d9a17694c176d39733', grace_period='d3043820717d74d9a17694c176d39733', strategy='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __automatic_roll__: bool
- __batch_size_percentage__: int
- __grace_period__: int
- __strategy__: BeanstalkDeploymentStrategy

<h1 id="spotinst_sdk.aws_elastigroup.BeanstalkDeploymentStrategy">BeanstalkDeploymentStrategy</h1>

```python
BeanstalkDeploymentStrategy(self, action='d3043820717d74d9a17694c176d39733', should_drain_instances='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __action__: str
- __should_drain_instances__: bool

<h1 id="spotinst_sdk.aws_elastigroup.EcsConfiguration">EcsConfiguration</h1>

```python
EcsConfiguration(self, cluster_name='d3043820717d74d9a17694c176d39733', auto_scale='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __cluster_name__: str
- __auto_scale__: EcsAutoScaleConfiguration

<h1 id="spotinst_sdk.aws_elastigroup.EcsAutoScaleConfiguration">EcsAutoScaleConfiguration</h1>

```python
EcsAutoScaleConfiguration(self, is_enabled='d3043820717d74d9a17694c176d39733', is_auto_config='d3043820717d74d9a17694c176d39733', cooldown='d3043820717d74d9a17694c176d39733', headroom='d3043820717d74d9a17694c176d39733', attributes='d3043820717d74d9a17694c176d39733', down='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __is_enabled__: bool
- __is_auto_config__:  bool
- __cooldown__: int
- __headroom__: EcsAutoScalerHeadroomConfiguration
- __attributes__: list[EcsAutoScalerAttributeConfiguration]
- __down__: EcsAutoScalerDownConfiguration

<h1 id="spotinst_sdk.aws_elastigroup.EcsAutoScalerHeadroomConfiguration">EcsAutoScalerHeadroomConfiguration</h1>

```python
EcsAutoScalerHeadroomConfiguration(self, cpu_per_unit='d3043820717d74d9a17694c176d39733', memory_per_unit='d3043820717d74d9a17694c176d39733', num_of_units='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __cpu_per_unit__: int
- __memory_per_unit__: int
- __num_of_units__: int

<h1 id="spotinst_sdk.aws_elastigroup.EcsAutoScalerAttributeConfiguration">EcsAutoScalerAttributeConfiguration</h1>

```python
EcsAutoScalerAttributeConfiguration(self, key='d3043820717d74d9a17694c176d39733', value='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __key__: str
- __value__: str

<h1 id="spotinst_sdk.aws_elastigroup.EcsAutoScalerDownConfiguration">EcsAutoScalerDownConfiguration</h1>

```python
EcsAutoScalerDownConfiguration(self, evaluation_periods='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __evaluation_periods__: int

<h1 id="spotinst_sdk.aws_elastigroup.MlbRuntimeConfiguration">MlbRuntimeConfiguration</h1>

```python
MlbRuntimeConfiguration(self, deployment_id='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __deployment_id__: str

<h1 id="spotinst_sdk.aws_elastigroup.KubernetesConfiguration">KubernetesConfiguration</h1>

```python
KubernetesConfiguration(self, api_server='d3043820717d74d9a17694c176d39733', token='d3043820717d74d9a17694c176d39733', integration_mode='d3043820717d74d9a17694c176d39733', cluster_identifier='d3043820717d74d9a17694c176d39733', auto_scale='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __api_server__: str
- __token__: str
- __integration_mode__: str
- __cluster_identifier__: str
- __auto_scale__: KubernetesAutoScalerConfiguration

<h1 id="spotinst_sdk.aws_elastigroup.KubernetesAutoScalerConfiguration">KubernetesAutoScalerConfiguration</h1>

```python
KubernetesAutoScalerConfiguration(self, is_enabled='d3043820717d74d9a17694c176d39733', is_auto_config='d3043820717d74d9a17694c176d39733', cooldown='d3043820717d74d9a17694c176d39733', headroom='d3043820717d74d9a17694c176d39733', labels='d3043820717d74d9a17694c176d39733', down='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __is_enabled__: bool
- __is_auto_config__: bool
- __cooldown__: int
- __headroom__: KubernetesAutoScalerHeadroomConfiguration
- __labels__: KubernetesAutoScalerLabelsConfiguration
- __down__: KubernetesAutoScalerDownConfiguration

<h1 id="spotinst_sdk.aws_elastigroup.KubernetesAutoScalerHeadroomConfiguration">KubernetesAutoScalerHeadroomConfiguration</h1>

```python
KubernetesAutoScalerHeadroomConfiguration(self, cpu_per_unit='d3043820717d74d9a17694c176d39733', memory_per_unit='d3043820717d74d9a17694c176d39733', num_of_units='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __cpu_per_unit__: int
- __memory_per_unit__: int
- __num_of_units__: int

<h1 id="spotinst_sdk.aws_elastigroup.KubernetesAutoScalerLabelsConfiguration">KubernetesAutoScalerLabelsConfiguration</h1>

```python
KubernetesAutoScalerLabelsConfiguration(self, key='d3043820717d74d9a17694c176d39733', value='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __key__: str
- __value__: str

<h1 id="spotinst_sdk.aws_elastigroup.KubernetesAutoScalerDownConfiguration">KubernetesAutoScalerDownConfiguration</h1>

```python
KubernetesAutoScalerDownConfiguration(self, evaluation_periods='d3043820717d74d9a17694c176d39733')
```

<h1 id="spotinst_sdk.aws_elastigroup.RightScaleConfiguration">RightScaleConfiguration</h1>

```python
RightScaleConfiguration(self, account_id='d3043820717d74d9a17694c176d39733', refresh_token='d3043820717d74d9a17694c176d39733', region='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __account_id__: str
- __refresh_token__: str
- __region__: str

<h1 id="spotinst_sdk.aws_elastigroup.OpsWorksConfiguration">OpsWorksConfiguration</h1>

```python
OpsWorksConfiguration(self, layer_id='d3043820717d74d9a17694c176d39733', stack_type='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __layer_id__: str
- __stack_type__: str

<h1 id="spotinst_sdk.aws_elastigroup.ChefConfiguration">ChefConfiguration</h1>

```python
ChefConfiguration(self, chef_server='d3043820717d74d9a17694c176d39733', organization='d3043820717d74d9a17694c176d39733', user='d3043820717d74d9a17694c176d39733', pem_key='d3043820717d74d9a17694c176d39733', chef_version='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __chef_server__: str
- __organization__: str
- __user__: str
- __pem_key__: str
- __chef_version__: str

<h1 id="spotinst_sdk.aws_elastigroup.CodeDeployConfiguration">CodeDeployConfiguration</h1>

```python
CodeDeployConfiguration(self, deployment_groups='d3043820717d74d9a17694c176d39733', clean_up_on_failure='d3043820717d74d9a17694c176d39733', terminate_instance_on_failure='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __deployment_groups__: list[CodeDeployDeploymentGroupsConfiguration]
- __clean_up_on_failure__: bool
- __terminate_instance_on_failure__: bool

<h1 id="spotinst_sdk.aws_elastigroup.CodeDeployDeploymentGroupsConfiguration">CodeDeployDeploymentGroupsConfiguration</h1>

```python
CodeDeployDeploymentGroupsConfiguration(self, application_name='d3043820717d74d9a17694c176d39733', deployment_group_name='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __application_name__: str
- __deployment_group_name__: str

<h1 id="spotinst_sdk.aws_elastigroup.NomadConfiguration">NomadConfiguration</h1>

```python
NomadConfiguration(self, master_host='d3043820717d74d9a17694c176d39733', master_port='d3043820717d74d9a17694c176d39733', acl_token='d3043820717d74d9a17694c176d39733', auto_scale='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __master_host__: str
- __master_port__: int
- __acl_token__: str
- __auto_scale__: NomadAutoScalerConfiguration

<h1 id="spotinst_sdk.aws_elastigroup.NomadAutoScalerConfiguration">NomadAutoScalerConfiguration</h1>

```python
NomadAutoScalerConfiguration(self, is_enabled='d3043820717d74d9a17694c176d39733', cooldown='d3043820717d74d9a17694c176d39733', headroom='d3043820717d74d9a17694c176d39733', constraints='d3043820717d74d9a17694c176d39733', down='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __is_enabled__: bool
- __cooldown__: int
- __headroom__: NomadAutoScalerHeadroomConfiguration
- __constraints__: list[NomadAutoScalerConstraintsConfiguration]
- __down__: NomadAutoScalerDownConfiguration

<h1 id="spotinst_sdk.aws_elastigroup.NomadAutoScalerHeadroomConfiguration">NomadAutoScalerHeadroomConfiguration</h1>

```python
NomadAutoScalerHeadroomConfiguration(self, cpu_per_unit='d3043820717d74d9a17694c176d39733', memory_per_unit='d3043820717d74d9a17694c176d39733', num_of_units='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __cpu_per_unit__: int
- __memory_per_unit__: int
- __num_of_units__: int

<h1 id="spotinst_sdk.aws_elastigroup.NomadAutoScalerConstraintsConfiguration">NomadAutoScalerConstraintsConfiguration</h1>

```python
NomadAutoScalerConstraintsConfiguration(self, key='d3043820717d74d9a17694c176d39733', value='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __key__: str
- __value__: str

<h1 id="spotinst_sdk.aws_elastigroup.NomadAutoScalerDownConfiguration">NomadAutoScalerDownConfiguration</h1>

```python
NomadAutoScalerDownConfiguration(self, evaluation_periods='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __evaluation_periods__: int

<h1 id="spotinst_sdk.aws_elastigroup.DockerSwarmConfiguration">DockerSwarmConfiguration</h1>

```python
DockerSwarmConfiguration(self, master_host='d3043820717d74d9a17694c176d39733', master_port='d3043820717d74d9a17694c176d39733', auto_scale='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __master_host__: str
- __master_port__: int
- __auto_scale__: DockerSwarmAutoScalerConfiguration

<h1 id="spotinst_sdk.aws_elastigroup.DockerSwarmAutoScalerConfiguration">DockerSwarmAutoScalerConfiguration</h1>

```python
DockerSwarmAutoScalerConfiguration(self, is_enabled='d3043820717d74d9a17694c176d39733', cooldown='d3043820717d74d9a17694c176d39733', headroom='d3043820717d74d9a17694c176d39733', down='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __is_enabled__: bool
- __cooldown__: int
- __headroom__: DockerSwarmAutoScalerHeadroomConfiguration
- __down__: DockerSwarmAutoScalerDownConfiguration

<h1 id="spotinst_sdk.aws_elastigroup.DockerSwarmAutoScalerHeadroomConfiguration">DockerSwarmAutoScalerHeadroomConfiguration</h1>

```python
DockerSwarmAutoScalerHeadroomConfiguration(self, cpu_per_unit='d3043820717d74d9a17694c176d39733', memory_per_unit='d3043820717d74d9a17694c176d39733', num_of_units='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __cpu_per_unit__: int
- __memory_per_unit__:
- __num_of_units__: int

<h1 id="spotinst_sdk.aws_elastigroup.DockerSwarmAutoScalerDownConfiguration">DockerSwarmAutoScalerDownConfiguration</h1>

```python
DockerSwarmAutoScalerDownConfiguration(self, evaluation_periods='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __evaluation_periods__: int

<h1 id="spotinst_sdk.aws_elastigroup.Route53Configuration">Route53Configuration</h1>

```python
Route53Configuration(self, domains='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __domains__: list[Route53DomainsConfiguration]

<h1 id="spotinst_sdk.aws_elastigroup.Route53DomainsConfiguration">Route53DomainsConfiguration</h1>

```python
Route53DomainsConfiguration(self, hosted_zone_id='d3043820717d74d9a17694c176d39733', record_sets='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __hosted_zone_id__: str
- __record_sets__: list[Route53RecordSetsConfiguration]

<h1 id="spotinst_sdk.aws_elastigroup.Route53RecordSetsConfiguration">Route53RecordSetsConfiguration</h1>

```python
Route53RecordSetsConfiguration(self, name='d3043820717d74d9a17694c176d39733', use_public_ip='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __use_public_ip__: bool

<h1 id="spotinst_sdk.aws_elastigroup.ThirdPartyIntegrations">ThirdPartyIntegrations</h1>

```python
ThirdPartyIntegrations(self, rancher='d3043820717d74d9a17694c176d39733', mesosphere='d3043820717d74d9a17694c176d39733', elastic_beanstalk='d3043820717d74d9a17694c176d39733', ecs='d3043820717d74d9a17694c176d39733', kubernetes='d3043820717d74d9a17694c176d39733', right_scale='d3043820717d74d9a17694c176d39733', ops_works='d3043820717d74d9a17694c176d39733', chef='d3043820717d74d9a17694c176d39733', mlb_runtime='d3043820717d74d9a17694c176d39733', code_deploy='d3043820717d74d9a17694c176d39733', nomad='d3043820717d74d9a17694c176d39733', docker_swarm='d3043820717d74d9a17694c176d39733', route53='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __rancher__: Rancher
- __mesosphere__: Mesosphere
- __elastic_beanstalk__: ElasticBeanstalk
- __ecs__: EcsConfiguration
- __kubernetes__: KubernetesConfiguration
- __right_scale__: RightScaleConfiguration
- __ops_works__: OpsWorksConfiguration
- __chef__: ChefConfiguration
- __mlb_runtime__: MlbRuntimeConfiguration
- __code_deploy__: CodeDeployConfiguration
- __nomad__: NomadConfiguration
- __docker_swarm__: DockerSwarmConfiguration
- __route53__: Route53Configuration

<h1 id="spotinst_sdk.aws_elastigroup.Compute">Compute</h1>

```python
Compute(self, launch_specification='d3043820717d74d9a17694c176d39733', instance_types='d3043820717d74d9a17694c176d39733', product='d3043820717d74d9a17694c176d39733', availability_zones='d3043820717d74d9a17694c176d39733', elastic_ips='d3043820717d74d9a17694c176d39733', private_ips='d3043820717d74d9a17694c176d39733', subnet_ids='d3043820717d74d9a17694c176d39733', preferred_availability_zones='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __launch_specification__: LaunchSpecification
- __instance_types__: InstanceTypes
- __product__: str
- __availability_zones__: list[AvailabilityZone]
- __elastic_ips__: list[str]
- __private_ips__: list[str]
- __subnet_ids__: list[str]
- __preferred_availability_zones__: list[str]

<h1 id="spotinst_sdk.aws_elastigroup.AvailabilityZone">AvailabilityZone</h1>

```python
AvailabilityZone(self, name='d3043820717d74d9a17694c176d39733', subnet_id='d3043820717d74d9a17694c176d39733', subnet_ids='d3043820717d74d9a17694c176d39733', placement_group_name='d3043820717d74d9a17694c176d39733')
```

__Aerguments__

name:
subnet_id:
subnet_ids:
placement_group_name:

<h1 id="spotinst_sdk.aws_elastigroup.InstanceTypes">InstanceTypes</h1>

```python
InstanceTypes(self, ondemand='d3043820717d74d9a17694c176d39733', spot='d3043820717d74d9a17694c176d39733', weights='d3043820717d74d9a17694c176d39733', preferred_spot='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __ondemand__: str
- __spot__: list[str]
- __weights__: list[Weight]
- __preferred_spot__: list[str]

<h1 id="spotinst_sdk.aws_elastigroup.Weight">Weight</h1>

```python
Weight(self, instance_type='d3043820717d74d9a17694c176d39733', weighted_capacity='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __instance_type__: str
- __weighted_capacity__: int

<h1 id="spotinst_sdk.aws_elastigroup.LaunchSpecification">LaunchSpecification</h1>

```python
LaunchSpecification(self, security_group_ids='d3043820717d74d9a17694c176d39733', image_id='d3043820717d74d9a17694c176d39733', monitoring='d3043820717d74d9a17694c176d39733', health_check_type='d3043820717d74d9a17694c176d39733', load_balancers_config='d3043820717d74d9a17694c176d39733', health_check_grace_period='d3043820717d74d9a17694c176d39733', health_check_unhealthy_duration_before_replacement='d3043820717d74d9a17694c176d39733', ebs_optimized='d3043820717d74d9a17694c176d39733', tenancy='d3043820717d74d9a17694c176d39733', iam_role='d3043820717d74d9a17694c176d39733', key_pair='d3043820717d74d9a17694c176d39733', user_data='d3043820717d74d9a17694c176d39733', shutdown_script='d3043820717d74d9a17694c176d39733', block_device_mappings='d3043820717d74d9a17694c176d39733', network_interfaces='d3043820717d74d9a17694c176d39733', tags='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __security_group_ids__: list[str]
- __image_id__: str
- __monitoring__: bool
- __health_check_type__: str
- __load_balancers_config__:  LoadBalancersConfig
- __health_check_grace_period__: int
- __health_check_unhealthy_duration_before_replacement__: int
- __ebs_optimized__: bool
- __tenancy__: str
- __iam_role__: IamRole
- __key_pair__: str
- __user_data__: str
- __shutdown_script__: str
- __block_device_mappings__: list[BlockDeviceMapping]
- __network_interfaces__: list[NetworkInterface]
- __tags__: list[Tag]

<h1 id="spotinst_sdk.aws_elastigroup.LoadBalancersConfig">LoadBalancersConfig</h1>

```python
LoadBalancersConfig(self, load_balancers='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __load_balancers__: list[LoadBalancer]

<h1 id="spotinst_sdk.aws_elastigroup.LoadBalancer">LoadBalancer</h1>

```python
LoadBalancer(self, type='d3043820717d74d9a17694c176d39733', arn='d3043820717d74d9a17694c176d39733', name='d3043820717d74d9a17694c176d39733', target_set_id='d3043820717d74d9a17694c176d39733', balancer_id='d3043820717d74d9a17694c176d39733', auto_weight='d3043820717d74d9a17694c176d39733', az_awareness='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __type__: str
- __arn__: str
- __name__: str
- __target_set_id__: str
- __balancer_id__: str
- __auto_weight__: bool
- __az_awareness__: bool

<h1 id="spotinst_sdk.aws_elastigroup.IamRole">IamRole</h1>

```python
IamRole(self, name='d3043820717d74d9a17694c176d39733', arn='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __arn__: str

<h1 id="spotinst_sdk.aws_elastigroup.BlockDeviceMapping">BlockDeviceMapping</h1>

```python
BlockDeviceMapping(self, device_name='d3043820717d74d9a17694c176d39733', ebs='d3043820717d74d9a17694c176d39733', no_device='d3043820717d74d9a17694c176d39733', virtual_name='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __device_name__: str
- __ebs__: list[EBS]
- __no_device__: bool
- __virtual_name__: str

<h1 id="spotinst_sdk.aws_elastigroup.EBS">EBS</h1>

```python
EBS(self, delete_on_termination='d3043820717d74d9a17694c176d39733', encrypted='d3043820717d74d9a17694c176d39733', iops='d3043820717d74d9a17694c176d39733', snapshot_id='d3043820717d74d9a17694c176d39733', volume_size='d3043820717d74d9a17694c176d39733', volume_type='d3043820717d74d9a17694c176d39733', kms_key_id='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __delete_on_termination__: bool
- __encrypted__: bool
- __iops__: int
- __snapshot_id__: str
- __volume_size__: int
- __volume_type__: str
- __kms_key_id__: str

<h1 id="spotinst_sdk.aws_elastigroup.Tag">Tag</h1>

```python
Tag(self, tag_key='d3043820717d74d9a17694c176d39733', tag_value='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __tag_key__: str
- __tag_value__: str

<h1 id="spotinst_sdk.aws_elastigroup.NetworkInterface">NetworkInterface</h1>

```python
NetworkInterface(self, delete_on_termination='d3043820717d74d9a17694c176d39733', device_index='d3043820717d74d9a17694c176d39733', description='d3043820717d74d9a17694c176d39733', secondary_private_ip_address_count='d3043820717d74d9a17694c176d39733', associate_public_ip_address='d3043820717d74d9a17694c176d39733', groups='d3043820717d74d9a17694c176d39733', network_interface_id='d3043820717d74d9a17694c176d39733', private_ip_address='d3043820717d74d9a17694c176d39733', private_ip_addresses='d3043820717d74d9a17694c176d39733', subnet_id='d3043820717d74d9a17694c176d39733', associate_ipv6_address='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __delete_on_termination__: bool
- __device_index__: int
- __description__: str
- __secondary_private_ip_address_count__: int
- __associate_public_ip_address__: bool
- __groups__: list[str]
- __network_interface_id__: str
- __private_ip_address__: str
- __private_ip_addresses__: PrivateIpAddress
- __subnet_id__: str
- __associate_ipv6_address__: str

<h1 id="spotinst_sdk.aws_elastigroup.PrivateIpAddress">PrivateIpAddress</h1>

```python
PrivateIpAddress(self, private_ip_address='d3043820717d74d9a17694c176d39733', primary='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __private_ip_address__: str
- __primary__: bool

<h1 id="spotinst_sdk.aws_elastigroup.Roll">Roll</h1>

```python
Roll(self, batch_size_percentage='d3043820717d74d9a17694c176d39733', grace_period='d3043820717d74d9a17694c176d39733', health_check_type='d3043820717d74d9a17694c176d39733', strategy='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __batch_size_percentage__: str
- __grace_period__: xstr
- __health_check_type__: str
- __strategy__: str

<h1 id="spotinst_sdk.aws_elastigroup.DetachConfiguration">DetachConfiguration</h1>

```python
DetachConfiguration(self, instances_to_detach='d3043820717d74d9a17694c176d39733', should_terminate_instances='d3043820717d74d9a17694c176d39733', draining_timeout='d3043820717d74d9a17694c176d39733', should_decrement_target_capacity='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __instances_to_detach__: bool
- __should_terminate_instances__: bool
- __draining_timeout__: int
- __should_decrement_target_capacity__: bool

<h1 id="spotinst_sdk.aws_elastigroup.StatefulDeallocation">StatefulDeallocation</h1>

```python
StatefulDeallocation(self, should_delete_images='d3043820717d74d9a17694c176d39733', should_delete_network_interfaces='d3043820717d74d9a17694c176d39733', should_delete_volumes='d3043820717d74d9a17694c176d39733', should_delete_snapshots='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __should_delete_images__: bool
- __should_delete_network_interfaces__: bool
- __should_delete_volumes__: bool
- __should_delete_snapshots__: bool

