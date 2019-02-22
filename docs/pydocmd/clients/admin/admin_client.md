<h1 id="spotinst_sdk.clients.admin.AdminClient">AdminClient</h1>

```python
AdminClient(self, session=None, print_output=True, log_level=None, user_agent=None)
```

<h2 id="spotinst_sdk.clients.admin.AdminClient.create_organization">create_organization</h2>

```python
AdminClient.create_organization(self, org_name)
```

Create an organization

__Arguments__

- __org_name (String)__: Orgnanization name

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.admin.AdminClient.delete_organization">delete_organization</h2>

```python
AdminClient.delete_organization(self, org_id)
```

delete organization

__Arguments__

- __org_id (String)__: Organization Id

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.admin.AdminClient.set_cloud_credentials">set_cloud_credentials</h2>

```python
AdminClient.set_cloud_credentials(self, iam_role, external_id)
```

set cloud credentials

__Arguments__

- __iam_role (String)__: IAM Role
- __external_id (String)__: External ID

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.admin.AdminClient.create_account">create_account</h2>

```python
AdminClient.create_account(self, account_name)
```

create an account

__Arguments__

- __account_name (String)__: Account Name

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.admin.AdminClient.get_accounts">get_accounts</h2>

```python
AdminClient.get_accounts(self)
```

get accounts in organization

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.admin.AdminClient.delete_account">delete_account</h2>

```python
AdminClient.delete_account(self, account_name)
```

delete account

__Arguments__

- __account_name (String)__: Account Name

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.admin.AdminClient.create_user">create_user</h2>

```python
AdminClient.create_user(self, first_name, last_name, email, password, role)
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

<h2 id="spotinst_sdk.clients.admin.AdminClient.add_exsisting_user">add_exsisting_user</h2>

```python
AdminClient.add_exsisting_user(self, user_email, role)
```

Add exsisting user

__Arguments__

- __user_email (String)__: User email
- __role (String)__: User role

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.admin.AdminClient.update_user_role">update_user_role</h2>

```python
AdminClient.update_user_role(self, user_email, role)
```

Update exsisting user

__Arguments__

- __user_email (String)__: User email
- __role (String)__: User role

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.admin.AdminClient.detach_user">detach_user</h2>

```python
AdminClient.detach_user(self, user_email)
```

Delete exsisting user

__Arguments__

- __user_email (String)__: User email

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.admin.AdminClient.get_user">get_user</h2>

```python
AdminClient.get_user(self, user_email)
```

Get user

__Arguments__

- __user_email (String)__: User email

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk.clients.admin.AdminClient.assign_user_to_account">assign_user_to_account</h2>

```python
AdminClient.assign_user_to_account(self, mappings)
```

Assign user to account

__Arguments__

- __mappings (List)__: List of UserMapping Objects

__Returns__

`(Object)`: Spotinst API response

