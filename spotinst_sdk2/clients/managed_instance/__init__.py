import json

from spotinst_sdk2.client import Client

import spotinst_sdk2.models.managed_instance.aws as aws_managed_instance

none = "d3043820717d74d9a17694c176d39733"


class ManagedInstanceAwsClient(Client):
    __base_mi_url = "https://api.spotinst.io/aws/ec2/managedInstance"
    ENTITY_NAME = 'managedInstance'

    def create_managed_instance(self, managed_instance: aws_managed_instance.ManagedInstance):
        """
        Create a Managed Instance

        # Arguments
        managed instance (ManagedInstance): ManagedInstance Object

        # Returns
        (Object): ManagedInstance API response
        """
        req = aws_managed_instance.ManagedInstanceCreationRequest(managed_instance)

        req_json_str = req.toJSON()
        req_exclude_missing = self.exclude_missing(json.loads(req_json_str))

        formatted_mi_dict = self.convert_json(
            req_exclude_missing, self.underscore_to_camel)

        body_json = json.dumps(formatted_mi_dict)

        self.print_output(body_json)

        mi_response = self.send_post(
            body=body_json,
            url=self.__base_mi_url,
            entity_name=self.ENTITY_NAME)

        formatted_response = self.convert_json(
            mi_response, self.camel_to_underscore)

        ret_val = formatted_response["response"]["items"][0]

        return ret_val

    def get_managed_instance(self, managed_instance_id: str):
        """
        Get a Managed Instance

        # Arguments
        managed_instance_id(String): Managed Instance ID

        # Returns
        (Object): ManagedInstance API response
        """
        geturl = self.__base_mi_url + "/" + managed_instance_id
        result = self.send_get(url=geturl, entity_name=self.ENTITY_NAME)

        formatted_response = self.convert_json(result, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_managed_instances(self):
        """
        Get all Managed Instance

        # Returns
        List: List of ManagedInstance API response
        """
        content = self.send_get(
            url=self.__base_mi_url,
            entity_name=self.ENTITY_NAME)
        formatted_response = self.convert_json(
            content, self.camel_to_underscore)
        return formatted_response["response"]["items"]

    def update_managed_instance(self, managed_instance_id: str,
                                managed_instance_update: aws_managed_instance.ManagedInstance):
        """
        Update a Managed Instance

        # Arguments
        managed_instance_id(String): Managed Instance ID
        managed_instance_update(ManagedInstance): ManagedInstance Object

        # Returns
        (Object): ManagedInstance API response
        """
        group = aws_managed_instance.ManagedInstanceUpdateRequest(managed_instance_update)

        excluded_group_update_dict = self.exclude_missing(
            json.loads(group.toJSON()))

        formatted_group_update_dict = self.convert_json(excluded_group_update_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_update_dict)

        self.print_output(body_json)

        req_url = self.__base_mi_url + "/" + managed_instance_id

        group_response = self.send_put(
            body=body_json,
            url=req_url,
            entity_name=self.ENTITY_NAME,
        )

        formatted_response = self.convert_json(group_response, self.camel_to_underscore)

        ret_val = formatted_response["response"]["items"][0]

        return ret_val

    def delete_managed_instance(self, managed_instance_id: str,
                                deallocation_config: aws_managed_instance.DeallocationConfig = none,
                                ami_backup: aws_managed_instance.AmiBackup = none):
        """
        Delete a Managed Instance

        # Arguments
        managed_instance_id(String): Managed Instance ID
        deallocation_config(DeallocationConfig): DeallocationConfig object
        ami_backup(AmiBackup): AmiBackup object

        # Returns
        (Object): ManagedInstance API response
        """
        req_url = self.__base_mi_url + "/" + managed_instance_id

        deletion_request = aws_managed_instance.ManagedInstanceDeletionRequest(deallocation_config, ami_backup)

        req_exclude_missing = self.exclude_missing(json.loads(deletion_request.toJSON()))

        formatted_deletion_dict = self.convert_json(req_exclude_missing, self.underscore_to_camel)

        body_json = json.dumps(formatted_deletion_dict)

        response = self.send_delete_with_body(
            body=body_json, url=req_url, entity_name=self.ENTITY_NAME)

        return response

    def recycle_managed_instance(self, managed_instance_id: str):
        """
        Recycle a Managed Instance

        # Arguments
        managed_instance_id(String): Managed Instance ID

        # Returns
        (Object): ManagedInstance API response
        """
        put_url = self.__base_mi_url + "/" + managed_instance_id + "/" + "recycle"
        result = self.send_put(url=put_url, entity_name=self.ENTITY_NAME)

        formatted_response = self.convert_json(result, self.camel_to_underscore)

        return formatted_response["response"]

    def pause_managed_instance(self, managed_instance_id: str):
        """
        Pause a Managed Instance

        # Arguments
        managed_instance_id(String): Managed Instance ID

        # Returns
        (Object): ManagedInstance API response
        """
        put_url = self.__base_mi_url + "/" + managed_instance_id + "/" + "pause"
        result = self.send_put(url=put_url, entity_name=self.ENTITY_NAME)

        formatted_response = self.convert_json(result, self.camel_to_underscore)

        return formatted_response["response"]

    def resume_managed_instance(self, managed_instance_id: str):
        """
        Resume a Managed Instance

        # Arguments
        managed_instance_id(String): Managed Instance ID

        # Returns
        (Object): ManagedInstance API response
        """
        put_url = self.__base_mi_url + "/" + managed_instance_id + "/" + "resume"
        result = self.send_put(url=put_url, entity_name=self.ENTITY_NAME)

        formatted_response = self.convert_json(result, self.camel_to_underscore)

        return formatted_response["response"]
