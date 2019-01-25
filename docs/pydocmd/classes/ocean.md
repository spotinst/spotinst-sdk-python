<h1 id="spotinst_sdk.spotinst_ocean.Ocean">Ocean</h1>

```python
Ocean(self, name='d3043820717d74d9a17694c176d39733', controller_cluster_id='d3043820717d74d9a17694c176d39733', region='d3043820717d74d9a17694c176d39733', auto_scaler='d3043820717d74d9a17694c176d39733', capacity='d3043820717d74d9a17694c176d39733', strategy='d3043820717d74d9a17694c176d39733', compute='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __controller_cluster_id__: str
- __region__: str
- __auto_scaler__: AutoScaler
- __capacity__: Capacity
- __strategy__: Strategy
- __compute__: Compute

<h1 id="spotinst_sdk.spotinst_ocean.AutoScaler">AutoScaler</h1>

```python
AutoScaler(self, is_enabled='d3043820717d74d9a17694c176d39733', cooldown='d3043820717d74d9a17694c176d39733', resource_limits='d3043820717d74d9a17694c176d39733', down='d3043820717d74d9a17694c176d39733', headroom='d3043820717d74d9a17694c176d39733', is_auto_config='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __is_enabled__: bool
- __cooldown__: int
- __resource_limits__: ResourceLimits
- __down__: Down
- __headroom__: Headroom
- __is_auto_config__: bool

<h1 id="spotinst_sdk.spotinst_ocean.ResourceLimits">ResourceLimits</h1>

```python
ResourceLimits(self, max_memory_gib='d3043820717d74d9a17694c176d39733', max_vCpu='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __max_memory_gib__: nint
- __max_vCpu__: int

<h1 id="spotinst_sdk.spotinst_ocean.Down">Down</h1>

```python
Down(self, evaluation_periods='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __evaluation_periods__: int

<h1 id="spotinst_sdk.spotinst_ocean.Headroom">Headroom</h1>

```python
Headroom(self, cpu_per_unit='d3043820717d74d9a17694c176d39733', memory_per_unit='d3043820717d74d9a17694c176d39733', num_of_units='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __cpu_per_unit__: int
- __memory_per_unit__: int
- __num_of_units__: int

<h1 id="spotinst_sdk.spotinst_ocean.Capacity">Capacity</h1>

```python
Capacity(self, minimum='d3043820717d74d9a17694c176d39733', maximum='d3043820717d74d9a17694c176d39733', target='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __minimum__: int
- __maximum__: int
- __target__: int

<h1 id="spotinst_sdk.spotinst_ocean.Strategy">Strategy</h1>

```python
Strategy(self, utilize_reserved_instances='d3043820717d74d9a17694c176d39733', fallback_to_od='d3043820717d74d9a17694c176d39733', spot_percentage='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __utilize_reserved_instances__: bool
- __fallback_to_od__: bool
- __spot_percentage__: int

<h1 id="spotinst_sdk.spotinst_ocean.Compute">Compute</h1>

```python
Compute(self, instance_types='d3043820717d74d9a17694c176d39733', subnet_ids='d3043820717d74d9a17694c176d39733', launch_specification='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __instance_types__: InstanceTypes
- __subnet_ids__: List[str]
- __launch_specification__: LaunchSpecifications

<h1 id="spotinst_sdk.spotinst_ocean.InstanceTypes">InstanceTypes</h1>

```python
InstanceTypes(self, whitelist='d3043820717d74d9a17694c176d39733', blacklist='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __whitelist__: List[str]
- __blacklist__: List[str]

<h1 id="spotinst_sdk.spotinst_ocean.LaunchSpecifications">LaunchSpecifications</h1>

```python
LaunchSpecifications(self, security_group_ids='d3043820717d74d9a17694c176d39733', image_id='d3043820717d74d9a17694c176d39733', iam_instance_profile='d3043820717d74d9a17694c176d39733', key_pair='d3043820717d74d9a17694c176d39733', user_data='d3043820717d74d9a17694c176d39733', tags='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __security_group_ids__: List[str]
- __image_id__: str
- __iam_instance_profile__: IamInstanceProfile
- __key_pair__: str
- __user_data__: str
- __tags__: List[Tag]

<h1 id="spotinst_sdk.spotinst_ocean.IamInstanceProfile">IamInstanceProfile</h1>

```python
IamInstanceProfile(self, arn='d3043820717d74d9a17694c176d39733', name='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __arn__: str
- __name__: str

<h1 id="spotinst_sdk.spotinst_ocean.Tag">Tag</h1>

```python
Tag(self, tag_key='d3043820717d74d9a17694c176d39733', tag_value='d3043820717d74d9a17694c176d39733')
```

__Argument__

tag_key: str
tag_value: str

