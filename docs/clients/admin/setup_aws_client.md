<h1 id="spotinst_sdk2.clients.setup.SetupAWSClient">SetupAWSClient</h1>

```python
SetupAWSClient(self,
               session=None,
               print_output=True,
               log_level=None,
               user_agent=None,
               timeout=None)
```

<h2 id="spotinst_sdk2.clients.setup.SetupAWSClient.create_external_id">create_external_id</h2>

```python
SetupAWSClient.create_external_id()
```

Create aws account external id.
You should use the external id when creating your AWS role for your spot account

__Returns__

`(Object)`: Spotinst API response

<h2 id="spotinst_sdk2.clients.setup.SetupAWSClient.set_credentials">set_credentials</h2>

```python
SetupAWSClient.set_credentials(iam_role)
```

Set aws credentials
Please create external id using spot api (see [`AdminClient.create_aws_external_id`](#spotinst_sdk2.clients.setup.SetupAWSClient.set_credentials.AdminClient.create_aws_external_id))
and use it when creating the AWS role

__Arguments__

- __iam_role (String)__: IAM Role

__Returns__

`(Object)`: Spotinst API response

