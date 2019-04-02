# Elastigroup Clients
Client used to perform requests for Spotinst Elastigroup

## [ElastigroupAwsClient](./elastigroup_aws_client.md)
### session.client("elastigroup_aws")

 * create_elastigroup
 * update_elastigroup
 * delete_elastigroup
 * delete_elastigroup_with_deallocation
 * get_elastigroup
 * get_elastigroups
 * get_elastigroup_active_instances
 * get_elastigroup_activity
 * get_instance_healthiness
 * create_instance_signal
 * suspend_process
 * remove_suspended_process
 * list_suspended_process
 * detach_elastigroup_instances
 * import_asg
 * get_activity_events
 * ami_backup
 * scale_elastigroup_up
 * scale_elastigroup_down
 * list_suspended_scaling_policies
 * suspend_scaling_policies
 * resume_suspended_scaling_policies
 * roll_group
 * get_deployment_status
 * stop_deployment
 * create_deployment_action
 * get_instance_type_by_region
 * lock_instance
 * unlock_instance
 * enter_instance_standby
 * exit_instance_standby
 * get_instance_status
 * get_cost_per_account
 * get_potential_savings
 * get_instance_potential_savings
 * get_cost_per_elastigroup
 * get_group_detailed_cost
 * beanstalk_maintenance_status
 * beanstalk_maintenance_start
 * beanstalk_maintenance_finish
 * beanstalk_import 
 * create_blue_green_deployment
 * get_blue_green_deployment
 * stop_blue_green_deployment
 * deallocate_stateful_instance
 * recycle_stateful_instance
 * get_stateful_instances
 * resume_stateful_instance
 * pause_stateful_instance
 * import_stateful_instance
 * get_stateful_import_status
 * delete_stateful_import
 * get_elastilog

## [ElastigroupGcpClient](./elastigroup_gcp_client.md)
### session.client("elastigroup_gcp")

 * create_elastigroup
 * get_elastigroup
 * get_elastigroups
 * update_elastigroup
 * delete_elastigroup
 * scale_elastigroup_up
 * scale_elastigroup_down
 * detach_elastigroup_instances
 * import_gke
 * roll_group
 * get_all_group_deployment
 * get_deployment_status
 * stop_deployment
 * get_elastigroup_active_instances
 * get_cost_per_elastigroup
 * get_elastigroup_activity

## [ElastigroupAzureClient](./elastigroup_azure_client.md)
### session.client("elastigroup_azure")

 * create_elastigroup
 * get_elastigroup
 * get_elastigroups
 * update_elastigroup
 * delete_elastigroup



