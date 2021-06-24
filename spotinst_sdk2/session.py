import os
import yaml
import configparser
from spotinst_sdk2.client import SpotinstClientException

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

        if auth_token is None:
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
                self.__load_credentials_yaml(profile, credentials_file)
                if not self.auth_token:
                    self.__load_credentials_ini(profile, credentials_file)

            if not self.auth_token:
                raise SpotinstClientException("failed to load credentials", "ERROR")

    def __load_credentials_yaml(self, profile, credentials_file):
        try:
            config = yaml.load(credentials_file, Loader=yaml.SafeLoader)
            if config:
                self.account_id = config.get(profile, {}).get("account", None)
                self.auth_token = config.get(profile, {}).get("token", None)
        except:
            return

    def __load_credentials_ini(self, profile, credentials_file):
        try:
            config = configparser.ConfigParser()
            config.read(credentials_file.name)
            if config[profile]:
                self.account_id = config[profile]["account"]
                self.auth_token = config[profile]["token"]
        except:
            return
