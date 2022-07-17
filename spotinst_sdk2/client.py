import json
import os
import re

import requests
import yaml
import logging

VAR_SPOTINST_LOG_LEVEL = 'SPOTINST_LOG_LEVEL'

version = {}
with open(os.path.join(os.path.dirname(__file__), "./version.py")) as fp:
    exec(fp.read(), version)

_SpotinstClient__spotinst_sdk_python_agent_name = 'spotinst-sdk-python'
_SpotinstClient__spotinst_sdk_user_agent = '{}/{}'.format(
    _SpotinstClient__spotinst_sdk_python_agent_name, version['__version__'])

class Client:
    camel_pat = re.compile(r'([A-Z])')
    under_pat = re.compile(r'_([a-z])')
    
    __account_id_key = "accountId"


    def __init__(self, session=None,
                 print_output=True,
                 log_level=None,
                 user_agent=None,
                 timeout=None):

        self.auth_token = session.auth_token
        self.account_id = session.account_id

        self.should_print_output = print_output
        self.user_agent = user_agent

        # initialize logger
        self.logger = self.init_logger()
        self.set_log_level(log_level=log_level)

        self.timeout = timeout

    # region Utils
    def print_output(self, output):
        if self.should_print_output is True:
            print(output)

    def send_get(self, url,entity_name,query_params=None):
        agent = self.resolve_user_agent()

        if query_params != None:
            query_params = self.build_query_params_with_input(query_params)
        else:
            query_params = self.build_query_params()

        headers = dict(
            {
                'User-Agent': agent,
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + self.auth_token
            }
        )

        self.print_output("Sending get request to spotinst API.")
        result = requests.get(url, params=query_params, headers=headers, timeout=self.timeout)

        if result.status_code == requests.codes.ok:
            self.print_output("Success")
            data = json.loads(result.content.decode('utf-8'))
            return data
        else:
            self.handle_exception("getting {}".format(entity_name), result)

    def send_delete(self, url, entity_name):
        agent = self.resolve_user_agent()
        query_params = self.build_query_params()
        headers = dict(
            {
                'User-Agent': agent,
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + self.auth_token
            }
        )

        self.print_output("Sending deletion request to spotinst API.")

        result = requests.delete(url, params=query_params, headers=headers, timeout=self.timeout)

        if result.status_code == requests.codes.ok:
            self.print_output("Success")
            return True
        else:
            self.handle_exception("deleting {}".format(entity_name), result)

    def send_delete_with_body(self, body, url, entity_name):
        agent = self.resolve_user_agent()
        query_params = self.build_query_params()
        headers = dict(
            {
                'User-Agent': agent,
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + self.auth_token
            }
        )

        self.print_output("Sending deletion request to spotinst API.")

        result = requests.delete(
            url,
            params=query_params,
            headers=headers,
            data=body,
            timeout=self.timeout)

        if result.status_code == requests.codes.ok:
            self.print_output("Success")
            return True
        else:
            self.handle_exception("deleting {}".format(entity_name), result)

    def send_post(self, url, entity_name, body=None, query_params=None):
        agent = self.resolve_user_agent()

        if query_params != None:
            query_params = self.build_query_params_with_input(query_params)
        else:
            query_params = self.build_query_params()
        
        headers = dict(
            {
                'User-Agent': agent,
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + self.auth_token
            }
        )

        self.print_output("Sending post request to spotinst API.")

        result = requests.post(
            url,
            params=query_params,
            data=body,
            headers=headers,
            timeout=self.timeout)

        if result.status_code == requests.codes.ok:
            self.print_output("Success")
            data = json.loads(result.content.decode('utf-8'))
            return data
        else:
            self.handle_exception("creating {}".format(entity_name), result)

    def send_put(self, url, entity_name, query_params=None, body=None):
        agent = self.resolve_user_agent()
        
        if query_params != None:
            query_params = self.build_query_params_with_input(query_params)
        else:
            query_params = self.build_query_params()

        headers = dict(
            {
                'User-Agent': agent,
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + self.auth_token
            }
        )

        self.print_output("Sending put request to spotinst API.")
        result = requests.put(
            url,
            params=query_params,
            data=body,
            headers=headers,
            timeout=self.timeout)

        if result.status_code == requests.codes.ok:
            self.print_output("Success")
            data = json.loads(result.content.decode('utf-8'))
            return data
        else:
            self.handle_exception("updating {}".format(entity_name), result)

    def send_put_with_params(self, body, url, entity_name, user_query_params):
        agent = self.resolve_user_agent()
        query_params = self.build_query_params_with_input(user_query_params)

        headers = dict(
            {
                'User-Agent': agent,
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + self.auth_token
            }
        )

        self.print_output("Sending put request to spotinst API.")

        result = requests.put(
            url,
            params=query_params,
            data=body,
            headers=headers,
            timeout=self.timeout)

        if result.status_code == requests.codes.ok:
            self.print_output("Success")
            data = json.loads(result.content.decode('utf-8'))
            return data
        else:
            self.handle_exception("updating {}".format(entity_name), result)

    def resolve_user_agent(self):
        global _SpotinstClient__spotinst_sdk_user_agent
        agent = _SpotinstClient__spotinst_sdk_user_agent
        if self.user_agent is not None:
            agent = '{}+{}'.format(self.user_agent, agent)
        return agent

    def handle_exception(self, action_string, result):
        self.print_output(result.status_code)

        if result.content  == "Bad Request":
            data = dict(response=result.content)
        else:
            data = json.loads(result.content.decode('utf-8'))

        response_json = json.dumps(data["response"])
        self.print_output(response_json)

        raise SpotinstClientException(
            "Error encountered while " +
            action_string,
            response_json)

    def convert_json(self, val, convert):
        new_json = {}
        if val is None:
            return val
        elif type(val) in (int, float, bool, "".__class__, u"".__class__):
            return val

        for k, v in list(val.items()):
            new_v = v
            if isinstance(v, dict):
                new_v = self.convert_json(v, convert)
            elif isinstance(v, list):
                new_v = list()
                for x in v:
                    new_v.append(self.convert_json(x, convert))
            new_json[convert(k)] = new_v
        return new_json

    def convert_json_with_list_of_lists(self, val, convert):
        new_json = {}
        if val is None:
            return val
        elif type(val) in (int, float, bool, "".__class__, u"".__class__):
            return val

        if isinstance(val, list):
            new_v = list()
            for x in val:
                new_v.append(self.convert_json_with_list_of_lists(x, convert))
            return new_v
        else:
            for k, v in list(val.items()):
                new_v = v
                if isinstance(v, dict):
                    new_v = self.convert_json_with_list_of_lists(v, convert)
                elif isinstance(v, list):
                    new_v = list()
                    for x in v:
                        new_v.append(self.convert_json_with_list_of_lists(x, convert))
                new_json[convert(k)] = new_v
        return new_json

    def exclude_missing(self, obj):
        # Delete keys with the value 'none' in a dictionary, recursively.

        # if obj.items() is not None:
        if obj.items() is not None:
            for key, value in list(obj.items()):

                # Remove none values
                if value == "d3043820717d74d9a17694c176d39733":
                    del obj[key]

                # Handle Objects
                elif isinstance(value, dict):
                    self.exclude_missing(obj=value)

                # Handle lists
                elif self.is_sequence(arg=value):
                    for listitem in value:
                        # Handle Lists of objects
                        try:
                            self.exclude_missing(obj=listitem)
                        except AttributeError:
                            pass
        return obj  # For convenience

    def is_sequence(self, arg):
        return (not hasattr(arg, "strip") and
                hasattr(arg, "__getitem__") or
                hasattr(arg, "__iter__"))

    def build_query_params(self):
        query_params = None
        if self.account_id is not None:
            query_params = dict({self.__account_id_key: self.account_id})

        return query_params

    def build_query_params_with_input(self, user_params):
        query_params = dict()
        if self.account_id is not None:
            query_params = dict({self.__account_id_key: self.account_id})

        if user_params is not None:
            query_params = self.merge_two_dicts(query_params, user_params)

        return query_params

    def print_output(self, output, level="debug"):
        if self.should_print_output is True:
            if level == "debug":
                self.logger.debug(output)
            if level == "info":
                self.logger.info(output)
            if level == "warn":
                self.logger.warn(output)
            if level == "error":
                self.logger.error(output)
            if level == "critical":
                self.logger.critical(output)

    @staticmethod
    def init_logger():
        logging.basicConfig(level=logging.CRITICAL)
        logger = logging.getLogger(__name__)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    def set_log_level(self, log_level):
        if log_level==None:
            level = os.environ.get(VAR_SPOTINST_LOG_LEVEL, 'critical')
        else:
            level = log_level

        if level == "debug":
            self.logger.setLevel(logging.DEBUG)
        if level == "info":
            self.logger.setLevel(logging.INFO)
        if level == "warn":
            self.logger.setLevel(logging.WARN)
        if level == "error":
            self.logger.setLevel(logging.ERROR)
        if level == "critical":
            self.logger.setLevel(logging.CRITICAL)

    @staticmethod
    def merge_two_dicts(x, y):
        z = x.copy()  # start with x's keys and values
        z.update(y)  # modifies z with y's keys and values & returns None
        return z

    def camel_to_underscore(self, name):
        return self.camel_pat.sub(lambda x: '_' + x.group(1).lower(), name)

    def underscore_to_camel(self, name):
        return self.under_pat.sub(lambda x: x.group(1).upper(), name)

class SpotinstClientException(Exception):
    def __init__(self, message, response):
        self.message = message + "\n" + response
        # Call the base class constructor with the parameters it needs
        super(SpotinstClientException, self).__init__(message)
    # endregion