[![Build Status](https://travis-ci.org/spotinst/spotinst-sdk-python.svg?branch=master)](https://travis-ci.org/spotinst/spotinst-sdk-python)
[![Coverage Status](https://coveralls.io/repos/github/spotinst/spotinst-sdk-python/badge.svg?branch=master)](https://coveralls.io/github/spotinst/spotinst-sdk-python?branch=master)
[![Python 2.7](https://img.shields.io/badge/python-2.7-blue.svg)](https://www.python.org/downloads/release/python-270/)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

# Spotinst SDK Python

The official Spotinst SDK for the Python programming language.

## Version 2

Version 2 for the Spotinst Python SDK will be moving from the `v2` branch to the `master` branch very soon. The current `master` will move to it's own `v1` branch and eventually be deprecated. Version 2 introduces some breaking changes from v1 and will require updates when switching over. Luckily this process should be easy and is completely explained on the [v2 branch in this repository](https://github.com/spotinst/spotinst-sdk-python/tree/v2). Both `v1` and `v2` will be released as `spotinst-sdk` and `spotinst-sdk2` respectively, to prevent any auto version upgrades.

## Table of Contents

- [Installation](#installation)
- [Authentication](#authentication)
- [Documentation](#documentation)
- [Getting Help](#getting-help)
- [Community](#community)
- [License](#license)

## Installation

```bash
pip install --upgrade spotinst-sdk
```

## Authentication

The mechanism in which the SDK looks for credentials is to search through a list of possible locations and stop as soon as it finds credentials. The order in which the SDK searches for credentials is:

1. Passing credentials as parameters when creating a `SpotinstClient` object:

```python
session = SpotinstClient(auth_token='foo', account_id='bar')
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

- Passing the credentials file location and the profile used as parameters when creating a `SpotinstClient` object:

```python
session = SpotinstClient(credentials_file='/path/to/credentials_file', profile='dev')
```

## Documentation

For a comprehensive documentation, check out the [API documentation](https://help.spot.io/).

- [Endpoints](docs/endpoints)
- [Classes](docs/classes)
- [Examples](docs/examples)

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
