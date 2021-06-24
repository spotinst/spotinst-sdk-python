# Change Log
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).

## [1.0.56] - 2021-06-23
### Added
 - New credentials file format: `INI` ([#84](https://github.com/spotinst/spotinst-sdk-python/pull/84))

## [1.0.54] - 2021-03-07
### Added
 - Model aws.groupRoll.strategy

### Fixed
 - Fixed aws.groupRoll.strategy field, it should be a json and not a string

## [1.0.53] - 2020-12-15
### Added
 - field aws.emr.coreGroup.capacity.unit
 - field aws.emr.taskGroup.capacity.unit

### Fixed
 - Fixed aws.emr.masterGroup documentation, it mentioned a field that didn't exist
 
## [1.0.52] - 2020-12-07
### Added 
- field aws.group.compute.launchSpecification.blockDeviceMappings.ebs.throughput

## [1.0.45] - 2019-04-02
### Added 
- get_elastilog for aws eg

### Updated
- README with v2 info

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
 

