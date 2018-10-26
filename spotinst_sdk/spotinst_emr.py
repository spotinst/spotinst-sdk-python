import json

none = "d3043820717d74d9a17694c176d39733"

# region EMR
class EMR:
	"""
	# Arguments
	name: str
	decription: str
	region: str
	strategy: Strategy
	:tpye compute: Compute
	scaling: Scaling
	"""
	def __init__(
		self,
		name=none,
		description=none,
		region=none,
		strategy=none,
		compute=none,
		scaling=none):

		self.name = name
		self.description = description
		self.region = region
		self.strategy = strategy
		self.compute = compute
		self.scaling = scaling

# endregion

# region Strategy
class Strategy:
	"""
	# Arguments
	wrapping: Wrapping
	cloning: Cloning
	provisioning_timeout: ProvisioningTimeout
	"""
	def __init__(
		self,
		wrapping=none,
		cloning=none,
		provisioning_timeout=none):

		self.wrapping = wrapping
		self.cloning = cloning
		self.provisioning_timeout = provisioning_timeout

class Wrapping:
	"""
	# Arguments
	source_cluster_id: str
	"""
	def __init__(
		self,
		source_cluster_id):

		self.source_cluster_id = source_cluster_id


class Cloning:
	"""
	# Arguments
	origin_cluster_id: str
	include_steps: bool
	"""
	def __init__(
		self,
		origin_cluster_id=none,
		include_steps=none):

		self.origin_cluster_id = origin_cluster_id
		self.include_steps = include_steps


class ProvisioningTimeout:
	"""
	# Arguments
	timeout: int
	:tpye timeout_action: str
	"""
	def __init__(
		self, 
		timeout = none,
		timeout_action = none):

		self.timeout = timeout
		self.timeout_action = timeout_action


# endregion

# region Compute
class Compute:
	"""
	# Arguments
	ebs_root_volume_size: int
	availability_zones: List[AvailabilityZone]
	bootstrap_actions: BootstrapActions
	steps: Steps
	instance_groups: InstanceGroups
	configurations: Configurations
	"""
	def __init__(
		self,
		ebs_root_volume_size=none,
		availability_zones=none,
		bootstrap_actions=none,
		steps=none,
		instance_groups=none,
		configurations=none):

		self.ebs_root_volume_size = ebs_root_volume_size
		self.availability_zones = availability_zones
		self.bootstrap_actions = bootstrap_actions
		self.steps = steps
		self.instance_groups = instance_groups
		self.configurations = configurations


class AvailabilityZone:
	"""
	# Arguments
	name: str
	subnet: str
	"""
	def __init__(
		self,
		name=none,
		subnet=none):

		self.name = name
		self.subnet = subnet


class BootstrapActions:
	"""
	# Arguments
	file: File
	"""
	def __init__(
		self,
		file=none):

		self.file = file


class File:
	"""
	# Arguments
	bucket: str
	key: str
	"""
	def __init__(
		self, 
		bucket=none,
		key=none):

		self.bucket = bucket
		self. key = key


class Steps:
	"""
	# Arguments
	file: File
	"""
	def __init__(
		self,
		file=none):

		self.file = file


class InstanceGroups:
	"""
	# Arguments
	master_group: MasterGroup
	core_group: CoreGroup
	task_group: TaskGroup
	"""
	def __init__(
		self, 
		master_group=none,
		core_group=none,
		task_group=none):

		self.master_group = master_group
		self.core_group = core_group
		self.task_group = task_group


class MasterGroup:
	"""
	# Arguments
	instance_types: List[str]
	target: int
	life_cycle: str
	"""
	def __init__(
		self,
		instance_types=none,
		target=none,
		life_cycle=none):

		self.instance_types = instance_types
		self.target = target
		self.life_cycle = life_cycle


class CoreGroup:
	"""
	# Arguments
	instance_types: List[str]
	target: int
	life_cycle: str
	ebs_configuration: EbsConfiguration
	"""
	def __init__(
		self,
		instance_types=none,
		target=none,
		life_cycle=none,
		ebs_configuration=none):

		self.instance_types = instance_types
		self.target = target
		self.life_cycle = life_cycle
		self.ebs_configuration = ebs_configuration


class TaskGroup:
	"""
	# Arguments
	instance_types: List[str]
	capacity: Capacity
	life_cycle: str
	ebs_configuration: EbsConfiguration
	"""
	def __init__(
		self,
		instance_types=none,
		capacity=none,
		life_cycle=none,
		ebs_configuration=none):

		self.instance_types = instance_types
		self.capacity = capacity
		self.life_cycle = life_cycle
		self.ebs_configuration = ebs_configuration


class Capacity:
	"""
	# Arguments
	target: int
	minimum: int
	maximum: int
	"""
	def __init__(
		self,
		target=none,
		minimum=none,
		maximum=none):

		self.target = target
		self.minimum = minimum
		self.maximum = maximum


class EbsConfiguration:
	"""
	# Arguments
	ebs_block_device_configs: List[SingleEbsConfig]
	ebs_optimized: bool
	"""
	def __init__(
		self,
		ebs_block_device_configs=none,
		ebs_optimized=none):

		self.ebs_block_device_configs = ebs_block_device_configs
		self.ebs_optimized = ebs_optimized


class SingleEbsConfig:
	"""
	# Arguments
	volume_specification: VolumeSpecification
	volumes_per_instance: int
	"""
	def __init__(
		self,
		volume_specification=none,
		volumes_per_instance=none):

		self.volume_specification = volume_specification
		self.volumes_per_instance = volumes_per_instance


class VolumeSpecification:
	"""
	# Arguments
	volume_type: str
	size_in_GB: int
	"""
	def __init__(
		self,
		volume_type=none,
		size_in_gb=none):

		self.volume_type = volume_type
		self.size_in_gB = size_in_gb


class Configurations:
	"""
	# Arguments
	file: File
	"""
	def __init__(
		self,
		file=none):

		self.file = file


# endregion

# region Scaling
class Scaling:
	"""
	# Arguments
	up: List[Metric]
	down: List[Metric]
	"""
	def __init__(
		self,
		up=none,
		down=none):

		self.up = up
		self.down = down


class Metric:
	"""
	# Arguments
	metric_name: str
	statistic: str
	unit: str
	threshold: int
	adjustment: int
	namespace: str
	period: int
	evaluation_periods: int
	action: Action
	cooldown: int
	dimensions: List[Dimension]
	operator: str
	"""
	def __init__(
		self,
		metric_name=none,
		statistic=none,
		unit=none,
		threshold=none,
		adjustment=none,
		namespace=none,
		period=none,
		evaluation_periods=none,
		action=none,
		cooldown=none,
		dimensions=none,
		operator=none):

		self.metric_name = metric_name
		self.statistic = statistic
		self.unit = unit
		self.threshold = threshold
		self.adjustment = adjustment
		self.namespace = namespace
		self.period = period
		self.evaluation_periods = evaluation_periods
		self.action = action
		self.cooldown = cooldown
		self.dimensions = dimensions
		self.operator = operator

class Action:
	"""
	# Arguments
	type: str
	adjustment: int
	min_target_capacity: int
	target: int
	minimum: int
	maximum: int
	"""
	def __init__(
		self,
		type=none,
		adjustment=none,
		min_target_capacity=none,
		target=none,
		minimum=none,
		maximum=none):

		self.type = type
		self.adjustment = adjustment
		self.min_target_capacity = min_target_capacity
		self.target = target
		self.minimum = minimum
		self.maximum = maximum

class Dimension:
	"""
	# Arguments
	name: str
	"""
	def __init__(
		self,
		name=none):

		self.name = name


#endregion



class EMRCreationRequest:
    def __init__(self, mrScaler):
        self.mrScaler = mrScaler

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)







