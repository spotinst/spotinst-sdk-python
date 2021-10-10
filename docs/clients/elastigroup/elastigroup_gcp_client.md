<h1 id="spotinst_sdk2.clients.elastigroup.ElastigroupGcpClient">ElastigroupGcpClient</h1>

```python
ElastigroupGcpClient(self,
                     session=None,
                     print_output=True,
                     log_level=None,
                     user_agent=None,
                     timeout=None)
```

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupGcpClient.create_elastigroup">create_elastigroup</h2>

```python
ElastigroupGcpClient.create_elastigroup(group)
```

Create an elastigroup

__Arguments__

- __group (Elastigroup)__: Elastigroup Object

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupGcpClient.update_elastigroup">update_elastigroup</h2>

```python
ElastigroupGcpClient.update_elastigroup(group_update, group_id)
```

Update an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __group_update (Elastigroup)__: Elastigroup Object

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupGcpClient.delete_elastigroup">delete_elastigroup</h2>

```python
ElastigroupGcpClient.delete_elastigroup(group_id)
```

Delete an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupGcpClient.get_elastigroup">get_elastigroup</h2>

```python
ElastigroupGcpClient.get_elastigroup(group_id)
```

Get an elastigroup

__Arguments__

- __group_id(String)__: Elastigroup ID

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupGcpClient.get_elastigroups">get_elastigroups</h2>

```python
ElastigroupGcpClient.get_elastigroups()
```

Get all elastigroup

__Returns__

`(List)`: List of Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupGcpClient.scale_elastigroup_up">scale_elastigroup_up</h2>

```python
ElastigroupGcpClient.scale_elastigroup_up(group_id, adjustment)
```

Scale up an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __adjustment (int)__: Ammount to scale group

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupGcpClient.scale_elastigroup_down">scale_elastigroup_down</h2>

```python
ElastigroupGcpClient.scale_elastigroup_down(group_id, adjustment)
```

Scale down an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __adjustment (int)__: Ammount to scale group

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupGcpClient.roll_group">roll_group</h2>

```python
ElastigroupGcpClient.roll_group(group_id, group_roll)
```

Roll an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __group_roll (ElastigroupRoll)__: GroupRoll Object

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupGcpClient.get_all_group_deployment">get_all_group_deployment</h2>

```python
ElastigroupGcpClient.get_all_group_deployment(group_id)
```

get all group deployment from an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupGcpClient.get_deployment_status">get_deployment_status</h2>

```python
ElastigroupGcpClient.get_deployment_status(group_id, roll_id)
```

get all a deployment status from an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __roll_id (String)__: Deployment ID

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupGcpClient.stop_deployment">stop_deployment</h2>

```python
ElastigroupGcpClient.stop_deployment(group_id, roll_id)
```

stop a deployment from an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __roll_id (String)__: Deployment ID

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupGcpClient.get_elastigroup_active_instances">get_elastigroup_active_instances</h2>

```python
ElastigroupGcpClient.get_elastigroup_active_instances(group_id)
```

Get active instances of an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupGcpClient.get_cost_per_elastigroup">get_cost_per_elastigroup</h2>

```python
ElastigroupGcpClient.get_cost_per_elastigroup(group_id,
                                              to_date=None,
                                              from_date=None)
```

get cost per elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __to_date (String) (Optional)__: Start Date
- __from_date (String) (Optional)__: End Date

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupGcpClient.get_elastigroup_activity">get_elastigroup_activity</h2>

```python
ElastigroupGcpClient.get_elastigroup_activity(group_id, start_date)
```

Get elastigroup activity

__Arguments__

- __group_id (String)__: Elastigroup ID
- __start_date (String)__: Date when to start checking

__Returns__

`(Object) `: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupGcpClient.import_gke">import_gke</h2>

```python
ElastigroupGcpClient.import_gke(location, gke_id, gke)
```

import gke attributes as JSON

__Arguments__

- __location (String)__: GKE location
- __gke_id (String)__: GKE ID
- __gke (GKE)__: GKE Object

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupGcpClient.detach_elastigroup_instances">detach_elastigroup_instances</h2>

```python
ElastigroupGcpClient.detach_elastigroup_instances(
  group_id, detach_configuration)
```

Detatch instances from an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __detatch_configuration (Detach)__: Detach Object

__Returns__

`(Object)`: Elastigroup API response

