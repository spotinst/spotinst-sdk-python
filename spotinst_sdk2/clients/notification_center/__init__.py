import json
from spotinst_sdk2.models.notification_center import notification_center
from spotinst_sdk2.client import Client

class NotificationCenterClient(Client):
    __base_url = "/notificationCenter"


    # get the list of resources associated with an account
    def get_account_resources(self):
        """
        get the list of resources associated with an account 

        # Returns
        (Object): Spotinst API response 
        """
        response = self.send_get(
            url=self.__base_url +
            "/compute/resource",
            entity_name="resources"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]
    
    # get the list of events associated with an account
    def get_aggregated_events(self):   
        """
        get the list of events assciated with an account 

        # Returns
        (Object): Spotinst API response 
        """
        response = self.send_get(
            url=self.__base_url +
            "/compute/event" ,
            entity_name="events"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]
    
    # get the list of resources associated with an account
    def get_all_notification_policies(self):
        """
        get the list of all notification policies

        # Returns
        (Object): Spotinst API response 
        """
        response = self.send_get(
            url=self.__base_url +
            "/policy",
            entity_name="events"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]
    
    # get the list of resources associated with an account
    def get_specific_notification_policy(self, policy_id: str):
        """
        get specific notification policy

        # Arguments
        policy_id: str

        # Returns
        (Object): Spotinst API response 
        """
        response = self.send_get(
            url=self.__base_url +
            "/policy/" + policy_id,
            entity_name="policy"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]
    
    # create notification policy
    def create_notification_policy(self, policy: notification_center.Policy):
        
        """
        create notification policy

        # Arguments
        policy (Policy): Policy object

        # Returns
        (Object): Spotinst API response 
        """
        request = notification_center.PolicyCreationRequest(policy)
        
        excluded_group_dict = self.exclude_missing(json.loads(request.toJSON()))

        formatted_policy_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)
        
        body_json = json.dumps(formatted_policy_dict)

        response = self.send_post(
            body = body_json,
            url=self.__base_url + "/policy",
            entity_name="policy"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        ret_val = formatted_response["response"]["items"][0]
        return ret_val
    
    # update notification policy
    def update_notification_policy(self, policy_id: str, policy: notification_center.Policy):
        
        """
        update notification policy

        # Arguments
        policy_id : str
        policy (Policy): Policy object

        # Returns
        (Object): Spotinst API response 
        """
        request = notification_center.PolicyUpdateRequest(policy)
        
        excluded_group_dict = self.exclude_missing(json.loads(request.toJSON()))

        formatted_policy_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)
        
        body_json = json.dumps(formatted_policy_dict)

        response = self.send_put(
            body = body_json,
            url=self.__base_url + "/policy/" + policy_id,
            entity_name="policy"
        )

        return response
    
    # delete notification policy
    def delete_notification_policy(self, policy_id: str):
        
        """
        delete notification policy

        # Arguments
        policy_id (String): Policy Id

        # Returns
        (Object): Spotinst API response 
        """
        return self.send_delete(
            url=self.__base_url + "/policy/" + policy_id,
            entity_name="policy"
        )