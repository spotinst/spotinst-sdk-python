<h1 id="spotinst_sdk.SpotinstClient.create_event_subscription">create_event_subscription</h1>

```python
SpotinstClient.create_event_subscription(self, subscription)
```

Create an event subscription

__Arguments__

- __subscription (Subscription)__: Subscription Object

__Returns__

`(Object)`: Subscription API response

<h1 id="spotinst_sdk.SpotinstClient.update_event_subscription">update_event_subscription</h1>

```python
SpotinstClient.update_event_subscription(self, subscription_id, subscription)
```

Update an exsisting event subscription

__Arguments__

- __subscription_id (String)__: Subscription id
- __subscription (Subscription)__: Subscription Object

__Returns__

`(Object)`: Subscription API response

<h1 id="spotinst_sdk.SpotinstClient.get_all_event_subscription">get_all_event_subscription</h1>

```python
SpotinstClient.get_all_event_subscription(self)
```

Get all Subscription in account

__Returns__

`(Object)`: Subscription API response

<h1 id="spotinst_sdk.SpotinstClient.get_event_subscription">get_event_subscription</h1>

```python
SpotinstClient.get_event_subscription(self, subscription_id)
```

Get an exsisting event subscription json

__Arguments__

- __subscription_id (String)__: Subscription id

__Returns__

`(Object)`: Subscription API response

<h1 id="spotinst_sdk.SpotinstClient.delete_event_subscription">delete_event_subscription</h1>

```python
SpotinstClient.delete_event_subscription(self, subscription_id)
```

Delete an event subscription

__Arguments__

- __subscription_id (String)__: Subscription id

__Returns__

`(Object)`: subscription response

