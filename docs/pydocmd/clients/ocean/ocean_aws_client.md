<h1 id="spotinst_sdk.clients.ocean.OceanAwsClient">OceanAwsClient</h1>

```python
OceanAwsClient(self, session=None, print_output=True, log_level=None, user_agent=None)
```

<h2 id="spotinst_sdk.clients.ocean.OceanAwsClient.create_ocean_cluster">create_ocean_cluster</h2>

```python
OceanAwsClient.create_ocean_cluster(self, ocean)
```

Create an Ocean Cluster

__Arguments__

- __ocean (Ocean)__: Ocean Object

__Returns__

`(Object)`: Ocean API response

<h2 id="spotinst_sdk.clients.ocean.OceanAwsClient.update_ocean_cluster">update_ocean_cluster</h2>

```python
OceanAwsClient.update_ocean_cluster(self, ocean_id, ocean)
```

Update an exsisting Ocean Cluster

__Arguments__

- __ocean_id (String)__: Ocean id
- __ocean (Ocean)__: Ocean Object

__Returns__

`(Object)`: Ocean API response

<h2 id="spotinst_sdk.clients.ocean.OceanAwsClient.get_all_ocean_cluster">get_all_ocean_cluster</h2>

```python
OceanAwsClient.get_all_ocean_cluster(self)
```

Get all Ocean in account

__Returns__

`(Object)`: Ocean API response

<h2 id="spotinst_sdk.clients.ocean.OceanAwsClient.get_ocean_cluster">get_ocean_cluster</h2>

```python
OceanAwsClient.get_ocean_cluster(self, ocean_id)
```

Get an exsisting Ocean Cluster json

__Arguments__

- __ocean_id (String)__: Ocean id

__Returns__

`(Object)`: Ocean API response

<h2 id="spotinst_sdk.clients.ocean.OceanAwsClient.delete_ocean_cluster">delete_ocean_cluster</h2>

```python
OceanAwsClient.delete_ocean_cluster(self, ocean_id)
```

Delete an Ocean Cluster

__Arguments__

- __ocean_id (String)__: Ocean id

__Returns__

`(Object)`: Elastigroup API response

