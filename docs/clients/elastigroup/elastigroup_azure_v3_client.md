<h1 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureV3Client">ElastigroupAzureV3Client</h1>

```python
ElastigroupAzureV3Client(self,
                         session=None,
                         print_output=True,
                         log_level=None,
                         user_agent=None,
                         timeout=None)
```

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureV3Client.create_elastigroup">create_elastigroup</h2>

```python
ElastigroupAzureV3Client.create_elastigroup(group)
```

Create an elastigroup

__Arguments__

- __group (Elastigroup)__: Elastigroup Object

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureV3Client.update_elastigroup">update_elastigroup</h2>

```python
ElastigroupAzureV3Client.update_elastigroup(group_update, group_id)
```

Update an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __group_update (Elastigroup)__: Elastigroup Object

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureV3Client.delete_elastigroup">delete_elastigroup</h2>

```python
ElastigroupAzureV3Client.delete_elastigroup(group_id)
```

Delete an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureV3Client.get_elastigroup">get_elastigroup</h2>

```python
ElastigroupAzureV3Client.get_elastigroup(group_id)
```

Get an elastigroup

__Arguments__

- __group_id(String)__: Elastigroup ID

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureV3Client.get_elastigroups">get_elastigroups</h2>

```python
ElastigroupAzureV3Client.get_elastigroups()
```

Get all elastigroups

__Returns__

`(List)`: List of Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureV3Client.update_elastigroup_capacity">update_elastigroup_capacity</h2>

```python
ElastigroupAzureV3Client.update_elastigroup_capacity(group_id, capacity)
```

Update capacity of Elastigroups

__Arguments__

- __group_id (String)__: Elastigroup ID
- __capacity__: Capacity Object

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureV3Client.scale_elastigroup_up">scale_elastigroup_up</h2>

```python
ElastigroupAzureV3Client.scale_elastigroup_up(group_id, adjustment)
```

Scale up an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __adjustment (int)__: Ammount to scale group

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureV3Client.scale_elastigroup_down">scale_elastigroup_down</h2>

```python
ElastigroupAzureV3Client.scale_elastigroup_down(group_id, adjustment)
```

Scale down an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __adjustment (int)__: Ammount to scale group

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureV3Client.detach_elastigroup_vms">detach_elastigroup_vms</h2>

```python
ElastigroupAzureV3Client.detach_elastigroup_vms(group_id,
                                                detach_configuration)
```

Detach VMs from an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __detach_configuration (Detach)__: DetachConfiguration Object

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureV3Client.protect_virtual_machine">protect_virtual_machine</h2>

```python
ElastigroupAzureV3Client.protect_virtual_machine(group_id,
                                                 vm_name,
                                                 ttl_in_minutes=None)
```

Protect virtual machines in Elastigroup cluster.

__Arguments__

- __group_id (String)__: Elastigroup ID
- __vm_name (String)__: VM ID
- __ttl_in_minutes (int) (Optional)__: How long protection will be valid

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureV3Client.unprotect_virtual_machine">unprotect_virtual_machine</h2>

```python
ElastigroupAzureV3Client.unprotect_virtual_machine(group_id, vm_name)
```

Un-Protect virtual machines in Elastigroup cluster.

__Arguments__

- __group_id (String)__: Elastigroup ID
- __vm_name (String)__: VM ID

__Returns__

`(Object)`: Spotinst API response

