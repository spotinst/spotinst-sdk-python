import json
import os
import re

import requests
import yaml
import logging

from spotinst_sdk import aws_elastigroup
from spotinst_sdk import spotinst_functions
from spotinst_sdk import spotinst_emr
from spotinst_sdk import spotinst_stateful
from spotinst_sdk import spotinst_blue_green_deployment
from spotinst_sdk import spotinst_deployment_action
from spotinst_sdk import spotinst_asg
from spotinst_sdk import spotinst_user_mapping
from spotinst_sdk import spotinst_mlb
from spotinst_sdk import spotinst_ocean
from spotinst_sdk import spotinst_event_subscription

VAR_SPOTINST_SHARED_CREDENTIALS_FILE = 'SPOTINST_SHARED_CREDENTIALS_FILE'
VAR_SPOTINST_PROFILE = 'SPOTINST_PROFILE'
VAR_SPOTINST_TOKEN = 'SPOTINST_TOKEN'
VAR_SPOTINST_ACCOUNT = 'SPOTINST_ACCOUNT'
VAR_SPOTINST_LOG_LEVEL = 'SPOTINST_LOG_LEVEL'

DEFAULT_PROFILE = 'default'
DEFAULT_CREDENTIALS_FILE = os.path.join(
    os.path.expanduser("~"), '.spotinst', 'credentials')

version = {}
with open(os.path.join(os.path.dirname(__file__), "./version.py")) as fp:
    exec(fp.read(), version)

_SpotinstClient__spotinst_sdk_python_agent_name = 'spotinst-sdk-python'
_SpotinstClient__spotinst_sdk_user_agent = '{}/{}'.format(
    _SpotinstClient__spotinst_sdk_python_agent_name, version['__version__'])


class SpotinstClient:
    __account_id_key = "accountId"
    __base_aws_url = "https://api.spotinst.io/aws/ec2"
    __base_elastigroup_url = "https://api.spotinst.io/aws/ec2/group"
    __base_emr_url = "https://api.spotinst.io/aws/emr/mrScaler"
    __base_functions_url = "https://api.spotinst.io/functions"
    __base_stateful_url = "https://api.spotinst.io/aws/ec2/statefulMigrationGroup"
    __base_kube_url = "https://api.spotinst.io/mcs/kubernetes/cluster"
    __base_saving_url = "https://api.spotinst.io/aws/potentialSavings"
    __base_setup_url = "https://api.spotinst.io/setup"
    __base_lb_url = "https://api.spotinst.io/loadBalancer"
    __base_ocean_url = "https://api.spotinst.io/ocean/aws/k8s/cluster"
    __base_event_subscription_url = "https://api.spotinst.io/events/subscription"

    camel_pat = re.compile(r'([A-Z])')
    under_pat = re.compile(r'_([a-z])')

    # region Constructor
    def __init__(self, auth_token=None,
                 account_id=None,
                 profile=None,
                 credentials_file=None,
                 print_output=True,
                 log_level=None,
                 user_agent=None):
        """
        :type auth_token: str
        :type account_id: str
        :type profile: str
        :type credentials_file: str
        :type print_output: bool
        :type log_level: str
        :type user_agent: str
        """

        if not auth_token:
            self.load_credentials(profile, credentials_file)
        else:
            self.auth_token = auth_token
            self.account_id = account_id

        self.should_print_output = print_output
        self.user_agent = user_agent

        # initialize logger
        self.logger = self.init_logger()
        self.set_log_level(log_level=log_level)

    # endregion

    # region Event Subscription
    def create_event_subscription(self, subscription):
        """
        Create an event subscription

        # Arguments
        subscription (Subscription): Subscription Object

        # Returns
        (Object): Subscription API response
        """
        subscription = spotinst_event_subscription.SubscriptionRequest(subscription)

        excluded_group_dict = self.exclude_missing(json.loads(subscription.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        group_response = self.send_post(
            body=body_json,
            url=self.__base_event_subscription_url,
            entity_name='subscription')

        formatted_response = self.convert_json(
            group_response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def update_event_subscription(self, subscription_id, subscription):
        """
        Update an exsisting event subscription

        # Arguments
        subscription_id (String): Subscription id
        subscription (Subscription): Subscription Object

        # Returns
        (Object): Subscription API response
        """
        subscription = spotinst_event_subscription.SubscriptionRequest(subscription)

        excluded_group_dict = self.exclude_missing(json.loads(subscription.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        group_response = self.send_put(
            body=body_json,
            url=self.__base_event_subscription_url +
                "/" + subscription_id,
            entity_name='subscription')

        formatted_response = self.convert_json(
            group_response, self.camel_to_underscore)

        retVal = formatted_response["response"]

        return retVal

    def get_all_event_subscription(self):
        """
        Get all Subscription in account

        # Returns
        (Object): Subscription API response
        """
        response = self.send_get(
            url=self.__base_event_subscription_url,
            entity_name="subscription"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"]

        return retVal

    def get_event_subscription(self, subscription_id):
        """
        Get an exsisting event subscription json

        # Arguments
        subscription_id (String): Subscription id

        # Returns
        (Object): Subscription API response
        """
        response = self.send_get(
            url=self.__base_event_subscription_url +
                "/" + subscription_id,
            entity_name="subscription"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def delete_event_subscription(self, subscription_id):
        """
        Delete an event subscription

        # Arguments
        subscription_id (String): Subscription id

        # Returns
        (Object): subscription response
        """
        response = self.send_delete(
            url=self.__base_event_subscription_url +
                "/" + subscription_id,
            entity_name="subscription"
        )

        return response

    # end region

    # region MLB
    def get_all_mlb_runtime(self):
        """
        Get all MLB runtime

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_get(
            url=self.__base_lb_url +
                "/runtime",
            entity_name="mlb runtime"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"]

        return retVal

    def get_mlb_runtime(self, runtime_id):
        """
        Get MLB runtime

        # Arguments
        runtime_id (String): Runtime id name

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_get(
            url=self.__base_lb_url +
                "/runtime/" + runtime_id,
            entity_name="mlb runtime"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def deregister_mlb_runtime(self, runtime_id):
        """
        Deregister MLB runtime

        # Arguments
        runtime_id (String): Runtime id name

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_put(
            url=self.__base_lb_url +
                "/runtime/" + runtime_id +
                "/deregister",
            entity_name="mlb runtime"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["status"]

        return retVal

    def delete_mlb_runtime(self, runtime_id):
        """
        Delete MLB runtime

        # Arguments
        runtime_id (String): Runtime id name

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_delete(
            url=self.__base_lb_url +
                "/runtime/" + runtime_id,
            entity_name="mlb runtime"
        )

        return response

    def create_mlb_deployment(self, deployment_name):
        """
        Create MLB deployment

        # Arguments
        deployment_name (String): Deployment name

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_post(
            url=self.__base_lb_url +
                "/deployment",
            body=json.dumps(dict(deployment=dict(name=deployment_name))),
            entity_name="mlb deployment"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def update_mlb_deployment(self, deployment_id, deployment_name):
        """
        Update MLB deployment

        # Arguments
        deployment_name (String): Deployment name
        deployment_id (String): Deployment Id

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_put(
            url=self.__base_lb_url +
                "/deployment/" + deployment_id,
            body=json.dumps(dict(deployment=dict(name=deployment_name))),
            entity_name="mlb deployment"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)
        retVal = formatted_response["response"]["status"]

        return retVal

    def get_mlb_deployment(self, deployment_id):
        """
        Get MLB deployment

        # Arguments
        deployment_id (String): Deployment Id

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_get(
            url=self.__base_lb_url +
                "/deployment/" + deployment_id,
            entity_name="mlb deployment"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def get_all_mlb_deployment(self):
        """
        Get All MLB deployment

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_get(
            url=self.__base_lb_url +
                "/deployment",
            entity_name="mlb deployment"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"]

        return retVal

    def delete_mlb_deployment(self, deployment_id):
        """
        Delete MLB deployment

        # Arguments
        deployment_id (String): Deployment Id

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_delete(
            url=self.__base_lb_url +
                "/deployment/" + deployment_id,
            entity_name="mlb deployment"
        )

        return response

    def create_mlb_balancer(self, balancer):
        """
        Create MLB balancer

        # Arguments
        balancer (Balancer): Balancer Object

        # Returns
        (Object): Spotinst API response
        """
        balancer = spotinst_mlb.BalancerRequest(balancer)

        excluded_group_dict = self.exclude_missing(json.loads(balancer.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        self.print_output(body_json)

        response = self.send_post(
            url=self.__base_lb_url +
                "/balancer",
            body=body_json,
            entity_name="mlb balancer"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def update_mlb_balancer(self, balancer_id, balancer):
        """
        Create MLB balancer

        # Arguments
        balancer_id (String): Balancer Id
        balancer (Balancer): Balancer Object

        # Returns
        (Object): Spotinst API response
        """
        balancer = spotinst_mlb.BalancerRequest(balancer)

        excluded_group_dict = self.exclude_missing(json.loads(balancer.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        self.print_output(body_json)

        response = self.send_put(
            url=self.__base_lb_url +
                "/balancer/" + balancer_id,
            body=body_json,
            entity_name="mlb balancer"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["status"]

        return retVal

    def get_mlb_balancer(self, balancer_id):
        """
        Get MLB balancer

        # Arguments
        balancer_id (String): Balancer Id

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_get(
            url=self.__base_lb_url +
                "/balancer/" + balancer_id,
            entity_name="mlb balancer"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def get_all_mlb_balancer(self):
        """
        Get All MLB balancer

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_get(
            url=self.__base_lb_url +
                "/balancer/",
            entity_name="mlb balancer"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"]

        return retVal

    def delete_mlb_balancer(self, balancer_id):
        """
        Delete MLB balancer

        # Arguments
        balancer_id (String): Balancer Id

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_delete(
            url=self.__base_lb_url +
                "/balancer/" + balancer_id,
            entity_name="mlb balancer"
        )

        return response

    def create_mlb_target_set(self, target_set):
        """
        Create MLB target set

        # Arguments
        target_set (TargetSet): TargetSet Object

        # Returns
        (Object): Spotinst API response
        """
        target_set = spotinst_mlb.TargetSetRequest(target_set)

        excluded_group_dict = self.exclude_missing(json.loads(target_set.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        self.print_output(body_json)

        response = self.send_post(
            url=self.__base_lb_url +
                "/targetSet",
            body=body_json,
            entity_name="mlb target set"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def update_mlb_target_set(self, target_set_id, target_set):
        """
        Update MLB target set

        # Arguments
        target_set_id (String): Target Set Id
        target_set (TargetSet): TargetSet Object

        # Returns
        (Object): Spotinst API response
        """
        target_set = spotinst_mlb.TargetSetRequest(target_set)

        excluded_group_dict = self.exclude_missing(json.loads(target_set.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        self.print_output(body_json)

        response = self.send_put(
            url=self.__base_lb_url +
                "/targetSet" + target_set_id,
            body=body_json,
            entity_name="mlb target set"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["status"]

        return retVal

    def get_mlb_target_set(self, target_set_id):
        """
        Gat an MLB target set

        # Arguments
        target_set_id (String): Target Set Id

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_get(
            url=self.__base_lb_url +
                "/targetSet/" + target_set_id,
            entity_name="mlb target set"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def get_all_mlb_target_set(self):
        """
        Get all MLB target sets

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_get(
            url=self.__base_lb_url +
                "/targetSet",
            entity_name="mlb target set"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"]

        return retVal

    def delete_mlb_target_set(self, target_set_id):
        """
        Delete an MLB target set

        # Arguments
        target_set_id (String): Target Set Id

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_delete(
            url=self.__base_lb_url +
                "/targetSet/" + target_set_id,
            entity_name="mlb target set"
        )

        return response

    def register_mlb_targets(self, target_set_id, targets):
        """
        Register MLB targets

        # Arguments
        target_set_id (String): Target Set Id
        Targets (List[Target]): List of Target Objects

        # Returns
        (Object): Spotinst API response
        """
        targets = spotinst_mlb.TargetsRequest(targets)

        excluded_group_dict = self.exclude_missing(json.loads(targets.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        self.print_output(body_json)

        response = self.send_put(
            url=self.__base_lb_url +
                "/targetSet/" + target_set_id +
                "/registerTargets",
            body=body_json,
            entity_name="mlb target set"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"]

        return retVal

    def deregister_mlb_targets(self, target_set_id, targets):
        """
        Deregister MLB targets

        # Arguments
        target_set_id (String): Target Set Id
        Targets (List[Target]): List of Target Objects

        # Returns
        (Object): Spotinst API response
        """
        targets = spotinst_mlb.TargetsRequest(targets)

        excluded_group_dict = self.exclude_missing(json.loads(targets.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        self.print_output(body_json)

        response = self.send_put(
            url=self.__base_lb_url +
                "/targetSet/" + target_set_id +
                "/deregisterTargets",
            body=body_json,
            entity_name="mlb target set"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["status"]

        return retVal

    def create_mlb_target(self, target):
        """
        Create MLB target

        # Arguments
        target (Target): Target Object

        # Returns
        (Object): Spotinst API response
        """
        target = spotinst_mlb.TargetRequest(target)

        excluded_group_dict = self.exclude_missing(json.loads(target.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        self.print_output(body_json)

        response = self.send_post(
            url=self.__base_lb_url +
                "/target",
            body=body_json,
            entity_name="mlb target"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def update_mlb_target(self, target_id, target):
        """
        Update MLB target

        # Arguments
        target_id (String): Target Id
        target (Target): Target Object

        # Returns
        (Object): Spotinst API response
        """
        target = spotinst_mlb.TargetRequest(target)

        excluded_group_dict = self.exclude_missing(json.loads(target.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        self.print_output(body_json)

        response = self.send_put(
            url=self.__base_lb_url +
                "/target/" + target_id,
            body=body_json,
            entity_name="mlb target"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["status"]

        return retVal

    def get_mlb_target(self, target_id):
        """
        Get MLB target

        # Arguments
        target_id (String): Target Id

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_get(
            url=self.__base_lb_url +
                "/target/" + target_id,
            entity_name="mlb target"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def get_all_mlb_target(self):
        """
        Get all MLB target

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_get(
            url=self.__base_lb_url +
                "/target",
            entity_name="mlb target"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"]

        return retVal

    def delete_mlb_target(self, target_id):
        """
        Delete MLB target

        # Arguments
        target_id (String): Target Id

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_delete(
            url=self.__base_lb_url +
                "/target/" + target_id,
            entity_name="mlb target"
        )

        return response

    def create_mlb_listener(self, listener):
        """
        Create MLB listener

        # Arguments
        listener (Listener): Listener Object

        # Returns
        (Object): Spotinst API response
        """
        listener = spotinst_mlb.ListenerRequest(listener)

        excluded_group_dict = self.exclude_missing(json.loads(listener.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        self.print_output(body_json)

        response = self.send_post(
            url=self.__base_lb_url +
                "/listener",
            body=body_json,
            entity_name="mlb listener"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def update_mlb_listener(self, listener_id, listener):
        """
        Update MLB listener

        # Arguments
        listener_id (String): Listener ID
        listener (Listener): Listener Object

        # Returns
        (Object): Spotinst API response
        """
        listener = spotinst_mlb.ListenerRequest(listener)

        excluded_group_dict = self.exclude_missing(json.loads(listener.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        self.print_output(body_json)

        response = self.send_put(
            url=self.__base_lb_url +
                "/listener/" + listener_id,
            body=body_json,
            entity_name="mlb listener"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["status"]

        return retVal

    def get_mlb_listener(self, listener_id):
        """
        Get MLB listener

        # Arguments
        listener_id (String): Listener ID

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_get(
            url=self.__base_lb_url +
                "/listener/" + listener_id,
            entity_name="mlb listener"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def get_all_mlb_listener(self):
        """
        Get all MLB listeners

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_get(
            url=self.__base_lb_url +
                "/listener",
            entity_name="mlb listener"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"]

        return retVal

    def delete_mlb_listener(self, listener_id):
        """
        Delete MLB listener

        # Arguments
        listener_id (String): Listener ID

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_delete(
            url=self.__base_lb_url +
                "/listener/" + listener_id,
            entity_name="mlb listener"
        )

        return response

    def create_mlb_routing_rule(self, routing_rule):
        """
        Create MLB routing rule

        # Arguments
        routing_rule (RoutingRule): RoutingRule Object

        # Returns
        (Object): Spotinst API response
        """
        routing_rule = spotinst_mlb.RoutingRuleRequest(routing_rule)

        excluded_group_dict = self.exclude_missing(json.loads(routing_rule.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        self.print_output(body_json)

        response = self.send_post(
            url=self.__base_lb_url +
                "/routingRule",
            body=body_json,
            entity_name="mlb routing rule"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def update_mlb_routing_rule(self, routing_rule_id, routing_rule):
        """
        Update MLB routing rule

        # Arguments
        routing_rule_id (String): Routing Rule Id
        routing_rule (RoutingRule): RoutingRule Object

        # Returns
        (Object): Spotinst API response
        """
        routing_rule = spotinst_mlb.RoutingRuleRequest(routing_rule)

        excluded_group_dict = self.exclude_missing(json.loads(routing_rule.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        self.print_output(body_json)

        response = self.send_put(
            url=self.__base_lb_url +
                "/routingRule/" + routing_rule_id,
            body=body_json,
            entity_name="mlb routing rule"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["status"]

        return retVal

    def get_mlb_routing_rule(self, routing_rule_id):
        """
        Get MLB routing rule

        # Arguments
        routing_rule_id (String): Routing Rule Id

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_get(
            url=self.__base_lb_url +
                "/routingRule/" + routing_rule_id,
            entity_name="mlb routing rule"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def get_all_mlb_routing_rule(self):
        """
        Get all MLB routing rule

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_get(
            url=self.__base_lb_url +
                "/routingRule",
            entity_name="mlb routing rule"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"]

        return retVal

    def delete_mlb_routing_rule(self, routing_rule_id):
        """
        Delete MLB routing rule

        # Arguments
        routing_rule_id (String): Routing Rule Id

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_delete(
            url=self.__base_lb_url +
                "/routingRule/" + routing_rule_id,
            entity_name="mlb routing rule"
        )

        return response

    def create_mlb_middleware(self, middleware):
        """
        Create MLB middleware

        # Arguments
        middleware (Middleware): Middleware Object

        # Returns
        (Object): Spotinst API response
        """
        middleware = spotinst_mlb.MiddlewareRequest(middleware)

        excluded_group_dict = self.exclude_missing(json.loads(middleware.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        self.print_output(body_json)

        response = self.send_post(
            url=self.__base_lb_url +
                "/middleware",
            body=body_json,
            entity_name="mlb middleware"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def update_mlb_middleware(self, middleware_id, middleware):
        """
        Update MLB middleware

        # Arguments
        middleware_id (String): Middleware ID
        middleware (Middleware): Middleware Object

        # Returns
        (Object): Spotinst API response
        """
        middleware = spotinst_mlb.MiddlewareRequest(middleware)

        excluded_group_dict = self.exclude_missing(json.loads(middleware.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        self.print_output(body_json)

        response = self.send_put(
            url=self.__base_lb_url +
                "/middleware/" + middleware_id,
            body=body_json,
            entity_name="mlb middleware"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["status"]

        return retVal

    def get_mlb_middleware(self, middleware_id):
        """
        Get MLB middleware

        # Arguments
        middleware_id (String): Middleware ID

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_get(
            url=self.__base_lb_url +
                "/middleware/" + middleware_id,
            entity_name="mlb middleware"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def get_all_mlb_middleware(self):
        """
        Get all MLB middleware

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_get(
            url=self.__base_lb_url +
                "/middleware",
            entity_name="mlb middleware"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"]

        return retVal

    def delete_mlb_middleware(self, middleware_id):
        """
        Delete MLB middleware

        # Arguments
        middleware_id (String): Middleware ID

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_delete(
            url=self.__base_lb_url +
                "/middleware/" + middleware_id,
            entity_name="mlb middleware"
        )

        return response

    # endregion

    # region Organization and Account
    def create_organization(self, org_name):
        """
        Create an organization

        # Arguments
        org_name (String): Orgnanization name

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_post(
            url=self.__base_setup_url +
                "/organization",
            body=json.dumps(dict(organization=dict(name=org_name))),
            entity_name="organization"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def delete_organization(self, org_id):
        """
        delete organization

        # Arguments
        org_id (String): Organization Id

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_delete(
            url=self.__base_setup_url +
                "/organization/" + str(org_id),
            entity_name="organization"
        )

        return response

    def create_aws_external_id(self):
        """
        Create aws account external id.
        You should use the external id when creating your AWS role for your spot account

        # Returns
        (Object): Spotinst API response 
        """
        response = self.send_post(
            url=self.__base_setup_url +
                "/credentials/aws/externalId",
            entity_name="credentials"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        ret_val = formatted_response["response"]["items"][0]

        return ret_val

    def set_cloud_credentials(self, iam_role, external_id=None):
        """
        set cloud credentials
        Please create external id using spot api (see #AdminClient.create_aws_external_id)
        and use it when creating the AWS role

        # Arguments
        iam_role (String): IAM Role
        external_id (String) (Optional): External ID

        # Returns
        (Object): Spotinst API response
        """
        credentials = {"iamRole": iam_role}

        if external_id is not None:
            credentials['externalId'] = external_id

        response = self.send_post(
            url=self.__base_setup_url +
                "/credentials/aws",
            body=json.dumps(dict(credentials=credentials)),
            entity_name="credentials"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["status"]

        return retVal

    def create_account(self, account_name):
        """
        create an account

        # Arguments
        account_name (String): Account Name

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_post(
            url=self.__base_setup_url +
                "/account",
            body=json.dumps(dict(account=dict(name=account_name))),
            entity_name="account"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def get_accounts(self):
        """
        get accounts in organization

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_get(
            url=self.__base_setup_url +
                "/account",
            entity_name="account"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"]

        return retVal

    def delete_account(self, account_name):
        """
        delete account

        # Arguments
        account_name (String): Account Name

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_delete(
            url=self.__base_setup_url +
                "/account/" + account_name,
            entity_name="account"
        )

        return response

    def create_user(self, first_name, last_name, email, password, role):
        """
        Create user

        # Arguments
        first_name (String): Users first name
        last_name (String): User last name
        email (String): Eser email
        password (String): User email
        role (String): User role


        # Returns
        (Object): Spotinst API response
        """
        response = self.send_post(
            url=self.__base_setup_url +
                "/user",
            body=json.dumps(dict(
                firstName=first_name,
                lastName=last_name,
                email=email,
                password=password,
                role=role)),
            entity_name="user"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def add_exsisting_user(self, user_email, role):
        """
        Add exsisting user

        # Arguments
        user_email (String): User email
        role (String): User role

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_post(
            url=self.__base_setup_url +
                "/account/" + self.account_id +
                "/user",
            body=json.dumps(dict(userEmail=user_email, role=role)),
            entity_name="user"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["status"]

        return retVal

    def update_user_role(self, user_email, role):
        """
        Update exsisting user

        # Arguments
        user_email (String): User email
        role (String): User role

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_put(
            url=self.__base_setup_url +
                "/account/" + self.account_id +
                "/user",
            body=json.dumps(dict(userEmail=user_email, role=role)),
            entity_name="user"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["status"]

        return retVal

    def detach_user(self, user_email):
        """
        Delete exsisting user

        # Arguments
        user_email (String): User email

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_delete_with_body(
            url=self.__base_setup_url +
                "/account/" + self.account_id +
                "/user",
            body=json.dumps(dict(userEmail=user_email)),
            entity_name="user"
        )

        return response

    def get_user(self, user_email):
        """
        Get user

        # Arguments
        user_email (String): User email

        # Returns
        (Object): Spotinst API response
        """
        query_params = dict(userEmail=user_email)
        response = self.send_get(
            url=self.__base_setup_url + "/accountUserMapping",
            query_params=query_params,
            entity_name="user"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"]

        return retVal

    def assign_user_to_account(self, mappings):
        """
        Assign user to account

        # Arguments
        mappings (List): List of UserMapping Objects

        # Returns
        (Object): Spotinst API response
        """
        mappings = spotinst_user_mapping.UserMappingRequest(mappings)

        excluded_group_dict = self.exclude_missing(json.loads(mappings.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        response = self.send_post(
            url=self.__base_setup_url + "/accountUserMapping",
            body=body_json,
            entity_name="user"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["status"]

        return retVal

    # endregion

    # region EMR
    def create_emr(self, emr):
        """
        Create an EMR

        # Arguments
        emr (EMR): EMR Object

        # Returns
        (Object): Elastigroup API response
        """
        emr = spotinst_emr.EMRCreationRequest(emr)

        excluded_group_dict = self.exclude_missing(json.loads(emr.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        group_response = self.send_post(
            body=body_json,
            url=self.__base_emr_url,
            entity_name='emr')

        formatted_response = self.convert_json(
            group_response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def update_emr(self, emr_id, emr):
        """
        Update an exsisting EMR

        # Arguments
        emr_id (String): EMR id
        emr (EMR): EMR Object

        # Returns
        (Object): Elastigroup API response
        """
        emr = spotinst_emr.EMRCreationRequest(emr)

        excluded_group_dict = self.exclude_missing(json.loads(emr.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        group_response = self.send_put(
            body=body_json,
            url=self.__base_emr_url +
                "/" + emr_id,
            entity_name='emr')

        formatted_response = self.convert_json(
            group_response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def get_all_emr(self):
        """
        Get all EMR in account

        # Returns
        (Object): Elastigroup API response
        """
        response = self.send_get(
            url=self.__base_emr_url,
            entity_name="emr"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"]

        return retVal

    def get_emr(self, emr_id):
        """
        Get an exsisting EMR json

        # Arguments
        emr_id (String): EMR id

        # Returns
        (Object): Elastigroup API response
        """
        response = self.send_get(
            url=self.__base_emr_url +
                "/" + emr_id,
            entity_name="emr"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def get_emr_instances(self, emr_id):
        """
        Get instances from EMR

        # Arguments
        emr_id (String): EMR id

        # Returns
        (Object): Elastigroup API response
        """
        response = self.send_get(
            url=self.__base_emr_url +
                "/" + emr_id +
                "/instance",
            entity_name="emr"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"]

        return retVal

    def get_emr_cluster(self, emr_id):
        """
        Get cluster from EMR

        # Arguments
        emr_id (String): EMR id

        # Returns
        (Object): Elastigroup API response
        """
        response = self.send_get(
            url=self.__base_emr_url +
                "/" + emr_id +
                "/cluster",
            entity_name="emr"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def get_emr_cost(self, emr_id, from_date=None, to_date=None):
        """
        Get cost from EMR

        # Arguments
        emr_id (String): EMR id
        from_date (String) (Optional): From Date
        to_date (String) (Optional): to date

        # Returns
        (Object): Elastigroup API response
        """
        query_params = dict(fromDate=from_date, toDate=to_date)

        response = self.send_get(
            url=self.__base_emr_url +
                "/" + emr_id +
                "/costs",
            query_params=query_params,
            entity_name="emr"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def delete_emr(self, emr_id):
        """
        Delete an EMR

        # Arguments
        emr_id (String): EMR id

        # Returns
        (Object): Elastigroup API response
        """
        response = self.send_delete(
            url=self.__base_emr_url +
                "/" + emr_id,
            entity_name="emr"
        )

        return response

    def scale_up_emr(self, emr_id, adjustment):
        """
        Scale up an EMR

        # Arguments
        emr_id (String): EMR id
        adjustment (Int): Ammount to scale

        # Returns
        (Object): Elastigroup API response
        """
        query_params = dict(adjustment=adjustment)

        response = self.send_put(
            url=self.__base_emr_url +
                "/" + emr_id +
                "/scale/up",
            query_params=query_params,
            entity_name="emr"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def scale_down_emr(self, emr_id, adjustment):
        """
        Scale down an EMR

        # Arguments
        emr_id (String): EMR id
        adjustment (Int): Ammount to scale

        # Returns
        (Object): Elastigroup API response
        """
        query_params = dict(adjustment=adjustment)

        response = self.send_put(
            url=self.__base_emr_url +
                "/" + emr_id +
                "/scale/down",
            query_params=query_params,
            entity_name="emr"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    # endregion

    # region Ocean
    def create_ocean_cluster(self, ocean):
        """
        Create an Ocean Cluster

        # Arguments
        ocean (Ocean): Ocean Object

        # Returns
        (Object): Ocean API response
        """
        ocean = spotinst_ocean.OceanRequest(ocean)

        excluded_group_dict = self.exclude_missing(json.loads(ocean.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        group_response = self.send_post(
            body=body_json,
            url=self.__base_ocean_url,
            entity_name='ocean')

        formatted_response = self.convert_json(
            group_response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def update_ocean_cluster(self, ocean_id, ocean):
        """
        Update an exsisting Ocean Cluster

        # Arguments
        ocean_id (String): Ocean id
        ocean (Ocean): Ocean Object

        # Returns
        (Object): Ocean API response
        """
        ocean = spotinst_ocean.OceanRequest(ocean)

        excluded_group_dict = self.exclude_missing(json.loads(ocean.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        group_response = self.send_put(
            body=body_json,
            url=self.__base_ocean_url +
                "/" + ocean_id,
            entity_name='ocean')

        formatted_response = self.convert_json(
            group_response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def get_all_ocean_cluster(self):
        """
        Get all Ocean in account

        # Returns
        (Object): Ocean API response
        """
        response = self.send_get(
            url=self.__base_ocean_url,
            entity_name="ocean"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"]

        return retVal

    def get_all_ocean_sizing(self, ocean_id, namespace):
        """
        Get all right sizing recommendations for an Ocean cluster

        # Returns
        (Object): Ocean API response
        """
        response = self.send_get(
            url=(self.__base_ocean_url +
                 "/" + ocean_id +
                 "/rightSizing/suggestion?namespace={}"
                 ).format(namespace),
            entity_name="ocean"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"]

        return retVal

    def get_ocean_cluster(self, ocean_id):
        """
        Get an exsisting Ocean Cluster json

        # Arguments
        ocean_id (String): Ocean id

        # Returns
        (Object): Ocean API response
        """
        response = self.send_get(
            url=self.__base_ocean_url +
                "/" + ocean_id,
            entity_name="ocean"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def delete_ocean_cluster(self, ocean_id):
        """
        Delete an Ocean Cluster

        # Arguments
        ocean_id (String): Ocean id

        # Returns
        (Object): Elastigroup API response
        """
        response = self.send_delete(
            url=self.__base_ocean_url +
                "/" + ocean_id,
            entity_name="ocean"
        )

        return response

    # endregion

    # region Kubernetes

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
        query_params = self.build_query_params_with_input({"toDate": to_date, "fromDate": from_date})

        result = self.send_get(url=geturl, query_params=query_params, entity_name='kubernetes')

        formatted_response = self.convert_json(
            result, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    # endregion

    # region Elastigroup
    def create_elastigroup(self, group):
        """
        Create an elastigroup

        # Arguments
        group (Elastigroup): Elastigroup Object

        # Returns
        (Object): Elastigroup API response
        """
        group = aws_elastigroup.ElastigroupCreationRequest(group)

        excluded_group_dict = self.exclude_missing(json.loads(group.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        self.print_output(body_json)

        group_response = self.send_post(
            body=body_json,
            url=self.__base_elastigroup_url,
            entity_name='elastigroup')

        formatted_response = self.convert_json(
            group_response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def scale_elastigroup_up(self, group_id, adjustment):
        """
        Scale up an elastigroup

        # Arguments
        group_id (String): Elastigroup ID
        adjustment (int): Ammount to scale group

        # Returns
        (Object): Elastigroup API response
        """
        query_params = dict({"adjustment": adjustment})
        content = self.send_put_with_params(
            url=self.__base_elastigroup_url +
                "/" +
                str(group_id) +
                "/scale/up",
            entity_name='elastigroup (scale up)',
            body=None,
            user_query_params=query_params)

        formatted_response = self.convert_json(
            content, self.camel_to_underscore)
        return formatted_response["response"]["items"]

    def scale_elastigroup_down(self, group_id, adjustment):
        """
        Scale down an elastigroup

        # Arguments
        group_id (String): Elastigroup ID
        adjustment (int): Ammount to scale group

        # Returns
        (Object): Elastigroup API response
        """
        query_params = dict({"adjustment": adjustment})
        content = self.send_put_with_params(
            url=self.__base_elastigroup_url +
                "/" +
                str(group_id) +
                "/scale/down",
            entity_name='elastigroup (scale down)',
            body=None,
            user_query_params=query_params)

        formatted_response = self.convert_json(
            content, self.camel_to_underscore)
        return formatted_response["response"]["items"]

    def update_elastigroup(self, group_update, group_id, auto_apply_tags=None):
        """
        Update an elastigroup

        # Arguments
        group_id (String): Elastigroup ID
        group_update (Elastigroup): Elastigroup Object

        # Returns
        (Object): Elastigroup API response
        """
        group = aws_elastigroup.ElastigroupUpdateRequest(group_update)

        excluded_group_update_dict = self.exclude_missing(
            json.loads(group.toJSON()))

        formatted_group_update_dict = self.convert_json(
            excluded_group_update_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_update_dict)

        self.print_output(body_json)

        group_response = self.send_put_with_params(
            body=body_json,
            url=self.__base_elastigroup_url + "/" + group_id,
            entity_name='elastigroup',
            user_query_params=dict(autoApplyTags=auto_apply_tags)
        )

        formatted_response = self.convert_json(
            group_response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def delete_elastigroup(self, group_id):
        """
        Delete an elastigroup

        # Arguments
        group_id (String): Elastigroup ID

        # Returns
        (Object): Elastigroup API response
        """
        delurl = self.__base_elastigroup_url + "/" + group_id
        response = self.send_delete(url=delurl, entity_name='elastigroup')
        return response

    def delete_elastigroup_with_deallocation(self, group_id, stateful_deallocation):
        """
        Delete a stateful elastigroup

        # Arguments
        group_id (String): Elastigroup ID
        stateful_deallocation (Deallocation): Deallocation Object

        # Returns
        (Object): Elastigroup API response
        """
        delurl = self.__base_elastigroup_url + "/" + group_id

        deletion_request = aws_elastigroup.ElastigroupDeletionRequest(
            stateful_deallocation)

        excluded_deletion_dict = self.exclude_missing(
            json.loads(deletion_request.toJSON()))
        formatted_deletion_dict = self.convert_json(
            excluded_deletion_dict, self.underscore_to_camel)
        body_json = json.dumps(formatted_deletion_dict)

        response = self.send_delete_with_body(
            body=body_json, url=delurl, entity_name='elastigroup')

        return response

    def get_elastilog(self, group_id, from_date, to_date, severity=None, resource_id=None, limit=None):
        """
        Get an elastilog for a specific elastigroup

        # Arguments
        group_id(String): Elastigroup ID
        to_date (String): to date
        from_date (String): to date
        severity(String) (Optional): Log level severity
        resource_id(String) (Optional): Filter log extracted entires related to a specific resource id
        limit(String) (Optional): Maximum number of lines to extract in a response

        # Returns
        (Object): Elastigroup API response
        """
        geturl = self.__base_elastigroup_url + "/" + group_id + "/logs"
        query_params = dict(toDate=to_date, fromDate=from_date, severity=severity,
                            resource_id=resource_id, limit=limit)

        result = self.send_get(url=geturl, entity_name='elastilog', query_params=query_params)

        formatted_response = self.convert_json(
            result, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def get_elastigroup(self, group_id):
        """
        Get an elastigroup

        # Arguments
        group_id(String): Elastigroup ID

        # Returns
        (Object): Elastigroup API response
        """
        geturl = self.__base_elastigroup_url + "/" + group_id
        result = self.send_get(url=geturl, entity_name='elastigroup')

        formatted_response = self.convert_json(
            result, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_elastigroups(self):
        """
        Get all elastigroup

        # Returns
        (List): List of Elastigroup API response
        """
        content = self.send_get(
            url=self.__base_elastigroup_url,
            entity_name='elastigroup')
        formatted_response = self.convert_json(
            content, self.camel_to_underscore)
        return formatted_response["response"]["items"]

    def get_elastigroup_active_instances(self, group_id):
        """
        Get active instances of an elastigroup

        # Arguments
        group_id (String): Elastigroup ID

        # Returns
        (Object): Elastigroup API response
        """
        content = self.send_get(
            url=self.__base_elastigroup_url +
                "/" +
                str(group_id) +
                "/status",
            entity_name='active instances')
        formatted_response = self.convert_json(
            content, self.camel_to_underscore)
        return formatted_response["response"]["items"]

    def get_elastigroup_activity(self, group_id, start_date):
        """
        Get elastigroup activity

        # Arguments
        group_id (String): Elastigroup ID
        start_date (String): Date when to start checking

        # Returns
        (Object) : Elastigroup API response
        """
        query_params = self.build_query_params_with_input({"fromDate": start_date})

        content = self.send_get(
            url=self.__base_elastigroup_url +
                "/" +
                str(group_id) +
                "/events",
            query_params=query_params,
            entity_name='active events')

        formatted_response = self.convert_json(
            content, self.camel_to_underscore)
        return formatted_response["response"]["items"]

    def roll_group(self, group_id, group_roll):
        """
        Roll an elastigroup

        # Arguments
        group_id (String): Elastigroup ID
        group_roll (ElastigroupRoll): GroupRoll Object

        # Returns
        (Object): Elastigroup API response
        """
        group_roll_request = aws_elastigroup.ElastigroupRollRequest(
            group_roll=group_roll)

        excluded_group_roll_dict = self.exclude_missing(
            json.loads(group_roll_request.toJSON()))

        formatted_group_roll_dict = self.convert_json(
            excluded_group_roll_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_roll_dict)

        roll_response = self.send_put(
            url=self.__base_elastigroup_url +
                "/" +
                str(group_id) +
                "/roll",
            body=body_json,
            entity_name='roll')

        formatted_response = self.convert_json(
            roll_response, self.camel_to_underscore)

        retVal = formatted_response["response"]

        return retVal

    def get_all_group_deployment(self, group_id):
        """
        get all group deployment from an elastigroup

        # Arguments
        group_id (String): Elastigroup ID

        # Returns
        (Object): Elastigroup API response
        """
        content = self.send_get(
            url=self.__base_elastigroup_url +
                "/" +
                str(group_id) +
                "/roll",
            entity_name='roll')

        formatted_response = self.convert_json(
            content, self.camel_to_underscore)
        return formatted_response["response"]["items"]

    def get_deployment_status(self, group_id, roll_id):
        """
        get all a deployment status from an elastigroup

        # Arguments
        group_id (String): Elastigroup ID
        roll_id (String): Deployment ID

        # Returns
        (Object): Elastigroup API response
        """
        content = self.send_get(
            url=self.__base_elastigroup_url +
                "/" +
                str(group_id) +
                "/roll/" +
                str(roll_id),
            entity_name='roll')

        formatted_response = self.convert_json(
            content, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def stop_deployment(self, group_id, roll_id):
        """
        stop a deployment from an elastigroup

        # Arguments
        group_id (String): Elastigroup ID
        roll_id (String): Deployment ID

        # Returns
        (Object): Elastigroup API response
        """
        content = self.send_put(
            url=self.__base_elastigroup_url +
                "/" +
                str(group_id) +
                "/roll/" +
                str(roll_id),
            body=json.dumps(dict(roll=dict(status="STOPPED"))),
            entity_name='roll')

        formatted_response = self.convert_json(
            content, self.camel_to_underscore)

        return formatted_response["response"]

    def create_deployment_action(self, group_id, roll_id, deployment_action):
        """
        create a deployment from an elastigroup

        # Arguments
        group_id (String): Elastigroup ID
        roll_id (String): Deployment ID
        deployment_action (Deployment): Deployment Object

        # Returns
        (Object): Elastigroup API response
        """
        deployment_action_request = spotinst_deployment_action.DeploymentActionRequest(deployment_action)

        deployment_action_dict = self.exclude_missing(
            json.loads(deployment_action_request.toJSON()))

        formatted_group = self.convert_json(
            deployment_action_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group)

        detach_response = self.send_post(
            url=self.__base_elastigroup_url +
                "/" +
                str(group_id) +
                "/roll/" +
                str(roll_id),
            body=body_json,
            entity_name='roll')

        formatted_response = self.convert_json(
            detach_response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"]

        return retVal

    def get_instance_type_by_region(self, region):
        """
        Get instance type by region

        # Arguments
        region (String): AWS region

        # Returns
        (Object): Spotinst API response
        """
        query_params = dict(region=region)
        response = self.send_get(
            url=self.__base_aws_url +
                "/spotType",
            query_params=query_params,
            entity_name="instance"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def lock_instance(self, instance_id, lock_time=None):
        """
        Lock instance

        # Arguments
        instance_id (String): Instance ID
        lock_time (int) (Optinal): Time to lock instance

        # Returns
        (Object): Spotinst API response
        """
        query_params = dict(ttlInMinutes=lock_time)

        response = self.send_post(
            url=self.__base_aws_url +
                "/instance/" +
                instance_id +
                "/lock",
            query_params=query_params,
            entity_name="instance"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["status"]

    def unlock_instance(self, instance_id):
        """
        Unlock instance

        # Arguments
        instance_id (String): Instance ID

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_post(
            url=self.__base_aws_url +
                "/instance/" +
                instance_id +
                "/unlock",
            entity_name="instance"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["status"]

    def enter_instance_standby(self, instance_id):
        """
        Enter standby for instance

        # Arguments
        instance_id (String): Instance ID

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_post(
            url=self.__base_aws_url +
                "/instance/" +
                instance_id +
                "/standby/enter",
            entity_name="instance"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["status"]

    def exit_instance_standby(self, instance_id):
        """
        Exit standby for instance

        # Arguments
        instance_id (String): Instance ID

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_post(
            url=self.__base_aws_url +
                "/instance/" +
                instance_id +
                "/standby/exit",
            entity_name="instance"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["status"]

    def get_instance_status(self, instance_id):
        """
        Get instance status

        # Arguments
        instance_id (String): Instance ID

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_get(
            url=self.__base_aws_url +
                "/instance/" +
                instance_id,
            entity_name="instance"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_instance_healthiness(self, group_id):
        """
        get all instances a healthyness from an elastigroup

        # Arguments
        group_id (String): Elastigroup ID

        # Returns
        (Object): Elastigroup API response
        """
        response = self.send_get(
            url=self.__base_elastigroup_url +
                "/" + group_id +
                "/instanceHealthiness",
            entity_name="instance"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def create_instance_signal(self, instance_id, signal):
        """
        create instance signal

        # Arguments
        instance_id (String): instance ID
        signal (String): Signal

        # Returns
        (Object): Elastigroup API response
        """
        body = json.dumps(dict(instanceId=instance_id, signal=signal))

        response = self.send_post(
            url=self.__base_aws_url +
                "/instance/signal",
            body=body,
            entity_name="instance"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["status"]

    def get_cost_per_account(self, to_date=None, from_date=None):
        """
        get cost per account

        # Arguments
        to_date (String) (Optional): to date
        from_date (String) (Optional): to date

        # Returns
        (Object): Spotinst API response
        """
        query_params = dict(toDate=to_date, fromDate=from_date)

        response = self.send_get(
            url="https://api.spotinst.io/aws/costs",
            query_params=query_params,
            entity_name="cost"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def get_cost_per_elastigroup(self, group_id, to_date=None, from_date=None):
        """
        get cost per elastigroup

        # Arguments
        group_id (String): Elastigroup ID
        to_date (String) (Optional): Start Date
        from_date (String) (Optional): End Date

        # Returns
        (Object): Elastigroup API response
        """
        query_params = dict(toDate=to_date, fromDate=from_date)

        response = self.send_get(
            url=self.__base_elastigroup_url +
                "/" + group_id +
                "/costs",
            query_params=query_params,
            entity_name="cost"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def get_group_detailed_cost(self, group_id, to_date=None, from_date=None):
        """
        get detailed cost per elastigroup

        # Arguments
        group_id (String): Elastigroup ID
        to_date (String) (Optional): Start Date
        from_date (String) (Optional): End Date

        # Returns
        (Object): Elastigroup API response
        """
        query_params = dict(toDate=to_date, fromDate=from_date)

        response = self.send_get(
            url=self.__base_elastigroup_url +
                "/" + group_id +
                "/costs/detailed",
            query_params=query_params,
            entity_name="cost"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def get_potential_savings(self):
        """
        get potential saving

        # Returns
        (Object): Elastigroup API response
        """
        response = self.send_get(
            url="https://api.spotinst.io/aws/potentialSavings",
            entity_name="saving"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def get_instance_potential_savings(self, instance_ids, region):
        """
        get potential saving

        # Arguments
        instance_ids (List): List of instance id strings
        region (String): region
        # Returns
        (Object): Elastigroup API response
        """
        instance_str = ""

        for instance in instance_ids:
            instance_str += instance + ","

        query_params = dict(region=region, instanceIds=instance_str)

        response = self.send_get(
            url="https://api.spotinst.io/aws/instancePotentialSavings",
            query_params=query_params,
            entity_name="saving"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def list_suspended_scaling_policies(self, group_id):
        """
        get suspended scaling policies for an elastigroup

        # Arguments
        group_id (String): Elastigroup ID

        # Returns
        (Object): Elastigroup API response
        """
        response = self.send_get(
            url=self.__base_elastigroup_url +
                "/" + group_id +
                "/scale/suspensions",
            entity_name="scaling policies"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def suspend_scaling_policies(self, group_id, policy_name):
        """
        suspended scaling policies for an elastigroup

        # Arguments
        group_id (String): Elastigroup ID
        policy_name (String): Scaling policy name

        # Returns
        (Object): Elastigroup API response
        """
        query_params = dict(policyName=policy_name)

        response = self.send_post(
            url=self.__base_elastigroup_url +
                "/" + group_id +
                "/scale/suspendPolicy",
            query_params=query_params,
            entity_name="scaling policies"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def resume_suspended_scaling_policies(self, group_id, policy_name):
        """
        Resume scaling policies for an elastigroup

        # Arguments
        group_id (String): Elastigroup ID
        policy_name (String): Scaling policy name

        # Returns
        (Object): Elastigroup API response
        """
        query_params = dict(policyName=policy_name)

        response = self.send_post(
            url=self.__base_elastigroup_url +
                "/" + group_id +
                "/scale/resumePolicy",
            query_params=query_params,
            entity_name="scaling policies"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["status"]

    def list_suspended_process(self, group_id):
        """
        List suspended process for an elastigroup

        # Arguments
        group_id (String): Elastigroup ID

        # Returns
        (Object): Elastigroup API response
        """
        response = self.send_get(
            url=self.__base_elastigroup_url +
                "/" + group_id +
                "/suspension",
            entity_name="suspend process"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def suspend_process(self, group_id, processes, suspensions):
        """
        suspended process for an elastigroup

        # Arguments
        group_id (String): Elastigroup ID
        processes (List): list of processes
        suspensions (List): list of suspensions

        # Returns
        (Object): Elastigroup API response
        """

        if suspensions is not None:
            if processes is not None:
                # should fail in API
                item_to_send = dict(suspensions=suspensions, processes=processes)
            else:
                item_to_send = dict(suspensions=suspensions)
        else:
            item_to_send = dict(processes=processes)

        body = json.dumps(item_to_send)

        response = self.send_post(
            url=self.__base_elastigroup_url +
                "/" + group_id +
                "/suspension",
            body=body,
            entity_name="suspend process"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def remove_suspended_process(self, group_id, processes):
        """
        remove suspended process for an elastigroup

        # Arguments
        group_id (String): Elastigroup ID
        processes (List): list of processes

        # Returns
        (Object): Elastigroup API response
        """
        body = json.dumps(dict(processes=processes))

        response = self.send_delete_with_body(
            url=self.__base_elastigroup_url +
                "/" + group_id +
                "/suspension",
            body=body,
            entity_name="suspend process"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response

    def detach_elastigroup_instances(self, group_id, detach_configuration):
        """
        Detatch instances from an elastigroup

        # Arguments
        group_id (String): Elastigroup ID
        detatch_configuration (Detach): Detach Object

        # Returns
        (Object): Elastigroup API response
        """
        group_detach_request = aws_elastigroup.ElastigroupDetachInstancesRequest(
            detach_configuration=detach_configuration)

        excluded_group_detach_dict = self.exclude_missing(
            json.loads(group_detach_request.toJSON()))

        formatted_group_detach_dict = self.convert_json(
            excluded_group_detach_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_detach_dict)

        detach_response = self.send_put(
            url=self.__base_elastigroup_url +
                "/" +
                str(group_id) +
                "/detachInstances",
            body=body_json,
            entity_name='detach')

        formatted_response = self.convert_json(
            detach_response, self.camel_to_underscore)

        retVal = formatted_response["response"]["status"]

        return retVal

    def import_stateful_instance(self, stateful_instance):
        """
        Import stateful instance parametes

        # Arguments
        stateful_instance (StatefulInstance): StatefulInstance Object

        # Returns
        (Object): Elastigroup API response
        """
        stateful_instance = spotinst_stateful.StatefulImportRequest(stateful_instance)

        excluded_group_dict = self.exclude_missing(json.loads(stateful_instance.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        group_response = self.send_post(
            body=body_json,
            url=self.__base_stateful_url,
            entity_name='import stateful instance')

        formatted_response = self.convert_json(
            group_response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def get_stateful_import_status(self, stateful_migration_id):
        """
        Get stateful instance status

        # Arguments
        stateful_migration_id (String): Stateful migration ID

        # Returns
        (Object): Elastigroup API response
        """
        content = self.send_get(
            url=self.__base_stateful_url +
                "/" +
                str(stateful_migration_id),
            entity_name='get stateful import status')

        formatted_response = self.convert_json(
            content, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def delete_stateful_import(self, stateful_migration_id):
        """
        Delete stateful instance

        # Arguments
        stateful_migration_id (String): Stateful migration ID

        # Returns
        (Object): Elastigroup API response
        """
        content = self.send_delete(
            url=self.__base_stateful_url +
                "/" +
                str(stateful_migration_id),
            entity_name='delete stateful import')

        formatted_response = self.convert_json(
            content, self.camel_to_underscore)
        return formatted_response

    def deallocate_stateful_instance(self, group_id, stateful_instance_id):
        """
        Deallocate stateful instances from an elastigroup

        # Arguments
        group_id (String): Elastigroup ID
        stateful_instance_id (String): Stateful Instance ID

        # Returns
        (Object): Elastigroup API response
        """
        content = self.send_put(
            url=self.__base_elastigroup_url +
                "/" +
                str(group_id) +
                "/statefulInstance/" +
                str(stateful_instance_id +
                    "/deallocate"),
            entity_name='deallocate stateful instance')

        formatted_response = self.convert_json(
            content, self.camel_to_underscore)
        return formatted_response["response"]

    def recycle_stateful_instance(self, group_id, stateful_instance_id):
        """
        Recycle stateful instances from an elastigroup

        # Arguments
        group_id (String): Elastigroup ID
        stateful_instance_id (String): Stateful Instance ID

        # Returns
        (Object): Elastigroup API response
        """
        content = self.send_put(
            url=self.__base_elastigroup_url +
                "/" +
                str(group_id) +
                "/statefulInstance/" +
                str(stateful_instance_id +
                    "/recycle"),
            entity_name='recycle stateful instance')

        formatted_response = self.convert_json(
            content, self.camel_to_underscore)
        return formatted_response["response"]

    def get_stateful_instances(self, group_id):
        """
        Deallocate stateful instances from an elastigroup

        # Arguments
        group_id (String): Elastigroup ID
        stateful_instance_id (String): Stateful Instance ID

        # Returns
        (Object): Elastigroup API response
        """
        content = self.send_get(
            url=self.__base_elastigroup_url +
                "/" +
                str(group_id) +
                "/statefulInstance",
            entity_name='get stateful instance')

        formatted_response = self.convert_json(
            content, self.camel_to_underscore)
        return formatted_response["response"]["items"]

    def resume_stateful_instance(self, group_id, stateful_instance_id):
        """
        Resume stateful instances from an elastigroup

        # Arguments
        group_id (String): Elastigroup ID
        stateful_instance_id (String): Stateful Instance ID

        # Returns
        (Object): Elastigroup API response
        """
        content = self.send_put(
            url=self.__base_elastigroup_url +
                "/" +
                str(group_id) +
                "/statefulInstance/" +
                str(stateful_instance_id +
                    "/resume"),
            entity_name='resume stateful instance')

        formatted_response = self.convert_json(
            content, self.camel_to_underscore)
        return formatted_response["response"]

    def pause_stateful_instance(self, group_id, stateful_instance_id):
        """
        Pause stateful instances from an elastigroup

        # Arguments
        group_id (String): Elastigroup ID
        stateful_instance_id (String): Stateful Instance ID

        # Returns
        (Object): Elastigroup API response
        """
        content = self.send_put(
            url=self.__base_elastigroup_url +
                "/" +
                str(group_id) +
                "/statefulInstance/" +
                str(stateful_instance_id) +
                "/pause",
            entity_name='pause stateful instance')

        formatted_response = self.convert_json(
            content, self.camel_to_underscore)

        return formatted_response["response"]

    def beanstalk_maintenance_status(self, group_id):
        """
        Beanstalk maintenance status

        # Arguments
        group_id (String): Elastigroup ID

        # Returns
        (Object): Elastigroup API response
        """
        status_response = self.send_get(
            url=self.__base_elastigroup_url +
                "/" +
                str(group_id) +
                "/beanstalk/maintenance/status",
            entity_name="beanstalk maintenance start")

        formatted_response = self.convert_json(
            status_response, self.camel_to_underscore)

        retVal = formatted_response["response"]["status"]

        return retVal

    def beanstalk_maintenance_start(self, group_id):
        """
        Beanstalk maintenance start

        # Arguments
        group_id (String): Elastigroup ID

        # Returns
        (Object): Elastigroup API response
        """
        start_response = self.send_put(
            url=self.__base_elastigroup_url +
                "/" +
                str(group_id) +
                "/beanstalk/maintenance/start",
            body={},
            entity_name="beanstalk maintenance start")

        formatted_response = self.convert_json(
            start_response, self.camel_to_underscore)

        retVal = formatted_response["response"]["status"]

        return retVal

    def beanstalk_maintenance_finish(self, group_id):
        """
        Beanstalk maintenance finish

        # Arguments
        group_id (String): Elastigroup ID

        # Returns
        (Object): Elastigroup API response
        """
        finish_response = self.send_put(
            url=self.__base_elastigroup_url +
                "/" +
                str(group_id) +
                "/beanstalk/maintenance/finish",
            body={},
            entity_name="beanstalk maintenance start")

        formatted_response = self.convert_json(
            finish_response, self.camel_to_underscore)

        retVal = formatted_response["response"]["status"]

        return retVal

    def beanstalk_import(self, region, env_id=None, env_name=None):
        """
        Import beanstalk attributes into JSON. Either env_id or env_name is required, both cannot be null

        # Arguments
        region (String): Beanstalk region
        env_id (String): Beanstalk env id
        env_name (String): Beanstalk env name

        # Returns
        (Object): Elastigroup API response
        """
        query_params = dict(region=region, environmentId=env_id, environmentName=env_name)

        response = self.send_get(
            url=self.__base_elastigroup_url +
                "/beanstalk/import",
            query_params=query_params,
            entity_name="beanstalk import"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def beanstalk_reimport(self, group_id):
        """
        Reimport beanstalk attributes

        # Arguments
        group_id (String): Elastigroup ID

        # Returns
        (Object): Elastigroup API response
        """
        response = self.send_put(
            url=self.__base_elastigroup_url +
                "/" + str(group_id) +
                "/beanstalk/reimport",
            entity_name="beanstalk reimport"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def import_asg(self, region, asg_name, asg, dry_run=None):
        """
        import asg attributes as JSON

        # Arguments
        region (String): ASG region
        asg_name (String): ASG Name
        asg (ASG): ASG Object
        dry_run (Bool) (Optional): if true only return JSON and not create group

        # Returns
        (Object): Elastigroup API response
        """
        query_params = dict(region=region, autoScalingGroupName=asg_name, dryRun=dry_run)

        asg = spotinst_asg.ImportASGRequest(asg)

        excluded_group_dict = self.exclude_missing(json.loads(asg.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        response = self.send_post(
            body=body_json,
            url=self.__base_elastigroup_url +
                "/autoScalingGroup/import",
            query_params=query_params,
            entity_name='import asg')

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def get_activity_events(self, group_id, from_date):
        """
        get activity events

        # Arguments
        group_id (String): Elastigroup ID
        from_date (String): From date

        # Returns
        (Object): Elastigroup API response
        """
        query_params = dict(fromDate=from_date)

        response = self.send_get(
            url=self.__base_elastigroup_url +
                "/" + group_id + "/events",
            query_params=query_params,
            entity_name="activity groups"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"]

        return retVal

    def ami_backup(self, group_id):
        """
        Start an AMI backup for Elastigroup

        # Arguments
        group_id (String): Elastigroup ID

        # Returns
        (Object): Elastigroup API response
        """
        response = self.send_post(
            url=self.__base_elastigroup_url +
                "/" + group_id + "/amiBackup",
            entity_name="ami backup"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response

        return retVal["response"]["status"]

    def create_blue_green_deployment(self, group_id, blue_green_deployment):
        """
        Start a Blue Green Deployment

        # Arguments
        group_id (String): Elastigroup ID
        blue_green_deployment (BGDeployment): Blue Green Deployment Object
        # Returns
        (Object): Elastigroup API response
        """
        blue_green_deployment = spotinst_blue_green_deployment.BlueGreenDeploymentRequest(blue_green_deployment)

        excluded_group_dict = self.exclude_missing(json.loads(blue_green_deployment.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        group_response = self.send_post(
            body=body_json,
            url=self.__base_elastigroup_url + "/" + group_id + "/codeDeploy/blueGreenDeployment",
            entity_name='create b/g deployment')

        formatted_response = self.convert_json(
            group_response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def get_blue_green_deployment(self, group_id):
        """
        Get Blue Green Deployment for an elastigroup

        # Arguments
        group_id (String): Elastigroup ID
        # Returns
        (Object): Elastigroup API response
        """
        response = self.send_get(
            url=self.__base_elastigroup_url + "/" + group_id + "/codeDeploy/blueGreenDeployment",
            entity_name="get b/g deployment")

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def stop_blue_green_deployment(self, group_id, deployment_id):
        """
        Stop Blue Green Deployment for an elastigroup

        # Arguments
        group_id (String): Elastigroup ID
        deployment_id (String):  BG Deployment ID
        # Returns
        (Object): Elastigroup API response
        """
        response = self.send_put(
            url=self.__base_elastigroup_url + "/" + group_id + "/codeDeploy/blueGreenDeployment/" + deployment_id + "/stop",
            entity_name="stop b/g deployment")

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]

        return retVal

    # endregion

    # region Functions
    def create_application(self, app):
        """
        Create Spotinst Functions Application

        # Arguments
        app (ApplicationCreate): ApplicationCreate Object
        # Returns
        (Object): Functions API response
        """
        app = spotinst_functions.ApplicationCreationRequest(app)

        excluded_group_dict = self.exclude_missing(json.loads(app.toJSON()))

        formatted_app_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_app_dict)

        self.print_output(body_json)

        app_response = self.send_post(
            body=body_json,
            url=self.__base_functions_url +
                '/application',
            entity_name='application')

        formatted_response = self.convert_json(
            app_response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def create_environment(self, env):
        """
        Create Spotinst Functions Environment

        # Arguments
        env (EnvironmentCreate): EnvironmentCreate Object
        # Returns
        (Object): Functions API response
        """
        env = spotinst_functions.EnvironmentCreationRequest(env)

        excluded_env_dict = self.exclude_missing(json.loads(env.toJSON()))

        formatted_env_dict = self.convert_json(
            excluded_env_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_env_dict)

        self.print_output(body_json)

        env_response = self.send_post(
            body=body_json,
            url=self.__base_functions_url +
                '/environment',
            entity_name='environment')

        formatted_response = self.convert_json(
            env_response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def create_function(self, fx):
        """
        Create Spotinst Functions

        # Arguments
        fx (FunctionCreate): FunctionCreate Object
        # Returns
        (Object): Functions API response
        """
        fx = spotinst_functions.FunctionCreationRequest(fx, self.should_print_output)

        excluded_fx_dict = self.exclude_missing(json.loads(fx.toJSON()))

        formatted_fx_dict = self.convert_json(
            excluded_fx_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_fx_dict)

        formatted_fx_dict['function']['code']['source'] = 'INLINE_BASE64_SOURCE_CODE'
        self.print_output(json.dumps(formatted_fx_dict))

        fx_response = self.send_post(
            body=body_json,
            url=self.__base_functions_url +
                '/function',
            entity_name='function')

        formatted_response = self.convert_json(
            fx_response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    # endregion

    # region Utils
    def print_output(self, output):
        if self.should_print_output is True:
            print(output)

    def send_get(self, url, entity_name, query_params=None):
        agent = self.resolve_user_agent()
        if query_params != None:
            query_params = self.build_query_params_with_input(query_params)
        else:
            query_params = self.build_query_params()
        headers = dict(
            {
                'User-Agent': agent,
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + self.auth_token
            }
        )

        self.print_output("Sending get request to spotinst API.")
        result = requests.get(url, params=query_params, headers=headers)

        if result.status_code == requests.codes.ok:
            self.print_output("Success")
            data = json.loads(result.content.decode('utf-8'))
            return data
        else:
            self.handle_exception("getting {}".format(entity_name), result)

    def send_delete(self, url, entity_name):
        agent = self.resolve_user_agent()
        query_params = self.build_query_params()
        headers = dict(
            {
                'User-Agent': agent,
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + self.auth_token
            }
        )

        self.print_output("Sending deletion request to spotinst API.")

        result = requests.delete(url, params=query_params, headers=headers)

        if result.status_code == requests.codes.ok:
            self.print_output("Success")
            return True
        else:
            self.handle_exception("deleting {}".format(entity_name), result)

    def send_delete_with_body(self, body, url, entity_name):
        agent = self.resolve_user_agent()
        query_params = self.build_query_params()
        headers = dict(
            {
                'User-Agent': agent,
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + self.auth_token
            }
        )

        self.print_output("Sending deletion request to spotinst API.")

        result = requests.delete(
            url,
            params=query_params,
            headers=headers,
            data=body)

        if result.status_code == requests.codes.ok:
            self.print_output("Success")
            return True
        else:
            self.handle_exception("deleting {}".format(entity_name), result)

    def send_post(self, url, entity_name, body=None, query_params=None):
        agent = self.resolve_user_agent()

        if query_params != None:
            query_params = self.build_query_params_with_input(query_params)
        else:
            query_params = self.build_query_params()

        headers = dict(
            {
                'User-Agent': agent,
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + self.auth_token
            }
        )

        self.print_output("Sending post request to spotinst API.")

        result = requests.post(
            url,
            params=query_params,
            data=body,
            headers=headers)

        if result.status_code == requests.codes.ok:
            self.print_output("Success")
            data = json.loads(result.content.decode('utf-8'))
            return data
        else:
            self.handle_exception("creating {}".format(entity_name), result)

    def send_put(self, url, entity_name, query_params=None, body=None):
        agent = self.resolve_user_agent()
        if query_params != None:
            query_params = self.build_query_params_with_input(query_params)
        else:
            query_params = self.build_query_params()
        headers = dict(
            {
                'User-Agent': agent,
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + self.auth_token
            }
        )

        self.print_output("Sending put request to spotinst API.")
        result = requests.put(
            url,
            params=query_params,
            data=body,
            headers=headers)

        if result.status_code == requests.codes.ok:
            self.print_output("Success")
            data = json.loads(result.content.decode('utf-8'))
            return data
        else:
            self.handle_exception("updating {}".format(entity_name), result)

    def send_put_with_params(self, body, url, entity_name, user_query_params):
        agent = self.resolve_user_agent()
        query_params = self.build_query_params_with_input(user_query_params)

        headers = dict(
            {
                'User-Agent': agent,
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + self.auth_token
            }
        )

        self.print_output("Sending put request to spotinst API.")

        result = requests.put(
            url,
            params=query_params,
            data=body,
            headers=headers)

        if result.status_code == requests.codes.ok:
            self.print_output("Success")
            data = json.loads(result.content.decode('utf-8'))
            return data
        else:
            self.handle_exception("updating {}".format(entity_name), result)

    def resolve_user_agent(self):
        global _SpotinstClient__spotinst_sdk_user_agent
        agent = _SpotinstClient__spotinst_sdk_user_agent
        if self.user_agent is not None:
            agent = '{}+{}'.format(self.user_agent, agent)
        return agent

    def handle_exception(self, action_string, result):
        self.print_output(result.status_code)

        if result.content == "Bad Request":
            data = dict(response=result.content)
        else:
            data = json.loads(result.content.decode('utf-8'))

        response_json = json.dumps(data["response"])
        self.print_output(response_json)

        raise SpotinstClientException(
            "Error encountered while " +
            action_string,
            response_json)

    def convert_json(self, val, convert):
        new_json = {}
        if val is None:
            return val
        elif type(val) in (int, float, bool, "".__class__, u"".__class__):
            return val

        for k, v in list(val.items()):
            new_v = v
            if isinstance(v, dict):
                new_v = self.convert_json(v, convert)
            elif isinstance(v, list):
                new_v = list()
                for x in v:
                    new_v.append(self.convert_json(x, convert))
            new_json[convert(k)] = new_v
        return new_json

    def exclude_missing(self, obj):
        # Delete keys with the value 'none' in a dictionary, recursively.

        # if obj.items() is not None:
        if obj.items() is not None:
            for key, value in list(obj.items()):

                # Remove none values
                if value == aws_elastigroup.none:
                    del obj[key]

                # Handle Objects
                elif isinstance(value, dict):
                    self.exclude_missing(obj=value)

                # Handle lists
                elif self.is_sequence(arg=value):
                    for listitem in value:
                        # Handle Lists of objects
                        try:
                            self.exclude_missing(obj=listitem)
                        except AttributeError:
                            pass
        return obj  # For convenience

    def is_sequence(self, arg):
        return (not hasattr(arg, "strip") and
                hasattr(arg, "__getitem__") or
                hasattr(arg, "__iter__"))

    def build_query_params(self):
        query_params = None
        if self.account_id is not None:
            query_params = dict({self.__account_id_key: self.account_id})

        return query_params

    def build_query_params_with_input(self, user_params):
        query_params = dict()
        if self.account_id is not None:
            query_params = dict({self.__account_id_key: self.account_id})

        if user_params is not None:
            query_params = self.merge_two_dicts(query_params, user_params)

        return query_params

    def print_output(self, output, level="debug"):
        if self.should_print_output is True:
            if level == "debug":
                self.logger.debug(output)
            if level == "info":
                self.logger.info(output)
            if level == "warn":
                self.logger.warn(output)
            if level == "error":
                self.logger.error(output)
            if level == "critical":
                self.logger.critical(output)

    @staticmethod
    def init_logger():
        logging.basicConfig(level=logging.CRITICAL)
        logger = logging.getLogger(__name__)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    def set_log_level(self, log_level):
        if log_level == None:
            level = os.environ.get(VAR_SPOTINST_LOG_LEVEL, 'critical')
        else:
            level = log_level

        if level == "debug":
            self.logger.setLevel(logging.DEBUG)
        if level == "info":
            self.logger.setLevel(logging.INFO)
        if level == "warn":
            self.logger.setLevel(logging.WARN)
        if level == "error":
            self.logger.setLevel(logging.ERROR)
        if level == "critical":
            self.logger.setLevel(logging.CRITICAL)

    @staticmethod
    def merge_two_dicts(x, y):
        z = x.copy()  # start with x's keys and values
        z.update(y)  # modifies z with y's keys and values & returns None
        return z

    def camel_to_underscore(self, name):
        return self.camel_pat.sub(lambda x: '_' + x.group(1).lower(), name)

    def underscore_to_camel(self, name):
        return self.under_pat.sub(lambda x: x.group(1).upper(), name)

    def load_credentials(self, profile, credentials_file):
        self.account_id = os.environ.get(VAR_SPOTINST_ACCOUNT, None)
        self.auth_token = os.environ.get(VAR_SPOTINST_TOKEN, None)

        if not self.auth_token:
            if not profile:
                profile = os.environ.get(VAR_SPOTINST_PROFILE, DEFAULT_PROFILE)

            if not credentials_file:
                credentials_file = os.environ.get(
                    VAR_SPOTINST_SHARED_CREDENTIALS_FILE,
                    DEFAULT_CREDENTIALS_FILE)

            with open(credentials_file, 'r') as credentials_file:
                config = yaml.load(credentials_file, Loader=yaml.SafeLoader)

                if config:
                    self.account_id = config.get(
                        profile, {}).get(
                        "account", None)
                    self.auth_token = config.get(
                        profile, {}).get("token", None)

            if not self.auth_token:
                raise SpotinstClientException("failed to load credentials")

    # endregion


class SpotinstClientException(Exception):
    def __init__(self, message, response):
        message = message + "\n" + response
        # Call the base class constructor with the parameters it needs
        super(SpotinstClientException, self).__init__(message)
