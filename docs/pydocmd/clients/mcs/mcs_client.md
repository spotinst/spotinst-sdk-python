<h1 id="spotinst_sdk.clients.mcs.McsClient">McsClient</h1>

```python
McsClient(self, session=None, print_output=True, log_level=None, user_agent=None)
```

<h2 id="spotinst_sdk.clients.mcs.McsClient.get_kubernetes_cluster_cost">get_kubernetes_cluster_cost</h2>

```python
McsClient.get_kubernetes_cluster_cost(self, custer_id, from_date, to_date)
```

Get kubernetes cluster cost

__Arguments__

- __custer_id (String)__: Kubernetes cluster id
- __from_date (String)__: From date
- __to_date (String)__: to date

__Returns__

`(Object)`: Elastigroup API response

