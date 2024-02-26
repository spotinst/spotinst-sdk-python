import json

from spotinst_sdk2.client import Client
import spotinst_sdk2.models.mrscaler.aws as mrScaler_aws


class MrScalerAwsClient(Client):
    __base_emr_url = "/aws/emr/mrScaler"

    # region EMR
    def create_emr(self, emr):
        """
        Create an EMR 

        # Arguments
        emr (EMR): EMR Object

        # Returns
        (Object): Elastigroup API response 
        """
        emr = mrScaler_aws.EMRCreationRequest(emr)

        excluded_group_dict = self.exclude_missing(json.loads(emr.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        group_response = self.send_post(
            body=body_json,
            url=self.__base_emr_url,
            entity_name='emr')

        formatted_response = self.convert_json(
            group_response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def update_emr(self, emr_id, emr):
        """
        Update an existing EMR 

        # Arguments
        emr_id (String): EMR id
        emr (EMR): EMR Object

        # Returns
        (Object): Elastigroup API response 
        """
        emr = mrScaler_aws.EMRCreationRequest(emr)

        excluded_group_dict = self.exclude_missing(json.loads(emr.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        group_response = self.send_put(
            body=body_json,
            url=self.__base_emr_url +
            "/" + emr_id,
            entity_name='emr')

        formatted_response = self.convert_json(
            group_response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_all_emr(self):
        """
        Get all EMR in account

        # Returns
        (Object): Elastigroup API response 
        """
        response = self.send_get(
            url=self.__base_emr_url,
            entity_name="emr"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def get_emr(self, emr_id):
        """
        Get an existing EMR json

        # Arguments
        emr_id (String): EMR id

        # Returns
        (Object): Elastigroup API response 
        """
        response = self.send_get(
            url=self.__base_emr_url +
            "/" + emr_id,
            entity_name="emr"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_emr_instances(self, emr_id):
        """
        Get instances from EMR 

        # Arguments
        emr_id (String): EMR id

        # Returns
        (Object): Elastigroup API response 
        """
        response = self.send_get(
            url=self.__base_emr_url +
            "/" + emr_id +
            "/instance",
            entity_name="emr"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def get_emr_cluster(self, emr_id):
        """
        Get cluster from EMR

        # Arguments
        emr_id (String): EMR id

        # Returns
        (Object): Elastigroup API response 
        """
        response = self.send_get(
            url=self.__base_emr_url +
            "/" + emr_id +
            "/cluster",
            entity_name="emr"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_emr_cost(self, emr_id, from_date=None, to_date=None):
        """
        Get cost from EMR

        # Arguments
        emr_id (String): EMR id
        from_date (String) (Optional): From Date
        to_date (String) (Optional): to date

        # Returns
        (Object): Elastigroup API response 
        """
        query_params = dict(fromDate=from_date, toDate=to_date)

        response = self.send_get(
            url=self.__base_emr_url +
            "/" + emr_id +
            "/costs",
            query_params=query_params,
            entity_name="emr"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def delete_emr(self, emr_id):
        """
        Delete an EMR

        # Arguments
        emr_id (String): EMR id

        # Returns
        (Object): Elastigroup API response 
        """
        response = self.send_delete(
            url=self.__base_emr_url +
            "/" + emr_id,
            entity_name="emr"
        )

        return response

    def scale_up_emr(self, emr_id, adjustment):
        """
        Scale up an EMR

        # Arguments
        emr_id (String): EMR id
        adjustment (Int): Ammount to scale

        # Returns
        (Object): Elastigroup API response 
        """
        query_params = dict(adjustment=adjustment)

        response = self.send_put(
            url=self.__base_emr_url +
            "/" + emr_id +
            "/scale/up",
            query_params=query_params,
            entity_name="emr"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def scale_down_emr(self, emr_id, adjustment):
        """
        Scale down an EMR

        # Arguments
        emr_id (String): EMR id
        adjustment (Int): Ammount to scale

        # Returns
        (Object): Elastigroup API response 
        """
        query_params = dict(adjustment=adjustment)

        response = self.send_put(
            url=self.__base_emr_url +
            "/" + emr_id +
            "/scale/down",
            query_params=query_params,
            entity_name="emr"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    # endregion
