import time
import logging

import dotenv
import json
from ddt import file_data, ddt
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

# from selenium.webdriver.common.by import By

from Locators.locators import PersonalDetailsLocator
from Tests.Pages.base_page import BasePage
import pytest
import json
from Utills.exceptions_loging import Exceptions_logs


class AutomationPage(BasePage):

    def __init__(self, driver:WebDriver):
        self.driver = driver
        super().__init__(self.driver)
        self.config = dotenv.dotenv_values(
            dotenv_path=dotenv.find_dotenv("C:/Python/AutomationProject/Tests/.env"))
        self.data = json.load(open(self.config["DATA"]))
        self.img_name = self.config["IMG_LOCATION"]

#  personal details

    def fname(self, kyes):
        try:
            # print()
            input = self.driver.find_element(*PersonalDetailsLocator.check_fname)
            input.clear()
            input.send_keys(kyes)
            time.sleep(1)
        except Exception as e:
            Exceptions_logs.send(self, e=self.config["TEST_FAIL"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def lname(self, kyes):
            try:
                input = self.driver.find_element(*PersonalDetailsLocator.check_lname)
                input.clear()
                input.send_keys(kyes)
                time.sleep(1)
            except Exception as e:
                img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
                self.driver.save_screenshot(img_name)
                Exceptions_logs.send(self, e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                     pic_name=self.img_name.format(
                                         time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def city(self):
        try:
            pass
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            Exceptions_logs.send(self, e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))


    def email(self):
        try:
            pass
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            Exceptions_logs.send(self, e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))


    def sel(self):
        try:
            pass
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            Exceptions_logs.send(self, e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))


    def checkbox(self):
        try:
            pass
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            Exceptions_logs.send(self, e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))


    def buttons(self):
        try:
            pass
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            Exceptions_logs.send(self, e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))


#  js buttons

    def stext(self):
        try:
            pass
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            Exceptions_logs.send(self, e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))


    def loading(self, title):
        try:
            pass
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            Exceptions_logs.send(self, e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))


#  links

    def links(self):
        try:
            pass
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            Exceptions_logs.send(self, e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))
