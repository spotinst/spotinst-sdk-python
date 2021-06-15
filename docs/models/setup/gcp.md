<h1 id="spotinst_sdk2.models.setup.gcp">spotinst_sdk2.models.setup.gcp</h1>


<h2 id="spotinst_sdk2.models.setup.gcp.GcpCredentials">GcpCredentials</h2>

```python
GcpCredentials(self, serviceAccount)
```

__Arguments__

- __serviceAccount__: ServiceAccount

<h2 id="spotinst_sdk2.models.setup.gcp.ServiceAccount">ServiceAccount</h2>

```python
ServiceAccount(self, type, project_id, private_key_id, private_key,
               client_email, client_id, auth_uri, token_uri,
               auth_provider_x509_cert_url, client_x509_cert_url)
```

__Arguments__

- __type__: str
- __project_id__: str
- __private_key_id__: str
- __private_key__: str
- __client_email__: str
- __client_id__: str
- __auth_uri__: str
- __token_uri__: str
- __auth_provider_x509_cert_url__: str
- __client_x509_cert_url__: str

<h2 id="spotinst_sdk2.models.setup.gcp.GcpSetCredentialsRequest">GcpSetCredentialsRequest</h2>

```python
GcpSetCredentialsRequest(self, gcp_credentials)
```

__Arguments__

- __gcp_credentials__: GcpCredentials

