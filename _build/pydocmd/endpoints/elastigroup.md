<h1 id="spotinst_sdk.SpotinstClient.create_elastigroup">create_elastigroup</h1>

```python
SpotinstClient.create_elastigroup(self, group)
```

Create an elastigroup

__Arguments__

- __- group (Elastigroup)__: Elastigroup Object

__Returns__

`(Object)`: Elastigroup API response

<h1 id="spotinst_sdk.SpotinstClient.update_elastigroup">update_elastigroup</h1>

```python
SpotinstClient.update_elastigroup(self, group_update, group_id)
```

Update an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __group_update (Elastigroup)__: Elastigroup Object

__Returns__

`(Object)`: Elastigroup API response

<h1 id="spotinst_sdk.SpotinstClient.delete_elastigroup">delete_elastigroup</h1>

```python
SpotinstClient.delete_elastigroup(self, group_id)
```

Delete an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID

__Returns__

`(Object)`: Elastigroup API response

<h1 id="spotinst_sdk.SpotinstClient.delete_elastigroup_with_deallocation">delete_elastigroup_with_deallocation</h1>

```python
SpotinstClient.delete_elastigroup_with_deallocation(self, group_id, stateful_deallocation)
```

Delete a stateful elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __stateful_deallocation (Deallocation)__: Deallocation Object

__Returns__

`(Object)`: Elastigroup API response

<h1 id="spotinst_sdk.SpotinstClient.get_elastigroup">get_elastigroup</h1>

```python
SpotinstClient.get_elastigroup(self, group_id)
```

Get an elastigroup

__Arguments__

- __group_id(String)__: Elastigroup ID

__Returns__

`(Object)`: Elastigroup API response

<h1 id="spotinst_sdk.SpotinstClient.get_elastigroups">get_elastigroups</h1>

```python
SpotinstClient.get_elastigroups(self)
```

Get all elastigroup

__Returns__

`(List)`: List of Elastigroup API response

<h1 id="spotinst_sdk.SpotinstClient.get_elastigroup_active_instances">get_elastigroup_active_instances</h1>

```python
SpotinstClient.get_elastigroup_active_instances(self, group_id)
```

Get active instances of an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID

__Returns__

`(Object)`: Elastigroup API response

<h1 id="spotinst_sdk.SpotinstClient.get_elastigroup_activity">get_elastigroup_activity</h1>

```python
SpotinstClient.get_elastigroup_activity(self, group_id, start_date)
```

Get elastigroup activity

__Arguments__

- __group_id (String)__: Elastigroup ID
- __start_date (String)__: Date when to start checking

__Returns__

`(Object) `: Elastigroup API response

<h1 id="spotinst_sdk.SpotinstClient.get_instance_healthiness">get_instance_healthiness</h1>

```python
SpotinstClient.get_instance_healthiness(self, group_id)
```

get all instances a healthyness from an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID

__Returns__

`(Object)`: Elastigroup API response

<h1 id="spotinst_sdk.SpotinstClient.get_cost_per_elastigroup">get_cost_per_elastigroup</h1>

```python
SpotinstClient.get_cost_per_elastigroup(self, group_id, to_date=None, from_date=None)
```

get cost per elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __to_date (String) (Optional)__: Start Date
- __from_date (String) (Optional)__: End Date

__Returns__

`(Object)`: Elastigroup API response

<h1 id="spotinst_sdk.SpotinstClient.get_group_detailed_cost">get_group_detailed_cost</h1>

```python
SpotinstClient.get_group_detailed_cost(self, group_id, to_date=None, from_date=None)
```

get detailed cost per elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __to_date (String) (Optional)__: Start Date
- __from_date (String) (Optional)__: End Date

__Returns__

`(Object)`: Elastigroup API response

<h1 id="spotinst_sdk.SpotinstClient.list_suspended_process">list_suspended_process</h1>

```python
SpotinstClient.list_suspended_process(self, group_id)
```

List suspended process for an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID

__Returns__

`(Object)`: Elastigroup API response

<h1 id="spotinst_sdk.SpotinstClient.detach_elastigroup_instances">detach_elastigroup_instances</h1>

```python
SpotinstClient.detach_elastigroup_instances(self, group_id, detach_configuration)
```

Detatch instances from an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __detatch_configuration (Detach)__: Detach Object

__Returns__

`(Object)`: Elastigroup API response

<h1 id="spotinst_sdk.SpotinstClient.import_asg">import_asg</h1>

```python
SpotinstClient.import_asg(self, region, asg_name, asg, dry_run=None)
```

import asg attributes as JSON

__Arguments__

- __region (String)__: ASG region
- __asg_name (String)__: ASG Name
- __asg (ASG)__: ASG Object
- __dry_run (Bool) (Optional)__: if true only return JSON and not create group

__Returns__

`(Object)`: Elastigroup API response

<h1 id="spotinst_sdk.SpotinstClient.get_activity_events">get_activity_events</h1>

```python
SpotinstClient.get_activity_events(self, group_id, from_date)
```

get activity events

__Arguments__

- __group_id (String)__: Elastigroup ID
- __from_date (String)__: From date

__Returns__

`(Object)`: Elastigroup API response

<h1 id="spotinst_sdk.SpotinstClient.ami_backup">ami_backup</h1>

```python
SpotinstClient.ami_backup(self, group_id)
```

Start an AMI backup for Elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID

__Returns__

`(Object)`: Elastigroup API response

