import json

from spotinst_sdk2.client import Client
import spotinst_sdk2.models.ocean.aws as aws_ocean


class OceanAwsClient(Client):
    __base_ocean_url = "/ocean/aws/k8s/cluster"
    __base_ocean_url1 = "/ocean/aws/k8s/launchSpec"

    def create_ocean_cluster(self, ocean: aws_ocean.Ocean, account_id: str):
        """
        Create an Ocean Cluster 
        
        # Arguments
        ocean (Ocean): Ocean Object
        account_id (String): The ID of the account associated with your token.
        
        # Returns
        (Object): Ocean API response 
        """
        ocean = aws_ocean.OceanRequest(ocean)
        query_params = dict(accountId=account_id)

        excluded_group_dict = self.exclude_missing(json.loads(ocean.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        group_response = self.send_post(
            body=body_json,
            url=self.__base_ocean_url,
            entity_name='ocean',
            query_params=query_params)

        formatted_response = self.convert_json(
            group_response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def update_ocean_cluster(self, ocean_id: str, account_id: str, ocean: aws_ocean.Ocean, auto_apply_tagsocean: str = "false"):
        """
        Update an exsisting Ocean Cluster 
        
        # Arguments
        ocean_id (String): Ocean id
        account_id (String): The ID of the account associated with your token.
        auto_apply_tagsocean (String): Option to update instance tags on the fly without rolling the cluster.
        ocean (Ocean): Ocean object
        
        # Returns
        (Object): Ocean API response 
        """
        ocean = aws_ocean.OceanRequest(ocean)

        excluded_group_dict = self.exclude_missing(json.loads(ocean.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)
        query_params = dict(accountId=account_id, autoApplyTags=auto_apply_tagsocean)

        group_response = self.send_put(
            body=body_json,
            url=self.__base_ocean_url + "/" + ocean_id,
            entity_name='ocean',
            query_params=query_params)

        formatted_response = self.convert_json(
            group_response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_all_ocean_cluster(self, account_id: str):
        """
        List the configurations for all Ocean clusters in the specified account.
        
        # Returns
        (Object): Ocean API response 
        """

        query_params = dict(accountId=account_id)
        response = self.send_get(
            url=self.__base_ocean_url,
            entity_name="ocean",
            query_params=query_params
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def get_all_ocean_sizing(self, ocean_id: str, account_id: str, filter: aws_ocean.RightSizingRecommendationFilter):
        """
        Get all right sizing recommendations for an Ocean cluster

        # Arguments
        ocean_id (String): Id of the ocean cluster
        account_id (String): The ID of the account associated with your token.
        filter (RightSizingRecommendationFilter): Optional - may be null.
        
        # Returns
        (Object): Ocean API response
        """
        group_dict = aws_ocean.RightSizingRecommendationRequest(filter)

        excluded_group_dict = self.exclude_missing(json.loads(group_dict.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        query_params = dict(accountId=account_id)
        body_json = json.dumps(formatted_group_dict)

        group_response = self.send_post(
            body=body_json,
            url=self.__base_ocean_url + "/" + ocean_id + "/rightSizing/suggestion",
            entity_name='ocean',
            query_params=query_params)

        formatted_response = self.convert_json(
            group_response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def fetch_rightsizing_recommendations(self, ocean_id: str, account_id: str, filter: aws_ocean.RightSizingRecommendationFilter = None):
        """
        Get right-sizing recommendations for an Ocean cluster and filter them according to namespace or label.

        # Arguments
        ocean_id (String): Id of the ocean cluster
        account_id (String): The ID of the account associated with your token.
        filter (RightSizingRecommendationFilter): Optional - may be null.

        # Returns
        (Object): Ocean API response
        """
        group_dict = aws_ocean.RightSizingRecommendationRequest(filter)

        excluded_group_dict = self.exclude_missing(json.loads(group_dict.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        query_params = dict(accountId=account_id)
        body_json = json.dumps(formatted_group_dict)

        group_response = self.send_post(
            body=body_json,
            url=self.__base_ocean_url +
            "/" + ocean_id + "/rightSizing/suggestion",
            entity_name='ocean',
            query_params=query_params)

        formatted_response = self.convert_json(
            group_response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def get_ocean_cluster(self, ocean_id: str, account_id: str):
        """
        Get an exsisting Ocean Cluster json

        # Arguments
        ocean_id (String): Ocean id
        account_id (String): The ID of the account associated with your token.

        # Returns
        (Object): Ocean API response 
        """
        query_params = dict(account_id=account_id)
        response = self.send_get(
            url=self.__base_ocean_url + "/" + ocean_id,
            entity_name="ocean",
            query_params=query_params
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def delete_ocean_cluster(self, ocean_id: str, account_id: str):
        """
        Delete an Ocean Cluster

        # Arguments
        ocean_id (String): Ocean id
        account_id (String): The ID of the account associated with your token.

        # Returns
        (Object): Ocean API response
        """
        query_params = dict(account_id=account_id)
        return self.send_delete(
            url=self.__base_ocean_url + "/" + ocean_id,
            entity_name="ocean",
            query_params=query_params
        )

    def get_aggregated_cluster_costs(self, ocean_id: str, account_id: str, aggregated_cluster_costs: aws_ocean.AggregatedClusterCosts):
        """
        Get aggregated cluster costs

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        account_id (String): The ID of the account associated with your token.
        aggregated_cluster_costs (AggregatedClusterCosts): Aggregated Cluster Costs request

        # Returns
        (Object): Aggregated Cluster Costs API response
        """
        aggregated_cluster_costs_request = aws_ocean.AggregatedClusterCostRequest(aggregated_cluster_costs)

        excluded_aggregated_costs_dict = self.exclude_missing(json.loads(aggregated_cluster_costs_request.toJSON()))

        formatted_aggregated_costs_dict = self.convert_json_with_list_of_lists(
            excluded_aggregated_costs_dict, self.underscore_to_camel)

        query_params = dict(account_id=account_id)
        body_json = json.dumps(formatted_aggregated_costs_dict)

        aggregated_costs_response = self.send_post(
            body=body_json,
            url=self.__base_ocean_url + "/" + ocean_id + "/aggregatedCosts",
            entity_name='ocean (aggregated cluster costs)',
            query_params=query_params)

        formatted_response = self.convert_json(
            aggregated_costs_response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def initiate_roll(self, ocean_id: str, account_id: str, cluster_roll: aws_ocean.Roll):
        """
        Initiate Cluster Rolls

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        account_id (String): The ID of the account associated with your token.
        cluster_roll (Roll): Roll with Instance Ids/ Launch specification Ids / None

        # Returns
        (Object): Cluster Roll API response
        """
        group_dict = aws_ocean.ClusterRollInitiateRequest(cluster_roll)

        excluded_aggregated_costs_dict = self.exclude_missing(json.loads(group_dict.toJSON()))

        formatted_aggregated_costs_dict = self.convert_json_with_list_of_lists(
            excluded_aggregated_costs_dict, self.underscore_to_camel)

        query_params = dict(account_id=account_id)
        body_json = json.dumps(formatted_aggregated_costs_dict)

        aggregated_costs_response = self.send_post(
            body=body_json,
            url=self.__base_ocean_url + "/" + ocean_id + "/roll",
            entity_name='ocean (Cluster Roll)',
            query_params=query_params)

        formatted_response = self.convert_json(
            aggregated_costs_response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def list_rolls(self, ocean_id: str, account_id: str):
        """
        Get status for all rolls of an Ocean cluster.

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        account_id (String): The ID of the account associated with your token.

        # Returns
        (Object): List of Cluster Roll API response
        """
        query_params = dict(accountId=account_id)
        response = self.send_get(
            url=self.__base_ocean_url + "/" + ocean_id + "/roll",
            entity_name="ocean (Cluster Roll)",
            query_params=query_params
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def update_roll(self, ocean_id: str, account_id: str, roll_id: str, update_roll: aws_ocean.UpdateRoll):
        """
        Update a roll of an Ocean cluster.
        Performing the request will stop the next batch in a roll.

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        account_id (String): The ID of the account associated with your token.
        roll_id (String): Ocean cluster roll identifier
        update_roll (UpdateRoll): update roll request

        # Returns
        (Object): Cluster Roll API response
        """
        group_dict = aws_ocean.ClusterRollUpdateRequest(update_roll)

        excluded_group_dict = self.exclude_missing(json.loads(group_dict.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)
        query_params = dict(accountId=account_id)

        group_response = self.send_put(
            body=body_json,
            url=self.__base_ocean_url + "/" + ocean_id + "/roll/" + roll_id,
            entity_name='ocean (Cluster Roll)',
            query_params=query_params)

        formatted_response = self.convert_json(
            group_response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_roll(self, ocean_id: str, account_id: str, roll_id: str):
        """
        Get status for a roll of an Ocean cluster.

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        account_id (String): The ID of the account associated with your token.
        roll_id (String): Ocean cluster roll identifier

        # Returns
        (Object): Cluster Roll API response
        """
        query_params = dict(accountId=account_id)
        response = self.send_get(
            url=self.__base_ocean_url + "/" + ocean_id + "/roll/" + roll_id,
            entity_name="ocean (Cluster Roll)",
            query_params=query_params
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_cluster_nodes(self, ocean_id: str, account_id: str, instance_id: str, launch_spec_id: str):
        """
        Get nodes data of an Ocean cluster.

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        account_id (String): The ID of the account associated with your token.
        instance_id (String): Get a specific node by instance id
        launch_spec_id (String): Ocean cluster launch specification identifier.

        # Returns
        (Object): Ocean Kubernetes AWS Nodes Data response
        """
        query_params = dict(accountId=account_id, instance_id=instance_id, launch_spec_id=launch_spec_id)
        response = self.send_get(
            url=self.__base_ocean_url + "/" + ocean_id + "/nodes",
            entity_name="ocean (Cluster Nodes)",
            query_params=query_params
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def get_heartbeat_status(self, ocean_id: str, account_id: str):
        """
        Get the heartbeat status of the Ocean Controller for the cluster.
        The response returns the heartbeat status and the last heartbeat timestamp.

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        account_id (String): The ID of the account associated with your token.

        # Returns
        (Object): Ocean Get Heartbeat response
        """
        query_params = dict(accountId=account_id)
        response = self.send_get(
            url=self.__base_ocean_url + "/" + ocean_id + "/controllerHeartbeat",
            entity_name="ocean (Cluster Heartbeat)",
            query_params=query_params
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def instance_types_filter_simulation(self, ocean_id: str, account_id: str,
                                         instance_type_filter: aws_ocean.InstanceTypesFilters):
        """
        Returns all instances types that match the given filters.
        These instance types will be used if the cluster is configured with these filters.

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        account_id (String): The ID of the account associated with your token.
        instance_type_filter (InstanceTypesFilters): The Instance types that match with all filters compose the
        Ocean's whitelist parameter. Cannot be configured together with whitelist/blacklist.

        # Returns
        (Object): Ocean Instance Types Filter Simulation response
        """
        group_dict = aws_ocean.InstanceTypesFilterSimulationRequest(instance_type_filter)

        excluded_aggregated_costs_dict = self.exclude_missing(json.loads(group_dict.toJSON()))

        formatted_aggregated_costs_dict = self.convert_json_with_list_of_lists(
            excluded_aggregated_costs_dict, self.underscore_to_camel)

        query_params = dict(account_id=account_id)
        body_json = json.dumps(formatted_aggregated_costs_dict)

        aggregated_costs_response = self.send_post(
            body=body_json,
            url=self.__base_ocean_url + "/" + ocean_id + "/instanceTypeFiltersSimulation",
            entity_name='ocean',
            query_params=query_params)

        formatted_response = self.convert_json(
            aggregated_costs_response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def allow_instance_types(self, ocean_id: str, account_id: str):
        """
        Return the list of the allowed Ocean cluster instance types.

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        account_id (String): The ID of the account associated with your token.

        # Returns
        (Object): Ocean Allowed Instance Types response
        """
        query_params = dict(accountId=account_id)
        response = self.send_get(
            url=self.__base_ocean_url + "/" + ocean_id + "/allowedInstanceTypes",
            entity_name="ocean",
            query_params=query_params
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_virtual_node_group(self, ocean_launch_spec_id: str, account_id: str):
        """
        Get Virtual Node Group of the cluster

        # Arguments
        ocean_launch_spec_id (String): Ocean cluster launch specification identifier
        account_id (String): The ID of the account associated with your token.

        # Returns
        (Object): Ocean Allowed Instance Types response
        """
        query_params = dict(accountId=account_id)
        response = self.send_get(
            url=self.__base_ocean_url1 + "/" + ocean_launch_spec_id,
            entity_name="ocean",
            query_params=query_params
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def launch_nodes_in_vng(self, ocean_launch_spec_id: str, account_id: str, launch_nodes: aws_ocean.LaunchNodes):
        """
        Launch nodes in Virtual Node Group.

        # Arguments
        ocean_launch_spec_id (String): Ocean cluster launch specification identifier.
        account_id (String): The ID of the account associated with your token.
        launch_nodes (LaunchNodes): Object specifying the details for the launch request.

        # Returns
        (Object): Ocean Virtual Node Group Launch API response
        """
        group_dict = aws_ocean.LaunchNodesRequest(launch_nodes)

        excluded_group_dict = self.exclude_missing(json.loads(group_dict.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)
        query_params = dict(accountId=account_id)

        group_response = self.send_put(
            body=body_json,
            url=self.__base_ocean_url1 + "/" + ocean_launch_spec_id + "/launchNodes",
            entity_name='ocean (Cluster Roll)',
            query_params=query_params)

        formatted_response = self.convert_json(
            group_response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]
