import json
from typing import List

none = "d3043820717d74d9a17694c176d39733"

# region organization


class Statement:
    """
    # Arguments
    effect: str
    actions: List[str]
    resources: List[str]
    """

    def __init__(
            self,
            effect: str = none,
            actions: List[str] = None,
            resources: List[str] = None):

        self.effect = effect
        self.actions = actions
        self.resources = resources


class PolicyContent:
    """
    # Arguments
    statements: List[Statement]
    """

    def __init__(
            self,
            statements: List[Statement] = none):

        self.statements = statements


class AccessPolicy:
    """
        # Arguments
        description: str
        name: str
        type: str
        policy_content: PolicyContent
        """

    def __init__(
            self,
            description: str = none,
            name: str = none,
            type: str = none,
            policy_content: PolicyContent = none):

        self.description = description
        self.name = name
        self.type = type
        self.policy_content = policy_content


class PolicyMapping:
    """
    # Arguments
    account_ids: List[str]
    policy_id: str
    """

    def __init__(
            self,
            policy_id: str = none,
            account_ids: List[str] = none):

        self.policy_id = policy_id
        self.account_ids = account_ids


class UserGroup:
    """
        # Arguments
        description: str
        name: str
        policies: List[PolicyMapping]
        user_ids: List[str]
        """

    def __init__(
            self,
            description: str = none,
            name: str = none,
            policies: List[PolicyMapping] = none,
            user_ids: List[str] = none):

        self.description = description
        self.name = name
        self.policies = policies
        self.user_ids = user_ids

# endregion


class AccessPolicyCreationRequest:
    def __init__(self, policy: AccessPolicy):
        self.policy = policy

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class AccessPolicyUpdationRequest:
    def __init__(self, policy: AccessPolicy):
        self.policy = policy

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class UserGroupCreationRequest:
    def __init__(self, group: UserGroup):
        self.description = group.description
        self.name = group.name
        self.policies = group.policies
        self.user_ids = group.user_ids

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
