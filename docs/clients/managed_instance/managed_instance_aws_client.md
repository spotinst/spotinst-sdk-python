<h1 id="spotinst_sdk2.clients.managed_instance.ManagedInstanceAwsClient">ManagedInstanceAwsClient</h1>

```python
ManagedInstanceAwsClient(self,
                         session=None,
                         print_output=True,
                         log_level=None,
                         user_agent=None,
                         timeout=None)
```

<h2 id="spotinst_sdk2.clients.managed_instance.ManagedInstanceAwsClient.ENTITY_NAME">ENTITY_NAME</h2>


<h2 id="spotinst_sdk2.clients.managed_instance.ManagedInstanceAwsClient.create_managed_instance">create_managed_instance</h2>

```python
ManagedInstanceAwsClient.create_managed_instance(
  managed_instance: ManagedInstance)
```

Create a Managed Instance

__Arguments__

- __managed instance (ManagedInstance)__: ManagedInstance Object

__Returns__

`(Object)`: ManagedInstance API response

<h2 id="spotinst_sdk2.clients.managed_instance.ManagedInstanceAwsClient.get_managed_instance">get_managed_instance</h2>

```python
ManagedInstanceAwsClient.get_managed_instance(managed_instance_id: str)
```

Get a Managed Instance

__Arguments__

- __managed_instance_id(String)__: Managed Instance ID

__Returns__

`(Object)`: ManagedInstance API response

<h2 id="spotinst_sdk2.clients.managed_instance.ManagedInstanceAwsClient.get_managed_instances">get_managed_instances</h2>

```python
ManagedInstanceAwsClient.get_managed_instances()
```

Get all Managed Instance

__Returns__

`List`: List of ManagedInstance API response

<h2 id="spotinst_sdk2.clients.managed_instance.ManagedInstanceAwsClient.update_managed_instance">update_managed_instance</h2>

```python
ManagedInstanceAwsClient.update_managed_instance(
  managed_instance_id: str, managed_instance_update: ManagedInstance)
```

Update a Managed Instance

__Arguments__

- __managed_instance_id(String)__: Managed Instance ID
- __managed_instance_update(ManagedInstance)__: ManagedInstance Object

__Returns__

`(Object)`: ManagedInstance API response

<h2 id="spotinst_sdk2.clients.managed_instance.ManagedInstanceAwsClient.delete_managed_instance">delete_managed_instance</h2>

```python
ManagedInstanceAwsClient.delete_managed_instance(
  managed_instance_id: str,
  deallocation_config:
    DeallocationConfig = 'd3043820717d74d9a17694c176d39733',
  ami_backup: AmiBackup = 'd3043820717d74d9a17694c176d39733')
```

Delete a Managed Instance

__Arguments__

- __managed_instance_id(String)__: Managed Instance ID
- __deallocation_config(DeallocationConfig)__: DeallocationConfig object
- __ami_backup(AmiBackup)__: AmiBackup object

__Returns__

`(Object)`: ManagedInstance API response

<h2 id="spotinst_sdk2.clients.managed_instance.ManagedInstanceAwsClient.recycle_managed_instance">recycle_managed_instance</h2>

```python
ManagedInstanceAwsClient.recycle_managed_instance(
  managed_instance_id: str)
```

Recycle a Managed Instance

__Arguments__

- __managed_instance_id(String)__: Managed Instance ID

__Returns__

`(Object)`: ManagedInstance API response

<h2 id="spotinst_sdk2.clients.managed_instance.ManagedInstanceAwsClient.pause_managed_instance">pause_managed_instance</h2>

```python
ManagedInstanceAwsClient.pause_managed_instance(
  managed_instance_id: str)
```

Pause a Managed Instance

__Arguments__

- __managed_instance_id(String)__: Managed Instance ID

__Returns__

`(Object)`: ManagedInstance API response

<h2 id="spotinst_sdk2.clients.managed_instance.ManagedInstanceAwsClient.resume_managed_instance">resume_managed_instance</h2>

```python
ManagedInstanceAwsClient.resume_managed_instance(
  managed_instance_id: str)
```

Resume a Managed Instance

__Arguments__

- __managed_instance_id(String)__: Managed Instance ID

__Returns__

`(Object)`: ManagedInstance API response

<h2 id="spotinst_sdk2.clients.managed_instance.ManagedInstanceAwsClient.get_managed_instance_status">get_managed_instance_status</h2>

```python
ManagedInstanceAwsClient.get_managed_instance_status(
  managed_instance_id: str)
```

Get Managed Instance Status

__Arguments__

- __managed_instance_id(String)__: Managed Instance ID

__Returns__

`(Object)`: ManagedInstance API response

<h2 id="spotinst_sdk2.clients.managed_instance.ManagedInstanceAwsClient.get_managed_instance_costs">get_managed_instance_costs</h2>

```python
ManagedInstanceAwsClient.get_managed_instance_costs(
  managed_instance_id: str,
  from_date: str,
  to_date: str,
  aggregation_period: str = None)
```

Get Managed Instance Costs

__Arguments__

- __managed_instance_id(String)__: Managed Instance ID
- __from_date (String)__: Get Cost on and after this Date
- __to_date (String)__: Get Cost on and before this Date
- __aggregation_period (String)__: Data values following either a date format or Unix seconds Timestamp

__Returns__

`(Object)`: ManagedInstance API response

<h2 id="spotinst_sdk2.clients.managed_instance.ManagedInstanceAwsClient.delete_volume_in_managed_instance">delete_volume_in_managed_instance</h2>

```python
ManagedInstanceAwsClient.delete_volume_in_managed_instance(
  managed_instance_id: str, volume_id: str)
```

Delete Volume in a Managed Instance

__Arguments__

- __managed_instance_id(String)__: Managed Instance ID
- __volume_id(String)__: Volume ID

__Returns__

`(Object)`: ManagedInstance API response

<h2 id="spotinst_sdk2.clients.managed_instance.ManagedInstanceAwsClient.update_managed_instance_states">update_managed_instance_states</h2>

```python
ManagedInstanceAwsClient.update_managed_instance_states(
  update_manage_instance_states_list: list)
```

Update a Managed Instance States

__Arguments__

- __update_manage_instance_state_list(List)__: Update Manage Instance List

__Returns__

`(Object)`: ManagedInstance API response

