import json

none = "d3043820717d74d9a17694c176d39733"

# region StatefulInstance
class StatefulInstance:

	def __init__(
		self,
		should_keep_private_ip=none,
		original_instance_id=none,
		name=none,
		product=none,
		spot_instance_types=none,
		region=none,
		availability_zones=none):
		"""

		:type shouldKeepPrivateIp: bool
		"type originalInstanceId: str
		"type name: str
		:type product: str
		:type spotInstanceTypes: List[str]
		:type region: str
		:type availabilityZones: List[AvailabiltyZones]
		"""
		self.should_keep_private_ip = should_keep_private_ip
		self.original_instance_id = original_instance_id
		self.name = name
		self.product = product
		self.spot_instance_types = spot_instance_types
		self.region = region
		self.availability_zones = availability_zones

class AvailabilityZone:

	def __init__(
		self,
		name=none,
		subnet_ids=none):
		"""

		:type name: str
		:type subnet: str
		"""
		self.name = name
		self.subnet_ids = subnet_ids

# endregion


class StatefulImportRequest:
    def __init__(self, statefulMigrationGroup):
        self.statefulMigrationGroup = statefulMigrationGroup

        print(self.statefulMigrationGroup)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)



