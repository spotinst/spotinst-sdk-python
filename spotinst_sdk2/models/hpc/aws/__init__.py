import json
from typing import List

none = "d3043820717d74d9a17694c176d39733"

# region Strategy
class Strategy:
    """
    # Arguments
    draining_timeout: int
    """
    def __init__(
            self,
            draining_timeout:int=none,
            ):
        self.draining_timeout = draining_timeout
        
# endregion

# region Capacity
class Capacity:
    """
    # Arguments
    minimum: int
    maximum: int
    target: int
    unit: str
    """
    def __init__(self, minimum:int=none, maximum:int=none, target:int=none, unit:str=none):

        self.minimum = minimum
        self.maximum = maximum
        self.target = target
        self.unit = unit

# endregion

# region Instance Types
class InstanceTypes:
    """
    # Arguments
    ondemand: str
    spot: List[str]
    """
    def __init__(
            self,
            onDemand:str=none,
            spot:List[str]=none):

        self.onDemand = onDemand
        self.spot = spot

# endregion

# region Launch Specification
class LaunchSpecification:
    """
    # Arguments
    security_group_ids: List[str]
    image_id: Image
    monitoring: bool
    key_pair: str
    user_data: str
    """
    def __init__(
            self,
            security_group_ids:List[str]=none,
            image_id:str=none,
            monitoring:bool=none,
            key_pair:str=none,
            user_data:str=none):

        self.security_group_ids = security_group_ids
        self.monitoring = monitoring
        self.image_id = image_id
        self.key_pair = key_pair
        self.user_data = user_data

# endregion



# region Compute
class Compute:
    """
    # Arguments
    launch_specification: LaunchSpecification
    instance_types: InstanceTypes
    subnet_ids: List[str]
    """
    def __init__(
            self,
            launch_specification:LaunchSpecification=none,
            instance_types:InstanceTypes=none,
            subnet_ids:List[str]=none):

        self.subnet_ids = subnet_ids
        self.instance_types = instance_types
        self.launch_specification = launch_specification

# endregion

# region HPC
class HPC:
    """
    # Arguments
    name: str
    description: str
    region: str
    capacity: Capacity
    strategy: Strategy
    compute: Compute
    """
    def __init__(
            self,
            name:str=none,
            description:str=none,
            region:str=none,
            capacity:Capacity=none,
            strategy:Strategy=none,
            compute:Compute=none,
            ):

        self.name = name
        self.description = description
        self.region = region
        self.capacity = capacity
        self.strategy = strategy
        self.compute = compute

# endregion

class LSFClusterCreationRequest:
    def __init__(self, lsf_cluster):
        self.lsf_cluster = lsf_cluster

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class LSFClusterDeletionRequest:
    def __init__(self, lsf_cluster):
        self.lsf_cluster = lsf_cluster

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
