<h1 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureClient">ElastigroupAzureClient</h1>

```python
ElastigroupAzureClient(self, session=None, print_output=True, log_level=None, user_agent=None)
```

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureClient.create_elastigroup">create_elastigroup</h2>

```python
ElastigroupAzureClient.create_elastigroup(self, group)
```

Create an elastigroup

__Arguments__

- __group (Elastigroup)__: Elastigroup Object

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureClient.update_elastigroup">update_elastigroup</h2>

```python
ElastigroupAzureClient.update_elastigroup(self, group_update, group_id)
```

Update an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __group_update (Elastigroup)__: Elastigroup Object

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureClient.delete_elastigroup">delete_elastigroup</h2>

```python
ElastigroupAzureClient.delete_elastigroup(self, group_id)
```

Delete an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureClient.get_elastigroup">get_elastigroup</h2>

```python
ElastigroupAzureClient.get_elastigroup(self, group_id)
```

Get an elastigroup

__Arguments__

- __group_id(String)__: Elastigroup ID

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.elastigroup.ElastigroupAzureClient.get_elastigroups">get_elastigroups</h2>

```python
ElastigroupAzureClient.get_elastigroups(self)
```

Get all elastigroup

__Returns__

`(List)`: List of Elastigroup API response

