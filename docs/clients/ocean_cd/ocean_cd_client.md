<h1 id="spotinst_sdk2.clients.ocean_cd.OceanCDClient">OceanCDClient</h1>

```python
OceanCDClient(self,
              session=None,
              print_output=True,
              log_level=None,
              user_agent=None,
              timeout=None)
```

<h2 id="spotinst_sdk2.clients.ocean_cd.OceanCDClient.get_oceancd_cluster">get_oceancd_cluster</h2>

```python
OceanCDClient.get_oceancd_cluster(cluster_id: str)
```

Get an existing Ocean CD cluster.

__Arguments__

- __cluster_id (String)__: OceanCD Cluster ID

__Returns__

`(Object)`: OceanCD Cluster API response

<h2 id="spotinst_sdk2.clients.ocean_cd.OceanCDClient.get_all_oceancd_clusters">get_all_oceancd_clusters</h2>

```python
OceanCDClient.get_all_oceancd_clusters()
```

List all Ocean CD clusters.

__Returns__

`(List)`: List of Ocean CD CLuster API response

<h2 id="spotinst_sdk2.clients.ocean_cd.OceanCDClient.update_oceancd_cluster">update_oceancd_cluster</h2>

```python
OceanCDClient.update_oceancd_cluster(
  cluster_notification: ClusterNotification, cluster_id: str)
```

Update Ocean CD cluster notification settings.

__Arguments__

- __cluster_id (String)__: OceanCD Cluster ID
- __cluster_notification (ClusterNotification)__: Cluster Notification

__Returns__

`(Boolean)`: Response Status

<h2 id="spotinst_sdk2.clients.ocean_cd.OceanCDClient.delete_oceancd_cluster">delete_oceancd_cluster</h2>

```python
OceanCDClient.delete_oceancd_cluster(cluster_id: str)
```

Delete an existing Ocean CD cluster.

__Arguments__

- __cluster_id (String)__: OceanCD Cluster ID

__Returns__

`(Boolean)`: Response Status

<h2 id="spotinst_sdk2.clients.ocean_cd.OceanCDClient.create_oceancd_verification_provider">create_oceancd_verification_provider</h2>

```python
OceanCDClient.create_oceancd_verification_provider(
  verification_provider: VerificationProvider)
```

Create Ocean CD Verification Provider. only one provider type can be defined

__Arguments__

- __verification_provider (VerificationProvider) __: OceanCD Verification Provider

__Returns__

`(Object) `: OceanCD Verification Provider

<h2 id="spotinst_sdk2.clients.ocean_cd.OceanCDClient.get_all_oceancd_verification_providers">get_all_oceancd_verification_providers</h2>

```python
OceanCDClient.get_all_oceancd_verification_providers()
```

List all Ocean CD verification providers.

__Returns__

`(List)`: List of Ocean CD Verification Provider API response

<h2 id="spotinst_sdk2.clients.ocean_cd.OceanCDClient.get_oceancd_verification_provider">get_oceancd_verification_provider</h2>

```python
OceanCDClient.get_oceancd_verification_provider(name: str)
```

Get an existing  Ocean CD Verification Provider.

__Arguments__

- __name (String)__: The identifier of the Ocean CD Verification Provider

__Returns__

`(Object)`: OceanCD Verification Provider API response

<h2 id="spotinst_sdk2.clients.ocean_cd.OceanCDClient.update_oceancd_verifcation_provider">update_oceancd_verifcation_provider</h2>

```python
OceanCDClient.update_oceancd_verifcation_provider(
  provider_update: VerificationProvider, name: str)
```

Full Update of Ocean CD Verification Provider configuration. All non included fields will be nullified

__Arguments__

- __name (String)__: The identifier name of the Ocean CD Verification Provider
- __provider_update (VerificationProvider)__: VerificationProvider Object

__Returns__

`(Boolean)`: Response Status

<h2 id="spotinst_sdk2.clients.ocean_cd.OceanCDClient.delete_oceancd_verification_provider">delete_oceancd_verification_provider</h2>

```python
OceanCDClient.delete_oceancd_verification_provider(name: str)
```

Delete an existing Ocean CD Verification Provider.

__Arguments__

- __name (String)__: OceanCD Cluster ID

__Returns__

`(Boolean)`: Response Status

<h2 id="spotinst_sdk2.clients.ocean_cd.OceanCDClient.create_oceancd_verification_template">create_oceancd_verification_template</h2>

```python
OceanCDClient.create_oceancd_verification_template(
  verification_template: VerificationTemplate)
```

Create Ocean CD Verification Template.

__Arguments__

- __verification_template (VerificationTemplate) __: OceanCD Verification Template

__Returns__

`(Object) `: OceanCD Verification Template

<h2 id="spotinst_sdk2.clients.ocean_cd.OceanCDClient.get_all_oceancd_verification_templates">get_all_oceancd_verification_templates</h2>

```python
OceanCDClient.get_all_oceancd_verification_templates()
```

List all Ocean CD verification templates.

__Returns__

`(List)`: List of Ocean CD Verification Template API response

<h2 id="spotinst_sdk2.clients.ocean_cd.OceanCDClient.get_oceancd_verification_template">get_oceancd_verification_template</h2>

```python
OceanCDClient.get_oceancd_verification_template(name: str)
```

Get an existing Ocean CD Verification Template.

__Arguments__

- __name (String)__: The identifier of the Ocean CD Verification Template

__Returns__

`(Object)`: OceanCD Verification Template API response

<h2 id="spotinst_sdk2.clients.ocean_cd.OceanCDClient.update_oceancd_verifcation_template">update_oceancd_verifcation_template</h2>

```python
OceanCDClient.update_oceancd_verifcation_template(
  template_update: VerificationTemplate, name: str)
```

Full Update of Ocean CD Verification Template configuration. All non included fields will be nullified

__Arguments__

- __name (String)__: The identifier name of the Ocean CD Verification Template
- __template_update (VerificationTemplate)__: VerificationTemplate Object

__Returns__

`(Boolean)`: Response Status

<h2 id="spotinst_sdk2.clients.ocean_cd.OceanCDClient.delete_oceancd_verification_template">delete_oceancd_verification_template</h2>

```python
OceanCDClient.delete_oceancd_verification_template(name: str)
```

Delete an existing Ocean CD Verification Template.

__Arguments__

- __name (String)__: The identifier name of the Ocean CD Verification Template

__Returns__

`(Boolean)`: Response Status

<h2 id="spotinst_sdk2.clients.ocean_cd.OceanCDClient.create_oceancd_strategy">create_oceancd_strategy</h2>

```python
OceanCDClient.create_oceancd_strategy(strat: Strategy)
```

Create Ocean CD Strategy.

__Arguments__

- __strat (Strategy) __: OceanCD Strategy

__Returns__

`(Object) `: OceanCD Strategy

<h2 id="spotinst_sdk2.clients.ocean_cd.OceanCDClient.get_all_oceancd_strategy">get_all_oceancd_strategy</h2>

```python
OceanCDClient.get_all_oceancd_strategy()
```

List all Ocean CD strategy.

__Returns__

`(List)`: List of Ocean CD Strategy API response

<h2 id="spotinst_sdk2.clients.ocean_cd.OceanCDClient.get_oceancd_strategy">get_oceancd_strategy</h2>

```python
OceanCDClient.get_oceancd_strategy(name: str)
```

Get an existing Ocean CD Strategy.

__Arguments__

- __name (String)__: The identifier of the Ocean CD Strategy

__Returns__

`(Object)`: OceanCD Strategy API response

<h2 id="spotinst_sdk2.clients.ocean_cd.OceanCDClient.update_oceancd_strategy">update_oceancd_strategy</h2>

```python
OceanCDClient.update_oceancd_strategy(strategy_update: Strategy,
                                      name: str)
```

Full Update of Ocean CD strategy configuration. All non included fields will be nullified

__Arguments__

- __name (String)__: The identifier name of the Ocean CD Strategy
- __strategy_update (Strategy)__: Strategy Object

__Returns__

`(Boolean)`: Response Status

<h2 id="spotinst_sdk2.clients.ocean_cd.OceanCDClient.delete_oceancd_strategy">delete_oceancd_strategy</h2>

```python
OceanCDClient.delete_oceancd_strategy(name: str)
```

Delete an existing Ocean CD Strategy.

__Arguments__

- __name (String)__: OceanCD Strategy

__Returns__

`(Boolean)`: Response Status

<h2 id="spotinst_sdk2.clients.ocean_cd.OceanCDClient.create_oceancd_rollout_spec">create_oceancd_rollout_spec</h2>

```python
OceanCDClient.create_oceancd_rollout_spec(rollouts: RolloutSpec)
```

Create Ocean CD rollout spec.

__Arguments__

- __rollouts (RolloutSpec) __: OceanCD Rollout Spec

__Returns__

`(Object) `: OceanCD Rollout Spec

<h2 id="spotinst_sdk2.clients.ocean_cd.OceanCDClient.get_all_oceancd_rollout_specs">get_all_oceancd_rollout_specs</h2>

```python
OceanCDClient.get_all_oceancd_rollout_specs()
```

List all Ocean CD rollout specs.

__Returns__

`(List)`: List of Ocean CD Rollout Spec API response

<h2 id="spotinst_sdk2.clients.ocean_cd.OceanCDClient.get_oceancd_rollout_spec">get_oceancd_rollout_spec</h2>

```python
OceanCDClient.get_oceancd_rollout_spec(name: str)
```

Get the configuration of an existing Ocean CD rollout spec.

__Arguments__

- __name (String)__: The identifier of the Ocean CD Rollout Spec

__Returns__

`(Object)`: OceanCD Rollout Spec API response

<h2 id="spotinst_sdk2.clients.ocean_cd.OceanCDClient.update_oceancd_rollout_spec">update_oceancd_rollout_spec</h2>

```python
OceanCDClient.update_oceancd_rollout_spec(
  rollout_spec_update: RolloutSpec, name: str)
```

Full Update Ocean CD rollout spec configuration. All non included fields will be nullified

__Arguments__

- __name (String)__: The identifier name of the Ocean CD Rollout Spec
- __rollout_spec_update (RolloutSpec)__: Rollout Spec Object

__Returns__

`(Boolean)`: Response Status

<h2 id="spotinst_sdk2.clients.ocean_cd.OceanCDClient.delete_oceancd_rollout">delete_oceancd_rollout</h2>

```python
OceanCDClient.delete_oceancd_rollout(name: str)
```

Delete an existing Ocean CD Rollout Spec.

__Arguments__

- __name (String)__: OceanCD Rollout Spec

__Returns__

`(Boolean)`: Response Status

<h2 id="spotinst_sdk2.clients.ocean_cd.OceanCDClient.describe_rollout_by_id">describe_rollout_by_id</h2>

```python
OceanCDClient.describe_rollout_by_id(rollout_id: str)
```

Get Ocean CD single rollout

__Arguments__

- __rollout_id (String)__: The identifier of the Ocean CD rollout

__Returns__

`(Object)`: OceanCD Rollout API response

<h2 id="spotinst_sdk2.clients.ocean_cd.OceanCDClient.ocean_cd_rollout_actions">ocean_cd_rollout_actions</h2>

```python
OceanCDClient.ocean_cd_rollout_actions(rollout_id: str,
                                       action_update: Action)
```

Execute action on an existing Ocean CD rollout.

__Arguments__

- __rollout_id (String)__: The identifier of the Ocean CD rollout

__Returns__

`(Boolean)`: Response Status

<h2 id="spotinst_sdk2.clients.ocean_cd.OceanCDClient.list_ocean_cd_rollouts">list_ocean_cd_rollouts</h2>

```python
OceanCDClient.list_ocean_cd_rollouts(from_date: str)
```

List Ocean CD rollouts.

__Arguments__

- __from_date (String)__: From Date

__Returns__

`(Object)`: OceanCD Rollout List API response

<h2 id="spotinst_sdk2.clients.ocean_cd.OceanCDClient.ocean_cd_describe_rollout_status">ocean_cd_describe_rollout_status</h2>

```python
OceanCDClient.ocean_cd_describe_rollout_status(rollout_id: str)
```

Ocean CD rollout status.

__Arguments__

- __rollout_id (String)__: The identifier of the Ocean CD rollout

__Returns__

`(Object)`: OceanCD Rollout List API response

<h2 id="spotinst_sdk2.clients.ocean_cd.OceanCDClient.ocean_cd_describe_latest_rollouts">ocean_cd_describe_latest_rollouts</h2>

```python
OceanCDClient.ocean_cd_describe_latest_rollouts(cluster_id: str,
                                                count: str,
                                                namespace: str,
                                                spot_deployment: str)
```

Ocean CD Latest rollout/s.

__Arguments__

- __clusterId (String)__: clusterId configured.
- __count (String)__: How many responses intended, sorted from the last one down.
- __namespace (String)__: namespace name configured
- __spot_deployment (String)__: SpotDeployment name configured

__Returns__

`(Object)`: OceanCD Rollout List API response

<h2 id="spotinst_sdk2.clients.ocean_cd.OceanCDClient.ocean_cd_describe_ongoing_rollouts">ocean_cd_describe_ongoing_rollouts</h2>

```python
OceanCDClient.ocean_cd_describe_ongoing_rollouts()
```

Ocean CD Ongoing rollouts.

__Returns__

`(Object)`: OceanCD Rollout List API response

<h2 id="spotinst_sdk2.clients.ocean_cd.OceanCDClient.ocean_cd_describe_rollout_verification">ocean_cd_describe_rollout_verification</h2>

```python
OceanCDClient.ocean_cd_describe_rollout_verification(rollout_id: str)
```

Ocean CD rollout verification.

__Arguments__

- __rolloutId (String)__: The identifier of the Ocean CD Verification Response

__Returns__

`(Object)`: OceanCD Rollout List API response

<h2 id="spotinst_sdk2.clients.ocean_cd.OceanCDClient.ocean_cd_describe_rollout_definition">ocean_cd_describe_rollout_definition</h2>

```python
OceanCDClient.ocean_cd_describe_rollout_definition(rollout_id: str)
```

Ocean CD rollout definition.

__Arguments__

- __rolloutId (String)__: The identifier of the Ocean CD Definition Response

__Returns__

`(Object)`: OceanCD Rollout List API response

<h2 id="spotinst_sdk2.clients.ocean_cd.OceanCDClient.ocean_cd_describe_rollout_resource">ocean_cd_describe_rollout_resource</h2>

```python
OceanCDClient.ocean_cd_describe_rollout_resource(rollout_id: str)
```

Ocean CD Resource

__Arguments__

- __rolloutId (String)__: The identifier of the Ocean CD Resource Response

__Returns__

`(Object)`: OceanCD Rollout List API response

<h2 id="spotinst_sdk2.clients.ocean_cd.OceanCDClient.ocean_cd_describe_rollout_phase">ocean_cd_describe_rollout_phase</h2>

```python
OceanCDClient.ocean_cd_describe_rollout_phase(rollout_id: str)
```

Ocean CD Rollout phase.

__Arguments__

- __rolloutId (String)__: The identifier of the Ocean CD phase

__Returns__

`(Object)`: OceanCD Rollout List API response

<h2 id="spotinst_sdk2.clients.ocean_cd.OceanCDClient.get_all_ocean_cd_workloads">get_all_ocean_cd_workloads</h2>

```python
OceanCDClient.get_all_ocean_cd_workloads()
```

List all Ocean CD workloads.

__Returns__

`(Object)`: OceanCD Workloads API response

<h2 id="spotinst_sdk2.clients.ocean_cd.OceanCDClient.ocean_cd_describe_workloads_migration_process">ocean_cd_describe_workloads_migration_process</h2>

```python
OceanCDClient.ocean_cd_describe_workloads_migration_process(
  deployment_name: str, namespace: str, cluster_id: str)
```

Describe How To Migrate Deployment CRD To SpotDeployment DRD.

__Arguments__

- __deployment_name (String)__: The identifier name of the Ocean CD Deployment
- __namespace (String)__: The workload's namespace
- __cluster_id (String)__: Cluster id where the workload is running

__Returns__

`(Object)`: OceanCD Workloads Migration API response

<h2 id="spotinst_sdk2.clients.ocean_cd.OceanCDClient.ocean_cd_describe_workloads_active_operations">ocean_cd_describe_workloads_active_operations</h2>

```python
OceanCDClient.ocean_cd_describe_workloads_active_operations(
  workload_id: str)
```

Describe What Operation Are Active For Specific Workload.

__Arguments__

- __workload_id (String)__: The workload's Id

__Returns__

`(Object)`: OceanCD Workloads Active Operations API response

<h2 id="spotinst_sdk2.clients.ocean_cd.OceanCDClient.ocean_cd_describe_workloads_revision">ocean_cd_describe_workloads_revision</h2>

```python
OceanCDClient.ocean_cd_describe_workloads_revision(workload_id: str)
```

Describe Workload's Revision.

__Arguments__

- __workload_id (String)__: The workload's Id

__Returns__

`(Object)`: OceanCD Workloads Revision API response

<h2 id="spotinst_sdk2.clients.ocean_cd.OceanCDClient.ocean_cd_describe_workloads_graph">ocean_cd_describe_workloads_graph</h2>

```python
OceanCDClient.ocean_cd_describe_workloads_graph(namespace: str,
                                                workload_name: str,
                                                cluster_id: str,
                                                kind: str)
```

Ocean CD workload graph.

__Arguments__

- __namespace (String)__: Workload's namespace name
- __workload_name (String)__: Workload name
- __cluster_id (String)__: Cluster id where the workload is running
- __kind (String)__: Kind of workload, currently only SpotDeployment is supported

__Returns__

`(Object)`: OceanCD Workloads Revision API response

<h2 id="spotinst_sdk2.clients.ocean_cd.OceanCDClient.ocean_cd_restart_workload">ocean_cd_restart_workload</h2>

```python
OceanCDClient.ocean_cd_restart_workload(workload_id: str)
```

Restart Workload By WorkloadId.

__Arguments__

- __workload_id (String)__: The workload's Id

__Returns__

`(Boolean)`: Response Status

<h2 id="spotinst_sdk2.clients.ocean_cd.OceanCDClient.ocean_cd_retry_workload">ocean_cd_retry_workload</h2>

```python
OceanCDClient.ocean_cd_retry_workload(revision_id: str, workload_id: str,
                                      rollout_id: str)
```

Retry Workload By WorkloadId,RevisionId And RolloutId

__Arguments__

- __revision_id (String)__: Relevant Revision Id
- __workload_id (String)__: The workload's Id
- __rollout_id (String)__: The rollout Id

__Returns__

`(Boolean)`: Response Status

<h2 id="spotinst_sdk2.clients.ocean_cd.OceanCDClient.ocean_cd_rollback_workload">ocean_cd_rollback_workload</h2>

```python
OceanCDClient.ocean_cd_rollback_workload(revision_id: str,
                                         workload_id: str,
                                         rollout_id: str)
```

Rollback Workload By WorkloadId,RevisionId And RolloutId

__Arguments__

- __revision_id (String)__: Relevant Revision Id
- __workload_id (String)__: The workload's Id
- __rollout_id (String)__: The rollout Id

__Returns__

`(Boolean)`: Response Status

