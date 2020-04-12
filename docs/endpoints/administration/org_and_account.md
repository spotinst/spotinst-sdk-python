<h1 id="spotinst_sdk.SpotinstClient.create_organization">create_organization</h1>

```python
SpotinstClient.create_organization(org_name)
```

Create an organization

__Arguments__

- __org_name (String)__: Orgnanization name

__Returns__

`(Object)`: Spotinst API response

<h1 id="spotinst_sdk.SpotinstClient.delete_organization">delete_organization</h1>

```python
SpotinstClient.delete_organization(org_id)
```

delete organization

__Arguments__

- __org_id (String)__: Organization Id

__Returns__

`(Object)`: Spotinst API response

<h1 id="spotinst_sdk.SpotinstClient.set_cloud_credentials">set_cloud_credentials</h1>

```python
SpotinstClient.set_cloud_credentials(iam_role, external_id)
```

set cloud credentials

__Arguments__

- __iam_role (String)__: IAM Role
- __external_id (String)__: External ID

__Returns__

`(Object)`: Spotinst API response

<h1 id="spotinst_sdk.SpotinstClient.create_account">create_account</h1>

```python
SpotinstClient.create_account(account_name)
```

create an account

__Arguments__

- __account_name (String)__: Account Name

__Returns__

`(Object)`: Spotinst API response

<h1 id="spotinst_sdk.SpotinstClient.get_accounts">get_accounts</h1>

```python
SpotinstClient.get_accounts()
```

get accounts in organization

__Returns__

`(Object)`: Spotinst API response

<h1 id="spotinst_sdk.SpotinstClient.delete_account">delete_account</h1>

```python
SpotinstClient.delete_account(account_name)
```

delete account

__Arguments__

- __account_name (String)__: Account Name

__Returns__

`(Object)`: Spotinst API response

<h1 id="spotinst_sdk.SpotinstClient.create_user">create_user</h1>

```python
SpotinstClient.create_user(first_name, last_name, email, password, role)
```

Create user

__Arguments__

- __first_name (String)__: Users first name
- __last_name (String)__: User last name
- __email (String)__: Eser email
- __password (String)__: User email
- __role (String)__: User role


__Returns__

`(Object)`: Spotinst API response

<h1 id="spotinst_sdk.SpotinstClient.add_exsisting_user">add_exsisting_user</h1>

```python
SpotinstClient.add_exsisting_user(user_email, role)
```

Add exsisting user

__Arguments__

- __user_email (String)__: User email
- __role (String)__: User role

__Returns__

`(Object)`: Spotinst API response

<h1 id="spotinst_sdk.SpotinstClient.update_user_role">update_user_role</h1>

```python
SpotinstClient.update_user_role(user_email, role)
```

Update exsisting user

__Arguments__

- __user_email (String)__: User email
- __role (String)__: User role

__Returns__

`(Object)`: Spotinst API response

<h1 id="spotinst_sdk.SpotinstClient.detach_user">detach_user</h1>

```python
SpotinstClient.detach_user(user_email)
```

Delete exsisting user

__Arguments__

- __user_email (String)__: User email

__Returns__

`(Object)`: Spotinst API response

<h1 id="spotinst_sdk.SpotinstClient.get_user">get_user</h1>

```python
SpotinstClient.get_user(user_email)
```

Get user

__Arguments__

- __user_email (String)__: User email

__Returns__

`(Object)`: Spotinst API response

<h1 id="spotinst_sdk.SpotinstClient.assign_user_to_account">assign_user_to_account</h1>

```python
SpotinstClient.assign_user_to_account(mappings)
```

Assign user to account

__Arguments__

- __mappings (List)__: List of UserMapping Objects

__Returns__

`(Object)`: Spotinst API response

