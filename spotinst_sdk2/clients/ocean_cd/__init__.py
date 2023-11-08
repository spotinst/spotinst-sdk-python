import json

from spotinst_sdk2.client import Client
import spotinst_sdk2.models.ocean_cd as oceancd_cluster
import spotinst_sdk2.models.ocean_cd.verification_provider as oceancd_vp
import spotinst_sdk2.models.ocean_cd.verification_template as oceancd_vt
from spotinst_sdk2.models.ocean_cd import strategy
from spotinst_sdk2.models.ocean_cd import rollout_spec
from spotinst_sdk2.models.ocean_cd import rollout


class OceanCDClient(Client):
    __base_oceancd_cluster_url = "/ocean/cd/cluster"
    __base_oceancd_vp_url = "/ocean/cd/verificationProvider"
    __base_oceancd_vt_url = "/ocean/cd/verificationTemplate"
    __base_strategy_url = "/ocean/cd/strategy"
    __base_rollout_spec_url = '/ocean/cd/rolloutSpec'
    __base_rollout_url = '/ocean/cd/rollout'
    __base_workload_url = '/ocean/cd/workload'

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
            entity_name="oceancdCluster")

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
            entity_name="oceancdCluster")

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def update_oceancd_cluster(self, cluster_notification: oceancd_cluster.ClusterNotification,
                               cluster_id: str):
        """
        Update Ocean CD cluster notification settings.

        # Arguments
        cluster_id (String): OceanCD Cluster ID
        cluster_notification (ClusterNotification): Cluster Notification

        # Returns
        (Boolean): Response Status
        """
        request = oceancd_cluster.UpdateClusterNotification(
            cluster_notification)

        excluded_node_update_dict = self.exclude_missing(
            json.loads(request.toJSON()))

        formatted_node_update_dict = self.convert_json(
            excluded_node_update_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_node_update_dict)

        response = self.send_put(
            body=body_json,
            url=self.__base_oceancd_cluster_url + "/" + cluster_id,
            entity_name="oceancdCluster")

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

        return self.send_delete(
            url=self.__base_oceancd_cluster_url + "/" + cluster_id,
            entity_name="oceancdCluster")

    def create_oceancd_verification_provider(self,
                                             verification_provider: oceancd_vp.VerificationProvider):
        """
        Create Ocean CD Verification Provider. only one provider type can be defined

        # Arguments
        verification_provider (VerificationProvider): OceanCD Verification Provider

        # Returns
        (Object) : OceanCD Verification Provider
        """
        request = oceancd_vp.CreateVerificationProviderRequest(
            verification_provider)

        excluded_node_update_dict = self.exclude_missing(
            json.loads(request.toJSON()))

        formatted_node_update_dict = self.convert_json(
            excluded_node_update_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_node_update_dict)

        response = self.send_post(
            body=body_json,
            url=self.__base_oceancd_vp_url,
            entity_name="oceancdVerificationProvider")

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def get_all_oceancd_verification_providers(self):
        """
        List all Ocean CD verification providers.

        # Returns
        (List): List of Ocean CD Verification Provider API response
        """
        response = self.send_get(
            url=self.__base_oceancd_vp_url,
            entity_name="oceancdVerificationProvider")

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
            entity_name="oceancdVerificationProvider")

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def update_oceancd_verifcation_provider(self, provider_update: oceancd_vp.VerificationProvider,
                                            name: str):
        """
        Full Update of Ocean CD Verification Provider configuration. All non included fields will be nullified

        # Arguments
        name (String): The identifier name of the Ocean CD Verification Provider
        provider_update (VerificationProvider): VerificationProvider Object

        # Returns
        (Boolean): Response Status
        """
        request = oceancd_vp.CreateVerificationProviderRequest(provider_update)

        excluded_node_update_dict = self.exclude_missing(
            json.loads(request.toJSON()))

        formatted_node_update_dict = self.convert_json(
            excluded_node_update_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_node_update_dict)

        response = self.send_put(
            body=body_json,
            url=self.__base_oceancd_vp_url + "/" + name,
            entity_name="oceancdVerificationProvider")

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

        return self.send_delete(
            url=self.__base_oceancd_vp_url + "/" + name,
            entity_name="oceancdVerificationProvider")

    def create_oceancd_verification_template(self,
                                             verification_template: oceancd_vt.VerificationTemplate):
        """
        Create Ocean CD Verification Template.

        # Arguments
        verification_template (VerificationTemplate) : OceanCD Verification Template

        # Returns
        (Object) : OceanCD Verification Template
        """
        request = oceancd_vt.CreateVerificationTemplateRequest(
            verification_template)

        excluded_node_update_dict = self.exclude_missing(
            json.loads(request.toJSON()))

        formatted_node_update_dict = self.convert_json(
            excluded_node_update_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_node_update_dict)

        response = self.send_post(
            body=body_json,
            url=self.__base_oceancd_vt_url,
            entity_name="oceancdVerificationTemplate")

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_all_oceancd_verification_templates(self):
        """
        List all Ocean CD verification templates.

        # Returns
        (List): List of Ocean CD Verification Template API response
        """
        response = self.send_get(
            url=self.__base_oceancd_vt_url,
            entity_name="oceancdVerificationTemplate")

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
            entity_name="oceancdVerificationTemplate")

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def update_oceancd_verifcation_template(self, template_update: oceancd_vt.VerificationTemplate, name: str):
        """
        Full Update of Ocean CD Verification Template configuration. All non included fields will be nullified

        # Arguments
        name (String): The identifier name of the Ocean CD Verification Template
        template_update (VerificationTemplate): VerificationTemplate Object

        # Returns
        (Boolean): Response Status
        """
        request = oceancd_vt.CreateVerificationTemplateRequest(template_update)

        excluded_node_update_dict = self.exclude_missing(
            json.loads(request.toJSON()))

        formatted_node_update_dict = self.convert_json(
            excluded_node_update_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_node_update_dict)

        response = self.send_put(
            body=body_json,
            url=self.__base_oceancd_vt_url + "/" + name,
            entity_name="oceancdVerificationTemplate")

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["status"]

    def delete_oceancd_verification_template(self, name: str):
        """
        Delete an existing Ocean CD Verification Template.

        # Arguments
        name (String): The identifier name of the Ocean CD Verification Template

        # Returns
        (Boolean): Response Status
        """

        return self.send_delete(
            url=self.__base_oceancd_vt_url + "/" + name,
            entity_name="oceancdVerificationTemplate")

    def create_oceancd_strategy(self, strat: strategy.Strategy):
        """
        Create Ocean CD Strategy.

        # Arguments
        strat (Strategy) : OceanCD Strategy

        # Returns
        (Object) : OceanCD Strategy
        """
        request = strategy.CreateStrategyRequest(strat)

        excluded_node_update_dict = self.exclude_missing(
            json.loads(request.toJSON()))

        formatted_node_update_dict = self.convert_json(
            excluded_node_update_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_node_update_dict)

        response = self.send_post(
            body=body_json,
            url=self.__base_strategy_url,
            entity_name="oceancdStrategy")

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_all_oceancd_strategy(self):
        """
        List all Ocean CD strategy.

        # Returns
        (List): List of Ocean CD Strategy API response
        """
        response = self.send_get(
            url=self.__base_strategy_url,
            entity_name="oceancdStrategy")

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
            entity_name="oceancdStrategy")

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def update_oceancd_strategy(self, strategy_update: strategy.Strategy, name: str):
        """
        Full Update of Ocean CD strategy configuration. All non included fields will be nullified

        # Arguments
        name (String): The identifier name of the Ocean CD Strategy
        strategy_update (Strategy): Strategy Object

        # Returns
        (Boolean): Response Status
        """
        request = strategy.CreateStrategyRequest(strategy_update)

        excluded_node_update_dict = self.exclude_missing(
            json.loads(request.toJSON()))

        formatted_node_update_dict = self.convert_json(
            excluded_node_update_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_node_update_dict)

        response = self.send_put(
            body=body_json,
            url=self.__base_strategy_url + "/" + name,
            entity_name="oceancdStrategy")

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

        return self.send_delete(
            url=self.__base_strategy_url + "/" + name,
            entity_name="oceancdStrategy")

    def create_oceancd_rollout_spec(self, rollouts: rollout_spec.RolloutSpec):
        """
        Create Ocean CD rollout spec.

        # Arguments
        rollouts (RolloutSpec): OceanCD Rollout Spec

        # Returns
        (Object): OceanCD Rollout Spec
        """
        request = rollout_spec.CreateRolloutSpecRequest(rollouts)

        excluded_node_update_dict = self.exclude_missing(
            json.loads(request.toJSON()))

        formatted_node_update_dict = self.convert_json(
            excluded_node_update_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_node_update_dict)

        response = self.send_post(
            body=body_json,
            url=self.__base_rollout_spec_url,
            entity_name="oceancdRolloutSpec")

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_all_oceancd_rollout_specs(self):
        """
        List all Ocean CD rollout specs.

        # Returns
        (List): List of Ocean CD Rollout Spec API response
        """
        response = self.send_get(
            url=self.__base_rollout_spec_url,
            entity_name="oceancdRolloutSpec")

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
            entity_name="oceancdRolloutSpec")

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def update_oceancd_rollout_spec(self, rollout_spec_update: rollout_spec.RolloutSpec, name: str):
        """
        Full Update Ocean CD rollout spec configuration. All non included fields will be nullified

        # Arguments
        name (String): The identifier name of the Ocean CD Rollout Spec
        rollout_spec_update (RolloutSpec): Rollout Spec Object

        # Returns
        (Boolean): Response Status
        """
        request = rollout_spec.CreateRolloutSpecRequest(rollout_spec_update)

        excluded_node_update_dict = self.exclude_missing(
            json.loads(request.toJSON()))

        formatted_node_update_dict = self.convert_json(
            excluded_node_update_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_node_update_dict)

        response = self.send_put(
            body=body_json,
            url=self.__base_rollout_spec_url + "/" + name,
            entity_name="oceancdRolloutSpec")

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

        return self.send_delete(
            url=self.__base_rollout_spec_url + "/" + name,
            entity_name="oceancdRolloutSpec")

    def describe_rollout_by_id(self, rollout_id: str):
        """
        Get Ocean CD single rollout

        # Arguments
        rollout_id (String): The identifier of the Ocean CD rollout

        # Returns
        (Object): OceanCD Rollout API response
        """
        response = self.send_get(
            url=self.__base_rollout_url + "/" + rollout_id,
            entity_name="oceancdRollout")

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
        request = rollout.CreateRolloutActionRequest(action_update)

        excluded_node_update_dict = self.exclude_missing(
            json.loads(request.toJSON()))

        formatted_node_update_dict = self.convert_json(
            excluded_node_update_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_node_update_dict)

        response = self.send_put(
            body=body_json,
            url=self.__base_rollout_url + "/" + rollout_id,
            entity_name="oceancdRollout")

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["status"]

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
            entity_name="oceancdRollout",
            query_params=query_params)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

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
            entity_name="oceancdRollout")

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
        query_params = dict(cluster_id=cluster_id, count=count,
                            namespace=namespace, spot_deployment=spot_deployment)

        response = self.send_get(
            url=self.__base_rollout_url + '/latest',
            entity_name="oceancdRollout",
            query_params=query_params)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def ocean_cd_describe_ongoing_rollouts(self):
        """
        Ocean CD Ongoing rollouts.

        # Returns
        (Object): OceanCD Rollout List API response
        """
        response = self.send_get(
            url=self.__base_rollout_url + '/ongoing',
            entity_name="oceancdRollout")

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def ocean_cd_describe_rollout_verification(self, rollout_id: str):
        """
        Ocean CD rollout verification.

        # Arguments
        rolloutId (String): The identifier of the Ocean CD Verification Response

        # Returns
        (Object): OceanCD Rollout List API response
        """
        response = self.send_get(
            url=self.__base_rollout_url + '/'+rollout_id+'/verification',
            entity_name="oceancdRollout")

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
            entity_name="oceancdRollout")

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def ocean_cd_describe_rollout_resource(self, rollout_id: str):
        """
        Ocean CD Resource

        # Arguments
        rolloutId (String): The identifier of the Ocean CD Resource Response

        # Returns
        (Object): OceanCD Rollout List API response
        """
        response = self.send_get(
            url=self.__base_rollout_url + '/'+rollout_id+'/resource',
            entity_name="oceancdRollout")

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
            entity_name="oceancdRollout")

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def get_all_ocean_cd_workloads(self):
        """
        List all Ocean CD workloads.

        # Returns
        (Object): OceanCD Workloads API response
        """
        response = self.send_get(
            url=self.__base_workload_url,
            entity_name="oceancdWorkloads")

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def ocean_cd_describe_workloads_migration_process(self, deployment_name: str, namespace: str, cluster_id: str):
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
            url=self.__base_workload_url + '/namespace/' +
            namespace+'/deployment/'+deployment_name+'/migrate',
            entity_name="oceancdWorkloads",
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
            entity_name="oceancdWorkloads")

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def ocean_cd_describe_workloads_revision(self, workload_id: str, namespace: str, cluster_id: str, kind: str):
        """
        Describe Workload's Revision.

        # Arguments
        workload_id (String): The workload's Id
        namespace (String): Workload's namespace name
        cluster_id (String): Cluster id where the workload is running
        kind (String): Kind of workload, currently only SpotDeployment is supported

        # Returns
        (Object): OceanCD Workloads Revision API response
        """

        query_params = dict(clusterId=cluster_id, kind=kind)
        response = self.send_get(
            url=self.__base_workload_url + '/'+workload_id +
            '/namespace/'+namespace+'/revision',
            entity_name="oceancdWorkloads",
            query_params=query_params)

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
            entity_name="oceancdWorkloads",
            query_params=query_params)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

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
            entity_name="oceancdWorkloads")

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]

    def ocean_cd_retry_workload(self, revision_id: str, workload_id: str, rollout_id: str):
        """
        Retry Workload By WorkloadId,RevisionId And RolloutId

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
            entity_name="oceancdWorkloads",
            query_params=query_params)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]

    def ocean_cd_rollback_workload(self, revision_id: str, workload_id: str, rollout_id: str):
        """
        Rollback Workload By WorkloadId,RevisionId And RolloutId

        # Arguments
        revision_id (String): Relevant Revision Id
        workload_id (String): The workload's Id
        rollout_id (String): The rollout Id

        # Returns
        (Boolean): Response Status
        """
        query_params = dict(rollout_id=rollout_id)
        response = self.send_put(
            url=self.__base_workload_url + '/'+workload_id +
            '/revision/'+revision_id+'/rollback',
            entity_name="oceancdWorkloads",
            query_params=query_params)

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]
