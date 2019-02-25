import json

from spotinst_sdk2.client import Client
import spotinst_sdk2.models.mlb as spotinst_mlb

class MlbClient(Client):
    __base_lb_url = "https://api.spotinst.io/loadBalancer"

    # region MLB
    def get_all_mlb_runtime(self):
        """
        Get all MLB runtime 
        
        # Returns
        (Object): Spotinst API response 
        """ 
        response = self.send_get(
            url=self.__base_lb_url +
            "/runtime",
            entity_name="mlb runtime"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"]

        return retVal     

    def get_mlb_runtime(self, runtime_id):
        """
        Get MLB runtime
        
        # Arguments
        runtime_id (String): Runtime id name
        
        # Returns
        (Object): Spotinst API response 
        """ 
        response = self.send_get(
            url=self.__base_lb_url +
            "/runtime/" + runtime_id,
            entity_name="mlb runtime"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal     

    def deregister_mlb_runtime(self, runtime_id):
        """
        Deregister MLB runtime
        
        # Arguments
        runtime_id (String): Runtime id name
        
        # Returns
        (Object): Spotinst API response 
        """ 
        response = self.send_put(
            url=self.__base_lb_url +
            "/runtime/" + runtime_id +
            "/deregister",
            entity_name="mlb runtime"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["status"]

        return retVal   

    def delete_mlb_runtime(self, runtime_id):
        """
        Delete MLB runtime
        
        # Arguments
        runtime_id (String): Runtime id name
        
        # Returns
        (Object): Spotinst API response 
        """ 
        response = self.send_delete(
            url=self.__base_lb_url +
            "/runtime/" + runtime_id,
            entity_name="mlb runtime"
        )

        return response 

    def create_mlb_deployment(self, deployment_name):
        """
        Create MLB deployment
        
        # Arguments
        deployment_name (String): Deployment name
        
        # Returns
        (Object): Spotinst API response 
        """ 
        response = self.send_post(
            url=self.__base_lb_url +
            "/deployment",
            body=json.dumps(dict(deployment=dict(name=deployment_name))),
            entity_name="mlb deployment"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal 

    def update_mlb_deployment(self, deployment_id, deployment_name):
        """
        Update MLB deployment
        
        # Arguments
        deployment_name (String): Deployment name
        deployment_id (String): Deployment Id
        
        # Returns
        (Object): Spotinst API response 
        """ 
        response = self.send_put(
            url=self.__base_lb_url +
            "/deployment/" + deployment_id,
            body=json.dumps(dict(deployment=dict(name=deployment_name))),
            entity_name="mlb deployment"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)
        retVal = formatted_response["response"]["status"]

        return retVal 

    def get_mlb_deployment(self, deployment_id):
        """
        Get MLB deployment
        
        # Arguments
        deployment_id (String): Deployment Id
        
        # Returns
        (Object): Spotinst API response 
        """ 
        response = self.send_get(
            url=self.__base_lb_url +
            "/deployment/"+deployment_id,
            entity_name="mlb deployment"
        )
        
        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal 

    def get_all_mlb_deployment(self):
        """
        Get All MLB deployment
        
        # Returns
        (Object): Spotinst API response 
        """ 
        response = self.send_get(
            url=self.__base_lb_url +
            "/deployment",
            entity_name="mlb deployment"
        )
        
        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"]

        return retVal 

    def delete_mlb_deployment(self, deployment_id):
        """
        Delete MLB deployment
        
        # Arguments
        deployment_id (String): Deployment Id
        
        # Returns
        (Object): Spotinst API response 
        """ 
        response = self.send_delete(
            url=self.__base_lb_url +
            "/deployment/"+deployment_id,
            entity_name="mlb deployment"
        )

        return response

    def create_mlb_balancer(self, balancer):
        """
        Create MLB balancer
        
        # Arguments
        balancer (Balancer): Balancer Object
        
        # Returns
        (Object): Spotinst API response 
        """ 
        balancer = spotinst_mlb.BalancerRequest(balancer)

        excluded_group_dict = self.exclude_missing(json.loads(balancer.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        self.print_output(body_json)

        response = self.send_post(
            url=self.__base_lb_url +
            "/balancer",
            body=body_json,
            entity_name="mlb balancer"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal        

    def update_mlb_balancer(self, balancer_id, balancer):
        """
        Create MLB balancer
        
        # Arguments
        balancer_id (String): Balancer Id
        balancer (Balancer): Balancer Object
        
        # Returns
        (Object): Spotinst API response 
        """ 
        balancer = spotinst_mlb.BalancerRequest(balancer)

        excluded_group_dict = self.exclude_missing(json.loads(balancer.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        self.print_output(body_json)

        response = self.send_put(
            url=self.__base_lb_url +
            "/balancer/" + balancer_id,
            body=body_json,
            entity_name="mlb balancer"
        )
        
        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["status"]

        return retVal 

    def get_mlb_balancer(self, balancer_id):
        """
        Get MLB balancer
        
        # Arguments
        balancer_id (String): Balancer Id
        
        # Returns
        (Object): Spotinst API response 
        """
        response = self.send_get(
            url=self.__base_lb_url +
            "/balancer/" + balancer_id,
            entity_name="mlb balancer" 
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal        

    def get_all_mlb_balancer(self):
        """
        Get All MLB balancer
        
        # Returns
        (Object): Spotinst API response 
        """
        response = self.send_get(
            url=self.__base_lb_url +
            "/balancer/",
            entity_name="mlb balancer" 
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"]

        return retVal   

    def delete_mlb_balancer(self, balancer_id):
        """
        Delete MLB balancer
        
        # Arguments
        balancer_id (String): Balancer Id
        
        # Returns
        (Object): Spotinst API response 
        """
        response = self.send_delete(
            url=self.__base_lb_url +
            "/balancer/" + balancer_id,
            entity_name="mlb balancer" 
        )

        return response   

    def create_mlb_target_set(self, target_set):
        """
        Create MLB target set
        
        # Arguments
        target_set (TargetSet): TargetSet Object
        
        # Returns
        (Object): Spotinst API response 
        """
        target_set = spotinst_mlb.TargetSetRequest(target_set)

        excluded_group_dict = self.exclude_missing(json.loads(target_set.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        self.print_output(body_json)

        response = self.send_post(
            url=self.__base_lb_url +
            "/targetSet",
            body=body_json,
            entity_name="mlb target set"
        )
        
        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal 

    def update_mlb_target_set(self, target_set_id, target_set):
        """
        Update MLB target set
        
        # Arguments
        target_set_id (String): Target Set Id
        target_set (TargetSet): TargetSet Object
        
        # Returns
        (Object): Spotinst API response 
        """
        target_set = spotinst_mlb.TargetSetRequest(target_set)

        excluded_group_dict = self.exclude_missing(json.loads(target_set.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        self.print_output(body_json)

        response = self.send_put(
            url=self.__base_lb_url +
            "/targetSet" + target_set_id,
            body=body_json,
            entity_name="mlb target set"
        )
        
        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["status"]

        return retVal 

    def get_mlb_target_set(self, target_set_id):
        """
        Gat an MLB target set
        
        # Arguments
        target_set_id (String): Target Set Id
        
        # Returns
        (Object): Spotinst API response 
        """
        response = self.send_get(
            url=self.__base_lb_url +
            "/targetSet/" + target_set_id,
            entity_name="mlb target set"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal 

    def get_all_mlb_target_set(self):
        """
        Get all MLB target sets
        
        # Returns
        (Object): Spotinst API response 
        """
        response = self.send_get(
            url=self.__base_lb_url +
            "/targetSet",
            entity_name="mlb target set"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"]

        return retVal 

    def delete_mlb_target_set(self, target_set_id):
        """
        Delete an MLB target set
        
        # Arguments
        target_set_id (String): Target Set Id
        
        # Returns
        (Object): Spotinst API response 
        """
        response = self.send_delete(
            url=self.__base_lb_url +
            "/targetSet/" + target_set_id,
            entity_name="mlb target set"
        )

        return response 

    def register_mlb_targets(self, target_set_id, targets):
        """
        Register MLB targets
        
        # Arguments
        target_set_id (String): Target Set Id
        Targets (List[Target]): List of Target Objects
        
        # Returns
        (Object): Spotinst API response 
        """
        targets = spotinst_mlb.TargetsRequest(targets)

        excluded_group_dict = self.exclude_missing(json.loads(targets.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        self.print_output(body_json)

        response = self.send_put(
            url=self.__base_lb_url +
            "/targetSet/" + target_set_id +
            "/registerTargets",
            body=body_json,
            entity_name="mlb target set"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"]

        return retVal 

    def deregister_mlb_targets(self, target_set_id, targets):
        """
        Deregister MLB targets
        
        # Arguments
        target_set_id (String): Target Set Id
        Targets (List[Target]): List of Target Objects
        
        # Returns
        (Object): Spotinst API response 
        """
        targets = spotinst_mlb.TargetsRequest(targets)

        excluded_group_dict = self.exclude_missing(json.loads(targets.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        self.print_output(body_json)

        response = self.send_put(
            url=self.__base_lb_url +
            "/targetSet/" + target_set_id +
            "/deregisterTargets",
            body=body_json,
            entity_name="mlb target set"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["status"]

        return retVal 

    def create_mlb_target(self, target):
        """
        Create MLB target
        
        # Arguments
        target (Target): Target Object
        
        # Returns
        (Object): Spotinst API response 
        """
        target = spotinst_mlb.TargetRequest(target)

        excluded_group_dict = self.exclude_missing(json.loads(target.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        self.print_output(body_json)

        response = self.send_post(
            url=self.__base_lb_url +
            "/target",
            body=body_json,
            entity_name="mlb target"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal 

    def update_mlb_target(self, target_id, target):
        """
        Update MLB target
        
        # Arguments
        target_id (String): Target Id
        target (Target): Target Object
        
        # Returns
        (Object): Spotinst API response 
        """
        target = spotinst_mlb.TargetRequest(target)

        excluded_group_dict = self.exclude_missing(json.loads(target.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        self.print_output(body_json)

        response = self.send_put(
            url=self.__base_lb_url +
            "/target/"+target_id,
            body=body_json,
            entity_name="mlb target"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["status"]

        return retVal 

    def get_mlb_target(self, target_id):
        """
        Get MLB target
        
        # Arguments
        target_id (String): Target Id
        
        # Returns
        (Object): Spotinst API response 
        """
        response = self.send_get(
            url=self.__base_lb_url +
            "/target/"+target_id,
            entity_name="mlb target"            
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal 

    def get_all_mlb_target(self):
        """
        Get all MLB target
        
        # Returns
        (Object): Spotinst API response 
        """
        response = self.send_get(
            url=self.__base_lb_url +
            "/target",
            entity_name="mlb target"            
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"]

        return retVal 

    def delete_mlb_target(self, target_id):
        """
        Delete MLB target
        
        # Arguments
        target_id (String): Target Id
        
        # Returns
        (Object): Spotinst API response 
        """
        response = self.send_delete(
            url=self.__base_lb_url +
            "/target/"+target_id,
            entity_name="mlb target"            
        )

        return response 

    def create_mlb_listener(self, listener):
        """
        Create MLB listener
        
        # Arguments
        listener (Listener): Listener Object
        
        # Returns
        (Object): Spotinst API response 
        """
        listener = spotinst_mlb.ListenerRequest(listener)

        excluded_group_dict = self.exclude_missing(json.loads(listener.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        self.print_output(body_json)

        response = self.send_post(
            url=self.__base_lb_url +
            "/listener",
            body=body_json,
            entity_name="mlb listener"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal 

    def update_mlb_listener(self, listener_id, listener):
        """
        Update MLB listener
        
        # Arguments
        listener_id (String): Listener ID
        listener (Listener): Listener Object
        
        # Returns
        (Object): Spotinst API response 
        """
        listener = spotinst_mlb.ListenerRequest(listener)

        excluded_group_dict = self.exclude_missing(json.loads(listener.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        self.print_output(body_json)

        response = self.send_put(
            url=self.__base_lb_url +
            "/listener/" + listener_id,
            body=body_json,
            entity_name="mlb listener"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["status"]

        return retVal 

    def get_mlb_listener(self, listener_id):
        """
        Get MLB listener
        
        # Arguments
        listener_id (String): Listener ID
        
        # Returns
        (Object): Spotinst API response 
        """
        response = self.send_get(
            url=self.__base_lb_url +
            "/listener/"+listener_id,
            entity_name="mlb listener"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal 

    def get_all_mlb_listener(self):
        """
        Get all MLB listeners
        
        # Returns
        (Object): Spotinst API response 
        """
        response = self.send_get(
            url=self.__base_lb_url +
            "/listener",
            entity_name="mlb listener"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"]

        return retVal 

    def delete_mlb_listener(self, listener_id):
        """
        Delete MLB listener
        
        # Arguments
        listener_id (String): Listener ID
        
        # Returns
        (Object): Spotinst API response 
        """
        response = self.send_delete(
            url=self.__base_lb_url +
            "/listener/"+listener_id,
            entity_name="mlb listener"
        )

        return response 

    def create_mlb_routing_rule(self, routing_rule):
        """
        Create MLB routing rule
        
        # Arguments
        routing_rule (RoutingRule): RoutingRule Object
        
        # Returns
        (Object): Spotinst API response 
        """
        routing_rule = spotinst_mlb.RoutingRuleRequest(routing_rule)

        excluded_group_dict = self.exclude_missing(json.loads(routing_rule.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        self.print_output(body_json)

        response = self.send_post(
            url=self.__base_lb_url +
            "/routingRule",
            body=body_json,
            entity_name="mlb routing rule"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal 

    def update_mlb_routing_rule(self, routing_rule_id, routing_rule):
        """
        Update MLB routing rule
        
        # Arguments
        routing_rule_id (String): Routing Rule Id
        routing_rule (RoutingRule): RoutingRule Object
        
        # Returns
        (Object): Spotinst API response 
        """
        routing_rule = spotinst_mlb.RoutingRuleRequest(routing_rule)

        excluded_group_dict = self.exclude_missing(json.loads(routing_rule.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        self.print_output(body_json)

        response = self.send_put(
            url=self.__base_lb_url +
            "/routingRule/" + routing_rule_id,
            body=body_json,
            entity_name="mlb routing rule"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["status"]

        return retVal 

    def get_mlb_routing_rule(self, routing_rule_id):
        """
        Get MLB routing rule
        
        # Arguments
        routing_rule_id (String): Routing Rule Id
        
        # Returns
        (Object): Spotinst API response 
        """
        response = self.send_get(
            url=self.__base_lb_url +
            "/routingRule/"+routing_rule_id,
            entity_name="mlb routing rule"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal 

    def get_all_mlb_routing_rule(self):
        """
        Get all MLB routing rule
        
        # Returns
        (Object): Spotinst API response 
        """
        response = self.send_get(
            url=self.__base_lb_url +
            "/routingRule",
            entity_name="mlb routing rule"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"]

        return retVal 

    def delete_mlb_routing_rule(self, routing_rule_id):
        """
        Delete MLB routing rule
        
        # Arguments
        routing_rule_id (String): Routing Rule Id
        
        # Returns
        (Object): Spotinst API response 
        """
        response = self.send_delete(
            url=self.__base_lb_url +
            "/routingRule/"+routing_rule_id,
            entity_name="mlb routing rule"
        )

        return response 

    def create_mlb_middleware(self, middleware):
        """
        Create MLB middleware
        
        # Arguments
        middleware (Middleware): Middleware Object
        
        # Returns
        (Object): Spotinst API response 
        """
        middleware = spotinst_mlb.MiddlewareRequest(middleware)

        excluded_group_dict = self.exclude_missing(json.loads(middleware.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        self.print_output(body_json)

        response = self.send_post(
            url=self.__base_lb_url +
            "/middleware",
            body=body_json,
            entity_name="mlb middleware"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal 

    def update_mlb_middleware(self, middleware_id, middleware):
        """
        Update MLB middleware
        
        # Arguments
        middleware_id (String): Middleware ID
        middleware (Middleware): Middleware Object
        
        # Returns
        (Object): Spotinst API response 
        """
        middleware = spotinst_mlb.MiddlewareRequest(middleware)

        excluded_group_dict = self.exclude_missing(json.loads(middleware.toJSON()))

        formatted_group_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_group_dict)

        self.print_output(body_json)

        response = self.send_put(
            url=self.__base_lb_url +
            "/middleware/" + middleware_id,
            body=body_json,
            entity_name="mlb middleware"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["status"]

        return retVal 

    def get_mlb_middleware(self, middleware_id):
        """
        Get MLB middleware
        
        # Arguments
        middleware_id (String): Middleware ID
        
        # Returns
        (Object): Spotinst API response 
        """
        response = self.send_get(
            url=self.__base_lb_url +
            "/middleware/"+middleware_id,
            entity_name="mlb middleware"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal 

    def get_all_mlb_middleware(self):
        """
        Get all MLB middleware
                
        # Returns
        (Object): Spotinst API response 
        """
        response = self.send_get(
            url=self.__base_lb_url +
            "/middleware",
            entity_name="mlb middleware"
        )

        formatted_response = self.convert_json(
            response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"]

        return retVal 

    def delete_mlb_middleware(self, middleware_id):
        """
        Delete MLB middleware
        
        # Arguments
        middleware_id (String): Middleware ID
        
        # Returns
        (Object): Spotinst API response 
        """
        response = self.send_delete(
            url=self.__base_lb_url +
            "/middleware/"+middleware_id,
            entity_name="mlb middleware"
        )

        return response 
    # endregion
