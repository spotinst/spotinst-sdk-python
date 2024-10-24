import json

from spotinst_sdk2.client import Client

# region AWS imports
import spotinst_sdk2.models.elastigroup.aws as aws_elastigroup
import spotinst_sdk2.models.elastigroup.aws.stateful as aws_stateful
import spotinst_sdk2.models.elastigroup.aws.deployment as aws_deployment
import spotinst_sdk2.models.elastigroup.aws.deployment_action as aws_deployment_action
import spotinst_sdk2.models.elastigroup.aws.asg as aws_import
# endregion

# region GCP imports
import spotinst_sdk2.models.elastigroup.gcp as gcp_elastigroup
# endregion

# region Azure V3 imports
import spotinst_sdk2.models.elastigroup.azure_v3 as azure_v3_elastigroup


# endregion

# region AWS


class ElastigroupAwsClient(Client):
    __base_elastigroup_url = "/aws/ec2/group"
    __base_aws_url = "/aws/ec2"
    __base_stateful_url = "/aws/ec2/statefulMigrationGroup"

    # region Elastigroup
    def create_elastigroup(self, group, async_scale=None):
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

        group_response = self.send_post_with_params(
            body=body_json,
            url=self.__base_elastigroup_url,
            entity_name='elastigroup',
            user_query_params=dict(asyncScale=async_scale))

        formatted_response = self.convert_json(
            group_response, self.camel_to_underscore)

        ret_val = formatted_response["response"]["items"][0]

        return ret_val

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

        group_response = self.send_put_with_params(
            body=body_json,
            url=self.__base_elastigroup_url + "/" + group_id,
            entity_name='elastigroup',
            user_query_params=dict(autoApplyTags=auto_apply_tags)
        )

        formatted_response = self.convert_json(
            group_response, self.camel_to_underscore)

        ret_val = formatted_response["response"]["items"][0]

        return ret_val

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
        Get all elastigroups

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
        query_params = self.build_query_params_with_input(
            {"fromDate": start_date})

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

        ret_val = formatted_response["response"]

        return ret_val

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
            str(roll_id) +
            "/status",
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
        deployment_action_request = aws_deployment_action.DeploymentActionRequest(
            deployment_action)

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

        ret_val = formatted_response["response"]["items"]

        return ret_val

    def get_instance_healthiness(self, group_id):
        """
        Get a list of instances with health status.

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
                item_to_send = dict(suspensions=suspensions,
                                    processes=processes)
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

        ret_val = formatted_response["response"]["status"]

        return ret_val

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

    def delete_volume_in_stateful_instance(self, group_id, stateful_instance_id, volume_id):
        """
        Delete stateful instance 

        # Arguments
        group_id (String): Elastigroup ID
        stateful_instance_id (String): Stateful Instance ID
        volume_id (String): Volume ID

        # Returns
        (Object): Elastigroup API response 
        """
        return self.send_delete(
            url=self.__base_elastigroup_url +
            "/" +
            str(group_id) +
            "/statefulInstance/" +
            str(stateful_instance_id) +
            "/volume/" +
            str(volume_id),
            entity_name='delete volume in stateful instance')

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

        ret_val = formatted_response["response"]["items"]

        return ret_val

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

        ret_val = formatted_response["response"]["status"]

        return ret_val

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

        ret_val = formatted_response["response"]["status"]

        return ret_val

    def beanstalk_import(self, region, env_id=None, env_name=None):
        """
        Import beanstalk attributes into JSON. Either env_id or env_name is 
        required, both cannot be null

        # Arguments
        region (String): Beanstalk region
        env_id (String): Beanstalk env id
        env_name (String): Beanstalk env name

        # Returns
        (Object): Elastigroup API response 
        """
        query_params = dict(
            region=region, environmentId=env_id, environmentName=env_name)

        response = self.send_get(
            url=self.__base_elastigroup_url +
            "/beanstalk/import",
            query_params=query_params,
            entity_name="beanstalk import"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        ret_val = formatted_response["response"]["items"][0]

        return ret_val

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

        ret_val = formatted_response["response"]["items"][0]

        return ret_val

    def import_instance(self, region, instance_id, instance: aws_import.ImportInstanceConfig):
        """
        Import an EC2 instance into a new Elastigroup

        # Arguments
        region (String): Instance Region
        instance_id (String): Instance ID
        instance (ImportInstanceConfig): Import Configuration

        # Returns
        (Object): Elastigroup API response 
        """
        query_params = dict(
            region=region, instanceId=instance_id)

        request = aws_import.ImportInstanceRequest(instance)

        excluded_group_dict = self.exclude_missing(
            json.loads(request.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        response = self.send_post(
            body=body_json,
            url=self.__base_elastigroup_url +
            "/instance/import",
            query_params=query_params,
            entity_name='import instance')

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        ret_val = formatted_response["response"]["items"][0]

        return ret_val

    def import_asg(self, region, asg_name, asg: aws_import.ASG, dry_run=None):
        """
        Create a new Elastigroup using the configuration of an existing Autoscaling group

        # Arguments
        region (String): ASG region
        asg_name (String): ASG Name
        asg (ASG): ASG Object
        dry_run (Bool) (Optional): if true only return JSON and not create group

        # Returns
        (Object): Elastigroup API response 
        """
        query_params = dict(
            region=region, autoScalingGroupName=asg_name, dryRun=dry_run)

        asg = aws_import.ImportASGRequest(asg)

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

        ret_val = formatted_response["response"]["items"][0]

        return ret_val

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

        ret_val = formatted_response["response"]["items"]

        return ret_val

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

        ret_val = formatted_response

        return ret_val["response"]["status"]

    def create_blue_green_deployment(self, group_id, blue_green_deployment):
        """
        Start a Blue Green Deployment

        # Arguments
        group_id (String): Elastigroup ID
        blue_green_deployment (BGDeployment): Blue Green Deployment Object
        # Returns
        (Object): Elastigroup API response 
        """
        blue_green_deployment = aws_deployment.BlueGreenDeploymentRequest(
            blue_green_deployment)

        excluded_group_dict = self.exclude_missing(
            json.loads(blue_green_deployment.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        group_response = self.send_post(
            body=body_json,
            url=self.__base_elastigroup_url + "/" +
            group_id + "/codeDeploy/blueGreenDeployment",
            entity_name='create b/g deployment')

        formatted_response = self.convert_json(
            group_response, self.camel_to_underscore)

        ret_val = formatted_response["response"]["items"][0]

        return ret_val

    def get_blue_green_deployment(self, group_id):
        """
        Get Blue Green Deployment for an elastigroup

        # Arguments
        group_id (String): Elastigroup ID
        # Returns
        (Object): Elastigroup API response 
        """
        response = self.send_get(
            url=self.__base_elastigroup_url + "/" +
            group_id + "/codeDeploy/blueGreenDeployment",
            entity_name="get b/g deployment")

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        ret_val = formatted_response["response"]["items"][0]

        return ret_val

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
            url=self.__base_elastigroup_url + "/" + group_id +
            "/codeDeploy/blueGreenDeployment/" + deployment_id + "/stop",
            entity_name="stop b/g deployment")

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        ret_val = formatted_response["response"]

        return ret_val

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
            url=self.__base_aws_url + "/potentialSavings",
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
        severity (String) (Optional): Log level severity
        resource_id (String) (Optional): Filter log extracted entires related to a
          specific resource id
        limit(String) (Optional): Maximum number of lines to extract in a response

        # Returns
        (Object): Elastigroup API response 
        """
        geturl = self.__base_elastigroup_url + "/" + group_id + "/logs"
        query_params = dict(toDate=to_date, fromDate=from_date, severity=severity,
                            resource_id=resource_id, limit=limit)

        result = self.send_get(
            url=geturl, entity_name='elastilog', query_params=query_params)

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
        stateful_instance = aws_stateful.StatefulImportRequest(
            stateful_instance)

        excluded_group_dict = self.exclude_missing(
            json.loads(stateful_instance.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        group_response = self.send_post(
            body=body_json,
            url=self.__base_stateful_url,
            entity_name='import stateful instance')

        formatted_response = self.convert_json(
            group_response, self.camel_to_underscore)

        ret_val = formatted_response["response"]["items"][0]

        return ret_val

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
    __base_elastigroup_url = "/gcp/gce/group"
    __base_gcp_url = "/gcp/gce"

    def create_elastigroup(self, group: gcp_elastigroup.Elastigroup):
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

        group_response = self.send_post(
            body=body_json,
            url=self.__base_elastigroup_url,
            entity_name='elastigroup')

        formatted_response = self.convert_json(
            group_response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def update_elastigroup(self, group_update: gcp_elastigroup.Elastigroup, group_id: str):
        """
        Update an GCP Elastigroup

        # Arguments
        group_id (String): Elastigroup ID
        group_update (Elastigroup): Elastigroup Object

        # Returns
        (Object): Elastigroup API response 
        """
        group = gcp_elastigroup.ElastigroupUpdateRequest(group_update)

        excluded_group_update_dict = self.exclude_missing(
            json.loads(group.toJSON()))

        formatted_group_update_dict = self.convert_json(
            excluded_group_update_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_update_dict)

        group_response = self.send_put(
            body=body_json,
            url=self.__base_elastigroup_url + "/" + group_id,
            entity_name='elastigroup'
        )

        formatted_response = self.convert_json(
            group_response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def delete_elastigroup(self, group_id: str):
        """
        Delete an Elastigroup GCP

        # Arguments
        group_id (String): Elastigroup ID

        # Returns
        (Object): Elastigroup API response 
        """
        delurl = self.__base_elastigroup_url + "/" + group_id
        response = self.send_delete(url=delurl, entity_name='elastigroup')
        return response

    def get_elastigroup(self, group_id: str):
        """
        List all properties for single GCP Elastigroup

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
        List all GCP Elastigroups for a Spot Account

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
    def scale_elastigroup_up(self, group_id: str, adjustment: int):
        """
        Add instances to the Elastigroup

        # Arguments
        group_id (String): Elastigroup ID
        adjustment (int): The number of instances to add to the group

        # Returns
        (Object): Elastigroup API response 
        """
        query_params = dict({"adjustment": adjustment})
        content = self.send_put_with_params(
            url=self.__base_elastigroup_url + "/" + group_id + "/scale/up",
            entity_name='elastigroup (scale up)',
            body=None,
            user_query_params=query_params)

        formatted_response = self.convert_json(
            content, self.camel_to_underscore)
        return formatted_response["response"]["items"]

    def scale_elastigroup_down(self, group_id: str, adjustment: int):
        """
        Remove instances from the Elastigroup

        # Arguments
        group_id (String): Elastigroup ID
        adjustment (int): Ammount to scale group

        # Returns
        (Object): Elastigroup API response 
        """
        query_params = dict({"adjustment": adjustment})
        content = self.send_put_with_params(
            url=self.__base_elastigroup_url + "/" + group_id + "/scale/down",
            entity_name='elastigroup (scale down)',
            body=None,
            user_query_params=query_params)

        formatted_response = self.convert_json(
            content, self.camel_to_underscore)
        return formatted_response["response"]["items"]
    # endregion

    # region Deploy
    def roll_group(self, group_id: str, group_roll: gcp_elastigroup.RollGroup):
        """
        Deploy the Elastigroup: Triggers a Blue/Green deployment that replaces the existing instances in the Elastigroup

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
            url=self.__base_elastigroup_url + "/" + group_id + "/roll",
            body=json.dumps(formatted_group_roll_dict),
            entity_name='roll')

        formatted_response = self.convert_json(
            roll_response, self.camel_to_underscore)

        return formatted_response["response"]

    def get_all_group_deployment(self, group_id: str):
        """
        Get all the deployments for a specific Elastigroup, and their status

        # Arguments
        group_id (String): Elastigroup ID

        # Returns
        (Object): Elastigroup API response 
        """
        content = self.send_get(
            url=self.__base_elastigroup_url + "/" + group_id + "/roll",
            entity_name='roll')

        formatted_response = self.convert_json(
            content, self.camel_to_underscore)
        return formatted_response["response"]["items"]

    def get_deployment_status(self, group_id: str, roll_id: str):
        """
        Get a specific deployment's status

        # Arguments
        group_id (String): The Spot Elastigroup ID you want to update
        roll_id (String): The deployment ID to query

        # Returns
        (Object): Elastigroup API response 
        """
        content = self.send_get(
            url=self.__base_elastigroup_url + "/" + group_id + "/roll/" + roll_id,
            entity_name='roll')

        formatted_response = self.convert_json(
            content, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def stop_deployment(self, group_id: str, roll_id: str):
        """
        Stop an existing deployment

        # Arguments
        group_id (String): Elastigroup ID
        roll_id (String): Deployment ID

        # Returns
        (Object): Elastigroup API response 
        """
        content = self.send_put(
            url=self.__base_elastigroup_url + "/" + group_id + "/roll/" + roll_id,
            body=json.dumps(dict(roll=dict(status="STOPPED"))),
            entity_name='roll')

        formatted_response = self.convert_json(
            content, self.camel_to_underscore)

        return formatted_response["response"]
    # endregion

    def get_elastigroup_active_instances(self, group_id: str):
        """
        Get the status for all instances that are memebers of the Elastigroup

        # Arguments
        group_id (String): Elastigroup ID

        # Returns
        (Object): Elastigroup API response 
        """
        content = self.send_get(
            url=self.__base_elastigroup_url +
            "/" +
            group_id +
            "/status",
            entity_name='active instances')
        formatted_response = self.convert_json(
            content, self.camel_to_underscore)
        return formatted_response["response"]["items"]

    def get_cost_per_elastigroup(self, group_id: str, to_date: str, from_date: str):
        """
        Get financial information on a specific Elastigroup

        # Arguments
        group_id (String): Elastigroup ID
        to_date (String) (Optional): Get items on or before this date (ISO 8601 or Unix timestamp)
        from_date (String) (Optional): Get items on or after this date (ISO 8601 or Unix timestamp)

        # Returns
        (Object): Elastigroup API response 
        """
        query_params = dict(toDate=to_date, fromDate=from_date)

        response = self.send_get(
            url=self.__base_elastigroup_url + "/" + group_id + "/costs",
            query_params=query_params,
            entity_name="cost"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def get_elastigroup_activity(self, group_id: str, start_date: str, end_date: str):
        """
        Get all activity events for the Elastigroup

        # Arguments
        group_id (String): Elastigroup ID
        start_date (String): Date when to start checking
        end_date (String): Get items on or before this date (ISO 8601)

        # Returns
        (Object) : Elastigroup API response 
        """
        query_params = dict(fromDate=start_date, toDate=end_date)

        content = self.send_get(
            url=self.__base_elastigroup_url + "/" + group_id + "/events",
            query_params=query_params,
            entity_name='active events')

        formatted_response = self.convert_json(
            content, self.camel_to_underscore)
        return formatted_response["response"]["items"]

    def detach_elastigroup_instances(self, group_id: str, detach_configuration: gcp_elastigroup.DetachConfiguration):
        """
        Detach instances from an Elastigroup

        # Arguments
        group_id (String): Elastigroup ID
        detatch_configuration (DetachConfiguration): DetachConfiguration Object

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
            url=self.__base_elastigroup_url + "/" + group_id + "/detachInstances",
            body=body_json,
            entity_name='detach')

        formatted_response = self.convert_json(
            detach_response, self.camel_to_underscore)

        return formatted_response["response"]["status"]

    def get_elastilog(self, group_id: str, start_date: str, end_date: str, limit: int):
        """
        Fetch a group's Elastilog

        # Arguments
        group_id (String): Elastigroup ID
        start_date (String): Get items on or after this date (ISO 8601 or Unix timestamp)
        end_date (String): Get items on or before this date (ISO 8601 or Unix timestamp)
        limit (Integer): Maximum number of items to return.

        # Returns
        (Object): Elastigroup API response
        """
        query_params = self.build_query_params_with_input(
            {"fromDate": start_date, "toDate": end_date, "limit": limit})

        content = self.send_get(
            url=self.__base_elastigroup_url + "/" + group_id + "/log",
            query_params=query_params,
            entity_name='active events')

        formatted_response = self.convert_json(
            content, self.camel_to_underscore)
        return formatted_response["response"]["items"]

    def get_cost_per_account(self, start_date: str, end_date: str):
        """
        Retrieve costs up to one year back per specified account over a specified time period.

        # Arguments
        start_date (String): The start date of the requested time period. The value cannot be earlier than 1 year back.
        end_date (String): The end date of the requested time period. The maximum of time period length is 90 days.

        # Returns
        (Object): Cost per Account Response
        """
        query_params = dict(fromDate=start_date, toDate=end_date)

        content = self.send_get(
            url=self.__base_gcp_url + "/costs/",
            query_params=query_params,
            entity_name='account cost')

        formatted_response = self.convert_json(
            content, self.camel_to_underscore)
        return formatted_response["response"]["items"]

    def get_instance_status(self, instance_id: str):
        """
        Get the current instance status. Possible status values: ACTIVE, TERMINATING

        # Arguments
        instance_id (String): GCP Instance ID

        # Returns
        (Object) Elastigroup API Response
        """
        content = self.send_get(
            url=self.__base_gcp_url + "/instance/" + instance_id,
            entity_name='instance status')

        formatted_response = self.convert_json(
            content, self.camel_to_underscore)
        return formatted_response["response"]["items"][0]

    def lock_instance(self, instance_id: str, ttl_in_minutes: str):
        """
        Set termination protection for a specific instance.

        # Arguments
        instance_id (String): GCP Instance ID
        ttl_in_minutes (String): Specify a TTL (in minutes) for this lock, i.e.: for how long the protection will be valid for.

        # Returns
        (Object) Spotinst API Response
        """
        query_params = dict(ttlInMinutes=ttl_in_minutes)

        response = self.send_post_with_params(
            url=self.__base_gcp_url + "/instance/" + instance_id + "/lock",
            user_query_params=query_params,
            entity_name="lock instance",
            body=None
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["status"]

    def unlock_instance(self, instance_id: str):
        """
        Remove termination protection for a specific instance.

        # Arguments
        instance_id (String): GCP Instance ID

        # Returns
        (Object): Spotinst API response
        """
        response = self.send_post(
            url=self.__base_gcp_url + "/instance/" + instance_id + "/unlock",
            entity_name="unlock instance"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["status"]
# endregion


# region Azure V3
class ElastigroupAzureV3Client(Client):
    __base_elastigroup_url = "/azure/compute/group"

    def create_elastigroup(self, group):
        """
        Create an elastigroup

        # Arguments
        group (Elastigroup): Elastigroup Object

        # Returns
        (Object): Elastigroup API response 
        """
        group = azure_v3_elastigroup.ElastigroupCreateRequest(group)

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

        return formatted_response["response"]["items"][0]

    def update_elastigroup(self, group_update, group_id):
        """
        Update an elastigroup

        # Arguments
        group_id (String): Elastigroup ID
        group_update (Elastigroup): Elastigroup Object

        # Returns
        (Object): Elastigroup API response
        """
        group = azure_v3_elastigroup.ElastigroupUpdateRequest(group_update)

        excluded_group_update_dict = self.exclude_missing(
            json.loads(group.toJSON()))

        formatted_group_update_dict = self.convert_json(
            excluded_group_update_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_update_dict)

        group_response = self.send_put(
            body=body_json,
            url=self.__base_elastigroup_url + "/" + group_id,
            entity_name='elastigroup'
        )

        formatted_response = self.convert_json(
            group_response, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def delete_elastigroup(self, group_id):
        """
        Delete an elastigroup

        # Arguments
        group_id (String): Elastigroup ID

        # Returns
        (Object): Elastigroup API response
        """
        delurl = self.__base_elastigroup_url + "/" + group_id
        return self.send_delete(url=delurl, entity_name='elastigroup')

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
        Get all elastigroups

        # Returns
        (List): List of Elastigroup API response
        """
        content = self.send_get(
            url=self.__base_elastigroup_url, entity_name='elastigroup')
        formatted_response = self.convert_json(
            content, self.camel_to_underscore)
        return formatted_response["response"]["items"]

    def update_elastigroup_capacity(self, group_id, capacity):
        """
        Update capacity of Elastigroups

        # Arguments
        group_id (String): Elastigroup ID
        capacity: Capacity Object

        # Returns
        (Object): Elastigroup API response
        """
        update_capacity_request = azure_v3_elastigroup.ElastigroupUpdateCapacityRequest(
            capacity=capacity)

        excluded_update_capacity_dict = self.exclude_missing(
            json.loads(update_capacity_request.toJSON()))

        formatted_update_capacity_dict = self.convert_json(
            excluded_update_capacity_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_update_capacity_dict)

        response = self.send_put(url=self.__base_elastigroup_url + "/" +
                                 str(group_id) + "/capacity",
                                 body=body_json,
                                 entity_name='update capacity')

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]

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

    def detach_elastigroup_vms(self, group_id, detach_configuration):
        """
        Detach VMs from an elastigroup

        # Arguments
        group_id (String): Elastigroup ID
        detach_configuration (Detach): DetachConfiguration Object

        # Returns
        (Object): Elastigroup API response
        """
        detach_request = azure_v3_elastigroup.ElastigroupDetachVMsRequest(
            detach_configuration=detach_configuration)

        excluded_detach_dict = self.exclude_missing(
            json.loads(detach_request.toJSON()))

        formatted_detach_dict = self.convert_json(
            excluded_detach_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_detach_dict)

        detach_response = self.send_put(
            url=self.__base_elastigroup_url +
            "/" + str(group_id) + "/detachVms",
            body=body_json,
            entity_name='detach')

        formatted_response = self.convert_json(
            detach_response, self.camel_to_underscore)

        ret_val = formatted_response["response"]

        return ret_val

    def protect_virtual_machine(self, group_id, vm_name, ttl_in_minutes=None):
        """
        Protect virtual machines in Elastigroup cluster.

        # Arguments
        group_id (String): Elastigroup ID
        vm_name (String): VM ID
        ttl_in_minutes (int) (Optional): How long protection will be valid

        # Returns
        (Object): Spotinst API response
        """
        query_params = dict(ttlInMinutes=ttl_in_minutes)

        response = self.send_post(url=self.__base_elastigroup_url +
                                  "/" + str(group_id) +
                                  "/vm/" + str(vm_name) + "/protection",
                                  query_params=query_params,
                                  entity_name="virtual machine"
                                  )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["status"]

    def unprotect_virtual_machine(self, group_id, vm_name):
        """
        Un-Protect virtual machines in Elastigroup cluster.

        # Arguments
        group_id (String): Elastigroup ID
        vm_name (String): VM ID

        # Returns
        (Object): Spotinst API response
        """
        return self.send_delete(url=self.__base_elastigroup_url +
                                "/" + str(group_id) +
                                "/vm/" + str(vm_name) + "/protection",
                                entity_name="virtual machine")

    def get_elastigroup_status(self, group_id):
        """
        Get status of Elastigroup cluster.

        # Arguments
        group_id (String): Elastigroup ID

        # Returns
        (Object): Elastigroup API response
        """
        content = self.send_get(url=self.__base_elastigroup_url + "/" + group_id + "/status",
                                entity_name='elastigroup')
        formatted_response = self.convert_json(
            content, self.camel_to_underscore)
        return formatted_response["response"]["items"][0]

    def get_vm_healthiness(self, group_id):
        """
        Get a list of vms with health status.

        # Arguments
        group_id (String): Elastigroup ID

        # Returns
        (Object): Elastigroup API response
        """
        response = self.send_get(
            url=self.__base_elastigroup_url +
            "/" + group_id +
            "/vmHealthiness",
            entity_name="instance"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["items"]

    def suspend_elastigroup(self, group_id, processes):
        """
        Suspends the Group.

        # Arguments
        group_id (String): Elastigroup ID
        processes (List): List of processes to create or update their suspensions

        # Returns
        (Object): Spotinst API response
        """
        processes_request = azure_v3_elastigroup.ElastigroupProcessesRequest(
            processes=processes)

        excluded_process_dict = self.exclude_missing(
            json.loads(processes_request.toJSON()))

        formatted_process_dict = self.convert_json(
            excluded_process_dict, self.underscore_to_camel)

        body = json.dumps(formatted_process_dict)

        response = self.send_put(
            url=self.__base_elastigroup_url + "/" + group_id + "/suspend",
            body=body,
            entity_name='suspend')

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["status"]

    def resume_elastigroup(self, group_id, processes):
        """
        Resumes the Group.

        # Arguments
        group_id (String): Elastigroup ID
        processes (List): List of processes to cancel their suspensions

        # Returns
        (Object): Spotinst API response
        """
        processes_request = azure_v3_elastigroup.ElastigroupProcessesRequest(
            processes=processes)

        excluded_process_dict = self.exclude_missing(
            json.loads(processes_request.toJSON()))

        formatted_process_dict = self.convert_json(
            excluded_process_dict, self.underscore_to_camel)

        body = json.dumps(formatted_process_dict)

        response = self.send_put(
            url=self.__base_elastigroup_url + "/" + group_id + "/resume",
            body=body,
            entity_name='resume')

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["status"]

    def start_deployment(self, group_id, deployment):
        """
        Deploy the Elastigroup.
        This triggers a Blue/Green deployment that replaces the existing VMs in the Elastigroup.

        # Arguments
        group_id (String): Elastigroup ID
        deployment: DeploymentConfiguration Object

        # Returns
        (Object): Elastigroup API response
        """
        start_deployment_request = azure_v3_elastigroup.ElastigroupDeploymentRequest(
            deployment_configuration=deployment)

        excluded_start_deployment_dict = self.exclude_missing(
            json.loads(start_deployment_request.toJSON()))

        formatted_start_deployment_dict = self.convert_json(
            excluded_start_deployment_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_start_deployment_dict)

        response = self.send_post(url=self.__base_elastigroup_url + "/" +
                                  str(group_id) + "/deployment",
                                  body=body_json,
                                  entity_name='start deployment')

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]

    def get_all_deployments(self, group_id, limit=None, sort=None):
        """
        Get a list of all the deployments of a specific Elastigroup and the status of each one.

        # Arguments
        group_id (String): Elastigroup ID
        limit (integer): Limits the number of deployments returned. Default: 5
        sort (String): Field by which to sort the results. Default: createdAt:DESC

        # Returns
        (Object) : Elastigroup API response
        """
        query_params = self.build_query_params_with_input(
            {"LIMIT": limit, "SORT": sort})

        content = self.send_get(
            url=self.__base_elastigroup_url +
            "/" +
            str(group_id) +
            "/deployment",
            query_params=query_params,
            entity_name='deployments')

        formatted_response = self.convert_json(
            content, self.camel_to_underscore)
        return formatted_response["response"]["items"]

    def get_deployment(self, group_id, deployment_id):
        """
        Get the status of a specific deployment.

        # Arguments
        group_id (String): Elastigroup ID
        deployment_id (String): The deployment ID you want to query

        # Returns
        (Object) : Elastigroup API response
        """
        content = self.send_get(
            url=self.__base_elastigroup_url +
            "/" +
            str(group_id) +
            "/deployment/" +
            deployment_id,
            entity_name='deployment')

        formatted_response = self.convert_json(
            content, self.camel_to_underscore)
        return formatted_response["response"]["items"][0]

    def get_deployment_status(self, group_id, deployment_id):
        """
        Get the detailed status of a specific deployment.
        This includes status details per batch and other information.

        # Arguments
        group_id (String): Elastigroup ID
        deployment_id (String): The deployment ID you want to query

        # Returns
        (Object) : Elastigroup API response
        """
        content = self.send_get(
            url=self.__base_elastigroup_url +
            "/" +
            str(group_id) +
            "/deployment/" +
            deployment_id +
            "/details",
            entity_name='deployment')

        formatted_response = self.convert_json(
            content, self.camel_to_underscore)
        return formatted_response["response"]

    def import_from_scale_set(self, resource_group_name, scale_set_name):
        """
        Given a scale set, constructs a valid group configuration based on the
          scale set and returns it.

        # Arguments
        resource_group_name (String): Resource Group Name
        scale_set_name (String): Scale Set Name

        # Returns
        (Object): Elastigroup API response
        """
        geturl = self.__base_elastigroup_url + "/import/resourceGroup/" + resource_group_name \
            + "/scaleSet/" + scale_set_name
        result = self.send_get(url=geturl, entity_name='elastigroup')

        formatted_response = self.convert_json(
            result, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def import_from_virtual_machine(self, resource_group_name, virtual_machine_name):
        """
        Given a virtual machine, constructs a valid group configuration based on the 
        virtual machine and returns it.

        # Arguments
        resource_group_name (String): Resource Group Name
        virtual_machine_name (String): Virtual Machine Name

        # Returns
        (Object): Elastigroup API response
        """
        geturl = self.__base_elastigroup_url + "/import/resourceGroup/" + resource_group_name \
            + "/virtualMachine/" + virtual_machine_name
        result = self.send_get(url=geturl, entity_name='elastigroup')

        formatted_response = self.convert_json(
            result, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def import_from_load_balancer(self, backend_pool_name, load_balancer_name, resource_group_name):
        """
        Given a load balancer, constructs a valid group configuration and returns it.

        # Arguments
        resource_group_name (String): Resource Group Name
        load_balancer_name (String): Virtual Machine Name
        backend_pool_name (String): Backend Pool Name

        # Returns
        (Object): Elastigroup API response
        """
        geturl = self.__base_elastigroup_url + "/import/resourceGroup/" + resource_group_name \
            + "/loadBalancer/" + load_balancer_name + "/backendPool/" + backend_pool_name
        result = self.send_get(url=geturl, entity_name='elastigroup')

        formatted_response = self.convert_json(
            result, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def import_from_application_gateway(self, backend_pool_name, application_gateway_name,
                                        resource_group_name):
        """
        Given a load balancer, constructs a valid group configuration and returns it.

        # Arguments
        resource_group_name (String): Resource Group Name
        application_gateway_name (String): Application Gateway Name
        backend_pool_name (String): Backend Pool Name

        # Returns
        (Object): Elastigroup API response
        """
        geturl = self.__base_elastigroup_url + "/import/resourceGroup/" + resource_group_name \
            + "/applicationGateway/" + application_gateway_name + \
            "/backendPool/" + backend_pool_name
        result = self.send_get(url=geturl, entity_name='elastigroup')

        formatted_response = self.convert_json(
            result, self.camel_to_underscore)

        return formatted_response["response"]["items"][0]

    def create_vm_signal(self, vm_name, signal_type):
        """
        The VM signal API is used for notifying Spot about the VM state so that
          Spot can act accordingly

        # Arguments
        vm_name (String): The virtual machine ID the signal refers to.
        signal_type (String): Signal Type (Enum: "vmReady" "vmReadyToShutdown")

        # Returns
        (Object): Elastigroup API response
        """
        body = json.dumps(dict(vmName=vm_name, signalType=signal_type))

        response = self.send_post(
            url="/azure/compute/vm/signal",
            body=body,
            entity_name="vm signal"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        return formatted_response["response"]["status"]

    def get_elastilog(self, group_id, from_date, to_date, severity=None,
                      resource_id=None, limit=None):
        """
        Get an elastilog for a specific elastigroup

        # Arguments
        group_id(String): Elastigroup ID
        to_date (String): to date
        from_date (String): from date
        severity(String) (Optional): Log level severity
        resource_id(String) (Optional): Filter log extracted entires 
        related to a specific resource id
        limit(String) (Optional): Maximum number of lines to extract in a response

        # Returns
        (Object): Elastigroup API response
        """
        geturl = self.__base_elastigroup_url + "/" + group_id + "/logs"
        query_params = dict(toDate=to_date, fromDate=from_date, SEVERITY=severity,
                            RESOURCE_ID=resource_id, limit=limit)

        result = self.send_get(
            url=geturl, entity_name='elastilog', query_params=query_params)

        formatted_response = self.convert_json(
            result, self.camel_to_underscore)

        return formatted_response["response"]["items"]

        # endregion
