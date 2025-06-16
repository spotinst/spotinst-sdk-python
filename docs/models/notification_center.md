<h1 id="spotinst_sdk2.models.notification_center.notification_center">spotinst_sdk2.models.notification_center.notification_center</h1>


<h2 id="spotinst_sdk2.models.notification_center.notification_center.FilterConditions">FilterConditions</h2>

```python
FilterConditions(self,
                 identifier: str = 'd3043820717d74d9a17694c176d39733',
                 operator: str = 'd3043820717d74d9a17694c176d39733',
                 expression: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __identifier__: str
- __operator__: str
- __expression__: str

<h2 id="spotinst_sdk2.models.notification_center.notification_center.DynamicRules">DynamicRules</h2>

```python
DynamicRules(
    self,
    filterConditions:
    typing.List[spotinst_sdk2.models.notification_center.notification_center.FilterConditions] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __filterConditions__: List[FilterConditions]

<h2 id="spotinst_sdk2.models.notification_center.notification_center.Events">Events</h2>

```python
Events(self,
       event: str = 'd3043820717d74d9a17694c176d39733',
       type: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __event__: str
- __type__: str

<h2 id="spotinst_sdk2.models.notification_center.notification_center.ComputePolicyConfig">ComputePolicyConfig</h2>

```python
ComputePolicyConfig(
    self,
    events:
    typing.List[spotinst_sdk2.models.notification_center.notification_center.Events] = 'd3043820717d74d9a17694c176d39733',
    shouldIncludeAllResources: bool = 'd3043820717d74d9a17694c176d39733',
    resourceIds: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
    dynamicRules:
    typing.List[spotinst_sdk2.models.notification_center.notification_center.DynamicRules] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __events__: List[Events]
- __shouldIncludeAllResources__: bool
- __resourceIds__: List[str]
- __dynamicRules__: List[DynamicRules]

<h2 id="spotinst_sdk2.models.notification_center.notification_center.RegisteredUsers">RegisteredUsers</h2>

```python
RegisteredUsers(
  self,
  userEmail: str = 'd3043820717d74d9a17694c176d39733',
  subscriptionTypes: typing.List[str] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __subscriptionTypes__: List[str]
- __userEmail__: str

<h2 id="spotinst_sdk2.models.notification_center.notification_center.Subscriptions">Subscriptions</h2>

```python
Subscriptions(self,
              type: str = 'd3043820717d74d9a17694c176d39733',
              endpoint: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __type__: str
- __endpoint__: str

<h2 id="spotinst_sdk2.models.notification_center.notification_center.Policy">Policy</h2>

```python
Policy(
    self,
    description: str = 'd3043820717d74d9a17694c176d39733',
    name: str = 'd3043820717d74d9a17694c176d39733',
    privacyLevel: str = 'd3043820717d74d9a17694c176d39733',
    isActive: bool = 'd3043820717d74d9a17694c176d39733',
    registeredUsers:
    typing.List[spotinst_sdk2.models.notification_center.notification_center.RegisteredUsers] = 'd3043820717d74d9a17694c176d39733',
    subscriptions:
    typing.List[spotinst_sdk2.models.notification_center.notification_center.Subscriptions] = 'd3043820717d74d9a17694c176d39733',
    computePolicyConfig:
    typing.List[spotinst_sdk2.models.notification_center.notification_center.ComputePolicyConfig] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __name__: str
- __description__: str
- __privacyLevel__: str
- __isActive__: bool
- __registeredUsers__: List[RegisteredUsers]
- __subscriptions__: List[Subscriptions]
- __computePolicyConfig__: List[ComputePolicyConfig]

