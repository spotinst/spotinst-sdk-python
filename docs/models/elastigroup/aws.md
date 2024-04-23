<h1 id="spotinst_sdk2.models.elastigroup.aws">spotinst_sdk2.models.elastigroup.aws</h1>


<h2 id="spotinst_sdk2.models.elastigroup.aws.Elastigroup">Elastigroup</h2>

```python
Elastigroup(
  self,
  name='d3043820717d74d9a17694c176d39733',
  description='d3043820717d74d9a17694c176d39733',
  region='d3043820717d74d9a17694c176d39733',
  capacity='d3043820717d74d9a17694c176d39733',
  strategy='d3043820717d74d9a17694c176d39733',
  compute='d3043820717d74d9a17694c176d39733',
  scaling='d3043820717d74d9a17694c176d39733',
  scheduling='d3043820717d74d9a17694c176d39733',
  third_parties_integration='d3043820717d74d9a17694c176d39733')
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
- __third_parties_integration__: ThirdPartyIntegrations

<h2 id="spotinst_sdk2.models.elastigroup.aws.Strategy">Strategy</h2>

```python
Strategy(
  self,
  availability_vs_cost='d3043820717d74d9a17694c176d39733',
  risk='d3043820717d74d9a17694c176d39733',
  utilize_commitments='d3043820717d74d9a17694c176d39733',
  utilize_reserved_instances='d3043820717d74d9a17694c176d39733',
  fallback_to_od='d3043820717d74d9a17694c176d39733',
  on_demand_count='d3043820717d74d9a17694c176d39733',
  draining_timeout='d3043820717d74d9a17694c176d39733',
  spin_up_time='d3043820717d74d9a17694c176d39733',
  lifetime_period='d3043820717d74d9a17694c176d39733',
  signals='d3043820717d74d9a17694c176d39733',
  scaling_strategy='d3043820717d74d9a17694c176d39733',
  persistence='d3043820717d74d9a17694c176d39733',
  revert_to_spot='d3043820717d74d9a17694c176d39733',
  immediate_o_d_recover_threshold='d3043820717d74d9a17694c176d39733',
  restrict_single_az: bool = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __availability_vs_cost__: str
- __risk__: int
- __utilize_commitments__: bool
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
- __restrict_single_az__: bool

<h2 id="spotinst_sdk2.models.elastigroup.aws.Signal">Signal</h2>

```python
Signal(self,
       name='d3043820717d74d9a17694c176d39733',
       timeout='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __timeout__: int

<h2 id="spotinst_sdk2.models.elastigroup.aws.ScalingStrategy">ScalingStrategy</h2>

```python
ScalingStrategy(
  self,
  terminate_at_end_of_billing_hour='d3043820717d74d9a17694c176d39733',
  terminationPolicy='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __terminate_at_end_of_billing_hour__: bool
- __terminationPolicy__: str

<h2 id="spotinst_sdk2.models.elastigroup.aws.Persistence">Persistence</h2>

```python
Persistence(
  self,
  should_persist_block_devices='d3043820717d74d9a17694c176d39733',
  should_persist_root_device='d3043820717d74d9a17694c176d39733',
  should_persist_private_ip='d3043820717d74d9a17694c176d39733',
  block_devices_mode='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __should_persist_block_devices__: bool
- __should_persist_root_device__: bool
- __should_persist_private_ip__: bool
- __block_devices_mode__: str

<h2 id="spotinst_sdk2.models.elastigroup.aws.RevertToSpot">RevertToSpot</h2>

```python
RevertToSpot(self,
             perform_at='d3043820717d74d9a17694c176d39733',
             time_windows='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __perform_at__: str
- __time_windows__: list[str]

<h2 id="spotinst_sdk2.models.elastigroup.aws.Capacity">Capacity</h2>

```python
Capacity(self,
         minimum='d3043820717d74d9a17694c176d39733',
         maximum='d3043820717d74d9a17694c176d39733',
         target='d3043820717d74d9a17694c176d39733',
         unit='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __minimum__: int
- __maximum__: int
- __target__: int
- __unit__: str

<h2 id="spotinst_sdk2.models.elastigroup.aws.Scaling">Scaling</h2>

```python
Scaling(self,
        up='d3043820717d74d9a17694c176d39733',
        down='d3043820717d74d9a17694c176d39733',
        target='d3043820717d74d9a17694c176d39733',
        multiple_metrics='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __up__:  list[ScalingPolicy]
- __down__: list[ScalingPolicy]
- __target__: list[TargetTrackingPolicy]
- __multiple_metrics__: MultipleMetrics

<h2 id="spotinst_sdk2.models.elastigroup.aws.ScalingPolicyDimension">ScalingPolicyDimension</h2>

```python
ScalingPolicyDimension(self,
                       name='d3043820717d74d9a17694c176d39733',
                       value='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __value__: str

<h2 id="spotinst_sdk2.models.elastigroup.aws.ScalingPolicyAction">ScalingPolicyAction</h2>

```python
ScalingPolicyAction(
  self,
  type='d3043820717d74d9a17694c176d39733',
  adjustment='d3043820717d74d9a17694c176d39733',
  min_target_capacity='d3043820717d74d9a17694c176d39733',
  max_target_capacity='d3043820717d74d9a17694c176d39733',
  target='d3043820717d74d9a17694c176d39733',
  minimum='d3043820717d74d9a17694c176d39733',
  maximum='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __type__: str
- __adjustment__: int
- __min_target_capacity__: int
- __max_target_capacity__: int
- __target__: int
- __minimum__: int
- __maximum__: int

<h2 id="spotinst_sdk2.models.elastigroup.aws.ScalingPolicyStepAdjustment">ScalingPolicyStepAdjustment</h2>

```python
ScalingPolicyStepAdjustment(
  self,
  action='d3043820717d74d9a17694c176d39733',
  threshold='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __action__: ScalingPolicyAction
- __threshold__: int

<h2 id="spotinst_sdk2.models.elastigroup.aws.ScalingPolicy">ScalingPolicy</h2>

```python
ScalingPolicy(self,
              namespace='d3043820717d74d9a17694c176d39733',
              metric_name='d3043820717d74d9a17694c176d39733',
              statistic='d3043820717d74d9a17694c176d39733',
              evaluation_periods='d3043820717d74d9a17694c176d39733',
              period='d3043820717d74d9a17694c176d39733',
              threshold='d3043820717d74d9a17694c176d39733',
              cooldown='d3043820717d74d9a17694c176d39733',
              action='d3043820717d74d9a17694c176d39733',
              unit='d3043820717d74d9a17694c176d39733',
              operator='d3043820717d74d9a17694c176d39733',
              dimensions='d3043820717d74d9a17694c176d39733',
              policy_name='d3043820717d74d9a17694c176d39733',
              source='d3043820717d74d9a17694c176d39733',
              extended_statistic='d3043820717d74d9a17694c176d39733',
              step_adjustments='d3043820717d74d9a17694c176d39733',
              min_target_capacity='d3043820717d74d9a17694c176d39733',
              max_target_capacity='d3043820717d74d9a17694c176d39733',
              should_resume_stateful='d3043820717d74d9a17694c176d39733',
              is_enabled='d3043820717d74d9a17694c176d39733')
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
- __step_adjustments__: list[ScalingPolicyStepAdjustment]
- __min_target_capacity__: int
- __max_target_capacity__: int
- __should_resume_stateful__: bool
- __is_enabled__: bool

<h2 id="spotinst_sdk2.models.elastigroup.aws.TargetTrackingPolicy">TargetTrackingPolicy</h2>

```python
TargetTrackingPolicy(self,
                     namespace='d3043820717d74d9a17694c176d39733',
                     metric_name='d3043820717d74d9a17694c176d39733',
                     statistic='d3043820717d74d9a17694c176d39733',
                     cooldown='d3043820717d74d9a17694c176d39733',
                     target='d3043820717d74d9a17694c176d39733',
                     unit='d3043820717d74d9a17694c176d39733',
                     dimensions='d3043820717d74d9a17694c176d39733',
                     policy_name='d3043820717d74d9a17694c176d39733',
                     source='d3043820717d74d9a17694c176d39733')
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

<h2 id="spotinst_sdk2.models.elastigroup.aws.ScalingPolicyMetric">ScalingPolicyMetric</h2>

```python
ScalingPolicyMetric(
  self,
  name='d3043820717d74d9a17694c176d39733',
  namespace='d3043820717d74d9a17694c176d39733',
  metric_name='d3043820717d74d9a17694c176d39733',
  statistic='d3043820717d74d9a17694c176d39733',
  unit='d3043820717d74d9a17694c176d39733',
  dimensions='d3043820717d74d9a17694c176d39733',
  extended_statistic='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __metric_name__: str
- __name_space__: str
- __statistic__: str
- __unit__: str
- __dimensions__: list[ScalingPolicyDimension]
- __extended_statistic__: str

<h2 id="spotinst_sdk2.models.elastigroup.aws.MetricExpression">MetricExpression</h2>

```python
MetricExpression(self,
                 name='d3043820717d74d9a17694c176d39733',
                 expression='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __expression__: str

<h2 id="spotinst_sdk2.models.elastigroup.aws.MultipleMetrics">MultipleMetrics</h2>

```python
MultipleMetrics(self,
                metrics='d3043820717d74d9a17694c176d39733',
                expressions='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __metrics__: list[ScalingPolicyMetric]
- __expressions__: list[MetricExpression]

<h2 id="spotinst_sdk2.models.elastigroup.aws.Scheduling">Scheduling</h2>

```python
Scheduling(self, tasks='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __tasks__: list[ScheduledTask]

<h2 id="spotinst_sdk2.models.elastigroup.aws.ScheduledTask">ScheduledTask</h2>

```python
ScheduledTask(self,
              task_type='d3043820717d74d9a17694c176d39733',
              scale_target_capacity='d3043820717d74d9a17694c176d39733',
              scale_min_capacity='d3043820717d74d9a17694c176d39733',
              scale_max_capacity='d3043820717d74d9a17694c176d39733',
              target_capacity='d3043820717d74d9a17694c176d39733',
              min_capacity='d3043820717d74d9a17694c176d39733',
              max_capacity='d3043820717d74d9a17694c176d39733',
              batch_size_percentage='d3043820717d74d9a17694c176d39733',
              grace_period='d3043820717d74d9a17694c176d39733',
              adjustment='d3043820717d74d9a17694c176d39733',
              adjustment_percentage='d3043820717d74d9a17694c176d39733',
              is_enabled='d3043820717d74d9a17694c176d39733',
              frequency='d3043820717d74d9a17694c176d39733',
              cron_expression='d3043820717d74d9a17694c176d39733',
              start_time='d3043820717d74d9a17694c176d39733')
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

<h2 id="spotinst_sdk2.models.elastigroup.aws.Rancher">Rancher</h2>

```python
Rancher(self,
        access_key='d3043820717d74d9a17694c176d39733',
        secret_key='d3043820717d74d9a17694c176d39733',
        master_host='d3043820717d74d9a17694c176d39733',
        version='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __access_key__: str
- __secret_key__: str
- __master_host__: str
- __version__: str

<h2 id="spotinst_sdk2.models.elastigroup.aws.Mesosphere">Mesosphere</h2>

```python
Mesosphere(self, api_server='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __api_server__: str

<h2 id="spotinst_sdk2.models.elastigroup.aws.ElasticBeanstalk">ElasticBeanstalk</h2>

```python
ElasticBeanstalk(
  self,
  environment_id='d3043820717d74d9a17694c176d39733',
  managed_actions='d3043820717d74d9a17694c176d39733',
  deployment_preferences='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __environment_id__: str
- __managed_actions__: ManagedActions
- __deployment_preferences__: DeploymentPreferences

<h2 id="spotinst_sdk2.models.elastigroup.aws.ManagedActions">ManagedActions</h2>

```python
ManagedActions(self, platform_update='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __platform_update__: PlatformUpdate

<h2 id="spotinst_sdk2.models.elastigroup.aws.PlatformUpdate">PlatformUpdate</h2>

```python
PlatformUpdate(self,
               perform_at='d3043820717d74d9a17694c176d39733',
               time_window='d3043820717d74d9a17694c176d39733',
               update_level='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __perform_at__: str
- __time_window__: str
- __update_level__: str

<h2 id="spotinst_sdk2.models.elastigroup.aws.DeploymentPreferences">DeploymentPreferences</h2>

```python
DeploymentPreferences(
  self,
  automatic_roll='d3043820717d74d9a17694c176d39733',
  batch_size_percentage='d3043820717d74d9a17694c176d39733',
  grace_period='d3043820717d74d9a17694c176d39733',
  strategy='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __automatic_roll__: bool
- __batch_size_percentage__: int
- __grace_period__: int
- __strategy__: BeanstalkDeploymentStrategy

<h2 id="spotinst_sdk2.models.elastigroup.aws.BeanstalkDeploymentStrategy">BeanstalkDeploymentStrategy</h2>

```python
BeanstalkDeploymentStrategy(
  self,
  action='d3043820717d74d9a17694c176d39733',
  should_drain_instances='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __action__: str
- __should_drain_instances__: bool

<h2 id="spotinst_sdk2.models.elastigroup.aws.EcsConfiguration">EcsConfiguration</h2>

```python
EcsConfiguration(self,
                 cluster_name='d3043820717d74d9a17694c176d39733',
                 auto_scale='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __cluster_name__: str
- __auto_scale__: EcsAutoScaleConfiguration

<h2 id="spotinst_sdk2.models.elastigroup.aws.EcsAutoScaleConfiguration">EcsAutoScaleConfiguration</h2>

```python
EcsAutoScaleConfiguration(
  self,
  is_enabled='d3043820717d74d9a17694c176d39733',
  is_auto_config='d3043820717d74d9a17694c176d39733',
  cooldown='d3043820717d74d9a17694c176d39733',
  headroom='d3043820717d74d9a17694c176d39733',
  attributes='d3043820717d74d9a17694c176d39733',
  down='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __is_enabled__: bool
- __is_auto_config__:  bool
- __cooldown__: int
- __headroom__: EcsAutoScalerHeadroomConfiguration
- __attributes__: list[EcsAutoScalerAttributeConfiguration]
- __down__: EcsAutoScalerDownConfiguration

<h2 id="spotinst_sdk2.models.elastigroup.aws.EcsAutoScalerHeadroomConfiguration">EcsAutoScalerHeadroomConfiguration</h2>

```python
EcsAutoScalerHeadroomConfiguration(
  self,
  cpu_per_unit='d3043820717d74d9a17694c176d39733',
  memory_per_unit='d3043820717d74d9a17694c176d39733',
  num_of_units='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __cpu_per_unit__: int
- __memory_per_unit__: int
- __num_of_units__: int

<h2 id="spotinst_sdk2.models.elastigroup.aws.EcsAutoScalerAttributeConfiguration">EcsAutoScalerAttributeConfiguration</h2>

```python
EcsAutoScalerAttributeConfiguration(
  self,
  key='d3043820717d74d9a17694c176d39733',
  value='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __key__: str
- __value__: str

<h2 id="spotinst_sdk2.models.elastigroup.aws.EcsAutoScalerDownConfiguration">EcsAutoScalerDownConfiguration</h2>

```python
EcsAutoScalerDownConfiguration(
  self, evaluation_periods='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __evaluation_periods__: int

<h2 id="spotinst_sdk2.models.elastigroup.aws.KubernetesConfiguration">KubernetesConfiguration</h2>

```python
KubernetesConfiguration(
  self,
  api_server='d3043820717d74d9a17694c176d39733',
  token='d3043820717d74d9a17694c176d39733',
  integration_mode='d3043820717d74d9a17694c176d39733',
  cluster_identifier='d3043820717d74d9a17694c176d39733',
  auto_scale='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __api_server__: str
- __token__: str
- __integration_mode__: str
- __cluster_identifier__: str
- __auto_scale__: KubernetesAutoScalerConfiguration

<h2 id="spotinst_sdk2.models.elastigroup.aws.KubernetesAutoScalerConfiguration">KubernetesAutoScalerConfiguration</h2>

```python
KubernetesAutoScalerConfiguration(
  self,
  is_enabled='d3043820717d74d9a17694c176d39733',
  is_auto_config='d3043820717d74d9a17694c176d39733',
  cooldown='d3043820717d74d9a17694c176d39733',
  headroom='d3043820717d74d9a17694c176d39733',
  labels='d3043820717d74d9a17694c176d39733',
  down='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __is_enabled__: bool
- __is_auto_config__: bool
- __cooldown__: int
- __headroom__: KubernetesAutoScalerHeadroomConfiguration
- __labels__: KubernetesAutoScalerLabelsConfiguration
- __down__: KubernetesAutoScalerDownConfiguration

<h2 id="spotinst_sdk2.models.elastigroup.aws.KubernetesAutoScalerHeadroomConfiguration">KubernetesAutoScalerHeadroomConfiguration</h2>

```python
KubernetesAutoScalerHeadroomConfiguration(
  self,
  cpu_per_unit='d3043820717d74d9a17694c176d39733',
  memory_per_unit='d3043820717d74d9a17694c176d39733',
  num_of_units='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __cpu_per_unit__: int
- __memory_per_unit__: int
- __num_of_units__: int

<h2 id="spotinst_sdk2.models.elastigroup.aws.KubernetesAutoScalerLabelsConfiguration">KubernetesAutoScalerLabelsConfiguration</h2>

```python
KubernetesAutoScalerLabelsConfiguration(
  self,
  key='d3043820717d74d9a17694c176d39733',
  value='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __key__: str
- __value__: str

<h2 id="spotinst_sdk2.models.elastigroup.aws.KubernetesAutoScalerDownConfiguration">KubernetesAutoScalerDownConfiguration</h2>

```python
KubernetesAutoScalerDownConfiguration(
  self, evaluation_periods='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __evaluation_periods__: int

<h2 id="spotinst_sdk2.models.elastigroup.aws.RightScaleConfiguration">RightScaleConfiguration</h2>

```python
RightScaleConfiguration(self,
                        account_id='d3043820717d74d9a17694c176d39733',
                        refresh_token='d3043820717d74d9a17694c176d39733',
                        region='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __account_id__: str
- __refresh_token__: str
- __region__: str

<h2 id="spotinst_sdk2.models.elastigroup.aws.OpsWorksConfiguration">OpsWorksConfiguration</h2>

```python
OpsWorksConfiguration(self,
                      layer_id='d3043820717d74d9a17694c176d39733',
                      stack_type='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __layer_id__: str
- __stack_type__: str

<h2 id="spotinst_sdk2.models.elastigroup.aws.ChefConfiguration">ChefConfiguration</h2>

```python
ChefConfiguration(self,
                  chef_server='d3043820717d74d9a17694c176d39733',
                  organization='d3043820717d74d9a17694c176d39733',
                  user='d3043820717d74d9a17694c176d39733',
                  pem_key='d3043820717d74d9a17694c176d39733',
                  chef_version='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __chef_server__: str
- __organization__: str
- __user__: str
- __pem_key__: str
- __chef_version__: str

<h2 id="spotinst_sdk2.models.elastigroup.aws.CodeDeployConfiguration">CodeDeployConfiguration</h2>

```python
CodeDeployConfiguration(
  self,
  deployment_groups='d3043820717d74d9a17694c176d39733',
  clean_up_on_failure='d3043820717d74d9a17694c176d39733',
  terminate_instance_on_failure='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __deployment_groups__: list[CodeDeployDeploymentGroupsConfiguration]
- __clean_up_on_failure__: bool
- __terminate_instance_on_failure__: bool

<h2 id="spotinst_sdk2.models.elastigroup.aws.CodeDeployDeploymentGroupsConfiguration">CodeDeployDeploymentGroupsConfiguration</h2>

```python
CodeDeployDeploymentGroupsConfiguration(
  self,
  application_name='d3043820717d74d9a17694c176d39733',
  deployment_group_name='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __application_name__: str
- __deployment_group_name__: str

<h2 id="spotinst_sdk2.models.elastigroup.aws.NomadConfiguration">NomadConfiguration</h2>

```python
NomadConfiguration(self,
                   master_host='d3043820717d74d9a17694c176d39733',
                   master_port='d3043820717d74d9a17694c176d39733',
                   acl_token='d3043820717d74d9a17694c176d39733',
                   auto_scale='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __master_host__: str
- __master_port__: int
- __acl_token__: str
- __auto_scale__: NomadAutoScalerConfiguration

<h2 id="spotinst_sdk2.models.elastigroup.aws.NomadAutoScalerConfiguration">NomadAutoScalerConfiguration</h2>

```python
NomadAutoScalerConfiguration(
  self,
  is_enabled='d3043820717d74d9a17694c176d39733',
  cooldown='d3043820717d74d9a17694c176d39733',
  headroom='d3043820717d74d9a17694c176d39733',
  constraints='d3043820717d74d9a17694c176d39733',
  down='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __is_enabled__: bool
- __cooldown__: int
- __headroom__: NomadAutoScalerHeadroomConfiguration
- __constraints__: list[NomadAutoScalerConstraintsConfiguration]
- __down__: NomadAutoScalerDownConfiguration

<h2 id="spotinst_sdk2.models.elastigroup.aws.NomadAutoScalerHeadroomConfiguration">NomadAutoScalerHeadroomConfiguration</h2>

```python
NomadAutoScalerHeadroomConfiguration(
  self,
  cpu_per_unit='d3043820717d74d9a17694c176d39733',
  memory_per_unit='d3043820717d74d9a17694c176d39733',
  num_of_units='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __cpu_per_unit__: int
- __memory_per_unit__: int
- __num_of_units__: int

<h2 id="spotinst_sdk2.models.elastigroup.aws.NomadAutoScalerConstraintsConfiguration">NomadAutoScalerConstraintsConfiguration</h2>

```python
NomadAutoScalerConstraintsConfiguration(
  self,
  key='d3043820717d74d9a17694c176d39733',
  value='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __key__: str
- __value__: str

<h2 id="spotinst_sdk2.models.elastigroup.aws.NomadAutoScalerDownConfiguration">NomadAutoScalerDownConfiguration</h2>

```python
NomadAutoScalerDownConfiguration(
  self, evaluation_periods='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __evaluation_periods__: int

<h2 id="spotinst_sdk2.models.elastigroup.aws.DockerSwarmConfiguration">DockerSwarmConfiguration</h2>

```python
DockerSwarmConfiguration(self,
                         master_host='d3043820717d74d9a17694c176d39733',
                         master_port='d3043820717d74d9a17694c176d39733',
                         auto_scale='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __master_host__: str
- __master_port__: int
- __auto_scale__: DockerSwarmAutoScalerConfiguration

<h2 id="spotinst_sdk2.models.elastigroup.aws.DockerSwarmAutoScalerConfiguration">DockerSwarmAutoScalerConfiguration</h2>

```python
DockerSwarmAutoScalerConfiguration(
  self,
  is_enabled='d3043820717d74d9a17694c176d39733',
  cooldown='d3043820717d74d9a17694c176d39733',
  headroom='d3043820717d74d9a17694c176d39733',
  down='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __is_enabled__: bool
- __cooldown__: int
- __headroom__: DockerSwarmAutoScalerHeadroomConfiguration
- __down__: DockerSwarmAutoScalerDownConfiguration

<h2 id="spotinst_sdk2.models.elastigroup.aws.DockerSwarmAutoScalerHeadroomConfiguration">DockerSwarmAutoScalerHeadroomConfiguration</h2>

```python
DockerSwarmAutoScalerHeadroomConfiguration(
  self,
  cpu_per_unit='d3043820717d74d9a17694c176d39733',
  memory_per_unit='d3043820717d74d9a17694c176d39733',
  num_of_units='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __cpu_per_unit__: int
- __memory_per_unit__:
- __num_of_units__: int

<h2 id="spotinst_sdk2.models.elastigroup.aws.DockerSwarmAutoScalerDownConfiguration">DockerSwarmAutoScalerDownConfiguration</h2>

```python
DockerSwarmAutoScalerDownConfiguration(
  self, evaluation_periods='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __evaluation_periods__: int

<h2 id="spotinst_sdk2.models.elastigroup.aws.Route53Configuration">Route53Configuration</h2>

```python
Route53Configuration(self, domains='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __domains__: list[Route53DomainsConfiguration]

<h2 id="spotinst_sdk2.models.elastigroup.aws.Route53DomainsConfiguration">Route53DomainsConfiguration</h2>

```python
Route53DomainsConfiguration(
  self,
  hosted_zone_id='d3043820717d74d9a17694c176d39733',
  record_sets='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __hosted_zone_id__: str
- __record_sets__: list[Route53RecordSetsConfiguration]

<h2 id="spotinst_sdk2.models.elastigroup.aws.Route53RecordSetsConfiguration">Route53RecordSetsConfiguration</h2>

```python
Route53RecordSetsConfiguration(
  self,
  name='d3043820717d74d9a17694c176d39733',
  use_public_ip='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __use_public_ip__: bool

<h2 id="spotinst_sdk2.models.elastigroup.aws.ThirdPartyIntegrations">ThirdPartyIntegrations</h2>

```python
ThirdPartyIntegrations(
  self,
  rancher='d3043820717d74d9a17694c176d39733',
  mesosphere='d3043820717d74d9a17694c176d39733',
  elastic_beanstalk='d3043820717d74d9a17694c176d39733',
  ecs='d3043820717d74d9a17694c176d39733',
  kubernetes='d3043820717d74d9a17694c176d39733',
  right_scale='d3043820717d74d9a17694c176d39733',
  ops_works='d3043820717d74d9a17694c176d39733',
  chef='d3043820717d74d9a17694c176d39733',
  code_deploy='d3043820717d74d9a17694c176d39733',
  nomad='d3043820717d74d9a17694c176d39733',
  docker_swarm='d3043820717d74d9a17694c176d39733',
  route53='d3043820717d74d9a17694c176d39733')
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
- __code_deploy__: CodeDeployConfiguration
- __nomad__: NomadConfiguration
- __docker_swarm__: DockerSwarmConfiguration
- __route53__: Route53Configuration

<h2 id="spotinst_sdk2.models.elastigroup.aws.Compute">Compute</h2>

```python
Compute(self,
        launch_specification='d3043820717d74d9a17694c176d39733',
        instance_types='d3043820717d74d9a17694c176d39733',
        product='d3043820717d74d9a17694c176d39733',
        availability_zones='d3043820717d74d9a17694c176d39733',
        elastic_ips='d3043820717d74d9a17694c176d39733',
        private_ips='d3043820717d74d9a17694c176d39733',
        subnet_ids='d3043820717d74d9a17694c176d39733',
        preferred_availability_zones='d3043820717d74d9a17694c176d39733')
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

<h2 id="spotinst_sdk2.models.elastigroup.aws.AvailabilityZone">AvailabilityZone</h2>

```python
AvailabilityZone(
  self,
  name='d3043820717d74d9a17694c176d39733',
  subnet_id='d3043820717d74d9a17694c176d39733',
  subnet_ids='d3043820717d74d9a17694c176d39733',
  placement_group_name='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __subnet_id__: str
- __subnet_ids__: list
- __placement_group_name__: str

<h2 id="spotinst_sdk2.models.elastigroup.aws.InstanceTypes">InstanceTypes</h2>

```python
InstanceTypes(self,
              ondemand='d3043820717d74d9a17694c176d39733',
              on_demand_types='d3043820717d74d9a17694c176d39733',
              spot='d3043820717d74d9a17694c176d39733',
              weights='d3043820717d74d9a17694c176d39733',
              preferred_spot='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __ondemand__: str
- __on_demand_types__: list[str]
- __spot__: list[str]
- __weights__: list[Weight]
- __preferred_spot__: list[str]

<h2 id="spotinst_sdk2.models.elastigroup.aws.Weight">Weight</h2>

```python
Weight(self,
       instance_type='d3043820717d74d9a17694c176d39733',
       weighted_capacity='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __instance_type__: str
- __weighted_capacity__: int

<h2 id="spotinst_sdk2.models.elastigroup.aws.TagSpecification">TagSpecification</h2>

```python
TagSpecification(self,
                 should_tag: bool = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __should_tag__: bool

<h2 id="spotinst_sdk2.models.elastigroup.aws.ResourceTagSpecification">ResourceTagSpecification</h2>

```python
ResourceTagSpecification(
  self,
  volumes: TagSpecification = 'd3043820717d74d9a17694c176d39733',
  snapshots: TagSpecification = 'd3043820717d74d9a17694c176d39733',
  enis: TagSpecification = 'd3043820717d74d9a17694c176d39733',
  amis: TagSpecification = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __volumes__: TagSpecification
- __snapshots__: TagSpecification
- __enis__: TagSpecification
- __amis__: TagSpecification

<h2 id="spotinst_sdk2.models.elastigroup.aws.LaunchSpecification">LaunchSpecification</h2>

```python
LaunchSpecification(
  self,
  security_group_ids='d3043820717d74d9a17694c176d39733',
  image_id='d3043820717d74d9a17694c176d39733',
  images='d3043820717d74d9a17694c176d39733',
  monitoring='d3043820717d74d9a17694c176d39733',
  credit_specification='d3043820717d74d9a17694c176d39733',
  health_check_type='d3043820717d74d9a17694c176d39733',
  load_balancers_config='d3043820717d74d9a17694c176d39733',
  health_check_grace_period='d3043820717d74d9a17694c176d39733',
  health_check_unhealthy_duration_before_replacement='d3043820717d74d9a17694c176d39733',
  ebs_optimized='d3043820717d74d9a17694c176d39733',
  tenancy='d3043820717d74d9a17694c176d39733',
  iam_role='d3043820717d74d9a17694c176d39733',
  key_pair='d3043820717d74d9a17694c176d39733',
  user_data='d3043820717d74d9a17694c176d39733',
  shutdown_script='d3043820717d74d9a17694c176d39733',
  block_device_mappings='d3043820717d74d9a17694c176d39733',
  network_interfaces='d3043820717d74d9a17694c176d39733',
  tags='d3043820717d74d9a17694c176d39733',
  resource_tag_specification='d3043820717d74d9a17694c176d39733',
  auto_healing='d3043820717d74d9a17694c176d39733',
  cpu_options='d3043820717d74d9a17694c176d39733',
  metadata_options='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __security_group_ids__: list[str]
- __credit_specification__: CreditSpecification
- __image_id__: str
- __images__: list[Image]
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
- __resource_tag_specification__: ResourceTagSpecification
- __auto_healing__: bool
- __cpu_options__: CpuOptions
- __metadata_options__: MetadataOptions

<h2 id="spotinst_sdk2.models.elastigroup.aws.CreditSpecification">CreditSpecification</h2>

```python
CreditSpecification(self,
                    cpu_credits='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __cpu_credits__: str

<h2 id="spotinst_sdk2.models.elastigroup.aws.Image">Image</h2>

```python
Image(self, id='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __id__: str

<h2 id="spotinst_sdk2.models.elastigroup.aws.LoadBalancersConfig">LoadBalancersConfig</h2>

```python
LoadBalancersConfig(self,
                    load_balancers='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __load_balancers__: list[LoadBalancer]

<h2 id="spotinst_sdk2.models.elastigroup.aws.LoadBalancer">LoadBalancer</h2>

```python
LoadBalancer(self,
             type='d3043820717d74d9a17694c176d39733',
             arn='d3043820717d74d9a17694c176d39733',
             name='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __type__: str
- __arn__: str
- __name__: str

<h2 id="spotinst_sdk2.models.elastigroup.aws.IamRole">IamRole</h2>

```python
IamRole(self,
        name='d3043820717d74d9a17694c176d39733',
        arn='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __arn__: str

<h2 id="spotinst_sdk2.models.elastigroup.aws.BlockDeviceMapping">BlockDeviceMapping</h2>

```python
BlockDeviceMapping(self,
                   device_name='d3043820717d74d9a17694c176d39733',
                   ebs='d3043820717d74d9a17694c176d39733',
                   no_device='d3043820717d74d9a17694c176d39733',
                   virtual_name='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __device_name__: str
- __ebs__: list[EBS]
- __no_device__: bool
- __virtual_name__: str

<h2 id="spotinst_sdk2.models.elastigroup.aws.EBS">EBS</h2>

```python
EBS(self,
    delete_on_termination='d3043820717d74d9a17694c176d39733',
    encrypted='d3043820717d74d9a17694c176d39733',
    iops='d3043820717d74d9a17694c176d39733',
    snapshot_id='d3043820717d74d9a17694c176d39733',
    volume_size='d3043820717d74d9a17694c176d39733',
    volume_type='d3043820717d74d9a17694c176d39733',
    kms_key_id='d3043820717d74d9a17694c176d39733',
    dynamic_volume_size='d3043820717d74d9a17694c176d39733',
    throughput='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __delete_on_termination__: bool
- __encrypted__: bool
- __iops__: int
- __snapshot_id__: str
- __volume_size__: int
- __volume_type__: str
- __kms_key_id__: str
- __dynamic_volume_size__: DynamicVolumeSize
- __throughput__: int

<h2 id="spotinst_sdk2.models.elastigroup.aws.DynamicVolumeSize">DynamicVolumeSize</h2>

```python
DynamicVolumeSize(
  self,
  base_size='d3043820717d74d9a17694c176d39733',
  resource='d3043820717d74d9a17694c176d39733',
  size_per_resource_unit='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __base_size__: int
- __resource__: str
- __size_per_resource_unit__: int

<h2 id="spotinst_sdk2.models.elastigroup.aws.Tag">Tag</h2>

```python
Tag(self,
    tag_key='d3043820717d74d9a17694c176d39733',
    tag_value='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __tag_key__: str
- __tag_value__: str

<h2 id="spotinst_sdk2.models.elastigroup.aws.NetworkInterface">NetworkInterface</h2>

```python
NetworkInterface(
  self,
  delete_on_termination='d3043820717d74d9a17694c176d39733',
  device_index='d3043820717d74d9a17694c176d39733',
  description='d3043820717d74d9a17694c176d39733',
  secondary_private_ip_address_count='d3043820717d74d9a17694c176d39733',
  associate_public_ip_address='d3043820717d74d9a17694c176d39733',
  groups='d3043820717d74d9a17694c176d39733',
  network_interface_id='d3043820717d74d9a17694c176d39733',
  private_ip_address='d3043820717d74d9a17694c176d39733',
  private_ip_addresses='d3043820717d74d9a17694c176d39733',
  subnet_id='d3043820717d74d9a17694c176d39733',
  associate_ipv6_address='d3043820717d74d9a17694c176d39733')
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

<h2 id="spotinst_sdk2.models.elastigroup.aws.PrivateIpAddress">PrivateIpAddress</h2>

```python
PrivateIpAddress(self,
                 private_ip_address='d3043820717d74d9a17694c176d39733',
                 primary='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __private_ip_address__: str
- __primary__: bool

<h2 id="spotinst_sdk2.models.elastigroup.aws.CpuOptions">CpuOptions</h2>

```python
CpuOptions(self, threads_per_core='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __threads_per_core__: int

<h2 id="spotinst_sdk2.models.elastigroup.aws.MetadataOptions">MetadataOptions</h2>

```python
MetadataOptions(
  self,
  http_put_response_hop_limit='d3043820717d74d9a17694c176d39733',
  http_tokens='d3043820717d74d9a17694c176d39733',
  instance_metadata_tags='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __http_put_response_hop_limit__: int
- __http_tokens__: str
- __instance_metadata_tags__: str

<h2 id="spotinst_sdk2.models.elastigroup.aws.Roll">Roll</h2>

```python
Roll(self,
     batch_size_percentage='d3043820717d74d9a17694c176d39733',
     grace_period='d3043820717d74d9a17694c176d39733',
     health_check_type='d3043820717d74d9a17694c176d39733',
     strategy='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __batch_size_percentage__: str
- __grace_period__: xstr
- __health_check_type__: str
- __strategy__: RollStrategy

<h2 id="spotinst_sdk2.models.elastigroup.aws.RollStrategy">RollStrategy</h2>

```python
RollStrategy(
  self,
  action='d3043820717d74d9a17694c176d39733',
  should_drain_instances='d3043820717d74d9a17694c176d39733',
  batch_min_healthy_percentage='d3043820717d74d9a17694c176d39733',
  on_failure='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __action__: str,
- __should_drain_instances__: bool,
- __batch_min_healthy_percentage__: int,
- __on_failure__: OnFailure

<h2 id="spotinst_sdk2.models.elastigroup.aws.OnFailure">OnFailure</h2>

```python
OnFailure(
  self,
  action_type='d3043820717d74d9a17694c176d39733',
  should_handle_all_batches='d3043820717d74d9a17694c176d39733',
  batch_num='d3043820717d74d9a17694c176d39733',
  draining_timeout='d3043820717d74d9a17694c176d39733',
  should_decrement_target_capacity='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __action_type__: str
- __should_handle_all_batches__: bool
- __batch_num__: int
- __draining_timeout__: int
- __should_decrement_target_capacity__: bool

<h2 id="spotinst_sdk2.models.elastigroup.aws.DetachConfiguration">DetachConfiguration</h2>

```python
DetachConfiguration(
  self,
  instances_to_detach='d3043820717d74d9a17694c176d39733',
  should_terminate_instances='d3043820717d74d9a17694c176d39733',
  draining_timeout='d3043820717d74d9a17694c176d39733',
  should_decrement_target_capacity='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __instances_to_detach__: list[str]
- __should_terminate_instances__: bool
- __draining_timeout__: int
- __should_decrement_target_capacity__: bool

<h2 id="spotinst_sdk2.models.elastigroup.aws.StatefulDeallocation">StatefulDeallocation</h2>

```python
StatefulDeallocation(
  self,
  should_delete_images='d3043820717d74d9a17694c176d39733',
  should_delete_network_interfaces='d3043820717d74d9a17694c176d39733',
  should_delete_volumes='d3043820717d74d9a17694c176d39733',
  should_delete_snapshots='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __should_delete_images__: bool
- __should_delete_network_interfaces__: bool
- __should_delete_volumes__: bool
- __should_delete_snapshots__: bool

<h1 id="spotinst_sdk2.models.elastigroup.aws.asg">spotinst_sdk2.models.elastigroup.aws.asg</h1>


<h2 id="spotinst_sdk2.models.elastigroup.aws.asg.ASG">ASG</h2>

```python
ASG(self,
    product='d3043820717d74d9a17694c176d39733',
    spot_instance_types='d3043820717d74d9a17694c176d39733',
    name='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __product__: str
- __spot_instance_types__: List[str]
- __name__: str

<h1 id="spotinst_sdk2.models.elastigroup.aws.deployment">spotinst_sdk2.models.elastigroup.aws.deployment</h1>


<h2 id="spotinst_sdk2.models.elastigroup.aws.deployment.BlueGreenDeployment">BlueGreenDeployment</h2>

```python
BlueGreenDeployment(
  self,
  timeout='d3043820717d74d9a17694c176d39733',
  tags='d3043820717d74d9a17694c176d39733',
  deployment_groups='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __timeout__: int
- __tags__: List[Tag]
- __deployment_groups__: List[DeploymentGroup]

<h2 id="spotinst_sdk2.models.elastigroup.aws.deployment.Tag">Tag</h2>

```python
Tag(self,
    tag_key='d3043820717d74d9a17694c176d39733',
    tag_value='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __tag_get__: str
- __tag_value__: str

<h2 id="spotinst_sdk2.models.elastigroup.aws.deployment.DeploymentGroup">DeploymentGroup</h2>

```python
DeploymentGroup(
  self,
  application_name='d3043820717d74d9a17694c176d39733',
  deployment_group_name='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __application_name__: str
- __deployment_group_name__: str

<h1 id="spotinst_sdk2.models.elastigroup.aws.deployment_action">spotinst_sdk2.models.elastigroup.aws.deployment_action</h1>


<h2 id="spotinst_sdk2.models.elastigroup.aws.deployment_action.DeploymentAction">DeploymentAction</h2>

```python
DeploymentAction(
  self,
  action_type='d3043820717d74d9a17694c176d39733',
  should_handle_all_batches='d3043820717d74d9a17694c176d39733',
  draining_timeout='d3043820717d74d9a17694c176d39733',
  should_decrement_target_capacity='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __action_type__: str
- __should_handle_all_batches__: bool
- __draining_timeout__: int
- __should_decrement_target_capacity__: bool

<h1 id="spotinst_sdk2.models.elastigroup.aws.stateful">spotinst_sdk2.models.elastigroup.aws.stateful</h1>


<h2 id="spotinst_sdk2.models.elastigroup.aws.stateful.StatefulInstance">StatefulInstance</h2>

```python
StatefulInstance(
  self,
  should_keep_private_ip='d3043820717d74d9a17694c176d39733',
  original_instance_id='d3043820717d74d9a17694c176d39733',
  name='d3043820717d74d9a17694c176d39733',
  product='d3043820717d74d9a17694c176d39733',
  spot_instance_types='d3043820717d74d9a17694c176d39733',
  region='d3043820717d74d9a17694c176d39733',
  availability_zones='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __shouldKeepPrivateIp__: bool
- __originalInstanceId__: str
- __name__: str
- __product__: str
- __spotInstanceTypes__: List[str]
- __region__: str
- __availabilityZones__: List[AvailabiltyZones]

<h2 id="spotinst_sdk2.models.elastigroup.aws.stateful.AvailabilityZone">AvailabilityZone</h2>

```python
AvailabilityZone(self,
                 name='d3043820717d74d9a17694c176d39733',
                 subnet_ids='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __subnet__: str

