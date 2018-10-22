<h1 id="spotinst_sdk.SpotinstClient.roll_group">roll_group</h1>

```python
SpotinstClient.roll_group(self, group_id, group_roll)
```

Roll an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __group_roll (ElastigroupRoll)__: GroupRoll Object

__Returns__

`(Object)`: Elastigroup API response

<h1 id="spotinst_sdk.SpotinstClient.get_deployment_status">get_deployment_status</h1>

```python
SpotinstClient.get_deployment_status(self, group_id, roll_id)
```

get all a deployment status from an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __roll_id (String)__: Deployment ID

__Returns__

`(Object)`: Elastigroup API response

<h1 id="spotinst_sdk.SpotinstClient.stop_deployment">stop_deployment</h1>

```python
SpotinstClient.stop_deployment(self, group_id, roll_id)
```

stop a deployment from an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __roll_id (String)__: Deployment ID

__Returns__

`(Object)`: Elastigroup API response

<h1 id="spotinst_sdk.SpotinstClient.create_deployment_action">create_deployment_action</h1>

```python
SpotinstClient.create_deployment_action(self, group_id, roll_id, deployment_action)
```

create a deployment from an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __roll_id (String)__: Deployment ID
- __deployment_action (Deployment)__: Deployment Object

__Returns__

`(Object) `: Elastigroup API response

