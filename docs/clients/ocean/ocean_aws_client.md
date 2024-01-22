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

**Arguments**

- **ocean (Ocean)**: Ocean Object

**Returns**

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.update_ocean_cluster">update_ocean_cluster</h2>

```python
OceanAwsClient.update_ocean_cluster(ocean_id: str,
                                    ocean: Ocean,
                                    auto_apply_tags: str = None)
```

Update an existing Ocean Cluster

**Arguments**

- **ocean_id (String)**: ID of the Ocean Cluster
- **auto_apply_tags (String)**: Option to update instance tags on the fly without rolling the cluster.
- **ocean (Ocean)**: Ocean object

**Returns**

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.get_all_ocean_cluster">get_all_ocean_cluster</h2>

```python
OceanAwsClient.get_all_ocean_cluster()
```

List the configurations for all Ocean clusters in the specified account.

**Returns**

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.get_all_ocean_sizing">get_all_ocean_sizing</h2>

```python
OceanAwsClient.get_all_ocean_sizing(ocean_id: str, namespace: str)
```

Get all right sizing recommendations for an Ocean cluster

**Returns**

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.fetch_rightsizing_recommendations">fetch_rightsizing_recommendations</h2>

```python
OceanAwsClient.fetch_rightsizing_recommendations(
  ocean_id: str, filter: RightSizingRecommendationFilter = None)
```

Get right-sizing recommendations for an Ocean cluster and filter them according to namespace or label.

**Arguments**

- **ocean_id (String)**: Id of the Ocean Cluster
- **filter (RightSizingRecommendationFilter)**: Optional - may be null.

**Returns**

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.get_ocean_cluster">get_ocean_cluster</h2>

```python
OceanAwsClient.get_ocean_cluster(ocean_id: str)
```

Get an existing Ocean Cluster json

**Arguments**

- **ocean_id (String)**: ID of the Ocean Cluster

**Returns**

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.delete_ocean_cluster">delete_ocean_cluster</h2>

```python
OceanAwsClient.delete_ocean_cluster(ocean_id: str)
```

Delete an Ocean Cluster

**Arguments**

- **ocean_id (String)**: ID of the Ocean Cluster

**Returns**

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.get_aggregated_cluster_costs">get_aggregated_cluster_costs</h2>

```python
OceanAwsClient.get_aggregated_cluster_costs(
  ocean_id: str, aggregated_cluster_costs: AggregatedClusterCosts)
```

Get aggregated cluster costs

**Arguments**

- **ocean_id (String)**: ID of the Ocean Cluster
- **aggregated_cluster_costs (AggregatedClusterCosts)**: Aggregated Cluster Costs request

**Returns**

`(Object)`: Aggregated Cluster Costs API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.initiate_roll">initiate_roll</h2>

```python
OceanAwsClient.initiate_roll(ocean_id: str, cluster_roll: Roll)
```

Initiate Cluster Rolls

**Arguments**

- **ocean_id (String)**: ID of the Ocean Cluster
- **cluster_roll (Roll)**: Cluster Roll / Roll with Instance Ids/ Launch specification Ids

**Returns**

`(Object)`: Cluster Roll API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.list_rolls">list_rolls</h2>

```python
OceanAwsClient.list_rolls(ocean_id: str)
```

Get status for all rolls of an Ocean cluster.

**Arguments**

- **ocean_id (String)**: ID of the Ocean Cluster

**Returns**

`(Object)`: List of Cluster Roll API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.update_roll">update_roll</h2>

```python
OceanAwsClient.update_roll(ocean_id: str, roll_id: str, status: str)
```

Update a roll of an Ocean cluster.
Performing the request will stop the next batch in a roll.

**Arguments**

- **ocean_id (String)**: ID of the Ocean Cluster
- **roll_id (String)**: Ocean cluster roll identifier
- **update_roll (UpdateRoll)**: update roll request

**Returns**

`(Object)`: Cluster Roll API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.get_roll">get_roll</h2>

```python
OceanAwsClient.get_roll(ocean_id: str, roll_id: str)
```

Get status for a roll of an Ocean cluster.

**Arguments**

- **ocean_id (String)**: ID of the Ocean Cluster
- **account_id (String)**: The ID of the account associated with your token.
- **roll_id (String)**: Ocean cluster roll identifier

**Returns**

`(Object)`: Cluster Roll API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.get_cluster_nodes">get_cluster_nodes</h2>

```python
OceanAwsClient.get_cluster_nodes(ocean_id: str,
                                 instance_id: str = None,
                                 launch_spec_id: str = None)
```

Get nodes data of an Ocean cluster.

**Arguments**

- **ocean_id (String)**: ID of the Ocean Cluster
- **instance_id (String)**: Get a specific node by instance id
- **launch_spec_id (String)**: Ocean cluster launch specification identifier.

**Returns**

`(Object)`: Ocean Kubernetes AWS Nodes Data response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.get_heartbeat_status">get_heartbeat_status</h2>

```python
OceanAwsClient.get_heartbeat_status(ocean_id: str)
```

Get the heartbeat status of the Ocean Controller for the cluster.
The response returns the heartbeat status and the last heartbeat timestamp.

**Arguments**

- **ocean_id (String)**: ID of the Ocean Cluster

**Returns**

`(Object)`: Ocean Get Heartbeat response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.instance_types_filter_simulation">instance_types_filter_simulation</h2>

```python
OceanAwsClient.instance_types_filter_simulation(
  ocean_id: str, instance_type_filter: InstanceTypesFilters)
```

Returns all instances types that match the given filters.
These instance types will be used if the cluster is configured with these filters.

**Arguments**

- **ocean_id (String)**: ID of the Ocean Cluster
- **instance_type_filter (InstanceTypesFilters)**: The Instance types that match with all filters compose the
  Ocean's whitelist parameter. Cannot be configured together with whitelist/blacklist.

**Returns**

`(Object)`: Ocean Instance Types Filter Simulation response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.allowed_instance_types">allowed_instance_types</h2>

```python
OceanAwsClient.allowed_instance_types(ocean_id: str)
```

Return the list of the allowed Ocean cluster instance types.

**Arguments**

- **ocean_id (String)**: ID of the Ocean Cluster

**Returns**

`(Object)`: Ocean Allowed Instance Types response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.get_virtual_node_group">get_virtual_node_group</h2>

```python
OceanAwsClient.get_virtual_node_group(ocean_launch_spec_id: str)
```

Get Virtual Node Group of the cluster

**Arguments**

- **ocean_launch_spec_id (String)**: Ocean cluster launch specification identifier

**Returns**

`(Object)`: Ocean Allowed Instance Types response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.launch_nodes_in_vng">launch_nodes_in_vng</h2>

```python
OceanAwsClient.launch_nodes_in_vng(ocean_launch_spec_id: str,
                                   amount: int)
```

Launch nodes in Virtual Node Group.

**Arguments**

- **ocean_launch_spec_id (String)**: Ocean cluster launch specification identifier.
- **amount (int)**: The number of nodes to launch.

**Returns**

`(Object)`: Ocean Virtual Node Group Launch API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.fetch_elastilog">fetch_elastilog</h2>

```python
OceanAwsClient.fetch_elastilog(ocean_id,
                               from_date,
                               to_date,
                               severity=None,
                               resource_id=None,
                               limit=None)
```

Create an Ocean configuration according to an AWS autoscaling group (ASG) configuration.

**Arguments**

- **to_date (String)**: to date
- **from_date (String)**: to date
- **severity(String) (Optional)**: Log level severity
- **resource_id(String) (Optional)**: Filter log extracted entires related to a
  specific resource id
- **limit(String) (Optional)**: Maximum number of lines to extract in a response

**Returns**

`(Object)`: Ocean Get Log API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.import_asg_to_ocean_cluster">import_asg_to_ocean_cluster</h2>

```python
OceanAwsClient.import_asg_to_ocean_cluster(
  auto_scaling_group_name, region,
  import_asg_to_ocean_cluster: ImportASGToOceanCluster)
```

Create an Ocean configuration according to an AWS autoscaling group (ASG) configuration.

**Arguments**

- **auto_scaling_group_name (String)**: The ASG name
- **region (String)**: region
- **import_asg_to_ocean_cluster (ImportASGToOceanCluster)**: ImportASGToOceanCluster Object

**Returns**

`(Object)`: Ocean Import ASG to Ocean Response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.create_virtual_node_group">create_virtual_node_group</h2>

```python
OceanAwsClient.create_virtual_node_group(vng: VirtualNodeGroup,
                                         initial_nodes: int = None)
```

Create a VNG inside ocean cluster

**Arguments**

- **vng (VirtualNodeGroup)**: VirtualNodeGroup Object
- **initial_nodes**: When set to an integer greater than 0, a corresponding number of nodes will be launched from the virtual node group created.

**Returns**

`(Object)`: Ocean Launch Spec response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.update_virtual_node_group">update_virtual_node_group</h2>

```python
OceanAwsClient.update_virtual_node_group(vng_id: str,
                                         vng: VirtualNodeGroup,
                                         auto_apply_tags: bool = None)
```

Update an existing VNG inside an Ocean Cluster

**Arguments**

- **vng_id (String)**: ID of the Ocean Virtual Node Group
- **ocean (Ocean)**: Ocean object

**Returns**

`(Object)`: Ocean Launch Spec response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.get_all_virtual_node_groups">get_all_virtual_node_groups</h2>

```python
OceanAwsClient.get_all_virtual_node_groups(ocean_id: str = None)
```

List the configurations for all virtual node groups in the account
or in a specified cluster.

**Returns**

`(Object)`: Ocean Launch Spec response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.delete_virtual_node_group">delete_virtual_node_group</h2>

```python
OceanAwsClient.delete_virtual_node_group(vng_id: str,
                                         delete_nodes: bool = None,
                                         force_delete: bool = None)
```

Delete an Ocean Cluster

**Arguments**

- **vng_id (String)**: ID of the Ocean VNG
- **delete_nodes (Bool)**: When set to "true", all instances belonging to the deleted launch specification will be drained, detached, and terminated.
- **force_delete (Bool)**: When set to "true", delete even if it is the only custom launch spec remaining, and default launch spec has useAsTemplateOnly = true.

**Returns**

`(Object)`: Ocean Launch Specification Delete response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.attach_load_balancers">attach_load_balancers</h2>

```python
OceanAwsClient.attach_load_balancers(ocean_id: str, load_balancers)
```

Add new load balancers to the existing load balancers on the Ocean Cluster.

**Arguments**

- **ocean_id (String)**: ID of the Ocean Cluster
- **load_balancers (List[LoadBalancer])**: Load balancers to add to the Ocean cluster.

**Returns**

`(Object)`: Ocean Attach Load Balancers API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.detach_load_balancers">detach_load_balancers</h2>

```python
OceanAwsClient.detach_load_balancers(ocean_id, load_balancers)
```

Delete an Ocean Cluster

**Arguments**

- **ocean_id (String)**: ID of the Ocean Cluster
- **load_balancers (List[LoadBalancer])**: Load balancers to remove from the Ocean cluster.

**Returns**

`(Object)`: Ocean Detach Load Balancers API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.update_elastigroup_to_ocean">update_elastigroup_to_ocean</h2>

```python
OceanAwsClient.update_elastigroup_to_ocean(group_id: str)
```

Upgrade an Elastigroup with Kubernetes integration to Ocean for Kubernetes cluster.

**Arguments**

- **group_id (str)**: Elastigroup identifier

**Returns**

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.detach_instances">detach_instances</h2>

```python
OceanAwsClient.detach_instances(ocean_id: str,
                                detach_instances: DetachInstances)
```

Detach instances from your Ocean cluster.

**Arguments**

- **ocean_id (String)**: ID of the Ocean Cluster
- **detach_instances (DetachInstances)**: Detach Instances Request

**Returns**

`(Object)`: Detach Instances API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.instance_types_filter_simulation_for_vng">instance_types_filter_simulation_for_vng</h2>

```python
OceanAwsClient.instance_types_filter_simulation_for_vng(
  launch_spec_id: str, instance_types_filters: InstanceTypesFilters)
```

Returns all instance types that match the given filters. These instance types will be used if the Virtual Node Group is configured with these filters.

**Arguments**

- **launch_spec_id (String)**: Ocean cluster launch specification identifier.
- **instance_type_filters (InstanceTypesFilters)**: List of instance types filters. The instance types that match with all filters compose the Virtual Node Group's instanceTypes parameter.
  The architectures that come from the Virtual Node Group's images will be taken into account when using this parameter.
  Cannot be configured together with Virtual Node Group's instanceTypes and with the Cluster's whitelist/blacklist/filters.

**Returns**

`(Object)`: Ocean Instance Types Filter Simulation response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.import_asg_to_ocean_vng">import_asg_to_ocean_vng</h2>

```python
OceanAwsClient.import_asg_to_ocean_vng(
  auto_scaling_group_name, ocean_id: str,
  import_asg_to_ocean_launch_spec: ImportASGToOceanVNG)
```

Returns an Ocean Virtual Node Group (VNG) configuration in a given AWS autoscaling group (ASG). The returned value ("Imported VNG") can then be used as input to the Create Virtual Node Group API in order to create an actual VNG in your Ocean cluster.

**Arguments**

- **ocean_id (String)**: ID of the Ocean Cluster
- **auto_scaling_group_name (String)**: The ASG name.
- **import_asg_to_ocean_launch_spec (ImportASGToOceanVNG)**: ImportASGToOceanVNG object

**Returns**

`(Object)`: Ocean Import ASG to Launch Spec Response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.allowed_instance_types_by_filters_for_vng">allowed_instance_types_by_filters_for_vng</h2>

```python
OceanAwsClient.allowed_instance_types_by_filters_for_vng(
  launch_spec_id: str)
```

Returns the Virtual Node Group's instance types when instance types filters is set.

**Arguments**

- **launch_spec_id (String)**: Ocean Cluster Launch Specification Identifier

**Returns**

`(Object)`: Ocean Allowed Instance Types response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.import_eks_cluster_node_group_to_ocean_vng">import_eks_cluster_node_group_to_ocean_vng</h2>

```python
OceanAwsClient.import_eks_cluster_node_group_to_ocean_vng(
  eks_cluster_name: str,
  eks_node_group_name: str,
  import_eks_node_group_to_ocean_launch_spec:
    ImportEKSNodeGroupToOceanVNG,
  ocean_id: str = None,
  region: str = None)
```

Returns an Ocean Virtual Node Group (VNG) configuration based on a given AWS EKS Cluster Node Group.
The returned value ("Imported VNG") can then be used as input to the Create Virtual Node Group API in order to create an actual VNG in your Ocean cluster.

**Arguments**

- **ocean_id (String)**: ID of the Ocean Cluster
- **eks_cluster_name (String)**: Cluster name of the EKS cluster.
- **eks_node_group_name (String)**: Node group name to import.
- **region (String)**: Node group name to import.
- **import_eks_node_group_to_ocean_launch_spec (ImportEKSNodeGroupToOceanVNG)**: ImportEKSNodeGroupToOceanVNG object

**Returns**

`(Object)`: Ocean Import EKS Cluster Node Group to Launch Spec Response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.create_migration">create_migration</h2>

```python
OceanAwsClient.create_migration(ocean_id: str, migration: Migration)
```

Create a migration for a given existing instances.

**Arguments**

- **migration (Migration)**: Migration Object

**Returns**

`(Object)`: Migration create response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.get_migration_discovery">get_migration_discovery</h2>

```python
OceanAwsClient.get_migration_discovery(ocean_id: str,
                                       should_fetch_pods: bool)
```

Get information about nodes which can be migrated into Ocean.

**Arguments**

- **ocean_id (String)**: ID of the Ocean Cluster
- **should_fetch_pods (bool)**: Should fetch data about running pods for each node.

**Returns**

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.stop_migration">stop_migration</h2>

```python
OceanAwsClient.stop_migration(ocean_id: str, migration_id: str,
                              migration: Migration)
```

Stop an ongoing Workload Migration.

**Arguments**

- **ocean_id (String)**: ID of the Ocean Cluster
- **migration_id (bool)**: The migration identifier of a specific migration
- **migration (Migration)**: Migration Update Configuration

**Returns**

`(Object)`: Ocean Migration response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.get_migration_status">get_migration_status</h2>

```python
OceanAwsClient.get_migration_status(ocean_id: str, migration_id: str)
```

Get Migration full info and status for an Ocean cluster.

**Arguments**

- **ocean_id (String)**: ID of the Ocean Cluster
- **migration_id (String)**: The migration identifier of a specific migration.

**Returns**

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.get_all_migrations_summary">get_all_migrations_summary</h2>

```python
OceanAwsClient.get_all_migrations_summary(ocean_id: str = None)
```

Get summary of migrations history for an Ocean cluster.

**Returns**

`(Object)`: Ocean Migrations response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.create_extended_resource_definition">create_extended_resource_definition</h2>

```python
OceanAwsClient.create_extended_resource_definition(
  extended_resource_definition: ExtendedResourceDefinition)
```

Creates an Ocean extended resource definition entity

**Arguments**

- **extended_resource_definition (ExtendedResourceDefinition)**: The Ocean extended resource definition

**Returns**

`(Object)`: Ocean Create Extended Resource Definition response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.get_extended_resource_definition">get_extended_resource_definition</h2>

```python
OceanAwsClient.get_extended_resource_definition(
  ocean_extended_resource_definition_id: str)
```

Get Migration full info and status for an Ocean cluster.

**Arguments**

- **ocean_extended_resource_definition_id (String)**: Identifier of the Ocean extended resource definition.

**Returns**

`(Object)`: Ocean Extended Resource Definition response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.get_all_extended_resource_definitions">get_all_extended_resource_definitions</h2>

```python
OceanAwsClient.get_all_extended_resource_definitions()
```

extended_resource_definition

**Returns**

`(Object)`: Ocean Extended Resource Defintion response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.update_extended_resource_definition">update_extended_resource_definition</h2>

```python
OceanAwsClient.update_extended_resource_definition(
  ocean_extended_resource_definition_id: str,
  extended_resource_definition: ExtendedResourceDefinition)
```

Only the mapping parameter is updatable for extended resource definition

**Arguments**

- **ocean_extended_resource_definition_id (String)**: Identifier of the Ocean extended resource definition.
- **extended_resource_definition (ExtendedResourceDefinition)**: The Ocean extended resource definition

**Returns**

`(Object)`: Ocean Extended Resource Definition response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.delete_extended_resource_definition">delete_extended_resource_definition</h2>

```python
OceanAwsClient.delete_extended_resource_definition(
  ocean_extended_resource_definition_id: str)
```

Delete a specified Ocean extended resource definition.

**Arguments**

- **ocean_extended_resource_definition_id (String)**: Identifier of the Ocean extended resource definition.

**Returns**

`(Object)`: Ocean Delete Extended Resource Definition response
