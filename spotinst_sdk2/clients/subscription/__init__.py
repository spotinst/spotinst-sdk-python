import json

from spotinst_sdk2.client import Client
import spotinst_sdk2.models.subscription as spotinst_event_subscription

class SubscriptionClient(Client):
    __base_event_subscription_url = "https://api.spotinst.io/events/subscription"

    # region Event Subscription
    def create_event_subscription(self, subscription):
        """
        Create an event subscription 
        
        # Arguments
        subscription (Subscription): Subscription Object
        
        # Returns
        (Object): Subscription API response 
        """ 
        subscription = spotinst_event_subscription.SubscriptionRequest(subscription)

        excluded_group_dict = self.exclude_missing(json.loads(subscription.toJSON()))
        
        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        group_response = self.send_post(
            body=body_json,
            url=self.__base_event_subscription_url,
            entity_name='subscription')

        formatted_response = self.convert_json(
            group_response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def update_event_subscription(self, subscription_id, subscription):
        """
        Update an exsisting event subscription 
        
        # Arguments
        subscription_id (String): Subscription id
        subscription (Subscription): Subscription Object
        
        # Returns
        (Object): Subscription API response 
        """ 
        subscription = spotinst_event_subscription.SubscriptionRequest(subscription)

        excluded_group_dict = self.exclude_missing(json.loads(subscription.toJSON()))
        
        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)
        
        group_response = self.send_put(
            body=body_json,
            url=self.__base_event_subscription_url +
            "/" + subscription_id,
            entity_name='subscription')

        formatted_response = self.convert_json(
            group_response, self.camel_to_underscore)

        retVal = formatted_response["response"]

        return retVal

    def get_all_event_subscription(self):
        """
        Get all Subscription in account
        
        # Returns
        (Object): Subscription API response 
        """ 
        response = self.send_get(
            url=self.__base_event_subscription_url,
            entity_name="subscription"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"]

        return retVal

    def get_event_subscription(self, subscription_id):
        """
        Get an exsisting event subscription json
        
        # Arguments
        subscription_id (String): Subscription id
        
        # Returns
        (Object): Subscription API response 
        """ 
        response = self.send_get(
            url=self.__base_event_subscription_url +
            "/" + subscription_id,
            entity_name="subscription"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal        
    
    def delete_event_subscription(self, subscription_id):
        """
        Delete an event subscription
        
        # Arguments
        subscription_id (String): Subscription id
        
        # Returns
        (Object): subscription response 
        """ 
        response = self.send_delete(
            url=self.__base_event_subscription_url +
            "/" + subscription_id,
            entity_name="subscription"
        )

        return response  
    # end region

