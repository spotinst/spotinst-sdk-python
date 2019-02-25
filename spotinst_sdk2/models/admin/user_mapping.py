import json

none = "d3043820717d74d9a17694c176d39733"

# region EMR
class UserMapping:
	"""
	# Arguments
	user_email: str
	account_id: str
	role: str
	"""
	def __init__(
		self,
		user_email=none,
		account_id=none,
		role=none):

		self.user_email = user_email
		self.account_id = account_id
		self.role = role


class UserMappingRequest:
    def __init__(self, mappings):
        self.mappings = mappings

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)



