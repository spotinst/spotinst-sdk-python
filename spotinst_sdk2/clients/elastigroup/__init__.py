import json

from spotinst_sdk2.client import Client

# region AWS imports
import spotinst_sdk2.models.elastigroup.aws as aws_elastigroup
import spotinst_sdk2.models.elastigroup.aws.stateful as aws_stateful
import spotinst_sdk2.models.elastigroup.aws.deployment as aws_deployment
import spotinst_sdk2.models.elastigroup.aws.deployment_action as aws_deployment_action
import spotinst_sdk2.models.elastigroup.aws.asg as aws_asg
# endregion

# region GCP imports
import spotinst_sdk2.models.elastigroup.gcp as gcp_elastigroup
import spotinst_sdk2.models.elastigroup.gcp.gke as gcp_gke
# endregion

# region Azure imports
import spotinst_sdk2.models.elastigroup.azure as azure_elastigroup
import spotinst_sdk2.models.elastigroup.azure.task as azure_task
# endregion

# region AWS
class ElastigroupAwsClient(Client):
    __base_elastigroup_url = "https://api.spotinst.io/aws/ec2/group"
    __base_aws_url = "https://api.spotinst.io/aws/ec2"
    __base_stateful_url = "https://api.spotinst.io/aws/ec2/statefulMigrationGroup"

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
        deployment_action_request = aws_deployment_action.DeploymentActionRequest(deployment_action)

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
        query_params=dict(toDate=to_date, fromDate=from_date)

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

        retVal = formatted_response["response"]["items"]

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

        asg = aws_asg.ImportASGRequest(asg)

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
        blue_green_deployment = aws_deployment.BlueGreenDeploymentRequest(blue_green_deployment)

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

    # region AWS
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
            url=self.__base_aws_url+
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
        query_params= dict(ttlInMinutes=lock_time)

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
            url= self.__base_aws_url + 
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
        query_params=dict(toDate=to_date, fromDate=from_date)

        response = self.send_get(
            url=self.__base_aws_url + "/costs",
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
            url=self.__base_aws_url +"/potentialSavings",
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
            url=self.__base_aws_url + "/instancePotentialSavings",
            query_params=query_params,
            entity_name="saving"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"] 

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
        query_params=dict(toDate=to_date, fromDate=from_date, severity=severity, 
            resource_id=resource_id, limit=limit)

        result = self.send_get(url=geturl, entity_name='elastilog', query_params=query_params)

        formatted_response = self.convert_json(
            result, self.camel_to_underscore)

        return formatted_response["response"]["items"]
    # endregion

    # region stateful
    def import_stateful_instance(self, stateful_instance):
        """
        Import stateful instance parametes
        
        # Arguments
        stateful_instance (StatefulInstance): StatefulInstance Object
        
        # Returns
        (Object): Elastigroup API response 
        """
        stateful_instance = aws_stateful.StatefulImportRequest(stateful_instance)

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
    # endregion
# endregion


# region GCP
class ElastigroupGcpClient(Client):
    __base_elastigroup_url = "https://api.spotinst.io/gcp/gce/group"

    def create_elastigroup(self, group):
        """
        Create an elastigroup
        
        # Arguments
        group (Elastigroup): Elastigroup Object
        
        # Returns
        (Object): Elastigroup API response 
        """    
        group = gcp_elastigroup.ElastigroupCreationRequest(group)

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

    def update_elastigroup(self, group_update, group_id):
        """
        Update an elastigroup
        
        # Arguments
        group_id (String): Elastigroup ID
        group_update (Elastigroup): Elastigroup Object
        
        # Returns
        (Object): Elastigroup API response 
        """
        group = gcp_elastigroup.ElastigroupCreationRequest(group_update)

        excluded_group_update_dict = self.exclude_missing(
            json.loads(group.toJSON()))

        formatted_group_update_dict = self.convert_json(
            excluded_group_update_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_update_dict)

        self.print_output(body_json)

        group_response = self.send_put(
            body=body_json, 
            url=self.__base_elastigroup_url + "/" + group_id, 
            entity_name='elastigroup'
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
    
    # region Scale
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
    # endregion

    # region Deploy
    def roll_group(self, group_id, group_roll):
        """
        Roll an elastigroup
        
        # Arguments
        group_id (String): Elastigroup ID
        group_roll (ElastigroupRoll): GroupRoll Object
        
        # Returns
        (Object): Elastigroup API response 
        """
        group_roll_request = gcp_elastigroup.ElastigroupRollRequest(
            group_roll=group_roll)

        excluded_group_roll_dict = self.exclude_missing(
            json.loads(group_roll_request.toJSON()))

        formatted_group_roll_dict = self.convert_json(
            excluded_group_roll_dict, self.underscore_to_camel)

        roll_response = self.send_put(
            url=self.__base_elastigroup_url +
                "/" + str(group_id) + "/roll",
            body=json.dumps(formatted_group_roll_dict),
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
    # endregion

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
            response, self.camel_to_underscore)

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

    def import_gke(self, location, gke_id, gke):
        """
        import gke attributes as JSON
        
        # Arguments
        location (String): GKE location
        gke_id (String): GKE ID
        gke (GKE): GKE Object
        
        # Returns
        (Object): Elastigroup API response 
        """ 
        query_params = dict(location=location, clusterId=gke_id)

        gke = gcp_gke.ImportGKERequest(gke)

        excluded_group_dict = self.exclude_missing(json.loads(gke.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)
        print(body_json)
        response = self.send_post(
            body=body_json,
            url=self.__base_elastigroup_url+
            "/gke/import",
            query_params=query_params,
            entity_name='import gke')

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def detach_elastigroup_instances(self, group_id, detach_configuration):
        """
        Detatch instances from an elastigroup
        
        # Arguments
        group_id (String): Elastigroup ID
        detatch_configuration (Detach): Detach Object
        
        # Returns
        (Object): Elastigroup API response 
        """        
        group_detach_request = gcp_elastigroup.ElastigroupDetachInstancesRequest(
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
# endregion


# region Azure
class ElastigroupAzureClient(Client):
    __base_elastigroup_url = "https://api.spotinst.io/compute/azure/group"
    __base_task_url = "https://api.spotinst.io/azure/compute/task"

    def create_elastigroup(self, group):
        """
        Create an elastigroup
        
        # Arguments
        group (Elastigroup): Elastigroup Object
        
        # Returns
        (Object): Elastigroup API response 
        """    
        group = azure_elastigroup.ElastigroupCreationRequest(group)

        excluded_group_dict = self.exclude_missing(json.loads(group.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        group_response = self.send_post(
            body=body_json,
            url=self.__base_elastigroup_url,
            entity_name='elastigroup')

        formatted_response = self.convert_json(
            group_response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def update_elastigroup(self, group_update, group_id):
        """
        Update an elastigroup
        
        # Arguments
        group_id (String): Elastigroup ID
        group_update (Elastigroup): Elastigroup Object
        
        # Returns
        (Object): Elastigroup API response 
        """
        group = azure_elastigroup.ElastigroupCreationRequest(group_update)

        excluded_group_update_dict = self.exclude_missing(
            json.loads(group.toJSON()))

        formatted_group_update_dict = self.convert_json(
            excluded_group_update_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_update_dict)

        self.print_output(body_json)

        group_response = self.send_put(
            body=body_json, 
            url=self.__base_elastigroup_url + "/" + group_id, 
            entity_name='elastigroup'
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

    # region Deploy
    def roll_group(self, group_id, group_roll):
        """
        Roll an elastigroup
        
        # Arguments
        group_id (String): Elastigroup ID
        group_roll (ElastigroupRoll): GroupRoll Object
        
        # Returns
        (Object): Elastigroup API response 
        """
        group_roll_request = azure_elastigroup.ElastigroupRollRequest(
            group_roll=group_roll)

        excluded_group_roll_dict = self.exclude_missing(
            json.loads(group_roll_request.toJSON()))

        formatted_group_roll_dict = self.convert_json(
            excluded_group_roll_dict, self.underscore_to_camel)

        roll_response = self.send_put(
            url=self.__base_elastigroup_url +
                "/" + str(group_id) + "/roll",
            body=json.dumps(formatted_group_roll_dict),
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
    # endregion


    # region Scale
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
        return formatted_response["response"]

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
        return formatted_response["response"]
    # endregion


    # region Task
    def create_task(self, task):
        """
        Create a scheduling task
        
        # Arguments
        task (Task): Task Object
        
        # Returns
        (Object): Task API response 
        """    
        task = azure_task.TaskCreationRequest(task)

        excluded_group_dict = self.exclude_missing(json.loads(task.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        group_response = self.send_post(
            body=json.dumps(formatted_group_dict),
            url=self.__base_task_url,
            entity_name='task')

        formatted_response = self.convert_json(
            group_response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def update_task(self, task_update, task_id):
        """
        Update a scheduling Task
        
        # Arguments
        task_id (String): Task ID
        task_update (Elastigroup): Task Object
        
        # Returns
        (Object): Task API response 
        """
        task = azure_task.TaskCreationRequest(task_update)

        excluded_group_update_dict = self.exclude_missing(
            json.loads(task.toJSON()))

        formatted_group_update_dict = self.convert_json(
            excluded_group_update_dict, self.underscore_to_camel)

        group_response = self.send_put(
            body=json.dumps(formatted_group_update_dict), 
            url=self.__base_task_url + "/" + task_id, 
            entity_name='task'
        )

        formatted_response = self.convert_json(
            group_response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def get_task(self, task_id):
        """
        Get a Task
        
        # Arguments
        task_id(String): Task ID
       
        # Returns
        (Object): Task API response 
        """
        result = self.send_get(
            url=self.__base_task_url + "/" + task_id, 
            entity_name='task')

        formatted_response = self.convert_json(
            result, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def get_all_tasks(self):
        """
        Get all Tasks
        # Returns
        (Object): Task API response 
        """
        result = self.send_get(
            url=self.__base_task_url + "/", 
            entity_name='task')

        formatted_response = self.convert_json(
            result, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def delete_task(self, task_id):
        """
        Delete a scheduling task
        
        # Arguments
        task_id (String): Task ID
        
        # Returns
        (Object): Task API response 
        """
        response = self.send_delete(
            url= self.__base_task_url + "/" + task_id, 
            entity_name='task')

        return response
    # endregion


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

    def detach_elastigroup_instances(self, group_id, detach_configuration):
        """
        Detatch instances from an elastigroup
        
        # Arguments
        group_id (String): Elastigroup ID
        detatch_configuration (Detach): Detach Object
        
        # Returns
        (Object): Elastigroup API response 
        """
        group_detach_request = azure_elastigroup.ElastigroupDetachInstancesRequest(
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

# endreion