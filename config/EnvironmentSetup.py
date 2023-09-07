import json
import os

from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn

folderWithEnvFiles = "C:/Coding/robotfwk/config/env_data"
LocalFilePath = os.path.join(folderWithEnvFiles,"LocalTestExecutionEnvironments.json")
RemoteFilePath = os.path.join(folderWithEnvFiles,"RemoteTestExecutionEnvironments.json")
QaEnvFilePath = os.path.join("QaTestExecutionEnvironment.json")

class EnvironmentSetup:
    ROBOT_LIBRARY_SCOPE = "GLOBAL"

    def __init__(self):
        self.load_arguments()
        self.__set_execution_location()
        self.__set_urls_and_endpoint_vars_from_json()
        self.__set_web_logins_from_json()

    def load_arguments(self):
        self.ENVIRONMENT = BuiltIn().get_variable_value("${ENVIRONMENT}")
        self.LOCAL = BuiltIn().get_variable_value("${LOCAL}")
        self.REMOTE = BuiltIn().get_variable_value("${REMOTE}")
        self.DEBUG = BuiltIn().get_variable_value("${DEBUG}")
        self.BROWSER = BuiltIn().get_variable_value("${BROWSER}")
        self.APIVERSION = BuiltIn().get_variable_value("${APIVERSION}")
        self.QAPORTAL = BuiltIn().get_variable_value("${QAPORTAL}")

    def __set_execution_location(self):
        try:
            if self.REMOTE == "True" and self.LOCAL == "False":
                newPath = self.__create_json_path(RemoteFilePath)
            elif self.QAPORTAL == "True":
                newPath = self.__create_json_path(QaEnvFilePath)
            else:
                newPath = self.__create_json_path(LocalFilePath)
        except IOError as error:
            logger.console("Can't load JSON config file")
            logger.console(error)
    
        logger.console("JSON config filepath set to: " + newPath)
        self.__loaded_environment_list = self.load_json_data(newPath)

    def __create_json_path(self, relativeFilePath):
        relativeFilePath = os.path.normpath(relativeFilePath)
        createdjsonPath = os.path.join(os.getcwd(), relativeFilePath)

        logger.console("Path to file: " + createdjsonPath)
        BuiltIn().log("Path to file: " + createdjsonPath, html=True)
        return createdjsonPath
    
    def load_json_data(self, jsonFilePath):
        logger.console("Load JSON data file: " + jsonFilePath)
        BuiltIn().log("Load JSON data file: " + jsonFilePath, html=True)

        with open(jsonFilePath) as json_file:
            fileCont = json.load(json_file)

            return fileCont
        
    def get_environment_specific_json(self):
        isEnvFound = False
        try:
            # based on the argument file get environment variables
            for env in self.__loaded_environment_list["environments"]:
                if self.ENVIRONMENT == env["environment"]:
                    self.__envVal = env
                    isEnvFound = True
                    return env
                
        except AssertionError as error:
            logger.console(error)

        if not isEnvFound:
            raise Exception(self.ENVIRONMENT + " Not available in the JSON config file")
    
    def __set_urls_and_endpoint_vars_from_json(self):
        try:
            env = self.get_environment_specific_json()
            self.PAGE_URL = env["urls"]["page_url"]
            self.PAGE_NAME = env["urls"]["page_name"]
            self.BROWSER_TIMEOUT = env["browser_settings"]["browser_timeout"]
            self.PLAYWRIGHT_DEBUG = env["browser_settings"]["playwright_debug"]
            self.HEADLESS = env["browser_settings"]["headless"]

        except AssertionError as error:
            logger.console(error)

    def __set_web_logins_from_json(self):
        try:
            env = self.get_environment_specific_json()
            self.LOGIN_EMAIL = env["web_logins"]["login_email"]
            self.LOGIN_PASSWORD = env["web_logins"]["login_password"]

        except AssertionError as error:
            logger.console(error)

    def read_json_file(self, relativePathToFile):
        path = self.__create_json_path(relativePathToFile)
        self.DataValues = self.load_json_data(path)
        return self.DataValues
        