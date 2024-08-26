<h1 id="spotinst_sdk2.clients.ocean.OceanEcsClient">OceanEcsClient</h1>

```python
OceanEcsClient(self,
               session=None,
               print_output=True,
               log_level=None,
               user_agent=None,
               timeout=None)
```

<h2 id="spotinst_sdk2.clients.ocean.OceanEcsClient.get_all_ocean_clusters">get_all_ocean_clusters</h2>

```python
OceanEcsClient.get_all_ocean_clusters()
```

Get the configurations for all Ocean ECS clusters in the specified account.

__Returns__

`(Object)`: Ocean ECS API response

<h2 id="spotinst_sdk2.clients.ocean.OceanEcsClient.create_ocean_cluster">create_ocean_cluster</h2>

```python
OceanEcsClient.create_ocean_cluster(ocean: Ocean)
```

Create an Ocean ECS Cluster

__Arguments__

- __ocean (Ocean)__: Ocean ECS Object

__Returns__

`(Object)`: Ocean ECS API response

<h2 id="spotinst_sdk2.clients.ocean.OceanEcsClient.get_ocean_cluster">get_ocean_cluster</h2>

```python
OceanEcsClient.get_ocean_cluster(ocean_id: str)
```

Get the configuration for a specified Ocean cluster.

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster

__Returns__

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanEcsClient.update_ocean_cluster">update_ocean_cluster</h2>

```python
OceanEcsClient.update_ocean_cluster(ocean_id: str, ocean: Ocean)
```

Update an existing Ocean Cluster

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __ocean (Ocean)__: Ocean object

__Returns__

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanEcsClient.delete_ocean_cluster">delete_ocean_cluster</h2>

```python
OceanEcsClient.delete_ocean_cluster(ocean_id: str)
```

Delete a specified Ocean cluster.

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster

__Returns__

`(Object)`: Ocean API response

<h2 id="spotinst_sdk2.clients.ocean.OceanEcsClient.import_ocean_cluster">import_ocean_cluster</h2>

```python
OceanEcsClient.import_ocean_cluster(
  ecs_cluster_name: str, import_cluster_config: ImportClusterConfig)
```

Create an Ocean ECS Cluster

__Arguments__

- __ecs_cluster_name (String)__: Name of the existing ECS Cluster to import
- __import_cluster_config (ImportClusterConfig)__: Import Cluster Object

__Returns__

`(Object)`: Ocean ECS API response

<h2 id="spotinst_sdk2.clients.ocean.OceanEcsClient.get_elastilog">get_elastilog</h2>

```python
OceanEcsClient.get_elastilog(ocean_id: str,
                             from_date: str,
                             to_date: str,
                             severity: str = None,
                             resource_id: str = None,
                             limit: int = None)
```

Get the log of an Ocean Cluster.

__Arguments__

- __ocean_id (String)__: Ocean cluster identifier
- __to_date (String)__: end date value
- __from_date (String)__: beginning date value
- __severity (String) (Optional)__: Log level severity
- __resource_id (String) (Optional)__: specific resource identifier
- __limit(int) (Optional)__: Maximum number of lines to extract in a response

__Returns__

`(Object)`: Ocean Get Log API response

<h2 id="spotinst_sdk2.clients.ocean.OceanEcsClient.instance_types_filters_simulation">instance_types_filters_simulation</h2>

```python
OceanEcsClient.instance_types_filters_simulation(
  ocean_id: str, filters: InstanceTypesFilters)
```

Returns all instances types that match the given filters.
These instance types will be used if the cluster is configured with these filters.

__Arguments__

- __ocean_id (String)__: Id of the Ocean Cluster
- __filters (InstanceTypesFilters)__: List of filters

__Returns__

`(Object)`: Ocean Instance Type Simultion response

<h2 id="spotinst_sdk2.clients.ocean.OceanEcsClient.get_allowed_instance_types">get_allowed_instance_types</h2>

```python
OceanEcsClient.get_allowed_instance_types(ocean_id: str)
```

Return the list of the allowed Ocean cluster instance types.

__Arguments__

- __ocean_id (String)__: Ocean cluster identifier

__Returns__

`(Object)`: Ocean Allowed Instance Types response

<h2 id="spotinst_sdk2.clients.ocean.OceanEcsClient.upgrade_elastigroup_to_ocean">upgrade_elastigroup_to_ocean</h2>

```python
OceanEcsClient.upgrade_elastigroup_to_ocean(group_id: str)
```

Upgrade an Elastigroup with ECS integration into Ocean for ECS cluster.

__Arguments__

- __group_id (String)__: Elastigroup ID

__Returns__

`(Object)`: Ocean ECS API response

<h2 id="spotinst_sdk2.clients.ocean.OceanEcsClient.initiate_roll">initiate_roll</h2>

```python
OceanEcsClient.initiate_roll(ocean_id: str, roll_config: RollConfig)
```

Initiate Cluster Rolls

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __roll_config (RollConfig)__: Cluster Roll / Roll with Instance Ids/ Roll with VNG Ids

__Returns__

`(Object)`: Cluster Roll API response

<h2 id="spotinst_sdk2.clients.ocean.OceanEcsClient.list_rolls">list_rolls</h2>

```python
OceanEcsClient.list_rolls(ocean_id: str)
```

List rolls of an Ocean cluster.

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster

__Returns__

`(Object)`: List of Cluster Roll API response

<h2 id="spotinst_sdk2.clients.ocean.OceanEcsClient.update_roll">update_roll</h2>

```python
OceanEcsClient.update_roll(ocean_id: str, roll_id: str, status: str)
```

Update a roll of an Ocean cluster.
Performing the request will stop the next batch in a roll.

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __roll_id (String)__: Ocean cluster roll identifier
- __status (String)__: update roll status request

__Returns__

`(Object)`: Cluster Roll API response

<h2 id="spotinst_sdk2.clients.ocean.OceanEcsClient.get_roll">get_roll</h2>

```python
OceanEcsClient.get_roll(ocean_id: str, roll_id: str)
```

Get status for a roll of an Ocean cluster.

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __roll_id (String)__: Ocean cluster roll identifier

__Returns__

`(Object)`: Cluster Roll API response

<h2 id="spotinst_sdk2.clients.ocean.OceanEcsClient.get_cluster_container_instances">get_cluster_container_instances</h2>

```python
OceanEcsClient.get_cluster_container_instances(ocean_id: str,
                                               instance_id: str = None,
                                               launch_spec_id: str = None
                                               )
```

Get container instances data of an Ocean cluster.

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __instance_id (String)__: Instance identifier
- __launch_spec_id (String)__: Ocean cluster VNG identifier.

__Returns__

`(Object)`: Ocean Aws Container Instances Data Response

<h2 id="spotinst_sdk2.clients.ocean.OceanEcsClient.detach_instances">detach_instances</h2>

```python
OceanEcsClient.detach_instances(
  ocean_id: str, detach_configuration: DetachInstancesConfig)
```

Detach instances from your Ocean cluster.

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __detach_configuration (DetachInstancesConfig)__: Detach instances request

__Returns__

`(Object)`: Detach Instance response

<h2 id="spotinst_sdk2.clients.ocean.OceanEcsClient.create_virtual_node_group">create_virtual_node_group</h2>

```python
OceanEcsClient.create_virtual_node_group(vng: VirtualNodeGroup)
```

Create a new Ocean ECS virtual node group in the specified account.

__Arguments__

- __vng (VirtualNodeGroup)__: VirtualNodeGroup Object

__Returns__

`(Object)`: Ocean Virtual Node Group API response

<h2 id="spotinst_sdk2.clients.ocean.OceanEcsClient.get_all_virtual_node_groups">get_all_virtual_node_groups</h2>

```python
OceanEcsClient.get_all_virtual_node_groups(ocean_id: str)
```

Get all VNGs for the specified Ocean cluster.

__Returns__

`(Object)`: Ocean Virtual Node Group API response

<h2 id="spotinst_sdk2.clients.ocean.OceanEcsClient.delete_virtual_node_group">delete_virtual_node_group</h2>

```python
OceanEcsClient.delete_virtual_node_group(
  vng_id: str, delete_container_instances: bool = None)
```

Delete a specified virtual node group in an Ocean cluster.

__Arguments__

- __vng_id (String)__: Ocean cluster Virtual Node Group identifier.
- __delete_container_instances (Bool)__: When set to "true", all instances belonging to the deleted VNG will be drained, detached, and terminated.

__Returns__

`(Object)`: Ocean Virtual Node Group Delete response

<h2 id="spotinst_sdk2.clients.ocean.OceanEcsClient.update_virtual_node_group">update_virtual_node_group</h2>

```python
OceanEcsClient.update_virtual_node_group(vng_id: str,
                                         vng: VirtualNodeGroup)
```

Update specified VNG for an Ocean cluster.

__Arguments__

- __vng_id (String)__: ID of the Ocean Virtual Node Group
- __vng (VirtualNodeGroup)__: VirtualNodeGroup Object

__Returns__

`(Object)`: Ocean Virtual Node Group API response

<h2 id="spotinst_sdk2.clients.ocean.OceanEcsClient.get_virtual_node_group">get_virtual_node_group</h2>

```python
OceanEcsClient.get_virtual_node_group(vng_id: str)
```

Get a specified VNG for an Ocean cluster.

__Arguments__

- __vng_id (String)__: Ocean cluster Virtual Node Group identifier.

__Returns__

`(Object)`: Ocean Virtual Node Group API response

<h2 id="spotinst_sdk2.clients.ocean.OceanEcsClient.import_fargate_to_existing_ocean_cluster">import_fargate_to_existing_ocean_cluster</h2>

```python
OceanEcsClient.import_fargate_to_existing_ocean_cluster(
  ocean_id: str,
  import_fargate_existing: ImportFargateToExistingOceanCluster)
```

Import a Fargate service into an existing Ocean ECS cluster.

__Arguments__

- __ocean_id (String)__: Ocean cluster Identifier
- __import_fargate_existing (Object)__: ImportFargateToExistingOceanCluster Object

__Returns__

`(Object)`: Ocean ECS Fargate Response

<h2 id="spotinst_sdk2.clients.ocean.OceanEcsClient.get_fargate_services_discovery">get_fargate_services_discovery</h2>

```python
OceanEcsClient.get_fargate_services_discovery(ocean_id: str)
```

Get existing Fargate services in the ECS cluster.

__Arguments__

- __ocean_id (String)__: Ocean cluster identifier

__Returns__

`(Object)`: Ocean ECS Fargate Response

<h2 id="spotinst_sdk2.clients.ocean.OceanEcsClient.get_fargate_migration_status">get_fargate_migration_status</h2>

```python
OceanEcsClient.get_fargate_migration_status(ocean_id: str)
```

Get the status of a Fargate service import.

__Arguments__

- __ocean_id (String)__: Ocean cluster identifier

__Returns__

`(Object)`: Ocean ECS Fargate Response

<h2 id="spotinst_sdk2.clients.ocean.OceanEcsClient.import_fargate_to_new_ocean_cluster">import_fargate_to_new_ocean_cluster</h2>

```python
OceanEcsClient.import_fargate_to_new_ocean_cluster(
  import_fargate_new: ImportFargateToNewOceanCluster)
```

Import a Fargate service into a new Ocean ECS cluster.

__Arguments__

- __ocean_id (String)__: Ocean cluster Identifier
- __import_fargate_new (Object)__: ImportFargateToNewOceanCluster Object

__Returns__

`(Object)`: Ocean ECS Fargate Response

<h2 id="spotinst_sdk2.clients.ocean.OceanEcsClient.launch_instances_in_vng">launch_instances_in_vng</h2>

```python
OceanEcsClient.launch_instances_in_vng(vng_id: str, amount: int)
```

Launch container instances in virtual node group.

__Arguments__

- __vng_id (String)__: Ocean cluster Virtual Node Group identifier.
- __amount (int)__: The number of nodes to launch.

__Returns__

`(Object)`: Ocean Virtual Node Group Launch API response

