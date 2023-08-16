import json
from typing import List

none = "d3043820717d74d9a17694c176d39733"


# region GKE
class Capacity:
    """
    # Arguments
    minimum: int
    maximum: int
    target: int
    """

    def __init__(
            self,
            minimum: int = none,
            maximum: int = none,
            target: int = none):
        self.minimum = minimum
        self.maximum = maximum
        self.target = target


class InstanceTypes:
    """
    # Arguments
    ondemand: str
    preemptible: List[str]
    """

    def __init__(self, ondemand: str = none, preemptible: List[str] = none):
        self.ondemand = ondemand
        self.preemptible = preemptible


class GKEImportConfig:
    """
    # Arguments
    name: str
    preemptible_percentage: int
    capacity: Capacity
    instance_types: InstanceTypes
    availability_zones: List[str]
    """

    def __init__(
            self,
            name: str = none,
            preemptible_percentage: int = none,
            capacity: Capacity = none,
            instance_types: InstanceTypes = none,
            availability_zones: List[str] = none):
        self.name = name
        self.preemptible_percentage = preemptible_percentage
        self.capacity = capacity
        self.instance_types = instance_types
        self.availability_zones = availability_zones


class ImportGKERequest:
    def __init__(self, group):
        self.group = group

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

# endregion
