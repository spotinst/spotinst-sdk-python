import json
from typing import List

none = "d3043820717d74d9a17694c176d39733"


# region ClusterNotification
class ClusterNotification:
    """
    # Arguments
    minutes_without_heartbeat: int
    providers: List[str]
    """

    def __init__(
            self,
            minutes_without_heartbeat: int = none,
            providers: List[str] = none):
        self.minutes_without_heartbeat = minutes_without_heartbeat
        self.providers = providers
# endregion


# region Client Requests
class UpdateClusterNotification:
    def __init__(self, cluster_notification: ClusterNotification):
        self.cluster_notification = cluster_notification

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
# endregion
