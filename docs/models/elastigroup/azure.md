<h1 id="spotinst_sdk2.models.elastigroup.azure">spotinst_sdk2.models.elastigroup.azure</h1>


<h2 id="spotinst_sdk2.models.elastigroup.azure.Elastigroup">Elastigroup</h2>

```python
Elastigroup(
  self,
  name='d3043820717d74d9a17694c176d39733',
  region='d3043820717d74d9a17694c176d39733',
  resource_group_name='d3043820717d74d9a17694c176d39733',
  capacity='d3043820717d74d9a17694c176d39733',
  strategy='d3043820717d74d9a17694c176d39733',
  compute='d3043820717d74d9a17694c176d39733',
  scaling='d3043820717d74d9a17694c176d39733',
  scheduling='d3043820717d74d9a17694c176d39733',
  third_parties_integration='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __region__: str
- __resource_group_name__: str
- __capacity__: Capacity
- __strategy__: Strategy
- __compute__: Compute
- __scaling__: Scaling
- __scheduling__: Scheduling
- __third_parties_integration__: ThirdPartiesIntegration

<h2 id="spotinst_sdk2.models.elastigroup.azure.Capacity">Capacity</h2>

```python
Capacity(self,
         minimum='d3043820717d74d9a17694c176d39733',
         maximum='d3043820717d74d9a17694c176d39733',
         target='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __minimum__: int
- __maximum__: int
- __target__: int

<h2 id="spotinst_sdk2.models.elastigroup.azure.Strategy">Strategy</h2>

```python
Strategy(self,
         low_priority_percentage='d3043820717d74d9a17694c176d39733',
         on_demand_count='d3043820717d74d9a17694c176d39733',
         draining_timeout='d3043820717d74d9a17694c176d39733')
```

__Arugments__

low_priority_percentage: int
on_demand_count: int
draining_timeout: int

<h2 id="spotinst_sdk2.models.elastigroup.azure.Compute">Compute</h2>

```python
Compute(self,
        vm_sizes='d3043820717d74d9a17694c176d39733',
        product='d3043820717d74d9a17694c176d39733',
        health='d3043820717d74d9a17694c176d39733',
        launch_specification='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __vm_sizes__: VmSizes
- __product__: str
- __health__: Health
- __launch_specification__: LaunchSpecification

<h2 id="spotinst_sdk2.models.elastigroup.azure.VmSizes">VmSizes</h2>

```python
VmSizes(self,
        od_sizes='d3043820717d74d9a17694c176d39733',
        low_priority_sizes='d3043820717d74d9a17694c176d39733')
```

#Arguments
od_sizes: list[str]
low_priority_sizes: list[str]

<h2 id="spotinst_sdk2.models.elastigroup.azure.Health">Health</h2>

```python
Health(self,
       health_check_type='d3043820717d74d9a17694c176d39733',
       auto_healing='d3043820717d74d9a17694c176d39733',
       grace_period='d3043820717d74d9a17694c176d39733')
```

#Arguments
health_check_type: str
auto_healing: bool
grace_period: int

<h2 id="spotinst_sdk2.models.elastigroup.azure.LaunchSpecification">LaunchSpecification</h2>

```python
LaunchSpecification(
  self,
  image='d3043820717d74d9a17694c176d39733',
  network='d3043820717d74d9a17694c176d39733',
  login='d3043820717d74d9a17694c176d39733',
  user_data='d3043820717d74d9a17694c176d39733',
  shutdown_script='d3043820717d74d9a17694c176d39733',
  custom_data='d3043820717d74d9a17694c176d39733',
  load_balancers_config='d3043820717d74d9a17694c176d39733',
  tags='d3043820717d74d9a17694c176d39733',
  extensions='d3043820717d74d9a17694c176d39733',
  managed_service_identities='d3043820717d74d9a17694c176d39733')
```

#Arguments
image: Image
network: Network
login: Login
user_data: str
shutdown_script: str
custom_data: str
load_balancers_config: LoadBalancerConfig
tags: list[Tag]
extensions: list[Extension]
managed_service_identities: list[ManagedServiceIdentity]

<h2 id="spotinst_sdk2.models.elastigroup.azure.Image">Image</h2>

```python
Image(self,
      marketplace='d3043820717d74d9a17694c176d39733',
      custom='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __marketplace__: Marketplace
- __custom__: Custom

<h2 id="spotinst_sdk2.models.elastigroup.azure.Marketplace">Marketplace</h2>

```python
Marketplace(self,
            publisher='d3043820717d74d9a17694c176d39733',
            offer='d3043820717d74d9a17694c176d39733',
            sku='d3043820717d74d9a17694c176d39733',
            version='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __publisher__: str
- __offer__: str
- __sku__: str
- __version__: str

<h2 id="spotinst_sdk2.models.elastigroup.azure.Custom">Custom</h2>

```python
Custom(self,
       resource_group_name='d3043820717d74d9a17694c176d39733',
       image_name='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __resource_group_name__: str
- __image_name__: str

<h2 id="spotinst_sdk2.models.elastigroup.azure.Network">Network</h2>

```python
Network(self,
        virtual_network_name='d3043820717d74d9a17694c176d39733',
        subnet_name='d3043820717d74d9a17694c176d39733',
        resource_group_name='d3043820717d74d9a17694c176d39733',
        assign_public_ip='d3043820717d74d9a17694c176d39733',
        additional_ip_configurations='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __virtual_network_name__: str
- __subnet_name__: str
- __resource_group_name__: str
- __assign_public_ip__: bool
- __additional_ip_configurations__: list[AdditionalIpConfiguration]

<h2 id="spotinst_sdk2.models.elastigroup.azure.AdditionalIpConfiguration">AdditionalIpConfiguration</h2>

```python
AdditionalIpConfiguration(
  self,
  name='d3043820717d74d9a17694c176d39733',
  private_ip_address_version='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __private_ip_address_version__: str

<h2 id="spotinst_sdk2.models.elastigroup.azure.Login">Login</h2>

```python
Login(self,
      ssh_public_key='d3043820717d74d9a17694c176d39733',
      user_name='d3043820717d74d9a17694c176d39733',
      password='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __ssh_public_key__: str
- __user_name__: str
- __password__: str

<h2 id="spotinst_sdk2.models.elastigroup.azure.LoadBalancerConfig">LoadBalancerConfig</h2>

```python
LoadBalancerConfig(self,
                   load_balancers='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __load_balancers__: list[LoadBalancer]

<h2 id="spotinst_sdk2.models.elastigroup.azure.LoadBalancer">LoadBalancer</h2>

```python
LoadBalancer(self,
             balancer_id='d3043820717d74d9a17694c176d39733',
             target_set_id='d3043820717d74d9a17694c176d39733',
             auto_weight='d3043820717d74d9a17694c176d39733',
             resource_group_name='d3043820717d74d9a17694c176d39733',
             application_gateway_name='d3043820717d74d9a17694c176d39733',
             backend_pool_name='d3043820717d74d9a17694c176d39733',
             balancer_type='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __balancer_id__: str
- __target_set_id__: str
- __auto_weight__: bool
- __resource_group_name__: str
- __application_gateway_name__: str
- __backend_pool_name__: str
- __balancer_type__: str

<h2 id="spotinst_sdk2.models.elastigroup.azure.Tag">Tag</h2>

```python
Tag(self,
    tag_key='d3043820717d74d9a17694c176d39733',
    tag_value='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __tag_key__: str
- __tag_value__: str

<h2 id="spotinst_sdk2.models.elastigroup.azure.Extension">Extension</h2>

```python
Extension(self,
          auto_upgrade_minor_version='d3043820717d74d9a17694c176d39733',
          name='d3043820717d74d9a17694c176d39733',
          publisher='d3043820717d74d9a17694c176d39733',
          extension_type='d3043820717d74d9a17694c176d39733',
          type_handler_version='d3043820717d74d9a17694c176d39733',
          protected_settings='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __auto_upgrade_minor_version__: bool
- __name__: str
- __publisher__: str
- __extension_type__: str
- __type_handler_version__: str
- __protected_settings__: ProtectedSettings

<h2 id="spotinst_sdk2.models.elastigroup.azure.ProtectedSettings">ProtectedSettings</h2>

```python
ProtectedSettings(self,
                  command_to_execute='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __command_to_execute__: str

<h2 id="spotinst_sdk2.models.elastigroup.azure.ManagedServiceIdentity">ManagedServiceIdentity</h2>

```python
ManagedServiceIdentity(
  self,
  resource_group_name='d3043820717d74d9a17694c176d39733',
  name='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __resource_group_name__: str
- __name__: str

<h2 id="spotinst_sdk2.models.elastigroup.azure.Scaling">Scaling</h2>

```python
Scaling(self,
        up='d3043820717d74d9a17694c176d39733',
        down='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __up__:  list[ScalingPolicy]
- __down__: list[ScalingPolicy]

<h2 id="spotinst_sdk2.models.elastigroup.azure.ScalingPolicy">ScalingPolicy</h2>

```python
ScalingPolicy(self,
              policy_name='d3043820717d74d9a17694c176d39733',
              namespace='d3043820717d74d9a17694c176d39733',
              metric_name='d3043820717d74d9a17694c176d39733',
              dimensions='d3043820717d74d9a17694c176d39733',
              statistic='d3043820717d74d9a17694c176d39733',
              unit='d3043820717d74d9a17694c176d39733',
              threshold='d3043820717d74d9a17694c176d39733',
              adjustment='d3043820717d74d9a17694c176d39733',
              min_target_capacity='d3043820717d74d9a17694c176d39733',
              period='d3043820717d74d9a17694c176d39733',
              evaluation_periods='d3043820717d74d9a17694c176d39733',
              cooldown='d3043820717d74d9a17694c176d39733',
              action='d3043820717d74d9a17694c176d39733',
              operator='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __policy_name__: str
- __namespace__: str
- __metric_name__: str
- __dimensions__: list[ScalingPolicyDimension]
- __statistic__: str
- __unit__: str
- __threshold__: float
- __adjustment__: int
- __min_target_capacity__: int
- __period__: int
- __evaluation_periods__: int
- __cooldown__: int
- __action__: ScalingPolicyAction
- __operator__: str

<h2 id="spotinst_sdk2.models.elastigroup.azure.ScalingPolicyDimension">ScalingPolicyDimension</h2>

```python
ScalingPolicyDimension(self,
                       name='d3043820717d74d9a17694c176d39733',
                       value='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __value__: str

<h2 id="spotinst_sdk2.models.elastigroup.azure.ScalingPolicyAction">ScalingPolicyAction</h2>

```python
ScalingPolicyAction(
  self,
  scaling_type='d3043820717d74d9a17694c176d39733',
  adjustment='d3043820717d74d9a17694c176d39733',
  min_target_capacity='d3043820717d74d9a17694c176d39733',
  target='d3043820717d74d9a17694c176d39733',
  maximum='d3043820717d74d9a17694c176d39733',
  minimum='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __scaling_type__: str
- __adjustment__: int
- __min_target_capacity__: int
- __target__: int
- __maximum__: int
- __minimum__: int

<h2 id="spotinst_sdk2.models.elastigroup.azure.Scheduling">Scheduling</h2>

```python
Scheduling(self, tasks='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __tasks__: list[SchedulingTask]

<h2 id="spotinst_sdk2.models.elastigroup.azure.SchedulingTask">SchedulingTask</h2>

```python
SchedulingTask(self,
               is_enabled='d3043820717d74d9a17694c176d39733',
               cron_expression='d3043820717d74d9a17694c176d39733',
               task_type='d3043820717d74d9a17694c176d39733',
               scale_target_capacity='d3043820717d74d9a17694c176d39733',
               scale_min_capacity='d3043820717d74d9a17694c176d39733',
               scale_max_capacity='d3043820717d74d9a17694c176d39733',
               batch_size_percentage='d3043820717d74d9a17694c176d39733',
               grace_period='d3043820717d74d9a17694c176d39733',
               adjustment='d3043820717d74d9a17694c176d39733',
               adjustment_percentage='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __is_enabled__: bool
- __cron_expression__: str
- __task_type__: str
- __scale_target_capacity__: int
- __scale_min_capacity__: int
- __scale_max_capacity__: int
- __batch_size_percentage__: int
- __grace_period__: int
- __adjustment__: int
- __adjustment_percentage__: int

<h2 id="spotinst_sdk2.models.elastigroup.azure.ThirdPartiesIntegration">ThirdPartiesIntegration</h2>

```python
ThirdPartiesIntegration(
  self,
  mlb_runtime='d3043820717d74d9a17694c176d39733',
  kubernetes='d3043820717d74d9a17694c176d39733',
  hpc_grid_engine='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __mlb_runtime__: MlbRuntime
- __kubernetes__: Kubernetes
- __hpc_grid_engine__: HpcGridEngine

<h2 id="spotinst_sdk2.models.elastigroup.azure.MlbRuntime">MlbRuntime</h2>

```python
MlbRuntime(self, deployment_id='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __deployment_id__: str

<h2 id="spotinst_sdk2.models.elastigroup.azure.Kubernetes">Kubernetes</h2>

```python
Kubernetes(self, cluster_identifier='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __cluster_identifier__: str

<h2 id="spotinst_sdk2.models.elastigroup.azure.HpcGridEngine">HpcGridEngine</h2>

```python
HpcGridEngine(self,
              cluster_id='d3043820717d74d9a17694c176d39733',
              queues='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __cluster_id__: str
- __queues__: List[str]

<h2 id="spotinst_sdk2.models.elastigroup.azure.RollGroup">RollGroup</h2>

```python
RollGroup(self,
          batch_size_percentage='d3043820717d74d9a17694c176d39733',
          grace_period='d3043820717d74d9a17694c176d39733',
          health_check_type='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __batch_size_percentage__: int
- __grace_period__: int
- __health_check_type__: str

<h2 id="spotinst_sdk2.models.elastigroup.azure.DetachConfiguration">DetachConfiguration</h2>

```python
DetachConfiguration(
  self,
  instances_to_detach='d3043820717d74d9a17694c176d39733',
  draining_timeout='d3043820717d74d9a17694c176d39733',
  should_decrement_target_capacity='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __instances_to_detach__: list[str]
- __draining_timeout__: int
- __should_decrement_target_capacity__: bool

<h1 id="spotinst_sdk2.models.elastigroup.azure.task">spotinst_sdk2.models.elastigroup.azure.task</h1>


<h2 id="spotinst_sdk2.models.elastigroup.azure.task.Task">Task</h2>

```python
Task(self,
     name='d3043820717d74d9a17694c176d39733',
     description='d3043820717d74d9a17694c176d39733',
     state='d3043820717d74d9a17694c176d39733',
     policies='d3043820717d74d9a17694c176d39733',
     instances='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __description__: str
- __state__: str
- __policies__: list[Policy]
- __instances__: list[Instance]

<h2 id="spotinst_sdk2.models.elastigroup.azure.task.Policy">Policy</h2>

```python
Policy(self,
       cron='d3043820717d74d9a17694c176d39733',
       action='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __cron__: str
- __action__: str

<h2 id="spotinst_sdk2.models.elastigroup.azure.task.Instance">Instance</h2>

```python
Instance(self,
         vm_name='d3043820717d74d9a17694c176d39733',
         resource_group_name='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __vm_name__: str
- __resource_group_name__: str

