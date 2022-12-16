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

