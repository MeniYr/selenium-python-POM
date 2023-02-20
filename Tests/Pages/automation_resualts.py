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
        """
        Name: meni rotblat\n
        Description: collect input result from element first name and send vals\n
        Date: 21.2.23\n
        :param kyes:
        """
        try:
            input = self.driver.find_element(*PersonalDetailsLocator.check_fname)
            return input.get_attribute("value")
        except Exception as e:
            self.log.send(e=self.config["TEST_FAIL"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def lname(self):
        """
        Name: meni rotblat\n
        Description: collect input result from element last name and send vals\n
        :param kyes: \n
        Date: 21.2.23\n
        """
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
        """
        Name: meni rotblat\n
        Description: collect result from downdrop element of city and send pick city val\n
        :param city: \n
        Date: 21.2.23\n
        """
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
        """
        Name: meni rotblat\n
        Description: collect result from input element of email and send it val\n
        :param Email: \n
        Date: 21.2.23\n
        """
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
        """
        Name: meni rotblat\n
        Description: collect result value select element of areaCode and pick from it val\n
        :param areaCode: \n
        Date: 21.2.23\n
        """
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
        """
        Name: meni rotblat\n
        Description: collect input value element of phone number and put on it val\n
        :param Phone:\n
        Date: 21.2.23\n
        """
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
        """
        Name: meni rotblat\n
        Description: collect checkbox result input Female element and checking it\n
        Date: 21.2.23\n
        """
        try:
            checkbox = self.driver.find_element(*PersonalDetailsLocator.check_checkbox_Female)
            return checkbox.is_selected()
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send( e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def checkbox_Male(self):
        """
        Name: meni rotblat\n
        Description: collect checkbox result input Male element and checking it\n
        Date: 21.2.23\n
        """
        try:
            checkbox = self.driver.find_element(*PersonalDetailsLocator.check_checkbox_Male)
            return checkbox.is_selected()
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send(e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def checkbox_Other(self):
        """
        Name: meni rotblat\n
        Description: collect checkbox result Other Male element and checking it\n
        Date: 21.2.23\n
        """
        try:
            checkbox = self.driver.find_element(*PersonalDetailsLocator.check_checkbox_Other)
            return checkbox.is_selected()
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send(e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def checkbox_Math(self):
        """
        Name: meni rotblat\n
        Description: collect checkbox result Math Male element and checking it\n
        Date: 21.2.23\n
        """
        try:
            checkbox = self.driver.find_element(*PersonalDetailsLocator.check_checkbox_Math)
            return checkbox.is_selected()
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send( e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def checkbox_Physics(self):
        """
        Name: meni rotblat\n
        Description: collect checkbox result Physics Male element and checking it\n
        Date: 21.2.23\n
        """
        try:
            checkbox = self.driver.find_element(*PersonalDetailsLocator.check_checkbox_Physics)
            return checkbox.is_selected()
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send(e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def checkbox_POP(self):
        """
        Name: meni rotblat\n
        Description: collect checkbox result POP element and checking it\n
        Date: 21.2.23\n
        """
        try:
            checkbox = self.driver.find_element(*PersonalDetailsLocator.check_checkbox_POP)
            return checkbox.is_selected()
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send( e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def checkbox_DUD(self):
        """
        Name: meni rotblat\n
        Description: collect checkbox result DUD element and checking it\n
        Date: 21.2.23\n
        """
        try:
            checkbox = self.driver.find_element(*PersonalDetailsLocator.check_checkbox_DUD)
            return checkbox.is_selected()
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send( e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def checkbox_Biology(self):
        """
        Name: meni rotblat\n
        Description: collect checkbox result Biology element and checking it\n
        Date: 21.2.23\n
        """
        try:
            checkbox = self.driver.find_element(*PersonalDetailsLocator.check_checkbox_Biology)
            return checkbox.is_selected()
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send(e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def checkbox_Chemistry(self):
        """
        Name: meni rotblat\n
        Description: collect checkbox result Chemistry element and checking it\n
        Date: 21.2.23\n
        """
        try:
            checkbox = self.driver.find_element(*PersonalDetailsLocator.check_checkbox_Chemistry)
            return checkbox.is_selected()
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send(e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def checkbox_English(self):
        """
        Name: meni rotblat\n
        Description: collect checkbox result English element and checking it\n
        Date: 21.2.23\n
        """
        try:
            checkbox = self.driver.find_element(*PersonalDetailsLocator.check_checkbox_English)
            return checkbox.is_selected()
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send(e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))
    #  js buttons

    def stext(self, val):
        """
        Name: meni rotblat\n
        Description: collect results of text area element and return text\n
        Date: 21.2.23\n
        """
        try:
            arialabel = self.driver.find_element(*PersonalDetailsLocator.check_stext_res)
            return arialabel.text
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send(e=self.config["GENERAL_ERR"].format("Exception_test_general", val, e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def loading(self, val):
        """
        Name: meni rotblat\n
        Description: collect results text area element and retrurn it\n
        Date: 21.2.23\n
        """
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

