[![Build Status](https://travis-ci.org/spotinst/spotinst-sdk-python.svg?branch=master)](https://travis-ci.org/spotinst/spotinst-sdk-python)
[![Coverage Status](https://coveralls.io/repos/github/spotinst/spotinst-sdk-python/badge.svg?branch=master)](https://coveralls.io/github/spotinst/spotinst-sdk-python?branch=master)
[![Python 2.7](https://img.shields.io/badge/python-2.7-blue.svg)](https://www.python.org/downloads/release/python-270/)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

# spotinst-sdk-python
Spotinst SDK for the Python programming language

# **V2 Is Coming!**
Version 2 for the Spotinst Python SDK will be merging into the master branch very soon. This is a breaking change from version 1 and will require updates if switching over. Luckily this process should be easy and is completly explained on the [v2 branch in this repository](https://github.com/spotinst/spotinst-sdk-python/tree/v2). 

## Table of contents
<!--ts-->
   * [Installation](#installation)
   * [Configuring Credentials](#configuring-credentials)
   * [SDK Docs](./docs/pydocmd/)
     * [Endpoints](./docs/pydocmd/endpoints/)
       * [Elastigroup](./docs/pydocmd/endpoints/elastigroup/)
       * [Functions](./docs/pydocmd/endpoints/functions/)
       * [Administration](./docs/pydocmd/endpoints/administration/)
       * [Multai Load Balancer](./docs/pydocmd/endpoints/mlb)
       * [Ocean](./docs/pydocmd/endpoints/ocean)
     * [Examples](./docs/pydocmd/examples/)
     * [Classes](./docs/pydocmd/classes/)
       * [ASG](./docs/pydocmd/classes/asg.md)
       * [Deployment](./docs/pydocmd/classes/deployment.md)
       * [Deployment Action](./docs/pydocmd/classes/deployment_action.md)
       * [Elastigroup](./docs/pydocmd/classes/elastigroup.md)
       * [EMR](./docs/pydocmd/classes/emr.md) 
       * [Functions](./docs/pydocmd/classes/functions.md)
       * [MLB](./docs/pydocmd/classes/mlb.md)
       * [Stateful](./docs/pydocmd/classes/stateful.md)
       * [User Mapping](./docs/pydocmd/classes/user_mapping.md)
       * [Ocean](./docs/pydocmd/classes/ocean.md)
       * [Event Subscription](./docs/pydocmd/classes/event_subscription.md)
<!--te-->

## Installation
```bash
pip install --upgrade spotinst-sdk
```

## Configuring Credentials
The mechanism in which the sdk looks for credentials is to search through a list of possible locations and stop as soon as it finds credentials. 
The order in which the sdk searches for credentials is:
  1. Passing credentials as parameters to the `SpotinstClient()` constructor
- example
```python
client = SpotinstClient(auth_token='token', account_id='act-123')
```

  2. Fetching the account and token from environment variables under `SPOTINST_ACCOUNT` & `SPOTINST_TOKEN`

If you choose to not pass your credentials directly you configure a credentials file, this file should be a valid `.yml` file.
The default shared credential file location is `~/.spotinst/credentials` and the default profile is `default`
- example
```yaml
default: #profile
  token: $defaul_spotinst_token
  account: $default_spotinst-account-id
my_profle:
  token: $my_spotinst_token
  account: $my_spotinst-account-id
```

  3. You can overwrite the credentials file location and the profile used as parameters in the `SpotinstClient()` constructor
- example
```python
client = SpotinstClient(credentials_file='/path/to/file', profile='my_profile')
```
  
  4. You can overwrite the credentials file location and the profile used as environment variables `SPOTINST_PROFILE` and/or `SPOTINST_SHARED_CREDENTIALS_FILE`
  5. Fetching from the default location with the default profile
  
