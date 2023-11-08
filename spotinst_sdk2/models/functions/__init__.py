import base64
import json
import os
import tempfile
import zipfile
import logging

none = "d3043820717d74d9a17694c176d39733"
logger = logging.getLogger(__name__)


# region Application
class Application:
    """
    # Arguments
    name: str
    """

    def __init__(self, name):
        self.name = name


# endregion

# region Environment
class Environment:
    """
    # Arguments
    name: str
    application_id: str
    providers: List[str]
    locations: List[str]
    """

    def __init__(self, name, application_id, providers=none, locations=none):
        self.name = name
        self.application_id = application_id
        self.preferences = {'providers': providers, 'locations': locations}


# endregion

# region Environment
class Function:
    """
    # Arguments
    name: str
    environment_id: str
    directory: str
    runtime: int
    memory: int
    timeout: int
    """

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
    def __init__(self, function, print_output=True):
        self.should_print_output = print_output
        self.function = self.rebuildFunctionInlineCode(function)

    def print_output(self, output, level="debug"):
        if self.should_print_output is True:
            if level == "debug":
                logger.debug(output)
            if level == "info":
                logger.info(output)
            if level == "warn":
                logger.warn(output)
            if level == "error":
                logger.error(output)
            if level == "critical":
                logger.critical(output)

    def rebuildFunctionInlineCode(self, function, ):
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
        self.print_output("info level", "info")
        zf = zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED)
        abs_src = os.path.abspath(src)
        for dirname, subdirs, files in os.walk(src):
            for filename in files:
                absname = os.path.abspath(os.path.join(dirname, filename))
                arcname = absname[len(abs_src) + 1:]

                self.print_output("collecting file {}".format(
                    os.path.join(
                        dirname, filename)))
                zf.write(absname, arcname)
        zf.close()

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
