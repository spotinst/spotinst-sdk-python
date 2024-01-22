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

**Arguments**

- **emr (EMR)**: EMR Object

**Returns**

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.mrscaler.MrScalerAwsClient.update_emr">update_emr</h2>

```python
MrScalerAwsClient.update_emr(emr_id, emr)
```

Update an existing EMR

**Arguments**

- **emr_id (String)**: EMR id
- **emr (EMR)**: EMR Object

**Returns**

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.mrscaler.MrScalerAwsClient.get_all_emr">get_all_emr</h2>

```python
MrScalerAwsClient.get_all_emr()
```

Get all EMR in account

**Returns**

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.mrscaler.MrScalerAwsClient.get_emr">get_emr</h2>

```python
MrScalerAwsClient.get_emr(emr_id)
```

Get an existing EMR json

**Arguments**

- **emr_id (String)**: EMR id

**Returns**

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.mrscaler.MrScalerAwsClient.get_emr_instances">get_emr_instances</h2>

```python
MrScalerAwsClient.get_emr_instances(emr_id)
```

Get instances from EMR

**Arguments**

- **emr_id (String)**: EMR id

**Returns**

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.mrscaler.MrScalerAwsClient.get_emr_cluster">get_emr_cluster</h2>

```python
MrScalerAwsClient.get_emr_cluster(emr_id)
```

Get cluster from EMR

**Arguments**

- **emr_id (String)**: EMR id

**Returns**

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.mrscaler.MrScalerAwsClient.get_emr_cost">get_emr_cost</h2>

```python
MrScalerAwsClient.get_emr_cost(emr_id, from_date=None, to_date=None)
```

Get cost from EMR

**Arguments**

- **emr_id (String)**: EMR id
- **from_date (String) (Optional)**: From Date
- **to_date (String) (Optional)**: to date

**Returns**

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.mrscaler.MrScalerAwsClient.delete_emr">delete_emr</h2>

```python
MrScalerAwsClient.delete_emr(emr_id)
```

Delete an EMR

**Arguments**

- **emr_id (String)**: EMR id

**Returns**

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.mrscaler.MrScalerAwsClient.scale_up_emr">scale_up_emr</h2>

```python
MrScalerAwsClient.scale_up_emr(emr_id, adjustment)
```

Scale up an EMR

**Arguments**

- **emr_id (String)**: EMR id
- **adjustment (Int)**: Ammount to scale

**Returns**

`(Object)`: Elastigroup API response

<h2 id="spotinst_sdk2.clients.mrscaler.MrScalerAwsClient.scale_down_emr">scale_down_emr</h2>

```python
MrScalerAwsClient.scale_down_emr(emr_id, adjustment)
```

Scale down an EMR

**Arguments**

- **emr_id (String)**: EMR id
- **adjustment (Int)**: Ammount to scale

**Returns**

`(Object)`: Elastigroup API response
