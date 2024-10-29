<h1 id="spotinst_sdk2.models.admin.user_mapping">spotinst_sdk2.models.admin.user_mapping</h1>


<h2 id="spotinst_sdk2.models.admin.user_mapping.UserMapping">UserMapping</h2>

```python
UserMapping(self,
            user_email='d3043820717d74d9a17694c176d39733',
            account_id='d3043820717d74d9a17694c176d39733',
            role='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __user_email__: str
- __account_id__: str
- __role__: str

<h1 id="spotinst_sdk2.models.admin.organization">spotinst_sdk2.models.admin.organization</h1>


<h2 id="spotinst_sdk2.models.admin.organization.Statement">Statement</h2>

```python
Statement(self,
          effect: str = 'd3043820717d74d9a17694c176d39733',
          actions: typing.List[str] = None,
          resources: typing.List[str] = None)
```

__Arguments__

- __effect__: str
- __actions__: List[str]
- __resources__: List[str]

<h2 id="spotinst_sdk2.models.admin.organization.PolicyContent">PolicyContent</h2>

```python
PolicyContent(
    self,
    statements:
    typing.List[spotinst_sdk2.models.admin.organization.Statement] = 'd3043820717d74d9a17694c176d39733'
)
```

__Arguments__

- __statements__: List[Statement]

<h2 id="spotinst_sdk2.models.admin.organization.AccessPolicy">AccessPolicy</h2>

```python
AccessPolicy(
  self,
  description: str = 'd3043820717d74d9a17694c176d39733',
  name: str = 'd3043820717d74d9a17694c176d39733',
  type: str = 'd3043820717d74d9a17694c176d39733',
  policy_content: PolicyContent = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __description__: str
- __name__: str
- __type__: str
- __policy_content__: PolicyContent

<h2 id="spotinst_sdk2.models.admin.organization.PolicyMapping">PolicyMapping</h2>

```python
PolicyMapping(
  self,
  policy_id: str = 'd3043820717d74d9a17694c176d39733',
  account_ids: typing.List[str] = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __account_ids__: List[str]
- __policy_id__: str

<h2 id="spotinst_sdk2.models.admin.organization.UserGroup">UserGroup</h2>

```python
UserGroup(
  self,
  description: str = 'd3043820717d74d9a17694c176d39733',
  name: str = 'd3043820717d74d9a17694c176d39733',
  policies:
    typing.List[spotinst_sdk2.models.admin.organization.PolicyMapping] = 'd3043820717d74d9a17694c176d39733',
  user_ids: typing.List[str] = 'd3043820717d74d9a17694c176d39733')
```

__Arguments__

- __description__: str
- __name__: str
- __policies__: List[PolicyMapping]
- __user_ids__: List[str]

