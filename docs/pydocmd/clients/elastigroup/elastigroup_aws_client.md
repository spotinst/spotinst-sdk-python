<h1 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient">ElastigroupAwsClient</h1>

```python
ElastigroupAwsClient(self, session=None, print_output=True, log_level=None, user_agent=None)
```

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.create_elastigroup">create_elastigroup</h2>

```python
ElastigroupAwsClient.create_elastigroup(self, group)
```

Create an elastigroup

__Arguments__

- __group (Elastigroup)__: Elastigroup Object

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.update_elastigroup">update_elastigroup</h2>

```python
ElastigroupAwsClient.update_elastigroup(self, group_update, group_id, auto_apply_tags=None)
```

Update an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __group_update (Elastigroup)__: Elastigroup Object

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.delete_elastigroup">delete_elastigroup</h2>

```python
ElastigroupAwsClient.delete_elastigroup(self, group_id)
```

Delete an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.get_elastigroup">get_elastigroup</h2>

```python
ElastigroupAwsClient.get_elastigroup(self, group_id)
```

Get an elastigroup

__Arguments__

- __group_id(String)__: Elastigroup ID

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.get_elastigroups">get_elastigroups</h2>

```python
ElastigroupAwsClient.get_elastigroups(self)
```

Get all elastigroup

__Returns__

`(List)`: List of Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.scale_elastigroup_up">scale_elastigroup_up</h2>

```python
ElastigroupAwsClient.scale_elastigroup_up(self, group_id, adjustment)
```

Scale up an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __adjustment (int)__: Ammount to scale group

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.scale_elastigroup_down">scale_elastigroup_down</h2>

```python
ElastigroupAwsClient.scale_elastigroup_down(self, group_id, adjustment)
```

Scale down an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __adjustment (int)__: Ammount to scale group

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.delete_elastigroup_with_deallocation">delete_elastigroup_with_deallocation</h2>

```python
ElastigroupAwsClient.delete_elastigroup_with_deallocation(self, group_id, stateful_deallocation)
```

Delete a stateful elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __stateful_deallocation (Deallocation)__: Deallocation Object

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.get_elastigroup_active_instances">get_elastigroup_active_instances</h2>

```python
ElastigroupAwsClient.get_elastigroup_active_instances(self, group_id)
```

Get active instances of an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.get_elastigroup_activity">get_elastigroup_activity</h2>

```python
ElastigroupAwsClient.get_elastigroup_activity(self, group_id, start_date)
```

Get elastigroup activity

__Arguments__

- __group_id (String)__: Elastigroup ID
- __start_date (String)__: Date when to start checking

__Returns__

`(Object) `: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.roll_group">roll_group</h2>

```python
ElastigroupAwsClient.roll_group(self, group_id, group_roll)
```

Roll an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __group_roll (ElastigroupRoll)__: GroupRoll Object

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.get_all_group_deployment">get_all_group_deployment</h2>

```python
ElastigroupAwsClient.get_all_group_deployment(self, group_id)
```

get all group deployment from an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.get_deployment_status">get_deployment_status</h2>

```python
ElastigroupAwsClient.get_deployment_status(self, group_id, roll_id)
```

get all a deployment status from an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __roll_id (String)__: Deployment ID

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.stop_deployment">stop_deployment</h2>

```python
ElastigroupAwsClient.stop_deployment(self, group_id, roll_id)
```

stop a deployment from an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __roll_id (String)__: Deployment ID

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.create_deployment_action">create_deployment_action</h2>

```python
ElastigroupAwsClient.create_deployment_action(self, group_id, roll_id, deployment_action)
```

create a deployment from an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __roll_id (String)__: Deployment ID
- __deployment_action (Deployment)__: Deployment Object

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.get_instance_healthiness">get_instance_healthiness</h2>

```python
ElastigroupAwsClient.get_instance_healthiness(self, group_id)
```

get all instances a healthyness from an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.get_cost_per_elastigroup">get_cost_per_elastigroup</h2>

```python
ElastigroupAwsClient.get_cost_per_elastigroup(self, group_id, to_date=None, from_date=None)
```

get cost per elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __to_date (String) (Optional)__: Start Date
- __from_date (String) (Optional)__: End Date

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.get_group_detailed_cost">get_group_detailed_cost</h2>

```python
ElastigroupAwsClient.get_group_detailed_cost(self, group_id, to_date=None, from_date=None)
```

get detailed cost per elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __to_date (String) (Optional)__: Start Date
- __from_date (String) (Optional)__: End Date

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.list_suspended_scaling_policies">list_suspended_scaling_policies</h2>

```python
ElastigroupAwsClient.list_suspended_scaling_policies(self, group_id)
```

get suspended scaling policies for an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.suspend_scaling_policies">suspend_scaling_policies</h2>

```python
ElastigroupAwsClient.suspend_scaling_policies(self, group_id, policy_name)
```

suspended scaling policies for an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __policy_name (String)__: Scaling policy name

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.resume_suspended_scaling_policies">resume_suspended_scaling_policies</h2>

```python
ElastigroupAwsClient.resume_suspended_scaling_policies(self, group_id, policy_name)
```

Resume scaling policies for an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __policy_name (String)__: Scaling policy name

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.list_suspended_process">list_suspended_process</h2>

```python
ElastigroupAwsClient.list_suspended_process(self, group_id)
```

List suspended process for an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.suspend_process">suspend_process</h2>

```python
ElastigroupAwsClient.suspend_process(self, group_id, processes, suspensions)
```

suspended process for an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __processes (List)__: list of processes
- __suspensions (List)__: list of suspensions

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.remove_suspended_process">remove_suspended_process</h2>

```python
ElastigroupAwsClient.remove_suspended_process(self, group_id, processes)
```

remove suspended process for an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __processes (List)__: list of processes

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.detach_elastigroup_instances">detach_elastigroup_instances</h2>

```python
ElastigroupAwsClient.detach_elastigroup_instances(self, group_id, detach_configuration)
```

Detatch instances from an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __detatch_configuration (Detach)__: Detach Object

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.deallocate_stateful_instance">deallocate_stateful_instance</h2>

```python
ElastigroupAwsClient.deallocate_stateful_instance(self, group_id, stateful_instance_id)
```

Deallocate stateful instances from an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __stateful_instance_id (String)__: Stateful Instance ID

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.recycle_stateful_instance">recycle_stateful_instance</h2>

```python
ElastigroupAwsClient.recycle_stateful_instance(self, group_id, stateful_instance_id)
```

Recycle stateful instances from an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __stateful_instance_id (String)__: Stateful Instance ID

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.get_stateful_instances">get_stateful_instances</h2>

```python
ElastigroupAwsClient.get_stateful_instances(self, group_id)
```

Deallocate stateful instances from an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __stateful_instance_id (String)__: Stateful Instance ID

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.resume_stateful_instance">resume_stateful_instance</h2>

```python
ElastigroupAwsClient.resume_stateful_instance(self, group_id, stateful_instance_id)
```

Resume stateful instances from an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __stateful_instance_id (String)__: Stateful Instance ID

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.pause_stateful_instance">pause_stateful_instance</h2>

```python
ElastigroupAwsClient.pause_stateful_instance(self, group_id, stateful_instance_id)
```

Pause stateful instances from an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __stateful_instance_id (String)__: Stateful Instance ID

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.beanstalk_maintenance_status">beanstalk_maintenance_status</h2>

```python
ElastigroupAwsClient.beanstalk_maintenance_status(self, group_id)
```

Beanstalk maintenance status

__Arguments__

- __group_id (String)__: Elastigroup ID

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.beanstalk_maintenance_start">beanstalk_maintenance_start</h2>

```python
ElastigroupAwsClient.beanstalk_maintenance_start(self, group_id)
```

Beanstalk maintenance start

__Arguments__

- __group_id (String)__: Elastigroup ID

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.beanstalk_maintenance_finish">beanstalk_maintenance_finish</h2>

```python
ElastigroupAwsClient.beanstalk_maintenance_finish(self, group_id)
```

Beanstalk maintenance finish

__Arguments__

- __group_id (String)__: Elastigroup ID

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.beanstalk_import">beanstalk_import</h2>

```python
ElastigroupAwsClient.beanstalk_import(self, region, env_id=None, env_name=None)
```

Import beanstalk attributes into JSON. Either env_id or env_name is required, both cannot be null

__Arguments__

- __region (String)__: Beanstalk region
- __env_id (String)__: Beanstalk env id
- __env_name (String)__: Beanstalk env name

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.beanstalk_reimport">beanstalk_reimport</h2>

```python
ElastigroupAwsClient.beanstalk_reimport(self, group_id)
```

Reimport beanstalk attributes

__Arguments__

- __group_id (String)__: Elastigroup ID

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.import_asg">import_asg</h2>

```python
ElastigroupAwsClient.import_asg(self, region, asg_name, asg, dry_run=None)
```

import asg attributes as JSON

__Arguments__

- __region (String)__: ASG region
- __asg_name (String)__: ASG Name
- __asg (ASG)__: ASG Object
- __dry_run (Bool) (Optional)__: if true only return JSON and not create group

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.get_activity_events">get_activity_events</h2>

```python
ElastigroupAwsClient.get_activity_events(self, group_id, from_date)
```

get activity events

__Arguments__

- __group_id (String)__: Elastigroup ID
- __from_date (String)__: From date

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.ami_backup">ami_backup</h2>

```python
ElastigroupAwsClient.ami_backup(self, group_id)
```

Start an AMI backup for Elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.create_blue_green_deployment">create_blue_green_deployment</h2>

```python
ElastigroupAwsClient.create_blue_green_deployment(self, group_id, blue_green_deployment)
```

Start a Blue Green Deployment

__Arguments__

- __group_id (String)__: Elastigroup ID
- __blue_green_deployment (BGDeployment)__: Blue Green Deployment Object
__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.get_blue_green_deployment">get_blue_green_deployment</h2>

```python
ElastigroupAwsClient.get_blue_green_deployment(self, group_id)
```

Get Blue Green Deployment for an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.stop_blue_green_deployment">stop_blue_green_deployment</h2>

```python
ElastigroupAwsClient.stop_blue_green_deployment(self, group_id, deployment_id)
```

Stop Blue Green Deployment for an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __deployment_id (String)__:  BG Deployment ID
__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.get_instance_type_by_region">get_instance_type_by_region</h2>

```python
ElastigroupAwsClient.get_instance_type_by_region(self, region)
```

Get instance type by region

__Arguments__

- __region (String)__: AWS region

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.lock_instance">lock_instance</h2>

```python
ElastigroupAwsClient.lock_instance(self, instance_id, lock_time=None)
```

Lock instance

__Arguments__

- __instance_id (String)__: Instance ID
- __lock_time (int) (Optinal)__: Time to lock instance

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.unlock_instance">unlock_instance</h2>

```python
ElastigroupAwsClient.unlock_instance(self, instance_id)
```

Unlock instance

__Arguments__

- __instance_id (String)__: Instance ID

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.enter_instance_standby">enter_instance_standby</h2>

```python
ElastigroupAwsClient.enter_instance_standby(self, instance_id)
```

Enter standby for instance

__Arguments__

- __instance_id (String)__: Instance ID

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.exit_instance_standby">exit_instance_standby</h2>

```python
ElastigroupAwsClient.exit_instance_standby(self, instance_id)
```

Exit standby for instance

__Arguments__

- __instance_id (String)__: Instance ID

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.get_instance_status">get_instance_status</h2>

```python
ElastigroupAwsClient.get_instance_status(self, instance_id)
```

Get instance status

__Arguments__

- __instance_id (String)__: Instance ID

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.create_instance_signal">create_instance_signal</h2>

```python
ElastigroupAwsClient.create_instance_signal(self, instance_id, signal)
```

create instance signal

__Arguments__

- __instance_id (String)__: instance ID
- __signal (String)__: Signal

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.get_cost_per_account">get_cost_per_account</h2>

```python
ElastigroupAwsClient.get_cost_per_account(self, to_date=None, from_date=None)
```

get cost per account

__Arguments__

- __to_date (String) (Optional)__: to date
- __from_date (String) (Optional)__: to date

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.get_potential_savings">get_potential_savings</h2>

```python
ElastigroupAwsClient.get_potential_savings(self)
```

get potential saving

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.get_instance_potential_savings">get_instance_potential_savings</h2>

```python
ElastigroupAwsClient.get_instance_potential_savings(self, instance_ids, region)
```

get potential saving

__Arguments__

- __instance_ids (List)__: List of instance id strings
- __region (String)__: region
__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.get_elastilog">get_elastilog</h2>

```python
ElastigroupAwsClient.get_elastilog(self, group_id, from_date, to_date, severity=None, resource_id=None, limit=None)
```

Get an elastilog for a specific elastigroup

__Arguments__

- __group_id(String)__: Elastigroup ID
- __to_date (String)__: to date
- __from_date (String)__: to date
- __severity(String) (Optional)__: Log level severity
- __resource_id(String) (Optional)__: Filter log extracted entires related to a specific resource id
- __limit(String) (Optional)__: Maximum number of lines to extract in a response

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.import_stateful_instance">import_stateful_instance</h2>

```python
ElastigroupAwsClient.import_stateful_instance(self, stateful_instance)
```

Import stateful instance parametes

__Arguments__

- __stateful_instance (StatefulInstance)__: StatefulInstance Object

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.get_stateful_import_status">get_stateful_import_status</h2>

```python
ElastigroupAwsClient.get_stateful_import_status(self, stateful_migration_id)
```

Get stateful instance status

__Arguments__

- __stateful_migration_id (String)__: Stateful migration ID

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAwsClient.delete_stateful_import">delete_stateful_import</h2>

```python
ElastigroupAwsClient.delete_stateful_import(self, stateful_migration_id)
```

Delete stateful instance

__Arguments__

- __stateful_migration_id (String)__: Stateful migration ID

__Returns__

`(Object)`: Elastigroup API response

