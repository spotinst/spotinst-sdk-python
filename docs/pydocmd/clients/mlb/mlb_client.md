<h1 id="spotinst_sdk.clients.mlb.MlbClient">MlbClient</h1>

```python
MlbClient(self, session=None, print_output=True, log_level=None, user_agent=None)
```

<h2 id="spotinst_sdk.clients.mlb.MlbClient.get_all_mlb_runtime">get_all_mlb_runtime</h2>

```python
MlbClient.get_all_mlb_runtime(self)
```

Get all MLB runtime

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.mlb.MlbClient.get_mlb_runtime">get_mlb_runtime</h2>

```python
MlbClient.get_mlb_runtime(self, runtime_id)
```

Get MLB runtime

__Arguments__

- __runtime_id (String)__: Runtime id name

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.mlb.MlbClient.deregister_mlb_runtime">deregister_mlb_runtime</h2>

```python
MlbClient.deregister_mlb_runtime(self, runtime_id)
```

Deregister MLB runtime

__Arguments__

- __runtime_id (String)__: Runtime id name

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.mlb.MlbClient.delete_mlb_runtime">delete_mlb_runtime</h2>

```python
MlbClient.delete_mlb_runtime(self, runtime_id)
```

Delete MLB runtime

__Arguments__

- __runtime_id (String)__: Runtime id name

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.mlb.MlbClient.create_mlb_deployment">create_mlb_deployment</h2>

```python
MlbClient.create_mlb_deployment(self, deployment_name)
```

Create MLB deployment

__Arguments__

- __deployment_name (String)__: Deployment name

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.mlb.MlbClient.update_mlb_deployment">update_mlb_deployment</h2>

```python
MlbClient.update_mlb_deployment(self, deployment_id, deployment_name)
```

Update MLB deployment

__Arguments__

- __deployment_name (String)__: Deployment name
- __deployment_id (String)__: Deployment Id

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.mlb.MlbClient.get_mlb_deployment">get_mlb_deployment</h2>

```python
MlbClient.get_mlb_deployment(self, deployment_id)
```

Get MLB deployment

__Arguments__

- __deployment_id (String)__: Deployment Id

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.mlb.MlbClient.get_all_mlb_deployment">get_all_mlb_deployment</h2>

```python
MlbClient.get_all_mlb_deployment(self)
```

Get All MLB deployment

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.mlb.MlbClient.delete_mlb_deployment">delete_mlb_deployment</h2>

```python
MlbClient.delete_mlb_deployment(self, deployment_id)
```

Delete MLB deployment

__Arguments__

- __deployment_id (String)__: Deployment Id

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.mlb.MlbClient.create_mlb_balancer">create_mlb_balancer</h2>

```python
MlbClient.create_mlb_balancer(self, balancer)
```

Create MLB balancer

__Arguments__

- __balancer (Balancer)__: Balancer Object

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.mlb.MlbClient.update_mlb_balancer">update_mlb_balancer</h2>

```python
MlbClient.update_mlb_balancer(self, balancer_id, balancer)
```

Create MLB balancer

__Arguments__

- __balancer_id (String)__: Balancer Id
- __balancer (Balancer)__: Balancer Object

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.mlb.MlbClient.get_mlb_balancer">get_mlb_balancer</h2>

```python
MlbClient.get_mlb_balancer(self, balancer_id)
```

Get MLB balancer

__Arguments__

- __balancer_id (String)__: Balancer Id

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.mlb.MlbClient.get_all_mlb_balancer">get_all_mlb_balancer</h2>

```python
MlbClient.get_all_mlb_balancer(self)
```

Get All MLB balancer

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.mlb.MlbClient.delete_mlb_balancer">delete_mlb_balancer</h2>

```python
MlbClient.delete_mlb_balancer(self, balancer_id)
```

Delete MLB balancer

__Arguments__

- __balancer_id (String)__: Balancer Id

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.mlb.MlbClient.create_mlb_target_set">create_mlb_target_set</h2>

```python
MlbClient.create_mlb_target_set(self, target_set)
```

Create MLB target set

__Arguments__

- __target_set (TargetSet)__: TargetSet Object

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.mlb.MlbClient.update_mlb_target_set">update_mlb_target_set</h2>

```python
MlbClient.update_mlb_target_set(self, target_set_id, target_set)
```

Update MLB target set

__Arguments__

- __target_set_id (String)__: Target Set Id
- __target_set (TargetSet)__: TargetSet Object

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.mlb.MlbClient.get_mlb_target_set">get_mlb_target_set</h2>

```python
MlbClient.get_mlb_target_set(self, target_set_id)
```

Gat an MLB target set

__Arguments__

- __target_set_id (String)__: Target Set Id

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.mlb.MlbClient.get_all_mlb_target_set">get_all_mlb_target_set</h2>

```python
MlbClient.get_all_mlb_target_set(self)
```

Get all MLB target sets

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.mlb.MlbClient.delete_mlb_target_set">delete_mlb_target_set</h2>

```python
MlbClient.delete_mlb_target_set(self, target_set_id)
```

Delete an MLB target set

__Arguments__

- __target_set_id (String)__: Target Set Id

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.mlb.MlbClient.register_mlb_targets">register_mlb_targets</h2>

```python
MlbClient.register_mlb_targets(self, target_set_id, targets)
```

Register MLB targets

__Arguments__

- __target_set_id (String)__: Target Set Id
- __Targets (List[Target])__: List of Target Objects

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.mlb.MlbClient.deregister_mlb_targets">deregister_mlb_targets</h2>

```python
MlbClient.deregister_mlb_targets(self, target_set_id, targets)
```

Deregister MLB targets

__Arguments__

- __target_set_id (String)__: Target Set Id
- __Targets (List[Target])__: List of Target Objects

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.mlb.MlbClient.create_mlb_target">create_mlb_target</h2>

```python
MlbClient.create_mlb_target(self, target)
```

Create MLB target

__Arguments__

- __target (Target)__: Target Object

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.mlb.MlbClient.update_mlb_target">update_mlb_target</h2>

```python
MlbClient.update_mlb_target(self, target_id, target)
```

Update MLB target

__Arguments__

- __target_id (String)__: Target Id
- __target (Target)__: Target Object

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.mlb.MlbClient.get_mlb_target">get_mlb_target</h2>

```python
MlbClient.get_mlb_target(self, target_id)
```

Get MLB target

__Arguments__

- __target_id (String)__: Target Id

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.mlb.MlbClient.get_all_mlb_target">get_all_mlb_target</h2>

```python
MlbClient.get_all_mlb_target(self)
```

Get all MLB target

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.mlb.MlbClient.delete_mlb_target">delete_mlb_target</h2>

```python
MlbClient.delete_mlb_target(self, target_id)
```

Delete MLB target

__Arguments__

- __target_id (String)__: Target Id

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.mlb.MlbClient.create_mlb_listener">create_mlb_listener</h2>

```python
MlbClient.create_mlb_listener(self, listener)
```

Create MLB listener

__Arguments__

- __listener (Listener)__: Listener Object

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.mlb.MlbClient.update_mlb_listener">update_mlb_listener</h2>

```python
MlbClient.update_mlb_listener(self, listener_id, listener)
```

Update MLB listener

__Arguments__

- __listener_id (String)__: Listener ID
- __listener (Listener)__: Listener Object

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.mlb.MlbClient.get_mlb_listener">get_mlb_listener</h2>

```python
MlbClient.get_mlb_listener(self, listener_id)
```

Get MLB listener

__Arguments__

- __listener_id (String)__: Listener ID

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.mlb.MlbClient.get_all_mlb_listener">get_all_mlb_listener</h2>

```python
MlbClient.get_all_mlb_listener(self)
```

Get all MLB listeners

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.mlb.MlbClient.delete_mlb_listener">delete_mlb_listener</h2>

```python
MlbClient.delete_mlb_listener(self, listener_id)
```

Delete MLB listener

__Arguments__

- __listener_id (String)__: Listener ID

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.mlb.MlbClient.create_mlb_routing_rule">create_mlb_routing_rule</h2>

```python
MlbClient.create_mlb_routing_rule(self, routing_rule)
```

Create MLB routing rule

__Arguments__

- __routing_rule (RoutingRule)__: RoutingRule Object

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.mlb.MlbClient.update_mlb_routing_rule">update_mlb_routing_rule</h2>

```python
MlbClient.update_mlb_routing_rule(self, routing_rule_id, routing_rule)
```

Update MLB routing rule

__Arguments__

- __routing_rule_id (String)__: Routing Rule Id
- __routing_rule (RoutingRule)__: RoutingRule Object

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.mlb.MlbClient.get_mlb_routing_rule">get_mlb_routing_rule</h2>

```python
MlbClient.get_mlb_routing_rule(self, routing_rule_id)
```

Get MLB routing rule

__Arguments__

- __routing_rule_id (String)__: Routing Rule Id

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.mlb.MlbClient.get_all_mlb_routing_rule">get_all_mlb_routing_rule</h2>

```python
MlbClient.get_all_mlb_routing_rule(self)
```

Get all MLB routing rule

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.mlb.MlbClient.delete_mlb_routing_rule">delete_mlb_routing_rule</h2>

```python
MlbClient.delete_mlb_routing_rule(self, routing_rule_id)
```

Delete MLB routing rule

__Arguments__

- __routing_rule_id (String)__: Routing Rule Id

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.mlb.MlbClient.create_mlb_middleware">create_mlb_middleware</h2>

```python
MlbClient.create_mlb_middleware(self, middleware)
```

Create MLB middleware

__Arguments__

- __middleware (Middleware)__: Middleware Object

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.mlb.MlbClient.update_mlb_middleware">update_mlb_middleware</h2>

```python
MlbClient.update_mlb_middleware(self, middleware_id, middleware)
```

Update MLB middleware

__Arguments__

- __middleware_id (String)__: Middleware ID
- __middleware (Middleware)__: Middleware Object

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.mlb.MlbClient.get_mlb_middleware">get_mlb_middleware</h2>

```python
MlbClient.get_mlb_middleware(self, middleware_id)
```

Get MLB middleware

__Arguments__

- __middleware_id (String)__: Middleware ID

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.mlb.MlbClient.get_all_mlb_middleware">get_all_mlb_middleware</h2>

```python
MlbClient.get_all_mlb_middleware(self)
```

Get all MLB middleware

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.mlb.MlbClient.delete_mlb_middleware">delete_mlb_middleware</h2>

```python
MlbClient.delete_mlb_middleware(self, middleware_id)
```

Delete MLB middleware

__Arguments__

- __middleware_id (String)__: Middleware ID

__Returns__

`(Object)`: Spotinst API response

