<h1 id="spotinst_sdk2.clients.ocean.OceanAzureClient">OceanAzureClient</h1>

```python
OceanAzureClient(self,
                 session=None,
                 print_output=True,
                 log_level=None,
                 user_agent=None,
                 timeout=None)
```

<h2 id="spotinst_sdk2.clients.ocean.OceanAzureClient.create_ocean_cluster">create_ocean_cluster</h2>

```python
OceanAzureClient.create_ocean_cluster(ocean: Ocean)
```

Create an Ocean Cluster

__Arguments__

- __ocean (Ocean)__: Ocean Object

__Returns__

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAzureClient.get_all_ocean_clusters">get_all_ocean_clusters</h2>

```python
OceanAzureClient.get_all_ocean_clusters()
```

List the configurations for all Ocean clusters in the specified account.

__Returns__

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAzureClient.get_ocean_cluster">get_ocean_cluster</h2>

```python
OceanAzureClient.get_ocean_cluster(ocean_id: str)
```

Get an existing Ocean Cluster json

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster

__Returns__

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAzureClient.delete_ocean_cluster">delete_ocean_cluster</h2>

```python
OceanAzureClient.delete_ocean_cluster(ocean_id: str)
```

Delete an Ocean Cluster

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster

__Returns__

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAzureClient.update_ocean_cluster">update_ocean_cluster</h2>

```python
OceanAzureClient.update_ocean_cluster(ocean_id: str, ocean: Ocean)
```

Update an existing Ocean Cluster

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __ocean (Ocean)__: Ocean object

__Returns__

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAzureClient.import_cluster_configuration">import_cluster_configuration</h2>

```python
OceanAzureClient.import_cluster_configuration(aks_cluster_name: str,
                                              resource_group_name: str)
```

Import cluster configuration of an AKS cluster to use in create_ocean_cluster api call

__Arguments__

- __aks_cluster_name (String)__: Name of the AKS cluster
- __resource_group_name (String)__: Resource Group Name

__Returns__

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAzureClient.create_ocean_vng">create_ocean_vng</h2>

```python
OceanAzureClient.create_ocean_vng(vng: VirtualNodeGroupTemplate)
```

Create a VNG inside ocean cluster

__Arguments__

- __vng (VirtualNodeGroup)__: VirtualNodeGroup Object

__Returns__

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAzureClient.update_ocean_vng">update_ocean_vng</h2>

```python
OceanAzureClient.update_ocean_vng(vng_id: str,
                                  vng: VirtualNodeGroupTemplate)
```

Update an existing VNG inside an Ocean Cluster

__Arguments__

- __vng_id (String)__: ID of the Ocean Virtual Node Group
- __ocean (Ocean)__: Ocean object

__Returns__

`(Object)`: Ocean VNG API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAzureClient.get_ocean_vng">get_ocean_vng</h2>

```python
OceanAzureClient.get_ocean_vng(vng_id: str)
```

Get an existing Ocean Virtual Node Group json

__Arguments__

- __vng_id (String)__: ID of the Ocean VNG

__Returns__

`(Object)`: Ocean VNG API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAzureClient.get_all_ocean_vngs">get_all_ocean_vngs</h2>

```python
OceanAzureClient.get_all_ocean_vngs(ocean_id: str = None)
```

List the configurations for all virtual node groups in the account
or in a specified cluster.

__Returns__

`(Object)`: Ocean VNG API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAzureClient.delete_ocean_vng">delete_ocean_vng</h2>

```python
OceanAzureClient.delete_ocean_vng(vng_id: str)
```

Delete an Ocean Cluster

__Arguments__

- __vng_id (String)__: ID of the Ocean VNG

__Returns__

`(Object)`: Ocean VNG API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAzureClient.import_vng_configuration">import_vng_configuration</h2>

```python
OceanAzureClient.import_vng_configuration(node_pool_name: str,
                                          ocean_id: str)
```

Import cluster configuration of an AKS cluster to use in create_ocean_cluster api call

__Returns__

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAzureClient.launch_new_nodes">launch_new_nodes</h2>

```python
OceanAzureClient.launch_new_nodes(node_config: LaunchNewNodes)
```

Launch new nodes for a cluster

__Arguments__

- __node_config (LaunchNewNodes)__: LaunchNewNodes object

__Returns__

`(Object)`: Ocean Launch New Nodes API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAzureClient.get_allowed_vng_vm_sizes">get_allowed_vng_vm_sizes</h2>

```python
OceanAzureClient.get_allowed_vng_vm_sizes(vng_id: str)
```

Get allowed vm sizes for a particular VNG

__Arguments__

- __vng_id (String)__: ID of the Ocean VNG

__Returns__

`(Object)`: Array of allowed vm sizes list

<h2 id="spotinst_sdk2.clients.ocean.OceanAzureClient.initiate_roll">initiate_roll</h2>

```python
OceanAzureClient.initiate_roll(ocean_id: str, cluster_roll: Roll)
```

Initiate Cluster Rolls

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __cluster_roll (Roll)__: Cluster Roll / Node Pool names/ VNG Ids

__Returns__

`(Object)`: Cluster Roll API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAzureClient.get_roll">get_roll</h2>

```python
OceanAzureClient.get_roll(ocean_id: str, roll_id: str)
```

Get status for a roll of an Ocean cluster.

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __account_id (String)__: The ID of the account associated with your token.
- __roll_id (String)__: Ocean cluster roll identifier

__Returns__

`(Object)`: Cluster Roll API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAzureClient.list_rolls">list_rolls</h2>

```python
OceanAzureClient.list_rolls(ocean_id: str)
```

Get status for all rolls of an Ocean cluster.

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster

__Returns__

`(Object)`: List of Cluster Roll API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAzureClient.stop_roll">stop_roll</h2>

```python
OceanAzureClient.stop_roll(ocean_id: str, roll_id: str)
```

Stop roll of an Ocean cluster.

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __account_id (String)__: The ID of the account associated with your token.
- __roll_id (String)__: Ocean cluster roll identifier

__Returns__

`(Object)`: Cluster Roll API response

