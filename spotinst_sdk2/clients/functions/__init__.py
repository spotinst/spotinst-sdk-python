import json

from spotinst_sdk2.client import Client
import spotinst_sdk2.models.functions as spotinst_functions


class FunctionsClient(Client):
    __base_functions_url = "/functions"

    # region Functions
    def create_application(self, app):
        """
        Create Spotinst Functions Application

        # Arguments
        app (ApplicationCreate): ApplicationCreate Object
        # Returns
        (Object): Functions API response 
        """
        app = spotinst_functions.ApplicationCreationRequest(app)

        excluded_group_dict = self.exclude_missing(json.loads(app.toJSON()))

        formatted_app_dict = self.convert_json(
            excluded_group_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_app_dict)

        self.print_output(body_json)

        app_response = self.send_post(
            body=body_json,
            url=self.__base_functions_url +
            '/application',
            entity_name='application')

        formatted_response = self.convert_json(
            app_response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def create_environment(self, env):
        """
        Create Spotinst Functions Environment

        # Arguments
        env (EnvironmentCreate): EnvironmentCreate Object
        # Returns
        (Object): Functions API response 
        """
        env = spotinst_functions.EnvironmentCreationRequest(env)

        excluded_env_dict = self.exclude_missing(json.loads(env.toJSON()))

        formatted_env_dict = self.convert_json(
            excluded_env_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_env_dict)

        self.print_output(body_json)

        env_response = self.send_post(
            body=body_json,
            url=self.__base_functions_url +
            '/environment',
            entity_name='environment')

        formatted_response = self.convert_json(
            env_response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    def create_function(self, fx):
        """
        Create Spotinst Functions

        # Arguments
        fx (FunctionCreate): FunctionCreate Object
        # Returns
        (Object): Functions API response 
        """
        fx = spotinst_functions.FunctionCreationRequest(
            fx, self.should_print_output)

        excluded_fx_dict = self.exclude_missing(json.loads(fx.toJSON()))

        formatted_fx_dict = self.convert_json(
            excluded_fx_dict, self.underscore_to_camel)

        body_json = json.dumps(formatted_fx_dict)

        formatted_fx_dict['function']['code']['source'] = 'INLINE_BASE64_SOURCE_CODE'
        self.print_output(json.dumps(formatted_fx_dict))

        fx_response = self.send_post(
            body=body_json,
            url=self.__base_functions_url +
            '/function',
            entity_name='function')

        formatted_response = self.convert_json(
            fx_response, self.camel_to_underscore)

        retVal = formatted_response["response"]["items"][0]

        return retVal

    # endregion
