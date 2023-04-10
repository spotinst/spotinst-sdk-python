import json
from typing import List

none = "d3043820717d74d9a17694c176d39733"


class BackgroundVerification:
    """
    # Arguments
    template_names: List[str]
    """

    def __init__(
            self,
            template_names: List[str] = none):
        self.template_names = template_names


class Scale:
    """
    # Arguments
    match_traffic_weight: bool
    replicas: int
    weight: int
    """

    def __init__(
            self,
            match_traffic_weight: bool = none,
            replicas: int = none,
            weight: int = none):
        self.match_traffic_weight = match_traffic_weight
        self.replicas = replicas
        self.weight = weight


class Verification:
    """
    # Arguments
    template_names: List[str]
    """

    def __init__(
            self,
            template_names: List[str] = none):
        self.template_names = template_names


class Pause:
    """
    # Arguments
    duration: str
    """

    def __init__(
            self,
            duration: str = none):
        self.duration = duration


class HeaderValue:
    """
    # Arguments
    exact: str
    prefix: str
    regex: str
    """

    def __init__(
            self,
            exact: str = none,
            prefix: str = none,
            regex: str = none):
        self.exact = exact
        self.prefix = prefix
        self.regex = regex


class Match:
    """
    # Arguments
    header_name: str
    header_value: HeaderValue
    """

    def __init__(
            self,
            header_name: str = none,
            header_value: HeaderValue = none):
        self.header_name = header_name
        self.header_value = header_value


class HeaderRoute:
    """
    # Arguments
    name: str
    match: List[Match]
    """

    def __init__(
            self,
            name: str = none,
            match: List[Match] = none):
        self.name = name
        self.match = match


class Steps:
    """
    # Arguments
    name: str
    set_weight: int
    set_canary_scale: Scale
    verification: Verification
    pause: Pause
    set_header_route: HeaderRoute
    """

    def __init__(
            self,
            name: str = none,
            set_weight: int = none,
            set_canary_scale: Scale = none,
            verification: Verification = none,
            pause: Pause = none,
            set_header_route: HeaderRoute = none):
        self.name = name
        self.set_weight = set_weight
        self.set_canary_scale = set_canary_scale
        self.verification = verification
        self.pause = pause
        self.set_header_route = set_header_route


class Canary:
    """
    # Arguments
    background_verification: BackgroundVerification
    steps: List[Steps]
    """

    def __init__(
            self,
            background_verification: BackgroundVerification = none,
            steps: List[Steps] = none):
        self.background_verification = background_verification
        self.steps = steps


class RollingPause:
    """
    # Arguments
    duration: str
    """

    def __init__(
            self,
            duration: str = none):
        self.duration = duration


class RollingUpdate:
    """
    # Arguments
    name: str
    pause: RollingPause
    verification: Verification
    """

    def __init__(
            self,
            name: str = none,
            pause: RollingPause = none,
            verification: Verification = none):
        self.name = name
        self.pause = pause
        self.verification = verification


class Strategy:
    """
    # Arguments
    name: str
    canary: Canary
    rolling: RollingUpdate
    created_at: str
    updated_at: str
    """

    def __init__(
            self,
            name: str = none,
            canary: Canary = none,
            rolling: RollingUpdate = none,
            created_at: str = none,
            updated_at: str = none):
        self.name = name
        self.canary = canary
        self.rolling = rolling
        self.created_at = created_at
        self.updated_at = updated_at


class StrategyRequest:
    """
    # Arguments
    strategy : Strategy
    """

    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
