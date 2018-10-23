<h1 id="spotinst_sdk.SpotinstClient.create_blue_green_deployment">create_blue_green_deployment</h1>

```python
SpotinstClient.create_blue_green_deployment(self, group_id, blue_green_deployment)
```

Start a Blue Green Deployment

__Arguments__

- __group_id (String)__: Elastigroup ID
- __blue_green_deployment (BGDeployment)__: Blue Green Deployment Object

__Returns__

`(Object)`: Elastigroup API response

<h1 id="spotinst_sdk.SpotinstClient.get_blue_green_deployment">get_blue_green_deployment</h1>

```python
SpotinstClient.get_blue_green_deployment(self, group_id)
```

Get Blue Green Deployment for an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID

__Returns__

`(Object)`: Elastigroup API response

<h1 id="spotinst_sdk.SpotinstClient.stop_blue_green_deployment">stop_blue_green_deployment</h1>

```python
SpotinstClient.stop_blue_green_deployment(self, group_id, deployment_id)
```

Stop Blue Green Deployment for an elastigroup

__Arguments__

- __group_id (String)__: Elastigroup ID
- __deployment_id (String)__:  BG Deployment ID

__Returns__

`(Object)`: Elastigroup API response

