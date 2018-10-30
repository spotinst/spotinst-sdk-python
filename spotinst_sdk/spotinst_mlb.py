import json

none = "d3043820717d74d9a17694c176d39733"

# region Balancer
class Balancer:
	"""
	# Arguments
	name: str
	timeouts: Timeout
	tags: List[Tag]
	"""
	def __init__(
		self,
		name=none,
		timeouts=none,
		tags=none):

		self.name = name
		self.timeouts = timeouts
		self.tags = tags

class Timeout:
	"""
	# Arguments
	draining: int
	idle: int
	"""
	def __init__(
		self,
		draining=none,
		idle=none):

		self.draining = draining
		self.idle = idle

class Tag:
	"""
	# Arguments
	key: str
	value: str
	"""
	def __init__(
		self,
		key=none,
		value=none):

		self.key = key
		self.value = value

class BalancerRequest:
    def __init__(self, balancer):
        self.balancer = balancer

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

# endregion



# region Target Set

class TargetSet:
	"""
	# Arguments
	name: str
	balancer_id: str
	deployment_id: str
	protocol: str
	weight: int
	config: Config
	integrations: Integrations
	health_check: HealthCheck
	tags: List[Tag]
	"""
	def __init__(
		self,
		name=none,
		balancer_id=none,
		deployment_id=none,
		protocol=none,
		weight=none,
		config=none,
		integrations=none,
		health_check=none,
		tags=none):

		self.name=name
		self.balancer_id=balancer_id
		self.deployment_id=deployment_id
		self.protocol=protocol
		self.weight=weight
		self.config=config
		self.integrations=integrations
		self.health_check=health_check
		self.tags=tags

class Config:
	"""
	# Argument
	rate_limiter: RateLimiter
	"""
	def __init__(
		self,
		rate_limiter=none):

		self.rate_limiter=rate_limiter

class RateLimiter:
	"""
	# Argument
	request_per_second: int
	"""
	def __init__(
		self,
		requests_per_second=none):

		self.requests_per_second=requests_per_second

class Integrations:
	"""
	# Arguments
	ecs: List[ECS]
	"""
	def __init__(
		self,
		ecs=none):

		self.ecs=ecs

class ECS:
	"""
	# Arguments
	target_group_arn: str
	target_group_name: str
	region: str
	service_name: str
	cluster_name: str
	"""
	def __init__(
		self,
		target_group_arn=none,
		target_group_name=none,
		region=none,
		service_name=none,
		cluster_name=none):

		self.target_group_arn=target_group_arn
		self.target_group_name=target_group_name
		self.region=region
		self.service_name=service_name
		self.cluster_name=cluster_name

class HealthCheck:
	"""
	# Arguments
	interval: int
	path: str
	port: int
	protocol: str
	timeout: int
	healthy_threshold_count: int
	unhealthy_threshold_count: int
	"""
	def __init__(
		self,
		interval=none,
		path=none,
		port=none,
		protocol=none,
		timeout=none,
		healthy_threshold_count=none,
		unhealthy_threshold_count=none):

		self.interval = interval
		self.path = path
		self.port = port
		self.protocol = protocol
		self.timeout = timeout
		self.healthy_threshold_count = healthy_threshold_count
		self.unhealthy_threshold_count = unhealthy_threshold_count

class TargetSetRequest:
    def __init__(self, target_set):
        self.target_set = target_set

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

# endregion




# region Target

class Target:
	"""
	# Arguments
	id: str (Deregister Target)
	balancer_id: (Create Target)
	target_set_id: (Create Target)
	name: str (Create & Register Target)
	host: str (Create & Register Target)
	port: int (Create Target)
	weight: int (Create & Register Target)
	tags: List[Tags] (Create & Register Target)
	"""
	def __init__(
		self,
		tags=none,
		name=none,
		id=none,
		balancer_id=none,
		port=none,
		target_set_id=none,
		host=none,
		weight=none):

		self.id=id
		self.balancer_id=balancer_id
		self.target_set_id=target_set_id
		self.name=name
		self.port=port
		self.host=host
		self.weight=weight
		self.tags=tags


class TargetsRequest:
    def __init__(self, targets):
        self.targets = targets

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

class TargetRequest:
    def __init__(self, target):
        self.target = target

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

# endregion




# region Middleware

class Middleware:
	"""
	# Arguments
	balancer_id: str
	type: str
	priority: int
	spec: Spec
	tags: List[Tag]
	"""
	def __init__(
		self,
		balancer_id=none,
		type=none,
		priority=none,
		spec=none,
		tags=none):

		self.balancer_id=balancer_id
		self.type=type
		self.priority=priority
		self.spec=spec
		self.tags=tags

class Spec:
	"""
	# Arguments
	action: str
	conditions: List[Condition]
	"""
	def __init__(
		self,
		action=none,
		conditions=none):

		self.action=action
		self.conditions=conditions


class Condition:
	"""
	# Arguments
	type: str
	values: List[str]
	"""
	def __init__(
		self,
		type=none,
		values=none):

		self.type=type
		self.values=values

class MiddlewareRequest:
    def __init__(self, middleware):
        self.middleware = middleware

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

# endregion




# region Listener

class Listener:
	"""
	# Arguments
	balancer_id: str
	protocol: str
	port: int
	tls_config: TLSConfig
	tags: List[Tag]
	"""
	def __init__(
		self,
		balancer_id=none,
		protocol=none,
		port=none,
		tls_config=none,
		tags=none):

		self.balancer_id=balancer_id
		self.protocol=protocol
		self.port=port
		self.tls_config=tls_config
		self.tags=tags

class TLSConfig:
	"""
	# Arguments
	min_version: str
	max_version: str
	session_ticket_disabled: bool
	prefer_service_cipher_suites: bool
	cipher_suites: List[str]
	insecure_skip_verify: bool
	certificate_ids: List[str]
	"""
	def __init__(
		self,
		min_version=none,
		max_version=none,
		session_tickets_disabled=none,
		prefer_server_cipher_suites=none,
		cipher_suites=none,
		insecure_skip_verify=none,
		certificate_ids=none):

		self.min_version=min_version
		self.max_version=max_version
		self.session_tickets_disabled=session_tickets_disabled
		self.prefer_server_cipher_suites=prefer_server_cipher_suites
		self.cipher_suites=cipher_suites
		self.insecure_skip_verify=insecure_skip_verify
		self.certificate_ids=certificate_ids


class ListenerRequest:
    def __init__(self, listener):
        self.listener = listener

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

# endregion




# region Routing Rule

class RoutingRule:
	"""
	# Arguments
	balancer_id: str
	route: str
	target_set_ids: List[str]
	middleware_ids: List[str]
	listener_id: str
	priority: int
	tags: List[Tag]
	"""
	def __init__(
		self,
		balancer_id=none,
		route=none,
		target_set_ids=none,
		middleware_ids=none,
		listener_id=none,
		priority=none,
		tags=none):

		self.balancer_id=balancer_id
		self.route=route
		self.target_set_ids=target_set_ids
		self.middleware_ids=middleware_ids
		self.listener_id=listener_id
		self.priority=priority
		self.tags=tags

class RoutingRuleRequest:
    def __init__(self, routing_rule):
        self.routing_rule = routing_rule

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)





