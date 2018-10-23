# Elastigroup

## Functions

### [AWS](./aws/)

#### [Core](./aws/core.md)
 * SpotinstClient.create_elastigroup
 * SpotinstClient.update_elastigroup
 * SpotinstClient.delete_elastigroup
 * SpotinstClient.delete_elastigroup_with_deallocation
 * SpotinstClient.get_elastigroup
 * SpotinstClient.get_elastigroups
 * SpotinstClient.get_elastigroup_active_instances
 * SpotinstClient.get_elastigroup_activity
 * SpotinstClient.get_instance_healthiness
 * SpotinstClient.list_suspended_process
 * SpotinstClient.detach_elastigroup_instances
 * SpotinstClient.import_asg
 * SpotinstClient.get_activity_events
 * SpotinstClient.ami_backup
 * SpotinstClient.scale_elastigroup_up
 * SpotinstClient.scale_elastigroup_down
 * SpotinstClient.list_suspended_scaling_policies
 * SpotinstClient.suspend_scaling_policies
 * SpotinstClient.resume_suspended_scaling_policies
 * SpotinstClient.roll_group
 * SpotinstClient.get_deployment_status
 * SpotinstClient.stop_deployment
 * SpotinstClient.create_deployment_action
 * SpotinstClient.get_kubernetes_cluster_cost
 * SpotinstClient.get_instance_type_by_region
 * SpotinstClient.lock_instance
 * SpotinstClient.unlock_instance
 * SpotinstClient.enter_instance_standby
 * SpotinstClient.exit_instance_standby
 * SpotinstClient.get_instance_status
 * SpotinstClient.get_cost_per_account
 * SpotinstClient.get_potential_savings
 * SpotinstClient.get_instance_potential_savings
 * SpotinstClient.get_cost_per_elastigroup
 * SpotinstClient.get_group_detailed_cost

#### [Beanstalk](./aws/beanstalk.md)
 * SpotinstClient.beanstalk_maintenance_status
 * SpotinstClient.beanstalk_maintenance_start
 * SpotinstClient.beanstalk_maintenance_finish
 * SpotinstClient.beanstalk_import 

#### [Code Deploy](./aws/codedeploy.md)
 * SpotinstClient.create_blue_green_deployment
 * SpotinstClient.get_blue_green_deployment
 * SpotinstClient.stop_blue_green_deployment

#### [Stateful](./aws/stateful.md)
 * SpotinstClient.deallocate_stateful_instance
 * SpotinstClient.recycle_stateful_instance
 * SpotinstClient.get_stateful_instances
 * SpotinstClient.resume_stateful_instance
 * SpotinstClient.pause_stateful_instance
 * SpotinstClient.import_stateful_instance
 * SpotinstClient.get_stateful_import_status
 * SpotinstClient.delete_stateful_import

#### [EMR](./aws/emr.md)
 * SpotinstClient.create_emr