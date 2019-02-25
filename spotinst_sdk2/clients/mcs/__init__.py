import json

from spotinst_sdk2.client import Client

class McsClient(Client):
    __base_kube_url = "https://api.spotinst.io/mcs/kubernetes/cluster"

    def get_kubernetes_cluster_cost(self, custer_id, from_date, to_date):   
        """
        Get kubernetes cluster cost 
        
        # Arguments
        custer_id (String): Kubernetes cluster id
        from_date (String): From date
        to_date (String): to date
        
        # Returns
        (Object): Elastigroup API response 
        """      
        geturl = self.__base_kube_url + "/" + custer_id + "/costs"
        query_params = self.build_query_params_with_input({"toDate":to_date, "fromDate":from_date})

        result = self.send_get(url=geturl, query_params=query_params, entity_name='kubernetes')

        formatted_response = self.convert_json(
            result, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]
