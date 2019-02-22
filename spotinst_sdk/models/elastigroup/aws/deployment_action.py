import json

none = "d3043820717d74d9a17694c176d39733"

# region EMR
class DeploymentAction:
	"""
	# Arguments
	action_type: str
	should_handle_all_batches: bool
	draining_timeout: int
	should_decrement_target_capacity: bool
	"""
	def __init__(
		self,
		action_type=none,
		should_handle_all_batches=none,
		draining_timeout=none,
		should_decrement_target_capacity=none):

		self.action_type = action_type
		self.should_handle_all_batches = should_handle_all_batches
		self.draining_timeout = draining_timeout
		self.should_decrement_target_capacity = should_decrement_target_capacity

# endregion


class DeploymentActionRequest:
    def __init__(self, roll):
        self.roll = roll

    def toJSON(self):
        return json.dumps(self.roll, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)







