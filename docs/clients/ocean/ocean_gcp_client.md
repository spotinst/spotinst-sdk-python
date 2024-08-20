<h1 id="spotinst_sdk2.clients.ocean.OceanGcpClient">OceanGcpClient</h1>

```python
OceanGcpClient(self,
               session=None,
               print_output=True,
               log_level=None,
               user_agent=None,
               timeout=None)
```

<h2 id="spotinst_sdk2.clients.ocean.OceanGcpClient.get_heartbeat_status">get_heartbeat_status</h2>

```python
OceanGcpClient.get_heartbeat_status(ocean_id: str)
```

Get the heartbeat status of the Ocean Controller for the cluster.
The response returns the heartbeat status and the last heartbeat timestamp.

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster

__Returns__

`(Object)`: Ocean Get Heartbeat response

<h2 id="spotinst_sdk2.clients.ocean.OceanGcpClient.create_ocean_cluster">create_ocean_cluster</h2>

```python
OceanGcpClient.create_ocean_cluster(ocean: Ocean)
```

Create an Ocean Cluster

__Arguments__

- __ocean (Ocean)__: Ocean Object

__Returns__

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanGcpClient.get_all_ocean_clusters">get_all_ocean_clusters</h2>

```python
OceanGcpClient.get_all_ocean_clusters()
```

List the configurations for all Ocean clusters in the specified account.

__Returns__

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanGcpClient.delete_ocean_cluster">delete_ocean_cluster</h2>

```python
OceanGcpClient.delete_ocean_cluster(ocean_id: str)
```

Delete a specified Ocean cluster.

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster

__Returns__

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanGcpClient.get_ocean_cluster">get_ocean_cluster</h2>

```python
OceanGcpClient.get_ocean_cluster(ocean_id: str)
```

Get the configuration for a specified Ocean cluster.

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster

__Returns__

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanGcpClient.update_ocean_cluster">update_ocean_cluster</h2>

```python
OceanGcpClient.update_ocean_cluster(ocean_id: str, ocean: Ocean)
```

Update an existing Ocean Cluster

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __ocean (Ocean)__: Ocean object

__Returns__

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanGcpClient.reimport_ocean_cluster">reimport_ocean_cluster</h2>

```python
OceanGcpClient.reimport_ocean_cluster(ocean_id: str)
```

Reimport the cluster's configuration from GKE.

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __ocean (Ocean)__: Ocean object

__Returns__

`(Object)`: Reimport cluster response

<h2 id="spotinst_sdk2.clients.ocean.OceanGcpClient.get_elastilog">get_elastilog</h2>

```python
OceanGcpClient.get_elastilog(ocean_id: str,
                             from_date: str,
                             to_date: str,
                             severity: str = None,
                             resource_id: str = None,
                             limit: int = None)
```

Get group's Elastilog by

__Arguments__

- __to_date (String)__: end date value
- __from_date (String)__: beginning date value
- __severity(String) (Optional)__: Log level severity
- __resource_id(String) (Optional)__: specific resource identifier
- __limit(int) (Optional)__: Maximum number of lines to extract in a response

__Returns__

`(Object)`: Ocean Get Log API response

<h2 id="spotinst_sdk2.clients.ocean.OceanGcpClient.get_rightsizing_recommendations">get_rightsizing_recommendations</h2>

```python
OceanGcpClient.get_rightsizing_recommendations(
  ocean_id: str, filter: RightSizingRecommendationFilter = None)
```

Get right-sizing recommendations for an Ocean cluster and filter them according to namespace or label.

__Arguments__

- __ocean_id (String)__: Id of the Ocean Cluster
- __filter (RightSizingRecommendationFilter)__: Optional - may be null.

__Returns__

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanGcpClient.get_aggregated_cluster_costs">get_aggregated_cluster_costs</h2>

```python
OceanGcpClient.get_aggregated_cluster_costs(
  ocean_id: str, aggregated_cluster_costs: AggregatedClusterCosts)
```

Get aggregated cluster costs

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __aggregated_cluster_costs (AggregatedClusterCosts)__: Aggregated Cluster Costs request

__Returns__

`(Object)`: Aggregated Cluster Costs API response

<h2 id="spotinst_sdk2.clients.ocean.OceanGcpClient.get_aggregated_summary_costs">get_aggregated_summary_costs</h2>

```python
OceanGcpClient.get_aggregated_summary_costs(
  ocean_id: str, aggregated_cluster_costs: AggregatedClusterCosts)
```

Get aggregated cluster costs

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __aggregated_cluster_costs (AggregatedClusterCosts)__: Aggregated Cluster Costs request

__Returns__

`(Object)`: Aggregated Cluster Costs API response

<h2 id="spotinst_sdk2.clients.ocean.OceanGcpClient.create_virtual_node_group">create_virtual_node_group</h2>

```python
OceanGcpClient.create_virtual_node_group(vng: VirtualNodeGroup,
                                         initial_nodes: int = None)
```

Create a virtual node group.

__Arguments__

- __vng (VirtualNodeGroup)__: VirtualNodeGroup Object
- __initial_nodes__: When set to an integer greater than 0, a corresponding number of nodes will be launched from the virtual node group created.

__Returns__

`(Object)`: Ocean Launch Spec response

<h2 id="spotinst_sdk2.clients.ocean.OceanGcpClient.get_all_virtual_node_groups">get_all_virtual_node_groups</h2>

```python
OceanGcpClient.get_all_virtual_node_groups(ocean_id: str)
```

List the configurations for all virtual node groups in the account
or in a specified cluster.

__Returns__

`(Object)`: Ocean VNG API response

<h2 id="spotinst_sdk2.clients.ocean.OceanGcpClient.import_gke_nodepool_to_vng_configuration">import_gke_nodepool_to_vng_configuration</h2>

```python
OceanGcpClient.import_gke_nodepool_to_vng_configuration(
  node_pool_name: str, ocean_id: str)
```

Import GKE Nodepool configurations and generate valid Ocean Virtual Node Group (VNG) configuration
which can be used to create VNGs

__Returns__

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanGcpClient.delete_virtual_node_group">delete_virtual_node_group</h2>

```python
OceanGcpClient.delete_virtual_node_group(vng_id: str,
                                         delete_nodes: bool = None)
```

Delete an Ocean Cluster

__Arguments__

- __vng_id (String)__: ID of the Ocean VNG
- __delete_nodes (Bool)__: When set to "true", all instances belonging to the deleted launch specification will be drained, detached, and terminated.

__Returns__

`(Object)`: Ocean Launch Specification Delete response

<h2 id="spotinst_sdk2.clients.ocean.OceanGcpClient.update_virtual_node_group">update_virtual_node_group</h2>

```python
OceanGcpClient.update_virtual_node_group(vng_id: str,
                                         vng: VirtualNodeGroup)
```

Update an existing VNG inside an Ocean Cluster

__Arguments__

- __vng_id (String)__: ID of the Ocean Virtual Node Group
- __ocean (Ocean)__: Ocean object

__Returns__

`(Object)`: Ocean Launch Spec response

<h2 id="spotinst_sdk2.clients.ocean.OceanGcpClient.get_virtual_node_group">get_virtual_node_group</h2>

```python
OceanGcpClient.get_virtual_node_group(ocean_launch_spec_id: str)
```

Get Virtual Node Group of the cluster

__Arguments__

- __ocean_launch_spec_id (String)__: Ocean cluster launch specification identifier

__Returns__

`(Object)`: Ocean Allowed Instance Types response

<h2 id="spotinst_sdk2.clients.ocean.OceanGcpClient.initiate_roll">initiate_roll</h2>

```python
OceanGcpClient.initiate_roll(ocean_id: str, cluster_roll: Roll)
```

Initiate Cluster Rolls

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __cluster_roll (Roll)__: Cluster Roll / Roll with Instance Ids/ Launch specification Ids

__Returns__

`(Object)`: Cluster Roll API response

<h2 id="spotinst_sdk2.clients.ocean.OceanGcpClient.list_rolls">list_rolls</h2>

```python
OceanGcpClient.list_rolls(ocean_id: str)
```

Get status for all rolls of an Ocean cluster.

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster

__Returns__

`(Object)`: List of Cluster Roll API response

<h2 id="spotinst_sdk2.clients.ocean.OceanGcpClient.update_roll">update_roll</h2>

```python
OceanGcpClient.update_roll(ocean_id: str, roll_id: str, status: str)
```

Update a roll of an Ocean cluster.
Performing the request will stop the next batch in a roll.

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __roll_id (String)__: Ocean cluster roll identifier
- __update_roll (UpdateRoll)__: update roll request

__Returns__

`(Object)`: Cluster Roll API response

<h2 id="spotinst_sdk2.clients.ocean.OceanGcpClient.get_roll">get_roll</h2>

```python
OceanGcpClient.get_roll(ocean_id: str, roll_id: str)
```

Get status for a roll of an Ocean cluster.

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __account_id (String)__: The ID of the account associated with your token.
- __roll_id (String)__: Ocean cluster roll identifier

__Returns__

`(Object)`: Cluster Roll API response

<h2 id="spotinst_sdk2.clients.ocean.OceanGcpClient.get_cluster_nodes">get_cluster_nodes</h2>

```python
OceanGcpClient.get_cluster_nodes(ocean_id: str,
                                 instance_name: str = None,
                                 launch_spec_id: str = None)
```

Get nodes data of an Ocean cluster.

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __instance_name (String)__: Get a specific node by instance id
- __launch_spec_id (String)__: Ocean cluster launch specification identifier.

__Returns__

`(Object)`: Ocean Kubernetes AWS Nodes Data response

<h2 id="spotinst_sdk2.clients.ocean.OceanGcpClient.update_elastigroup_to_ocean">update_elastigroup_to_ocean</h2>

```python
OceanGcpClient.update_elastigroup_to_ocean(group_id: str)
```

Upgrade an Elastigroup with Kubernetes integration to Ocean for Kubernetes cluster.

__Arguments__

- __group_id (str)__: Elastigroup identifier

__Returns__

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanGcpClient.import_gke_cluster_to_ocean">import_gke_cluster_to_ocean</h2>

```python
OceanGcpClient.import_gke_cluster_to_ocean(
  cluster_name: str,
  location: str,
  import_gke_to_ocean: ImportGkeClusterToOcean,
  include_launchSpecs: bool = None,
  node_pool_name: str = None)
```

Create an Ocean configuration according to an GKE Cluster configuration.

__Arguments__

- __cluster_name (String)__: Name of the GKE Cluster.
- __include_launchSpecs (String)__: When set to "true", GKE cluster node pools will be imported to Ocean custom VNG ("customLaunchSpec") configurations.
- __location (String)__: Location GKE Cluster Master.
- __node_pool_name (String)__: Name of the Node Pool to use as a default for the Cluster configuration.
- __import_gke_to_ocean (ImportGkeClusterToOcean)__: ImportGkeClusterToOcean Object

__Returns__

`(Object)`: Ocean GKE Cluster Import Response

<h2 id="spotinst_sdk2.clients.ocean.OceanGcpClient.launch_nodes_in_vng">launch_nodes_in_vng</h2>

```python
OceanGcpClient.launch_nodes_in_vng(ocean_launch_spec_id: str,
                                   amount: int)
```

Launch nodes in Virtual Node Group.

__Arguments__

- __ocean_launch_spec_id (String)__: Ocean cluster launch specification identifier.
- __amount (int)__: The number of nodes to launch.

__Returns__

`(Object)`: Ocean Virtual Node Group Launch API response

