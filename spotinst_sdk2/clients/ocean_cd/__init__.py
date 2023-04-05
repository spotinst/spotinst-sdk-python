import json

from spotinst_sdk2.client import Client
import spotinst_sdk2.models.ocean_cd as oceancd_cluster
import spotinst_sdk2.models.ocean_cd.verification_provider as oceancd_vp
import spotinst_sdk2.models.ocean_cd.verification_template as oceancd_vt
import spotinst_sdk2.models.ocean_cd.strategy as strategy
import spotinst_sdk2.models.ocean_cd.rollout_spec as rollout_spec
import spotinst_sdk2.models.ocean_cd.rollout as rollout


class OceanCDClient(Client):
    __base_oceancd_cluster_url = "https://api.spotinst.io/ocean/cd/cluster"
    __base_oceancd_vp_url = "https://api.spotinst.io/ocean/cd/verificationProvider"
    __base_oceancd_vt_url = "https://api.spotinst.io/ocean/cd/verificationTemplate"
    __base_strategy_url = "https://api.spotinst.io/ocean/cd/strategy"
    __base_rollout_spec_url = 'https://api.spotinst.io/ocean/cd/rolloutSpec'
    __base_rollout_url = 'https://api.spotinst.io/ocean/cd/rollout'
    __base_workload_url = 'https://api.spotinst.io/ocean/cd/workload'
    ENTITY_NAME1 = 'oceancd_cluster'
    ENTITY_NAME2 = 'oceancd_verification_provider'
    ENTITY_NAME3 = 'oceancd_verification_template'
    ENTITY_NAME4 = 'oceancd_strategy'
    ENTITY_NAME5 = 'oceancd_rollout_spec'
    ENTITY_NAME6 = 'oceancd_rollout'
    ENTITY_NAME7 = 'oceancd_workloads'

    def get_oceancd_cluster(self, cluster_id: str):
        """
        Get an existing Ocean CD cluster.

        # Arguments
        cluster_id (String): OceanCD Cluster ID

        # Returns
        (Object): OceanCD Cluster API response
        """
        response = self.send_get(
            url=self.__base_oceancd_cluster_url + "/" + cluster_id,
            entity_name=self.ENTITY_NAME1)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_all_oceancd_clusters(self):
        """
        List all Ocean CD clusters.

        # Returns
        (List): List of Ocean CD CLuster API response
        """
        response = self.send_get(
            url=self.__base_oceancd_cluster_url,
            entity_name=self.ENTITY_NAME1)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def update_oceancd_cluster(self, cluster_notification: oceancd_cluster.ClusterNotification, cluster_id: str):
        """
        Update Ocean CD cluster notification settings.

        # Arguments
        cluster_id (String): OceanCD Cluster ID
        node_update (StatefulNode): StatefulNode Object

        # Returns
        (Boolean): Response Status
        """
        request = oceancd_cluster.UpdateClusterNotification(cluster_notification)

        excluded_node_update_dict = self.exclude_missing(
            json.loads(request.toJSON()))

        formatted_node_update_dict = self.convert_json(
            excluded_node_update_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_node_update_dict)

        response = self.send_put(
            body=body_json,
            url=self.__base_oceancd_cluster_url + "/" + cluster_id,
            entity_name=self.ENTITY_NAME1)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["status"]

    def delete_oceancd_cluster(self, cluster_id: str):
        """
        Delete an existing Ocean CD cluster.

        # Arguments
        cluster_id (String): OceanCD Cluster ID

        # Returns
        (Boolean): Response Status
        """

        response = self.send_delete(
            url=self.__base_oceancd_cluster_url + "/" + cluster_id,
            entity_name=self.ENTITY_NAME1)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["status"]

    def create_oceancd_verification_provider(self, verification_provider: oceancd_vp.VerificationProvider):
        """
        Create Ocean CD Verification Provider. only one provider type can be defined

        # Arguments
        verification_provider (VerificationProvider) : OceanCD Verification Provider

        # Returns
        (Object) : OceanCD Verification Provider
        """
        request = oceancd_vp.VerificationProviderRequest(verification_provider)

        excluded_node_update_dict = self.exclude_missing(
            json.loads(request.toJSON()))

        formatted_node_update_dict = self.convert_json(
            excluded_node_update_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_node_update_dict)

        response = self.send_post(
            body=body_json,
            url=self.__base_oceancd_vp_url,
            entity_name=self.ENTITY_NAME2)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def get_all_oceancd_verification_provider(self):
        """
        List all Ocean CD verification providers.

        # Returns
        (List): List of Ocean CD Verification Provider API response
        """
        response = self.send_get(
            url=self.__base_oceancd_vp_url,
            entity_name=self.ENTITY_NAME2)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def get_oceancd_verification_provider(self, name: str):
        """
        Get an existing  Ocean CD Verification Provider.

        # Arguments
        name (String): The identifier of the Ocean CD Verification Provider

        # Returns
        (Object): OceanCD Verification Provider API response
        """
        response = self.send_get(
            url=self.__base_oceancd_vp_url + "/" + name,
            entity_name=self.ENTITY_NAME2)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def update_oceancd_verifcation_provider(self, provider_update: oceancd_vp.VerificationProvider, name: str):
        """
        Full Update of Ocean CD Verification Provider configuration. All non included fields will be nullified

        # Arguments
        name (String): The identifier name of the Ocean CD Verification Provider
        provider_update (VerificationProvider): VerificationProvider Object

        # Returns
        (Boolean): Response Status
        """
        request = oceancd_vp.VerificationProviderRequest(provider_update)

        excluded_node_update_dict = self.exclude_missing(
            json.loads(request.toJSON()))

        formatted_node_update_dict = self.convert_json(
            excluded_node_update_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_node_update_dict)

        response = self.send_put(
            body=body_json,
            url=self.__base_oceancd_vp_url + "/" + name,
            entity_name=self.ENTITY_NAME2)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["status"]

    def delete_oceancd_verification_provider(self, name: str):
        """
        Delete an existing Ocean CD Verification Provider.

        # Arguments
        name (String): OceanCD Cluster ID

        # Returns
        (Boolean): Response Status
        """

        response = self.send_delete(
            url=self.__base_oceancd_vp_url + "/" + name,
            entity_name=self.ENTITY_NAME2)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["status"]

    def create_oceancd_verification_template(self, verification_template: oceancd_vt.VerificationTemplate):
        """
        Create Ocean CD Verification Template.

        # Arguments
        verification_template (VerificationTemplate) : OceanCD Verification Template

        # Returns
        (Object) : OceanCD Verification Template
        """
        request = oceancd_vt.VerificationTemplateRequest(verification_template)

        excluded_node_update_dict = self.exclude_missing(
            json.loads(request.toJSON()))

        formatted_node_update_dict = self.convert_json(
            excluded_node_update_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_node_update_dict)

        response = self.send_post(
            body=body_json,
            url=self.__base_oceancd_vt_url,
            entity_name=self.ENTITY_NAME3)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def get_all_oceancd_verification_template(self):
        """
        List all Ocean CD verification templates.

        # Returns
        (List): List of Ocean CD Verification Template API response
        """
        response = self.send_get(
            url=self.__base_oceancd_vt_url,
            entity_name=self.ENTITY_NAME3)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def get_oceancd_verification_template(self, name: str):
        """
        Get an existing Ocean CD Verification Template.

        # Arguments
        name (String): The identifier of the Ocean CD Verification Template

        # Returns
        (Object): OceanCD Verification Template API response
        """
        response = self.send_get(
            url=self.__base_oceancd_vt_url + "/" + name,
            entity_name=self.ENTITY_NAME3)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def update_oceancd_verifcation_template(self, provider_update: oceancd_vt.VerificationTemplate, name: str):
        """
        Full Update of Ocean CD Verification Template configuration. All non included fields will be nullified

        # Arguments
        name (String): The identifier name of the Ocean CD Verification Template
        provider_update (VerificationTemplate): VerificationTemplate Object

        # Returns
        (Boolean): Response Status
        """
        request = oceancd_vt.VerificationTemplateRequest(provider_update)

        excluded_node_update_dict = self.exclude_missing(
            json.loads(request.toJSON()))

        formatted_node_update_dict = self.convert_json(
            excluded_node_update_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_node_update_dict)

        response = self.send_put(
            body=body_json,
            url=self.__base_oceancd_vt_url + "/" + name,
            entity_name=self.ENTITY_NAME3)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["status"]

    def delete_oceancd_verification_template(self, name: str):
        """
        Delete an existing Ocean CD Verification Template.

        # Arguments
        name (String): OceanCD Cluster ID

        # Returns
        (Boolean): Response Status
        """

        response = self.send_delete(
            url=self.__base_oceancd_vt_url + "/" + name,
            entity_name=self.ENTITY_NAME3)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["status"]

    def create_oceancd_strategy(self, strat: strategy.Strategy):
        """
        Create Ocean CD Strategy.

        # Arguments
        strategy (Strategy) : OceanCD Strategy

        # Returns
        (Object) : OceanCD Strategy
        """
        request = strategy.StrategyRequest(strat)

        excluded_node_update_dict = self.exclude_missing(
            json.loads(request.toJSON()))

        formatted_node_update_dict = self.convert_json(
            excluded_node_update_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_node_update_dict)

        response = self.send_post(
            body=body_json,
            url=self.__base_strategy_url,
            entity_name=self.ENTITY_NAME4)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def get_all_oceancd_strategy(self):
        """
        List all Ocean CD strategy.

        # Returns
        (List): List of Ocean CD Strategy API response
        """
        response = self.send_get(
            url=self.__base_strategy_url,
            entity_name=self.ENTITY_NAME4)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def get_oceancd_strategy(self, name: str):
        """
        Get an existing Ocean CD Strategy.

        # Arguments
        name (String): The identifier of the Ocean CD Strategy

        # Returns
        (Object): OceanCD Strategy API response
        """
        response = self.send_get(
            url=self.__base_strategy_url + "/" + name,
            entity_name=self.ENTITY_NAME4)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def update_oceancd_strategy(self, provider_update: strategy.Strategy, name: str):
        """
        Full Update of Ocean CD strategy configuration. All non included fields will be nullified

        # Arguments
        name (String): The identifier name of the Ocean CD Strategy
        provider_update (Strategy): Strategy Object

        # Returns
        (Boolean): Response Status
        """
        request = strategy.StrategyRequest(provider_update)

        excluded_node_update_dict = self.exclude_missing(
            json.loads(request.toJSON()))

        formatted_node_update_dict = self.convert_json(
            excluded_node_update_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_node_update_dict)

        response = self.send_put(
            body=body_json,
            url=self.__base_strategy_url + "/" + name,
            entity_name=self.ENTITY_NAME4)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["status"]

    def delete_oceancd_strategy(self, name: str):
        """
        Delete an existing Ocean CD Strategy.

        # Arguments
        name (String): OceanCD Strategy

        # Returns
        (Boolean): Response Status
        """

        response = self.send_delete(
            url=self.__base_strategy_url + "/" + name,
            entity_name=self.ENTITY_NAME4)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["status"]

    def create_oceancd_rollout_spec(self, rollout: rollout_spec.RolloutSpec):
        """
        Create Ocean CD rollout spec.

        # Arguments
        rollout_spec (RolloutSpec) : OceanCD Rollout Spec

        # Returns
        (Object) : OceanCD Rollout Spec
        """
        request = rollout_spec.RolloutSpecRequest(rollout)

        excluded_node_update_dict = self.exclude_missing(
            json.loads(request.toJSON()))

        formatted_node_update_dict = self.convert_json(
            excluded_node_update_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_node_update_dict)

        response = self.send_post(
            body=body_json,
            url=self.__base_rollout_spec_url,
            entity_name=self.ENTITY_NAME5)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def get_all_oceancd_rollout_specs(self):
        """
        List all Ocean CD rollout specs.

        # Returns
        (List): List of Ocean CD Rollout Spec API response
        """
        response = self.send_get(
            url=self.__base_rollout_spec_url,
            entity_name=self.ENTITY_NAME5)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def get_oceancd_rollout_spec(self, name: str):
        """
        Get the configuration of an existing Ocean CD rollout spec.

        # Arguments
        name (String): The identifier of the Ocean CD Rollout Spec

        # Returns
        (Object): OceanCD Rollout Spec API response
        """
        response = self.send_get(
            url=self.__base_rollout_spec_url + "/" + name,
            entity_name=self.ENTITY_NAME5)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def update_oceancd_rollout_spec(self, provider_update: rollout_spec.RolloutSpec, name: str):
        """
        Full Update Ocean CD rollout spec configuration. All non included fields will be nullified

        # Arguments
        name (String): The identifier name of the Ocean CD Rollout Spec
        provider_update (RolloutSpec): Rollout Spec Object

        # Returns
        (Boolean): Response Status
        """
        request = rollout_spec.RolloutSpecRequest(provider_update)

        excluded_node_update_dict = self.exclude_missing(
            json.loads(request.toJSON()))

        formatted_node_update_dict = self.convert_json(
            excluded_node_update_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_node_update_dict)

        response = self.send_put(
            body=body_json,
            url=self.__base_rollout_spec_url + "/" + name,
            entity_name=self.ENTITY_NAME5)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["status"]

    def delete_oceancd_rollout(self, name: str):
        """
        Delete an existing Ocean CD Rollout Spec.

        # Arguments
        name (String): OceanCD Rollout Spec

        # Returns
        (Boolean): Response Status
        """

        response = self.send_delete(
            url=self.__base_rollout_spec_url + "/" + name,
            entity_name=self.ENTITY_NAME5)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["status"]

    def describe_rollout_by_id(self, rollout_id: str):
        """
        Get Ocean CD single rollout

        # Arguments
        rollout_id (String): The identifier of the Ocean CD rollout

        # Returns
        (Object): OceanCD Rollout List API response
        """
        response = self.send_get(
            url=self.__base_rollout_url + "/" + rollout_id,
            entity_name=self.ENTITY_NAME6)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def ocean_cd_rollout_actions(self, rollout_id: str, action_update: rollout.Action):
        """
        Execute action on an existing Ocean CD rollout.

        # Arguments
        rollout_id (String): The identifier of the Ocean CD rollout

        # Returns
        (Boolean): Response Status
        """
        request = rollout.ActionRequest(action_update)

        excluded_node_update_dict = self.exclude_missing(
            json.loads(request.toJSON()))

        formatted_node_update_dict = self.convert_json(
            excluded_node_update_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_node_update_dict)

        response = self.send_put(
            body=body_json,
            url=self.__base_rollout_url + "/" + rollout_id,
            entity_name=self.ENTITY_NAME6)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def list_ocean_cd_rollouts(self, from_date: str):
        """
        List Ocean CD rollouts.

        # Arguments
        from_date (String): From Date

        # Returns
        (Object): OceanCD Rollout List API response
        """
        query_params = dict(fromDate=from_date)

        response = self.send_get(
            url=self.__base_rollout_url,
            entity_name=self.ENTITY_NAME6,
            query_params=query_params)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def ocean_cd_describe_rollout_status(self, rollout_id: str):
        """
        Ocean CD rollout status.

        # Arguments
        rollout_id (String): The identifier of the Ocean CD rollout

        # Returns
        (Object): OceanCD Rollout List API response
        """
        response = self.send_get(
            url=self.__base_rollout_url + '/'+rollout_id+'/status',
            entity_name=self.ENTITY_NAME6)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def ocean_cd_describe_latest_rollouts(self, cluster_id: str, count: str, namespace: str, spot_deployment: str):
        """
        Ocean CD Latest rollout/s.

        # Arguments
        clusterId (String): clusterId configured.
        count (String): How many responses intended, sorted from the last one down.
        namespace (String): namespace name configured
        spot_deployment (String): SpotDeployment name configured

        # Returns
        (Object): OceanCD Rollout List API response
        """
        query_params = dict(cluster_id=cluster_id, count=count, namespace=namespace, spot_deployment=spot_deployment)

        response = self.send_get(
            url=self.__base_rollout_url + '/latest',
            entity_name=self.ENTITY_NAME6,
            query_params=query_params)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def ocean_cd_describe_ongoing_rollouts(self):
        """
        Ocean CD Latest rollout/s.

        # Returns
        (Object): OceanCD Rollout List API response
        """
        response = self.send_get(
            url=self.__base_rollout_url + '/ongoing',
            entity_name=self.ENTITY_NAME6)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def ocean_cd_describe_rollout_verification(self, rollout_id: str):
        """
        Ocean CD Latest rollout/s.

        # Arguments
        rolloutId (String): The identifier of the Ocean CD Verification Response

        # Returns
        (Object): OceanCD Rollout List API response
        """
        response = self.send_get(
            url=self.__base_rollout_url + '/'+rollout_id+'/verification',
            entity_name=self.ENTITY_NAME6)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def ocean_cd_describe_rollout_definition(self, rollout_id: str):
        """
        Ocean CD rollout definition.

        # Arguments
        rolloutId (String): The identifier of the Ocean CD Definition Response

        # Returns
        (Object): OceanCD Rollout List API response
        """
        response = self.send_get(
            url=self.__base_rollout_url + '/'+rollout_id+'/definition',
            entity_name=self.ENTITY_NAME6)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def ocean_cd_describe_rollout_resource(self, rollout_id: str):
        """
        Ocean CD rollout definition.

        # Arguments
        rolloutId (String): The identifier of the Ocean CD Resource Response

        # Returns
        (Object): OceanCD Rollout List API response
        """
        response = self.send_get(
            url=self.__base_rollout_url + '/'+rollout_id+'/resource',
            entity_name=self.ENTITY_NAME6)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def ocean_cd_describe_rollout_phase(self, rollout_id: str):
        """
        Ocean CD Rollout phase.

        # Arguments
        rolloutId (String): The identifier of the Ocean CD phase

        # Returns
        (Object): OceanCD Rollout List API response
        """
        response = self.send_get(
            url=self.__base_rollout_url + '/'+rollout_id+'/phase',
            entity_name=self.ENTITY_NAME6)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_all_ocean_cd_workloads(self):
        """
        List all Ocean CD workloads.

        # Returns
        (Object): OceanCD Workloads API response
        """
        response = self.send_get(
            url=self.__base_workload_url,
            entity_name=self.ENTITY_NAME7)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def ocean_cd_describe_workloads_migration(self, deployment_name: str, namespace: str, cluster_id: str):
        """
        Describe How To Migrate Deployment CRD To SpotDeployment DRD.

        # Arguments
        deployment_name (String): The identifier name of the Ocean CD Deployment
        namespace (String): The workload's namespace
        cluster_id (String): Cluster id where the workload is running

        # Returns
        (Object): OceanCD Workloads Migration API response
        """
        query_params = dict(cluster_id=cluster_id)

        response = self.send_get(
            url=self.__base_workload_url + '/namespace/'+namespace+'/deployment/'+deployment_name+'/migrate',
            entity_name=self.ENTITY_NAME7,
            query_params=query_params)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def ocean_cd_describe_workloads_active_operations(self, workload_id: str):
        """
        Describe What Operation Are Active For Specific Workload.

        # Arguments
        workload_id (String): The workload's Id

        # Returns
        (Object): OceanCD Workloads Active Operations API response
        """
        response = self.send_get(
            url=self.__base_workload_url + '/'+workload_id+'/activeOperation',
            entity_name=self.ENTITY_NAME7)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def ocean_cd_describe_workloads_revision(self, workload_id: str):
        """
        Describe Workload's Revision.

        # Arguments
        workload_id (String): The workload's Id

        # Returns
        (Object): OceanCD Workloads Revision API response
        """
        response = self.send_get(
            url=self.__base_workload_url + '/'+workload_id+'/revision',
            entity_name=self.ENTITY_NAME7)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def ocean_cd_describe_workloads_graph(self, namespace: str, workload_name: str, cluster_id: str, kind: str):
        """
        Ocean CD workload graph.

        # Arguments
        namespace (String): Workload's namespace name
        workload_name (String): Workload name
        cluster_id (String): Cluster id where the workload is running
        kind (String): Kind of workload, currently only SpotDeployment is supported

        # Returns
        (Object): OceanCD Workloads Revision API response
        """
        query_params = dict(cluster_id=cluster_id, kind=kind)
        response = self.send_get(
            url=self.__base_workload_url + '/'+workload_name+'/namespace/'+namespace+'/graph',
            entity_name=self.ENTITY_NAME7,
            query_params=query_params)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def ocean_cd_restart_workload(self, workload_id: str):
        """
        Restart Workload By WorkloadId.

        # Arguments
        workload_id (String): The workload's Id

        # Returns
        (Boolean): Response Status
        """
        response = self.send_put(
            url=self.__base_workload_url + '/'+workload_id+'/restart',
            entity_name=self.ENTITY_NAME7)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def ocean_cd_retry_workload(self, revision_id: str, workload_id: str, rollout_id: str):
        """
        Ocean CD workload graph.

        # Arguments
        revision_id (String): Relevant Revision Id
        workload_id (String): The workload's Id
        rollout_id (String): The rollout Id

        # Returns
        (Boolean): Response Status
        """
        query_params = dict(rollout_id=rollout_id)
        response = self.send_put(
            url=self.__base_workload_url + '/'+workload_id+'/revision/'+revision_id+'/retry',
            entity_name=self.ENTITY_NAME7,
            query_params=query_params)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def ocean_cd_rollback_workload(self, revision_id: str, workload_id: str, rollout_id: str):
        """
        Ocean CD workload graph.

        # Arguments
        revision_id (String): Relevant Revision Id
        workload_id (String): The workload's Id
        rollout_id (String): The rollout Id

        # Returns
        (Boolean): Response Status
        """
        query_params = dict(rollout_id=rollout_id)
        response = self.send_put(
            url=self.__base_workload_url + '/'+workload_id+'/revision/'+revision_id+'/rollback',
            entity_name=self.ENTITY_NAME7,
            query_params=query_params)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]