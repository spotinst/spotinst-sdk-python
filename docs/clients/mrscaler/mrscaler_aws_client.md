<h1 id="spotinst_sdk2.clients.mrscaler.MrScalerAwsClient">MrScalerAwsClient</h1>

```python
MrScalerAwsClient(self,
                  session=None,
                  print_output=True,
                  log_level=None,
                  user_agent=None,
                  timeout=None)
```

<h2 id="spotinst_sdk2.clients.mrscaler.MrScalerAwsClient.create_emr">create_emr</h2>

```python
MrScalerAwsClient.create_emr(emr)
```

Create an EMR

__Arguments__

- __emr (EMR)__: EMR Object

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.mrscaler.MrScalerAwsClient.update_emr">update_emr</h2>

```python
MrScalerAwsClient.update_emr(emr_id, emr)
```

Update an exsisting EMR

__Arguments__

- __emr_id (String)__: EMR id
- __emr (EMR)__: EMR Object

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.mrscaler.MrScalerAwsClient.get_all_emr">get_all_emr</h2>

```python
MrScalerAwsClient.get_all_emr()
```

Get all EMR in account

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.mrscaler.MrScalerAwsClient.get_emr">get_emr</h2>

```python
MrScalerAwsClient.get_emr(emr_id)
```

Get an exsisting EMR json

__Arguments__

- __emr_id (String)__: EMR id

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.mrscaler.MrScalerAwsClient.get_emr_instances">get_emr_instances</h2>

```python
MrScalerAwsClient.get_emr_instances(emr_id)
```

Get instances from EMR

__Arguments__

- __emr_id (String)__: EMR id

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.mrscaler.MrScalerAwsClient.get_emr_cluster">get_emr_cluster</h2>

```python
MrScalerAwsClient.get_emr_cluster(emr_id)
```

Get cluster from EMR

__Arguments__

- __emr_id (String)__: EMR id

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.mrscaler.MrScalerAwsClient.get_emr_cost">get_emr_cost</h2>

```python
MrScalerAwsClient.get_emr_cost(emr_id, from_date=None, to_date=None)
```

Get cost from EMR

__Arguments__

- __emr_id (String)__: EMR id
- __from_date (String) (Optional)__: From Date
- __to_date (String) (Optional)__: to date

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.mrscaler.MrScalerAwsClient.delete_emr">delete_emr</h2>

```python
MrScalerAwsClient.delete_emr(emr_id)
```

Delete an EMR

__Arguments__

- __emr_id (String)__: EMR id

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.mrscaler.MrScalerAwsClient.scale_up_emr">scale_up_emr</h2>

```python
MrScalerAwsClient.scale_up_emr(emr_id, adjustment)
```

Scale up an EMR

__Arguments__

- __emr_id (String)__: EMR id
- __adjustment (Int)__: Ammount to scale

__Returns__

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.mrscaler.MrScalerAwsClient.scale_down_emr">scale_down_emr</h2>

```python
MrScalerAwsClient.scale_down_emr(emr_id, adjustment)
```

Scale down an EMR

__Arguments__

- __emr_id (String)__: EMR id
- __adjustment (Int)__: Ammount to scale

__Returns__

`(Object)`: Elastigroup API response

