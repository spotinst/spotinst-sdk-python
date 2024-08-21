import json
from enum import Enum
from typing import List

none = "d3043820717d74d9a17694c176d39733"


# region WeeklyRepetitionBasis
class IntervalHours:
    """
    # Arguments
    start_time: str
    end_time: str
    """

    def __init__(
            self,
            start_time: str = none,
            end_time: str = none
    ):
        self.start_time = start_time
        self.end_time = end_time


class IntervalDays(Enum):
    Monday = "MONDAY"
    Tuesday = "TUESDAY"
    Wednesday = "WEDNESDAY"
    Thursday = "THURSDAY"
    Friday = "FRIDAY"
    Saturday = "SATURDAY"
    Sunday = "SUNDAY"


class WeeklyRepetitionBasis:
    """
    # Arguments
    interval_days: List[IntervalDays]
    interval_hours: IntervalHours
    """

    def __init__(
            self,
            interval_days: List[IntervalDays] = none,
            interval_hours: IntervalHours = none
    ):
        self.interval_days = interval_days
        self.interval_hours = interval_hours
# endregion

# region MonthlyRepetitionBasis


class WeekOfTheMonth(Enum):
    First = "FIRST"
    Second = "SECOND"
    Third = "THIRD"
    Fourth = "FOURTH"
    Last = "LAST"


class MonthlyRepetitionBasis:
    """
    # Arguments
    interval_months: List[int]
    week_of_the_month: List[WeekOfTheMonth]
    weekly_repetition_basis: WeeklyRepetitionBasis
    """

    def __init__(
            self,
            interval_months: List[int] = none,
            week_of_the_month: List[WeekOfTheMonth] = none,
            weekly_repetition_basis: WeeklyRepetitionBasis = none
    ):
        self.interval_months = interval_months
        self.week_of_the_month = week_of_the_month
        self.weekly_repetition_basis = weekly_repetition_basis
# endregion


# region RecommendationApplicationInterval
class RepetitionBasis(Enum):
    Weekly = "WEEKLY"
    Monthly = "MONTHLY"


class RecommendationApplicationInterval:
    """
    # Arguments
    repetition_basis: RepetitionBasis
    monthly_repetition_basis: MonthlyRepetitionBasis
    weekly_repetition_basis: WeeklyRepetitionBasis
    """

    def __init__(
            self,
            repetition_basis: RepetitionBasis = none,
            monthly_repetition_basis: MonthlyRepetitionBasis = none,
            weekly_repetition_basis: WeeklyRepetitionBasis = none
    ):
        self.repetition_basis = repetition_basis
        self.monthly_repetition_basis = monthly_repetition_basis
        self.weekly_repetition_basis = weekly_repetition_basis
# endregion

# region RecommendationApplicationMinThreshold


class RecommendationApplicationMinThreshold:
    """
    # Arguments
    cpu_percentage: float
    memory_percentage: float
    """

    def __init__(
            self,
            cpu_percentage: float = none,
            memory_percentage: float = none
    ):
        self.cpu_percentage = cpu_percentage
        self.memory_percentage = memory_percentage
# endregion

# region RecommendationApplicationBoundaries


class CPU:
    """
    # Arguments
    min: int
    max: int
    """

    def __init__(
            self,
            min: int = none,
            max: int = none
    ):
        self.min = min
        self.max = max


class Memory:
    """
    # Arguments
    min: int
    max: int
    """

    def __init__(
            self,
            min: int = none,
            max: int = none
    ):
        self.min = min
        self.max = max


class RecommendationApplicationBoundaries:
    """
    # Arguments
    cpu: CPU
    memory: Memory
    """

    def __init__(
            self,
            cpu: CPU = none,
            memory: Memory = none
    ):
        self.cpu = cpu
        self.memory = memory
# endregion

# region RecommendationApplicationOverheadValues


class RecommendationApplicationOverheadValues:
    """
    # Arguments
    cpu_percentage: float
    memory_percentage: float
    """

    def __init__(
            self,
            cpu_percentage: float = none,
            memory_percentage: float = none
    ):
        self.cpu_percentage = cpu_percentage
        self.memory_percentage = memory_percentage
# endregion


# region RecommendationApplicationHPA
class RecommendationApplicationHPA:
    """
    # Arguments
    allow_h_p_a_recommendations: bool
    """

    def __init__(
            self,
            allow_h_p_a_recommendations: bool = none,
    ):
        self.allow_h_p_a_recommendations = allow_h_p_a_recommendations

# endregion


# region Label

class Label:
    """
    # Arguments
    key: str
    value: str
    """

    def __init__(
            self,
            key: str = none,
            value: str = none
    ):
        self.key = key
        self.value = value
# endregion

# region Workload


class Workload:
    """
    # Arguments
    name: str
    workload_type: str
    regex_name: str
    """

    def __init__(
            self,
            name: str = none,
            workload_type: str = none,
            regex_name: str = none

    ):
        self.name = name
        self.workload_type = workload_type
        self.regex_name = regex_name

# endregion


# region Namespace


class Namespace:
    """
    # Arguments
    namespace_name: str
    labels: List[Label]
    workloads: List[Workload]
    """

    def __init__(
            self,
            namespace_name: str = none,
            labels: List[Label] = none,
            workloads: List[Workload] = none
    ):
        self.namespace_name = namespace_name
        self.labels = labels
        self.workloads = workloads
# endregion


class ClusterResources:
    """
    # Arguments
    data: dict
    """

    def __init__(
            self,
            data: dict
    ):
        self.data = data

# endregion


class ClusterLabels:
    """
    # Arguments
    data: dict
    """

    def __init__(
            self,
            data: dict
    ):
        self.data = data

# endregion


class RestartReplicas(Enum):
    More_than_one_replica = "MORE_THAN_ONE_REPLICA"
    All_manifest = "ALL_MANIFEST"
    No_restart = "NO_RESTART"


class CreateRightSizingRuleRequest:
    def __init__(self,
                 rule_name: str,
                 restart_replicas: RestartReplicas,
                 exclude_preliminary_recommendations: bool,
                 recommendation_application_intervals: List[RecommendationApplicationInterval],
                 recommendation_application_min_threshold: RecommendationApplicationMinThreshold,
                 recommendation_application_boundaries: RecommendationApplicationBoundaries,
                 recommendation_application_overhead_values: RecommendationApplicationOverheadValues,
                 recommendation_application_hpa: RecommendationApplicationHPA):
        self.rule_name = rule_name
        self.restart_replicas = restart_replicas
        self.exclude_preliminary_recommendations = exclude_preliminary_recommendations
        self.recommendation_application_intervals = recommendation_application_intervals
        self.recommendation_application_min_threshold = recommendation_application_min_threshold
        self.recommendation_application_boundaries = recommendation_application_boundaries
        self.recommendation_application_overhead_values = recommendation_application_overhead_values
        self.recommendation_application_h_p_a = recommendation_application_hpa

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class DeleteRightSizingRulesRequest:
    def __init__(self, rule_names: List[str]):
        self.rule_names = rule_names

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class UpdateRightSizingRuleRequest:
    def __init__(self,
                 restart_replicas: RestartReplicas,
                 exclude_preliminary_recommendations: bool,
                 recommendation_application_intervals: List[RecommendationApplicationInterval],
                 recommendation_application_min_threshold: RecommendationApplicationMinThreshold,
                 recommendation_application_boundaries: RecommendationApplicationBoundaries,
                 recommendation_application_overhead_values: RecommendationApplicationOverheadValues,
                 recommendation_application_hpa: RecommendationApplicationHPA):
        self.restart_replicas = restart_replicas
        self.exclude_preliminary_recommendations = exclude_preliminary_recommendations
        self.recommendation_application_intervals = recommendation_application_intervals
        self.recommendation_application_min_threshold = recommendation_application_min_threshold
        self.recommendation_application_boundaries = recommendation_application_boundaries
        self.recommendation_application_overhead_values = recommendation_application_overhead_values
        self.recommendation_application_h_p_a = recommendation_application_hpa

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class AttachRightSizingRuleRequest:
    def __init__(self, namespaces: List[Namespace]):
        self.namespaces = namespaces

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class DetachRightSizingRuleRequest:
    def __init__(self, namespaces: List[Namespace]):
        self.namespaces = namespaces

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class GetOceanRightSizingRecommendationsRequest:
    def __init__(self, cluster_resources: ClusterResources, cluster_labels: ClusterLabels):
        if cluster_resources is not None:
            self.cluster_resources = cluster_resources.data
        if cluster_labels is not None:
            self.cluster_labels = cluster_labels.data

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
