<h1 id="spotinst_sdk2.clients.subscription.SubscriptionClient">SubscriptionClient</h1>

```python
SubscriptionClient(self,
                   session=None,
                   print_output=True,
                   log_level=None,
                   user_agent=None,
                   timeout=None)
```

<h2 id="spotinst_sdk2.clients.subscription.SubscriptionClient.create_event_subscription">create_event_subscription</h2>

```python
SubscriptionClient.create_event_subscription(subscription)
```

Create an event subscription

**Arguments**

- **subscription (Subscription)**: Subscription Object

**Returns**

`(Object)`: Subscription API response

<h2 id="spotinst_sdk2.clients.subscription.SubscriptionClient.update_event_subscription">update_event_subscription</h2>

```python
SubscriptionClient.update_event_subscription(subscription_id,
                                             subscription)
```

Update an existing event subscription

**Arguments**

- **subscription_id (String)**: Subscription id
- **subscription (Subscription)**: Subscription Object

**Returns**

`(Object)`: Subscription API response

<h2 id="spotinst_sdk2.clients.subscription.SubscriptionClient.get_all_event_subscription">get_all_event_subscription</h2>

```python
SubscriptionClient.get_all_event_subscription()
```

Get all Subscription in account

**Returns**

`(Object)`: Subscription API response

<h2 id="spotinst_sdk2.clients.subscription.SubscriptionClient.get_event_subscription">get_event_subscription</h2>

```python
SubscriptionClient.get_event_subscription(subscription_id)
```

Get an existing event subscription json

**Arguments**

- **subscription_id (String)**: Subscription id

**Returns**

`(Object)`: Subscription API response

<h2 id="spotinst_sdk2.clients.subscription.SubscriptionClient.delete_event_subscription">delete_event_subscription</h2>

```python
SubscriptionClient.delete_event_subscription(subscription_id)
```

Delete an event subscription

**Arguments**

- **subscription_id (String)**: Subscription id

**Returns**

`(Object)`: subscription response
