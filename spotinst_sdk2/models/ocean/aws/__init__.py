import json

none = "d3043820717d74d9a17694c176d39733"

# region Ocean
class Ocean:
	"""
	# Arguments
	name: str
	controller_cluster_id: str
	region: str
	auto_scaler: AutoScaler
	capacity: Capacity
	strategy: Strategy
	compute: Compute
	"""
	def __init__(
		self,
		name=none,
		controller_cluster_id=none,
		region=none,
		auto_scaler=none,
		capacity=none,
		strategy=none,
		compute=none):

		self.name = name
		self.controller_cluster_id = controller_cluster_id
		self.region = region
		self.auto_scaler = auto_scaler
		self.capacity = capacity
		self.strategy = strategy
		self.compute = compute
# endregion

# region AutoScaler
class AutoScaler:
	"""
	# Arguments
	is_enabled: bool
	cooldown: int
	resource_limits: ResourceLimits
	down: Down
	headroom: Headroom
	is_auto_config: bool
	"""
	def __init__(
		self,
		is_enabled=none,
		cooldown=none,
		resource_limits=none,
		down=none,
		headroom=none,
		is_auto_config=none):

		self.is_enabled = is_enabled
		self.cooldown = cooldown
		self.resource_limits = resource_limits
		self.down = down
		self.headroom = headroom
		self.is_auto_config = is_auto_config

class ResourceLimits:
	"""
	# Arguments
	max_memory_gib: nint
	max_vCpu: int
	"""
	def __init__(
		self,
		max_memory_gib=none,
		max_vCpu=none):

		self.max_memory_gib=max_memory_gib
		self.max_vCpu=max_vCpu

class Down:
	"""
	# Arguments
	evaluation_periods: int
	"""
	def __init__(
		self,
		evaluation_periods=none):
		self.evaluation_periods = evaluation_periods

class Headroom:
	"""
	# Arguments
	cpu_per_unit: int
	memory_per_unit: int
	num_of_units: int
	"""
	def __init__(
		self,
		cpu_per_unit=none,
		memory_per_unit=none,
		num_of_units=none):
		self.cpu_per_unit = cpu_per_unit
		self.memory_per_unit = memory_per_unit
		self.num_of_units = num_of_units
# endregion

# region Capacity
class Capacity:
	"""
	# Arguments
	minimum: int
	maximum: int
	target: int
	"""
	def __init__(
		self,
		minimum=none,
		maximum=none,
		target=none):

		self.minimum = minimum
		self.maximum = maximum
		self.target = target
# endregion

# region Strategy
class Strategy:
	"""
	# Arguments
	utilize_reserved_instances: bool
	fallback_to_od: bool
	spot_percentage: int
	"""
	def __init__(
		self,
		utilize_reserved_instances=none,
		fallback_to_od=none,
		spot_percentage=none):

		self.utilize_reserved_instances = utilize_reserved_instances
		self.fallback_to_od = fallback_to_od
		self.spot_percentage = spot_percentage
# endregion

# region Compute
class Compute:
	"""
	# Arguments
	instance_types: InstanceTypes
	subnet_ids: List[str]
	launch_specification: LaunchSpecifications
	"""
	def __init__(
		self,
		instance_types=none,
		subnet_ids=none,
		launch_specification=none):

		self.instance_types = instance_types
		self.subnet_ids = subnet_ids
		self.launch_specification = launch_specification

class InstanceTypes:
	"""
	# Arguments
	whitelist: List[str]
	blacklist: List[str]
	"""
	def __init__(
		self,
		whitelist=none,
		blacklist=none):

		self.whitelist = whitelist
		self.blacklist = blacklist

class LaunchSpecifications:
	"""
	# Arguments
	security_group_ids: List[str]
	image_id: str
	iam_instance_profile: IamInstanceProfile
	key_pair: str
	user_data: str
	tags: List[Tag]
	"""
	def __init__(
		self,
		security_group_ids=none,
		image_id=none,
		iam_instance_profile=none,
		key_pair=none,
		user_data=none,
		tags=none):

		self.security_group_ids = security_group_ids
		self.image_id = image_id
		self.iam_instance_profile = iam_instance_profile
		self.key_pair = key_pair
		self.user_data = user_data
		self.tags = tags

class IamInstanceProfile:
	"""
	# Arguments
	arn: str
	name: str
	"""
	def __init__(
		self,
		arn=none,
		name=none):
		self.arn = arn
		self.name = name

class Tag:
	"""
	# Argument
	tag_key: str
	tag_value: str
	"""
	def __init__(
		self,
		tag_key=none,
		tag_value=none):
		self.tag_key = tag_key
		self.tag_value = tag_value
# endregion


class OceanRequest:
    def __init__(self, cluster):
        self.cluster = cluster

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)





