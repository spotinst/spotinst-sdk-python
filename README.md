[![Build Status](https://travis-ci.org/spotinst/spotinst-sdk-python.svg?branch=master)](https://travis-ci.org/spotinst/spotinst-sdk-python)
[![Coverage Status](https://coveralls.io/repos/github/spotinst/spotinst-sdk-python/badge.svg?branch=master)](https://coveralls.io/github/spotinst/spotinst-sdk-python?branch=master)
[![Python 2.7](https://img.shields.io/badge/python-2.7-blue.svg)](https://www.python.org/downloads/release/python-270/)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

# spotinst-sdk-python
Spotinst SDK for the Python programming language

## Breaking Change: Version 2.x.x

The new Spotinst Python SDK comes with a few breaking changes but do not fear, here we will explain all you need to know to make sure you can go right back in buisness in no time. 

 * There is no longer the `SpotinstClient()` class which was used to validate your credentials and make requests all in one
 * Now there is the `SpotinstSession()` class which is used to validate credentials. [Configure Session Docs](#Configuring-Session)
 * From the session object you can create client objects which correlate to specific Spotinst Services and are used to make requests. [Setup Clients Docs](#Setup-Clients)
 * Some methods required you to pass in a Model object

Here is a basic example of how to create an Ocean cluster using the Ocean Client and the Ocean Models

```python
from spotinst_sdk import SpotinstSession
from spotinst_sdk.models.ocean.aws import *

session = SpotinstSession()
client = session.client("ocean_aws")

################ Compute ################
launch_specification = LaunchSpecifications(security_group_ids=["sg-12345"],
 image_id="ami-12345", key_pair="Noam-key")

instance_types = InstanceTypes(whitelist=["c4.8xlarge"])

compute = Compute(instance_types=instance_types, 
  subnet_ids=["subnet-1234"], launch_specification=launch_specification)

################ Strategy ################

strategy = Strategy(utilize_reserved_instances=False, fallback_to_od=True, spot_percentage=100)

################ Capacity ################

capacity = Capacity(minimum=0, maximum=0, target=0)

################# Ocean #################

ocean = Ocean(name="Ocean SDK Test", controller_cluster_id="ocean.k8s", 
  region="us-west-2", capacity=capacity, strategy=strategy, compute=compute)

client.create_ocean_cluster(ocean=ocean)
```

In the [SDK Client documentation](./docs/pydocmd/clients/) you can view what methods are supported by each client. <br>
For information on what models are supported checkout the [SDK Model documentation](./docs/pydocmd/models/). <br>
More examples can be found in the [SDK Examples Documentation](./docs/pydocmd/examples/). <br>

## Table of contents
<!--ts-->
   * [Installation](#installation)
   * [Configuring Session](#configuring-session)
   * [Setup Clients](#setup-clients)
   * [SDK Docs](./docs/pydocmd/)
     * [Examples](./docs/pydocmd/examples/)
     * [Clients](./docs/pydocmd/clients/)
       * [Administration](./docs/pydocmd/clients/admin/)
       * [Elastigroup](./docs/pydocmd/clients/elastigroup/)
       * [Functions](./docs/pydocmd/clients/functions/)
       * [MCS](./docs/pydocmd/clients/mcs/)
       * [MLB](./docs/pydocmd/clients/mlb/)
       * [MrScaler](./docs/pydocmd/clients/mrscaler/)
       * [Ocean](./docs/pydocmd/clients/ocean/)
       * [Subscription](./docs/pydocmd/clients/subscription/)
     * [Models](./docs/pydocmd/models/)
       * [Administration](./docs/pydocmd/models/admin.md)
       * [Elasitgroups](./docs/pydocmd/models/elastigroup/)
       * [Functions](./docs/pydocmd/models/functions.md)
       * [MLB](./docs/pydocmd/models/mlb.md)
       * [MrScalers](./docs/pydocmd/models/mrscaler/)
       * [Oceans](./docs/pydocmd/models/ocean/)
       * [Subscription](./docs/pydocmd/models/subscription.md)
<!--te-->

## Installation
```bash
pip install --upgrade spotinst-sdk
```

## Configuring Session
The mechanism in which the sdk looks for credentials is to search through a list of possible locations and stop as soon as it finds credentials. 
The order in which the sdk searches for credentials is:
  1. Passing credentials as parameters to the `SpotinstSession()` constructor
- example
```python
session = SpotinstSession(auth_token='token', account_id='act-123')
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

  3. You can overwrite the credentials file location and the profile used as parameters in the `SpotinstSession()` constructor
- example
```python
session = SpotinstSession(credentials_file='/path/to/file', profile='my_profile')
```
  
  4. You can overwrite the credentials file location and the profile used as environment variables `SPOTINST_PROFILE` and/or `SPOTINST_SHARED_CREDENTIALS_FILE`
  5. Fetching from the default location with the default profile
  
## Setup Clients
After a session is created you can use the session object to create clients. Clients are used to make request to the different services that Spotinsts has to offer. To create a client simply use the method `client` from the session object and pass in the string of the client you wish to create. Here is an example:

```python
session = SpotinstSession()

eg_client = session.client("elastigroup_aws")
ocean_client = session.client("ocean")
```

Take note you can create more than one client with the session. The currently supported clients are

### Client Options:
 * `session.client("admin")`
 * `session.client("elastigroup_aws")`
 * `session.client("elastigroup_azure")`
 * `session.client("elastigroup_gcp")`
 * `session.client("functions")`
 * `session.client("mcs")`
 * `session.client("mlb")`
 * `session.client("mrScaler_aws")`
 * `session.client("ocean_aws")`
 * `session.client("subscription")`

A full list of endpoints and clients can be found in the documentation [here](./docs/pydocmd/clients/).

## License
Code is licensed under the [Apache License 2.0](LICENSE). See [NOTICE.md](NOTICE.md) for complete details, including software and third-party licenses and permissions.