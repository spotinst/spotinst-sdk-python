import json

from spotinst_sdk2.client import Client
import spotinst_sdk2.models.ocean.aws as aws_ocean


class OceanAwsClient(Client):
    __base_ocean_cluster_url = "/ocean/aws/k8s/cluster"
    __base_ocean_launchspec_url = "/ocean/aws/k8s/launchSpec"
    __base_ocean_url = "/ocean/k8s/cluster/"

    def create_ocean_cluster(self, ocean: aws_ocean.Ocean):
        """
        Create an Ocean Cluster 
        
        # Arguments
        ocean (Ocean): Ocean Object

        # Returns
        (Object): Ocean API response 
        """
        ocean = aws_ocean.OceanRequest(ocean)

        excluded_missing_dict = self.exclude_missing(json.loads(ocean.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        response = self.send_post(
            body=body_json,
            url=self.__base_ocean_cluster_url,
            entity_name='ocean')

        formatted_response = self.convert_json(response, 
                                               self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def update_ocean_cluster(self, ocean_id: str, ocean: aws_ocean.Ocean, auto_apply_tags: str = None):
        """
        Update an existing Ocean Cluster 
        
        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        auto_apply_tags (String): Option to update instance tags on the fly without rolling the cluster.
        ocean (Ocean): Ocean object
        
        # Returns
        (Object): Ocean API response 
        """
        ocean = aws_ocean.OceanRequest(ocean)

        excluded_missing_dict = self.exclude_missing(json.loads(ocean.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        response = self.send_put_with_params(
            body=body_json,
            url=self.__base_ocean_cluster_url + "/" + ocean_id,
            entity_name='ocean',
            user_query_params=dict(autoApplyTags=auto_apply_tags))

        formatted_response = self.convert_json(
            response,
            self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_all_ocean_cluster(self):
        """
        List the configurations for all Ocean clusters in the specified account.
        
        # Returns
        (Object): Ocean API response 
        """

        response = self.send_get(
            url=self.__base_ocean_cluster_url,
            entity_name="ocean"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def get_all_ocean_sizing(self, ocean_id: str, namespace: str):
        """
        Get all right sizing recommendations for an Ocean cluster

        # Returns
        (Object): Ocean API response
        """
        response = self.send_get(
            url=(self.__base_ocean_cluster_url +
                 "/" + ocean_id +
                 "/rightSizing/suggestion?namespace={}"
                 ).format(namespace),
            entity_name="ocean"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def fetch_rightsizing_recommendations(self, ocean_id: str, filter: aws_ocean.RightSizingRecommendationFilter = None):
        """
        Get right-sizing recommendations for an Ocean cluster and filter them according to namespace or label.

        # Arguments
        ocean_id (String): Id of the Ocean Cluster
        filter (RightSizingRecommendationFilter): Optional - may be null.

        # Returns
        (Object): Ocean API response
        """
        recommendation_request = aws_ocean.RightSizingRecommendationRequest(filter)

        excluded_missing_dict = self.exclude_missing(json.loads(recommendation_request.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        group_response = self.send_post(
            body=body_json,
            url=self.__base_ocean_cluster_url +
            "/" + ocean_id + "/rightSizing/suggestion",
            entity_name='ocean')

        formatted_response = self.convert_json(
            group_response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def get_ocean_cluster(self, ocean_id: str):
        """
        Get an exsisting Ocean Cluster json

        # Arguments
        ocean_id (String): ID of the Ocean Cluster

        # Returns
        (Object): Ocean API response 
        """
        response = self.send_get(
            url=self.__base_ocean_cluster_url + "/" + ocean_id,
            entity_name="ocean"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def delete_ocean_cluster(self, ocean_id: str):
        """
        Delete an Ocean Cluster

        # Arguments
        ocean_id (String): ID of the Ocean Cluster

        # Returns
        (Object): Ocean API response
        """
        return self.send_delete(
            url=self.__base_ocean_cluster_url + "/" + ocean_id,
            entity_name="ocean"
        )

    def get_aggregated_cluster_costs(self, ocean_id: str, aggregated_cluster_costs: aws_ocean.AggregatedClusterCosts):
        """
        Get aggregated cluster costs

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        aggregated_cluster_costs (AggregatedClusterCosts): Aggregated Cluster Costs request

        # Returns
        (Object): Aggregated Cluster Costs API response
        """
        aggregated_cluster_costs_request = aws_ocean.AggregatedClusterCostRequest(aggregated_cluster_costs)

        excluded_missing_dict = self.exclude_missing(json.loads(aggregated_cluster_costs_request.toJSON()))

        formatted_missing_dict = self.convert_json_with_list_of_lists(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        aggregated_costs_response = self.send_post(
            body=body_json,
            url=self.__base_ocean_cluster_url + "/" + ocean_id + "/aggregatedCosts",
            entity_name='ocean (aggregated cluster costs)')

        formatted_response = self.convert_json(
            aggregated_costs_response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def initiate_roll(self, ocean_id: str, cluster_roll: aws_ocean.Roll):
        """
        Initiate Cluster Rolls

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        cluster_roll (Roll): Cluster Roll / Roll with Instance Ids/ Launch specification Ids

        # Returns
        (Object): Cluster Roll API response
        """
        roll_request = aws_ocean.ClusterRollInitiateRequest(cluster_roll)

        excluded_missing_dict = self.exclude_missing(json.loads(roll_request.toJSON()))

        formatted_missing_dict = self.convert_json_with_list_of_lists(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        aggregated_costs_response = self.send_post(
            body=body_json,
            url=self.__base_ocean_cluster_url + "/" + ocean_id + "/roll",
            entity_name='ocean (Cluster Roll)')

        formatted_response = self.convert_json(
            aggregated_costs_response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def list_rolls(self, ocean_id: str):
        """
        Get status for all rolls of an Ocean cluster.

        # Arguments
        ocean_id (String): ID of the Ocean Cluster

        # Returns
        (Object): List of Cluster Roll API response
        """
        response = self.send_get(
            url=self.__base_ocean_cluster_url + "/" + ocean_id + "/roll",
            entity_name="ocean (Cluster Roll)"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def update_roll(self, ocean_id: str, roll_id: str, status: str):
        """
        Update a roll of an Ocean cluster.
        Performing the request will stop the next batch in a roll.

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        roll_id (String): Ocean cluster roll identifier
        update_roll (UpdateRoll): update roll request

        # Returns
        (Object): Cluster Roll API response
        """
        update_roll_request = aws_ocean.ClusterRollUpdateRequest(status)

        excluded_missing_dict = self.exclude_missing(json.loads(update_roll_request.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        response = self.send_put(
            body=body_json,
            url=self.__base_ocean_cluster_url + "/" + ocean_id + "/roll/" + roll_id,
            entity_name='ocean (Cluster Roll)')

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_roll(self, ocean_id: str, roll_id: str):
        """
        Get status for a roll of an Ocean cluster.

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        account_id (String): The ID of the account associated with your token.
        roll_id (String): Ocean cluster roll identifier

        # Returns
        (Object): Cluster Roll API response
        """
        response = self.send_get(
            url=self.__base_ocean_cluster_url + "/" + ocean_id + "/roll/" + roll_id,
            entity_name="ocean (Cluster Roll)"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_cluster_nodes(self, ocean_id: str, instance_id: str = None, launch_spec_id: str = None):
        """
        Get nodes data of an Ocean cluster.

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        instance_id (String): Get a specific node by instance id
        launch_spec_id (String): Ocean cluster launch specification identifier.

        # Returns
        (Object): Ocean Kubernetes AWS Nodes Data response
        """
        query_params = dict(instanceId = instance_id, launchSpecId = launch_spec_id)
        
        response = self.send_get(
            url=self.__base_ocean_cluster_url + "/" + ocean_id + "/nodes",
            entity_name="ocean (Cluster Nodes)",
            query_params=query_params
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def get_heartbeat_status(self, ocean_id: str):
        """
        Get the heartbeat status of the Ocean Controller for the cluster.
        The response returns the heartbeat status and the last heartbeat timestamp.

        # Arguments
        ocean_id (String): ID of the Ocean Cluster

        # Returns
        (Object): Ocean Get Heartbeat response
        """
        response = self.send_get(
            url=self.__base_ocean_url + ocean_id + "/controllerHeartbeat",
            entity_name="ocean (Cluster Heartbeat)"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def instance_types_filter_simulation(self, ocean_id: str,
                                         instance_type_filter: aws_ocean.InstanceTypesFilters):
        """
        Returns all instances types that match the given filters.
        These instance types will be used if the cluster is configured with these filters.

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        instance_type_filter (InstanceTypesFilters): The Instance types that match with all filters compose the
        Ocean's whitelist parameter. Cannot be configured together with whitelist/blacklist.

        # Returns
        (Object): Ocean Instance Types Filter Simulation response
        """
        group_dict = aws_ocean.InstanceTypesFilterSimulationRequest(instance_type_filter)

        excluded_missing_dict = self.exclude_missing(json.loads(group_dict.toJSON()))

        formatted_missing_dict = self.convert_json_with_list_of_lists(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        aggregated_costs_response = self.send_post(
            body=body_json,
            url=self.__base_ocean_cluster_url + "/" + ocean_id + "/instanceTypeFiltersSimulation",
            entity_name='ocean')

        formatted_response = self.convert_json(
            aggregated_costs_response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def allowed_instance_types(self, ocean_id: str):
        """
        Return the list of the allowed Ocean cluster instance types.

        # Arguments
        ocean_id (String): ID of the Ocean Cluster

        # Returns
        (Object): Ocean Allowed Instance Types response
        """
        response = self.send_get(
            url=self.__base_ocean_cluster_url + "/" + ocean_id + "/allowedInstanceTypes",
            entity_name="ocean"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_virtual_node_group(self, ocean_launch_spec_id: str):
        """
        Get Virtual Node Group of the cluster

        # Arguments
        ocean_launch_spec_id (String): Ocean cluster launch specification identifier

        # Returns
        (Object): Ocean Allowed Instance Types response
        """
        response = self.send_get(
            url=self.__base_ocean_launchspec_url + "/" + ocean_launch_spec_id,
            entity_name="ocean"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def launch_nodes_in_vng(self, ocean_launch_spec_id: str, amount: int):
        """
        Launch nodes in Virtual Node Group.

        # Arguments
        ocean_launch_spec_id (String): Ocean cluster launch specification identifier.
        launch_nodes (LaunchNodes): Object specifying the details for the launch request.

        # Returns
        (Object): Ocean Virtual Node Group Launch API response
        """
        launch_node_request = aws_ocean.LaunchNodesRequest(amount)

        excluded_missing_dict = self.exclude_missing(json.loads(launch_node_request.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        response = self.send_put(
            body=body_json,
            url=self.__base_ocean_launchspec_url + "/" + ocean_launch_spec_id + "/launchNodes",
            entity_name='ocean (Cluster Roll)')

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]
