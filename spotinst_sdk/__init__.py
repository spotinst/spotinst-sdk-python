from spotinst_sdk.session import Session

from spotinst_sdk.clients.elastigroup import *
from spotinst_sdk.clients.ocean import *
from spotinst_sdk.clients.admin import *
from spotinst_sdk.clients.functions import *
from spotinst_sdk.clients.mcs import *
from spotinst_sdk.clients.mlb import *
from spotinst_sdk.clients.mrscaler import *
from spotinst_sdk.clients.subscription import *
from spotinst_sdk.clients.ocean import *

class SpotinstSession:
    def __init__(self, 
        auth_token=None,
        account_id=None,
        profile=None,
        credentials_file=None):

        self.session = Session(auth_token=auth_token,
            account_id=account_id,
            profile=profile,
            credentials_file=credentials_file)

    def client(self, service, print_output=True, log_level=None, user_agent=None):
        switcher = {
            "admin":             AdminClient(session=self.session, print_output=print_output, log_level=log_level, user_agent=user_agent),
            "elastigroup_aws":   ElastigroupAwsClient(session=self.session, print_output=print_output, log_level=log_level, user_agent=user_agent),
            "elastigroup_azure": ElastigroupAzureClient(session=self.session, print_output=print_output, log_level=log_level, user_agent=user_agent),
            "elastigroup_gcp":   ElastigroupGcpClient(session=self.session, print_output=print_output, log_level=log_level, user_agent=user_agent),
            "functions":         FunctionsClient(session=self.session, print_output=print_output, log_level=log_level, user_agent=user_agent),
            "mcs":               McsClient(session=self.session, print_output=print_output, log_level=log_level, user_agent=user_agent),
            "mlb" :              MlbClient(session=self.session, print_output=print_output, log_level=log_level, user_agent=user_agent),
            "mrScaler_aws":      MrScalerAwsClient(session=self.session, print_output=print_output, log_level=log_level, user_agent=user_agent),
            "ocean_aws":         OceanAwsClient(session=self.session, print_output=print_output, log_level=log_level, user_agent=user_agent),
            "subscription":      SubscriptionClient(session=self.session, print_output=print_output, log_level=log_level, user_agent=user_agent),
        }

        return switcher.get(service, "Invalid Service")



