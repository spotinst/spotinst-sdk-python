import json

none = "d3043820717d74d9a17694c176d39733"

# region EMR


class BlueGreenDeployment:
    """
    # Arguments
    timeout: int
    tags: List[Tag]
    deployment_groups: List[DeploymentGroup]
    """

    def __init__(
            self,
            timeout=none,
            tags=none,
            deployment_groups=none):

        self.timeout = timeout
        self.tags = tags
        self.deployment_groups = deployment_groups

# endregion


class Tag:
    """
    # Arguments
    tag_get: str
    tag_value: str
    """

    def __init__(
            self,
            tag_key=none,
            tag_value=none):

        self.tag_key = tag_key
        self.tag_value = tag_value


class DeploymentGroup:
    """
    # Arguments
    application_name: str
    deployment_group_name: str
    """

    def __init__(
            self,
            application_name=none,
            deployment_group_name=none):

        self.application_name = application_name
        self.deployment_group_name = deployment_group_name


class BlueGreenDeploymentRequest:
    def __init__(self, deployment):
        self.deployment = deployment

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
