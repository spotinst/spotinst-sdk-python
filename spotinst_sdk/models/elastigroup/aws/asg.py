import json

none = "d3043820717d74d9a17694c176d39733"

# region ASG
class ASG:
	"""
	# Arguments
	product: str
	spot_instance_types: List[str]
	name: str
	"""
	def __init__(
		self,
		product=none,
		spot_instance_types=none,
		name=none):

		self.product = product
		self.spot_instance_types = spot_instance_types
		self.name = name

# endregion


class ImportASGRequest:
    def __init__(self, group):
        self.group = group

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

