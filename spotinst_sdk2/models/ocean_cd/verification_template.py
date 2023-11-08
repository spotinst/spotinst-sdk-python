import json
from enum import Enum
from typing import List

none = "d3043820717d74d9a17694c176d39733"

# region Verification Arguments


class SecretKeyRef:
    """
    # Arguments
    key : str
    name : str
    """

    def __init__(
            self,
            key: str = none,
            name: str = none):
        self.key = key
        self.name = name


class VerificationTemplateArgument:
    """
    # Arguments
    name : str
    secret_key_ref : SecretKeyRef
    value : str
    """

    def __init__(
            self,
            name: str = none,
            secret_key_ref: SecretKeyRef = none,
            value: str = none):
        self.name = name
        self.secret_key_ref = secret_key_ref
        self.value = value
# endregion


# region Verification Metrics
class Prometheus:
    """
    # Arguments
    query : str
    """

    def __init__(
            self,
            query: str = none):
        self.query = query


class NewRelic:
    """
    # Arguments
    profile : str
    query : str
    """

    def __init__(
            self,
            profile: str = none,
            query: str = none):
        self.profile = profile
        self.query = query


class Datadog:
    """
    # Arguments
    duration : str
    query : str
    """

    def __init__(
            self,
            duration: str = none,
            query: str = none):
        self.duration = duration
        self.query = query


class Dimensions:
    """
    # Arguments
    name : str
    value : str
    """

    def __init__(
            self,
            name: str = none,
            value: str = none):
        self.name = name
        self.value = value


class MetricUnit(Enum):
    Seconds = "Seconds"
    Microseconds = "Microseconds"
    Milliseconds = "Milliseconds"
    Bytes = "Bytes"
    Kilobytes = "Kilobytes"
    Megabytes = "Megabytes"
    Gigabytes = "Gigabytes"
    Terabytes = "Terabytes"
    Bits = "Bits"
    Kilobits = "Kilobits"
    Megabits = "Megabits"
    Gigabits = "Gigabits"
    Terabits = "Terabits"
    Percent = "Percent"
    Count = "Count"
    BytesBySecond = "Bytes/Second"
    KilobytesBySecond = "Kilobytes/Second"
    MegabytesBySecond = "Megabytes/Second"
    GigabytesBySecond = "Gigabytes/Second"
    TerabytesBySecond = "Terabytes/Second"
    BitsBySecond = "Bits/Second"
    KilobitsBySecond = "Kilobits/Second"
    MegabitsBySecond = "Megabits/Second"
    GigabitsBySecond = "Gigabits/Second"
    TerabitsBySecond = "Terabits/Second"
    CountBySecond = "Count/Second"
    NONE = "None"


class Metric:
    """
    # Arguments
    metric_name : str
    namespace : str
    dimensions : List[Dimensions]
    """

    def __init__(
            self,
            metric_name: str = none,
            namespace: str = none,
            dimensions: List[Dimensions] = none):
        self.metric_name = metric_name
        self.namespace = namespace
        self.dimensions = dimensions


class MetricStat:
    """
    # Arguments
    metric : Metric
    period : int
    stat : str
    unit : MetricUnit
    """

    def __init__(
            self,
            metric: Metric = none,
            period: int = none,
            stat: str = none,
            unit: MetricUnit = none):
        self.metric = metric
        self.period = period
        self.stat = stat
        self.unit = unit


class MetricDataQueries:
    """
    # Arguments
    id : str
    metric_stat : MetricStat
    expression : str
    label : str
    return_data : boolean
    period : int
    """

    def __init__(
            self,
            id: str = none,
            metric_stat: MetricStat = none,
            expression: str = none,
            label: str = none,
            return_data: bool = none,
            period: int = none):
        self.id = id
        self.metric_stat = metric_stat
        self.expression = expression
        self.label = label
        self.return_data = return_data
        self.period = period


class CloudWatch:
    """
    # Arguments
    duration : str
    metric_data_queries : List[MetricDataQueries]
    """

    def __init__(
            self,
            duration: str = none,
            metric_data_queries: List[MetricDataQueries] = none):
        self.duration = duration
        self.metric_data_queries = metric_data_queries


class Headers:
    """
    # Arguments
    key : str
    value : str
    """

    def __init__(
            self,
            key: str = none,
            value: str = none):
        self.key = key
        self.value = value


class Web:
    """
    # Arguments
    method : str
    url : str
    headers : List[Headers]
    body : str
    timeout_seconds : int
    json_path : str
    insecure : bool
    """

    def __init__(
            self,
            method: str = none,
            url: str = none,
            headers: List[Headers] = none,
            body: str = none,
            timeout_seconds: int = none,
            json_path: str = none,
            insecure: bool = none):
        self.method = method
        self.url = url
        self.headers = headers
        self.body = body
        self.timeout_seconds = timeout_seconds
        self.json_path = json_path
        self.insecure = insecure


class Containers:
    """
    # Arguments
    name : str
    command : List[str]
    image : str
    """

    def __init__(
            self,
            name: str = none,
            command: List[str] = none,
            image: str = none):
        self.name = name
        self.command = command
        self.image = image


class TemplateSpec:
    """
    # Arguments
    containers : List[Containers]
    restart_policy : str
    """

    def __init__(
            self,
            containers: List[Containers] = none,
            restart_policy: str = none):
        self.containers = containers
        self.restart_policy = restart_policy


class JobSpec:
    """
    # Arguments
    backoff_limit : int
    template : TemplateSpec
    """

    def __init__(
            self,
            backoff_limit: int = none,
            template: TemplateSpec = none):
        self.backoff_limit = backoff_limit
        self.template = template


class Job:
    """
    # Arguments
    spec : JobSpec
    """

    def __init__(
            self,
            spec: JobSpec = none):
        self.spec = spec


class Provider:
    """
    # Arguments
    prometheus : Prometheus
    new_relic : NewRelic
    datadog : Datadog
    cloud_watch : CloudWatch
    web : Web
    job : Job
    """

    def __init__(
            self,
            prometheus: Prometheus = none,
            new_relic: NewRelic = none,
            datadog: Datadog = none,
            cloud_watch: CloudWatch = none,
            web: Web = none,
            job: Job = none):
        self.prometheus = prometheus
        self.new_relic = new_relic
        self.datadog = datadog
        self.cloud_watch = cloud_watch
        self.web = web
        self.job = job


class VerificationMetric:
    """
    # Arguments
    name : str
    dry_run : boolean
    interval : str
    initial_delay : str
    count : int
    success_condition : str
    failure_condition : str
    failure_limit : int
    consecutive_error_limit : int
    provider : Provider
    """

    def __init__(
            self,
            name: str = none,
            dry_run: bool = none,
            interval: str = none,
            initial_delay: str = none,
            count: int = none,
            success_condition: str = none,
            failure_condition: str = none,
            failure_limit: int = none,
            consecutive_error_limit: int = none,
            provider: Provider = none):
        self.name = name
        self.dry_run = dry_run
        self.interval = interval
        self.initial_delay = initial_delay
        self.count = count
        self.success_condition = success_condition
        self.failure_condition = failure_condition
        self.failure_limit = failure_limit
        self.consecutive_error_limit = consecutive_error_limit
        self.provider = provider
# endregion


# region Verification Template
class VerificationTemplate:
    """
    # Arguments
    name : str
    args : List[VerificationTemplateArgument]
    metrics : List[VerificationMetric]
    """

    def __init__(
            self,
            name: str = none,
            args: List[VerificationTemplateArgument] = none,
            metrics: List[VerificationMetric] = none,
            created_at: str = none,
            updated_at: str = none):
        self.name = name
        self.args = args
        self.metrics = metrics
# endregion


# region Client Requests
class CreateVerificationTemplateRequest:
    """
    # Arguments
    verification_template : VerificationTemplate
    """

    def __init__(self, verification_template: VerificationTemplate):
        self.verification_template = verification_template

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
# endregion
