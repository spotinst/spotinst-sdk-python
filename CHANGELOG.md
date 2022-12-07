# Change Log
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).

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
 

