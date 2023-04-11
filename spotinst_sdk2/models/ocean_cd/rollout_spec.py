import json
from enum import Enum
from typing import List

none = "d3043820717d74d9a17694c176d39733"


# region SpotDeployment
class SpotDeployment:
    """
    # Arguments
    cluster_id: str
    name: str
    namespace: str
    """

    def __init__(
            self,
            cluster_id: str = none,
            name: str = none,
            namespace: str = none):
        self.cluster_id = cluster_id
        self.name = name
        self.namespace = namespace
# endregion


# region Strategy
class SecretRef:
    """
    # Arguments
    name: str
    key: str
    """

    def __init__(
            self,
            name: str = none,
            key: str = none):
        self.name = name
        self.key = key


class FieldRef:
    """
    # Arguments
    field_path: str
    """

    def __init__(
            self,
            field_path: str = none):
        self.field_path = field_path


class ValueFrom:
    """
    # Arguments
    secret_ref: SecretRef
    field_ref: FieldRef
    """

    def __init__(
            self,
            secret_ref: SecretRef = none,
            field_ref: FieldRef = none):
        self.secret_ref = secret_ref
        self.field_ref = field_ref


class Argument:
    """
    # Arguments
    name: str
    value: str
    value_from: ValueFrom
    """

    def __init__(
            self,
            name: str = none,
            value: str = none,
            value_from: ValueFrom = none):
        self.name = name
        self.value = value
        self.value_from = value_from


class Strategy:
    """
    # Arguments
    name: str
    args: List[Argument]
    """

    def __init__(
            self,
            name: str = none,
            args: List[Argument] = none):
        self.name = name
        self.args = args
# endregion


# region Traffic
class TlsRoutes:
    """
    # Arguments
    port: int
    sni_hosts: List[str]
    """

    def __init__(
            self,
            port: int = none,
            sni_hosts: List[str] = none):
        self.port = port
        self.sni_hosts = sni_hosts


class VirtualServices:
    """
    # Arguments
    name: str
    routes: List[str]
    tls_routes: List[TlsRoutes]
    """

    def __init__(
            self,
            name: str = none,
            routes: List[str] = none,
            tls_routes: List[TlsRoutes] = none):
        self.name = name
        self.routes = routes
        self.tls_routes = tls_routes


class DestinationRule:
    """
    # Arguments
    name: str
    canary_subset_name: str
    stable_subset_name: str
    """

    def __init__(
            self,
            name: str = none,
            canary_subset_name: str = none,
            stable_subset_name: str = none):
        self.name = name
        self.canary_subset_name = canary_subset_name
        self.stable_subset_name = stable_subset_name


class Istio:
    """
    # Arguments
    virtual_services: List[VirtualServices]
    destination_rule: DestinationRule
    """

    def __init__(
            self,
            virtual_services: List[VirtualServices] = none,
            destination_rule: DestinationRule = none):
        self.virtual_services = virtual_services
        self.destination_rule = destination_rule


class Nginx:
    """
    # Arguments
    annotation_prefix: str
    stable_ingress: str
    """

    def __init__(
            self,
            annotation_prefix: str = none,
            stable_ingress: str = none):
        self.annotation_prefix = annotation_prefix
        self.stable_ingress = stable_ingress


class StickinessConfig:
    """
    # Arguments
    enabled: bool
    duration_seconds: int
    """

    def __init__(
            self,
            enabled: bool = none,
            duration_seconds: int = none):
        self.enabled = enabled
        self.duration_seconds = duration_seconds


class Alb:
    """
    # Arguments
    ingress: str
    service_port: int
    root_service: str
    stickiness_config: StickinessConfig
    annotation_prefix: str
    """

    def __init__(
            self,
            ingress: str = none,
            service_port: int = none,
            root_service: str = none,
            stickiness_config: StickinessConfig = none,
            annotation_prefix: str = none):
        self.ingress = ingress
        self.service_port = service_port
        self.root_service = root_service
        self.stickiness_config = stickiness_config
        self.annotation_prefix = annotation_prefix


class Smi:
    """
    # Arguments
    root_service: str
    traffic_split_name: str
    """

    def __init__(
            self,
            root_service: str = none,
            traffic_split_name: str = none):
        self.root_service = root_service
        self.traffic_split_name = traffic_split_name


class Ambassador:
    """
    # Arguments
    mappings: List[str]
    """

    def __init__(
            self,
            mappings: List[str] = none):
        self.mappings = mappings


class VirtualService:
    """
    # Arguments
    name: str
    routes: List[str]
    """

    def __init__(
            self,
            name: str = none,
            routes: List[str] = none):
        self.name = name
        self.routes = routes


class CanaryVirtualNodeRef:
    """
    # Arguments
    name: str
    """

    def __init__(
            self,
            name: str = none):
        self.name = name


class StableVirtualNodeRef:
    """
    # Arguments
    name: str
    """

    def __init__(
            self,
            name: str = none):
        self.name = name


class VirtualNodeGroup:
    """
    # Arguments
    canary_virtual_node_ref: CanaryVirtualNodeRef
    stable_virtual_node_ref: StableVirtualNodeRef
    """

    def __init__(
            self,
            canary_virtual_node_ref: CanaryVirtualNodeRef = none,
            stable_virtual_node_ref: StableVirtualNodeRef = none):
        self.canary_virtual_node_ref = canary_virtual_node_ref
        self.stable_virtual_node_ref = stable_virtual_node_ref


class AppMesh:
    """
    # Arguments
    virtual_service: VirtualService
    virtual_node_group: VirtualNodeGroup
    """

    def __init__(
            self,
            virtual_service: VirtualService = none,
            virtual_node_group: VirtualNodeGroup = none):
        self.virtual_service = virtual_service
        self.virtual_node_group = virtual_node_group


class PingPong:
    """
    ping_service: str
    pong_service: str
    """

    def __init__(
            self,
            ping_service: str = none,
            pong_service: str = none):
        self.ping_service = ping_service
        self.pong_service = pong_service


class Traffic:
    """
    # Arguments
    canary_service: str
    stable_service: str
    istio: Istio
    nginx: Nginx
    alb: Alb
    smi: Smi
    ambassador: Ambassador
    app_mesh: AppMesh
    ping_pong: PingPong
    """

    def __init__(
            self,
            canary_service: str = none,
            stable_service: str = none,
            istio: Istio = none,
            nginx: Nginx = none,
            alb: Alb = none,
            smi: Smi = none,
            ambassador: Ambassador = none,
            app_mesh: AppMesh = none,
            ping_pong: PingPong = none):
        self.canary_service = canary_service
        self.stable_service = stable_service
        self.istio = istio
        self.nginx = nginx
        self.alb = alb
        self.smi = smi
        self.ambassador = ambassador
        self.app_mesh = app_mesh
        self.ping_pong = ping_pong
# endregion


# region Failure Policy
class FailureAction(Enum):
    abort = "abort"
    pause = "pause"
    promote = "promote"


class FailurePolicy:
    """
    # Arguments
    action: FailureAction
    """

    def __init__(
            self,
            action: FailureAction = none):
        self.action = action
# endregion


# region rolloutSpec
class RolloutSpec:
    """
    # Arguments
    name: str
    spot_deployment: SpotDeployment
    strategy: Strategy
    traffic: Traffic
    failure_policy: FailurePolicy
    """

    def __init__(
            self,
            name: str = none,
            spot_deployment: SpotDeployment = none,
            strategy: Strategy = none,
            traffic: Traffic = none,
            failure_policy: FailurePolicy = none):
        self.name = name
        self.spot_deployment = spot_deployment
        self.strategy = strategy
        self.traffic = traffic
        self.failure_policy = failure_policy
# endregion


# region Client Requests
class CreateRolloutSpecRequest:
    """
    # Arguments
    rollout_spec : RolloutSpec
    """

    def __init__(self, rollout_spec: RolloutSpec):
        self.rollout_spec = rollout_spec

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
# endregion
