# Change Log
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).

## [1.0.41] - UNRELEASED
### Added
- Logger using standard logging module
- "--log-level" command line argument (more info in "--help")
- "log_level" constructor parameter, defaults to "critical"
- Created changelog

## [1.0.40] - 2018-20-22
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
 

