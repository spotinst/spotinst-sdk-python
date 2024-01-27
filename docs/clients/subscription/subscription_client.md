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

__Arguments__

- __subscription (Subscription)__: Subscription Object

__Returns__

`(Object)`: Subscription API response

<h2 id="spotinst_sdk2.clients.subscription.SubscriptionClient.update_event_subscription">update_event_subscription</h2>

```python
SubscriptionClient.update_event_subscription(subscription_id,
                                             subscription)
```

Update an existing event subscription

__Arguments__

- __subscription_id (String)__: Subscription id
- __subscription (Subscription)__: Subscription Object

__Returns__

`(Object)`: Subscription API response

<h2 id="spotinst_sdk2.clients.subscription.SubscriptionClient.get_all_event_subscription">get_all_event_subscription</h2>

```python
SubscriptionClient.get_all_event_subscription()
```

Get all Subscription in account

__Returns__

`(Object)`: Subscription API response

<h2 id="spotinst_sdk2.clients.subscription.SubscriptionClient.get_event_subscription">get_event_subscription</h2>

```python
SubscriptionClient.get_event_subscription(subscription_id)
```

Get an existing event subscription json

__Arguments__

- __subscription_id (String)__: Subscription id

__Returns__

`(Object)`: Subscription API response

<h2 id="spotinst_sdk2.clients.subscription.SubscriptionClient.delete_event_subscription">delete_event_subscription</h2>

```python
SubscriptionClient.delete_event_subscription(subscription_id)
```

Delete an event subscription

__Arguments__

- __subscription_id (String)__: Subscription id

__Returns__

`(Object)`: subscription response

