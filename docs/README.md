[![Build Status](https://travis-ci.org/spotinst/spotinst-sdk-python.svg?branch=master)](https://travis-ci.org/spotinst/spotinst-sdk-python)
[![Coverage Status](https://coveralls.io/repos/github/spotinst/spotinst-sdk-python/badge.svg?branch=master)](https://coveralls.io/github/spotinst/spotinst-sdk-python?branch=master)
[![Python 2.7](https://img.shields.io/badge/python-2.7-blue.svg)](https://www.python.org/downloads/release/python-270/)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

# Spotinst SDK Python

The official Spotinst SDK for the Python programming language.

## Version 2

Version 2 for the Spotinst Python SDK will be moving from the `v2` branch to the `master` branch very soon. The current `master` will move to it's own `v1` branch and eventually be deprecated. Version 2 introduces some breaking changes from v1 and will require updates when switching over. Luckily this process should be easy and is completely explained on the [v2 branch in this repository](https://github.com/spotinst/spotinst-sdk-python/tree/v2). Both `v1` and `v2` will be released as `spotinst-sdk` and `spotinst-sdk2` respectively, to prevent any auto version upgrades.

## Contents

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

The mechanism in which the sdk looks for credentials is to search through a list of possible locations and stop as soon as it finds credentials. The order in which the sdk searches for credentials is:

1. Passing credentials as parameters to the `SpotinstClient()` constructor.

```python
client = SpotinstClient(auth_token='token', account_id='act-123')
```

2. Fetching the account and token from environment variables under `SPOTINST_ACCOUNT` and `SPOTINST_TOKEN`.

If you choose to not pass your credentials directly you configure a credentials file, this file should be a valid `.yml` file. The default shared credential file location is `~/.spotinst/credentials` and the default profile is `default`.

```yaml
default: #profile
  token: $defaul_spotinst_token
  account: $default_spotinst-account-id
my_profile:
  token: $my_spotinst_token
  account: $my_spotinst-account-id
```

3. You can overwrite the credentials file location and the profile used as parameters in the `SpotinstClient()` constructor.

```python
client = SpotinstClient(credentials_file='/path/to/file', profile='my_profile')
```

4. You can overwrite the credentials file location and the profile used as environment variables `SPOTINST_PROFILE` and/or `SPOTINST_SHARED_CREDENTIALS_FILE`.

5. Fetching from the default location with the default profile.

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
