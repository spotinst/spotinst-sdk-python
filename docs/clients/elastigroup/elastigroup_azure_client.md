<h1 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureClient">ElastigroupAzureClient</h1>

```python
ElastigroupAzureClient(self,
                       session=None,
                       print_output=True,
                       log_level=None,
                       user_agent=None)
```

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureClient.create_elastigroup">create_elastigroup</h2>

```python
ElastigroupAzureClient.create_elastigroup(group)
```

Create an elastigroup

__Arguments__

- __group (Elastigroup)__: Elastigroup Object

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureClient.update_elastigroup">update_elastigroup</h2>

```python
ElastigroupAzureClient.update_elastigroup(group_update, group_id)
```

Update an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __group_update (Elastigroup)__: Elastigroup Object

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureClient.delete_elastigroup">delete_elastigroup</h2>

```python
ElastigroupAzureClient.delete_elastigroup(group_id)
```

Delete an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureClient.get_elastigroup">get_elastigroup</h2>

```python
ElastigroupAzureClient.get_elastigroup(group_id)
```

Get an elastigroup

__Arguments__

- __group_id(String)__: Elastigroup ID

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureClient.get_elastigroups">get_elastigroups</h2>

```python
ElastigroupAzureClient.get_elastigroups()
```

Get all elastigroup

__Returns__

`(List)`: List of Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureClient.roll_group">roll_group</h2>

```python
ElastigroupAzureClient.roll_group(group_id, group_roll)
```

Roll an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __group_roll (ElastigroupRoll)__: GroupRoll Object

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureClient.get_all_group_deployment">get_all_group_deployment</h2>

```python
ElastigroupAzureClient.get_all_group_deployment(group_id)
```

get all group deployment from an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureClient.get_deployment_status">get_deployment_status</h2>

```python
ElastigroupAzureClient.get_deployment_status(group_id, roll_id)
```

get all a deployment status from an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __roll_id (String)__: Deployment ID

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureClient.stop_deployment">stop_deployment</h2>

```python
ElastigroupAzureClient.stop_deployment(group_id, roll_id)
```

stop a deployment from an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __roll_id (String)__: Deployment ID

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureClient.scale_elastigroup_up">scale_elastigroup_up</h2>

```python
ElastigroupAzureClient.scale_elastigroup_up(group_id, adjustment)
```

Scale up an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __adjustment (int)__: Ammount to scale group

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureClient.scale_elastigroup_down">scale_elastigroup_down</h2>

```python
ElastigroupAzureClient.scale_elastigroup_down(group_id, adjustment)
```

Scale down an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __adjustment (int)__: Ammount to scale group

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureClient.create_task">create_task</h2>

```python
ElastigroupAzureClient.create_task(task)
```

Create a scheduling task

__Arguments__

- __task (Task)__: Task Object

__Returns__

`(Object)`: Task API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureClient.update_task">update_task</h2>

```python
ElastigroupAzureClient.update_task(task_update, task_id)
```

Update a scheduling Task

__Arguments__

- __task_id (String)__: Task ID
- __task_update (Elastigroup)__: Task Object

__Returns__

`(Object)`: Task API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureClient.get_task">get_task</h2>

```python
ElastigroupAzureClient.get_task(task_id)
```

Get a Task

__Arguments__

- __task_id(String)__: Task ID

__Returns__

`(Object)`: Task API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureClient.get_all_tasks">get_all_tasks</h2>

```python
ElastigroupAzureClient.get_all_tasks()
```

Get all Tasks
__Returns__

`(Object)`: Task API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureClient.delete_task">delete_task</h2>

```python
ElastigroupAzureClient.delete_task(task_id)
```

Delete a scheduling task

__Arguments__

- __task_id (String)__: Task ID

__Returns__

`(Object)`: Task API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureClient.get_elastigroup_active_instances">get_elastigroup_active_instances</h2>

```python
ElastigroupAzureClient.get_elastigroup_active_instances(group_id)
```

Get active instances of an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureClient.detach_elastigroup_instances">detach_elastigroup_instances</h2>

```python
ElastigroupAzureClient.detach_elastigroup_instances(
  group_id, detach_configuration)
```

Detatch instances from an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __detatch_configuration (Detach)__: Detach Object

__Returns__

`(Object)`: Elastigroup API response

