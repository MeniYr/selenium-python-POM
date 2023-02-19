import time
import logging

import dotenv
import json
from ddt import file_data, ddt
from selenium import webdriver
from selenium.webdriver.common.by import By

# from selenium.webdriver.common.by import By
from Locators.locators import PersonalDetailsLocator
import pytest
import json

from Tests.Pages.automation import AutomationPage
from Tests.Pages.automation_resualts import AutomationResPage
from Utills.exceptions_loging import Exceptions_logs


# @ddt
@pytest.mark.usefixtures("setup")
class TestAutomation():
    @pytest.fixture(autouse=True)
    def setup_method(self):

        self.config = dotenv.dotenv_values(dotenv_path=dotenv.find_dotenv("C:/Python/AutomationProject/Tests/.env"))
        self.data = json.load(open(self.config["DATA"]))
        self.au = AutomationPage(self.driver)
        self.res = AutomationResPage(self.driver)

    # @pytest.mark.general
    def test_general_title(self):
        img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
        try:
            gettitle = self.au.check_title(self.data["data"]["general"]["title"])
            # print(*PersonalDetailsLocator.check_title)
            assert gettitle is True
            Exceptions_logs.send(self, e=self.config["TEST_PASS"].format("check_title", self.data["data"]["general"]["title"]), pic_name=None)

        except AssertionError as ae:
            self.driver.save_screenshot(filename=img_name)
            Exceptions_logs.send(self, e=self.config["ASSERT_FAIL"].format("AssertionError_test_general", "", ae),
                                 pic_name=img_name)
        except Exception as e:
            self.driver.save_screenshot(filename=img_name)
            Exceptions_logs.send(self, e=self.config["TEST_FAIL"].format("Exception_test_general", "", e),
                                 pic_name=img_name)
        finally:
            pass

#  personal details
    def test_personals_fname(self):
        img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
        try:
            for i in self.data["data"]["pesonal_details"]["firstName"]["trueVal"]:
                self.au.fname(i)
                assert self.res.fname() == i
            for i in self.data["data"]["pesonal_details"]["firstName"]["wrongValues"]:
                self.au.fname(i)
                assert self.res.fname() == ''
            Exceptions_logs.send(self, e=self.config["TEST_PASS"].format("test_personals_fname", self.data["data"]["pesonal_details"]["firstName"]["trueVal"]), pic_name=None)
        except Exception as e:
            self.driver.save_screenshot(filename=img_name)
            Exceptions_logs.send(self, e=self.config["TEST_FAIL"].format("test_personals_fname", self.data["data"]["pesonal_details"]["firstName"]["trueVal"], e),
                                 pic_name=img_name)
            assert False,e
        except AssertionError as ae:
            self.driver.save_screenshot(filename=img_name)
            Exceptions_logs.send(self, e=self.config["ASSERT_FAIL"].format("test_personals_fname",
                self.data["data"]["pesonal_details"]["firstName"]["trueVal"], ae),
                                 pic_name=img_name)
            assert False,ae

    def test_personals_lname(self):
        img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
        try:
            for i in self.data["data"]["pesonal_details"]["lastName"]["trueVal"]:
                self.au.lname(i)
                assert self.res.lname() == i
            for i in self.data["data"]["pesonal_details"]["lastName"]["wrongValues"]:
                self.au.lname(i)
                assert self.res.lname() == ''
            Exceptions_logs.send(self, e=self.config["TEST_PASS"].format("test_personals_fname", self.data["data"]["pesonal_details"]["lastName"]["trueVal"]), pic_name=None)
        except Exception as e:
            self.driver.save_screenshot(filename=img_name)
            Exceptions_logs.send(self, e=self.config["TEST_FAIL"].format("test_personals_lname", self.data["data"]["pesonal_details"]["lastName"]["trueVal"], e),
                                 pic_name=img_name)
            assert False,e
        except AssertionError as ae:
            self.driver.save_screenshot(filename=img_name)
            Exceptions_logs.send(self, e=self.config["ASSERT_FAIL"].format("test_personals_lname",
                self.data["data"]["pesonal_details"]["lastName"]["trueVal"], ae),
                                 pic_name=img_name)
            assert False,ae
#  js buttons

#  links