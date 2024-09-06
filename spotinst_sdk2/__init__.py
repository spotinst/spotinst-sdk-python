from spotinst_sdk2.session import Session

from spotinst_sdk2.clients.managed_instance import *
from spotinst_sdk2.clients.elastigroup import *
from spotinst_sdk2.clients.stateful_node import *
from spotinst_sdk2.clients.ocean import *
from spotinst_sdk2.clients.admin import *
from spotinst_sdk2.clients.functions import *
from spotinst_sdk2.clients.mcs import *
from spotinst_sdk2.clients.mrscaler import *
from spotinst_sdk2.clients.subscription import *
from spotinst_sdk2.clients.setup import *
from spotinst_sdk2.clients.ocean_cd import *
from spotinst_sdk2.clients.hpc import *


class SpotinstSession:
    def __init__(self,
                 base_url=None,
                 auth_token=None,
                 account_id=None,
                 profile=None,
                 credentials_file=None):
        self.session = Session(base_url=base_url,
                               auth_token=auth_token,
                               account_id=account_id,
                               profile=profile,
                               credentials_file=credentials_file)

    def client(self, service, print_output=True, log_level=None, user_agent=None, timeout=None):
        switcher = {
            "admin": AdminClient(session=self.session, print_output=print_output, log_level=log_level,
                                 user_agent=user_agent, timeout=timeout),
            "setup_aws": SetupAWSClient(session=self.session, print_output=print_output, log_level=log_level,
                                        user_agent=user_agent, timeout=timeout),
            "setup_azure": SetupAzureClient(session=self.session, print_output=print_output, log_level=log_level,
                                            user_agent=user_agent, timeout=timeout),
            "setup_gcp": SetupGCPClient(session=self.session, print_output=print_output, log_level=log_level,
                                        user_agent=user_agent, timeout=timeout),
            "elastigroup_aws": ElastigroupAwsClient(session=self.session, print_output=print_output,
                                                    log_level=log_level, user_agent=user_agent, timeout=timeout),
            "elastigroup_azure_v3": ElastigroupAzureV3Client(session=self.session, print_output=print_output,
                                                             log_level=log_level, user_agent=user_agent,
                                                             timeout=timeout),
            "elastigroup_gcp": ElastigroupGcpClient(session=self.session, print_output=print_output,
                                                    log_level=log_level, user_agent=user_agent, timeout=timeout),
            "stateful_node_azure": StatefulNodeAzureClient(session=self.session, print_output=print_output,
                                                           log_level=log_level, user_agent=user_agent, timeout=timeout),
            "functions": FunctionsClient(session=self.session, print_output=print_output, log_level=log_level,
                                         user_agent=user_agent, timeout=timeout),
            "mcs": McsClient(session=self.session, print_output=print_output, log_level=log_level,
                             user_agent=user_agent, timeout=timeout),
            "mrScaler_aws": MrScalerAwsClient(session=self.session, print_output=print_output, log_level=log_level,
                                              user_agent=user_agent, timeout=timeout),
            "ocean_aws": OceanAwsClient(session=self.session, print_output=print_output, log_level=log_level,
                                        user_agent=user_agent, timeout=timeout),
            "ocean_azure": OceanAzureClient(session=self.session, print_output=print_output, log_level=log_level,
                                            user_agent=user_agent, timeout=timeout),
            "ocean_gcp": OceanGcpClient(session=self.session, print_output=print_output, log_level=log_level,
                                        user_agent=user_agent, timeout=timeout),
            "ocean_ecs": OceanEcsClient(session=self.session, print_output=print_output, log_level=log_level,
                                        user_agent=user_agent, timeout=timeout),
            "ocean_rightsizing": OceanRightSizingClient(session=self.session, print_output=print_output, log_level=log_level,
                                                        user_agent=user_agent, timeout=timeout),
            "oceancd": OceanCDClient(session=self.session, print_output=print_output, log_level=log_level,
                                     user_agent=user_agent, timeout=timeout),
            "managed_instance_aws": ManagedInstanceAwsClient(session=self.session, print_output=print_output,
                                                             log_level=log_level, user_agent=user_agent,
                                                             timeout=timeout),
            "subscription": SubscriptionClient(session=self.session, print_output=print_output, log_level=log_level,
                                               user_agent=user_agent, timeout=timeout),
            "hpc": HPCAwsClient(session=self.session, print_output=print_output,
                                log_level=log_level, user_agent=user_agent, timeout=timeout)
        }

        client = switcher.get(service)
        if client is None:
            raise ValueError(f"Invalid service selected: {service}")
        return client
