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
Get account resources

__Returns__

`(Object)`: Spotinst API response


<h2 id="spotinst_sdk2.clients.notification_center.NotificationCenterClient.get_aggregated_events">get_aggregated_events</h2>

```python
NotificationCenterClient.get_aggregated_events()
```

Get aggregated events

__Returns__

`(Object)`: Spotinst API response


<h2 id="spotinst_sdk2.clients.notification_center.NotificationCenterClient.get_all_notification_policies">get_all_notification_policies</h2>

```python
NotificationCenterClient.get_all_notification_policies(account_id: str)
```

Get all notification policies

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.notification_center.NotificationCenterClient.get_specific_notification_policy">get_specific_notification_policy</h2>

```python
NotificationCenterClient.get_specific_notification_policy(policy_id: str)
```

Get specific notification policy

__Arguments__

- __policy_id (String)__: Policy ID

__Returns__

`(Object)`: Spotinst API response


<h2 id="spotinst_sdk2.clients.notification_center.NotificationCenterClient.create_notification_policy">create_notification_policy</h2>

```python
NotificationCenterClient.create_notification_policy(policy : Policy)
```

Create notification policy

__Arguments__

- __group (Policy)__: Policy Object

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.notification_center.NotificationCenterClient.delete_notification_policy">delete_notification_policy</h2>

```python
NotificationCenterClient.delete_notification_policy(policy : Policy)
```

Dlete notification policy

__Arguments__

- __policy_id (String)__: Policy ID

__Returns__

`(Object)`: Spotinst API response