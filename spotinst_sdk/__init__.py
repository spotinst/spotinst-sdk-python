"""
This module provides utilities for importing Python objects by name.
"""
import json
import os
import re

import requests
import yaml
import logging
import argparse

from spotinst_sdk import aws_elastigroup
from spotinst_sdk import spotinst_functions
from spotinst_sdk import spotinst_emr
from spotinst_sdk import spotinst_stateful
from spotinst_sdk import spotinst_blue_green_deployment
from spotinst_sdk import spotinst_deployment_action
from spotinst_sdk import spotinst_asg

VAR_SPOTINST_SHARED_CREDENTIALS_FILE = 'SPOTINST_SHARED_CREDENTIALS_FILE'
VAR_SPOTINST_PROFILE = 'SPOTINST_PROFILE'
VAR_SPOTINST_TOKEN = 'SPOTINST_TOKEN'
VAR_SPOTINST_ACCOUNT = 'SPOTINST_ACCOUNT'

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
    __base_url = "https://api.spotinst.io/aws/ec2"
    __base_elastigroup_url = "https://api.spotinst.io/aws/ec2/group"
    __base_emr_url = "https://api.spotinst.io/aws/emr/mrScaler"
    __base_functions_url = "https://api.spotinst.io/functions"
    __base_stateful_url = "https://api.spotinst.io/aws/ec2/statefulMigrationGroup"
    __base_kube_url = "https://api.spotinst.io/mcs/kubernetes/cluster"
    __base_saving_url = "https://api.spotinst.io/aws/potentialSavings"

    camel_pat = re.compile(r'([A-Z])')
    under_pat = re.compile(r'_([a-z])')

    # region Constructor
    def __init__(self, auth_token=None,
                 account_id=None,
                 profile=None,
                 credentials_file=None,
                 print_output=True,
                 log_level="critical",
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
        options = self.get_args()

        if options:
            self.set_log_level(options)
        else:
            self.set_log_level(log_level)


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
        query_params = self.build_query_params_with_input({"toDate":to_date, "fromDate":from_date})

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

    def update_elastigroup(self, group_update, group_id):
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

        group_response = self.send_put(
            self.__base_elastigroup_url +
            "/" +
            group_id,
            entity_name='elastigroup',
            body=body_json)

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

    def delete_elastigroup_with_deallocation(
            self, group_id, stateful_deallocation):
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
        query_params = self.build_query_params_with_input({"fromDate":start_date})

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
                "/roll/"+
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
                "/roll/"+
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
                "/roll/"+
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
            url=self.__base_url+
            "/spotType",
            query_params=query_params,
            entity_name="instance"
        )

        formatted_response = self.convert_json(
            response, self. camel_to_underscore)

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
        query_params= dict(ttlInMinutes=lock_time)

        response = self.send_post(
            url=self.__base_url +
            "/instance/" +
            instance_id +
            "/lock",
            query_params=query_params,
            entity_name="instance"
        )

        formatted_response = self.convert_json(
            response, self. camel_to_underscore)

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
            url=self.__base_url +
            "/instance/" +
            instance_id +
            "/unlock",
            entity_name="instance"
        )
        
        formatted_response = self.convert_json(
            response, self. camel_to_underscore)

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
            url=self.__base_url + 
            "/instance/" + 
            instance_id +
            "/standby/enter",
            entity_name="instance"
        )

        formatted_response = self.convert_json(
            response, self. camel_to_underscore)

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
            url=self.__base_url + 
            "/instance/" + 
            instance_id +
            "/standby/exit",
            entity_name="instance"
        )

        formatted_response = self.convert_json(
            response, self. camel_to_underscore)

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
            url=self.__base_url + 
            "/instance/" +
            instance_id,
            entity_name="instance"
        )

        formatted_response = self.convert_json(
            response, self. camel_to_underscore)

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
            response, self. camel_to_underscore)

        return formatted_response["response"]["items"][0]  


    def create_instance_signal(self, instance_id, signal):

        body = dict(instanceId=instance_id, signal=signal)

        response = self.send_post(
            url= self.__base_url + 
            "/instance/signal",
            body=body,
            entity_name="instance"
        )

        formatted_response = self.convert_json(
            response, self. camel_to_underscore)

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
        query_params=dict(toDate=to_date, fromDate=from_date)

        response = self.send_get(
            url="https://api.spotinst.io/aws/costs",
            query_params=query_params,
            entity_name="cost"
        )

        formatted_response = self.convert_json(
            response, self. camel_to_underscore)

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
        query_params=dict(toDate=to_date, fromDate=from_date)

        response = self.send_get(
            url=self.__base_elastigroup_url +
            "/" + group_id +
            "/costs",
            query_params=query_params,
            entity_name="cost"
        )

        formatted_response = self.convert_json(
            response, self. camel_to_underscore)

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
        query_params=dict(toDate=to_date, fromDate=from_date)

        response = self.send_get(
            url=self.__base_elastigroup_url +
            "/" + group_id +
            "/costs/detailed",
            query_params=query_params,
            entity_name="cost"
        )

        formatted_response = self.convert_json(
            response, self. camel_to_underscore)

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
            response, self. camel_to_underscore)

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
            response, self. camel_to_underscore)

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
            response, self. camel_to_underscore)

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
            response, self. camel_to_underscore)

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
            response, self. camel_to_underscore)

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
            response, self. camel_to_underscore)

        return formatted_response["response"]["items"]

    def suspend_process(self, group_id, processes, suspensions):
        body = dict(suspensions=suspensions, processes=processes)
        
        response = self.send_post(
            url=self.__base_elastigroup_url +
            "/" + group_id + 
            "/suspension",
            body=body,
            entity_name="suspend process"
        )

        formatted_response = self.convert_json(
            response, self. camel_to_underscore)

        return formatted_response["response"]["items"]

    def remove_suspended_process(self, group_id, processes):
        body = dict(processes=processes)

        response = self.send_delete(
            url=self.__base_elastigroup_url +
            "/" + group_id + 
            "/suspension",
            body=body,
            entity_name="suspend process"
        )

        formatted_response = self.convert_json(
            response, self. camel_to_underscore)

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
            url=self.__base_elastigroup_url+
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
            url=self.__base_elastigroup_url+
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
            url=self.__base_elastigroup_url+
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
            url=self.__base_elastigroup_url+
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
            url= self.__base_elastigroup_url + "/" + group_id + "/codeDeploy/blueGreenDeployment",
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

    def send_get(self, url,entity_name,query_params=None):
        agent = self.resolve_user_agent()
        query_params = query_params or self.build_query_params()
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

    def send_delete(self, url, entity_name, body=None):
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

        result = requests.delete(url, params=query_params, body=body, headers=headers)

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
        query_params = query_params or self.build_query_params()
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

    def send_put(self, url, entity_name, body=None):
        agent = self.resolve_user_agent()
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

    @staticmethod
    def get_args():
        parser = argparse.ArgumentParser(description='Options for Spotinst python-sdk')
        parser.add_argument('--log-level',
                            choices=["debug", "info", "warn", "error", "critical"],
                            help='set log level: debug, info, warn, error, critical')
        args = parser.parse_args()
        return args

    def set_log_level(self, args):
        level = vars(args)['log_level']

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
                config = yaml.load(credentials_file)

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
