import json

none = "d3043820717d74d9a17694c176d39733"

# region ASG


class ASG:
    """
    # Arguments
    product: str
    spot_instance_types: List[str]
    name: str
    availability_vs_cost: str
    """

    def __init__(
            self,
            product=none,
            spot_instance_types=none,
            name=none,
            availability_vs_cost=none):

        self.product = product
        self.spot_instance_types = spot_instance_types
        self.name = name
        self.availability_vs_cost = availability_vs_cost

# endregion

# region Instance


class ImportInstanceConfig:
    """
    # Arguments
    spot_instance_types: List[str]
    name: str
    """

    def __init__(
            self,
            spot_instance_types=none,
            name=none):

        self.spot_instance_types = spot_instance_types
        self.name = name

# endregion


class ImportASGRequest:
    def __init__(self, group):
        self.group = group

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class ImportInstanceRequest:
    def __init__(self, group):
        self.group = group

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
