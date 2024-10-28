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
AdminClient.create_organization(org_name: str)
```

Create an organization

__Arguments__

- __org_name (String)__: Orgnanization name

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.admin.AdminClient.delete_organization">delete_organization</h2>

```python
AdminClient.delete_organization(org_id: str)
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
AdminClient.set_cloud_credentials(iam_role: str,
                                  external_id: str = None)
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
AdminClient.create_account(account_name: str)
```

create an account

__Arguments__

- __account_name (String)__: Account Name

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.admin.AdminClient.update_account">update_account</h2>

```python
AdminClient.update_account(
  account_id: str,
  new_account_name: str,
  slack_notification_channels: typing.List[str] = None)
```

create an account

__Arguments__

- __account_id (String)__: Account Id
- __new_account_name (String)__: New Account Name
- __slack_notification_channels List(str)__: List of slack notification channels

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
AdminClient.delete_account(account_name: str)
```

delete account

__Arguments__

- __account_name (String)__: Account Name

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.admin.AdminClient.create_user">create_user</h2>

```python
AdminClient.create_user(first_name: str, last_name: str, email: str,
                        password: str, role: str)
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
AdminClient.detach_user(user_email: str)
```

Delete existing user

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

<h2 id="spotinst_sdk2.clients.admin.AdminClient.get_users">get_users</h2>

```python
AdminClient.get_users()
```

Retrieves all users from an organization.

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.admin.AdminClient.get_policies">get_policies</h2>

```python
AdminClient.get_policies()
```

Retrieves all policies from an organization.

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.admin.AdminClient.get_user_details">get_user_details</h2>

```python
AdminClient.get_user_details(user_id: str)
```

Retrieves an individual user details.

__Arguments__

- __user_id (String)__: User ID

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.admin.AdminClient.delete_user">delete_user</h2>

```python
AdminClient.delete_user(user_id: str)
```

Deletes a user (console or programmatic) from an organization.

__Arguments__

- __user_id (String)__: User ID

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.admin.AdminClient.update_user_to_user_group_mapping">update_user_to_user_group_mapping</h2>

```python
AdminClient.update_user_to_user_group_mapping(
  user_id: str, user_group_ids: typing.List[str])
```

Update the mapping of a given user to user groups

__Arguments__

- __user_id (String)__: Identifier of a user.
- __user_group_ids (List)__: A list of the user groups to register the given user to

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.admin.AdminClient.update_user_to_policy_mapping">update_user_to_policy_mapping</h2>

```python
AdminClient.update_user_to_policy_mapping(user_id: str, policies)
```

Update the mapping of a given user to policies

__Arguments__

- __user_id (String)__: Identifier of a user.
- __policies (List)__: A list of policies to register under the given user

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.admin.AdminClient.get_user">get_user</h2>

```python
AdminClient.get_user(user_email: str)
```

Get user's account mapping.

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.admin.AdminClient.create_programmatic_user">create_programmatic_user</h2>

```python
AdminClient.create_programmatic_user(name: str,
                                     description: str,
                                     accounts=None,
                                     policies=None)
```

Create a programmatic user

__Arguments__

- __name (String)__: Name of the programmatic user
- __description (String)__: Brief description of the user
- __accounts (List)__: All the accounts the programmatic user will have access to
- __policies (List)__: All the policies the programmatic user will have access to

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.admin.AdminClient.get_access_policy_actions">get_access_policy_actions</h2>

```python
AdminClient.get_access_policy_actions(category: str = None,
                                      name: str = None,
                                      resource_pattern: str = None,
                                      scope: str = None,
                                      service: str = None)
```

Get actions for access policies.

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.admin.AdminClient.create_access_policy">create_access_policy</h2>

```python
AdminClient.create_access_policy(policy: AccessPolicy)
```

Create an access policy

__Arguments__

- __policy (AccessPolicy)__: AccessPolicy Object

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.admin.AdminClient.update_access_policy">update_access_policy</h2>

```python
AdminClient.update_access_policy(policy_id: str, policy_name: str)
```

Updates an access policy settings.

__Arguments__

- __policy_id (String)__: Policy ID
- __policy_name (String)__: Name to be set for the policy

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.admin.AdminClient.delete_access_policy">delete_access_policy</h2>

```python
AdminClient.delete_access_policy(policy_id: str)
```

Deletes an access policy.

__Arguments__

- __policy_id (String)__: Policy ID

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.admin.AdminClient.get_user_groups">get_user_groups</h2>

```python
AdminClient.get_user_groups()
```

Retrieves all user-groups from an organization.

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.admin.AdminClient.create_user_group">create_user_group</h2>

```python
AdminClient.create_user_group(user_group: UserGroup)
```

Create a new User Group

__Arguments__

- __group (UserGroup)__: UserGroup Object

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.admin.AdminClient.get_user_group_details">get_user_group_details</h2>

```python
AdminClient.get_user_group_details(user_group_id: str)
```

Get the details of a user Group

__Arguments__

- __user_group_id (String)__: User Group ID

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.admin.AdminClient.delete_user_group">delete_user_group</h2>

```python
AdminClient.delete_user_group(user_group_id: str)
```

Delete a user group.

__Arguments__

- __user_group_id (String)__: User Group ID

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.admin.AdminClient.update_user_group_to_user_mapping">update_user_group_to_user_mapping</h2>

```python
AdminClient.update_user_group_to_user_mapping(
  user_group_id: str, user_ids: typing.List[str])
```

Update the mapping of a given user group to users

__Arguments__

- __user_group_id (String)__: Identifier of a usergroup.
- __user_ids (List)__: The users to register under the given user group (should be existing users only)

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.admin.AdminClient.update_user_group_to_policy_mapping">update_user_group_to_policy_mapping</h2>

```python
AdminClient.update_user_group_to_policy_mapping(user_group_id: str,
                                                policies)
```

Update the mapping of a given user group to policies

__Arguments__

- __user_group_id (String)__: Identifier of a user group.
- __policies (List)__: The policies to register under the given user group (should be existing policies only)

__Returns__

`(Object)`: Spotinst API response

