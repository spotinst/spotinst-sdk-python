import json
from typing import List

from spotinst_sdk2.client import Client
import spotinst_sdk2.models.ocean.aws as aws_ocean
import spotinst_sdk2.models.ocean.azure as azure_ocean
import spotinst_sdk2.models.ocean.gcp as gcp_ocean
import spotinst_sdk2.models.ocean.ecs as ecs_ocean
import spotinst_sdk2.models.ocean.rightsizing as right_sizing_ocean

# region AWS


class OceanAwsClient(Client):
    __base_ocean_cluster_url = "/ocean/aws/k8s/cluster"
    __base_ocean_launchspec_url = "/ocean/aws/k8s/launchSpec"
    __base_ocean_url = "/ocean/k8s/cluster/"
    __base_ocean_extended_resource_definition_url = "/ocean/k8s/extendedResourceDefinition"

    def create_ocean_cluster(self, ocean: aws_ocean.Ocean):
        """
        Create an Ocean Cluster 

        # Arguments
        ocean (Ocean): Ocean Object

        # Returns
        (Object): Ocean API response
        """
        ocean = aws_ocean.OceanRequest(ocean)

        excluded_missing_dict = self.exclude_missing(
            json.loads(ocean.toJSON()))

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

        excluded_missing_dict = self.exclude_missing(
            json.loads(ocean.toJSON()))

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

    def fetch_rightsizing_recommendations(self, ocean_id: str,
                                          filter: aws_ocean.RightSizingRecommendationFilter = None):
        """
        Get right-sizing recommendations for an Ocean cluster and filter them according to namespace or label.

        # Arguments
        ocean_id (String): Id of the Ocean Cluster
        filter (RightSizingRecommendationFilter): Optional - may be null.

        # Returns
        (Object): Ocean API response
        """
        recommendation_request = aws_ocean.RightSizingRecommendationRequest(
            filter)

        excluded_missing_dict = self.exclude_missing(
            json.loads(recommendation_request.toJSON()))

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
        Get an existing Ocean Cluster json

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
        aggregated_cluster_costs_request = aws_ocean.AggregatedClusterCostRequest(
            aggregated_cluster_costs)

        excluded_missing_dict = self.exclude_missing(
            json.loads(aggregated_cluster_costs_request.toJSON()))

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

        excluded_missing_dict = self.exclude_missing(
            json.loads(roll_request.toJSON()))

        formatted_missing_dict = self.convert_json_with_list_of_lists(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        rolls_response = self.send_post(
            body=body_json,
            url=self.__base_ocean_cluster_url + "/" + ocean_id + "/roll",
            entity_name='ocean (Cluster Roll)')

        formatted_response = self.convert_json(
            rolls_response, self.camel_to_underscore)

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

        excluded_missing_dict = self.exclude_missing(
            json.loads(update_roll_request.toJSON()))

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
        query_params = dict(instanceId=instance_id,
                            launchSpecId=launch_spec_id)

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
        group_dict = aws_ocean.InstanceTypesFilterSimulationRequest(
            instance_type_filter)

        excluded_missing_dict = self.exclude_missing(
            json.loads(group_dict.toJSON()))

        formatted_missing_dict = self.convert_json_with_list_of_lists(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        aggregated_costs_response = self.send_post(
            body=body_json,
            url=self.__base_ocean_cluster_url + "/" +
            ocean_id + "/instanceTypeFiltersSimulation",
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
        amount (int): The number of nodes to launch.

        # Returns
        (Object): Ocean Virtual Node Group Launch API response
        """
        launch_node_request = aws_ocean.LaunchNodesRequest(amount)

        excluded_missing_dict = self.exclude_missing(
            json.loads(launch_node_request.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        response = self.send_put(
            body=body_json,
            url=self.__base_ocean_launchspec_url + "/" +
            ocean_launch_spec_id + "/launchNodes",
            entity_name='ocean (Cluster Roll)')

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def fetch_elastilog(self, ocean_id, from_date, to_date, severity=None, resource_id=None, limit=None):
        """
        Create an Ocean configuration according to an AWS autoscaling group (ASG) configuration.

        # Arguments
        to_date (String): to date
        from_date (String): to date
        severity(String) (Optional): Log level severity
        resource_id(String) (Optional): Filter log extracted entires related to a
          specific resource id
        limit(String) (Optional): Maximum number of lines to extract in a response

        # Returns
        (Object): Ocean Get Log API response
        """
        geturl = self.__base_ocean_cluster_url + "/" + ocean_id + "/log"
        query_params = dict(toDate=to_date, fromDate=from_date, severity=severity,
                            resourceId=resource_id, limit=limit)

        result = self.send_get(
            url=geturl, entity_name='ocean_aws_log', query_params=query_params)

        formatted_response = self.convert_json(
            result, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def import_asg_to_ocean_cluster(self, auto_scaling_group_name, region,
                                    import_asg_to_ocean_cluster: aws_ocean.ImportASGToOceanCluster):
        """
        Create an Ocean configuration according to an AWS autoscaling group (ASG) configuration.

        # Arguments
        auto_scaling_group_name (String): The ASG name
        region (String): region
        import_asg_to_ocean_cluster (ImportASGToOceanCluster): ImportASGToOceanCluster Object

        # Returns
        (Object): Ocean Import ASG to Ocean Response
        """
        import_asg_to_ocean_cluster_body = aws_ocean.ImportASGToOceanClusterRequest(
            import_asg_to_ocean_cluster)

        excluded_missing_dict = self.exclude_missing(
            json.loads(import_asg_to_ocean_cluster_body.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        geturl = self.__base_ocean_cluster_url + "/autoScalingGroup/import"

        query_params = dict(
            autoScalingGroupName=auto_scaling_group_name, region=region)

        result = self.send_post_with_params(
            body=body_json,
            url=geturl,
            entity_name='import_asg_to_ocean_cluster',
            user_query_params=query_params)

        formatted_response = self.convert_json(
            result, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def create_virtual_node_group(self, vng: aws_ocean.VirtualNodeGroup, initial_nodes: int = None):
        """
        Create a VNG inside ocean cluster

        # Arguments
        vng (VirtualNodeGroup): VirtualNodeGroup Object
        initial_nodes: When set to an integer greater than 0, a corresponding number of nodes will be launched from the virtual node group created.

        # Returns
        (Object): Ocean Launch Spec response
        """
        ocean = aws_ocean.VNGRequest(vng)

        excluded_missing_dict = self.exclude_missing(
            json.loads(ocean.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        query_params = dict(initialNodes=initial_nodes)

        body_json = json.dumps(formatted_missing_dict)

        response = self.send_post_with_params(
            body=body_json,
            url=self.__base_ocean_launchspec_url,
            entity_name='ocean_aws_vng',
            user_query_params=query_params)

        formatted_response = self.convert_json(response,
                                               self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def update_virtual_node_group(self, vng_id: str, vng: aws_ocean.VirtualNodeGroup, auto_apply_tags: bool = None):
        """
        Update an existing VNG inside an Ocean Cluster 

        # Arguments
        vng_id (String): ID of the Ocean Virtual Node Group
        ocean (Ocean): Ocean object

        # Returns
        (Object): Ocean Launch Spec response
        """
        ocean = aws_ocean.VNGRequest(vng)

        excluded_missing_dict = self.exclude_missing(
            json.loads(ocean.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        response = self.send_put_with_params(
            body=body_json,
            url=self.__base_ocean_launchspec_url + "/" + vng_id,
            entity_name='ocean_aws_vng',
            user_query_params=dict(autoApplyTags=auto_apply_tags))

        formatted_response = self.convert_json(
            response,
            self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_all_virtual_node_groups(self, ocean_id: str = None):
        """
        List the configurations for all virtual node groups in the account
        or in a specified cluster.

        # Returns
        (Object): Ocean Launch Spec response
        """

        response = self.send_get(
            url=self.__base_ocean_launchspec_url,
            entity_name="ocean_aws_vng",
            query_params=dict(oceanId=ocean_id)
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def delete_virtual_node_group(self, vng_id: str, delete_nodes: bool = None, force_delete: bool = None):
        """
        Delete an Ocean Cluster

        # Arguments
        vng_id (String): ID of the Ocean VNG
        delete_nodes (Bool): When set to "true", all instances belonging to the deleted launch specification will be drained, detached, and terminated.
        force_delete (Bool): When set to "true", delete even if it is the only custom launch spec remaining, and default launch spec has useAsTemplateOnly = true.

        # Returns
        (Object): Ocean Launch Specification Delete response
        """
        return self.send_delete_with_params(
            url=self.__base_ocean_launchspec_url + "/" + vng_id,
            entity_name="ocean_aws_vng",
            user_query_params=dict(
                deleteNodes=delete_nodes, forceDelete=force_delete)
        )

    def attach_load_balancers(self, ocean_id: str, load_balancers):
        """
        Add new load balancers to the existing load balancers on the Ocean Cluster.

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        load_balancers (List[LoadBalancer]): Load balancers to add to the Ocean cluster.

        # Returns
        (Object): Ocean Attach Load Balancers API response
        """

        load_balancers = aws_ocean.LoadBalancersRequest(load_balancers)

        excluded_missing_dict = self.exclude_missing(
            json.loads(load_balancers.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        return self.send_put(
            url=self.__base_ocean_cluster_url + "/" + ocean_id + "/loadBalancer/attach",
            entity_name="ocean_aws_attach_load_balancer",
            body=body_json
        )

    def detach_load_balancers(self, ocean_id, load_balancers):
        """
        Delete an Ocean Cluster

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        load_balancers (List[LoadBalancer]): Load balancers to remove from the Ocean cluster.

        # Returns
        (Object): Ocean Detach Load Balancers API response
        """

        load_balancers = aws_ocean.LoadBalancersRequest(load_balancers)

        excluded_missing_dict = self.exclude_missing(
            json.loads(load_balancers.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        return self.send_put(
            url=self.__base_ocean_cluster_url + "/" + ocean_id + "/loadBalancer/detach",
            entity_name="ocean_aws_detach_load_balancer",
            body=body_json
        )

    def update_elastigroup_to_ocean(self, group_id: str):
        """
        Upgrade an Elastigroup with Kubernetes integration to Ocean for Kubernetes cluster. 

        # Arguments
        group_id (str): Elastigroup identifier

        # Returns
        (Object): Ocean API response
        """

        query_params = dict(groupId=group_id)

        response = self.send_post_with_params(
            body=None,
            url=self.__base_ocean_cluster_url + "/import",
            entity_name='ocean_aws_update_eg_to_ocean',
            user_query_params=query_params)

        formatted_response = self.convert_json(response,
                                               self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def detach_instances(self, ocean_id: str, detach_instances: aws_ocean.DetachInstances):
        """
        Detach instances from your Ocean cluster.

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        detach_instances (DetachInstances): Detach Instances Request

        # Returns
        (Object): Detach Instances API response
        """
        detach_instances_request = aws_ocean.DetachInstancesRequest(
            detach_instances)

        excluded_missing_dict = self.exclude_missing(
            json.loads(detach_instances_request.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        detach_instances_response = self.send_put(
            body=body_json,
            url=self.__base_ocean_cluster_url + "/" + ocean_id + "/detachInstances",
            entity_name='ocean_aws_detach_instances)')

        formatted_response = self.convert_json(
            detach_instances_response, self.camel_to_underscore)

        return formatted_response["response"]

    def instance_types_filter_simulation_for_vng(self, launch_spec_id: str,
                                                 instance_types_filters: aws_ocean.InstanceTypesFilters):
        """
        Returns all instance types that match the given filters. These instance types will be used if the Virtual Node Group is configured with these filters.

        # Arguments
        launch_spec_id (String): Ocean cluster launch specification identifier.
        instance_type_filters (InstanceTypesFilters): List of instance types filters. The instance types that match with all filters compose the Virtual Node Group's instanceTypes parameter.
        The architectures that come from the Virtual Node Group's images will be taken into account when using this parameter.
        Cannot be configured together with Virtual Node Group's instanceTypes and with the Cluster's whitelist/blacklist/filters.

        # Returns
        (Object): Ocean Instance Types Filter Simulation response
        """
        group_dict = aws_ocean.InstanceTypesFilterSimulationRequestForVNG(
            instance_types_filters)

        excluded_missing_dict = self.exclude_missing(
            json.loads(group_dict.toJSON()))

        formatted_missing_dict = self.convert_json_with_list_of_lists(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        aggregated_costs_response = self.send_post(
            body=body_json,
            url=self.__base_ocean_launchspec_url + "/" +
            launch_spec_id + "/instanceTypeFiltersSimulation",
            entity_name='ocean_instance_type_filters_simulation_for_vng')

        formatted_response = self.convert_json(
            aggregated_costs_response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def import_asg_to_ocean_vng(self, auto_scaling_group_name, ocean_id: str,
                                import_asg_to_ocean_launch_spec: aws_ocean.ImportASGToOceanVNG):
        """
        Returns an Ocean Virtual Node Group (VNG) configuration in a given AWS autoscaling group (ASG). The returned value ("Imported VNG") can then be used as input to the Create Virtual Node Group API in order to create an actual VNG in your Ocean cluster.

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        auto_scaling_group_name (String): The ASG name.
        import_asg_to_ocean_launch_spec (ImportASGToOceanVNG): ImportASGToOceanVNG object 

        # Returns
        (Object): Ocean Import ASG to Launch Spec Response
        """

        import_asg_to_ocean_launch_spec_body = aws_ocean.ImportASGToOceanVNGRequest(
            import_asg_to_ocean_launch_spec)

        excluded_missing_dict = self.exclude_missing(
            json.loads(import_asg_to_ocean_launch_spec_body.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        query_params = dict(
            autoScalingGroupName=auto_scaling_group_name, oceanId=ocean_id)

        response = self.send_post_with_params(
            body=body_json,
            url=self.__base_ocean_launchspec_url + "/autoScalingGroup/import",
            entity_name="ocean_aws_asg_ocean_vng_import",
            user_query_params=query_params
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def allowed_instance_types_by_filters_for_vng(self, launch_spec_id: str):
        """
        Returns the Virtual Node Group's instance types when instance types filters is set.

        # Arguments
        launch_spec_id (String): Ocean Cluster Launch Specification Identifier

        # Returns
        (Object): Ocean Allowed Instance Types response
        """
        response = self.send_get(
            url=self.__base_ocean_launchspec_url + "/" +
            launch_spec_id + "/allowedInstanceTypesByFilters",
            entity_name="ocean_aws_allowed_instance_types_by_filters_for_vng"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def import_eks_cluster_node_group_to_ocean_vng(self, eks_cluster_name: str, eks_node_group_name: str,
                                                   import_eks_node_group_to_ocean_launch_spec: aws_ocean.ImportEKSNodeGroupToOceanVNG,
                                                   ocean_id: str = None, region: str = None):
        """
        Returns an Ocean Virtual Node Group (VNG) configuration based on a given AWS EKS Cluster Node Group. 
        The returned value ("Imported VNG") can then be used as input to the Create Virtual Node Group API in order to create an actual VNG in your Ocean cluster.

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        eks_cluster_name (String): Cluster name of the EKS cluster.
        eks_node_group_name (String): Node group name to import.
        region (String): Node group name to import.
        import_eks_node_group_to_ocean_launch_spec (ImportEKSNodeGroupToOceanVNG): ImportEKSNodeGroupToOceanVNG object

        # Returns
        (Object): Ocean Import EKS Cluster Node Group to Launch Spec Response
        """

        import_eks_node_group_to_ocean_launch_spec_body = aws_ocean.ImportEKSNodeGroupToOceanVNGRequest(
            import_eks_node_group_to_ocean_launch_spec)

        excluded_missing_dict = self.exclude_missing(json.loads(
            import_eks_node_group_to_ocean_launch_spec_body.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        query_params = dict(eksClusterName=eks_cluster_name,
                            eksNodeGroupName=eks_node_group_name, region=region, oceanId=ocean_id)

        response = self.send_post_with_params(
            body=body_json,
            url=self.__base_ocean_launchspec_url + "/eksNodeGroup/import",
            entity_name="ocean_aws_eks_ocean_vng_import",
            user_query_params=query_params
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def create_migration(self, ocean_id: str, migration: aws_ocean.Migration):
        """
        Create a migration for a given existing instances.

        # Arguments
        migration (Migration): Migration Object

        # Returns
        (Object): Migration create response
        """
        migration = aws_ocean.MigrationRequest(migration)

        excluded_missing_dict = self.exclude_missing(
            json.loads(migration.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        response = self.send_post(
            body=body_json,
            url=self.__base_ocean_cluster_url + "/" + ocean_id + "/migration",
            entity_name='ocean_aws_migration')

        formatted_response = self.convert_json(response,
                                               self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_migration_discovery(self, ocean_id: str, should_fetch_pods: bool):
        """
        Get information about nodes which can be migrated into Ocean.

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        should_fetch_pods (bool): Should fetch data about running pods for each node.

        # Returns
        (Object): Ocean API response
        """
        query_params = dict(shouldFetchPods=should_fetch_pods)

        response = self.send_get(
            url=self.__base_ocean_cluster_url + "/" + ocean_id + "/migration/discovery",
            entity_name="ocean_aws_migration",
            query_params=query_params
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def stop_migration(self, ocean_id: str, migration_id: str, migration: aws_ocean.Migration):
        """
        Stop an ongoing Workload Migration.

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        migration_id (String): The migration identifier of a specific migration
        migration (Migration): Migration Update Configuration

        # Returns
        (Object): Ocean Migration response 
        """

        migration = aws_ocean.MigrationRequest(migration)

        excluded_missing_dict = self.exclude_missing(
            json.loads(migration.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        response = self.send_put(
            body=body_json,
            url=self.__base_ocean_cluster_url + "/" +
            ocean_id + "/migration/" + migration_id,
            entity_name="ocean_aws_migration",
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_migration_status(self, ocean_id: str, migration_id: str):
        """
        Get Migration full info and status for an Ocean cluster.

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        migration_id (String): The migration identifier of a specific migration.

        # Returns
        (Object): Ocean API response 
        """

        response = self.send_get(
            url=self.__base_ocean_cluster_url + "/" +
            ocean_id + "/migration/" + migration_id,
            entity_name="ocean_aws_migration"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_all_migrations_summary(self, ocean_id: str = None):
        """
        Get summary of migrations history for an Ocean cluster.

        # Returns
        (Object): Ocean Migrations response 
        """

        response = self.send_get(
            url=self.__base_ocean_cluster_url + "/" + ocean_id + "/migration",
            entity_name="ocean_aws_migration",
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def create_extended_resource_definition(self, extended_resource_definition: aws_ocean.ExtendedResourceDefinition):
        """
        Creates an Ocean extended resource definition entity

        # Arguments
        extended_resource_definition (ExtendedResourceDefinition): The Ocean extended resource definition

        # Returns
        (Object): Ocean Create Extended Resource Definition response 
        """
        extended_resource_definition = aws_ocean.ExtendedResourceDefinitionRequest(
            extended_resource_definition)

        excluded_missing_dict = self.exclude_missing(
            json.loads(extended_resource_definition.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        response = self.send_post(
            body=body_json,
            url=self.__base_ocean_extended_resource_definition_url,
            entity_name='ocean_aws_extended_resource_defintion')

        formatted_response = self.convert_json(response,
                                               self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_extended_resource_definition(self, ocean_extended_resource_definition_id: str):
        """
        Get Migration full info and status for an Ocean cluster.

        # Arguments
        ocean_extended_resource_definition_id (String): Identifier of the Ocean extended resource definition.

        # Returns
        (Object): Ocean Extended Resource Definition response 
        """

        response = self.send_get(
            url=self.__base_ocean_extended_resource_definition_url +
            "/" + ocean_extended_resource_definition_id,
            entity_name='ocean_aws_extended_resource_defintion'
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_all_extended_resource_definitions(self):
        """
        extended_resource_definition

        # Returns
        (Object): Ocean Extended Resource Defintion response 
        """

        response = self.send_get(
            url=self.__base_ocean_extended_resource_definition_url,
            entity_name="ocean_extended_resource_definition",
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def update_extended_resource_definition(self, ocean_extended_resource_definition_id: str,
                                            extended_resource_definition: aws_ocean.ExtendedResourceDefinition):
        """
        Only the mapping parameter is updatable for extended resource definition

        # Arguments
        ocean_extended_resource_definition_id (String): Identifier of the Ocean extended resource definition.
        extended_resource_definition (ExtendedResourceDefinition): The Ocean extended resource definition

        # Returns
        (Object): Ocean Extended Resource Definition response
        """
        extended_resource_definition = aws_ocean.ExtendedResourceDefinitionRequest(
            extended_resource_definition)

        excluded_missing_dict = self.exclude_missing(
            json.loads(extended_resource_definition.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        response = self.send_put(
            body=body_json,
            url=self.__base_ocean_extended_resource_definition_url +
            "/" + ocean_extended_resource_definition_id,
            entity_name='ocean_extended_resource_defintion')

        formatted_response = self.convert_json(
            response,
            self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def delete_extended_resource_definition(self, ocean_extended_resource_definition_id: str):
        """
        Delete a specified Ocean extended resource definition.

        # Arguments
        ocean_extended_resource_definition_id (String): Identifier of the Ocean extended resource definition.

        # Returns
        (Object): Ocean Delete Extended Resource Definition response
        """
        return self.send_delete(
            url=self.__base_ocean_extended_resource_definition_url +
            "/" + ocean_extended_resource_definition_id,
            entity_name='ocean_extended_resource_defintion')
# endregion


# region Azure
class OceanAzureClient(Client):
    __base_ocean_cluster_url = "/ocean/azure/np/cluster"
    __base_ocean_vng_url = "/ocean/azure/np/virtualNodeGroup"
    __base_ocean_k8s_url = "/ocean/azure/k8s/cluster/"

    def create_ocean_cluster(self, ocean: azure_ocean.Ocean):
        """
        Create an Ocean Cluster 

        # Arguments
        ocean (Ocean): Ocean Object

        # Returns
        (Object): Ocean API response
        """
        ocean = azure_ocean.OceanRequest(ocean)

        excluded_missing_dict = self.exclude_missing(
            json.loads(ocean.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        response = self.send_post(
            body=body_json,
            url=self.__base_ocean_cluster_url,
            entity_name='ocean_aks')

        formatted_response = self.convert_json(response,
                                               self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_all_ocean_clusters(self):
        """
        List the configurations for all Ocean clusters in the specified account.

        # Returns
        (Object): Ocean API response
        """

        response = self.send_get(
            url=self.__base_ocean_cluster_url,
            entity_name="ocean_aks"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def get_ocean_cluster(self, ocean_id: str):
        """
        Get an existing Ocean Cluster json

        # Arguments
        ocean_id (String): ID of the Ocean Cluster

        # Returns
        (Object): Ocean API response
        """
        response = self.send_get(
            url=self.__base_ocean_cluster_url + "/" + ocean_id,
            entity_name="ocean_aks"
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
            entity_name="ocean_aks"
        )

    def update_ocean_cluster(self, ocean_id: str, ocean: azure_ocean.Ocean):
        """
        Update an existing Ocean Cluster 

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        ocean (Ocean): Ocean object

        # Returns
        (Object): Ocean API response
        """
        ocean = azure_ocean.OceanRequest(ocean)

        excluded_missing_dict = self.exclude_missing(
            json.loads(ocean.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        response = self.send_put(
            body=body_json,
            url=self.__base_ocean_cluster_url + "/" + ocean_id,
            entity_name='ocean_aks')

        formatted_response = self.convert_json(
            response,
            self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def import_cluster_configuration(self, aks_cluster_name: str, resource_group_name: str):
        """
        Import cluster configuration of an AKS cluster to use in create_ocean_cluster api call

        # Arguments
        aks_cluster_name (String): Name of the AKS cluster
        resource_group_name (String): Resource Group Name 

        # Returns
        (Object): Ocean API response
        """

        response = self.send_post_with_params(
            body=None,
            url=self.__base_ocean_cluster_url + "/aks/import",
            entity_name='ocean_aks',
            user_query_params=dict(aksClusterName=aks_cluster_name, resourceGroupName=resource_group_name))

        formatted_response = self.convert_json(response,
                                               self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def create_ocean_vng(self, vng: azure_ocean.VirtualNodeGroupTemplate):
        """
        Create a VNG inside ocean cluster

        # Arguments
        vng (VirtualNodeGroup): VirtualNodeGroup Object

        # Returns
        (Object): Ocean API response
        """
        ocean = azure_ocean.VNGRequest(vng)

        excluded_missing_dict = self.exclude_missing(
            json.loads(ocean.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        response = self.send_post(
            body=body_json,
            url=self.__base_ocean_vng_url,
            entity_name='ocean_aks_vng')

        formatted_response = self.convert_json(response,
                                               self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def update_ocean_vng(self, vng_id: str, vng: azure_ocean.VirtualNodeGroupTemplate):
        """
        Update an existing VNG inside an Ocean Cluster 

        # Arguments
        vng_id (String): ID of the Ocean Virtual Node Group
        ocean (Ocean): Ocean object

        # Returns
        (Object): Ocean VNG API response
        """
        ocean = azure_ocean.VNGRequest(vng)

        excluded_missing_dict = self.exclude_missing(
            json.loads(ocean.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        response = self.send_put(
            body=body_json,
            url=self.__base_ocean_vng_url + "/" + vng_id,
            entity_name='ocean_aks_vng')

        formatted_response = self.convert_json(
            response,
            self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_ocean_vng(self, vng_id: str):
        """
        Get an existing Ocean Virtual Node Group json

        # Arguments
        vng_id (String): ID of the Ocean VNG

        # Returns
        (Object): Ocean VNG API response
        """
        response = self.send_get(
            url=self.__base_ocean_vng_url + "/" + vng_id,
            entity_name="ocean_aks_vng"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_all_ocean_vngs(self, ocean_id: str = None):
        """
        List the configurations for all virtual node groups in the account
        or in a specified cluster.

        # Returns
        (Object): Ocean VNG API response
        """

        response = self.send_get(
            url=self.__base_ocean_vng_url,
            entity_name="ocean_aks_vng",
            query_params=dict(oceanId=ocean_id)
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def delete_ocean_vng(self, vng_id: str):
        """
        Delete an Ocean Cluster

        # Arguments
        vng_id (String): ID of the Ocean VNG

        # Returns
        (Object): Ocean VNG API response
        """
        return self.send_delete(
            url=self.__base_ocean_vng_url + "/" + vng_id,
            entity_name="ocean_aks_vng"
        )

    def import_vng_configuration(self, node_pool_name: str, ocean_id: str):
        """
        Import cluster configuration of an AKS cluster to use in create_ocean_cluster api call 

        # Returns
        (Object): Ocean API response
        """

        response = self.send_post_with_params(
            body=None,
            url=self.__base_ocean_vng_url + "/import",
            entity_name='ocean_aks',
            user_query_params=dict(nodePoolName=node_pool_name, oceanId=ocean_id))

        formatted_response = self.convert_json(response,
                                               self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def launch_new_nodes(self, node_config: azure_ocean.LaunchNewNodes):
        """
        Launch new nodes for a cluster

        # Arguments
        node_config (LaunchNewNodes): LaunchNewNodes object

        # Returns
        (Object): Ocean Launch New Nodes API response
        """

        request = azure_ocean.LaunchNewNodesRequest(node_config)

        excluded_missing_dict = self.exclude_missing(
            json.loads(request.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        response = self.send_put(
            body=body_json,
            url=self.__base_ocean_cluster_url + "/launchNewNodes",
            entity_name='ocean_aks')

        formatted_response = self.convert_json(response,
                                               self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_allowed_vng_vm_sizes(self, vng_id: str):
        """
        Get allowed vm sizes for a particular VNG

        # Arguments
        vng_id (String): ID of the Ocean VNG

        # Returns
        (Object): Array of allowed vm sizes list 
        """
        response = self.send_get(
            url=self.__base_ocean_vng_url + "/vmSizes",
            entity_name="ocean_aks_vng",
            query_params=dict(virtualNodeGroupId=vng_id))

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def initiate_roll(self, ocean_id: str, cluster_roll: azure_ocean.Roll):
        """
        Initiate Cluster Rolls

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        cluster_roll (Roll): Cluster Roll / Node Pool names/ VNG Ids

        # Returns
        (Object): Cluster Roll API response
        """
        roll_request = azure_ocean.ClusterRollInitiateRequest(cluster_roll)

        excluded_missing_dict = self.exclude_missing(
            json.loads(roll_request.toJSON()))

        formatted_missing_dict = self.convert_json_with_list_of_lists(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        response = self.send_post(
            body=body_json,
            url=self.__base_ocean_cluster_url + "/" + ocean_id + "/roll",
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

    def stop_roll(self, ocean_id: str, roll_id: str):
        """
        Stop roll of an Ocean cluster.

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        account_id (String): The ID of the account associated with your token.
        roll_id (String): Ocean cluster roll identifier

        # Returns
        (Object): Cluster Roll API response
        """
        response = self.send_put(
            url=self.__base_ocean_cluster_url + "/" +
            ocean_id + "/roll/" + roll_id + "/stop",
            entity_name="ocean (Cluster Roll)"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def create_migration(self, ocean_id: str, migration: azure_ocean.Migration):
        """
        Create a migration for a given existing instances.

        # Arguments
        migration (Migration): Migration Object

        # Returns
        (Object): Migration create response
        """
        migration = azure_ocean.MigrationRequest(migration)

        excluded_missing_dict = self.exclude_missing(
            json.loads(migration.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        response = self.send_post(
            body=body_json,
            url=self.__base_ocean_cluster_url + "/" + ocean_id + "/migration",
            entity_name='ocean_azure_migration')

        formatted_response = self.convert_json(response,
                                               self.camel_to_underscore)

        return formatted_response["response"]

    def get_migration_discovery(self, ocean_id: str, should_fetch_pods: bool):
        """
        Get information about nodes which can be migrated into Ocean.

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        should_fetch_pods (bool): Should fetch data about running pods for each node.

        # Returns
        (Object): Ocean API response
        """
        query_params = dict(shouldFetchPods=should_fetch_pods)

        response = self.send_get(
            url=self.__base_ocean_cluster_url + "/" + ocean_id + "/migration/discovery",
            entity_name="ocean_azure_migration",
            query_params=query_params
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]

    def stop_migration(self, ocean_id: str, migration_id: str):
        """
        Stop an ongoing Workload Migration.

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        migration_id (String): The migration identifier of a specific migration

        # Returns
        (Object): Ocean Migration response 
        """

        response = self.send_put(
            url=self.__base_ocean_cluster_url + "/" +
            ocean_id + "/migration/" + migration_id + "/stop",
            entity_name="ocean_azure_migration",
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]

    def get_migration(self, ocean_id: str, migration_id: str):
        """
        Get Migration full info and status for an Ocean cluster.

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        migration_id (String): The migration identifier of a specific migration.

        # Returns
        (Object): Ocean API response 
        """

        response = self.send_get(
            url=self.__base_ocean_cluster_url + "/" +
            ocean_id + "/migration/" + migration_id,
            entity_name="ocean_azure_migration"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]

    def list_migrations(self, ocean_id: str):
        """
        Get summary of migrations history for an Ocean cluster.

        # Returns
        (Object): Ocean Migrations response 
        """

        response = self.send_get(
            url=self.__base_ocean_cluster_url + "/" + ocean_id + "/migration",
            entity_name="ocean_azure_migration",
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]

    def detach_nodes(self, detach_nodes: azure_ocean.DetachNodes):
        """
        Detach nodes from your Ocean cluster.

        # Arguments
        detach_nodes (DetachNodes): Detach Nodes Object

        # Returns
        (Object): Detach Nodes response
        """
        request = azure_ocean.DetachNodesRequest(detach_nodes)

        excluded_missing_dict = self.exclude_missing(
            json.loads(request.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        response = self.send_put(
            body=body_json,
            url=self.__base_ocean_cluster_url + "/detachNodes",
            entity_name='ocean detach nodes')

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_elastilog(self, ocean_id: str, from_date: str, to_date: str, severity: str = None, resource_id: str = None,
                      limit: int = None):
        """
        Get the log of an Ocean Cluster.

        # Arguments
        to_date (String): end date value
        from_date (String): beginning date value
        severity(String) (Optional): Log level severity
        resource_id(String) (Optional): specific resource identifier
        limit(int) (Optional): Maximum number of lines to extract in a response

        # Returns
        (Object): Ocean Get Log API response
        """
        geturl = self.__base_ocean_cluster_url + "/" + ocean_id + "/log"
        query_params = dict(toDate=to_date, fromDate=from_date, severity=severity,
                            resourceId=resource_id, limit=limit)

        result = self.send_get(
            url=geturl, entity_name='ocean azure elastilog', query_params=query_params)

        formatted_response = self.convert_json(
            result, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def get_aggregated_detailed_costs(self, ocean_id: str, aggregated_cluster_costs: azure_ocean.AggregatedClusterCosts):
        """
        Provides Kubernetes cluster resource usage and costs over a time interval which can be grouped and/or filtered by label/annotaion

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        aggregated_cluster_costs (AggregatedClusterCosts): Aggregated Cluster Costs request

        # Returns
        (Object): Aggregated Cluster Costs API response
        """
        aggregated_cluster_costs_request = azure_ocean.AggregatedClusterCostRequest(
            aggregated_cluster_costs)

        excluded_missing_dict = self.exclude_missing(
            json.loads(aggregated_cluster_costs_request.toJSON()))

        formatted_missing_dict = self.convert_json_with_list_of_lists(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        aggregated_costs_response = self.send_post(
            body=body_json,
            url=self.__base_ocean_k8s_url + ocean_id + "/aggregatedCosts",
            entity_name='ocean (aggregated cluster costs)')

        formatted_response = self.convert_json(
            aggregated_costs_response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_aggregated_summary_costs(self, ocean_id: str, aggregated_cluster_costs: azure_ocean.AggregatedClusterCosts):
        """
        Provides Kubernetes cluster summary usage and costs over a time interval which can be grouped and/or filtered by label/annotaion

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        aggregated_cluster_costs (AggregatedClusterCosts): Aggregated Cluster Costs request

        # Returns
        (Object): Aggregated Cluster Costs API response
        """
        aggregated_cluster_costs_request = azure_ocean.AggregatedClusterCostRequest(
            aggregated_cluster_costs)

        excluded_missing_dict = self.exclude_missing(
            json.loads(aggregated_cluster_costs_request.toJSON()))

        formatted_missing_dict = self.convert_json_with_list_of_lists(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        aggregated_summary_costs_response = self.send_post(
            body=body_json,
            url=self.__base_ocean_k8s_url +
            ocean_id + "/aggregatedCosts/summary",
            entity_name='ocean (aggregated summary costs)')

        formatted_response = self.convert_json(
            aggregated_summary_costs_response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]
# endregion

# region GCP


class OceanGcpClient(Client):
    __base_ocean_url = "/ocean/k8s/cluster/"
    __base_ocean_cluster_url = "/ocean/gcp/k8s/cluster"
    __base_ocean_launchspec_url = "/ocean/gcp/k8s/launchSpec"

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

    def create_ocean_cluster(self, ocean: gcp_ocean.Ocean):
        """
        Create an Ocean Cluster

        # Arguments
        ocean (Ocean): Ocean Object

        # Returns
        (Object): Ocean API response
        """
        ocean = gcp_ocean.OceanRequest(ocean)

        excluded_missing_dict = self.exclude_missing(
            json.loads(ocean.toJSON()))

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

    def get_all_ocean_clusters(self):
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

    def delete_ocean_cluster(self, ocean_id: str):
        """
        Delete a specified Ocean cluster.

        # Arguments
        ocean_id (String): ID of the Ocean Cluster

        # Returns
        (Object): Ocean API response
        """
        return self.send_delete(
            url=self.__base_ocean_cluster_url + "/" + ocean_id,
            entity_name="ocean"
        )

    def get_ocean_cluster(self, ocean_id: str):
        """
        Get the configuration for a specified Ocean cluster.

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

    def update_ocean_cluster(self, ocean_id: str, ocean: gcp_ocean.Ocean):
        """
        Update an existing Ocean Cluster

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        ocean (Ocean): Ocean object

        # Returns
        (Object): Ocean API response
        """
        ocean = gcp_ocean.OceanRequest(ocean)

        excluded_missing_dict = self.exclude_missing(
            json.loads(ocean.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        response = self.send_put(
            body=body_json,
            url=self.__base_ocean_cluster_url + "/" + ocean_id,
            entity_name='ocean')

        formatted_response = self.convert_json(
            response,
            self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def reimport_ocean_cluster(self, ocean_id: str):
        """
        Reimport the cluster's configuration from GKE.

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        ocean (Ocean): Ocean object

        # Returns
        (Object): Reimport cluster response
        """

        response = self.send_put(
            url=self.__base_ocean_cluster_url + "/" + ocean_id + '/reImport',
            entity_name='ocean')

        formatted_response = self.convert_json(
            response,
            self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_elastilog(self, ocean_id: str, from_date: str, to_date: str, severity: str = None, resource_id: str = None,
                      limit: int = None):
        """
        Get group's Elastilog by

        # Arguments
        to_date (String): end date value
        from_date (String): beginning date value
        severity(String) (Optional): Log level severity
        resource_id(String) (Optional): specific resource identifier
        limit(int) (Optional): Maximum number of lines to extract in a response

        # Returns
        (Object): Ocean Get Log API response
        """
        geturl = self.__base_ocean_cluster_url + "/" + ocean_id + "/log"
        query_params = dict(toDate=to_date, fromDate=from_date, severity=severity,
                            resourceId=resource_id, limit=limit)

        result = self.send_get(
            url=geturl, entity_name='ocean_gcp_log', query_params=query_params)

        formatted_response = self.convert_json(
            result, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def get_rightsizing_recommendations(self, ocean_id: str, filter: gcp_ocean.RightSizingRecommendationFilter = None):
        """
        Get right-sizing recommendations for an Ocean cluster and filter them according to namespace or label.

        # Arguments
        ocean_id (String): Id of the Ocean Cluster
        filter (RightSizingRecommendationFilter): Optional - may be null.

        # Returns
        (Object): Ocean API response
        """
        recommendation_request = gcp_ocean.RightSizingRecommendationRequest(
            filter)

        excluded_missing_dict = self.exclude_missing(
            json.loads(recommendation_request.toJSON()))

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

    def get_aggregated_cluster_costs(self, ocean_id: str, aggregated_cluster_costs: gcp_ocean.AggregatedClusterCosts):
        """
        Get aggregated cluster costs

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        aggregated_cluster_costs (AggregatedClusterCosts): Aggregated Cluster Costs request

        # Returns
        (Object): Aggregated Cluster Costs API response
        """
        aggregated_cluster_costs_request = gcp_ocean.AggregatedClusterCostRequest(
            aggregated_cluster_costs)

        excluded_missing_dict = self.exclude_missing(
            json.loads(aggregated_cluster_costs_request.toJSON()))

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

    def get_aggregated_summary_costs(self, ocean_id: str, aggregated_cluster_costs: gcp_ocean.AggregatedClusterCosts):
        """
        Get aggregated cluster costs

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        aggregated_cluster_costs (AggregatedClusterCosts): Aggregated Cluster Costs request

        # Returns
        (Object): Aggregated Cluster Costs API response
        """
        aggregated_cluster_costs_request = gcp_ocean.AggregatedClusterCostRequest(
            aggregated_cluster_costs)

        excluded_missing_dict = self.exclude_missing(
            json.loads(aggregated_cluster_costs_request.toJSON()))

        formatted_missing_dict = self.convert_json_with_list_of_lists(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        aggregated_summary_costs_response = self.send_post(
            body=body_json,
            url=self.__base_ocean_cluster_url + "/" +
            ocean_id + "/aggregatedCosts/summary",
            entity_name='ocean (aggregated summary costs)')

        formatted_response = self.convert_json(
            aggregated_summary_costs_response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def create_virtual_node_group(self, vng: gcp_ocean.VirtualNodeGroup, initial_nodes: int = None):
        """
        Create a virtual node group.

        # Arguments
        vng (VirtualNodeGroup): VirtualNodeGroup Object
        initial_nodes: When set to an integer greater than 0, a corresponding number of nodes will be launched from the virtual node group created.

        # Returns
        (Object): Ocean Launch Spec response
        """
        ocean = gcp_ocean.VNGRequest(vng)

        excluded_missing_dict = self.exclude_missing(
            json.loads(ocean.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        query_params = dict(initialNodes=initial_nodes)

        response = self.send_post_with_params(
            body=body_json,
            url=self.__base_ocean_launchspec_url,
            entity_name='ocean_gcp_vng',
            user_query_params=query_params)

        formatted_response = self.convert_json(response,
                                               self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_all_virtual_node_groups(self, ocean_id: str):
        """
        List the configurations for all virtual node groups in the account
        or in a specified cluster.

        # Returns
        (Object): Ocean VNG API response
        """

        response = self.send_get(
            url=self.__base_ocean_launchspec_url,
            entity_name="ocean_gcp_vng",
            query_params=dict(oceanId=ocean_id)
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def import_gke_nodepool_to_vng_configuration(self, node_pool_name: str, ocean_id: str):
        """
        Import GKE Nodepool configurations and generate valid Ocean Virtual Node Group (VNG) configuration
        which can be used to create VNGs

        # Returns
        (Object): Ocean API response
        """

        response = self.send_post_with_params(
            body=None,
            url=self.__base_ocean_launchspec_url + "/import",
            entity_name='ocean_gcp_vng',
            user_query_params=dict(nodePoolName=node_pool_name, oceanId=ocean_id))

        formatted_response = self.convert_json(response,
                                               self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def delete_virtual_node_group(self, vng_id: str, delete_nodes: bool = None):
        """
        Delete an Ocean Cluster

        # Arguments
        vng_id (String): ID of the Ocean VNG
        delete_nodes (Bool): When set to "true", all instances belonging to the deleted launch specification will be drained, detached, and terminated.

        # Returns
        (Object): Ocean Launch Specification Delete response
        """
        return self.send_delete_with_params(
            url=self.__base_ocean_launchspec_url + "/" + vng_id,
            entity_name="ocean_gcp_vng",
            user_query_params=dict(deleteNodes=delete_nodes)
        )

    def update_virtual_node_group(self, vng_id: str, vng: gcp_ocean.VirtualNodeGroup):
        """
        Update an existing VNG inside an Ocean Cluster

        # Arguments
        vng_id (String): ID of the Ocean Virtual Node Group
        ocean (Ocean): Ocean object

        # Returns
        (Object): Ocean Launch Spec response
        """
        ocean = gcp_ocean.VNGRequest(vng)

        excluded_missing_dict = self.exclude_missing(
            json.loads(ocean.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        response = self.send_put(
            body=body_json,
            url=self.__base_ocean_launchspec_url + "/" + vng_id,
            entity_name='ocean_gcp_vng')

        formatted_response = self.convert_json(
            response,
            self.camel_to_underscore)

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
            entity_name="ocean_gcp_vng"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def initiate_roll(self, ocean_id: str, cluster_roll: gcp_ocean.Roll):
        """
        Initiate Cluster Rolls

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        cluster_roll (Roll): Cluster Roll / Roll with Instance Ids/ Launch specification Ids

        # Returns
        (Object): Cluster Roll API response
        """
        roll_request = gcp_ocean.ClusterRollInitiateRequest(cluster_roll)

        excluded_missing_dict = self.exclude_missing(
            json.loads(roll_request.toJSON()))

        formatted_missing_dict = self.convert_json_with_list_of_lists(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        rolls_response = self.send_post(
            body=body_json,
            url=self.__base_ocean_cluster_url + "/" + ocean_id + "/roll",
            entity_name='ocean (Cluster Roll)')

        formatted_response = self.convert_json(
            rolls_response, self.camel_to_underscore)

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
        update_roll_request = gcp_ocean.ClusterRollUpdateRequest(status)

        excluded_missing_dict = self.exclude_missing(
            json.loads(update_roll_request.toJSON()))

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

    def get_cluster_nodes(self, ocean_id: str, instance_name: str = None, launch_spec_id: str = None):
        """
        Get nodes data of an Ocean cluster.

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        instance_name (String): Get a specific node by instance id
        launch_spec_id (String): Ocean cluster launch specification identifier.

        # Returns
        (Object): Ocean Kubernetes AWS Nodes Data response
        """
        query_params = dict(instanceName=instance_name,
                            launchSpecId=launch_spec_id)

        response = self.send_get(
            url=self.__base_ocean_cluster_url + "/" + ocean_id + "/nodes",
            entity_name="ocean (Cluster Nodes)",
            query_params=query_params
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def update_elastigroup_to_ocean(self, group_id: str):
        """
        Upgrade an Elastigroup with Kubernetes integration to Ocean for Kubernetes cluster.

        # Arguments
        group_id (str): Elastigroup identifier

        # Returns
        (Object): Ocean API response
        """

        query_params = dict(groupId=group_id)

        response = self.send_post_with_params(
            body=None,
            url=self.__base_ocean_cluster_url + "/import",
            entity_name='ocean_gcp_update_eg_to_ocean',
            user_query_params=query_params)

        formatted_response = self.convert_json(response,
                                               self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def import_gke_cluster_to_ocean(self, cluster_name: str, location: str,
                                    import_gke_to_ocean: gcp_ocean.ImportGkeClusterToOcean,
                                    include_launchSpecs: bool = None, node_pool_name: str = None):
        """
        Create an Ocean configuration according to an GKE Cluster configuration.

        # Arguments
        cluster_name (String): Name of the GKE Cluster.
        include_launchSpecs (String): When set to "true", GKE cluster node pools will be imported to Ocean custom VNG ("customLaunchSpec") configurations.
        location (String): Location GKE Cluster Master.
        node_pool_name (String): Name of the Node Pool to use as a default for the Cluster configuration.
        import_gke_to_ocean (ImportGkeClusterToOcean): ImportGkeClusterToOcean Object

        # Returns
        (Object): Ocean GKE Cluster Import Response
        """
        import_gke_to_ocean_body = gcp_ocean.ImportGkeClusterToOceanRequest(
            import_gke_to_ocean)

        excluded_missing_dict = self.exclude_missing(
            json.loads(import_gke_to_ocean_body.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        geturl = self.__base_ocean_cluster_url + "/gke/import"

        query_params = dict(
            clusterName=cluster_name, includeLaunchSpecs=include_launchSpecs, location=location,
            nodePoolName=node_pool_name)

        result = self.send_post_with_params(
            body=body_json,
            url=geturl,
            entity_name='import_gke_cluster_to_ocean',
            user_query_params=query_params)

        formatted_response = self.convert_json(
            result, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def launch_nodes_in_vng(self, ocean_launch_spec_id: str, amount: int):
        """
        Launch nodes in Virtual Node Group.

        # Arguments
        ocean_launch_spec_id (String): Ocean cluster launch specification identifier.
        amount (int): The number of nodes to launch.

        # Returns
        (Object): Ocean Virtual Node Group Launch API response
        """
        launch_node_request = gcp_ocean.LaunchNodesRequest(amount)

        excluded_missing_dict = self.exclude_missing(
            json.loads(launch_node_request.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        response = self.send_put(
            body=body_json,
            url=self.__base_ocean_launchspec_url + "/" +
            ocean_launch_spec_id + "/launchNodes",
            entity_name='ocean (Cluster Roll)')

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def detach_instances(self, ocean_id: str, detach_configuration: gcp_ocean.DetachInstancesConfig):
        """
        Detach instances from your Ocean cluster.

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        detach_configuration (DetachInstancesConfig): Detach instances request

        # Returns
        (Object): Detach Instance response
        """
        request = gcp_ocean.DetachInstancesRequest(
            detach_config=detach_configuration)

        excluded_missing_dict = self.exclude_missing(
            json.loads(request.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        response = self.send_put(
            body=body_json,
            url=self.__base_ocean_cluster_url + "/" + ocean_id + "/detachInstances",
            entity_name='ocean gcp detach instances')

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]

    def instance_types_filters_simulation(self, ocean_id: str, filters: gcp_ocean.InstanceTypesFilters):
        """
        Returns all instances types that match the given filters.
        These instance types will be used if the cluster is configured with these filters.

        # Arguments
        ocean_id (String): Id of the Ocean Cluster
        filters (InstanceTypesFilters): List of filters

        # Returns
        (Object): Ocean Instance Type Simultion response
        """
        request = gcp_ocean.InstanceTypesFilterRequest(filters)

        excluded_missing_dict = self.exclude_missing(
            json.loads(request.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        group_response = self.send_post(
            body=body_json,
            url=self.__base_ocean_cluster_url +
            "/" + ocean_id + "/instanceTypeFiltersSimulation",
            entity_name='ocean gcp')

        formatted_response = self.convert_json(
            group_response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

# endregion

# region RightSizing


class OceanRightSizingClient(Client):

    def create_right_sizing_rule(self, ocean_id: str, rule_name: str,
                                 application_intervals: List[right_sizing_ocean.RecommendationApplicationInterval],
                                 restart_replicas: right_sizing_ocean.RestartReplicas = None,
                                 exclude_preliminary_recommendations: bool = None,
                                 application_min_threshold: right_sizing_ocean.RecommendationApplicationMinThreshold = None,
                                 application_boundaries: right_sizing_ocean.RecommendationApplicationBoundaries = None,
                                 application_overhead_values: right_sizing_ocean.RecommendationApplicationOverheadValues = None,
                                 application_hpa: right_sizing_ocean.RecommendationApplicationHPA = None):
        """
        Create a right sizing rule for an Ocean cluster.

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        rule_name (String): Name of the Right Sizing Rule
        restart_replicas (RestartReplicas): Restart Replicas
        exclude_preliminary_recommendations (boolean): Exclude preliminary recommendations
        application_intervals (List[RecommendationApplicationIntervals]): Recommendation Application Intervals
        application_min_threshold (RecommendationApplicationMinThreshold): Recommendation Application Min Threshold
        application_boundaries (RecommendationApplicationBoundaries): Recommendation Application Boundaries
        application_overhead_values (RecommendationApplicationOverheadValues): Recommendation Application Overhead Values
        application_hpa (RecommendationApplicationHPA): Recommendation Application HPA

        # Returns
        (Object): Ocean Right Sizing Rule API response

        """
        right_sizing_rule_request = right_sizing_ocean.CreateRightSizingRuleRequest(rule_name=rule_name,
                                                                                    restart_replicas=restart_replicas,
                                                                                    exclude_preliminary_recommendations=exclude_preliminary_recommendations,
                                                                                    recommendation_application_intervals=application_intervals,
                                                                                    recommendation_application_min_threshold=application_min_threshold,
                                                                                    recommendation_application_boundaries=application_boundaries,
                                                                                    recommendation_application_overhead_values=application_overhead_values,
                                                                                    recommendation_application_hpa=application_hpa)

        excluded_missing_dict = self.exclude_missing(
            json.loads(right_sizing_rule_request.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        response = self.send_post(
            body=body_json,
            url="/ocean/"+ocean_id+"/rightSizing/rule",
            entity_name='right_sizing')

        formatted_response = self.convert_json(response,
                                               self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def delete_right_sizing_rule(self, ocean_id: str, rule_names: List[str]):
        """
        Delete a right sizing rule for an Ocean cluster.

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        rule_names (List[String]): List of Right Sizing Rule Names

        # Returns
        (Object): Ocean Right Sizing Rule API response
        """

        right_sizing_rule_request = right_sizing_ocean.DeleteRightSizingRulesRequest(
            rule_names)

        excluded_missing_dict = self.exclude_missing(
            json.loads(right_sizing_rule_request.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        return self.send_delete_with_body(
            body=body_json,
            url="/ocean/"+ocean_id+"/rightSizing/rule",
            entity_name='right_sizing')

    def update_right_sizing_rule(self, ocean_id: str,
                                 rule_name: str,
                                 application_intervals: List[right_sizing_ocean.RecommendationApplicationInterval],
                                 restart_replicas: right_sizing_ocean.RestartReplicas = None,
                                 exclude_preliminary_recommendations: bool = None,
                                 application_min_threshold: right_sizing_ocean.RecommendationApplicationMinThreshold = None,
                                 application_boundaries: right_sizing_ocean.RecommendationApplicationBoundaries = None,
                                 application_overhead_values: right_sizing_ocean.RecommendationApplicationOverheadValues = None,
                                 application_hpa: right_sizing_ocean.RecommendationApplicationHPA = None):
        """
        Update a right sizing rule for an Ocean cluster.

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        rule_name (String): Rightsizing Rule name
        restart_replicas (RestartReplicas): Restart Replicas
        exclude_preliminary_recommendations (boolean): Exclude preliminary recommendations
        application_intervals (RecommendationApplicationIntervals): Recommendation Application Intervals
        application_min_threshold (RecommendationApplicationMinThreshold): Recommendation Application Min Threshold
        application_boundaries (RecommendationApplicationBoundaries): Recommendation Application Boundaries
        application_overhead_values (RecommendationApplicationOverheadValues): Recommendation Application Overhead Values
        application_hpa (RecommendationApplicationHPA): Recommendation Application HPA

        # Returns
        (Object): Ocean Right Sizing Rule API response
        """
        right_sizing_rule_request = right_sizing_ocean.UpdateRightSizingRuleRequest(restart_replicas=restart_replicas,
                                                                                    exclude_preliminary_recommendations=exclude_preliminary_recommendations,
                                                                                    recommendation_application_intervals=application_intervals,
                                                                                    recommendation_application_min_threshold=application_min_threshold,
                                                                                    recommendation_application_boundaries=application_boundaries,
                                                                                    recommendation_application_overhead_values=application_overhead_values,
                                                                                    recommendation_application_hpa=application_hpa)

        excluded_missing_dict = self.exclude_missing(
            json.loads(right_sizing_rule_request.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        response = self.send_put(
            body=body_json,
            url="/ocean/"+ocean_id+"/rightSizing/rule/" + rule_name,
            entity_name='right_sizing')

        formatted_response = self.convert_json(response,
                                               self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def attach_right_sizing_rule(self, ocean_id: str, rule_name: str, namespaces: List[right_sizing_ocean.Namespace]):
        """
        Attach right sizing rule to an Ocean cluster.

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        rule_name (String): Ocean right sizing rule
        namespaces (List[Namespace]): List of namespaces to attach the right sizing rule to

        # Returns
        (Object): Ocean Right Sizing Rule API response
        """
        attach_right_sizing_rule_request = right_sizing_ocean.AttachRightSizingRuleRequest(
            namespaces)

        excluded_missing_dict = self.exclude_missing(
            json.loads(attach_right_sizing_rule_request.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        response = self.send_post(
            body=body_json,
            url="/ocean/"+ocean_id+"/rightSizing/rule/"+rule_name+"/attachment",
            entity_name='right_sizing')

        formatted_response = self.convert_json(response,
                                               self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def detach_right_sizing_rule(self, ocean_id: str, rule_name: str, namespaces: List[right_sizing_ocean.Namespace]):
        """
        Detach right sizing rule from an Ocean cluster.

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        rule_name (String): Ocean right sizing rule
        namespaces (List[Namespace]): List of namespaces to detach the right sizing rule from

        # Returns
        (Object): Ocean Right Sizing Rule API response
        """
        detach_right_sizing_rule_request = right_sizing_ocean.DetachRightSizingRuleRequest(
            namespaces)

        excluded_missing_dict = self.exclude_missing(
            json.loads(detach_right_sizing_rule_request.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        response = self.send_post(
            body=body_json,
            url="/ocean/"+ocean_id+"/rightSizing/rule/"+rule_name+"/detachment",
            entity_name='right_sizing')

        formatted_response = self.convert_json(response,
                                               self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_right_sizing_rule(self, ocean_id: str, rule_name: str):
        """
        Get right sizing rule for an Ocean cluster.

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        rule_name (String): Name of the Right Sizing Rule

        # Returns
        (Object): Ocean Right Sizing Rule API response
        """
        response = self.send_get(
            url="/ocean/"+ocean_id+"/rightSizing/rule/"+rule_name,
            entity_name="right_sizing"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def list_right_sizing_rules(self, ocean_id: str):
        """
        Get right sizing rule for an Ocean cluster.

        # Arguments
        ocean_id (String): ID of the Ocean Cluster


        # Returns
        (Object): Ocean Right Sizing Rules API response
        """
        response = self.send_get(
            url="/ocean/"+ocean_id+"/rightSizing/rule/",
            entity_name="right_sizing"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def get_ocean_right_sizing_recommendations(self, ocean_id: str, cluster_resources: right_sizing_ocean.ClusterResources = None, cluster_labels: right_sizing_ocean.ClusterLabels = None):
        """
        Attach right sizing rule to an Ocean cluster.

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        cluster_resources (ClusterResources): Cluster Resources
        cluster_labels (ClusterLabels): Cluster Labels

        # Returns
        (Object): Ocean Right Sizing Rule API response
        """
        get_ocean_right_sizing_recommendations_request = right_sizing_ocean.GetOceanRightSizingRecommendationsRequest(
            cluster_resources=cluster_resources, cluster_labels=cluster_labels)

        excluded_missing_dict = self.exclude_missing(
            json.loads(get_ocean_right_sizing_recommendations_request.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        response = self.send_post(
            body=body_json,
            url="/ocean/"+ocean_id+"/rightSizing/recommendations",
            entity_name='right_sizing')

        formatted_response = self.convert_json(response,
                                               self.camel_to_underscore)

        return formatted_response["response"]["items"]

# endregion

# region OceanEcs


class OceanEcsClient(Client):
    __base_ocean_url = "/ocean/aws/ecs/cluster"
    __base_launch_spec_url = "/ocean/aws/ecs/launchSpec"

    def get_all_ocean_clusters(self):
        """
        Get the configurations for all Ocean ECS clusters in the specified account.

        # Returns
        (Object): Ocean ECS API response
        """

        response = self.send_get(
            url=self.__base_ocean_url,
            entity_name="ocean ecs"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def create_ocean_cluster(self, ocean: ecs_ocean.Ocean):
        """
        Create an Ocean ECS Cluster

        # Arguments
        ocean (Ocean): Ocean ECS Object

        # Returns
        (Object): Ocean ECS API response
        """
        ocean = ecs_ocean.OceanRequest(ocean)

        excluded_missing_dict = self.exclude_missing(
            json.loads(ocean.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        response = self.send_post(
            body=body_json,
            url=self.__base_ocean_url,
            entity_name='ocean ecs')

        formatted_response = self.convert_json(response,
                                               self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_ocean_cluster(self, ocean_id: str):
        """
        Get the configuration for a specified Ocean cluster.

        # Arguments
        ocean_id (String): ID of the Ocean Cluster

        # Returns
        (Object): Ocean API response
        """
        response = self.send_get(
            url=self.__base_ocean_url + "/" + ocean_id,
            entity_name="ocean ecs"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def update_ocean_cluster(self, ocean_id: str, ocean: ecs_ocean.Ocean):
        """
        Update an existing Ocean Cluster

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        ocean (Ocean): Ocean object

        # Returns
        (Object): Ocean API response
        """
        ocean = ecs_ocean.OceanRequest(ocean)

        excluded_missing_dict = self.exclude_missing(
            json.loads(ocean.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        response = self.send_put(
            body=body_json,
            url=self.__base_ocean_url + "/" + ocean_id,
            entity_name='ocean ecs')

        formatted_response = self.convert_json(
            response,
            self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def delete_ocean_cluster(self, ocean_id: str):
        """
        Delete a specified Ocean cluster.

        # Arguments
        ocean_id (String): ID of the Ocean Cluster

        # Returns
        (Object): Ocean API response
        """
        return self.send_delete(
            url=self.__base_ocean_url + "/" + ocean_id,
            entity_name="ocean ecs"
        )

    def import_ocean_cluster(self, ecs_cluster_name: str, import_cluster_config: ecs_ocean.ImportClusterConfig):
        """
        Create an Ocean ECS Cluster

        # Arguments
        ecs_cluster_name (String): Name of the existing ECS Cluster to import 
        import_cluster_config (ImportClusterConfig): Import Cluster Object

        # Returns
        (Object): Ocean ECS API response
        """
        ocean = ecs_ocean.ImportClusterRequest(
            import_cluster_config=import_cluster_config)

        excluded_missing_dict = self.exclude_missing(
            json.loads(ocean.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        response = self.send_post(
            body=body_json,
            url=self.__base_ocean_url + "/" + ecs_cluster_name + "/import",
            entity_name='ocean ecs')

        formatted_response = self.convert_json(response,
                                               self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_elastilog(self, ocean_id: str, from_date: str, to_date: str, severity: str = None, resource_id: str = None,
                      limit: int = None):
        """
        Get the log of an Ocean Cluster.

        # Arguments
        ocean_id (String): Ocean cluster identifier
        to_date (String): end date value
        from_date (String): beginning date value
        severity (String) (Optional): Log level severity
        resource_id (String) (Optional): specific resource identifier
        limit(int) (Optional): Maximum number of lines to extract in a response

        # Returns
        (Object): Ocean Get Log API response
        """
        geturl = self.__base_ocean_url + "/" + ocean_id + "/log"
        query_params = dict(toDate=to_date, fromDate=from_date, severity=severity,
                            resourceId=resource_id, limit=limit)

        result = self.send_get(
            url=geturl, entity_name='ocean ecs', query_params=query_params)

        formatted_response = self.convert_json(
            result, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def instance_types_filters_simulation(self, ocean_id: str, filters: ecs_ocean.InstanceTypesFilters):
        """
        Returns all instances types that match the given filters.
        These instance types will be used if the cluster is configured with these filters.

        # Arguments
        ocean_id (String): Id of the Ocean Cluster
        filters (InstanceTypesFilters): List of filters

        # Returns
        (Object): Ocean Instance Type Simultion response
        """
        request = ecs_ocean.InstanceTypesFilterRequest(filters)

        excluded_missing_dict = self.exclude_missing(
            json.loads(request.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        group_response = self.send_post(
            body=body_json,
            url=self.__base_ocean_url +
            "/" + ocean_id + "/instanceTypeFiltersSimulation",
            entity_name='ocean ecs')

        formatted_response = self.convert_json(
            group_response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def get_allowed_instance_types(self, ocean_id: str):
        """
        Return the list of the allowed Ocean cluster instance types.

        # Arguments
        ocean_id (String): Ocean cluster identifier

        # Returns
        (Object): Ocean Allowed Instance Types response
        """
        response = self.send_get(
            url=self.__base_ocean_url + "/" + ocean_id + "/allowedInstanceTypes",
            entity_name="ocean ecs"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def upgrade_elastigroup_to_ocean(self, group_id: str):
        """
        Upgrade an Elastigroup with ECS integration into Ocean for ECS cluster.

        # Arguments
        group_id (String): Elastigroup ID

        # Returns
        (Object): Ocean ECS API response
        """
        query_params = dict(groupId=group_id)

        response = self.send_post_with_params(
            url=self.__base_ocean_url + "/import",
            entity_name='ocean ecs',
            body=None,
            user_query_params=query_params)

        formatted_response = self.convert_json(response,
                                               self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def initiate_roll(self, ocean_id: str, roll_config: ecs_ocean.RollConfig):
        """
        Initiate Cluster Rolls

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        roll_config (RollConfig): Cluster Roll / Roll with Instance Ids/ Roll with VNG Ids

        # Returns
        (Object): Cluster Roll API response
        """
        roll_request = ecs_ocean.ClusterRollInitiateRequest(roll_config)

        excluded_missing_dict = self.exclude_missing(
            json.loads(roll_request.toJSON()))

        formatted_missing_dict = self.convert_json_with_list_of_lists(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        rolls_response = self.send_post(
            body=body_json,
            url=self.__base_ocean_url + "/" + ocean_id + "/roll",
            entity_name='ocean ecs (Cluster Roll)')

        formatted_response = self.convert_json(
            rolls_response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def list_rolls(self, ocean_id: str):
        """
        List rolls of an Ocean cluster.

        # Arguments
        ocean_id (String): ID of the Ocean Cluster

        # Returns
        (Object): List of Cluster Roll API response
        """
        response = self.send_get(
            url=self.__base_ocean_url + "/" + ocean_id + "/roll",
            entity_name="ocean ecs (Cluster Roll)"
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
        status (String): update roll status request

        # Returns
        (Object): Cluster Roll API response
        """
        update_roll_request = ecs_ocean.ClusterRollUpdateRequest(status)

        excluded_missing_dict = self.exclude_missing(
            json.loads(update_roll_request.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        response = self.send_put(
            body=body_json,
            url=self.__base_ocean_url + "/" + ocean_id + "/roll/" + roll_id,
            entity_name='ocean ecs (Cluster Roll)')

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_roll(self, ocean_id: str, roll_id: str):
        """
        Get status for a roll of an Ocean cluster.

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        roll_id (String): Ocean cluster roll identifier

        # Returns
        (Object): Cluster Roll API response
        """
        response = self.send_get(
            url=self.__base_ocean_url + "/" + ocean_id + "/roll/" + roll_id,
            entity_name="ocean ecs (Cluster Roll)"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_cluster_container_instances(self, ocean_id: str, instance_id: str = None, launch_spec_id: str = None):
        """
        Get container instances data of an Ocean cluster.

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        instance_id (String): Instance identifier
        launch_spec_id (String): Ocean cluster VNG identifier.

        # Returns
        (Object): Ocean Aws Container Instances Data Response
        """
        query_params = dict(instanceId=instance_id,
                            launchSpecId=launch_spec_id)

        response = self.send_get(
            url=self.__base_ocean_url + "/" + ocean_id + "/containerInstances",
            query_params=query_params,
            entity_name="ocean ecs instances"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def detach_instances(self, ocean_id: str, detach_configuration: ecs_ocean.DetachInstancesConfig):
        """
        Detach instances from your Ocean cluster.

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        detach_configuration (DetachInstancesConfig): Detach instances request

        # Returns
        (Object): Detach Instance response
        """
        request = ecs_ocean.DetachInstancesRequest(
            detach_config=detach_configuration)

        excluded_missing_dict = self.exclude_missing(
            json.loads(request.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        response = self.send_put(
            body=body_json,
            url=self.__base_ocean_url + "/" + ocean_id + "/detachInstances",
            entity_name='ocean ecs detach instances')

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]

    def create_virtual_node_group(self, vng: ecs_ocean.VirtualNodeGroup):
        """
        Create a new Ocean ECS virtual node group in the specified account.

        # Arguments
        vng (VirtualNodeGroup): VirtualNodeGroup Object

        # Returns
        (Object): Ocean Virtual Node Group API response
        """
        ocean = ecs_ocean.VNGRequest(vng)

        excluded_missing_dict = self.exclude_missing(
            json.loads(ocean.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        response = self.send_post(
            body=body_json,
            url=self.__base_launch_spec_url,
            entity_name='ocean ecs vng')

        formatted_response = self.convert_json(response,
                                               self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_all_virtual_node_groups(self, ocean_id: str):
        """
        Get all VNGs for the specified Ocean cluster.

        # Returns
        (Object): Ocean Virtual Node Group API response
        """

        response = self.send_get(
            url=self.__base_launch_spec_url,
            entity_name="ocean ecs vng",
            query_params=dict(oceanId=ocean_id)
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def delete_virtual_node_group(self, vng_id: str, delete_container_instances: bool = None):
        """
        Delete a specified virtual node group in an Ocean cluster.

        # Arguments
        vng_id (String): Ocean cluster Virtual Node Group identifier.
        delete_container_instances (Bool): When set to "true", all instances belonging to the deleted VNG will be drained, detached, and terminated.

        # Returns
        (Object): Ocean Virtual Node Group Delete response
        """
        return self.send_delete_with_params(
            url=self.__base_launch_spec_url + "/" + vng_id,
            entity_name="ocean ecs vng",
            user_query_params=dict(
                deleteContainerInstances=delete_container_instances)
        )

    def update_virtual_node_group(self, vng_id: str, vng: ecs_ocean.VirtualNodeGroup):
        """
        Update specified VNG for an Ocean cluster.

        # Arguments
        vng_id (String): ID of the Ocean Virtual Node Group
        vng (VirtualNodeGroup): VirtualNodeGroup Object

        # Returns
        (Object): Ocean Virtual Node Group API response
        """
        ocean = ecs_ocean.VNGRequest(vng)

        excluded_missing_dict = self.exclude_missing(
            json.loads(ocean.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        response = self.send_put(
            body=body_json,
            url=self.__base_launch_spec_url + "/" + vng_id,
            entity_name='ocean ecs vng')

        formatted_response = self.convert_json(
            response,
            self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_virtual_node_group(self, vng_id: str):
        """
        Get a specified VNG for an Ocean cluster.

        # Arguments
        vng_id (String): Ocean cluster Virtual Node Group identifier.

        # Returns
        (Object): Ocean Virtual Node Group API response
        """
        response = self.send_get(
            url=self.__base_launch_spec_url + "/" + vng_id,
            entity_name="ocean ecs vng"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def import_fargate_to_existing_ocean_cluster(self, ocean_id: str,
                                                 import_fargate_existing: ecs_ocean.ImportFargateToExistingOceanCluster):
        """
        Import a Fargate service into an existing Ocean ECS cluster.

        # Arguments
        ocean_id (String): Ocean cluster Identifier
        import_fargate_existing (Object): ImportFargateToExistingOceanCluster Object

        # Returns
        (Object): Ocean ECS Fargate Response
        """
        ocean = ecs_ocean.ImportFargateToExistingOceanClusterRequest(
            import_config=import_fargate_existing)

        excluded_missing_dict = self.exclude_missing(
            json.loads(ocean.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        response = self.send_post(
            body=body_json,
            url=self.__base_ocean_url + ocean_id + "/fargateMigration",
            entity_name='ocean ecs fargate')

        formatted_response = self.convert_json(response,
                                               self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_fargate_services_discovery(self, ocean_id: str):
        """
        Get existing Fargate services in the ECS cluster.

        # Arguments
        ocean_id (String): Ocean cluster identifier

        # Returns
        (Object): Ocean ECS Fargate Response
        """
        response = self.send_get(
            url=self.__base_ocean_url + "/" + ocean_id +
            "/fargateMigration/serviceDiscovery",
            entity_name="ocean ecs fargate"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def get_fargate_migration_status(self, ocean_id: str):
        """
        Get the status of a Fargate service import.

        # Arguments
        ocean_id (String): Ocean cluster identifier

        # Returns
        (Object): Ocean ECS Fargate Response
        """
        response = self.send_get(
            url=self.__base_ocean_url + "/" + ocean_id + "/fargateMigration/status",
            entity_name="ocean ecs fargate"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def import_fargate_to_new_ocean_cluster(self, import_fargate_new: ecs_ocean.ImportFargateToNewOceanCluster):
        """
        Import a Fargate service into a new Ocean ECS cluster.

        # Arguments
        ocean_id (String): Ocean cluster Identifier
        import_fargate_new (Object): ImportFargateToNewOceanCluster Object

        # Returns
        (Object): Ocean ECS Fargate Response
        """
        ocean = ecs_ocean.ImportFargateToNewOceanClusterRequest(
            import_config=import_fargate_new)

        excluded_missing_dict = self.exclude_missing(
            json.loads(ocean.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        response = self.send_post(
            body=body_json,
            url=self.__base_ocean_url + "/fargate/import",
            entity_name='ocean ecs fargate')

        formatted_response = self.convert_json(response,
                                               self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def launch_instances_in_vng(self, vng_id: str, amount: int):
        """
        Launch container instances in virtual node group.

        # Arguments
        vng_id (String): Ocean cluster Virtual Node Group identifier.
        amount (int): The number of nodes to launch.

        # Returns
        (Object): Ocean Virtual Node Group Launch API response
        """
        launch_node_request = ecs_ocean.LaunchInstancesRequest(amount)

        excluded_missing_dict = self.exclude_missing(
            json.loads(launch_node_request.toJSON()))

        formatted_missing_dict = self.convert_json(
            excluded_missing_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_missing_dict)

        response = self.send_put(
            body=body_json,
            url=self.__base_launch_spec_url + "/" +
            vng_id + "/launchContainerInstances",
            entity_name='ocean ecs vng')

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

# endregion
