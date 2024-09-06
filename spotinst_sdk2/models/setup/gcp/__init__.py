import json

none = "d3043820717d74d9a17694c176d39733"

# region GcpCredentials


class GcpCredentials:
    """
    # Arguments
    serviceAccount: ServiceAccount
    """

    def __init__(
            self,
            serviceAccount):

        self.serviceAccount = serviceAccount


class ServiceAccount:
    """
    # Arguments
    type: str
    project_id: str
    private_key_id: str
    private_key: str
    client_email: str
    client_id: str
    auth_uri: str
    token_uri: str
    auth_provider_x509_cert_url: str
    client_x509_cert_url: str
    """

    def __init__(
            self,
            type,
            project_id,
            private_key_id,
            private_key,
            client_email,
            client_id,
            auth_uri,
            token_uri,
            auth_provider_x509_cert_url,
            client_x509_cert_url):

        self.type = type
        self.project_id = project_id
        self.private_key_id = private_key_id
        self.private_key = private_key
        self.client_email = client_email
        self.client_id = client_id
        self.auth_uri = auth_uri
        self.token_uri = token_uri
        self.auth_provider_x509_cert_url = auth_provider_x509_cert_url
        self.client_x509_cert_url = client_x509_cert_url


class GcpSetCredentialsRequest:
    """
    # Arguments
    gcp_credentials: GcpCredentials
    """

    def __init__(self, gcp_credentials):
        self.serviceAccount = gcp_credentials.serviceAccount

    def to_json(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=4)
# endregion
