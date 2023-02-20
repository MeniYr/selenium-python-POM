import time
import logging
from selenium.webdriver.support import expected_conditions as ec
from selenium.common import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select as select

import dotenv
import json
from ddt import file_data, ddt
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# from selenium.webdriver.common.by import By

from Locators.locators import PersonalDetailsLocator
from Tests.Pages.base_page import BasePage
import pytest
import json
from Utills.exceptions_loging import Exceptions_logs


class AutomationResPage(BasePage):

    def __init__(self, driver: WebDriver, log):
        self.driver = driver
        super().__init__(self.driver)
        self.config = dotenv.dotenv_values(
            dotenv_path=dotenv.find_dotenv("C:/Python/AutomationProject/Tests/.env"))
        self.data = json.load(open(self.config["DATA"]))
        self.img_name = self.config["IMG_LOCATION"]
        self.log = log

    #  personal details

    def fname(self):
        try:
            input = self.driver.find_element(*PersonalDetailsLocator.check_fname)
            return input.get_attribute("value")
        except Exception as e:
            self.log.send(e=self.config["TEST_FAIL"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def lname(self):
        try:
            input = self.driver.find_element(*PersonalDetailsLocator.check_lname)
            return input.get_attribute("value")
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send(e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(
                                     time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def city(self, city):
        try:
            drop = self.driver.find_element(*PersonalDetailsLocator.check_city)
            dropdown = select(drop)
            time.sleep(1)
            # print(dropdown.first_selected_option.text)
            return dropdown.first_selected_option.text
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send(e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def email(self):
        try:
            email = self.driver.find_element(*PersonalDetailsLocator.check_email)
            # email.send_keys(Email)
            return email.get_attribute("value")
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send(e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def areaCode(self, areaCode):
        try:
            drop = self.driver.find_element(*PersonalDetailsLocator.check_areaCode)
            dropdown = select(drop)
            dropdown.select_by_visible_text(areaCode)
            return dropdown.first_selected_option.text
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send(e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def sel(self):
        try:
            phone = self.driver.find_element(*PersonalDetailsLocator.check_sel)
            return phone.get_attribute("value")
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send(e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))
        finally:
            pass

    # checkboxes
    def checkbox_Female(self):
        try:
            checkbox = self.driver.find_element(*PersonalDetailsLocator.check_checkbox_Female)
            return checkbox.is_selected()
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send( e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def checkbox_Male(self):
        try:
            checkbox = self.driver.find_element(*PersonalDetailsLocator.check_checkbox_Male)
            return checkbox.is_selected()
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send(e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def checkbox_Other(self):
        try:
            checkbox = self.driver.find_element(*PersonalDetailsLocator.check_checkbox_Other)
            return checkbox.is_selected()
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send(e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def checkbox_Math(self):
        try:
            checkbox = self.driver.find_element(*PersonalDetailsLocator.check_checkbox_Math)
            return checkbox.is_selected()
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send( e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def checkbox_Physics(self):
        try:
            checkbox = self.driver.find_element(*PersonalDetailsLocator.check_checkbox_Physics)
            return checkbox.is_selected()
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send(e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def checkbox_POP(self):
        try:
            checkbox = self.driver.find_element(*PersonalDetailsLocator.check_checkbox_POP)
            return checkbox.is_selected()
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send( e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def checkbox_DUD(self):
        try:
            checkbox = self.driver.find_element(*PersonalDetailsLocator.check_checkbox_DUD)
            return checkbox.is_selected()
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send( e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def checkbox_Biology(self):
        try:
            checkbox = self.driver.find_element(*PersonalDetailsLocator.check_checkbox_Biology)
            return checkbox.is_selected()
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send(e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def checkbox_Chemistry(self):
        try:
            checkbox = self.driver.find_element(*PersonalDetailsLocator.check_checkbox_Chemistry)
            return checkbox.is_selected()
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send(e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def checkbox_English(self):
        try:
            checkbox = self.driver.find_element(*PersonalDetailsLocator.check_checkbox_English)
            return checkbox.is_selected()
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send(e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def buttons(self):
        try:
            pass
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send(e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    #  js buttons

    def stext(self, val):
        try:
            arialabel = self.driver.find_element(*PersonalDetailsLocator.check_stext_res)
            return arialabel.text
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send(e=self.config["GENERAL_ERR"].format("Exception_test_general", val, e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def loading(self, val):
        try:
            wait = WebDriverWait(self.driver, timeout=15, poll_frequency=1,
                                 ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
            loading = wait.until(ec.text_to_be_present_in_element(PersonalDetailsLocator.check_loading_text, val))
            return loading
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send(e=self.config["GENERAL_ERR"].format("Exception_loading_res", val, e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))
            assert False

