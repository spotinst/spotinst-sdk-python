import json

none = "d3043820717d74d9a17694c176d39733"

# region Task
class Task:
    """
    # Arguments
    name: str
    description: str
    state: str
    policies: list[Policy]
    instances: list[Instance]
    """
    def __init__(
            self,
            name=none,
            description=none,
            state=none,
            policies=none,
            instances=none):

        self.name = name
        self.description = description
        self.state = state
        self.policies = policies
        self.instances = instances

class Policy:
    """
    # Arguments
    cron: str
    action: str
    """
    def __init__(
            self,
            cron=none,
            action=none):

        self.cron = cron
        self.action = action

class Instance:
    """
    # Arguments
    vm_name: str
    resource_group_name: str
    """
    def __init__(
            self,
            vm_name=none,
            resource_group_name=none):

        self.vm_name = vm_name
        self.resource_group_name = resource_group_name

class TaskCreationRequest:
    def __init__(self, task):
        self.name = task.name
        self.description = task.description
        self.state = task.state
        self.policies = task.policies
        self.instances = task.instances

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
# endregion