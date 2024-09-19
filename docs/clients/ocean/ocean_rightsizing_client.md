<h1 id="spotinst_sdk2.clients.ocean.OceanRightSizingClient">OceanRightSizingClient</h1>

```python
OceanRightSizingClient(self,
                       session=None,
                       print_output=True,
                       log_level=None,
                       user_agent=None,
                       timeout=None)
```

<h2 id="spotinst_sdk2.clients.ocean.OceanRightSizingClient.create_right_sizing_rule">create_right_sizing_rule</h2>

```python
OceanRightSizingClient.create_right_sizing_rule(
  ocean_id: str,
  rule_name: str,
  application_intervals:
    typing.List[spotinst_sdk2.models.ocean.rightsizing.RecommendationApplicationInterval],
  restart_replicas: RestartReplicas = None,
  exclude_preliminary_recommendations: bool = None,
  application_min_threshold: RecommendationApplicationMinThreshold = None,
  application_boundaries: RecommendationApplicationBoundaries = None,
  application_overhead_values:
    RecommendationApplicationOverheadValues = None,
  application_hpa: RecommendationApplicationHPA = None)
```

Create a right sizing rule for an Ocean cluster.

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __rule_name (String)__: Name of the Right Sizing Rule
- __restart_replicas (RestartReplicas)__: Restart Replicas
- __exclude_preliminary_recommendations (boolean)__: Exclude preliminary recommendations
- __application_intervals (List[RecommendationApplicationIntervals])__: Recommendation Application Intervals
- __application_min_threshold (RecommendationApplicationMinThreshold)__: Recommendation Application Min Threshold
- __application_boundaries (RecommendationApplicationBoundaries)__: Recommendation Application Boundaries
- __application_overhead_values (RecommendationApplicationOverheadValues)__: Recommendation Application Overhead Values
- __application_hpa (RecommendationApplicationHPA)__: Recommendation Application HPA

__Returns__

`(Object)`: Ocean Right Sizing Rule API response


<h2 id="spotinst_sdk2.clients.ocean.OceanRightSizingClient.delete_right_sizing_rule">delete_right_sizing_rule</h2>

```python
OceanRightSizingClient.delete_right_sizing_rule(
  ocean_id: str, rule_names: typing.List[str])
```

Delete a right sizing rule for an Ocean cluster.

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __rule_names (List[String])__: List of Right Sizing Rule Names

__Returns__

`(Object)`: Ocean Right Sizing Rule API response

<h2 id="spotinst_sdk2.clients.ocean.OceanRightSizingClient.update_right_sizing_rule">update_right_sizing_rule</h2>

```python
OceanRightSizingClient.update_right_sizing_rule(
  ocean_id: str,
  rule_name: str,
  application_intervals:
    typing.List[spotinst_sdk2.models.ocean.rightsizing.RecommendationApplicationInterval],
  restart_replicas: RestartReplicas = None,
  exclude_preliminary_recommendations: bool = None,
  application_min_threshold: RecommendationApplicationMinThreshold = None,
  application_boundaries: RecommendationApplicationBoundaries = None,
  application_overhead_values:
    RecommendationApplicationOverheadValues = None,
  application_hpa: RecommendationApplicationHPA = None)
```

Update a right sizing rule for an Ocean cluster.

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __rule_name (String)__: Rightsizing Rule name
- __restart_replicas (RestartReplicas)__: Restart Replicas
- __exclude_preliminary_recommendations (boolean)__: Exclude preliminary recommendations
- __application_intervals (RecommendationApplicationIntervals)__: Recommendation Application Intervals
- __application_min_threshold (RecommendationApplicationMinThreshold)__: Recommendation Application Min Threshold
- __application_boundaries (RecommendationApplicationBoundaries)__: Recommendation Application Boundaries
- __application_overhead_values (RecommendationApplicationOverheadValues)__: Recommendation Application Overhead Values
- __application_hpa (RecommendationApplicationHPA)__: Recommendation Application HPA

__Returns__

`(Object)`: Ocean Right Sizing Rule API response

<h2 id="spotinst_sdk2.clients.ocean.OceanRightSizingClient.attach_right_sizing_rule">attach_right_sizing_rule</h2>

```python
OceanRightSizingClient.attach_right_sizing_rule(
  ocean_id: str, rule_name: str, namespaces:
    typing.List[spotinst_sdk2.models.ocean.rightsizing.Namespace])
```

Attach right sizing rule to an Ocean cluster.

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __rule_name (String)__: Ocean right sizing rule
- __namespaces (List[Namespace])__: List of namespaces to attach the right sizing rule to

__Returns__

`(Object)`: Ocean Right Sizing Rule API response

<h2 id="spotinst_sdk2.clients.ocean.OceanRightSizingClient.detach_right_sizing_rule">detach_right_sizing_rule</h2>

```python
OceanRightSizingClient.detach_right_sizing_rule(
  ocean_id: str, rule_name: str, namespaces:
    typing.List[spotinst_sdk2.models.ocean.rightsizing.Namespace])
```

Detach right sizing rule from an Ocean cluster.

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __rule_name (String)__: Ocean right sizing rule
- __namespaces (List[Namespace])__: List of namespaces to detach the right sizing rule from

__Returns__

`(Object)`: Ocean Right Sizing Rule API response

<h2 id="spotinst_sdk2.clients.ocean.OceanRightSizingClient.get_right_sizing_rule">get_right_sizing_rule</h2>

```python
OceanRightSizingClient.get_right_sizing_rule(ocean_id: str,
                                             rule_name: str)
```

Get right sizing rule for an Ocean cluster.

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __rule_name (String)__: Name of the Right Sizing Rule

__Returns__

`(Object)`: Ocean Right Sizing Rule API response

<h2 id="spotinst_sdk2.clients.ocean.OceanRightSizingClient.list_right_sizing_rules">list_right_sizing_rules</h2>

```python
OceanRightSizingClient.list_right_sizing_rules(ocean_id: str)
```

Get right sizing rule for an Ocean cluster.

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster


__Returns__

`(Object)`: Ocean Right Sizing Rules API response

<h2 id="spotinst_sdk2.clients.ocean.OceanRightSizingClient.get_ocean_right_sizing_recommendations">get_ocean_right_sizing_recommendations</h2>

```python
OceanRightSizingClient.get_ocean_right_sizing_recommendations(
  ocean_id: str,
  cluster_resources: ClusterResources = None,
  cluster_labels: ClusterLabels = None)
```

Attach right sizing rule to an Ocean cluster.

__Arguments__

- __ocean_id (String)__: ID of the Ocean Cluster
- __cluster_resources (ClusterResources)__: Cluster Resources
- __cluster_labels (ClusterLabels)__: Cluster Labels

__Returns__

`(Object)`: Ocean Right Sizing Rule API response

