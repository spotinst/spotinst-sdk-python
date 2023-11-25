import json

from spotinst_sdk2.client import Client

import spotinst_sdk2.models.stateful_node as azure_stateful_node

none = "d3043820717d74d9a17694c176d39733"


class StatefulNodeAzureClient(Client):
    __base_stateful_node_url = "/azure/compute/statefulNode"
    ENTITY_NAME = 'statefulNode'

    def create_stateful_node(self, node: azure_stateful_node.StatefulNode):
        """
        Create a New Stateful Node

        # Arguments
        node (StatefulNode): StatefulNode Object

        # Returns
        (Object): StatefulNode API response
        """
        request = azure_stateful_node.CreateStatefulNodeRequest(node)

        excluded_node_dict = self.exclude_missing(json.loads(request.toJSON()))

        formatted_node_dict = self.convert_json(
            excluded_node_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_node_dict)

        response = self.send_post(
            body=body_json,
            url=self.__base_stateful_node_url,
            entity_name=self.ENTITY_NAME)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def update_stateful_node(self, node_update: azure_stateful_node.StatefulNode, node_id: str):
        """
        Update a Stateful Node

        # Arguments
        node_id (String): Stateful Node  ID
        node_update (StatefulNode): StatefulNode Object

        # Returns
        (Object): StatefulNode API response
        """
        request = azure_stateful_node.UpdateStatefulNodeRequest(node_update)

        excluded_node_update_dict = self.exclude_missing(
            json.loads(request.toJSON()))

        formatted_node_update_dict = self.convert_json(
            excluded_node_update_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_node_update_dict)

        response = self.send_put(
            body=body_json,
            url=self.__base_stateful_node_url + "/" + node_id,
            entity_name=self.ENTITY_NAME)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def delete_stateful_node(self, node_id: str, deallocation_config: azure_stateful_node.DeallocationConfig):
        """
        Delete a Stateful Node

        # Arguments
        node_id (String): Stateful Node ID
        deallocation_config (DeallocationConfig): DeallocationConfig object

        # Returns
        (Object): StatefulNode API response
        """
        request = azure_stateful_node.DeleteStatefulNodeRequest(
            deallocation_config)

        excluded_node_delete_dict = self.exclude_missing(
            json.loads(request.toJSON()))

        formatted_node_delete_dict = self.convert_json(
            excluded_node_delete_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_node_delete_dict)

        response = self.send_delete_with_body(
            body=body_json,
            url=self.__base_stateful_node_url + "/" + node_id,
            entity_name=self.ENTITY_NAME)

        return response

    def get_stateful_node(self, node_id: str):
        """
        Get a Stateful Node

        # Arguments
        node_id (String): Stateful Node ID

        # Returns
        (Object): Stateful Node API response
        """
        response = self.send_get(
            url=self.__base_stateful_node_url + "/" + node_id,
            entity_name=self.ENTITY_NAME)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_all_stateful_nodes(self, name: str = None, region: str = None):
        """
        Get all Stateful Nodes

        # Returns
        (List): List of Stateful Nodes API response
        """
        query_params = dict(name=name, region=region)

        response = self.send_get(
            url=self.__base_stateful_node_url,
            query_params=query_params,
            entity_name=self.ENTITY_NAME)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def get_stateful_node_resources(self, node_id: str):
        """
        Get the node's attached resources (storage and network interfaces)

        # Arguments
        node_id (String): Stateful Node ID

        # Returns
        (Object): Stateful Node API response
        """
        response = self.send_get(
            url=self.__base_stateful_node_url + "/" + node_id + "/resources",
            entity_name=self.ENTITY_NAME)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_stateful_node_status(self, node_id: str):
        """
        Get the status of a specific stateful node.

        # Arguments
        node_id (String): Stateful Node ID

        # Returns
        (Object): Stateful Node API response
        """
        response = self.send_get(
            url=self.__base_stateful_node_url + "/" + node_id + "/status",
            entity_name=self.ENTITY_NAME)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_all_stateful_node_statuses(self):
        """
        Get the statuses of all Stateful Nodes in a specific account.

        # Returns
        (Object): List of Stateful Node Statuses
        """
        response = self.send_get(
            url=self.__base_stateful_node_url + "/status",
            entity_name=self.ENTITY_NAME)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def update_stateful_node_state(self, node_id: str, state: str):
        """
        Update a Stateful Node State

        # Arguments
        node_id (String): Stateful Node  ID
        state (String): Desired state

        # Returns
        (Object): StatefulNode API response
        """
        body_json = json.dumps(dict(state=state))

        response = self.send_put(
            body=body_json,
            url=self.__base_stateful_node_url + "/" + node_id + "/state",
            entity_name=self.ENTITY_NAME)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["status"]

    def get_stateful_node_from_azure_vm(self, resource_group_name: str, virtual_machine_name: str):
        """
        Get the configuration of a stateful node from a Azure VM for importing.

        # Arguments
        resource_group_name (String): Resource Group of the VM to Import
        virtual_machine_name (String): Virtual Machine to import

        # Returns
        (Object): Stateful Node API response
        """
        response = self.send_get(
            url=self.__base_stateful_node_url + "/resourceGroup/" + resource_group_name +
            "/virtualMachine/" + virtual_machine_name + "/importConfiguration",
            entity_name=self.ENTITY_NAME)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def import_vm_to_stateful_node(self, import_vm_configuration: azure_stateful_node.ImportVmConfiguration):
        """
        Import an Azure VM and create a Stateful Node by providing a node configuration.

        # Arguments
        import_vm_configuration (StatefulNode): Configuration of VM to import

        # Returns
        (Object): StatefulNode API response
        """
        request = azure_stateful_node.ImportVmToStatefulNodeRequest(
            import_vm_configuration=import_vm_configuration)

        excluded_node_dict = self.exclude_missing(json.loads(request.toJSON()))

        formatted_node_dict = self.convert_json(
            excluded_node_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_node_dict)

        response = self.send_post(
            body=body_json,
            url=self.__base_stateful_node_url + "/import",
            entity_name=self.ENTITY_NAME)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_stateful_node_import_status(self, import_id):
        """
        Get the import process status of a Stateful Node.

        # Arguments
        import_id (String): Import ID

        # Returns
        (Object) : Stateful Node API response
        """
        response = self.send_get(
            url=self.__base_stateful_node_url + "/import/" + import_id + "/status",
            entity_name=self.ENTITY_NAME)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]

    def attach_data_disk_to_stateful_node(self, node_id: str,
                                          data_disk_configuration: azure_stateful_node.AttachDataDiskConfiguration):
        """
        Create a new data disk and attche it to the Stateful Node.

        # Arguments
        node_id (String): Stateful Node  ID
        data_disk_configuration (AttachDataDiskConfiguration): Configuration of Data Disk

        # Returns
        (Object): StatefulNode API response
        """
        request = azure_stateful_node.AttachDataDiskToStatefulNodeRequest(
            data_disk_configuration)

        excluded_node_update_dict = self.exclude_missing(
            json.loads(request.toJSON()))

        formatted_node_update_dict = self.convert_json(
            excluded_node_update_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_node_update_dict)

        response = self.send_put(
            body=body_json,
            url=self.__base_stateful_node_url + "/" + node_id + "/dataDisk/attach",
            entity_name=self.ENTITY_NAME)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]

    def detach_data_disk_from_stateful_node(self, node_id: str,
                                            data_disk_configuration: azure_stateful_node.DetachDataDiskConfiguration):
        """
        Detach a data disk from a Stateful Node.

        # Arguments
        node_id (String): Stateful Node  ID
        data_disk_configuration (DetachDataDiskConfiguration): Configuration of Data Disk

        # Returns
        (Object): StatefulNode API response
        """
        request = azure_stateful_node.DetachDataDiskFromStatefulNodeRequest(
            data_disk_configuration)

        excluded_node_update_dict = self.exclude_missing(
            json.loads(request.toJSON()))

        formatted_node_update_dict = self.convert_json(
            excluded_node_update_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_node_update_dict)

        response = self.send_put(
            body=body_json,
            url=self.__base_stateful_node_url + "/" + node_id + "/dataDisk/detach",
            entity_name=self.ENTITY_NAME)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["status"]

    def get_stateful_node_logs(self, node_id, from_date, to_date, severity=None, resource_id=None, limit=None):
        """
        Get the logs of a Stateful Node according to severity and time period filter parameters.

        # Arguments
        node_id (String): Stateful ID
        to_date (String): On or Before this date 
        from_date (String): On or After this date
        severity(String) (Optional): Log level severity
        resource_id(String) (Optional): Filter log extracted entires related to a specific resource id
        limit(String) (Optional): Maximum number of lines to extract in a response

        # Returns
        (Object): Stateful Node API response
        """
        query_params = dict(toDate=to_date, fromDate=from_date, severity=severity,
                            resourceId=resource_id, limit=limit)

        response = self.send_get(
            url=self.__base_stateful_node_url + "/" + node_id + "/log",
            query_params=query_params,
            entity_name=self.ENTITY_NAME)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def swap_os_disk_to_stateful_node(self, node_id: str,
                                      swap_osdisk_configuration: azure_stateful_node.SwapOsDiskConfiguration):
        """
        Configure a new managed OS disk for an OS persisted paused Stateful Node

        # Arguments
        node_id (String): Stateful Node  ID
        swap_osdisk_configuration (SwapOsDiskConfiguration): Configuration of OS Disk

        # Returns
        (Object): StatefulNode API response
        """
        request = azure_stateful_node.SwapOsDiskToStatefulNodeRequest(
            swap_osdisk_configuration)

        excluded_node_update_dict = self.exclude_missing(
            json.loads(request.toJSON()))

        formatted_node_update_dict = self.convert_json(
            excluded_node_update_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_node_update_dict)

        response = self.send_put(
            body=body_json,
            url=self.__base_stateful_node_url + "/" + node_id + "/osDisk/swap",
            entity_name=self.ENTITY_NAME)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]

    def get_all_stateful_node_costs(self, from_date: str, to_date: str, owner_id: str = None):
        """
        Get the total costs of a single stateful node/all stateful nodes and for a specific time period.

        # Arguments
        to_date (String): On or Before this date
        from_date (String): On or After this date
        ownerId (String) (Optional): Log level severity

        # Returns
        (Object): Stateful Node API response
        """
        query_params = dict(
            toDate=to_date, fromDate=from_date, ownerId=owner_id)

        response = self.send_get(
            url=self.__base_stateful_node_url + "/cost",
            query_params=query_params,
            entity_name=self.ENTITY_NAME)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def get_all_stateful_node_aggregated_daily_costs(self, from_date: str, to_date: str, owner_id: str = None):
        """
        Get the total costs per day of a single stateful node/all stateful nodes and for a specific time period.

        # Arguments
        to_date (String): On or Before this date
        from_date (String): On or After this date
        ownerId (String) (Optional): Log level severity

        # Returns
        (Object): Stateful Node API response
        """
        query_params = dict(fromDate=from_date,
                            toDate=to_date, ownerId=owner_id)

        response = self.send_get(
            url=self.__base_stateful_node_url + "/cost/daily",
            query_params=query_params,
            entity_name=self.ENTITY_NAME)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def get_stateful_node_size_usage(self, from_date: str, to_date: str, owner_id: str = None):
        """
        Get the daily costs per VM size of a single stateful node/all stateful nodes and for a specific time period.

        # Arguments
        to_date (String): On or Before this date
        from_date (String): On or After this date
        ownerId (String) (Optional): Log level severity

        # Returns
        (Object): Stateful Node API response
        """
        query_params = dict(fromDate=from_date,
                            toDate=to_date, ownerId=owner_id)

        response = self.send_get(
            url=self.__base_stateful_node_url + "/sizeUsage/daily",
            query_params=query_params,
            entity_name=self.ENTITY_NAME)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]
