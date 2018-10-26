<h1 id="spotinst_sdk.SpotinstClient.create_emr">create_emr</h1>

```python
SpotinstClient.create_emr(self, emr)
```

Create an EMR

__Arguments__

- __emr (EMR)__: EMR Object

__Returns__

`(Object)`: Elastigroup API response

<h1 id="spotinst_sdk.SpotinstClient.update_emr">update_emr</h1>

```python
SpotinstClient.update_emr(self, emr_id, emr)
```

Update an exsisting EMR

__Arguments__

- __emr_id (String)__: EMR id
- __emr (EMR)__: EMR Object

__Returns__

`(Object)`: Elastigroup API response

<h1 id="spotinst_sdk.SpotinstClient.get_all_emr">get_all_emr</h1>

```python
SpotinstClient.get_all_emr(self)
```

Get all EMR in account

__Returns__

`(Object)`: Elastigroup API response

<h1 id="spotinst_sdk.SpotinstClient.get_emr">get_emr</h1>

```python
SpotinstClient.get_emr(self, emr_id)
```

Get an exsisting EMR json

__Arguments__

- __emr_id (String)__: EMR id

__Returns__

`(Object)`: Elastigroup API response

<h1 id="spotinst_sdk.SpotinstClient.get_emr_instances">get_emr_instances</h1>

```python
SpotinstClient.get_emr_instances(self, emr_id)
```

Get instances from EMR

__Arguments__

- __emr_id (String)__: EMR id

__Returns__

`(Object)`: Elastigroup API response

<h1 id="spotinst_sdk.SpotinstClient.get_emr_cluster">get_emr_cluster</h1>

```python
SpotinstClient.get_emr_cluster(self, emr_id)
```

Get cluster from EMR

__Arguments__

- __emr_id (String)__: EMR id

__Returns__

`(Object)`: Elastigroup API response

<h1 id="spotinst_sdk.SpotinstClient.get_emr_cost">get_emr_cost</h1>

```python
SpotinstClient.get_emr_cost(self, emr_id, from_date=None, to_date=None)
```

Get cost from EMR

__Arguments__

- __emr_id (String)__: EMR id
- __from_date (String) (Optional)__: From Date
- __to_date (String) (Optional)__: to date

__Returns__

`(Object)`: Elastigroup API response

<h1 id="spotinst_sdk.SpotinstClient.delete_emr">delete_emr</h1>

```python
SpotinstClient.delete_emr(self, emr_id)
```

Delete an EMR

__Arguments__

- __emr_id (String)__: EMR id

__Returns__

`(Object)`: Elastigroup API response

<h1 id="spotinst_sdk.SpotinstClient.scale_up_emr">scale_up_emr</h1>

```python
SpotinstClient.scale_up_emr(self, emr_id, adjustment)
```

Scale up an EMR

__Arguments__

- __emr_id (String)__: EMR id
- __adjustment (Int)__: Ammount to scale

__Returns__

`(Object)`: Elastigroup API response

<h1 id="spotinst_sdk.SpotinstClient.scale_down_emr">scale_down_emr</h1>

```python
SpotinstClient.scale_down_emr(self, emr_id, adjustment)
```

Scale down an EMR

__Arguments__

- __emr_id (String)__: EMR id
- __adjustment (Int)__: Ammount to scale

__Returns__

`(Object)`: Elastigroup API response

