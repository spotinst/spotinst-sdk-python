import json

from spotinst_sdk2.client import Client

import spotinst_sdk2.models.hpc.aws as aws_hpc


class HPCAwsClient(Client):
    __base_hpc_url = "/hpc/aws/lsf/cluster"

    def create_hpc_cluster(self, cluster: aws_hpc.HPC):
        """
        Create an hpc cluster

        # Arguments
        group (HPCCluster): HPCCluster Object

        # Returns
        (Object): HPCCluster API response 
        """
        cluster = aws_hpc.LSFClusterCreationRequest(cluster)

        excluded_cluster_dict = self.exclude_missing(
            json.loads(cluster.toJSON()))

        formatted_cluster_dict = self.convert_json(
            excluded_cluster_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_cluster_dict)

        cluster_response = self.send_post(
            body=body_json,
            url=self.__base_hpc_url,
            entity_name='hpc_cluster')

        formatted_response = self.convert_json(
            cluster_response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def delete_hpc_cluster(self, cluster_id: str):
        """
        Delete a hpc cluster

        # Arguments
        group_id (String): Cluster ID

        # Returns
        (Object): HPC Cluster API response 
        """
        delurl = self.__base_hpc_url + "/" + cluster_id
        return self.send_delete(url=delurl, entity_name='hpc_cluster')

    def get_hpc_cluster(self, cluster_id: str):
        """
        Get an hpc cluster

        # Arguments
        group_id(String): Cluster ID

        # Returns
        (Object): HPC Cluster API response 
        """
        geturl = self.__base_hpc_url + "/" + cluster_id
        result = self.send_get(url=geturl, entity_name='hpc_cluster')

        formatted_response = self.convert_json(
            result, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_all_hpc_clusters(self):
        """
        Get all hpc clusters
        # Returns
        (List): List of HPC Cluster API response
        """
        content = self.send_get(
            url=self.__base_hpc_url,
            entity_name='hpc_cluster')
        formatted_response = self.convert_json(
            content, self.camel_to_underscore)
        return formatted_response["response"]["items"]

    def update_hpc_cluster(self, hpc_cluster_update: aws_hpc.HPC, cluster_id: str):
        """
        Update hpc cluster
        # Arguments
        cluster_id (String): Cluster ID
        hpc_cluster_update (HPC Cluster): HPC Cluster Object

        # Returns
        (Object): HPC Cluster API response
        """
        cluster = aws_hpc.LSFClusterUpdateRequest(hpc_cluster_update)

        excluded_cluster_update_dict = self.exclude_missing(
            json.loads(cluster.toJSON()))

        formatted_cluster_update_dict = self.convert_json(
            excluded_cluster_update_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_cluster_update_dict)

        cluster_response = self.send_put(
            body=body_json,
            url=self.__base_hpc_url + "/" + cluster_id,
            entity_name='hpc_cluster'
        )

        formatted_response = self.convert_json(
            cluster_response, self.camel_to_underscore)

        ret_val = formatted_response["response"]["items"][0]

        return ret_val
