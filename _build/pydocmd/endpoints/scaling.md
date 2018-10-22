<h1 id="spotinst_sdk.SpotinstClient.scale_elastigroup_up">scale_elastigroup_up</h1>

```python
SpotinstClient.scale_elastigroup_up(self, group_id, adjustment)
```

Scale up an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __adjustment (int)__: Ammount to scale group

__Returns__

`(Object)`: Elastigroup API response

<h1 id="spotinst_sdk.SpotinstClient.scale_elastigroup_down">scale_elastigroup_down</h1>

```python
SpotinstClient.scale_elastigroup_down(self, group_id, adjustment)
```

Scale down an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __adjustment (int)__: Ammount to scale group

__Returns__

`(Object)`: Elastigroup API response

<h1 id="spotinst_sdk.SpotinstClient.list_suspended_scaling_policies">list_suspended_scaling_policies</h1>

```python
SpotinstClient.list_suspended_scaling_policies(self, group_id)
```

get suspended scaling policies for an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID

__Returns__

`(Object)`: Elastigroup API response

<h1 id="spotinst_sdk.SpotinstClient.suspend_scaling_policies">suspend_scaling_policies</h1>

```python
SpotinstClient.suspend_scaling_policies(self, group_id, policy_name)
```

suspended scaling policies for an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __policy_name (String)__: Scaling policy name

__Returns__

`(Object)`: Elastigroup API response

<h1 id="spotinst_sdk.SpotinstClient.resume_suspended_scaling_policies">resume_suspended_scaling_policies</h1>

```python
SpotinstClient.resume_suspended_scaling_policies(self, group_id, policy_name)
```

Resume scaling policies for an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __policy_name (String)__: Scaling policy name

__Returns__

`(Object)`: Elastigroup API response

