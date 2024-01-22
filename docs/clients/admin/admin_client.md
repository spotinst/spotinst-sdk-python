<h1 id="spotinst_sdk2.clients.admin.AdminClient">AdminClient</h1>

```python
AdminClient(self,
            session=None,
            print_output=True,
            log_level=None,
            user_agent=None,
            timeout=None)
```

<h2 id="spotinst_sdk2.clients.admin.AdminClient.create_organization">create_organization</h2>

```python
AdminClient.create_organization(org_name)
```

Create an organization

__Arguments__

- __org_name (String)__: Orgnanization name

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.admin.AdminClient.delete_organization">delete_organization</h2>

```python
AdminClient.delete_organization(org_id)
```

delete organization

__Arguments__

- __org_id (String)__: Organization Id

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.admin.AdminClient.create_aws_external_id">create_aws_external_id</h2>

```python
AdminClient.create_aws_external_id()
```

Important note: This is deprecated, please use setup_aws client instead(SetupAWSClient#create_external_id)

Create aws account external id.
You should use the external id when creating your AWS role for your spot account

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.admin.AdminClient.set_cloud_credentials">set_cloud_credentials</h2>

```python
AdminClient.set_cloud_credentials(iam_role, external_id=None)
```

Important note: This is deprecated, please use setup_aws client instead(SetupAWSClient#set_credentials)

set cloud credentials
Please create external id using spot api (see [`AdminClient.create_aws_external_id`](#spotinst_sdk2.clients.admin.AdminClient.set_cloud_credentials.AdminClient.create_aws_external_id))
and use it when creating the AWS role

__Arguments__

- __iam_role (String)__: IAM Role
- __external_id (String) (Optional)__: External ID

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.admin.AdminClient.create_account">create_account</h2>

```python
AdminClient.create_account(account_name)
```

create an account

__Arguments__

- __account_name (String)__: Account Name

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.admin.AdminClient.get_accounts">get_accounts</h2>

```python
AdminClient.get_accounts()
```

get accounts in organization

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.admin.AdminClient.delete_account">delete_account</h2>

```python
AdminClient.delete_account(account_name)
```

delete account

__Arguments__

- __account_name (String)__: Account Name

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.admin.AdminClient.create_user">create_user</h2>

```python
AdminClient.create_user(first_name, last_name, email, password, role)
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

<h2 id="spotinst_sdk2.clients.admin.AdminClient.add_existing_user">add_existing_user</h2>

```python
AdminClient.add_existing_user(user_email, role)
```

Add existing user

__Arguments__

- __user_email (String)__: User email
- __role (String)__: User role

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.admin.AdminClient.update_user_role">update_user_role</h2>

```python
AdminClient.update_user_role(user_email, role)
```

Update existing user

__Arguments__

- __user_email (String)__: User email
- __role (String)__: User role

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.admin.AdminClient.detach_user">detach_user</h2>

```python
AdminClient.detach_user(user_email)
```

Delete existing user

__Arguments__

- __user_email (String)__: User email

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.admin.AdminClient.get_user">get_user</h2>

```python
AdminClient.get_user(user_email)
```

Get user

__Arguments__

- __user_email (String)__: User email

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.admin.AdminClient.assign_user_to_account">assign_user_to_account</h2>

```python
AdminClient.assign_user_to_account(mappings)
```

Assign user to account

__Arguments__

- __mappings (List)__: List of UserMapping Objects

__Returns__

`(Object)`: Spotinst API response
