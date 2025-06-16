import json
from typing import List

none = "d3043820717d74d9a17694c176d39733"

class NotificationPolicy:
    def __init__(
            self,
            account_id=None):
        self.account_id = account_id

class FilterConditions:
    """
    # Arguments
    identifier: str
    operator: str
    expression: str
    """

    def __init__(
            self,
            identifier: str = none,
            operator: str = none,
            expression: str = none):
        
        self.identifier = identifier
        self.operator = operator
        self.expression = expression

class DynamicRules:
    """
    # Arguments
    filterConditions: List[FilterConditions]
    """

    def __init__(
            self,
            filterConditions: List[FilterConditions] = none):
        
        self.filterConditions = filterConditions

class Events:
    """
    # Arguments
    event: str
    type: str
    """

    def __init__(
            self,
            event: str = none,
            type: str = none):

        self.event = event
        self.type = type


class ComputePolicyConfig:
    """
    # Arguments
    events: List[Events]
    shouldIncludeAllResources: bool
    resourceIds: List[str]
    dynamicRules: List[DynamicRules]
    """

    def __init__(
            self,
            events: List[Events] = none,
            shouldIncludeAllResources: bool = none,
            resourceIds: List[str] = none,
            dynamicRules: List[DynamicRules] = none):
        
        self.shouldIncludeAllResources = shouldIncludeAllResources
        self.events = events
        self.resourceIds = resourceIds
        self.dynamicRules = dynamicRules

class RegisteredUsers:
    """
    # Arguments
    subscriptionTypes: List[str]
    userEmail: str
    """

    def __init__(
            self,
            userEmail: str = none,
            subscriptionTypes: List[str] = none):

        self.userEmail = userEmail
        self.subscriptionTypes = subscriptionTypes

class Subscriptions:
    """
    # Arguments
    type: str
    endpoint: str
    """

    def __init__(
            self,
            type: str = none,
            endpoint: str = none):

        self.type = type
        self.endpoint = endpoint

class Policy:
    """
    # Arguments
    name: str
    description: str
    privacyLevel: str
    isActive: bool
    registeredUsers: List[RegisteredUsers]
    subscriptions: List[Subscriptions]
    computePolicyConfig: List[ComputePolicyConfig]
    """

    def __init__(
            self,
            description: str = none,
            name: str = none,
            privacyLevel: str = none,
            isActive: bool = none,
            registeredUsers: List[RegisteredUsers] = none,
            subscriptions: List[Subscriptions] = none,
            computePolicyConfig: List[ComputePolicyConfig] = none):

        self.description = description
        self.name = name
        self.privacyLevel = privacyLevel
        self.isActive = isActive
        self.registeredUsers = registeredUsers
        self.subscriptions = subscriptions
        self.computePolicyConfig = computePolicyConfig


class PolicyCreationRequest:
    def __init__(
            self,policy: Policy):

            self.description = policy.description
            self.name = policy.name
            self.privacyLevel = policy.privacyLevel
            self.isActive = policy.isActive
            self.registeredUsers = policy.registeredUsers
            self.subscriptions = policy.subscriptions
            self.computePolicyConfig = policy.computePolicyConfig

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
    
class PolicyUpdateRequest:
    def __init__(self, policy: Policy):

            self.policy = policy

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)    