<h1 id="spotinst_sdk.spotinst_mlb">spotinst_sdk.spotinst_mlb</h1>


<h2 id="spotinst_sdk.spotinst_mlb.Balancer">Balancer</h2>

```python
Balancer(self, name='d3043820717d74d9a17694c176d39733', timeouts='d3043820717d74d9a17694c176d39733', tags='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __timeouts__: Timeout
- __tags__: List[Tag]

<h2 id="spotinst_sdk.spotinst_mlb.Timeout">Timeout</h2>

```python
Timeout(self, draining='d3043820717d74d9a17694c176d39733', idle='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __draining__: int
- __idle__: int

<h2 id="spotinst_sdk.spotinst_mlb.Tag">Tag</h2>

```python
Tag(self, key='d3043820717d74d9a17694c176d39733', value='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __key__: str
- __value__: str

<h2 id="spotinst_sdk.spotinst_mlb.TargetSet">TargetSet</h2>

```python
TargetSet(self, name='d3043820717d74d9a17694c176d39733', balancer_id='d3043820717d74d9a17694c176d39733', deployment_id='d3043820717d74d9a17694c176d39733', protocol='d3043820717d74d9a17694c176d39733', weight='d3043820717d74d9a17694c176d39733', config='d3043820717d74d9a17694c176d39733', integrations='d3043820717d74d9a17694c176d39733', health_check='d3043820717d74d9a17694c176d39733', tags='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __balancer_id__: str
- __deployment_id__: str
- __protocol__: str
- __weight__: int
- __config__: Config
- __integrations__: Integrations
- __health_check__: HealthCheck
- __tags__: List[Tag]

<h2 id="spotinst_sdk.spotinst_mlb.Config">Config</h2>

```python
Config(self, rate_limiter='d3043820717d74d9a17694c176d39733')
```

__Argument__

rate_limiter: RateLimiter

<h2 id="spotinst_sdk.spotinst_mlb.RateLimiter">RateLimiter</h2>

```python
RateLimiter(self, requests_per_second='d3043820717d74d9a17694c176d39733')
```

__Argument__

request_per_second: int

<h2 id="spotinst_sdk.spotinst_mlb.Integrations">Integrations</h2>

```python
Integrations(self, ecs='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __ecs__: List[ECS]

<h2 id="spotinst_sdk.spotinst_mlb.ECS">ECS</h2>

```python
ECS(self, target_group_arn='d3043820717d74d9a17694c176d39733', target_group_name='d3043820717d74d9a17694c176d39733', region='d3043820717d74d9a17694c176d39733', service_name='d3043820717d74d9a17694c176d39733', cluster_name='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __target_group_arn__: str
- __target_group_name__: str
- __region__: str
- __service_name__: str
- __cluster_name__: str

<h2 id="spotinst_sdk.spotinst_mlb.HealthCheck">HealthCheck</h2>

```python
HealthCheck(self, interval='d3043820717d74d9a17694c176d39733', path='d3043820717d74d9a17694c176d39733', port='d3043820717d74d9a17694c176d39733', protocol='d3043820717d74d9a17694c176d39733', timeout='d3043820717d74d9a17694c176d39733', healthy_threshold_count='d3043820717d74d9a17694c176d39733', unhealthy_threshold_count='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __interval__: int
- __path__: str
- __port__: int
- __protocol__: str
- __timeout__: int
- __healthy_threshold_count__: int
- __unhealthy_threshold_count__: int

<h2 id="spotinst_sdk.spotinst_mlb.Target">Target</h2>

```python
Target(self, tags='d3043820717d74d9a17694c176d39733', name='d3043820717d74d9a17694c176d39733', id='d3043820717d74d9a17694c176d39733', balancer_id='d3043820717d74d9a17694c176d39733', port='d3043820717d74d9a17694c176d39733', target_set_id='d3043820717d74d9a17694c176d39733', host='d3043820717d74d9a17694c176d39733', weight='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __id__: str (Deregister Target)
- __balancer_id__: (Create Target)
- __target_set_id__: (Create Target)
- __name__: str (Create & Register Target)
- __host__: str (Create & Register Target)
- __port__: int (Create Target)
- __weight__: int (Create & Register Target)
- __tags__: List[Tags] (Create & Register Target)

<h2 id="spotinst_sdk.spotinst_mlb.Middleware">Middleware</h2>

```python
Middleware(self, balancer_id='d3043820717d74d9a17694c176d39733', type='d3043820717d74d9a17694c176d39733', priority='d3043820717d74d9a17694c176d39733', spec='d3043820717d74d9a17694c176d39733', tags='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __balancer_id__: str
- __type__: str
- __priority__: int
- __spec__: Spec
- __tags__: List[Tag]

<h2 id="spotinst_sdk.spotinst_mlb.Spec">Spec</h2>

```python
Spec(self, action='d3043820717d74d9a17694c176d39733', conditions='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __action__: str
- __conditions__: List[Condition]

<h2 id="spotinst_sdk.spotinst_mlb.Condition">Condition</h2>

```python
Condition(self, type='d3043820717d74d9a17694c176d39733', values='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __type__: str
- __values__: List[str]

<h2 id="spotinst_sdk.spotinst_mlb.Listener">Listener</h2>

```python
Listener(self, balancer_id='d3043820717d74d9a17694c176d39733', protocol='d3043820717d74d9a17694c176d39733', port='d3043820717d74d9a17694c176d39733', tls_config='d3043820717d74d9a17694c176d39733', tags='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __balancer_id__: str
- __protocol__: str
- __port__: int
- __tls_config__: TLSConfig
- __tags__: List[Tag]

<h2 id="spotinst_sdk.spotinst_mlb.TLSConfig">TLSConfig</h2>

```python
TLSConfig(self, min_version='d3043820717d74d9a17694c176d39733', max_version='d3043820717d74d9a17694c176d39733', session_tickets_disabled='d3043820717d74d9a17694c176d39733', prefer_server_cipher_suites='d3043820717d74d9a17694c176d39733', cipher_suites='d3043820717d74d9a17694c176d39733', insecure_skip_verify='d3043820717d74d9a17694c176d39733', certificate_ids='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __min_version__: str
- __max_version__: str
- __session_ticket_disabled__: bool
- __prefer_service_cipher_suites__: bool
- __cipher_suites__: List[str]
- __insecure_skip_verify__: bool
- __certificate_ids__: List[str]

<h2 id="spotinst_sdk.spotinst_mlb.RoutingRule">RoutingRule</h2>

```python
RoutingRule(self, balancer_id='d3043820717d74d9a17694c176d39733', route='d3043820717d74d9a17694c176d39733', target_set_ids='d3043820717d74d9a17694c176d39733', middleware_ids='d3043820717d74d9a17694c176d39733', listener_id='d3043820717d74d9a17694c176d39733', priority='d3043820717d74d9a17694c176d39733', tags='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __balancer_id__: str
- __route__: str
- __target_set_ids__: List[str]
- __middleware_ids__: List[str]
- __listener_id__: str
- __priority__: int
- __tags__: List[Tag]

