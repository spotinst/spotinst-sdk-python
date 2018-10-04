import json

none = "d3043820717d74d9a17694c176d39733"

# region EMR
class EMR:

	def __init__(
		self,
		name=none,
		description=none,
		region=none,
		strategy=none,
		compute=none,
		scaling=none):
		"""

		:type name: str
		:type decription: str
		:type region: str
		:type strategy: Strategy
		:tpye compute: Compute
		:type scaling: Scaling
		"""
		self.name = name
		self.description = description
		self.region = region
		self.strategy = strategy
		self.compute = compute
		self.scaling = scaling

# endregion

# region Strategy
class Strategy:

	def __init__(
		self,
		wrapping=none,
		cloning=none,
		provisioning_timeout=none):
		"""

		:type wrapping: Wrapping
		:type cloning: Cloning
		:type provisioning_timeout: ProvisioningTimeout
		"""
		self.wrapping = wrapping
		self.cloning = cloning
		self.provisioning_timeout = provisioning_timeout

class Wrapping:

	def __init__(
		self,
		source_cluster_id):
		"""

		:type source_cluster_id: str
		"""
		self.source_cluster_id = source_cluster_id


class Cloning:

	def __init__(
		self,
		origin_cluster_id=none,
		include_steps=none):
		"""

		:type origin_cluster_id: str
		:type include_steps: bool
		"""
		self.origin_cluster_id = origin_cluster_id
		self.include_steps = include_steps


class ProvisioningTimeout:

	def __init__(
		self, 
		timeout = none,
		timeout_action = none):
		"""

		:type timeout: int
		:tpye timeout_action: str
		"""
		self.timeout = timeout
		self.timeout_action = timeout_action


# endregion

# region Compute
class Compute:

	def __init__(
		self,
		ebs_root_volume_size=none,
		availability_zones=none,
		bootstrap_actions=none,
		steps=none,
		instance_groups=none,
		configurations=none):
		"""

		:type ebs_root_volume_size: int
		:type availability_zones: List[AvailabilityZone]
		:type bootstrap_actions: BootstrapActions
		:type steps: Steps
		:type instance_groups: InstanceGroups
		:type configurations: Configurations
		"""
		self.ebs_root_volume_size = ebs_root_volume_size
		self.availability_zones = availability_zones
		self.bootstrap_actions = bootstrap_actions
		self.steps = steps
		self.instance_groups = instance_groups
		self.configurations = configurations


class AvailabilityZone:

	def __init__(
		self,
		name=none,
		subnet=none):
		"""

		:type name: str
		:type subnet: str
		"""
		self.name = name
		self.subnet = subnet


class BootstrapActions:

	def __init__(
		self,
		file=none):
		"""

		:type file: File
		"""
		self.file = file


class File:

	def __init__(
		self, 
		bucket=none,
		key=none):
		"""

		:type bucket: str
		:type key: str
		"""
		self.bucket = bucket
		self. key = key


class Steps:

	def __init__(
		self,
		file=none):
		"""
		:type file: File
		"""
		self.file = file


class InstanceGroups:

	def __init__(
		self, 
		master_group=none,
		core_group=none,
		task_group=none):
		"""

		:type master_group: MasterGroup
		:type core_group: CoreGroup
		:type task_group: TaskGroup
		"""
		self.master_group = master_group
		self.core_group = core_group
		self.task_group = task_group


class MasterGroup:

	def __init__(
		self,
		instance_types=none,
		target=none,
		life_cycle=none):
		"""

		:type instance_types: List[str]
		:type target: int
		:type life_cycle: str
		"""
		self.instance_types = instance_types
		self.target = target
		self.life_cycle = life_cycle


class CoreGroup:

	def __init__(
		self,
		instance_types=none,
		target=none,
		life_cycle=none,
		ebs_configuration=none):
		"""

		:type instance_types: List[str]
		:type target: int
		:type life_cycle: str
		:type ebs_configuration: EbsConfiguration
		"""
		self.instance_types = instance_types
		self.target = target
		self.life_cycle = life_cycle
		self.ebs_configuration = ebs_configuration


class TaskGroup:

	def __init__(
		self,
		instance_types=none,
		capacity=none,
		life_cycle=none,
		ebs_configuration=none):
		"""

		:type instance_types: List[str]
		:type capacity: Capacity
		:type life_cycle: str
		:type ebs_configuration: EbsConfiguration
		"""
		self.instance_types = instance_types
		self.capacity = capacity
		self.life_cycle = life_cycle
		self.ebs_configuration = ebs_configuration


class Capacity:

	def __init__(
		self,
		target=none,
		minimum=none,
		maximum=none):
		"""
		
		:type target: int
		:type minimum: int
		:type maximum: int
		"""
		self.target = target
		self.minimum = minimum
		self.maximum = maximum


class EbsConfiguration:

	def __init__(
		self,
		ebs_block_device_configs=none,
		ebs_optimized=none):
		"""

		:type ebs_block_device_configs: List[SingleEbsConfig]
		:type ebs_optimized: bool
		"""
		self.ebs_block_device_configs = ebs_block_device_configs
		self.ebs_optimized = ebs_optimized


class SingleEbsConfig:

	def __init__(
		self,
		volume_specification=none,
		volumes_per_instance=none):
		"""

		:type volume_specification: VolumeSpecification
		:type volumes_per_instance: int
		"""
		self.volume_specification = volume_specification
		self.volumes_per_instance = volumes_per_instance


class VolumeSpecification:
	def __init__(
		self,
		volume_type=none,
		size_in_gb=none):
		"""

		:type volume_type: str
		:type size_in_GB: int
		"""
		self.volume_type = volume_type
		self.size_in_gB = size_in_gb


class Configurations:

	def __init__(
		self,
		file=none):
		"""

		:type file: File
		"""
		self.file = file


# endregion

# region Scaling
class Scaling:

	def __init__(
		self,
		up=none,
		down=none):
		"""

		:type up: List[Metric]
		:type down: List[Metric]
		"""
		self.up = up
		self.down = down


class Metric:

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
		"""

		:type metric_name: str
		:type statistic: str
		:type unit: str
		:type threshold: int
		:type adjustment: int
		:type namespace: str
		:type period: int
		:type evaluation_periods: int
		:type action: Action
		:type cooldown: int
		:type dimensions: List[Dimension]
		:type operator: str
		"""
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

	def __init__(
		self,
		type=none,
		adjustment=none,
		min_target_capacity=none,
		target=none,
		minimum=none,
		maximum=none):
		"""

		:type type: str
		:type adjustment: int
		:type min_target_capacity: int
		:type target: int
		:type minimum: int
		:type maximum: int
		"""
		self.type = type
		self.adjustment = adjustment
		self.min_target_capacity = min_target_capacity
		self.target = target
		self.minimum = minimum
		self.maximum = maximum

class Dimension:

	def __init__(
		self,
		name=none):
		"""
		:type name: str
		"""
		self.name = name


#endregion



class EMRCreationRequest:
    def __init__(self, mrScaler):
        self.mrScaler = mrScaler

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)







