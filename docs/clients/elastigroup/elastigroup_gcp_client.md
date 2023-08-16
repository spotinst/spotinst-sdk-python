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
ElastigroupGcpClient.create_elastigroup(group: Elastigroup)
```

Create an elastigroup

__Arguments__

- __group (Elastigroup)__: Elastigroup Object

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupGcpClient.update_elastigroup">update_elastigroup</h2>

```python
ElastigroupGcpClient.update_elastigroup(group_update: Elastigroup,
                                        group_id: str)
```

Update an GCP Elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __group_update (Elastigroup)__: Elastigroup Object

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupGcpClient.delete_elastigroup">delete_elastigroup</h2>

```python
ElastigroupGcpClient.delete_elastigroup(group_id: str)
```

Delete an Elastigroup GCP

__Arguments__

- __group_id (String)__: Elastigroup ID

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupGcpClient.get_elastigroup">get_elastigroup</h2>

```python
ElastigroupGcpClient.get_elastigroup(group_id: str)
```

List all properties for single GCP Elastigroup

__Arguments__

- __group_id(String)__: Elastigroup ID

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupGcpClient.get_elastigroups">get_elastigroups</h2>

```python
ElastigroupGcpClient.get_elastigroups()
```

List all GCP Elastigroups for a Spot Account

__Returns__

`(List)`: List of Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupGcpClient.scale_elastigroup_up">scale_elastigroup_up</h2>

```python
ElastigroupGcpClient.scale_elastigroup_up(group_id: str,
                                          adjustment: int)
```

Add instances to the Elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __adjustment (int)__: The number of instances to add to the group

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupGcpClient.scale_elastigroup_down">scale_elastigroup_down</h2>

```python
ElastigroupGcpClient.scale_elastigroup_down(group_id: str,
                                            adjustment: int)
```

Remove instances from the Elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __adjustment (int)__: Ammount to scale group

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupGcpClient.roll_group">roll_group</h2>

```python
ElastigroupGcpClient.roll_group(group_id: str, group_roll: RollGroup)
```

Deploy the Elastigroup: Triggers a Blue/Green deployment that replaces the existing instances in the Elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __group_roll (ElastigroupRoll)__: GroupRoll Object

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupGcpClient.get_all_group_deployment">get_all_group_deployment</h2>

```python
ElastigroupGcpClient.get_all_group_deployment(group_id: str)
```

Get all the deployments for a specific Elastigroup, and their status

__Arguments__

- __group_id (String)__: Elastigroup ID

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupGcpClient.get_deployment_status">get_deployment_status</h2>

```python
ElastigroupGcpClient.get_deployment_status(group_id: str, roll_id: str)
```

Get a specific deployment's status

__Arguments__

- __group_id (String)__: The Spot Elastigroup ID you want to update
- __roll_id (String)__: The deployment ID to query

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupGcpClient.stop_deployment">stop_deployment</h2>

```python
ElastigroupGcpClient.stop_deployment(group_id: str, roll_id: str)
```

Stop an existing deployment

__Arguments__

- __group_id (String)__: Elastigroup ID
- __roll_id (String)__: Deployment ID

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupGcpClient.get_elastigroup_active_instances">get_elastigroup_active_instances</h2>

```python
ElastigroupGcpClient.get_elastigroup_active_instances(group_id: str)
```

Get the status for all instances that are memebers of the Elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupGcpClient.get_cost_per_elastigroup">get_cost_per_elastigroup</h2>

```python
ElastigroupGcpClient.get_cost_per_elastigroup(group_id: str,
                                              to_date: str,
                                              from_date: str)
```

Get financial information on a specific Elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __to_date (String) (Optional)__: Get items on or before this date (ISO 8601 or Unix timestamp)
- __from_date (String) (Optional)__: Get items on or after this date (ISO 8601 or Unix timestamp)

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupGcpClient.get_elastigroup_activity">get_elastigroup_activity</h2>

```python
ElastigroupGcpClient.get_elastigroup_activity(group_id: str,
                                              start_date: str,
                                              end_date: str)
```

Get all activity events for the Elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __start_date (String)__: Date when to start checking
- __end_date (String)__: Get items on or before this date (ISO 8601)

__Returns__

`(Object) `: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupGcpClient.detach_elastigroup_instances">detach_elastigroup_instances</h2>

```python
ElastigroupGcpClient.detach_elastigroup_instances(
  group_id: str, detach_configuration: DetachConfiguration)
```

Detach instances from an Elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __detatch_configuration (DetachConfiguration)__: DetachConfiguration Object

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupGcpClient.get_elastilog">get_elastilog</h2>

```python
ElastigroupGcpClient.get_elastilog(group_id: str, start_date: str,
                                   end_date: str, limit: int)
```

Fetch a group's Elastilog

__Arguments__

- __group_id (String)__: Elastigroup ID
- __start_date (String)__: Get items on or after this date (ISO 8601 or Unix timestamp)
- __end_date (String)__: Get items on or before this date (ISO 8601 or Unix timestamp)
- __limit (Integer)__: Maximum number of items to return.

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupGcpClient.get_cost_per_account">get_cost_per_account</h2>

```python
ElastigroupGcpClient.get_cost_per_account(start_date: str,
                                          end_date: str)
```

Retrieve costs up to one year back per specified account over a specified time period.

__Arguments__

- __start_date (String)__: The start date of the requested time period. The value cannot be earlier than 1 year back.
- __end_date (String)__: The end date of the requested time period. The maximum of time period length is 90 days.

__Returns__

`(Object)`: Cost per Account Response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupGcpClient.get_instance_status">get_instance_status</h2>

```python
ElastigroupGcpClient.get_instance_status(instance_id: str)
```

Get the current instance status. Possible status values: ACTIVE, TERMINATING

__Arguments__

- __instance_id (String)__: GCP Instance ID

__Returns__

(Object) Elastigroup API Response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupGcpClient.lock_instance">lock_instance</h2>

```python
ElastigroupGcpClient.lock_instance(instance_id: str,
                                   ttl_in_minutes: str)
```

Set termination protection for a specific instance.

__Arguments__

- __instance_id (String)__: GCP Instance ID
- __ttl_in_minutes (String)__: Specify a TTL (in minutes) for this lock, i.e.: for how long the protection will be valid for.

__Returns__

(Object) Spotinst API Response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupGcpClient.unlock_instance">unlock_instance</h2>

```python
ElastigroupGcpClient.unlock_instance(instance_id: str)
```

Remove termination protection for a specific instance.

__Arguments__

- __instance_id (String)__: GCP Instance ID

__Returns__

`(Object)`: Spotinst API response

