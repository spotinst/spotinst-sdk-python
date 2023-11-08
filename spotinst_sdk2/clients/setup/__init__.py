import json

from spotinst_sdk2.client import Client

# region Azure imports
import spotinst_sdk2.models.setup.azure as azure_setup
import spotinst_sdk2.models.setup.gcp as gcp_setup
# endregion

# region AWS


class SetupAWSClient(Client):
    __base_setup_url = "/setup"

    def create_external_id(self):
        """
        Create aws account external id.
        You should use the external id when creating your AWS role for your spot account

        # Returns
        (Object): Spotinst API response 
        """
        response = self.send_post(
            url=self.__base_setup_url + "/credentials/aws/externalId",
            entity_name="credentials"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        ret_val = formatted_response["response"]["items"][0]

        return ret_val

    def set_credentials(self, iam_role):
        """
        Set aws credentials 
        Please create external id using spot api (see #AdminClient.create_aws_external_id)
        and use it when creating the AWS role

        # Arguments
        iam_role (String): IAM Role

        # Returns
        (Object): Spotinst API response 
        """
        credentials = {"iamRole": iam_role}

        response = self.send_post(
            url=self.__base_setup_url +
            "/credentials/aws",
            body=json.dumps(dict(credentials=credentials)),
            entity_name="credentials"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        ret_val = formatted_response["response"]["status"]

        return ret_val
# endregion


# region Azure
class SetupAzureClient(Client):
    __base_setup_url = "/azure/setup"

    def set_credentials(self, credentials):
        """"
        Set azure credentials 

        # Arguments
        credentials (AzureCredentials): Azure Credentials Object

        # Returns
        (Object): Spotinst API response 
        """
        set_credentials_request = azure_setup.AzureSetCredentialsRequest(
            azure_credentials=credentials)

        excluded_set_credentials_dict = self.exclude_missing(
            json.loads(set_credentials_request.to_json()))

        formatted_set_credentials_dict = self.convert_json(
            excluded_set_credentials_dict, self.underscore_to_camel)

        response = self.send_post(
            url=self.__base_setup_url + "/credentials",
            body=json.dumps(formatted_set_credentials_dict),
            entity_name='credentials')

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        ret_val = formatted_response["response"]["status"]

        return ret_val

    def validate_credentials(self, credentials):
        """"
        Validate azure credentials 

        # Arguments
        credentials (AzureCredentials): Azure Credentials Object

        # Returns
        (Object): Spotinst API response 
        """
        set_credentials_request = azure_setup.AzureSetCredentialsRequest(
            azure_credentials=credentials)

        excluded_set_credentials_dict = self.exclude_missing(
            json.loads(set_credentials_request.to_json()))

        formatted_set_credentials_dict = self.convert_json(
            excluded_set_credentials_dict, self.underscore_to_camel)

        response = self.send_post(
            url=self.__base_setup_url + "/credentials/validation",
            body=json.dumps(formatted_set_credentials_dict),
            entity_name='credentials')

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        ret_val = formatted_response["response"]["status"]

        return ret_val
# endregion


# region GCP
class SetupGCPClient(Client):
    __base_setup_url = "/gcp/setup"

    def set_credentials(self, credentials):
        """
        Set gcp credentials 

        # Arguments
        credentials (GcpCredentials): Gcp Credentials Object

        # Returns
        (Object): Spotinst API response 
        """
        set_credentials_request = gcp_setup.GcpSetCredentialsRequest(
            gcp_credentials=credentials)

        excluded_set_credentials_dict = self.exclude_missing(
            json.loads(set_credentials_request.to_json()))

        response = self.send_post(
            url=self.__base_setup_url + "/credentials",
            body=json.dumps(excluded_set_credentials_dict),
            entity_name='credentials')

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        ret_val = formatted_response["response"]["status"]

        return ret_val

    def validate_credentials(self, credentials):
        """
        Validate gcp credentials 

        # Arguments
        credentials (GcpCredentials): Gcp Credentials Object

        # Returns
        (Object): Spotinst API response 
        """
        set_credentials_request = gcp_setup.GcpSetCredentialsRequest(
            gcp_credentials=credentials)

        excluded_set_credentials_dict = self.exclude_missing(
            json.loads(set_credentials_request.to_json()))

        response = self.send_post(
            url=self.__base_setup_url + "/credentials/validation",
            body=json.dumps(excluded_set_credentials_dict),
            entity_name='credentials')

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        ret_val = formatted_response["response"]["status"]

        return ret_val
# endregion
