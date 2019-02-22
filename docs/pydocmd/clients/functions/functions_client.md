<h1 id="spotinst_sdk.clients.functions.FunctionsClient">FunctionsClient</h1>

```python
FunctionsClient(self, session=None, print_output=True, log_level=None, user_agent=None)
```

<h2 id="spotinst_sdk.clients.functions.FunctionsClient.create_application">create_application</h2>

```python
FunctionsClient.create_application(self, app)
```

Create Spotinst Functions Application

__Arguments__

- __app (ApplicationCreate)__: ApplicationCreate Object
__Returns__

`(Object)`: Functions API response

<h2 id="spotinst_sdk.clients.functions.FunctionsClient.create_environment">create_environment</h2>

```python
FunctionsClient.create_environment(self, env)
```

Create Spotinst Functions Environment

__Arguments__

- __env (EnvironmentCreate)__: EnvironmentCreate Object
__Returns__

`(Object)`: Functions API response

<h2 id="spotinst_sdk.clients.functions.FunctionsClient.create_function">create_function</h2>

```python
FunctionsClient.create_function(self, fx)
```

Create Spotinst Functions

__Arguments__

- __fx (FunctionCreate)__: FunctionCreate Object
__Returns__

`(Object)`: Functions API response

