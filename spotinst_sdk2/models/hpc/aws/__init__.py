import json
from typing import List

none = "d3043820717d74d9a17694c176d39733"

# region Strategy


class Strategy:
    """
    # Arguments
    draining_timeout: int
    availability_vs_cost: str
    risk: int
    fallback_to_od: bool
    """

    def __init__(
            self,
            draining_timeout: int = none,
            availability_vs_cost: str = none,
            risk: int = none,
            fallback_to_od: bool = none
    ):
        self.draining_timeout = draining_timeout
        self.availability_vs_cost = availability_vs_cost
        self.risk = risk
        self.fallback_to_od = fallback_to_od
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

    def __init__(self, minimum: int = none, maximum: int = none, target: int = none, unit: str = none):

        self.minimum = minimum
        self.maximum = maximum
        self.target = target
        self.unit = unit

# endregion

# region Weight


class Weight:
    """
    # Arguments
    instance_type: str
    weighted_capacity: int
    """

    def __init__(self, instance_type: str = none, weighted_capacity: int = none):
        self.instance_type = instance_type
        self.weighted_capacity = weighted_capacity

# endregion

# region Instance Types


class InstanceTypes:
    """
    # Arguments
    on_demand: str
    spot: List[str]
    weights: List[Weight]
    preferred_spot: List[str]
    """

    def __init__(
            self,
            on_demand: str = none,
            spot: List[str] = none,
            weights: List[Weight] = none,
            preferred_spot: List[str] = none):

        self.on_demand = on_demand
        self.spot = spot
        self.weights = weights
        self.preferred_spot = preferred_spot

# endregion

# region Image


class Image:
    """
    # Arguments
    id: str
    """

    def __init__(
            self,
            id: str = none):
        self.id = id

# endregion

# region Tag


class Tag:
    """
    # Arguments
    tag_key: str
    tag_value: str
    """

    def __init__(self, tag_key: str = none, tag_value: str = none):

        self.tag_key = tag_key
        self.tag_value = tag_value

# endregion

# region Launch Specification


class LaunchSpecification:
    """
    # Arguments
    security_group_ids: List[str]
    image_id: str
    monitoring: bool
    key_pair: str
    user_data: str
    images: List[Image]
    tags: List[Tag]
    """

    def __init__(
            self,
            security_group_ids: List[str] = none,
            image_id: str = none,
            monitoring: bool = none,
            key_pair: str = none,
            user_data: str = none,
            images: List[Image] = none,
            tags: List[Tag] = none):

        self.security_group_ids = security_group_ids
        self.monitoring = monitoring
        self.image_id = image_id
        self.key_pair = key_pair
        self.user_data = user_data
        self.images = images
        self.tags = tags

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
            launch_specification: LaunchSpecification = none,
            instance_types: InstanceTypes = none,
            subnet_ids: List[str] = none):

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
            name: str = none,
            description: str = none,
            region: str = none,
            capacity: Capacity = none,
            strategy: Strategy = none,
            compute: Compute = none,
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


class LSFClusterUpdateRequest:
    def __init__(self, lsf_cluster):
        self.lsf_cluster = lsf_cluster

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
