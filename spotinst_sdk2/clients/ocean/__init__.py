import json

from spotinst_sdk2.client import Client
import spotinst_sdk2.models.ocean.aws as aws_ocean

class OceanAwsClient(Client):
    __base_ocean_url = "https://api.spotinst.io/ocean/aws/k8s/cluster"

    def create_ocean_cluster(self, ocean):
        """
        Create an Ocean Cluster 
        
        # Arguments
        ocean (Ocean): Ocean Object
        
        # Returns
        (Object): Ocean API response 
        """ 
        ocean = aws_ocean.OceanRequest(ocean)

        excluded_group_dict = self.exclude_missing(json.loads(ocean.toJSON()))
        
        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        group_response = self.send_post(
            body=body_json,
            url=self.__base_ocean_url,
            entity_name='ocean')

        formatted_response = self.convert_json(
            group_response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def update_ocean_cluster(self, ocean_id, ocean):
        """
        Update an exsisting Ocean Cluster 
        
        # Arguments
        ocean_id (String): Ocean id
        ocean (Ocean): Ocean Object
        
        # Returns
        (Object): Ocean API response 
        """ 
        ocean = aws_ocean.OceanRequest(ocean)

        excluded_group_dict = self.exclude_missing(json.loads(ocean.toJSON()))
        
        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)
        
        group_response = self.send_put(
            body=body_json,
            url=self.__base_ocean_url +
            "/" + ocean_id,
            entity_name='ocean')

        formatted_response = self.convert_json(
            group_response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def get_all_ocean_cluster(self):
        """
        Get all Ocean in account
        
        # Returns
        (Object): Ocean API response 
        """ 
        response = self.send_get(
            url=self.__base_ocean_url,
            entity_name="ocean"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"]

        return retVal

    def get_all_ocean_sizing(self, ocean_id, namespace):
        """
        Get all right sizing recommendations for an Ocean cluster
        
        # Returns
        (Object): Ocean API response
        """
        response = self.send_get(
            url=(self.__base_ocean_url +
                 "/" + ocean_id +
                 "/rightSizing/suggestion?namespace={}"
                 ).format(namespace),
            entity_name="ocean"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"]

        return retVal

    def get_ocean_cluster(self, ocean_id):
        """
        Get an exsisting Ocean Cluster json
        
        # Arguments
        ocean_id (String): Ocean id
        
        # Returns
        (Object): Ocean API response 
        """ 
        response = self.send_get(
            url=self.__base_ocean_url +
            "/" + ocean_id,
            entity_name="ocean"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal        
    
    def delete_ocean_cluster(self, ocean_id):
        """
        Delete an Ocean Cluster
        
        # Arguments
        ocean_id (String): Ocean id
        
        # Returns
        (Object): Elastigroup API response 
        """ 
        response = self.send_delete(
            url=self.__base_ocean_url +
            "/" + ocean_id,
            entity_name="ocean"
        )

        return response  

