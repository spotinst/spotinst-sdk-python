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


class WeeklyRepetitionBasis:
    """
    # Arguments
    interval_days: List[str]
    interval_hours: IntervalHours
    """

    def __init__(
            self,
            interval_days: List[str] = none,
            interval_hours: IntervalHours = none
    ):
        self.interval_days = interval_days
        self.interval_hours = interval_hours
# endregion

# region MonthlyRepetitionBasis


class MonthlyRepetitionBasis:
    """
    # Arguments
    interval_months: List[str]
    week_of_the_month: List[str]
    weekly_repetition_basis: WeeklyRepetitionBasis
    """

    def __init__(
            self,
            interval_months: List[str] = none,
            week_of_the_month: List[str] = none,
            weekly_repetition_basis: WeeklyRepetitionBasis = none
    ):
        self.interval_months = interval_months
        self.week_of_the_month = week_of_the_month
        self.weekly_repetition_basis = weekly_repetition_basis
# endregion

# region RecommendationApplicationInterval


class RecommendationApplicationInterval:
    """
    # Arguments
    repetition_basis: str
    monthly_repetition_basis: MonthlyRepetitionBasis
    weekly_repetition_basis: WeeklyRepetitionBasis
    """

    def __init__(
            self,
            repetition_basis: str = none,
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
    cpu_percentage: str
    memory_percentage: str
    """

    def __init__(
            self,
            cpu_percentage: str = none,
            memory_percentage: str = none
    ):
        self.cpu_percentage = cpu_percentage
        self.memory_percentage = memory_percentage
# endregion

# region CPU


class CPU:
    """
    # Arguments
    min: str
    max: str
    """

    def __init__(
            self,
            min: str = none,
            max: str = none
    ):
        self.min = min
        self.max = max
# endregion

# region Memory


class Memory:
    """
    # Arguments
    min: str
    max: str
    """

    def __init__(
            self,
            min: str = none,
            max: str = none
    ):
        self.min = min
        self.max = max
# endregion

# region RuleName


class RuleNames:
    """
    # Arguments
    rule_names: List[str]
    """

    def __init__(
            self,
            rule_names: List[str] = none
    ):
        self.rule_names = rule_names
# endregion

# region RecommendationApplicationBoundaries


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
    cpu_percentage: str
    memory_percentage: str
    """

    def __init__(
            self,
            cpu_percentage: str = none,
            memory_percentage: str = none
    ):
        self.cpu_percentage = cpu_percentage
        self.memory_percentage = memory_percentage
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
    workload_type: str
    name: str
    """

    def __init__(
            self,
            workload_type: str = none,
            name: str = none
    ):
        self.workload_type = workload_type
        self.name = name

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


class CreateRightSizingRuleRequest:
    def __init__(self,
                 rule_name: str,
                 restart_pods: bool,
                 application_intervals: List[RecommendationApplicationInterval],
                 application_min_threshold: RecommendationApplicationMinThreshold,
                 application_boundaries: RecommendationApplicationBoundaries,
                 application_overhead_values: RecommendationApplicationOverheadValues):
        self.rule_name = rule_name
        self.restart_pods = restart_pods
        self.recommendation_application_intervals = application_intervals
        self.recommendation_application_min_threshold = application_min_threshold
        self.recommendation_application_boundaries = application_boundaries
        self.recommendation_application_overhead_values = application_overhead_values

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
                 rule_name: str,
                 restart_pods: bool,
                 application_intervals: List[RecommendationApplicationInterval],
                 application_min_threshold: RecommendationApplicationMinThreshold,
                 application_boundaries: RecommendationApplicationBoundaries,
                 application_overhead_values: RecommendationApplicationOverheadValues):
        self.rule_name = rule_name
        self.restart_pods = restart_pods
        self.recommendation_application_intervals = application_intervals
        self.recommendation_application_min_threshold = application_min_threshold
        self.recommendation_application_boundaries = application_boundaries
        self.recommendation_application_overhead_values = application_overhead_values

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
