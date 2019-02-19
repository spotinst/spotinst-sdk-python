import json
import os

VAR_SPOTINST_SHARED_CREDENTIALS_FILE = 'SPOTINST_SHARED_CREDENTIALS_FILE'
VAR_SPOTINST_PROFILE = 'SPOTINST_PROFILE'
VAR_SPOTINST_TOKEN = 'SPOTINST_TOKEN'
VAR_SPOTINST_ACCOUNT = 'SPOTINST_ACCOUNT'

DEFAULT_PROFILE = 'default'
DEFAULT_CREDENTIALS_FILE = os.path.join(
    os.path.expanduser("~"), '.spotinst', 'credentials')

class Session:
    def __init__(self, auth_token=None,
                 account_id=None,
                 profile=None,
                 credentials_file=None):

        if not auth_token:
            self.load_credentials(profile, credentials_file)
        else:
            self.auth_token = auth_token
            self.account_id = account_id

    def load_credentials(self, profile, credentials_file):
        self.account_id = os.environ.get(VAR_SPOTINST_ACCOUNT, None)
        self.auth_token = os.environ.get(VAR_SPOTINST_TOKEN, None)

        if not self.auth_token:
            if not profile:
                profile = os.environ.get(VAR_SPOTINST_PROFILE, DEFAULT_PROFILE)

            if not credentials_file:
                credentials_file = os.environ.get(
                    VAR_SPOTINST_SHARED_CREDENTIALS_FILE,
                    DEFAULT_CREDENTIALS_FILE)

            with open(credentials_file, 'r') as credentials_file:
                config = yaml.load(credentials_file)

                if config:
                    self.account_id = config.get(
                        profile, {}).get(
                        "account", None)
                    self.auth_token = config.get(
                        profile, {}).get("token", None)

            if not self.auth_token:
                raise SpotinstClientException("failed to load credentials")

