import json

from spotinst_sdk2.client import Client
import spotinst_sdk2.models.admin.user_mapping as spotinst_user_mapping


class AdminClient(Client):
    __base_setup_url = "/setup"

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
            url=self.__base_setup_url +
            "/organization",
            body=json.dumps(dict(organization=dict(name=org_name))),
            entity_name="organization"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def delete_organization(self, org_id):
        """
        delete organization 

        # Arguments
        org_id (String): Organization Id

        # Returns
        (Object): Spotinst API response 
        """
        response = self.send_delete(
            url=self.__base_setup_url +
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
            url=self.__base_setup_url + "/credentials/aws/externalId",
            entity_name="credentials"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

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
            url=self.__base_setup_url +
            "/credentials/aws",
            body=json.dumps(dict(credentials=credentials)),
            entity_name="credentials"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["status"]

    def create_account(self, account_name):
        """
        create an account 

        # Arguments
        account_name (String): Account Name

        # Returns
        (Object): Spotinst API response 
        """
        response = self.send_post(
            url=self.__base_setup_url +
            "/account",
            body=json.dumps(dict(account=dict(name=account_name))),
            entity_name="account"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_accounts(self):
        """
        get accounts in organization

        # Returns
        (Object): Spotinst API response 
        """
        response = self.send_get(
            url=self.__base_setup_url +
            "/account",
            entity_name="account"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def delete_account(self, account_name):
        """
        delete account

        # Arguments
        account_name (String): Account Name

        # Returns
        (Object): Spotinst API response 
        """
        response = self.send_delete(
            url=self.__base_setup_url +
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
            url=self.__base_setup_url +
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

        return formatted_response["response"]["items"][0]

    def add_existing_user(self, user_email, role):
        """
        Add existing user

        # Arguments
        user_email (String): User email
        role (String): User role

        # Returns
        (Object): Spotinst API response 
        """
        response = self.send_post(
            url=self.__base_setup_url +
            "/account/" + self.account_id +
            "/user",
            body=json.dumps(dict(userEmail=user_email, role=role)),
            entity_name="user"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["status"]

    def update_user_role(self, user_email, role):
        """
        Update existing user

        # Arguments
        user_email (String): User email
        role (String): User role

        # Returns
        (Object): Spotinst API response 
        """
        response = self.send_put(
            url=self.__base_setup_url +
            "/account/" + self.account_id +
            "/user",
            body=json.dumps(dict(userEmail=user_email, role=role)),
            entity_name="user"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["status"]

    def detach_user(self, user_email):
        """
        Delete existing user

        # Arguments
        user_email (String): User email

        # Returns
        (Object): Spotinst API response 
        """
        response = self.send_delete_with_body(
            url=self.__base_setup_url +
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
        query_params = dict(userEmail=user_email)
        response = self.send_get(
            url=self.__base_setup_url + "/accountUserMapping",
            query_params=query_params,
            entity_name="user"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def assign_user_to_account(self, mappings):
        """
        Assign user to account

        # Arguments
        mappings (List): List of UserMapping Objects

        # Returns
        (Object): Spotinst API response 
        """
        mappings = spotinst_user_mapping.UserMappingRequest(mappings)

        excluded_group_dict = self.exclude_missing(
            json.loads(mappings.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        response = self.send_post(
            url=self.__base_setup_url + "/accountUserMapping",
            body=body_json,
            entity_name="user"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["status"]

    # endregion
    def get_users(self):
        """
        Retrieves all users from an organization.

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_get(
            url=self.__base_setup_url + "/organization/user", entity_name="user"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def get_user_details(self, user_id):
        """
        Retrieves an individual user details.

        # Arguments
        user_id (String): User ID

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_get(
            url=self.__base_setup_url + "/user/" + user_id, entity_name="user"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def delete_user(self, user_id):
        """
        Deletes a user from an organization.

        # Arguments
        user_id (String): User ID

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_delete(
            url=self.__base_setup_url + "/user/" + user_id, entity_name="user"
        )

        return response

    def update_user_to_user_group_mapping(self, user_id, user_group_ids):
        """
        Update the mapping of a given user to user groups

        # Arguments
        user_id (String): Identifier of a user.
        user_group_ids (List): A list of the user groups to register the given user to

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_put(
            url=self.__base_setup_url + "/user/" + user_id + "/userGroupMapping",
            body=json.dumps(dict(userGroupIds=user_group_ids)),
            entity_name="user",
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["status"]

    def update_user_to_policy_mapping(self, user_id, policies):
        """
        Update the mapping of a given user to policies

        # Arguments
        user_id (String): Identifier of a user.
        policies (List): A list of policies to register under the given user

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_put(
            url=self.__base_setup_url + "/user/" + user_id + "/policyMapping",
            body=json.dumps(dict(policies=policies)),
            entity_name="user",
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["status"]

    def create_programmatic_user(self, name, description, accounts=None, policies=None):
        """
        Create a programmatic user

        # Arguments
        name (String): Name of the programmatic user
        description (String): Brief description of the user
        accounts (List): All the accounts the programmatic user will have access to
        policies (List): All the policies the programmatic user will have access to

        # Returns
        (Object): Spotinst API response
        """
        if accounts is None and policies is None:
            raise ValueError(
                "Either accounts or policies must be provided in create_programmatic_user"
            )

        payload = {
            "description": description,
            "name": name,
        }
        if accounts is not None:
            payload["accounts"] = accounts
        if policies is not None:
            payload["policies"] = policies

        response = self.send_post(
            url=self.__base_setup_url + "/user/programmatic",
            body=json.dumps(payload),
            entity_name="programmaticUser",
        )
        formatted_response = self.convert_json(
            response, self.camel_to_underscore)
        return formatted_response["response"]["items"][0]
