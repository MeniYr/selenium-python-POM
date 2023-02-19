import dotenv
from selenium import webdriver

from Tests.testcases.test_automation import TestAutomation
from Utills.exceptions_loging import Exceptions_logs
import pytest


class TestProjectFinal:

    def setup_method(self):
        try:
            self.config = dotenv.dotenv_values(
                dotenv_path=dotenv.find_dotenv("C:/Python/AutomationProject/Tests/.env"))
        except Exception as e:
            print(" Test_project_final Exception: ", e)

    def run_tests(self):
        try:
            TestAutomation()
        except Exception as e:
            print("Test_project_final, test_aoutomation: =>  \n", e)
