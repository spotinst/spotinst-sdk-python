# Change Log
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).

## [2.1.31] - 2023-04-03
### Added
- Add support for AWS Ocean API: `fetch_rightsizing_recommendations`
- Add request and response logging in client at DEBUG level.
### Fixed
- Fixed issue of adding multiple streamhandlers for each client.

## [2.1.30] - 2023-03-19
### Added
- Add `immediate_o_d_recover_threshold` field in `Strategy` model in spotinst_sdk2.models.elastigroup.aws

## [2.1.29] - 2023-03-06
### Added
- Add support for AWS Managed Instance API: `import_multiple_instances_from_aws`
- Add support for AWS Managed Instance API: `get_multiple_instances_migration_status`

## [2.1.28] - 2023-03-03
### Added
- Add `cpu_options`, `auto_healing`, `metadata_options` fields in `LaunchSpecification` model in spotinst_sdk2.models.elastigroup.aws

### Fixed
- Changed `health_check_types` to string list in `Health` model in spotinst_sdk2.models.stateful_node

## [2.1.27] - 2023-02-24
### Fixed
- TypeError in spotinst_sdk2.models.stateful_node

## [2.1.26] - 2023-02-16
### Added
- Add support for Azure Stateful Node APIs

## [2.1.25] - 2023-02-13
### Added
- Add support for remaining Azure V3 APIs: 
`get_elastigroup_status`, `get_vm_healthiness`, `suspend_elastigroup`, `resume_elastigroup`,
`start_deployment`, `get_all_deployments`, `get_deployment`, `get_deployment_status`, 
`import_from_scale_set`, `import_from_virtual_machine`, `import_from_load_balancer`,
`import_from_application_gateway`, `create_vm_signal`, `get_elastilog`

## [2.1.24] - 2023-02-10
### Fixed
- Fixed the parameter annotation of `update_managed_instance_states` API

## [2.1.23] - 2023-02-10
### Fixed
- Fixed the parameter type of `update_managed_instance_states` API
- Modified the return object of `update_managed_instance_states` API 

## [2.1.22] - 2023-02-03
### Added
- Add support for AWS Managed Instance API: `get_managed_instance_costs`
- Add support for AWS Managed Instance API: `delete_volume_in_managed_instance`
- Add support for AWS Managed Instance API: `update_managed_instance_states`

## [2.1.21] - 2022-12-15
### Added
- Add support for Azure V3 CRUD APIs

## [2.1.20] - 2022-12-7
### Added
- Add support for AWS Managed Instance API: `get_managed_instance_status`

## [2.1.19] - 2022-10-18
### Added
- Add support for AWS Elastigroup compute-> launchSpecification field: `images`
- Add support for AWS Elastigroup strategy field: `utilizeCommitments`

## [2.1.18] - 2022-07-18
### Added
- Add support for Ocean AWS field: `aggregatedCosts`

## [2.1.17] - 2022-01-31
### Added
- Add support for Ocean AWS LaunchSpec field: `loadBalancers`

### Fixed
- correctly classify v2's minimum Python version

## [2.1.16] - 2021-11-22
### Added
- Add support for Elastigroup Scaling field: `multipleMetrics`
- Add support for Elastigroup Scaling Up/Down field: `stepAdjustments`
- Add support for Elastigroup Scaling Up/Down field: `isEnabled`
- Add support for Elastigroup Scaling Up field: `minTarget capacity`
- Add support for Elastigroup Scaling Up field: `maxTarget capacity`
- Add support for Elastigroup Scaling Up field: `shouldResumeStateful`

## [2.1.15] - 2021-11-10
### Fixed
- Change the api call made by elastigroup aws `get_deployment_status`

## [2.1.14] - 2021-11-02
### Added
- Add support for Elastigroup field: `resourceTagSpecification`

## [2.1.13] - 2021-10-12
### Added
- Add support for timeout parameter. defaults to "None"

## [2.1.12] - 2021-07-13
### Fixed
 - Properly populate message in client exception
 - Type annotation for Managed Instance object

## [2.1.11] - 2021-07-04
### Added
 - Managed Instance load balancer config can be initialized without arguments

## [2.1.10] - 2021-06-30
### Added
 - Add support for Managed Instance (AWS)

## [2.1.9] - 2021-06-24
### Added
 - New credentials file format: `INI` ([#84](https://github.com/spotinst/spotinst-sdk-python/pull/84))

## [2.1.8] - 2021-06-23
### Added
 - Model setup.azure.AzureCredentials
 - Model setup.azure.AzureSetCredentialsRequest
 - Model setup.gcp.GcpCredentials
 - Model setup.gcp.GcpCredentials.ServiceAccount
 - Model setup.gcp.GcpSetCredentialsRequest
 - Client setup for aws to handle credentials routes
 - Client setup for azure to handle credentials routes
 - Client setup for gcp to handle credentials routes

### Deprecated
 - Credentials routes for aws under admin client

## [2.1.7] - 2021-04-25
### Added
 - Added aws create external id route to admin client

## [2.1.6] - 2021-03-07
### Added
 - Model aws.groupRoll.strategy

### Fixed
 - Fixed aws.groupRoll.strategy field, it should be a json and not a string

## [2.1.5] - 2020-12-15
### Added
 - field aws.emr.coreGroup.capacity.unit
 - field aws.emr.taskGroup.capacity.unit

### Fixed
 - Fixed aws.emr.masterGroup documentation, it mentioned a field that didn't exist

## [2.1.4] - 2020-12-03
### Added
 - get all ocean right sizing recommendations
 - field aws.group.compute.launchSpecification.blockDeviceMappings.ebs.throughput

### Fixed
 - process suspension by user
 - License and documentation

### Removed
 - field aws.group.strategy.scalingStrategy.terminate_at_end_of_billing_hour from documentation

## [2.1.3] - 2020-12-01
### Added
 - field aws.group.strategy.scalingStrategy.terminationPolicy
 - field aws.group.compute.launchSpecification.blockDeviceMappings.ebs.dynamicVolumeSize

### Removed
 - field aws.group.strategy.scalingStrategy.terminate_at_end_of_billing_hour from documentation

## [2.1.2] - 2019-04-02
### Added
 - get_elastilog for aws client
 - hpcGridEngine to azure eg model

## [2.1.1] - 2019-02-29
### Added
 - last 13 Azure endpoints

## [2.0.1] - 2019-02-24
### Updated
 - Changed single client to multiple clients
 - Added Session object
 - Moved models to /models dir

### Added
 - gcp client with all endpoints
 - azure client with 5/18 endpoints

## [1.0.44] - 2019-02-04
### Added
 - Event subscription endpoints

### Updated
 - `auto_apply_tags` parameter added to update EG
 - `managed_actions` parameter added to beanstalk EG


## [1.0.44] - 2019-01-24
### Updated
 - Emr support new strategy type, cluster object and additional computer parameters

### Added
 - `create_ocean_cluster`
 - `update_ocean_cluster`
 - `get_all_ocean_cluster`
 - `get_ocean_cluster`
 - `delete_ocean_cluster`
 - parameter credit_specification to EG schema

## [1.0.43] - NA

## [1.0.42] - 2018-11-09
### Commits
 - [src] - fixing documentation
 - [src] - removing argparse from SDK
 - [src] - adding log level to ENV

## [1.0.41] - 2018-11
### Added
 - Logger using standard logging module
 - "--log-level" command line argument (more info in "--help")
 - "log_level" constructor parameter, defaults to "critical"
 - Created changelog

### New
 - Documentation for the entire project

## [1.0.40] - 2018-10-22
### Added
 - kubernetes api calls
 - b/g deployment api calls
 - beanstalk api calls
 - stateful api calls
 - process and scaling policy api calls
 - deployment api calls
 - instance api calls
 - cost api calls
 - other misc api calls

## [1.0.39] - 2018-10-04
### Updated
 - update_elastigroup() had error with the send_put() request arguments

## [1.0.38] - 2018-09-28
### Added
 - version to Rancher integration

## [1.0.37] - 2018-09-21
### Added
 - `get_deployment_status` 
 - `get_elastigroup_activity` 
 - `import_stateful_instance`
 - `get_stateful_import_status`
 - `delete_stateful_import`
 - `deallocate_stateful_instance`
 - `recycle_stateful_instance` 
 - `get_stateful_instances` 
 - `resume_stateful_instance`
 - `pause_stateful_instance`
 - testing for `__init__.py`
 

