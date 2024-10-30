import json
from typing import List

from spotinst_sdk2.client import Client
import spotinst_sdk2.models.admin.user_mapping as spotinst_user_mapping
import spotinst_sdk2.models.admin.organization as admin_org


class AdminClient(Client):
    __base_setup_url = "/setup"

    # region Organization and Account
    def create_organization(self, org_name: str):
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

    def delete_organization(self, org_id: str):
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

    def set_cloud_credentials(self, iam_role: str, external_id: str = None):
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

    def create_account(self, account_name: str):
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

    def update_account(self, account_id: str, new_account_name: str, slack_notification_channels: List[str] = None):
        """
        create an account 

        # Arguments
        account_id (String): Account Id
        new_account_name (String): New Account Name
        slack_notification_channels List(str): List of slack notification channels

        # Returns
        (Object): Spotinst API response 
        """
        response = self.send_put(
            url=self.__base_setup_url +
            "/account/" + account_id,
            body=json.dumps(dict(account=dict(
                name=new_account_name, slackNotificationChannels=slack_notification_channels))),
            entity_name="account"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["status"]

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

    def delete_account(self, account_name: str):
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

    def create_user(self, first_name: str, last_name: str, email: str, password: str, role: str):
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

    def detach_user(self, user_email: str):
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

    def get_user(self, user_email: str):
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

    def get_policies(self):
        """
        Retrieves all policies from an organization.

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_get(
            url=self.__base_setup_url + "/organization/policy", entity_name="policy"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def get_user_details(self, user_id: str):
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

    def delete_user(self, user_id: str):
        """
        Deletes a user (console or programmatic) from an organization.

        # Arguments
        user_id (String): User ID

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_delete(
            url=self.__base_setup_url + "/user/" + user_id, entity_name="user"
        )

        return response

    def update_user_to_user_group_mapping(self, user_id: str, user_group_ids: List[str]):
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

    def update_user_to_policy_mapping(self, user_id: str, policies):
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

    def get_user(self, user_email: str):
        """
        Get user's account mapping.

        # Returns
        (Object): Spotinst API response
        """
        query_params = dict(userEmail=user_email)

        response = self.send_get(
            url=self.__base_setup_url + "/accountUserMapping", entity_name="user",
            query_params=query_params
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def create_programmatic_user(self, name: str, description: str, accounts=None, policies=None):
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

    def get_access_policy_actions(self, category: str = None, name: str = None, resource_pattern: str = None, scope: str = None, service: str = None):
        """
        Get actions for access policies.

        # Returns
        (Object): Spotinst API response
        """
        query_params = dict(category=category, name=name,
                            resourcePattern=resource_pattern, scope=scope, service=service)

        response = self.send_get(
            url=self.__base_setup_url + "/access/policyAction", entity_name="user",
            query_params=query_params
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def create_access_policy(self, policy: admin_org.AccessPolicy):
        """
        Create an access policy

        # Arguments
        policy (AccessPolicy): AccessPolicy Object

        # Returns
        (Object): Spotinst API response 
        """
        request = admin_org.AccessPolicyCreationRequest(policy)

        excluded_policy_dict = self.exclude_missing(
            json.loads(request.toJSON()))

        formatted_policy_dict = self.convert_json(
            excluded_policy_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_policy_dict)

        policy_response = self.send_post(
            body=body_json,
            url=self.__base_setup_url + "/access/policy", entity_name="policy")

        formatted_response = self.convert_json(
            policy_response, self.camel_to_underscore)

        ret_val = formatted_response["response"]["items"][0]

        return ret_val

    def update_access_policy(self, policy_id: str, policy: admin_org.AccessPolicy):
        """
        Updates an access policy settings.

        # Arguments
        policy_id (String): Policy ID
        policy (AccessPolicy): AccessPolicy Object

        # Returns
        (Object): Spotinst API response
        """
        request = admin_org.AccessPolicyUpdationRequest(policy)

        excluded_policy_dict = self.exclude_missing(
            json.loads(request.toJSON()))

        formatted_policy_dict = self.convert_json(
            excluded_policy_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_policy_dict)

        policy_response = self.send_put(
            body=body_json,
            url=self.__base_setup_url + "/access/policy/" + policy_id, entity_name="policy")

        formatted_response = self.convert_json(
            policy_response, self.camel_to_underscore)

        return formatted_response["response"]["status"]

    def delete_access_policy(self, policy_id: str):
        """
        Deletes an access policy.

        # Arguments
        policy_id (String): Policy ID

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_delete(
            url=self.__base_setup_url + "/access/policy/" + policy_id, entity_name="policy"
        )

        return response

    def get_user_groups(self):
        """
        Retrieves all user-groups from an organization.

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_get(
            url=self.__base_setup_url + "/access/userGroup", entity_name="usergroup"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def create_user_group(self, user_group: admin_org.UserGroup):
        """
        Create a new User Group

        # Arguments
        group (UserGroup): UserGroup Object

        # Returns
        (Object): Spotinst API response 
        """
        request = admin_org.UserGroupCreationRequest(user_group)

        excluded_group_dict = self.exclude_missing(
            json.loads(request.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        policy_response = self.send_post(
            body=body_json,
            url=self.__base_setup_url + "/access/userGroup", entity_name="usergroup")

        formatted_response = self.convert_json(
            policy_response, self.camel_to_underscore)

        ret_val = formatted_response["response"]["items"][0]

        return ret_val

    def get_user_group_details(self, user_group_id: str):
        """
        Get the details of a user Group

        # Arguments
        user_group_id (String): User Group ID

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_get(
            url=self.__base_setup_url + "/access/userGroup/" + user_group_id, entity_name="usergroup"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def delete_user_group(self, user_group_id: str):
        """
        Delete a user group.

        # Arguments
        user_group_id (String): User Group ID

        # Returns
        (Object): Spotinst API response
        """
        return self.send_delete(
            url=self.__base_setup_url + "/access/userGroup/" + user_group_id, entity_name="usergroup"
        )

    def update_user_group_to_user_mapping(self, user_group_id: str, user_ids: List[str]):
        """
        Update the mapping of a given user group to users

        # Arguments
        user_group_id (String): Identifier of a usergroup.
        user_ids (List): The users to register under the given user group (should be existing users only)

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_put(
            url=self.__base_setup_url + "/access/userGroup/" + user_group_id + "/userMapping",
            body=json.dumps(dict(userIds=user_ids)),
            entity_name="usergroup",
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["status"]

    def update_user_group_to_policy_mapping(self, user_group_id: str, policies):
        """
        Update the mapping of a given user group to policies

        # Arguments
        user_group_id (String): Identifier of a user group.
        policies (List): The policies to register under the given user group (should be existing policies only)

        # Returns
        (Object): Spotinst API response
        """

        response = self.send_put(
            url=self.__base_setup_url + "/access/userGroup/" +
            user_group_id + "/policyMapping",
            body=json.dumps(dict(policies=policies)),
            entity_name="usergroup",
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["status"]
