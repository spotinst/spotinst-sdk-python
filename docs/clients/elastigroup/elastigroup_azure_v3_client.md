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

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureV3Client.get_elastigroup_status">get_elastigroup_status</h2>

```python
ElastigroupAzureV3Client.get_elastigroup_status(group_id)
```

Get status of Elastigroup cluster.

__Arguments__

- __group_id (String)__: Elastigroup ID

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureV3Client.get_vm_healthiness">get_vm_healthiness</h2>

```python
ElastigroupAzureV3Client.get_vm_healthiness(group_id)
```

Get a list of vms with health status.

__Arguments__

- __group_id (String)__: Elastigroup ID

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureV3Client.suspend_elastigroup">suspend_elastigroup</h2>

```python
ElastigroupAzureV3Client.suspend_elastigroup(group_id, processes)
```

Suspends the Group.

__Arguments__

- __group_id (String)__: Elastigroup ID
- __processes (List)__: List of processes to create or update their suspensions

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureV3Client.resume_elastigroup">resume_elastigroup</h2>

```python
ElastigroupAzureV3Client.resume_elastigroup(group_id, processes)
```

Resumes the Group.

__Arguments__

- __group_id (String)__: Elastigroup ID
- __processes (List)__: List of processes to cancel their suspensions

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureV3Client.start_deployment">start_deployment</h2>

```python
ElastigroupAzureV3Client.start_deployment(group_id, deployment)
```

Deploy the Elastigroup.
This triggers a Blue/Green deployment that replaces the existing VMs in the Elastigroup.

__Arguments__

- __group_id (String)__: Elastigroup ID
- __deployment__: DeploymentConfiguration Object

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureV3Client.get_all_deployments">get_all_deployments</h2>

```python
ElastigroupAzureV3Client.get_all_deployments(group_id,
                                             limit=None,
                                             sort=None)
```

Get a list of all the deployments of a specific Elastigroup and the status of each one.

__Arguments__

- __group_id (String)__: Elastigroup ID
- __limit (integer)__: Limits the number of deployments returned. Default: 5
- __sort (String)__: Field by which to sort the results. Default: createdAt:DESC

__Returns__

`(Object) `: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureV3Client.get_deployment">get_deployment</h2>

```python
ElastigroupAzureV3Client.get_deployment(group_id, deployment_id)
```

Get the status of a specific deployment.

__Arguments__

- __group_id (String)__: Elastigroup ID
- __deployment_id (String)__: The deployment ID you want to query

__Returns__

`(Object) `: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureV3Client.get_deployment_status">get_deployment_status</h2>

```python
ElastigroupAzureV3Client.get_deployment_status(group_id, deployment_id)
```

Get the detailed status of a specific deployment.
This includes status details per batch and other information.

__Arguments__

- __group_id (String)__: Elastigroup ID
- __deployment_id (String)__: The deployment ID you want to query

__Returns__

`(Object) `: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureV3Client.import_from_scale_set">import_from_scale_set</h2>

```python
ElastigroupAzureV3Client.import_from_scale_set(resource_group_name,
                                               scale_set_name)
```

Given a scale set, constructs a valid group configuration based on the scale set and returns it.

__Arguments__

- __resource_group_name (String)__: Resource Group Name
- __scale_set_name (String)__: Scale Set Name

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureV3Client.import_from_virtual_machine">import_from_virtual_machine</h2>

```python
ElastigroupAzureV3Client.import_from_virtual_machine(
  resource_group_name, virtual_machine_name)
```

Given a virtual machine, constructs a valid group configuration based on the virtual machine and returns it.

__Arguments__

- __resource_group_name (String)__: Resource Group Name
- __virtual_machine_name (String)__: Virtual Machine Name

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureV3Client.import_from_load_balancer">import_from_load_balancer</h2>

```python
ElastigroupAzureV3Client.import_from_load_balancer(
  backend_pool_name, load_balancer_name, resource_group_name)
```

Given a load balancer, constructs a valid group configuration and returns it.

__Arguments__

- __resource_group_name (String)__: Resource Group Name
- __load_balancer_name (String)__: Virtual Machine Name
- __backend_pool_name (String)__: Backend Pool Name

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureV3Client.import_from_application_gateway">import_from_application_gateway</h2>

```python
ElastigroupAzureV3Client.import_from_application_gateway(
  backend_pool_name, application_gateway_name, resource_group_name)
```

Given a load balancer, constructs a valid group configuration and returns it.

__Arguments__

- __resource_group_name (String)__: Resource Group Name
- __application_gateway_name (String)__: Application Gateway Name
- __backend_pool_name (String)__: Backend Pool Name

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureV3Client.create_vm_signal">create_vm_signal</h2>

```python
ElastigroupAzureV3Client.create_vm_signal(vm_name, signal_type)
```

The VM signal API is used for notifying Spot about the VM state so that Spot can act accordingly

__Arguments__

- __vm_name (String)__: The virtual machine ID the signal refers to.
- __signal_type (String)__: Signal Type (Enum: "vmReady" "vmReadyToShutdown")

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureV3Client.get_elastilog">get_elastilog</h2>

```python
ElastigroupAzureV3Client.get_elastilog(group_id,
                                       from_date,
                                       to_date,
                                       severity=None,
                                       resource_id=None,
                                       limit=None)
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

