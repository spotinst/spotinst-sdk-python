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
	compute: Compute
	cluster: Cluster
	scheduling: Scheduling
	scaling: Scaling
	"""
	def __init__(
		self,
		name=none,
		description=none,
		region=none,
		strategy=none,
		compute=none,
		cluster=none,
		scheduling=none,
		scaling=none):

		self.name = name
		self.description = description
		self.region = region
		self.strategy = strategy
		self.compute = compute
		self.cluster = cluster
		self.scheduling = scheduling
		self.scaling = scaling

# endregion

# region Strategy
class Strategy:
	"""
	# Arguments
	wrapping: Wrapping
	cloning: Cloning
	new: Newing
	provisioning_timeout: ProvisioningTimeout
	"""
	def __init__(
		self,
		wrapping=none,
		cloning=none,
		new=none,
		provisioning_timeout=none):

		self.wrapping = wrapping
		self.cloning = cloning
		self.new = new
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
	number_of_retries: int
	"""
	def __init__(
		self,
		origin_cluster_id=none,
		include_steps=none,
		number_of_retries=none):

		self.origin_cluster_id = origin_cluster_id
		self.include_steps = include_steps
		self.number_of_retries=number_of_retries

class New:
	"""
	# Arguments
	release_label: str
	number_of_retries: int
	"""
	def __init__(
		self,
		release_label=none,
		number_of_retries=none):

		self.release_label=release_label
		self.number_of_retries=number_of_retries

class ProvisioningTimeout:
	"""
	# Arguments
	timeout: int
	timeout_action: str
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
	emr_managed_master_security_group: str
	emr_managed_slave_security_group: str
	additional_master_security_groups: List[str]
	service_access_security_group: str
	custom_ami_id: str
	repo_upgrade_on_boot: str
	additional_slave_security_groups: List[str]
	ec2_key_name: str
	applications: List[Application]
	"""
	def __init__(
		self,
		ebs_root_volume_size=none,
		availability_zones=none,
		bootstrap_actions=none,
		steps=none,
		instance_groups=none,
		configurations=none,
		emr_managed_master_security_group=none,
		emr_managed_slave_security_group=none,
		additional_master_security_groups=none,
		service_access_security_group=none,
		custom_ami_id=none,
		repo_upgrade_on_boot=none,
		additional_slave_security_groups=none,
		ec2_key_name=none,
		applications=none):

		self.ebs_root_volume_size = ebs_root_volume_size
		self.availability_zones = availability_zones
		self.bootstrap_actions = bootstrap_actions
		self.steps = steps
		self.instance_groups = instance_groups
		self.configurations = configurations
		self.emr_managed_master_security_group = emr_managed_master_security_group
		self.emr_managed_slave_security_group = emr_managed_slave_security_group
		self.additional_master_security_groups = additional_master_security_groups
		self.service_access_security_group = service_access_security_group
		self.custom_ami_id = custom_ami_id
		self.repo_upgrade_on_boot = repo_upgrade_on_boot
		self.additional_slave_security_groups = additional_slave_security_groups
		self.ec2_key_name = ec2_key_name
		self.applications = applications

class AvailabilityZone:
	"""
	# Arguments
	name: str
	subnetId: str
	"""
	def __init__(
		self,
		name=none,
		subnetId=none):

		self.name = name
		self.subnetId = subnetId

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

class Application:
	"""
	# Arguments
	name: str
	args: List[str]
	version: str
	"""
	def __init__(
		self,
		name=none,
		args=none,
		version=none):
	
		self.name = name
		self.args = args
		self.version = version

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
	configurations: Configurations
	"""
	def __init__(
		self,
		instance_types=none,
		target=none,
		life_cycle=none,
		configurations=none):

		self.instance_types = instance_types
		self.target = target
		self.life_cycle = life_cycle
		self.configurations = configurations

class CoreGroup:
	"""
	# Arguments
	instance_types: List[str]
	target: int
	capacity: Capacity
	life_cycle: str
	ebs_configuration: EbsConfiguration
	configurations: Configurations
	"""
	def __init__(
		self,
		instance_types=none,
		target=none,
		capacity=none,
		life_cycle=none,
		ebs_configuration=none,
		configurations=none):

		self.instance_types = instance_types
		self.target = target
		self.capacity = capacity
		self.life_cycle = life_cycle
		self.ebs_configuration = ebs_configuration
		self.configurations = configurations

class TaskGroup:
	"""
	# Arguments
	instance_types: List[str]
	capacity: Capacity
	life_cycle: str
	ebs_configuration: EbsConfiguration
	configurations: Configurations
	"""
	def __init__(
		self,
		instance_types=none,
		capacity=none,
		life_cycle=none,
		ebs_configuration=none,
		configurations=none):

		self.instance_types = instance_types
		self.capacity = capacity
		self.life_cycle = life_cycle
		self.ebs_configuration = ebs_configuration
		self.configurations = configurations

class Capacity:
	"""
	# Arguments
	target: int
	minimum: int
	maximum: int
	unit: str
	"""
	def __init__(
		self,
		target=none,
		minimum=none,
		maximum=none,
		unit=none):

		self.target = target
		self.minimum = minimum
		self.maximum = maximum
		self.unit = unit

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

# region Cluster
class Cluster:
	"""
	# Arguments
	visible_to_all_users: Boolean
	termination_protected: Boolean
	keep_job_flow_alive_when_no_steps: Boolean
	log_uri: str
	additional_info: str
	job_flow_role: str
	security_configuration: str
	"""
	def __init__(
		self,
		visible_to_all_users=none,
		termination_protected=none,
		keep_job_flow_alive_when_no_steps=none,
		log_uri=none,
		additional_info=none,
		job_flow_role=none,
		security_configuration=none):

		self.visible_to_all_users = visible_to_all_users
		self.termination_protected = termination_protected
		self.keep_job_flow_alive_when_no_steps = keep_job_flow_alive_when_no_steps
		self.log_uri = log_uri
		self.additional_info = additional_info
		self.job_flow_role = job_flow_role
		self.security_configuration = security_configuration
# endregion

# region Scheduling
class Scheduling:
	"""
	# Arguments 
	tasks: List[Task]
	"""
	def __init__(
		self,
		tasks=none):

		self.tasks = tasks

class Task:
	"""
	# Arguments
	is_enabled: bool
	instance_group_type: str
	task_type: str
	cron_expression: str
	target_capacity: int
	min_capacity: int
	max_capacity: int
	"""
	def __init__(
		self,
		is_enabled=none,
		instance_group_type=none,
		task_type=none,
		cron_expression=none,
		target_capacity=none,
		min_capacity=none,
		max_capacity=none):

		self.is_enabled = is_enabled
		self.instance_group_type = instance_group_type
		self.task_type = task_type
		self.cron_expression = cron_expression
		self.target_capacity = target_capacity
		self.min_capacity = min_capacity
		self.max_capacity = max_capacity

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







