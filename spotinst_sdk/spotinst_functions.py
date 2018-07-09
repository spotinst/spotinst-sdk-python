import base64
import json
import os
import tempfile
import zipfile
import logging
import argparse

none = "d3043820717d74d9a17694c176d39733"


# region Application
class Application:
    def __init__(self, name):
        self.name = name


# endregion

# region Environment
class Environment:
    def __init__(self, name, application_id, providers=none, locations=none):
        self.name = name
        self.application_id = application_id
        self.preferences = {'providers': providers, 'locations': locations}


# endregion

# region Environment
class Function:
    def __init__(
            self,
            name,
            environment_id,
            directory,
            handler,
            runtime,
            memory,
            timeout):
        self.name = name
        self.environment_id = environment_id
        self.directory = directory
        self.handler = handler
        self.runtime = runtime
        self.memory = memory
        self.timeout = timeout
        self.logger = self.init_logger()

    @staticmethod
    def init_logger():
        logger = logging.getLogger(__name__)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    @staticmethod
    def get_args():
        parser = argparse.ArgumentParser(description='Options for Spotinst python-sdk')
        parser.add_argument('--log-level',
                            choices=["debug", "info", "warn", "error", "critical"],
                            help='set log level: debug, info, warn, error, critical')
        args = parser.parse_args()
        return args

    def set_log_level(self, args):
        level = vars(args)['log_level']
        if level == "info":
            self.logger.setLevel(logging.INFO)
        if level == "debug":
            self.logger.setLevel(logging.DEBUG)
        if level == "warn":
            self.logger.setLevel(logging.WARN)
        if level == "error":
            self.logger.setLevel(logging.ERROR)
        if level == "critical":
            self.logger.setLevel(logging.CRITICAL)


# endregion


class ApplicationCreationRequest:
    def __init__(self, application):
        self.application = application

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class EnvironmentCreationRequest:
    def __init__(self, environment):
        self.environment = environment

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


class FunctionCreationRequest:
    def __init__(self, function):
        self.function = self.rebuildFunctionInlineCode(function)

    def rebuildFunctionInlineCode(self, function):
        directory = function.directory
        handler = function.handler

        with tempfile.NamedTemporaryFile() as temp:
            self.zip(directory, temp.name)

            temp.seek(0)
            base64content = base64.b64encode(temp.read())
            function.code = {'source': base64content, 'handler': handler}
            del function.directory
            del function.handler

        return function

    def zip(self, src, dst):
        zf = zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED)
        abs_src = os.path.abspath(src)
        for dirname, subdirs, files in os.walk(src):
            for filename in files:
                absname = os.path.abspath(os.path.join(dirname, filename))
                arcname = absname[len(abs_src) + 1:]
                self.logger.debug("collecting file {}".format(
                        os.path.join(
                            dirname, filename)))
                zf.write(absname, arcname)
        zf.close()

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
