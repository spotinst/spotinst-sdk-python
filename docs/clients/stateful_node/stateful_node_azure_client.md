<h1 id="spotinst_sdk2.clients.stateful_node.StatefulNodeAzureClient">StatefulNodeAzureClient</h1>

```python
StatefulNodeAzureClient(self,
                        session=None,
                        print_output=True,
                        log_level=None,
                        user_agent=None,
                        timeout=None)
```

<h2 id="spotinst_sdk2.clients.stateful_node.StatefulNodeAzureClient.ENTITY_NAME">ENTITY_NAME</h2>


<h2 id="spotinst_sdk2.clients.stateful_node.StatefulNodeAzureClient.create_stateful_node">create_stateful_node</h2>

```python
StatefulNodeAzureClient.create_stateful_node(node: StatefulNode)
```

Create a New Stateful Node

__Arguments__

- __node (StatefulNode)__: StatefulNode Object

__Returns__

`(Object)`: StatefulNode API response

<h2 id="spotinst_sdk2.clients.stateful_node.StatefulNodeAzureClient.update_stateful_node">update_stateful_node</h2>

```python
StatefulNodeAzureClient.update_stateful_node(node_update: StatefulNode,
                                             node_id: str)
```

Update a Stateful Node

__Arguments__

- __node_id (String)__: Stateful Node  ID
- __node_update (StatefulNode)__: StatefulNode Object

__Returns__

`(Object)`: StatefulNode API response

<h2 id="spotinst_sdk2.clients.stateful_node.StatefulNodeAzureClient.delete_stateful_node">delete_stateful_node</h2>

```python
StatefulNodeAzureClient.delete_stateful_node(
  node_id: str, deallocation_config: DeallocationConfig)
```

Delete a Stateful Node

__Arguments__

- __node_id (String)__: Stateful Node ID
- __deallocation_config (DeallocationConfig)__: DeallocationConfig object

__Returns__

`(Object)`: StatefulNode API response

<h2 id="spotinst_sdk2.clients.stateful_node.StatefulNodeAzureClient.get_stateful_node">get_stateful_node</h2>

```python
StatefulNodeAzureClient.get_stateful_node(node_id: str)
```

Get a Stateful Node

__Arguments__

- __node_id (String)__: Stateful Node ID

__Returns__

`(Object)`: Stateful Node API response

<h2 id="spotinst_sdk2.clients.stateful_node.StatefulNodeAzureClient.get_all_stateful_nodes">get_all_stateful_nodes</h2>

```python
StatefulNodeAzureClient.get_all_stateful_nodes()
```

Get all Stateful Nodes

__Returns__

`(List)`: List of Stateful Nodes API response

<h2 id="spotinst_sdk2.clients.stateful_node.StatefulNodeAzureClient.get_stateful_node_resources">get_stateful_node_resources</h2>

```python
StatefulNodeAzureClient.get_stateful_node_resources(node_id: str)
```

Get the node's attached resources (storage and network interfaces)

__Arguments__

- __node_id (String)__: Stateful Node ID

__Returns__

`(Object)`: Stateful Node API response

<h2 id="spotinst_sdk2.clients.stateful_node.StatefulNodeAzureClient.get_stateful_node_status">get_stateful_node_status</h2>

```python
StatefulNodeAzureClient.get_stateful_node_status(node_id: str)
```

Get the status of a specific stateful node.

__Arguments__

- __node_id (String)__: Stateful Node ID

__Returns__

`(Object)`: Stateful Node API response

<h2 id="spotinst_sdk2.clients.stateful_node.StatefulNodeAzureClient.get_all_stateful_node_statuses">get_all_stateful_node_statuses</h2>

```python
StatefulNodeAzureClient.get_all_stateful_node_statuses()
```

Get the statuses of all Stateful Nodes in a specific account.

__Returns__

`(Object)`: List of Stateful Node Statuses

<h2 id="spotinst_sdk2.clients.stateful_node.StatefulNodeAzureClient.update_stateful_node_state">update_stateful_node_state</h2>

```python
StatefulNodeAzureClient.update_stateful_node_state(
  node_id: str, state: str)
```

Update a Stateful Node State

__Arguments__

- __node_id (String)__: Stateful Node  ID
- __state (String)__: Desired state

__Returns__

`(Object)`: StatefulNode API response

<h2 id="spotinst_sdk2.clients.stateful_node.StatefulNodeAzureClient.get_stateful_node_from_azure_vm">get_stateful_node_from_azure_vm</h2>

```python
StatefulNodeAzureClient.get_stateful_node_from_azure_vm(
  resource_group_name: str, virtual_machine_name: str)
```

Get the configuration of a stateful node from a Azure VM for importing.

__Arguments__

- __resource_group_name (String)__: Resource Group of the VM to Import
- __virtual_machine_name (String)__: Virtual Machine to import

__Returns__

`(Object)`: Stateful Node API response

<h2 id="spotinst_sdk2.clients.stateful_node.StatefulNodeAzureClient.import_vm_to_stateful_node">import_vm_to_stateful_node</h2>

```python
StatefulNodeAzureClient.import_vm_to_stateful_node(
  import_vm_configuration: ImportVmConfiguration)
```

Import an Azure VM and create a Stateful Node by providing a node configuration.

__Arguments__

- __import_vm_configuration (StatefulNode)__: Configuration of VM to import

__Returns__

`(Object)`: StatefulNode API response

<h2 id="spotinst_sdk2.clients.stateful_node.StatefulNodeAzureClient.get_stateful_node_import_status">get_stateful_node_import_status</h2>

```python
StatefulNodeAzureClient.get_stateful_node_import_status(import_id)
```

Get the import process status of a Stateful Node.

__Arguments__

- __import_id (String)__: Import ID

__Returns__

`(Object) `: Stateful Node API response

<h2 id="spotinst_sdk2.clients.stateful_node.StatefulNodeAzureClient.attach_data_disk_to_stateful_node">attach_data_disk_to_stateful_node</h2>

```python
StatefulNodeAzureClient.attach_data_disk_to_stateful_node(
  node_id: str, data_disk_configuration: AttachDataDiskConfiguration)
```

Create a new data disk and attche it to the Stateful Node.

__Arguments__

- __node_id (String)__: Stateful Node  ID
- __data_disk_configuration (AttachDataDiskConfiguration)__: Configuration of Data Disk

__Returns__

`(Object)`: StatefulNode API response

<h2 id="spotinst_sdk2.clients.stateful_node.StatefulNodeAzureClient.detach_data_disk_from_stateful_node">detach_data_disk_from_stateful_node</h2>

```python
StatefulNodeAzureClient.detach_data_disk_from_stateful_node(
  node_id: str, data_disk_configuration: DetachDataDiskConfiguration)
```

Detach a data disk from a Stateful Node.

__Arguments__

- __node_id (String)__: Stateful Node  ID
- __data_disk_configuration (DetachDataDiskConfiguration)__: Configuration of Data Disk

__Returns__

`(Object)`: StatefulNode API response

<h2 id="spotinst_sdk2.clients.stateful_node.StatefulNodeAzureClient.get_stateful_node_logs">get_stateful_node_logs</h2>

```python
StatefulNodeAzureClient.get_stateful_node_logs(node_id,
                                               from_date,
                                               to_date,
                                               severity=None,
                                               resource_id=None,
                                               limit=None)
```

Get the logs of a Stateful Node according to severity and time period filter parameters.

__Arguments__

- __node_id (String)__: Stateful ID
- __to_date (String)__: On or Before this date
- __from_date (String)__: On or After this date
- __severity(String) (Optional)__: Log level severity
- __resource_id(String) (Optional)__: Filter log extracted entires related to a specific resource id
- __limit(String) (Optional)__: Maximum number of lines to extract in a response

__Returns__

`(Object)`: Stateful Node API response

