import json

none = "d3043820717d74d9a17694c176d39733"


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
            name=none,
            description=none,
            region=none,
            capacity=none,
            strategy=none,
            compute=none,
            ):

        self.name = name
        self.description = description
        self.region = region
        self.capacity = capacity
        self.strategy = strategy
        self.compute = compute


# endregion

# region Strategy
class Strategy:
    """
    # Arguments
    draining_timeout: int
    """
    def __init__(
            self,
            draining_timeout=none,
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
    def __init__(self, minimum=none, maximum=none, target=none, unit=none):

        self.minimum = minimum
        self.maximum = maximum
        self.target = target
        self.unit = unit


# endregion

# region Compute
class Compute:
    """
    # Arguments
    launch_specification: LaunchSpecification
    instance_types: InstanceTypes
    product: str
    subnet_ids: list[str]
    """
    def __init__(
            self,
            launch_specification=none,
            instance_types=none,
            product=none,
            subnet_ids=none):

        self.subnet_ids = subnet_ids
        self.instance_types = instance_types
        self.product = product
        self.launch_specification = launch_specification

class InstanceTypes:
    """
    # Arguments
    ondemand: str
    spot: list[str]
    """
    def __init__(
            self,
            ondemand=none,
            spot=none):

        self.ondemand = ondemand
        self.spot = spot


class LaunchSpecification:
    """
    # Arguments
    security_group_ids: list[str]
    image_id: str
    monitoring: bool
    key_pair: str
    user_data: str
    """
    def __init__(
            self,
            security_group_ids=none,
            image_id=none,
            monitoring=none,
            key_pair=none,
            user_data=none):

        self.security_group_ids = security_group_ids
        self.monitoring = monitoring
        self.image_id = image_id
        self.key_pair = key_pair
        self.user_data = user_data


class Image:
    """
    # Arguments
    id: str
    """
    def __init__(
        self,
        id=none):
        self.id = id

# endregion

class HPCClusterCreationRequest:
    def __init__(self, hpc_cluster):
        self.hpc_cluster = hpc_cluster

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class HPCClusterDeletionRequest:
    def __init__(self, stateful_deallocation):
        self.stateful_deallocation = stateful_deallocation

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class ElastigroupUpdateRequest:
    def __init__(self, elastigroup):
        self.group = elastigroup

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class ElastigroupRollRequest:
    def __init__(self, group_roll):
        self.batch_size_percentage = group_roll.batch_size_percentage
        self.grace_period = group_roll.grace_period
        self.health_check_type = group_roll.health_check_type
        self.strategy = group_roll.strategy

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class ElastigroupDetachInstancesRequest:
    def __init__(self, detach_configuration):
        self.should_decrement_target_capacity = detach_configuration.should_decrement_target_capacity
        self.draining_timeout = detach_configuration.draining_timeout
        self.instances_to_detach = detach_configuration.instances_to_detach
        self.should_terminate_instances = detach_configuration.should_terminate_instances

    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            sort_keys=True,
            indent=4)
