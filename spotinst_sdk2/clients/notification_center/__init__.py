import json
from typing import List

from spotinst_sdk2.clients import Client

class NotificationCenterClient(Client):
    __base_url = "/notificationCenter"


    # get the list of resources associated with an account
    def get_account_resources(self,  account_id: str):
        """
        get the list of resources associated with an account 

        # Arguments
        account_id (String): Account Id

        # Returns
        (Object): Spotinst API response 
        """
        response = self.send_get(
            url=self.__base_url +
            "/compute/resource/" + account_id,
            entity_name="reources"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]
    
    # get the list of events associated with an account
    def get_aggregated_events(self, account_id: str):   
        """
        get the list of events assciated with an account 

        # Arguments
        account_id (String): Account Id

        # Returns
        (Object): Spotinst API response 
        """
        response = self.send_get(
            url=self.__base_url +
            "/compute/event/" + account_id,
            entity_name="events"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]
    
    # get the list of resources associated with an account
    def get_all_notification_policies(self, account_id: str):
        """
        get the list of all notification policies

        # Returns
        (Object): Spotinst API response 
        """
        response = self.send_get(
            url=self.__base_url +
            "/policy/" + account_id,
            entity_name="events"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]