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

Get an existing Ocean Cluster json

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
- __amount (int)__: The number of nodes to launch.

__Returns__

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

__Arguments__

- __to_date (String)__: to date
- __from_date (String)__: to date
- __severity(String) (Optional)__: Log level severity
- __resource_id(String) (Optional)__: Filter log extracted entires related to a
  specific resource id
- __limit(String) (Optional)__: Maximum number of lines to extract in a response

__Returns__

`(Object)`: Ocean Get Log API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.import_asg_to_ocean_cluster">import_asg_to_ocean_cluster</h2>

```python
OceanAwsClient.import_asg_to_ocean_cluster(
  auto_scaling_group_name, region,
  import_asg_to_ocean_cluster: ImportASGToOceanCluster)
```

Create an Ocean configuration according to an AWS autoscaling group (ASG) configuration.

__Arguments__

- __auto_scaling_group_name (String)__: The ASG name
- __region (String)__: region
- __import_asg_to_ocean_cluster (ImportASGToOceanCluster)__: ImportASGToOceanCluster Object

__Returns__

`(Object)`: Ocean Import ASG to Ocean Response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.create_virtual_node_group">create_virtual_node_group</h2>

```python
OceanAwsClient.create_virtual_node_group(vng: VirtualNodeGroup,
                                         initial_nodes: int = None)
```

Create a VNG inside ocean cluster

__Arguments__

- __vng (VirtualNodeGroup)__: VirtualNodeGroup Object
- __initial_nodes__: When set to an integer greater than 0, a corresponding number of nodes will be launched from the virtual node group created.

__Returns__

`(Object)`: Ocean Launch Spec response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.update_virtual_node_group">update_virtual_node_group</h2>

```python
OceanAwsClient.update_virtual_node_group(vng_id: str,
                                         vng: VirtualNodeGroup,
                                         auto_apply_tags: bool = None)
```

Update an existing VNG inside an Ocean Cluster

__Arguments__

- __vng_id (String)__: ID of the Ocean Virtual Node Group
- __ocean (Ocean)__: Ocean object

__Returns__

`(Object)`: Ocean Launch Spec response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.get_all_virtual_node_groups">get_all_virtual_node_groups</h2>

```python
OceanAwsClient.get_all_virtual_node_groups(ocean_id: str = None)
```

List the configurations for all virtual node groups in the account
or in a specified cluster.

__Returns__

`(Object)`: Ocean Launch Spec response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.delete_virtual_node_group">delete_virtual_node_group</h2>

```python
OceanAwsClient.delete_virtual_node_group(vng_id: str,
                                         delete_nodes: bool = None,
                                         force_delete: bool = None)
```

Delete an Ocean Cluster

__Arguments__

- __vng_id (String)__: ID of the Ocean VNG
- __delete_nodes (Bool)__: When set to "true", all instances belonging to the deleted launch specification will be drained, detached, and terminated.
- __force_delete (Bool)__: When set to "true", delete even if it is the only custom launch spec remaining, and default launch spec has useAsTemplateOnly = true.

__Returns__

`(Object)`: Ocean Launch Specification Delete response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.attach_load_balancers">attach_load_balancers</h2>

```python
OceanAwsClient.attach_load_balancers(ocean_id: str, load_balancers)
```

Add new load balancers to the existing load balancers on the Ocean Cluster.

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __load_balancers (List[LoadBalancer])__: Load balancers to add to the Ocean cluster.

__Returns__

`(Object)`: Ocean Attach Load Balancers API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.detach_load_balancers">detach_load_balancers</h2>

```python
OceanAwsClient.detach_load_balancers(ocean_id, load_balancers)
```

Delete an Ocean Cluster

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __load_balancers (List[LoadBalancer])__: Load balancers to remove from the Ocean cluster.

__Returns__

`(Object)`: Ocean Detach Load Balancers API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.update_elastigroup_to_ocean">update_elastigroup_to_ocean</h2>

```python
OceanAwsClient.update_elastigroup_to_ocean(group_id: str)
```

Upgrade an Elastigroup with Kubernetes integration to Ocean for Kubernetes cluster.

__Arguments__

- __group_id (str)__: Elastigroup identifier

__Returns__

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.detach_instances">detach_instances</h2>

```python
OceanAwsClient.detach_instances(ocean_id: str,
                                detach_instances: DetachInstances)
```

Detach instances from your Ocean cluster.

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __detach_instances (DetachInstances)__: Detach Instances Request

__Returns__

`(Object)`: Detach Instances API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.instance_types_filter_simulation_for_vng">instance_types_filter_simulation_for_vng</h2>

```python
OceanAwsClient.instance_types_filter_simulation_for_vng(
  launch_spec_id: str, instance_types_filters: InstanceTypesFilters)
```

Returns all instance types that match the given filters. These instance types will be used if the Virtual Node Group is configured with these filters.

__Arguments__

- __launch_spec_id (String)__: Ocean cluster launch specification identifier.
- __instance_type_filters (InstanceTypesFilters)__: List of instance types filters. The instance types that match with all filters compose the Virtual Node Group's instanceTypes parameter.
The architectures that come from the Virtual Node Group's images will be taken into account when using this parameter.
Cannot be configured together with Virtual Node Group's instanceTypes and with the Cluster's whitelist/blacklist/filters.

__Returns__

`(Object)`: Ocean Instance Types Filter Simulation response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.import_asg_to_ocean_vng">import_asg_to_ocean_vng</h2>

```python
OceanAwsClient.import_asg_to_ocean_vng(
  auto_scaling_group_name, ocean_id: str,
  import_asg_to_ocean_launch_spec: ImportASGToOceanVNG)
```

Returns an Ocean Virtual Node Group (VNG) configuration in a given AWS autoscaling group (ASG). The returned value ("Imported VNG") can then be used as input to the Create Virtual Node Group API in order to create an actual VNG in your Ocean cluster.

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __auto_scaling_group_name (String)__: The ASG name.
- __import_asg_to_ocean_launch_spec (ImportASGToOceanVNG)__: ImportASGToOceanVNG object

__Returns__

`(Object)`: Ocean Import ASG to Launch Spec Response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.allowed_instance_types_by_filters_for_vng">allowed_instance_types_by_filters_for_vng</h2>

```python
OceanAwsClient.allowed_instance_types_by_filters_for_vng(
  launch_spec_id: str)
```

Returns the Virtual Node Group's instance types when instance types filters is set.

__Arguments__

- __launch_spec_id (String)__: Ocean Cluster Launch Specification Identifier

__Returns__

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

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __eks_cluster_name (String)__: Cluster name of the EKS cluster.
- __eks_node_group_name (String)__: Node group name to import.
- __region (String)__: Node group name to import.
- __import_eks_node_group_to_ocean_launch_spec (ImportEKSNodeGroupToOceanVNG)__: ImportEKSNodeGroupToOceanVNG object

__Returns__

`(Object)`: Ocean Import EKS Cluster Node Group to Launch Spec Response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.create_migration">create_migration</h2>

```python
OceanAwsClient.create_migration(ocean_id: str, migration: Migration)
```

Create a migration for a given existing instances.

__Arguments__

- __migration (Migration)__: Migration Object

__Returns__

`(Object)`: Migration create response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.get_migration_discovery">get_migration_discovery</h2>

```python
OceanAwsClient.get_migration_discovery(ocean_id: str,
                                       should_fetch_pods: bool)
```

Get information about nodes which can be migrated into Ocean.

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __should_fetch_pods (bool)__: Should fetch data about running pods for each node.

__Returns__

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.stop_migration">stop_migration</h2>

```python
OceanAwsClient.stop_migration(ocean_id: str, migration_id: str,
                              migration: Migration)
```

Stop an ongoing Workload Migration.

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __migration_id (String)__: The migration identifier of a specific migration
- __migration (Migration)__: Migration Update Configuration

__Returns__

`(Object)`: Ocean Migration response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.get_migration_status">get_migration_status</h2>

```python
OceanAwsClient.get_migration_status(ocean_id: str, migration_id: str)
```

Get Migration full info and status for an Ocean cluster.

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __migration_id (String)__: The migration identifier of a specific migration.

__Returns__

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.get_all_migrations_summary">get_all_migrations_summary</h2>

```python
OceanAwsClient.get_all_migrations_summary(ocean_id: str = None)
```

Get summary of migrations history for an Ocean cluster.

__Returns__

`(Object)`: Ocean Migrations response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.create_extended_resource_definition">create_extended_resource_definition</h2>

```python
OceanAwsClient.create_extended_resource_definition(
  extended_resource_definition: ExtendedResourceDefinition)
```

Creates an Ocean extended resource definition entity

__Arguments__

- __extended_resource_definition (ExtendedResourceDefinition)__: The Ocean extended resource definition

__Returns__

`(Object)`: Ocean Create Extended Resource Definition response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.get_extended_resource_definition">get_extended_resource_definition</h2>

```python
OceanAwsClient.get_extended_resource_definition(
  ocean_extended_resource_definition_id: str)
```

Get Migration full info and status for an Ocean cluster.

__Arguments__

- __ocean_extended_resource_definition_id (String)__: Identifier of the Ocean extended resource definition.

__Returns__

`(Object)`: Ocean Extended Resource Definition response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.get_all_extended_resource_definitions">get_all_extended_resource_definitions</h2>

```python
OceanAwsClient.get_all_extended_resource_definitions()
```

extended_resource_definition

__Returns__

`(Object)`: Ocean Extended Resource Defintion response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.update_extended_resource_definition">update_extended_resource_definition</h2>

```python
OceanAwsClient.update_extended_resource_definition(
  ocean_extended_resource_definition_id: str,
  extended_resource_definition: ExtendedResourceDefinition)
```

Only the mapping parameter is updatable for extended resource definition

__Arguments__

- __ocean_extended_resource_definition_id (String)__: Identifier of the Ocean extended resource definition.
- __extended_resource_definition (ExtendedResourceDefinition)__: The Ocean extended resource definition

__Returns__

`(Object)`: Ocean Extended Resource Definition response

<h2 id="spotinst_sdk2.clients.ocean.OceanAwsClient.delete_extended_resource_definition">delete_extended_resource_definition</h2>

```python
OceanAwsClient.delete_extended_resource_definition(
  ocean_extended_resource_definition_id: str)
```

Delete a specified Ocean extended resource definition.

__Arguments__

- __ocean_extended_resource_definition_id (String)__: Identifier of the Ocean extended resource definition.

__Returns__

`(Object)`: Ocean Delete Extended Resource Definition response

