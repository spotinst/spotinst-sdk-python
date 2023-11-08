import json
from enum import Enum

none = "d3043820717d74d9a17694c176d39733"


# region Rollouts
class SpotDeployment:
    """
    # Arguments
    name: str
    old_version: str
    new_version: str
    old_manifest: str
    new_manifest: str
    """

    def __init__(
            self,
            name: str = none,
            old_version: str = none,
            new_version: str = none,
            old_manifest: str = none,
            new_manifest: str = none):
        self.name = name
        self.old_version = old_version
        self.new_version = new_version
        self.old_manifest = old_manifest
        self.new_manifest = new_manifest


class Status(Enum):
    manual_pausing = 'manualPausing'
    deallocating = 'deallocating'
    manual_paused = 'manualPaused'
    canceled = 'canceled'
    pending = 'pending'
    in_progress = 'inProgress'
    finished = 'finished'
    failed = 'failed'
    paused = 'paused'
    aborting = 'aborting'
    aborted = 'aborted'


class Rollouts:
    """
    # Arguments
    spot_deployment: SpotDeployment
    namespace: str
    cluster_id: str
    original_rollout_id: str
    new_rollout_id: str
    strategy: str
    strategy_type: str
    strategy_name: str
    status: Status
    start_time: str
    end_time: str
    rollout_spec: str
    cloud_provider: str
    identity: str
    """

    def __init__(
            self,
            spot_deployment: SpotDeployment = none,
            namespace: str = none,
            cluster_id: str = none,
            original_rollout_id: str = none,
            new_rollout_id: str = none,
            strategy: str = none,
            strategy_type: str = none,
            strategy_name: str = none,
            status: Status = none,
            start_time: str = none,
            end_time: str = none,
            rollout_spec: str = none,
            cloud_provider: str = none,
            identity: str = none):
        self.spot_deployment = spot_deployment
        self.namespace = namespace
        self.cluster_id = cluster_id
        self.original_rollout_id = original_rollout_id
        self.new_rollout_id = new_rollout_id
        self.strategy = strategy
        self.strategy_type = strategy_type
        self.strategy_name = strategy_name
        self.status = status
        self.start_time = start_time
        self.end_time = end_time
        self.rollout_spec = rollout_spec
        self.cloud_provider = cloud_provider
        self.identity = identity
# endregion


# region Action
class Action(Enum):
    promote = 'promote'
    promote_full = 'promoteFull'
    pause = 'pause'
    abort = 'abort'
    retry = 'retry'
# endregion


# region Client Requests
class CreateRolloutActionRequest:
    """
    # Arguments
    action : Action
    """

    def __init__(self, action: Action):
        self.action = action

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
# endregion
