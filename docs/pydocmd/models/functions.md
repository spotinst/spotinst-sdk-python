<h1 id="spotinst_sdk2.models.functions">spotinst_sdk2.models.functions</h1>


<h2 id="spotinst_sdk2.models.functions.Application">Application</h2>

```python
Application(self, name)
```

__Arguments__

- __name__: str

<h2 id="spotinst_sdk2.models.functions.Environment">Environment</h2>

```python
Environment(self, name, application_id, providers='d3043820717d74d9a17694c176d39733', locations='d3043820717d74d9a17694c176d39733')
```

__Arguments__

- __name__: str
- __application_id__: str
- __providers__: List[str]
- __locations__: List[str]

<h2 id="spotinst_sdk2.models.functions.Function">Function</h2>

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

