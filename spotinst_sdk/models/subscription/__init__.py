import json

none = "d3043820717d74d9a17694c176d39733"

# region Subscription
class Subscription:
	"""
	# Arguments
	resource_id: str
	protocol: str
	endpoint: str
	event_type: str
	event_format: dict
	"""
	def __init__(
		self,
		resource_id=none,
		protocol=none,
		endpoint=none,
		event_type=none,
		event_format=none):

		self.resource_id = resource_id
		self.protocol = protocol
		self.endpoint = endpoint
		self.event_type = event_type
		self.event_format = event_format

# endregion


class SubscriptionRequest:
    def __init__(self, subscription):
        self.subscription = subscription

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

