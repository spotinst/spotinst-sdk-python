import json

from spotinst_sdk2.client import Client
import spotinst_sdk2.models.admin.user_mapping as spotinst_user_mapping

class AdminClient(Client):
    __base_setup_url = "https://api.spotinst.io/setup"

    # region Organization and Account
    def create_organization(self, org_name):
        """
        Create an organization 
        
        # Arguments
        org_name (String): Orgnanization name
        
        # Returns
        (Object): Spotinst API response 
        """ 
        response = self.send_post(
            url= self.__base_setup_url + 
            "/organization",
            body=json.dumps(dict(organization=dict(name=org_name))),
            entity_name="organization"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def delete_organization(self, org_id):
        """
        delete organization 
        
        # Arguments
        org_id (String): Organization Id
        
        # Returns
        (Object): Spotinst API response 
        """ 
        response = self.send_delete(
            url= self.__base_setup_url + 
            "/organization/" + str(org_id),
            entity_name="organization"
        )

        return response

    def create_aws_external_id(self):
        """
        Important note: This is deprecated, please use setup_aws client instead(SetupAWSClient#create_external_id)

        Create aws account external id.
        You should use the external id when creating your AWS role for your spot account

        # Returns
        (Object): Spotinst API response 
        """
        response = self.send_post(
            url= self.__base_setup_url + "/credentials/aws/externalId",
            entity_name="credentials"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        ret_val = formatted_response["response"]["items"][0]

        return ret_val

    def set_cloud_credentials(self, iam_role, external_id=None):
        """
        Important note: This is deprecated, please use setup_aws client instead(SetupAWSClient#set_credentials)

        set cloud credentials 
        Please create external id using spot api (see #AdminClient.create_aws_external_id)
        and use it when creating the AWS role
        
        # Arguments
        iam_role (String): IAM Role
        external_id (String) (Optional): External ID
        
        # Returns
        (Object): Spotinst API response 
        """ 
        credentials = {"iamRole": iam_role}

        if external_id is not None:
            credentials['externalId'] = external_id

        response = self.send_post(
            url= self.__base_setup_url +
            "/credentials/aws",
            body=json.dumps(dict(credentials=credentials)),
            entity_name="credentials"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["status"]

        return retVal

    def create_account(self, account_name):
        """
        create an account 
        
        # Arguments
        account_name (String): Account Name
        
        # Returns
        (Object): Spotinst API response 
        """ 
        response = self.send_post(
            url= self.__base_setup_url +
            "/account",
            body=json.dumps(dict(account=dict(name=account_name))),
            entity_name="account"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def get_accounts(self):
        """
        get accounts in organization
        
        # Returns
        (Object): Spotinst API response 
        """ 
        response = self.send_get(
            url= self.__base_setup_url +
            "/account",
            entity_name="account"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"]

        return retVal

    def delete_account(self, account_name):
        """
        delete account
        
        # Arguments
        account_name (String): Account Name
        
        # Returns
        (Object): Spotinst API response 
        """ 
        response = self.send_delete(
            url= self.__base_setup_url +
            "/account/" + account_name,
            entity_name="account"
        )

        return response

    def create_user(self, first_name, last_name, email, password, role):
        """
        Create user
        
        # Arguments
        first_name (String): Users first name
        last_name (String): User last name
        email (String): Eser email
        password (String): User email
        role (String): User role
        
        # Returns
        (Object): Spotinst API response 
        """ 
        response = self.send_post(
            url= self.__base_setup_url +
            "/user",
            body=json.dumps(dict(
                firstName=first_name,
                lastName=last_name,
                email=email,
                password=password,
                role=role)),
            entity_name="user"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal       

    def add_exsisting_user(self, user_email, role):
        """
        Add exsisting user
        
        # Arguments
        user_email (String): User email
        role (String): User role
        
        # Returns
        (Object): Spotinst API response 
        """ 
        response = self.send_post(
            url= self.__base_setup_url +
            "/account/" + self.account_id +
            "/user",
            body=json.dumps(dict(userEmail=user_email, role=role)),
            entity_name="user"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["status"]

        return retVal 

    def update_user_role(self, user_email, role):
        """
        Update exsisting user
        
        # Arguments
        user_email (String): User email
        role (String): User role
        
        # Returns
        (Object): Spotinst API response 
        """ 
        response = self.send_put(
            url= self.__base_setup_url +
            "/account/" + self.account_id +
            "/user",
            body=json.dumps(dict(userEmail=user_email, role=role)),
            entity_name="user"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["status"]

        return retVal 

    def detach_user(self, user_email):
        """
        Delete exsisting user
        
        # Arguments
        user_email (String): User email
        
        # Returns
        (Object): Spotinst API response 
        """ 
        response = self.send_delete_with_body(
            url= self.__base_setup_url +
            "/account/" + self.account_id +
            "/user",
            body=json.dumps(dict(userEmail=user_email)),
            entity_name="user"
        )

        return response 

    def get_user(self, user_email):
        """
        Get user
        
        # Arguments
        user_email (String): User email
        
        # Returns
        (Object): Spotinst API response 
        """ 
        query_params= dict(userEmail=user_email)
        response = self.send_get(
            url= self.__base_setup_url + "/accountUserMapping",
            query_params=query_params,
            entity_name="user"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"]

        return retVal 

    def assign_user_to_account(self, mappings):
        """
        Assign user to account
        
        # Arguments
        mappings (List): List of UserMapping Objects
        
        # Returns
        (Object): Spotinst API response 
        """ 
        mappings = spotinst_user_mapping.UserMappingRequest(mappings)

        excluded_group_dict = self.exclude_missing(json.loads(mappings.toJSON()))
        
        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        response = self.send_post(
            url= self.__base_setup_url + "/accountUserMapping",
            body= body_json,
            entity_name="user"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["status"]

        return retVal 
    # endregion



