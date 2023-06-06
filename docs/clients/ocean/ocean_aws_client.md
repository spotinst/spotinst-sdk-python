<h1 id="spotinst_sdk2.clients.ocean.OceanAwsClient">OceanAwsClient</h1>

```python
OceanAwsClient(self,
               session=None,
               print_output=True,
               log_level=None,
               user_agent=None,
               timeout=None)
```

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.create_ocean_cluster">create_ocean_cluster</h2>

```python
OceanAwsClient.create_ocean_cluster(ocean: Ocean)
```

Create an Ocean Cluster

__Arguments__

- __ocean (Ocean)__: Ocean Object

__Returns__

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.update_ocean_cluster">update_ocean_cluster</h2>

```python
OceanAwsClient.update_ocean_cluster(ocean_id: str,
                                    ocean: Ocean,
                                    auto_apply_tags: str = None)
```

Update an existing Ocean Cluster

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __auto_apply_tags (String)__: Option to update instance tags on the fly without rolling the cluster.
- __ocean (Ocean)__: Ocean object

__Returns__

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.get_all_ocean_cluster">get_all_ocean_cluster</h2>

```python
OceanAwsClient.get_all_ocean_cluster()
```

List the configurations for all Ocean clusters in the specified account.

__Returns__

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.get_all_ocean_sizing">get_all_ocean_sizing</h2>

```python
OceanAwsClient.get_all_ocean_sizing(ocean_id: str, namespace: str)
```

Get all right sizing recommendations for an Ocean cluster

__Returns__

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.fetch_rightsizing_recommendations">fetch_rightsizing_recommendations</h2>

```python
OceanAwsClient.fetch_rightsizing_recommendations(
  ocean_id: str, filter: RightSizingRecommendationFilter = None)
```

Get right-sizing recommendations for an Ocean cluster and filter them according to namespace or label.

__Arguments__

- __ocean_id (String)__: Id of the Ocean Cluster
- __filter (RightSizingRecommendationFilter)__: Optional - may be null.

__Returns__

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.get_ocean_cluster">get_ocean_cluster</h2>

```python
OceanAwsClient.get_ocean_cluster(ocean_id: str)
```

Get an exsisting Ocean Cluster json

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster

__Returns__

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.delete_ocean_cluster">delete_ocean_cluster</h2>

```python
OceanAwsClient.delete_ocean_cluster(ocean_id: str)
```

Delete an Ocean Cluster

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster

__Returns__

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.get_aggregated_cluster_costs">get_aggregated_cluster_costs</h2>

```python
OceanAwsClient.get_aggregated_cluster_costs(
  ocean_id: str, aggregated_cluster_costs: AggregatedClusterCosts)
```

Get aggregated cluster costs

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __aggregated_cluster_costs (AggregatedClusterCosts)__: Aggregated Cluster Costs request

__Returns__

`(Object)`: Aggregated Cluster Costs API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.initiate_roll">initiate_roll</h2>

```python
OceanAwsClient.initiate_roll(ocean_id: str, cluster_roll: Roll)
```

Initiate Cluster Rolls

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __cluster_roll (Roll)__: Cluster Roll / Roll with Instance Ids/ Launch specification Ids

__Returns__

`(Object)`: Cluster Roll API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.list_rolls">list_rolls</h2>

```python
OceanAwsClient.list_rolls(ocean_id: str)
```

Get status for all rolls of an Ocean cluster.

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster

__Returns__

`(Object)`: List of Cluster Roll API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.update_roll">update_roll</h2>

```python
OceanAwsClient.update_roll(ocean_id: str, roll_id: str, status: str)
```

Update a roll of an Ocean cluster.
Performing the request will stop the next batch in a roll.

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __roll_id (String)__: Ocean cluster roll identifier
- __update_roll (UpdateRoll)__: update roll request

__Returns__

`(Object)`: Cluster Roll API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.get_roll">get_roll</h2>

```python
OceanAwsClient.get_roll(ocean_id: str, roll_id: str)
```

Get status for a roll of an Ocean cluster.

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __account_id (String)__: The ID of the account associated with your token.
- __roll_id (String)__: Ocean cluster roll identifier

__Returns__

`(Object)`: Cluster Roll API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.get_cluster_nodes">get_cluster_nodes</h2>

```python
OceanAwsClient.get_cluster_nodes(ocean_id: str,
                                 instance_id: str = None,
                                 launch_spec_id: str = None)
```

Get nodes data of an Ocean cluster.

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __instance_id (String)__: Get a specific node by instance id
- __launch_spec_id (String)__: Ocean cluster launch specification identifier.

__Returns__

`(Object)`: Ocean Kubernetes AWS Nodes Data response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.get_heartbeat_status">get_heartbeat_status</h2>

```python
OceanAwsClient.get_heartbeat_status(ocean_id: str)
```

Get the heartbeat status of the Ocean Controller for the cluster.
The response returns the heartbeat status and the last heartbeat timestamp.

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster

__Returns__

`(Object)`: Ocean Get Heartbeat response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.instance_types_filter_simulation">instance_types_filter_simulation</h2>

```python
OceanAwsClient.instance_types_filter_simulation(
  ocean_id: str, instance_type_filter: InstanceTypesFilters)
```

Returns all instances types that match the given filters.
These instance types will be used if the cluster is configured with these filters.

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __instance_type_filter (InstanceTypesFilters)__: The Instance types that match with all filters compose the
Ocean's whitelist parameter. Cannot be configured together with whitelist/blacklist.

__Returns__

`(Object)`: Ocean Instance Types Filter Simulation response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.allowed_instance_types">allowed_instance_types</h2>

```python
OceanAwsClient.allowed_instance_types(ocean_id: str)
```

Return the list of the allowed Ocean cluster instance types.

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster

__Returns__

`(Object)`: Ocean Allowed Instance Types response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.get_virtual_node_group">get_virtual_node_group</h2>

```python
OceanAwsClient.get_virtual_node_group(ocean_launch_spec_id: str)
```

Get Virtual Node Group of the cluster

__Arguments__

- __ocean_launch_spec_id (String)__: Ocean cluster launch specification identifier

__Returns__

`(Object)`: Ocean Allowed Instance Types response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.launch_nodes_in_vng">launch_nodes_in_vng</h2>

```python
OceanAwsClient.launch_nodes_in_vng(ocean_launch_spec_id: str,
                                   amount: int)
```

Launch nodes in Virtual Node Group.

__Arguments__

- __ocean_launch_spec_id (String)__: Ocean cluster launch specification identifier.
- __launch_nodes (LaunchNodes)__: Object specifying the details for the launch request.

__Returns__

`(Object)`: Ocean Virtual Node Group Launch API response

