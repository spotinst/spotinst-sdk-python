import json
from typing import List

from spotinst_sdk2.client import Client
import spotinst_sdk2.models.ocean.aws as aws_ocean
import spotinst_sdk2.models.ocean.azure as azure_ocean

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

    def fetch_rightsizing_recommendations(self, ocean_id: str, filter: aws_ocean.RightSizingRecommendationFilter = None):
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

    def import_asg_to_ocean_cluster(self, auto_scaling_group_name, region, import_asg_to_ocean_cluster: aws_ocean.ImportASGToOceanCluster):
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

    def delete_virtual_node_group(self, vng_id: str, delete_nodes: bool=None, force_delete: bool=None):
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
            user_query_params=dict(deleteNodes=delete_nodes, forceDelete=force_delete)
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
            url=self.__base_ocean_cluster_url+"/import",
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

    def import_asg_to_ocean_vng(self, auto_scaling_group_name, ocean_id: str, import_asg_to_ocean_launch_spec: aws_ocean.ImportASGToOceanVNG):
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

    def import_eks_cluster_node_group_to_ocean_vng(self, eks_cluster_name: str, eks_node_group_name: str, import_eks_node_group_to_ocean_launch_spec: aws_ocean.ImportEKSNodeGroupToOceanVNG,  ocean_id: str = None, region: str = None):
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
            url=self.__base_ocean_cluster_url+"/"+ocean_id+"/migration",
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
            url=self.__base_ocean_cluster_url+"/"+ocean_id+"/migration/discovery",
            entity_name="ocean_aws_migration",
            query_params=query_params
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def stop_migration(self, ocean_id: str, migration_id: str, migration: aws_ocean.Migration):
        """
        Stop an ongoing Workload Migration.

        # Arguments
        ocean_id (String): ID of the Ocean Cluster
        migration_id (bool): The migration identifier of a specific migration
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
            url=self.__base_ocean_cluster_url+"/"+ocean_id+"/migration/"+migration_id,
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
            url=self.__base_ocean_cluster_url+"/"+ocean_id+"/migration/"+migration_id,
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
            url=self.__base_ocean_cluster_url+"/"+ocean_id+"/migration",
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
            "/"+ocean_extended_resource_definition_id,
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

    def update_extended_resource_definition(self, ocean_extended_resource_definition_id: str, extended_resource_definition: aws_ocean.ExtendedResourceDefinition):
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
            url=self.__base_ocean_cluster_url+"/aks/import",
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
            url=self.__base_ocean_vng_url+"/import",
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
            url=self.__base_ocean_cluster_url+"/launchNewNodes",
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
    # endregion
