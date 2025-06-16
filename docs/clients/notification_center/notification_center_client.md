<h1 id="spotinst_sdk2.clients.notification_center.NotificationCenterClient">NotificationCenterClient</h1>

```python
NotificationCenterClient(self,
                         session=None,
                         print_output=True,
                         log_level=None,
                         user_agent=None,
                         timeout=None)
```

<h2 id="spotinst_sdk2.clients.notification_center.NotificationCenterClient.get_account_resources">get_account_resources</h2>

```python
NotificationCenterClient.get_account_resources()
```

get the list of resources associated with an account

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.notification_center.NotificationCenterClient.get_aggregated_events">get_aggregated_events</h2>

```python
NotificationCenterClient.get_aggregated_events()
```

get the list of events assciated with an account

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.notification_center.NotificationCenterClient.get_all_notification_policies">get_all_notification_policies</h2>

```python
NotificationCenterClient.get_all_notification_policies()
```

get the list of all notification policies

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.notification_center.NotificationCenterClient.get_specific_notification_policy">get_specific_notification_policy</h2>

```python
NotificationCenterClient.get_specific_notification_policy(
  policy_id: str)
```

get specific notification policy

__Arguments__

- __policy_id__: str

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.notification_center.NotificationCenterClient.create_notification_policy">create_notification_policy</h2>

```python
NotificationCenterClient.create_notification_policy(policy: Policy)
```

create notification policy

__Arguments__

- __policy (Policy)__: Policy object

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.notification_center.NotificationCenterClient.update_notification_policy">update_notification_policy</h2>

```python
NotificationCenterClient.update_notification_policy(
  policy_id: str, policy: Policy)
```

update notification policy

__Arguments__

- __policy_id __: str
- __policy (Policy)__: Policy object

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.notification_center.NotificationCenterClient.delete_notification_policy">delete_notification_policy</h2>

```python
NotificationCenterClient.delete_notification_policy(policy_id: str)
```

delete notification policy

__Arguments__

- __policy_id (String)__: Policy Id

__Returns__

`(Object)`: Spotinst API response

