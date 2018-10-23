<h1 id="spotinst_sdk.SpotinstClient.create_elastigroup">create_elastigroup</h1>

```python
SpotinstClient.create_elastigroup(self, group)
```

Create an elastigroup

__Arguments__

- __group (Elastigroup)__: Elastigroup Object

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

<h1 id="spotinst_sdk.SpotinstClient.roll_group">roll_group</h1>

```python
SpotinstClient.roll_group(self, group_id, group_roll)
```

Roll an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __group_roll (ElastigroupRoll)__: GroupRoll Object

__Returns__

`(Object)`: Elastigroup API response

<h1 id="spotinst_sdk.SpotinstClient.get_deployment_status">get_deployment_status</h1>

```python
SpotinstClient.get_deployment_status(self, group_id, roll_id)
```

get all a deployment status from an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __roll_id (String)__: Deployment ID

__Returns__

`(Object)`: Elastigroup API response

<h1 id="spotinst_sdk.SpotinstClient.stop_deployment">stop_deployment</h1>

```python
SpotinstClient.stop_deployment(self, group_id, roll_id)
```

stop a deployment from an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __roll_id (String)__: Deployment ID

__Returns__

`(Object)`: Elastigroup API response

<h1 id="spotinst_sdk.SpotinstClient.create_deployment_action">create_deployment_action</h1>

```python
SpotinstClient.create_deployment_action(self, group_id, roll_id, deployment_action)
```

create a deployment from an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __roll_id (String)__: Deployment ID
- __deployment_action (Deployment)__: Deployment Object

__Returns__

`(Object)`: Elastigroup API response

<h1 id="spotinst_sdk.SpotinstClient.get_kubernetes_cluster_cost">get_kubernetes_cluster_cost</h1>

```python
SpotinstClient.get_kubernetes_cluster_cost(self, custer_id, from_date, to_date)
```

Get kubernetes cluster cost

__Arguments__

- __custer_id (String)__: Kubernetes cluster id
- __from_date (String)__: From date
- __to_date (String)__: to date

__Returns__

`(Object)`: Elastigroup API response

<h1 id="spotinst_sdk.SpotinstClient.get_instance_type_by_region">get_instance_type_by_region</h1>

```python
SpotinstClient.get_instance_type_by_region(self, region)
```

Get instance type by region

__Arguments__

- __region (String)__: AWS region

__Returns__

`(Object)`: Spotinst API response

<h1 id="spotinst_sdk.SpotinstClient.lock_instance">lock_instance</h1>

```python
SpotinstClient.lock_instance(self, instance_id, lock_time=None)
```

Lock instance

__Arguments__

- __instance_id (String)__: Instance ID
- __lock_time (int) (Optinal)__: Time to lock instance

__Returns__

`(Object)`: Spotinst API response

<h1 id="spotinst_sdk.SpotinstClient.unlock_instance">unlock_instance</h1>

```python
SpotinstClient.unlock_instance(self, instance_id)
```

Unlock instance

__Arguments__

- __instance_id (String)__: Instance ID

__Returns__

`(Object)`: Spotinst API response

<h1 id="spotinst_sdk.SpotinstClient.enter_instance_standby">enter_instance_standby</h1>

```python
SpotinstClient.enter_instance_standby(self, instance_id)
```

Enter standby for instance

__Arguments__

- __instance_id (String)__: Instance ID

__Returns__

`(Object)`: Spotinst API response

<h1 id="spotinst_sdk.SpotinstClient.exit_instance_standby">exit_instance_standby</h1>

```python
SpotinstClient.exit_instance_standby(self, instance_id)
```

Exit standby for instance

__Arguments__

- __instance_id (String)__: Instance ID

__Returns__

`(Object)`: Spotinst API response

<h1 id="spotinst_sdk.SpotinstClient.get_instance_status">get_instance_status</h1>

```python
SpotinstClient.get_instance_status(self, instance_id)
```

Get instance status

__Arguments__

- __instance_id (String)__: Instance ID

__Returns__

`(Object)`: Spotinst API response

<h1 id="spotinst_sdk.SpotinstClient.get_cost_per_account">get_cost_per_account</h1>

```python
SpotinstClient.get_cost_per_account(self, to_date=None, from_date=None)
```

get cost per account

__Arguments__

- __to_date (String) (Optional)__: to date
- __from_date (String) (Optional)__: to date

__Returns__

`(Object)`: Spotinst API response

<h1 id="spotinst_sdk.SpotinstClient.get_potential_savings">get_potential_savings</h1>

```python
SpotinstClient.get_potential_savings(self)
```

get potential saving

__Returns__

`(Object)`: Elastigroup API response

<h1 id="spotinst_sdk.SpotinstClient.get_instance_potential_savings">get_instance_potential_savings</h1>

```python
SpotinstClient.get_instance_potential_savings(self, instance_ids, region)
```

get potential saving

__Arguments__

- __instance_ids (List)__: List of instance id strings
- __region (String)__: region
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

