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

**Arguments**

- **org_name (String)**: Orgnanization name

**Returns**

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.admin.AdminClient.delete_organization">delete_organization</h2>

```python
AdminClient.delete_organization(org_id)
```

delete organization

**Arguments**

- **org_id (String)**: Organization Id

**Returns**

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.admin.AdminClient.create_aws_external_id">create_aws_external_id</h2>

```python
AdminClient.create_aws_external_id()
```

Important note: This is deprecated, please use setup_aws client instead(SetupAWSClient#create_external_id)

Create aws account external id.
You should use the external id when creating your AWS role for your spot account

**Returns**

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.admin.AdminClient.set_cloud_credentials">set_cloud_credentials</h2>

```python
AdminClient.set_cloud_credentials(iam_role, external_id=None)
```

Important note: This is deprecated, please use setup_aws client instead(SetupAWSClient#set_credentials)

set cloud credentials
Please create external id using spot api (see [`AdminClient.create_aws_external_id`](#spotinst_sdk2.clients.admin.AdminClient.set_cloud_credentials.AdminClient.create_aws_external_id))
and use it when creating the AWS role

**Arguments**

- **iam_role (String)**: IAM Role
- **external_id (String) (Optional)**: External ID

**Returns**

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.admin.AdminClient.create_account">create_account</h2>

```python
AdminClient.create_account(account_name)
```

create an account

**Arguments**

- **account_name (String)**: Account Name

**Returns**

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.admin.AdminClient.get_accounts">get_accounts</h2>

```python
AdminClient.get_accounts()
```

get accounts in organization

**Returns**

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.admin.AdminClient.delete_account">delete_account</h2>

```python
AdminClient.delete_account(account_name)
```

delete account

**Arguments**

- **account_name (String)**: Account Name

**Returns**

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.admin.AdminClient.create_user">create_user</h2>

```python
AdminClient.create_user(first_name, last_name, email, password, role)
```

Create user

**Arguments**

- **first_name (String)**: Users first name
- **last_name (String)**: User last name
- **email (String)**: Eser email
- **password (String)**: User email
- **role (String)**: User role

**Returns**

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.admin.AdminClient.add_existing_user">add_existing_user</h2>

```python
AdminClient.add_existing_user(user_email, role)
```

Add existing user

**Arguments**

- **user_email (String)**: User email
- **role (String)**: User role

**Returns**

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.admin.AdminClient.update_user_role">update_user_role</h2>

```python
AdminClient.update_user_role(user_email, role)
```

Update existing user

**Arguments**

- **user_email (String)**: User email
- **role (String)**: User role

**Returns**

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.admin.AdminClient.detach_user">detach_user</h2>

```python
AdminClient.detach_user(user_email)
```

Delete existing user

**Arguments**

- **user_email (String)**: User email

**Returns**

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.admin.AdminClient.get_user">get_user</h2>

```python
AdminClient.get_user(user_email)
```

Get user

**Arguments**

- **user_email (String)**: User email

**Returns**

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.admin.AdminClient.assign_user_to_account">assign_user_to_account</h2>

```python
AdminClient.assign_user_to_account(mappings)
```

Assign user to account

**Arguments**

- **mappings (List)**: List of UserMapping Objects

**Returns**

`(Object)`: Spotinst API response
