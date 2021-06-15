import json

none = "d3043820717d74d9a17694c176d39733"

# region AzureCredentials
class AzureCredentials:
    """
    # Arguments
    client_id: str
    client_secret: str
    tenant_id: str
    subscription_id: str
    """
    def __init__(
            self, 
            client_id, 
            client_secret, 
            tenant_id, 
            subscription_id):

        self.client_id = client_id
        self.client_secret = client_secret
        self.tenant_id = tenant_id
        self.subscription_id = subscription_id

class AzureSetCredentialsRequest:
    """
    # Arguments
    azure_credentials: AzureCredentials
    """
    def __init__(self, azure_credentials):
        self.client_id = azure_credentials.client_id
        self.client_secret = azure_credentials.client_secret
        self.tenant_id = azure_credentials.tenant_id
        self.subscription_id = azure_credentials.subscription_id

    def to_json(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=4)
# endregion