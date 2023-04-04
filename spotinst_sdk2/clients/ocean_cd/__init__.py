import json

from spotinst_sdk2.client import Client
import spotinst_sdk2.models.ocean_cd as oceancd_cluster
import spotinst_sdk2.models.ocean_cd.verification_provider as oceancd_vp
import spotinst_sdk2.models.ocean_cd.verification_template as oceancd_vt
import spotinst_sdk2.models.ocean_cd.strategy as strategy
import spotinst_sdk2.models.ocean_cd.rollout_spec as rollout_spec


class OceanCDClient(Client):
    __base_oceancd_cluster_url = "https://api.spotinst.io/ocean/cd/cluster"
    __base_oceancd_vp_url = "https://api.spotinst.io/ocean/cd/verificationProvider"
    __base_oceancd_vt_url = "https://api.spotinst.io/ocean/cd/verificationTemplate"
    __base_strategy_url = "https://api.spotinst.io/ocean/cd/strategy"
    __base_rollout_spec_url = 'https://api.spotinst.io/ocean/cd/rolloutSpec'
    ENTITY_NAME1 = 'oceancd_cluster'
    ENTITY_NAME2 = 'oceancd_verification_provider'
    ENTITY_NAME3 = 'oceancd_verification_template'
    ENTITY_NAME4 = 'oceancd_strategy'
    ENTITY_NAME5 = 'oceancd_rollout'

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
