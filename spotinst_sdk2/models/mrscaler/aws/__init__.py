import json
from typing import List

none = "d3043820717d74d9a17694c176d39733"


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
    service_role: str
    security_configuration: str
    """

    def __init__(
            self,
            visible_to_all_users: bool = none,
            termination_protected: bool = none,
            keep_job_flow_alive_when_no_steps: bool = none,
            log_uri: str = none,
            additional_info: str = none,
            job_flow_role: str = none,
            service_role: str = none,
            security_configuration: str = none):

        self.visible_to_all_users = visible_to_all_users
        self.termination_protected = termination_protected
        self.keep_job_flow_alive_when_no_steps = keep_job_flow_alive_when_no_steps
        self.log_uri = log_uri
        self.additional_info = additional_info
        self.job_flow_role = job_flow_role
        self.service_role = service_role
        self.security_configuration = security_configuration
# endregion


# region Strategy

class Wrapping:
    """
    # Arguments
    source_cluster_id: str
    """

    def __init__(
            self,
            source_cluster_id: str = none):

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
            origin_cluster_id: str = none,
            include_steps: bool = none,
            number_of_retries: int = none):

        self.origin_cluster_id = origin_cluster_id
        self.include_steps = include_steps
        self.number_of_retries = number_of_retries


class New:
    """
    # Arguments
    release_label: str
    number_of_retries: int
    """

    def __init__(
            self,
            release_label: str = none,
            number_of_retries: int = none):

        self.release_label = release_label
        self.number_of_retries = number_of_retries


class ProvisioningTimeout:
    """
    # Arguments
    timeout: int
    timeout_action: str
    """

    def __init__(
            self,
            timeout: int = none,
            timeout_action: str = none):

        self.timeout = timeout
        self.timeout_action = timeout_action


class Strategy:
    """
    # Arguments
    wrapping: Wrapping
    cloning: Cloning
    new: New
    provisioning_timeout: ProvisioningTimeout
    """

    def __init__(
            self,
            wrapping: Wrapping = none,
            cloning: Cloning = none,
            new: New = none,
            provisioning_timeout: ProvisioningTimeout = none):

        self.wrapping = wrapping
        self.cloning = cloning
        self.new = new
        self.provisioning_timeout = provisioning_timeout


# endregion


# region Compute

class Application:
    """
    # Arguments
    name: str
    args: List[str]
    version: str
    """

    def __init__(
            self,
            name: str = none,
            args: List[str] = none,
            version: str = none):

        self.name = name
        self.args = args
        self.version = version


class AvailabilityZone:
    """
    # Arguments
    name: str
    subnetId: str
    """

    def __init__(
            self,
            name: str = none,
            subnet_id: str = none):

        self.name = name
        self.subnet_id = subnet_id


class File:
    """
    # Arguments
    bucket: str
    key: str
    """

    def __init__(
            self,
            bucket: str = none,
            key: str = none):

        self.bucket = bucket
        self. key = key


class ScriptBootstrapAction:
    """
    # Arguments
    args: List[str]
    path: str
    """

    def __init__(
            self,
            args: List[str] = none,
            path: str = none):

        self.args = args
        self.path = path


class JsonConfiguration:
    """
    # Arguments
    name: str
    script_bootstrap_action: ScriptBootstrapAction
    """

    def __init__(
            self,
            name: str = none,
            script_bootstrap_action: ScriptBootstrapAction = none):

        self.name = name
        self.script_bootstrap_action = script_bootstrap_action


class BootstrapActions:
    """
    # Arguments
    file: File
    json_configuration: List[JsonConfiguration]
    """

    def __init__(
            self,
            file: File = none,
            json_configuration: List[JsonConfiguration] = none):

        self.file = file
        self.json_configuration = json_configuration


class Configurations:
    """
    # Arguments
    file: File
    """

    def __init__(
            self,
            file: File = none):

        self.file = file


class DynamicVolumeSize:
    """
    # Arguments
    base_size: int
    resource: str
    size_per_resource_unit: int
    """

    def __init__(
            self,
            base_size: int = none,
            resource: str = none,
            size_per_resource_unit: int = none):

        self.base_size = base_size
        self.resource = resource
        self.size_per_resource_unit = size_per_resource_unit


class VolumeSpecification:
    """
    # Arguments
    volume_type: str
    size_in_g_b: int
    iops: int
    dynamic_volume_size: DynamicVolumeSize
    """

    def __init__(
            self,
            volume_type: str = none,
            size_in_g_b: int = none,
            iops: int = none,
            dynamic_volume_size: DynamicVolumeSize = none):

        self.volume_type = volume_type
        self.size_in_g_b = size_in_g_b
        self.iops = iops
        self.dynamic_volume_size = dynamic_volume_size


class SingleEbsConfig:
    """
    # Arguments
    volume_specification: VolumeSpecification
    volumes_per_instance: int
    """

    def __init__(
            self,
            volume_specification: VolumeSpecification = none,
            volumes_per_instance: int = none):

        self.volume_specification = volume_specification
        self.volumes_per_instance = volumes_per_instance


class EbsConfiguration:
    """
    # Arguments
    ebs_optimized: bool
    ebs_block_device_configs: List[SingleEbsConfig]
    """

    def __init__(
            self,
            ebs_optimized: bool = none,
            ebs_block_device_configs: List[SingleEbsConfig] = none):

        self.ebs_optimized = ebs_optimized
        self.ebs_block_device_configs = ebs_block_device_configs


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
            target: int = none,
            minimum: int = none,
            maximum: int = none,
            unit: str = none):

        self.target = target
        self.minimum = minimum
        self.maximum = maximum
        self.unit = unit


class MasterGroup:
    """
    # Arguments
    instance_types: List[str]
    target: int
    life_cycle: str
    ebs_configuration: EbsConfiguration
    configurations: Configurations
    """

    def __init__(
            self,
            instance_types: List[str] = none,
            target: int = none,
            life_cycle: str = none,
            ebs_configuration: EbsConfiguration = none,
            configurations: Configurations = none):

        self.instance_types = instance_types
        self.target = target
        self.life_cycle = life_cycle
        self.ebs_configuration = ebs_configuration
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
            instance_types: List[str] = none,
            target: int = none,
            capacity: Capacity = none,
            life_cycle: str = none,
            ebs_configuration: EbsConfiguration = none,
            configurations: Configurations = none):

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
            instance_types: List[str] = none,
            capacity: Capacity = none,
            life_cycle: str = none,
            ebs_configuration: EbsConfiguration = none,
            configurations: Configurations = none):

        self.instance_types = instance_types
        self.capacity = capacity
        self.life_cycle = life_cycle
        self.ebs_configuration = ebs_configuration
        self.configurations = configurations


class InstanceGroups:
    """
    # Arguments
    master_group: MasterGroup
    core_group: CoreGroup
    task_group: TaskGroup
    """

    def __init__(
            self,
            master_group: MasterGroup = none,
            core_group: CoreGroup = none,
            task_group: TaskGroup = none):

        self.master_group = master_group
        self.core_group = core_group
        self.task_group = task_group


class InstanceWeight:
    """
    # Arguments
    instance_type: str
    weighted_capacity: int
    """

    def __init__(
            self,
            instance_type: str = none,
            weighted_capacity: int = none):

        self.instance_type = instance_type
        self.weighted_capacity = weighted_capacity


class Steps:
    """
    # Arguments
    file: File
    """

    def __init__(
            self,
            file=none):

        self.file = file


class Tag:
    """
    # Arguments
    tag_key: str
    tag_value: str
    """

    def __init__(
            self,
            tag_key: str = none,
            tag_value: str = none):

        self.tag_key = tag_key
        self.tag_value = tag_value


class Compute:
    """
    # Arguments
    additional_master_security_groups: List[str]
    additional_slave_security_groups: List[str]
    applications: List[Application]
    availability_zones: List[AvailabilityZone]
    bootstrap_actions: BootstrapActions
    configurations: Configurations
    custom_ami_id: str
    ebs_root_volume_size: int
    ec2_key_name: str
    emr_managed_master_security_group: str
    emr_managed_slave_security_group: str
    instance_groups: InstanceGroups
    instance_weights: List[InstanceWeight]
    repo_upgrade_on_boot: str
    service_access_security_group: str
    steps: Steps
    tags: List[Tag]
    """

    def __init__(
            self,
            additional_master_security_groups: List[str] = none,
            additional_slave_security_groups: List[str] = none,
            applications: List[Application] = none,
            availability_zones: List[AvailabilityZone] = none,
            bootstrap_actions: BootstrapActions = none,
            configurations: Configurations = none,
            custom_ami_id: str = none,
            ebs_root_volume_size: int = none,
            ec2_key_name: str = none,
            emr_managed_master_security_group: str = none,
            emr_managed_slave_security_group: str = none,
            instance_groups: InstanceGroups = none,
            instance_weights: List[InstanceWeight] = none,
            repo_upgrade_on_boot: str = none,
            service_access_security_group: str = none,
            steps: Steps = none,
            tags: List[Tag] = none):

        self.additional_master_security_groups = additional_master_security_groups
        self.additional_slave_security_groups = additional_slave_security_groups
        self.applications = applications
        self.availability_zones = availability_zones
        self.bootstrap_actions = bootstrap_actions
        self.configurations = configurations
        self.custom_ami_id = custom_ami_id
        self.ebs_root_volume_size = ebs_root_volume_size
        self.ec2_key_name = ec2_key_name
        self.emr_managed_master_security_group = emr_managed_master_security_group
        self.emr_managed_slave_security_group = emr_managed_slave_security_group
        self.instance_groups = instance_groups
        self.instance_weights = instance_weights
        self.repo_upgrade_on_boot = repo_upgrade_on_boot
        self.service_access_security_group = service_access_security_group
        self.steps = steps
        self.tags = tags

# endregion


# region Scheduling

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
            is_enabled: bool = none,
            instance_group_type: str = none,
            task_type: str = none,
            cron_expression: str = none,
            target_capacity: int = none,
            min_capacity: int = none,
            max_capacity: int = none):

        self.is_enabled = is_enabled
        self.instance_group_type = instance_group_type
        self.task_type = task_type
        self.cron_expression = cron_expression
        self.target_capacity = target_capacity
        self.min_capacity = min_capacity
        self.max_capacity = max_capacity


class Scheduling:
    """
    # Arguments 
    tasks: List[Task]
    """

    def __init__(
            self,
            tasks: List[Task] = none):

        self.tasks = tasks

# endregion


# region Scaling

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
            type: str = none,
            adjustment: int = none,
            min_target_capacity: int = none,
            target: int = none,
            minimum: int = none,
            maximum: int = none):

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
    value: str
    """

    def __init__(
            self,
            name: str = none,
            value: str = none):

        self.name = name
        self.value = value


class Metric:
    """
    # Arguments
    policy_name: str
    metric_name: str
    statistic: str
    unit: str
    threshold: int
    adjustment: int
    namespace: str
    min_target_capacity: int
    period: int
    evaluation_periods: int
    action: Action
    cooldown: int
    dimensions: List[Dimension]
    operator: str
    """

    def __init__(
            self,
            policy_name: str = none,
            metric_name: str = none,
            statistic: str = none,
            unit: str = none,
            threshold: int = none,
            adjustment: int = none,
            namespace: str = none,
            min_target_capacity: int = none,
            period: int = none,
            evaluation_periods: int = none,
            action: Action = none,
            cooldown: int = none,
            dimensions: List[Dimension] = none,
            operator: str = none):

        self.policy_name = policy_name
        self.metric_name = metric_name
        self.statistic = statistic
        self.unit = unit
        self.threshold = threshold
        self.adjustment = adjustment
        self.namespace = namespace
        self.min_target_capacity = min_target_capacity
        self.period = period
        self.evaluation_periods = evaluation_periods
        self.action = action
        self.cooldown = cooldown
        self.dimensions = dimensions
        self.operator = operator


class Scaling:
    """
    # Arguments
    up: List[Metric]
    down: List[Metric]
    """

    def __init__(
            self,
            up: List[Metric] = none,
            down: List[Metric] = none):

        self.up = up
        self.down = down

# endregion

# region TerminationPolicy


class Statement:
    """
    # Arguments
    metric_name: str
    statistic: str
    unit: str
    threshold: int
    namespace: str
    period: int
    evaluation_periods: int
    operator: str
    """

    def __init__(
            self,
            metric_name: str = none,
            statistic: str = none,
            unit: str = none,
            threshold: int = none,
            evaluation_periods: int = none,
            namespace: str = none,
            period: int = none,
            operator: str = none):

        self.metric_name = metric_name
        self.statistic = statistic
        self.unit = unit
        self.threshold = threshold
        self.evaluation_periods = evaluation_periods
        self.namespace = namespace
        self.period = period
        self.operator = operator


class TerminationPolicy:
    """
    # Arguments
    statements: List[Statement]
    """

    def __init__(
            self,
            statements: List[Statement] = none):

        self.statements = statements

# endregion

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
    termination_policies: List[TerminationPolicy]
    """

    def __init__(
            self,
            name: str = none,
            description: str = none,
            region: str = none,
            strategy: Strategy = none,
            compute: Compute = none,
            cluster: Cluster = none,
            scheduling: Scheduling = none,
            scaling: Scaling = none,
            termination_policies: List[TerminationPolicy] = none):

        self.name = name
        self.description = description
        self.region = region
        self.strategy = strategy
        self.compute = compute
        self.cluster = cluster
        self.scheduling = scheduling
        self.scaling = scaling
        self.termination_policies = termination_policies

# endregion


class EMRCreationRequest:
    def __init__(self, mrScaler):
        self.mrScaler = mrScaler

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
