import dotenv
from selenium import webdriver

from Tests.testcases.test_automation import TestAutomation
from Tests.testcases.test_next_page import TestNextPage
from Utills.exceptions_loging import Exceptions_logs
import pytest


class TestProjectFinal:
    @pytest.fixture()
    def setup_method(self):
        self.config = dotenv.dotenv_values(
            dotenv_path=dotenv.find_dotenv("C:/Python/AutomationProject/Tests/.env"))


    def run_tests(self):
        try:
            TestAutomation()
            TestNextPage()
        except Exception as e:
            print("Test_project_final, test_aoutomation: =>  \n", e)
