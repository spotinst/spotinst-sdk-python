<h1 id="spotinst_sdk2.models.ocean_cd">spotinst_sdk2.models.ocean_cd</h1>


<h2 id="spotinst_sdk2.models.ocean_cd.ClusterNotification">ClusterNotification</h2>

```python
ClusterNotification(
  self,
  minutes_without_heartbeat: int = 'd3043820717d74d9a17694c176d39733',
  providers: typing.List[str] = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __minutes_without_heartbeat__: int
- __providers__: List[str]

<h1 id="spotinst_sdk2.models.ocean_cd.rollout_spec">spotinst_sdk2.models.ocean_cd.rollout_spec</h1>


<h2 id="spotinst_sdk2.models.ocean_cd.rollout_spec.SpotDeployment">SpotDeployment</h2>

```python
SpotDeployment(self,
               cluster_id: str = 'd3043820717d74d9a17694c176d39733',
               name: str = 'd3043820717d74d9a17694c176d39733',
               namespace: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __cluster_id__: str
- __name__: str
- __namespace__: str

<h2 id="spotinst_sdk2.models.ocean_cd.rollout_spec.SecretRef">SecretRef</h2>

```python
SecretRef(self,
          name: str = 'd3043820717d74d9a17694c176d39733',
          key: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __key__: str

<h2 id="spotinst_sdk2.models.ocean_cd.rollout_spec.FieldRef">FieldRef</h2>

```python
FieldRef(self, field_path: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __field_path__: str

<h2 id="spotinst_sdk2.models.ocean_cd.rollout_spec.ValueFrom">ValueFrom</h2>

```python
ValueFrom(self,
          secret_ref: SecretRef = 'd3043820717d74d9a17694c176d39733',
          field_ref: FieldRef = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __secret_ref__: SecretRef
- __field_ref__: FieldRef

<h2 id="spotinst_sdk2.models.ocean_cd.rollout_spec.Argument">Argument</h2>

```python
Argument(self,
         name: str = 'd3043820717d74d9a17694c176d39733',
         value: str = 'd3043820717d74d9a17694c176d39733',
         value_from: ValueFrom = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __value__: str
- __value_from__: ValueFrom

<h2 id="spotinst_sdk2.models.ocean_cd.rollout_spec.Strategy">Strategy</h2>

```python
Strategy(
    self,
    name: str = 'd3043820717d74d9a17694c176d39733',
    args:
    typing.List[spotinst_sdk2.models.ocean_cd.rollout_spec.Argument] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __name__: str
- __args__: List[Argument]

<h2 id="spotinst_sdk2.models.ocean_cd.rollout_spec.TlsRoutes">TlsRoutes</h2>

```python
TlsRoutes(
  self,
  port: int = 'd3043820717d74d9a17694c176d39733',
  sni_hosts: typing.List[str] = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __port__: int
- __sni_hosts__: List[str]

<h2 id="spotinst_sdk2.models.ocean_cd.rollout_spec.VirtualServices">VirtualServices</h2>

```python
VirtualServices(
    self,
    name: str = 'd3043820717d74d9a17694c176d39733',
    routes: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
    tls_routes:
    typing.List[spotinst_sdk2.models.ocean_cd.rollout_spec.TlsRoutes] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __name__: str
- __routes__: List[str]
- __tls_routes__: List[TlsRoutes]

<h2 id="spotinst_sdk2.models.ocean_cd.rollout_spec.DestinationRule">DestinationRule</h2>

```python
DestinationRule(
  self,
  name: str = 'd3043820717d74d9a17694c176d39733',
  canary_subset_name: str = 'd3043820717d74d9a17694c176d39733',
  stable_subset_name: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __canary_subset_name__: str
- __stable_subset_name__: str

<h2 id="spotinst_sdk2.models.ocean_cd.rollout_spec.Istio">Istio</h2>

```python
Istio(
  self,
  virtual_services:
    typing.List[spotinst_sdk2.models.ocean_cd.rollout_spec.VirtualServices] = 'd3043820717d74d9a17694c176d39733',
  destination_rule: DestinationRule = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __virtual_services__: List[VirtualServices]
- __destination_rule__: DestinationRule

<h2 id="spotinst_sdk2.models.ocean_cd.rollout_spec.Nginx">Nginx</h2>

```python
Nginx(self,
      annotation_prefix: str = 'd3043820717d74d9a17694c176d39733',
      stable_ingress: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __annotation_prefix__: str
- __stable_ingress__: str

<h2 id="spotinst_sdk2.models.ocean_cd.rollout_spec.StickinessConfig">StickinessConfig</h2>

```python
StickinessConfig(
  self,
  enabled: bool = 'd3043820717d74d9a17694c176d39733',
  duration_seconds: int = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __enabled__: bool
- __duration_seconds__: int

<h2 id="spotinst_sdk2.models.ocean_cd.rollout_spec.Alb">Alb</h2>

```python
Alb(self,
    ingress: str = 'd3043820717d74d9a17694c176d39733',
    service_port: int = 'd3043820717d74d9a17694c176d39733',
    root_service: str = 'd3043820717d74d9a17694c176d39733',
    stickiness_config:
    StickinessConfig = 'd3043820717d74d9a17694c176d39733',
    annotation_prefix: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __ingress__: str
- __service_port__: int
- __root_service__: str
- __stickiness_config__: StickinessConfig
- __annotation_prefix__: str

<h2 id="spotinst_sdk2.models.ocean_cd.rollout_spec.Smi">Smi</h2>

```python
Smi(self,
    root_service: str = 'd3043820717d74d9a17694c176d39733',
    traffic_split_name: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __root_service__: str
- __traffic_split_name__: str

<h2 id="spotinst_sdk2.models.ocean_cd.rollout_spec.Ambassador">Ambassador</h2>

```python
Ambassador(
  self, mappings: typing.List[str] = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __mappings__: List[str]

<h2 id="spotinst_sdk2.models.ocean_cd.rollout_spec.VirtualService">VirtualService</h2>

```python
VirtualService(
  self,
  name: str = 'd3043820717d74d9a17694c176d39733',
  routes: typing.List[str] = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __routes__: List[str]

<h2 id="spotinst_sdk2.models.ocean_cd.rollout_spec.CanaryVirtualNodeRef">CanaryVirtualNodeRef</h2>

```python
CanaryVirtualNodeRef(self,
                     name: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str

<h2 id="spotinst_sdk2.models.ocean_cd.rollout_spec.StableVirtualNodeRef">StableVirtualNodeRef</h2>

```python
StableVirtualNodeRef(self,
                     name: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str

<h2 id="spotinst_sdk2.models.ocean_cd.rollout_spec.VirtualNodeGroup">VirtualNodeGroup</h2>

```python
VirtualNodeGroup(
    self,
    canary_virtual_node_ref:
    CanaryVirtualNodeRef = 'd3043820717d74d9a17694c176d39733',
    stable_virtual_node_ref:
    StableVirtualNodeRef = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __canary_virtual_node_ref__: CanaryVirtualNodeRef
- __stable_virtual_node_ref__: StableVirtualNodeRef

<h2 id="spotinst_sdk2.models.ocean_cd.rollout_spec.AppMesh">AppMesh</h2>

```python
AppMesh(
  self,
  virtual_service: VirtualService = 'd3043820717d74d9a17694c176d39733',
  virtual_node_group:
    VirtualNodeGroup = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __virtual_service__: VirtualService
- __virtual_node_group__: VirtualNodeGroup

<h2 id="spotinst_sdk2.models.ocean_cd.rollout_spec.PingPong">PingPong</h2>

```python
PingPong(self,
         ping_service: str = 'd3043820717d74d9a17694c176d39733',
         pong_service: str = 'd3043820717d74d9a17694c176d39733')
```

ping_service: str
pong_service: str

<h2 id="spotinst_sdk2.models.ocean_cd.rollout_spec.Traffic">Traffic</h2>

```python
Traffic(self,
        canary_service: str = 'd3043820717d74d9a17694c176d39733',
        stable_service: str = 'd3043820717d74d9a17694c176d39733',
        istio: Istio = 'd3043820717d74d9a17694c176d39733',
        nginx: Nginx = 'd3043820717d74d9a17694c176d39733',
        alb: Alb = 'd3043820717d74d9a17694c176d39733',
        smi: Smi = 'd3043820717d74d9a17694c176d39733',
        ambassador: Ambassador = 'd3043820717d74d9a17694c176d39733',
        app_mesh: AppMesh = 'd3043820717d74d9a17694c176d39733',
        ping_pong: PingPong = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __canary_service__: str
- __stable_service__: str
- __istio__: Istio
- __nginx__: Nginx
- __alb__: Alb
- __smi__: Smi
- __ambassador__: Ambassador
- __app_mesh__: AppMesh
- __ping_pong__: PingPong

<h2 id="spotinst_sdk2.models.ocean_cd.rollout_spec.FailureAction">FailureAction</h2>

```python
FailureAction(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean_cd.rollout_spec.FailureAction.abort">abort</h3>


<h3 id="spotinst_sdk2.models.ocean_cd.rollout_spec.FailureAction.pause">pause</h3>


<h3 id="spotinst_sdk2.models.ocean_cd.rollout_spec.FailureAction.promote">promote</h3>


<h2 id="spotinst_sdk2.models.ocean_cd.rollout_spec.FailurePolicy">FailurePolicy</h2>

```python
FailurePolicy(self,
              action: FailureAction = 'd3043820717d74d9a17694c176d39733'
              )
```

__Arguments__

- __action__: FailureAction

<h2 id="spotinst_sdk2.models.ocean_cd.rollout_spec.RolloutSpec">RolloutSpec</h2>

```python
RolloutSpec(
  self,
  name: str = 'd3043820717d74d9a17694c176d39733',
  spot_deployment: SpotDeployment = 'd3043820717d74d9a17694c176d39733',
  strategy: Strategy = 'd3043820717d74d9a17694c176d39733',
  traffic: Traffic = 'd3043820717d74d9a17694c176d39733',
  failure_policy: FailurePolicy = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __spot_deployment__: SpotDeployment
- __strategy__: Strategy
- __traffic__: Traffic
- __failure_policy__: FailurePolicy

<h2 id="spotinst_sdk2.models.ocean_cd.rollout_spec.CreateRolloutSpecRequest">CreateRolloutSpecRequest</h2>

```python
CreateRolloutSpecRequest(self, rollout_spec: RolloutSpec)
```

__Arguments__

- __rollout_spec __: RolloutSpec

<h1 id="spotinst_sdk2.models.ocean_cd.rollout">spotinst_sdk2.models.ocean_cd.rollout</h1>


<h2 id="spotinst_sdk2.models.ocean_cd.rollout.SpotDeployment">SpotDeployment</h2>

```python
SpotDeployment(self,
               name: str = 'd3043820717d74d9a17694c176d39733',
               old_version: str = 'd3043820717d74d9a17694c176d39733',
               new_version: str = 'd3043820717d74d9a17694c176d39733',
               old_manifest: str = 'd3043820717d74d9a17694c176d39733',
               new_manifest: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __old_version__: str
- __new_version__: str
- __old_manifest__: str
- __new_manifest__: str

<h2 id="spotinst_sdk2.models.ocean_cd.rollout.Status">Status</h2>

```python
Status(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean_cd.rollout.Status.aborted">aborted</h3>


<h3 id="spotinst_sdk2.models.ocean_cd.rollout.Status.aborting">aborting</h3>


<h3 id="spotinst_sdk2.models.ocean_cd.rollout.Status.canceled">canceled</h3>


<h3 id="spotinst_sdk2.models.ocean_cd.rollout.Status.deallocating">deallocating</h3>


<h3 id="spotinst_sdk2.models.ocean_cd.rollout.Status.failed">failed</h3>


<h3 id="spotinst_sdk2.models.ocean_cd.rollout.Status.finished">finished</h3>


<h3 id="spotinst_sdk2.models.ocean_cd.rollout.Status.in_progress">in_progress</h3>


<h3 id="spotinst_sdk2.models.ocean_cd.rollout.Status.manual_paused">manual_paused</h3>


<h3 id="spotinst_sdk2.models.ocean_cd.rollout.Status.manual_pausing">manual_pausing</h3>


<h3 id="spotinst_sdk2.models.ocean_cd.rollout.Status.paused">paused</h3>


<h3 id="spotinst_sdk2.models.ocean_cd.rollout.Status.pending">pending</h3>


<h2 id="spotinst_sdk2.models.ocean_cd.rollout.Rollouts">Rollouts</h2>

```python
Rollouts(
  self,
  spot_deployment: SpotDeployment = 'd3043820717d74d9a17694c176d39733',
  namespace: str = 'd3043820717d74d9a17694c176d39733',
  cluster_id: str = 'd3043820717d74d9a17694c176d39733',
  original_rollout_id: str = 'd3043820717d74d9a17694c176d39733',
  new_rollout_id: str = 'd3043820717d74d9a17694c176d39733',
  strategy: str = 'd3043820717d74d9a17694c176d39733',
  strategy_type: str = 'd3043820717d74d9a17694c176d39733',
  strategy_name: str = 'd3043820717d74d9a17694c176d39733',
  status: Status = 'd3043820717d74d9a17694c176d39733',
  start_time: str = 'd3043820717d74d9a17694c176d39733',
  end_time: str = 'd3043820717d74d9a17694c176d39733',
  rollout_spec: str = 'd3043820717d74d9a17694c176d39733',
  cloud_provider: str = 'd3043820717d74d9a17694c176d39733',
  identity: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __spot_deployment__: SpotDeployment
- __namespace__: str
- __cluster_id__: str
- __original_rollout_id__: str
- __new_rollout_id__: str
- __strategy__: str
- __strategy_type__: str
- __strategy_name__: str
- __status__: Status
- __start_time__: str
- __end_time__: str
- __rollout_spec__: str
- __cloud_provider__: str
- __identity__: str

<h2 id="spotinst_sdk2.models.ocean_cd.rollout.Action">Action</h2>

```python
Action(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean_cd.rollout.Action.abort">abort</h3>


<h3 id="spotinst_sdk2.models.ocean_cd.rollout.Action.pause">pause</h3>


<h3 id="spotinst_sdk2.models.ocean_cd.rollout.Action.promote">promote</h3>


<h3 id="spotinst_sdk2.models.ocean_cd.rollout.Action.promote_full">promote_full</h3>


<h3 id="spotinst_sdk2.models.ocean_cd.rollout.Action.retry">retry</h3>


<h2 id="spotinst_sdk2.models.ocean_cd.rollout.CreateRolloutActionRequest">CreateRolloutActionRequest</h2>

```python
CreateRolloutActionRequest(self, action: Action)
```

__Arguments__

- __action __: Action

<h1 id="spotinst_sdk2.models.ocean_cd.strategy">spotinst_sdk2.models.ocean_cd.strategy</h1>


<h2 id="spotinst_sdk2.models.ocean_cd.strategy.BackgroundVerification">BackgroundVerification</h2>

```python
BackgroundVerification(
  self,
  template_names: typing.List[str] = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __template_names__: List[str]

<h2 id="spotinst_sdk2.models.ocean_cd.strategy.SetCanaryScale">SetCanaryScale</h2>

```python
SetCanaryScale(
  self,
  match_traffic_weight: bool = 'd3043820717d74d9a17694c176d39733',
  replicas: int = 'd3043820717d74d9a17694c176d39733',
  weight: int = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __match_traffic_weight__: bool
- __replicas__: int
- __weight__: int

<h2 id="spotinst_sdk2.models.ocean_cd.strategy.Verification">Verification</h2>

```python
Verification(
  self,
  template_names: typing.List[str] = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __template_names__: List[str]

<h2 id="spotinst_sdk2.models.ocean_cd.strategy.Pause">Pause</h2>

```python
Pause(self, duration: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __duration__: str

<h2 id="spotinst_sdk2.models.ocean_cd.strategy.HeaderValue">HeaderValue</h2>

```python
HeaderValue(self,
            exact: str = 'd3043820717d74d9a17694c176d39733',
            prefix: str = 'd3043820717d74d9a17694c176d39733',
            regex: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __exact__: str
- __prefix__: str
- __regex__: str

<h2 id="spotinst_sdk2.models.ocean_cd.strategy.Match">Match</h2>

```python
Match(self,
      header_name: str = 'd3043820717d74d9a17694c176d39733',
      header_value: HeaderValue = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __header_name__: str
- __header_value__: HeaderValue

<h2 id="spotinst_sdk2.models.ocean_cd.strategy.HeaderRoute">HeaderRoute</h2>

```python
HeaderRoute(
    self,
    name: str = 'd3043820717d74d9a17694c176d39733',
    match:
    typing.List[spotinst_sdk2.models.ocean_cd.strategy.Match] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __name__: str
- __match__: List[Match]

<h2 id="spotinst_sdk2.models.ocean_cd.strategy.CanarySteps">CanarySteps</h2>

```python
CanarySteps(
  self,
  name: str = 'd3043820717d74d9a17694c176d39733',
  set_weight: int = 'd3043820717d74d9a17694c176d39733',
  set_canary_scale: SetCanaryScale = 'd3043820717d74d9a17694c176d39733',
  verification: Verification = 'd3043820717d74d9a17694c176d39733',
  pause: Pause = 'd3043820717d74d9a17694c176d39733',
  set_header_route: HeaderRoute = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __set_weight__: int
- __set_canary_scale__: SetCanaryScale
- __verification__: Verification
- __pause__: Pause
- __set_header_route__: HeaderRoute

<h2 id="spotinst_sdk2.models.ocean_cd.strategy.Canary">Canary</h2>

```python
Canary(
    self,
    background_verification:
    BackgroundVerification = 'd3043820717d74d9a17694c176d39733',
    steps:
    typing.List[spotinst_sdk2.models.ocean_cd.strategy.CanarySteps] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __background_verification__: BackgroundVerification
- __steps__: List[CanarySteps]

<h2 id="spotinst_sdk2.models.ocean_cd.strategy.RollingSteps">RollingSteps</h2>

```python
RollingSteps(
  self,
  name: str = 'd3043820717d74d9a17694c176d39733',
  pause: Pause = 'd3043820717d74d9a17694c176d39733',
  verification: Verification = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __pause__: Pause
- __verification__: Verification

<h2 id="spotinst_sdk2.models.ocean_cd.strategy.Strategy">Strategy</h2>

```python
Strategy(self,
         name: str = 'd3043820717d74d9a17694c176d39733',
         canary: Canary = 'd3043820717d74d9a17694c176d39733',
         rolling: RollingSteps = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __canary__: Canary
- __rolling__: RollingSteps

<h2 id="spotinst_sdk2.models.ocean_cd.strategy.CreateStrategyRequest">CreateStrategyRequest</h2>

```python
CreateStrategyRequest(self, strategy: Strategy)
```

__Arguments__

- __strategy __: Strategy

<h1 id="spotinst_sdk2.models.ocean_cd.verification_provider">spotinst_sdk2.models.ocean_cd.verification_provider</h1>


<h2 id="spotinst_sdk2.models.ocean_cd.verification_provider.Prometheus">Prometheus</h2>

```python
Prometheus(self, address: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __address __: str

<h2 id="spotinst_sdk2.models.ocean_cd.verification_provider.Datadog">Datadog</h2>

```python
Datadog(self,
        address: str = 'd3043820717d74d9a17694c176d39733',
        api_key: str = 'd3043820717d74d9a17694c176d39733',
        app_key: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __address __: str
- __api_key __: str
- __app_key __: str

<h2 id="spotinst_sdk2.models.ocean_cd.verification_provider.NewRelic">NewRelic</h2>

```python
NewRelic(self,
         account_id: str = 'd3043820717d74d9a17694c176d39733',
         base_url_nerd_graph: str = 'd3043820717d74d9a17694c176d39733',
         base_url_rest: str = 'd3043820717d74d9a17694c176d39733',
         personal_api_key: str = 'd3043820717d74d9a17694c176d39733',
         region: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __account_id __: str
- __base_url_nerd_graph __: str
- __base_url_rest __: str
- __personal_api_key __: str
- __region __: str

<h2 id="spotinst_sdk2.models.ocean_cd.verification_provider.CloudWatch">CloudWatch</h2>

```python
CloudWatch(self, iam_arn: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __iam_arn __: str

<h2 id="spotinst_sdk2.models.ocean_cd.verification_provider.VerificationProvider">VerificationProvider</h2>

```python
VerificationProvider(
  self,
  name: str = 'd3043820717d74d9a17694c176d39733',
  cluster_ids: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  prometheus: Prometheus = 'd3043820717d74d9a17694c176d39733',
  datadog: Datadog = 'd3043820717d74d9a17694c176d39733',
  new_relic: NewRelic = 'd3043820717d74d9a17694c176d39733',
  cloud_watch: CloudWatch = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name __: str
- __cluster_ids __: List[str]
- __prometheus __: Prometheus
- __datadog __: Datadog
- __newRelic __: NewRelic
- __cloudWatch __: CloudWatch

<h2 id="spotinst_sdk2.models.ocean_cd.verification_provider.CreateVerificationProviderRequest">CreateVerificationProviderRequest</h2>

```python
CreateVerificationProviderRequest(
  self, verification_provider: VerificationProvider)
```

__Arguments__

- __verification_provider __: VerificationProvider

<h1 id="spotinst_sdk2.models.ocean_cd.verification_template">spotinst_sdk2.models.ocean_cd.verification_template</h1>


<h2 id="spotinst_sdk2.models.ocean_cd.verification_template.SecretKeyRef">SecretKeyRef</h2>

```python
SecretKeyRef(self,
             key: str = 'd3043820717d74d9a17694c176d39733',
             name: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __key __: str
- __name __: str

<h2 id="spotinst_sdk2.models.ocean_cd.verification_template.VerificationTemplateArgument">VerificationTemplateArgument</h2>

```python
VerificationTemplateArgument(
  self,
  name: str = 'd3043820717d74d9a17694c176d39733',
  secret_key_ref: SecretKeyRef = 'd3043820717d74d9a17694c176d39733',
  value: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name __: str
- __secret_key_ref __: SecretKeyRef
- __value __: str

<h2 id="spotinst_sdk2.models.ocean_cd.verification_template.Prometheus">Prometheus</h2>

```python
Prometheus(self, query: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __query __: str

<h2 id="spotinst_sdk2.models.ocean_cd.verification_template.NewRelic">NewRelic</h2>

```python
NewRelic(self,
         profile: str = 'd3043820717d74d9a17694c176d39733',
         query: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __profile __: str
- __query __: str

<h2 id="spotinst_sdk2.models.ocean_cd.verification_template.Datadog">Datadog</h2>

```python
Datadog(self,
        duration: str = 'd3043820717d74d9a17694c176d39733',
        query: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __duration __: str
- __query __: str

<h2 id="spotinst_sdk2.models.ocean_cd.verification_template.Dimensions">Dimensions</h2>

```python
Dimensions(self,
           name: str = 'd3043820717d74d9a17694c176d39733',
           value: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name __: str
- __value __: str

<h2 id="spotinst_sdk2.models.ocean_cd.verification_template.MetricUnit">MetricUnit</h2>

```python
MetricUnit(cls, value, names=None, *, module, qualname, type, start)
```
An enumeration.
<h3 id="spotinst_sdk2.models.ocean_cd.verification_template.MetricUnit.Bits">Bits</h3>


<h3 id="spotinst_sdk2.models.ocean_cd.verification_template.MetricUnit.BitsBySecond">BitsBySecond</h3>


<h3 id="spotinst_sdk2.models.ocean_cd.verification_template.MetricUnit.Bytes">Bytes</h3>


<h3 id="spotinst_sdk2.models.ocean_cd.verification_template.MetricUnit.BytesBySecond">BytesBySecond</h3>


<h3 id="spotinst_sdk2.models.ocean_cd.verification_template.MetricUnit.Count">Count</h3>


<h3 id="spotinst_sdk2.models.ocean_cd.verification_template.MetricUnit.CountBySecond">CountBySecond</h3>


<h3 id="spotinst_sdk2.models.ocean_cd.verification_template.MetricUnit.Gigabits">Gigabits</h3>


<h3 id="spotinst_sdk2.models.ocean_cd.verification_template.MetricUnit.GigabitsBySecond">GigabitsBySecond</h3>


<h3 id="spotinst_sdk2.models.ocean_cd.verification_template.MetricUnit.Gigabytes">Gigabytes</h3>


<h3 id="spotinst_sdk2.models.ocean_cd.verification_template.MetricUnit.GigabytesBySecond">GigabytesBySecond</h3>


<h3 id="spotinst_sdk2.models.ocean_cd.verification_template.MetricUnit.Kilobits">Kilobits</h3>


<h3 id="spotinst_sdk2.models.ocean_cd.verification_template.MetricUnit.KilobitsBySecond">KilobitsBySecond</h3>


<h3 id="spotinst_sdk2.models.ocean_cd.verification_template.MetricUnit.Kilobytes">Kilobytes</h3>


<h3 id="spotinst_sdk2.models.ocean_cd.verification_template.MetricUnit.KilobytesBySecond">KilobytesBySecond</h3>


<h3 id="spotinst_sdk2.models.ocean_cd.verification_template.MetricUnit.Megabits">Megabits</h3>


<h3 id="spotinst_sdk2.models.ocean_cd.verification_template.MetricUnit.MegabitsBySecond">MegabitsBySecond</h3>


<h3 id="spotinst_sdk2.models.ocean_cd.verification_template.MetricUnit.Megabytes">Megabytes</h3>


<h3 id="spotinst_sdk2.models.ocean_cd.verification_template.MetricUnit.MegabytesBySecond">MegabytesBySecond</h3>


<h3 id="spotinst_sdk2.models.ocean_cd.verification_template.MetricUnit.Microseconds">Microseconds</h3>


<h3 id="spotinst_sdk2.models.ocean_cd.verification_template.MetricUnit.Milliseconds">Milliseconds</h3>


<h3 id="spotinst_sdk2.models.ocean_cd.verification_template.MetricUnit.NONE">NONE</h3>


<h3 id="spotinst_sdk2.models.ocean_cd.verification_template.MetricUnit.Percent">Percent</h3>


<h3 id="spotinst_sdk2.models.ocean_cd.verification_template.MetricUnit.Seconds">Seconds</h3>


<h3 id="spotinst_sdk2.models.ocean_cd.verification_template.MetricUnit.Terabits">Terabits</h3>


<h3 id="spotinst_sdk2.models.ocean_cd.verification_template.MetricUnit.TerabitsBySecond">TerabitsBySecond</h3>


<h3 id="spotinst_sdk2.models.ocean_cd.verification_template.MetricUnit.Terabytes">Terabytes</h3>


<h3 id="spotinst_sdk2.models.ocean_cd.verification_template.MetricUnit.TerabytesBySecond">TerabytesBySecond</h3>


<h2 id="spotinst_sdk2.models.ocean_cd.verification_template.Metric">Metric</h2>

```python
Metric(
    self,
    metric_name: str = 'd3043820717d74d9a17694c176d39733',
    namespace: str = 'd3043820717d74d9a17694c176d39733',
    dimensions:
    typing.List[spotinst_sdk2.models.ocean_cd.verification_template.Dimensions] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __metric_name __: str
- __namespace __: str
- __dimensions __: List[Dimensions]

<h2 id="spotinst_sdk2.models.ocean_cd.verification_template.MetricStat">MetricStat</h2>

```python
MetricStat(self,
           metric: Metric = 'd3043820717d74d9a17694c176d39733',
           period: int = 'd3043820717d74d9a17694c176d39733',
           stat: str = 'd3043820717d74d9a17694c176d39733',
           unit: MetricUnit = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __metric __: Metric
- __period __: int
- __stat __: str
- __unit __: MetricUnit

<h2 id="spotinst_sdk2.models.ocean_cd.verification_template.MetricDataQueries">MetricDataQueries</h2>

```python
MetricDataQueries(
  self,
  id: str = 'd3043820717d74d9a17694c176d39733',
  metric_stat: MetricStat = 'd3043820717d74d9a17694c176d39733',
  expression: str = 'd3043820717d74d9a17694c176d39733',
  label: str = 'd3043820717d74d9a17694c176d39733',
  return_data: bool = 'd3043820717d74d9a17694c176d39733',
  period: int = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __id __: str
- __metric_stat __: MetricStat
- __expression __: str
- __label __: str
- __return_data __: boolean
- __period __: int

<h2 id="spotinst_sdk2.models.ocean_cd.verification_template.CloudWatch">CloudWatch</h2>

```python
CloudWatch(
    self,
    duration: str = 'd3043820717d74d9a17694c176d39733',
    metric_data_queries:
    typing.List[spotinst_sdk2.models.ocean_cd.verification_template.MetricDataQueries] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __duration __: str
- __metric_data_queries __: List[MetricDataQueries]

<h2 id="spotinst_sdk2.models.ocean_cd.verification_template.Headers">Headers</h2>

```python
Headers(self,
        key: str = 'd3043820717d74d9a17694c176d39733',
        value: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __key __: str
- __value __: str

<h2 id="spotinst_sdk2.models.ocean_cd.verification_template.Web">Web</h2>

```python
Web(
  self,
  method: str = 'd3043820717d74d9a17694c176d39733',
  url: str = 'd3043820717d74d9a17694c176d39733',
  headers:
    typing.List[spotinst_sdk2.models.ocean_cd.verification_template.Headers] = 'd3043820717d74d9a17694c176d39733',
  body: str = 'd3043820717d74d9a17694c176d39733',
  timeout_seconds: int = 'd3043820717d74d9a17694c176d39733',
  json_path: str = 'd3043820717d74d9a17694c176d39733',
  insecure: bool = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __method __: str
- __url __: str
- __headers __: List[Headers]
- __body __: str
- __timeout_seconds __: int
- __json_path __: str
- __insecure __: bool

<h2 id="spotinst_sdk2.models.ocean_cd.verification_template.Containers">Containers</h2>

```python
Containers(
  self,
  name: str = 'd3043820717d74d9a17694c176d39733',
  command: typing.List[str] = 'd3043820717d74d9a17694c176d39733',
  image: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name __: str
- __command __: List[str]
- __image __: str

<h2 id="spotinst_sdk2.models.ocean_cd.verification_template.TemplateSpec">TemplateSpec</h2>

```python
TemplateSpec(
  self,
  containers:
    typing.List[spotinst_sdk2.models.ocean_cd.verification_template.Containers] = 'd3043820717d74d9a17694c176d39733',
  restart_policy: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __containers __: List[Containers]
- __restart_policy __: str

<h2 id="spotinst_sdk2.models.ocean_cd.verification_template.JobSpec">JobSpec</h2>

```python
JobSpec(self,
        backoff_limit: int = 'd3043820717d74d9a17694c176d39733',
        template: TemplateSpec = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __backoff_limit __: int
- __template __: TemplateSpec

<h2 id="spotinst_sdk2.models.ocean_cd.verification_template.Job">Job</h2>

```python
Job(self, spec: JobSpec = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __spec __: JobSpec

<h2 id="spotinst_sdk2.models.ocean_cd.verification_template.Provider">Provider</h2>

```python
Provider(self,
         prometheus: Prometheus = 'd3043820717d74d9a17694c176d39733',
         new_relic: NewRelic = 'd3043820717d74d9a17694c176d39733',
         datadog: Datadog = 'd3043820717d74d9a17694c176d39733',
         cloud_watch: CloudWatch = 'd3043820717d74d9a17694c176d39733',
         web: Web = 'd3043820717d74d9a17694c176d39733',
         job: Job = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __prometheus __: Prometheus
- __new_relic __: NewRelic
- __datadog __: Datadog
- __cloud_watch __: CloudWatch
- __web __: Web
- __job __: Job

<h2 id="spotinst_sdk2.models.ocean_cd.verification_template.VerificationMetric">VerificationMetric</h2>

```python
VerificationMetric(
  self,
  name: str = 'd3043820717d74d9a17694c176d39733',
  dry_run: bool = 'd3043820717d74d9a17694c176d39733',
  interval: str = 'd3043820717d74d9a17694c176d39733',
  initial_delay: str = 'd3043820717d74d9a17694c176d39733',
  count: int = 'd3043820717d74d9a17694c176d39733',
  success_condition: str = 'd3043820717d74d9a17694c176d39733',
  failure_condition: str = 'd3043820717d74d9a17694c176d39733',
  failure_limit: int = 'd3043820717d74d9a17694c176d39733',
  consecutive_error_limit: int = 'd3043820717d74d9a17694c176d39733',
  provider: Provider = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name __: str
- __dry_run __: boolean
- __interval __: str
- __initial_delay __: str
- __count __: int
- __success_condition __: str
- __failure_condition __: str
- __failure_limit __: int
- __consecutive_error_limit __: int
- __provider __: Provider

<h2 id="spotinst_sdk2.models.ocean_cd.verification_template.VerificationTemplate">VerificationTemplate</h2>

```python
VerificationTemplate(
  self,
  name: str = 'd3043820717d74d9a17694c176d39733',
  args:
    typing.List[spotinst_sdk2.models.ocean_cd.verification_template.VerificationTemplateArgument] = 'd3043820717d74d9a17694c176d39733',
  metrics:
    typing.List[spotinst_sdk2.models.ocean_cd.verification_template.VerificationMetric] = 'd3043820717d74d9a17694c176d39733',
  created_at: str = 'd3043820717d74d9a17694c176d39733',
  updated_at: str = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name __: str
- __args __: List[VerificationTemplateArgument]
- __metrics __: List[VerificationMetric]

<h2 id="spotinst_sdk2.models.ocean_cd.verification_template.CreateVerificationTemplateRequest">CreateVerificationTemplateRequest</h2>

```python
CreateVerificationTemplateRequest(
  self, verification_template: VerificationTemplate)
```

__Arguments__

- __verification_template __: VerificationTemplate

