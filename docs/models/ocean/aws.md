<h1 id="spotinst_sdk2.models.ocean.aws">spotinst_sdk2.models.ocean.aws</h1>


<h2 id="spotinst_sdk2.models.ocean.aws.Ocean">Ocean</h2>

```python
Ocean(self,
      name='d3043820717d74d9a17694c176d39733',
      controller_cluster_id='d3043820717d74d9a17694c176d39733',
      region='d3043820717d74d9a17694c176d39733',
      auto_scaler='d3043820717d74d9a17694c176d39733',
      capacity='d3043820717d74d9a17694c176d39733',
      strategy='d3043820717d74d9a17694c176d39733',
      compute='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __controller_cluster_id__: str
- __region__: str
- __auto_scaler__: AutoScaler
- __capacity__: Capacity
- __strategy__: Strategy
- __compute__: Compute

<h2 id="spotinst_sdk2.models.ocean.aws.AutoScaler">AutoScaler</h2>

```python
AutoScaler(self,
           is_enabled='d3043820717d74d9a17694c176d39733',
           cooldown='d3043820717d74d9a17694c176d39733',
           resource_limits='d3043820717d74d9a17694c176d39733',
           down='d3043820717d74d9a17694c176d39733',
           headroom='d3043820717d74d9a17694c176d39733',
           is_auto_config='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __is_enabled__: bool
- __cooldown__: int
- __resource_limits__: ResourceLimits
- __down__: Down
- __headroom__: Headroom
- __is_auto_config__: bool

<h2 id="spotinst_sdk2.models.ocean.aws.ResourceLimits">ResourceLimits</h2>

```python
ResourceLimits(self,
               max_memory_gib='d3043820717d74d9a17694c176d39733',
               max_vCpu='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __max_memory_gib__: nint
- __max_vCpu__: int

<h2 id="spotinst_sdk2.models.ocean.aws.Down">Down</h2>

```python
Down(self, evaluation_periods='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __evaluation_periods__: int

<h2 id="spotinst_sdk2.models.ocean.aws.Headroom">Headroom</h2>

```python
Headroom(self,
         cpu_per_unit='d3043820717d74d9a17694c176d39733',
         memory_per_unit='d3043820717d74d9a17694c176d39733',
         num_of_units='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __cpu_per_unit__: int
- __memory_per_unit__: int
- __num_of_units__: int

<h2 id="spotinst_sdk2.models.ocean.aws.Capacity">Capacity</h2>

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

<h2 id="spotinst_sdk2.models.ocean.aws.Strategy">Strategy</h2>

```python
Strategy(self,
         utilize_reserved_instances='d3043820717d74d9a17694c176d39733',
         fallback_to_od='d3043820717d74d9a17694c176d39733',
         spot_percentage='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __utilize_reserved_instances__: bool
- __fallback_to_od__: bool
- __spot_percentage__: int

<h2 id="spotinst_sdk2.models.ocean.aws.Compute">Compute</h2>

```python
Compute(self,
        instance_types='d3043820717d74d9a17694c176d39733',
        subnet_ids='d3043820717d74d9a17694c176d39733',
        launch_specification='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __instance_types__: InstanceTypes
- __subnet_ids__: List[str]
- __launch_specification__: LaunchSpecifications

<h2 id="spotinst_sdk2.models.ocean.aws.InstanceTypes">InstanceTypes</h2>

```python
InstanceTypes(self,
              whitelist='d3043820717d74d9a17694c176d39733',
              blacklist='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __whitelist__: List[str]
- __blacklist__: List[str]

<h2 id="spotinst_sdk2.models.ocean.aws.LaunchSpecifications">LaunchSpecifications</h2>

```python
LaunchSpecifications(
  self,
  security_group_ids='d3043820717d74d9a17694c176d39733',
  image_id='d3043820717d74d9a17694c176d39733',
  iam_instance_profile='d3043820717d74d9a17694c176d39733',
  key_pair='d3043820717d74d9a17694c176d39733',
  user_data='d3043820717d74d9a17694c176d39733',
  tags='d3043820717d74d9a17694c176d39733',
  load_balancers='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __security_group_ids__: List[str]
- __image_id__: str
- __iam_instance_profile__: IamInstanceProfile
- __key_pair__: str
- __user_data__: str
- __tags__: List[Tag]
- __load_balancers__: List[LoadBalancer]

<h2 id="spotinst_sdk2.models.ocean.aws.IamInstanceProfile">IamInstanceProfile</h2>

```python
IamInstanceProfile(self,
                   arn='d3043820717d74d9a17694c176d39733',
                   name='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __arn__: str
- __name__: str

<h2 id="spotinst_sdk2.models.ocean.aws.Tag">Tag</h2>

```python
Tag(self,
    tag_key='d3043820717d74d9a17694c176d39733',
    tag_value='d3043820717d74d9a17694c176d39733')
```

__Argument__

tag_key: str
tag_value: str

<h2 id="spotinst_sdk2.models.ocean.aws.LoadBalancer">LoadBalancer</h2>

```python
LoadBalancer(self,
             arn='d3043820717d74d9a17694c176d39733',
             name='d3043820717d74d9a17694c176d39733',
             lb_type='d3043820717d74d9a17694c176d39733')
```

__Argument__

arn:  str
name: str
type: str

