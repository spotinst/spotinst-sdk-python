[![Build Status](https://travis-ci.org/spotinst/spotinst-sdk-python.svg?branch=v2)](https://travis-ci.org/spotinst/spotinst-sdk-python)
[![Coverage Status](https://coveralls.io/repos/github/spotinst/spotinst-sdk-python/badge.svg?branch=v2)](https://coveralls.io/github/spotinst/spotinst-sdk-python?branch=master)
[![Python 2.7](https://img.shields.io/badge/python-2.7-blue.svg)](https://www.python.org/downloads/release/python-270/)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

# Spotinst SDK Python

The official Spotinst SDK for the Python programming language.

## Version 2

The new Spotinst Python SDK comes with a few breaking changes but do not fear, here we will explain all you need to know to make sure you can go right back in buisness in no time. 

- There is no longer the `SpotinstClient()` class which was used to validate your credentials and make requests all in one
- Now there is the `SpotinstSession()` class which is used to validate credentials. [Configure Session Docs](#Configuring-Session)
- From the session object you can create client objects which correlate to specific Spotinst Services and are used to make requests. [Setup Clients Docs](#Setup-Clients)
- Some methods required you to pass in a Model object

Here is a basic example of how to create an Ocean cluster using the Ocean Client and the Ocean Models

```python
from spotinst_sdk2 import SpotinstSession
from spotinst_sdk2.models.ocean.aws import *

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

In the [SDK Client documentation](./docs/clients/) you can view what methods are supported by each client. <br>
For information on what models are supported checkout the [SDK Model documentation](./docs/models/). <br>
More examples can be found in the [SDK Examples Documentation](./docs/examples/). <br>

## Table of Contents

- [Installation](#installation)
- [Authentication](#authentication)
- [Setup Clients](#setup-clients)
- [Documentation](#documentation)
- [Getting Help](#getting-help)
- [Community](#community)
- [License](#license)

## Installation

```bash
pip install --upgrade spotinst-sdk2
```

## Authentication

The mechanism in which the SDK looks for credentials is to search through a list of possible locations and stop as soon as it finds credentials. The order in which the SDK searches for credentials is:

1. Passing credentials as parameters when creating a `SpotinstSession` object:

```python
session = SpotinstSession(auth_token='foo', account_id='bar')
```

2. Environment variables:

```sh
export SPOTINST_TOKEN=foo
export SPOTINST_ACCOUNT=bar
```

3. Shared credentials file:

- The shared credentials file has a default location of `~/.spotinst/credentials`. This file is an INI formatted file with section names corresponding to profiles. With each section, two configuration variables can be specified: `token`, `account`. These are the only supported values in the shared credential file.

- Below is a minimal example of the shared credentials file:

```ini
[default]
token   = foo
account = bar
```

- The shared credentials file also supports the concept of profiles. Profiles represent logical groups of configuration. The shared credential file can have multiple profiles:

```ini
[default]
token   = foo
account = bar

[dev]
token   = foo2
account = bar2

[prod]
token   = foo3
account = bar3
```

- You can configure your Spot credentials using the `spotctl configure` command. For more information, see the `spotctl` [Getting Started](https://github.com/spotinst/spotctl#getting-started).

- To maintain compatibility with previous SDK versions, the file can also be in YAML format:

```yaml
default:
  token: foo
  account: bar
  
dev:
  token: foo2
  account: bar2
  
prod:
  token: foo3
  account: bar3
```

- You can change the location of the credentials file and the profile used by setting the `SPOTINST_SHARED_CREDENTIALS_FILE` and/or `SPOTINST_PROFILE` environment variables:

```sh
export SPOTINST_SHARED_CREDENTIALS_FILE=/path/to/credentials_file
export SPOTINST_PROFILE=dev
```

- Passing the credentials file location and the profile used as parameters when creating a `SpotinstSession` object:

```python
session = SpotinstSession(credentials_file='/path/to/credentials_file', profile='dev')
```
  
## Setup Clients

After a session is created you can use the session object to create clients. Clients are used to make request to the different services that Spotinsts has to offer. To create a client simply use the method `client` from the session object and pass in the string of the client you wish to create. Here is an example:

```python
session = SpotinstSession()

eg_client = session.client("elastigroup_aws")
ocean_client = session.client("ocean")
```

Take note you can create more than one client with the session. The currently supported clients are

### Client Options

- `session.client("admin")`
- `session.client("setup_aws")`
- `session.client("setup_azure")`
- `session.client("setup_gcp")`
- `session.client("elastigroup_aws")`
- `session.client("elastigroup_azure_v3")`
- `session.client("elastigroup_gcp")`
- `session.client("mcs")`
- `session.client("mrScaler_aws")`
- `session.client("ocean_aws")`
- `session.client("ocean_azure")`
- `session.client("ocean_gcp")`
- `session.client("ocean_ecs")`
- `session.client("ocean_rightsizing")`
- `session.client("subscription")`
- `session.client("managed_instance_aws")`
- `session.client("stateful_node_azure")`
- `session.client("functions")`

A full list of endpoints and clients can be found in the documentation [here](./docs/clients/).

## Documentation

For a comprehensive documentation, check out the [API documentation](https://help.spot.io/).

## Getting Help

We use GitHub issues for tracking bugs and feature requests. Please use these community resources for getting help:

- Ask a question on [Stack Overflow](https://stackoverflow.com/) and tag it with [spotinst-sdk-python](https://stackoverflow.com/questions/tagged/spotinst-sdk-python/).
- Join our Spotinst community on [Slack](http://slack.spot.io/).
- Open an [issue](https://github.com/spotinst/spotinst-sdk-python/issues/new/).

## Community

- [Slack](http://slack.spot.io/)
- [Twitter](https://twitter.com/spot_hq/)

## License

Code is licensed under the [Apache License 2.0](LICENSE). See [NOTICE.md](NOTICE.md) for complete details, including software and third-party licenses and permissions.
