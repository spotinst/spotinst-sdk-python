<h1 id="spotinst_sdk.spotinst_functions.Application">Application</h1>

```python
Application(self, name)
```

__Arguments__

- __name__: str

<h1 id="spotinst_sdk.spotinst_functions.Environment">Environment</h1>

```python
Environment(self, name, application_id, providers='d3043820717d74d9a17694c176d39733', locations='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __application_id__: str
- __providers__: List[str]
- __locations__: List[str]

<h1 id="spotinst_sdk.spotinst_functions.Function">Function</h1>

```python
Function(self, name, environment_id, directory, handler, runtime, memory, timeout)
```

__Arguments__

- __name__: str
- __environment_id__: str
- __directory__: str
- __runtime__: int
- __memory__: int
- __timeout__: int

