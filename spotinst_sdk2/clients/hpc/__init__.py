import json

from spotinst_sdk2.client import Client

# region AWS imports
import spotinst_sdk2.models.hpc.aws as aws_hpc
# endregion


# region AWS


class HPCAwsClient(Client):
    __base_hpc_url = "/hpc/aws/lsf/cluster"
    __base_aws_url = "/hpc/aws/lsf"

 # endregion

    # region HPCCluster
    def create_hpc_cluster(self, cluster:aws_hpc.HPC, async_scale=None):
        """
        Create an hpc cluster

        # Arguments
        group (HPCCluster): HPCCluster Object

        # Returns
        (Object): HPCCluster API response 
        """
        cluster = aws_hpc.HPCClusterCreationRequest(cluster)

        excluded_cluster_dict = self.exclude_missing(json.loads(cluster.toJSON()))

        formatted_cluster_dict = self.convert_json(
            excluded_cluster_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_cluster_dict)

        cluster_response = self.send_post_with_params(
            body=body_json,
            url=self.__base_hpc_url,
            entity_name='hpc_cluster',
            user_query_params=dict(asyncScale=async_scale))

        formatted_response = self.convert_json(
            cluster_response, self.camel_to_underscore)

        ret_val = formatted_response["response"]["items"][0]

        return ret_val
    
    # endregion
