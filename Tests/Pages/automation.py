import time
import logging

import dotenv
import json
from ddt import file_data, ddt
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select as select
from selenium.webdriver.common.alert import Alert

# from selenium.webdriver.common.by import By

from Locators.locators import PersonalDetailsLocator
from Tests.Pages.base_page import BasePage
import pytest
import json
from Utills.exceptions_loging import Exceptions_logs


class AutomationPage(BasePage):

    def __init__(self, driver: WebDriver, log):
        self.driver = driver
        super().__init__(self.driver)
        self.config = dotenv.dotenv_values(
            dotenv_path=dotenv.find_dotenv("C:/Python/AutomationProject/Tests/.env"))
        self.data = json.load(open(self.config["DATA"]))
        self.img_name = self.config["IMG_LOCATION"]
        self.log = log
    #  personal details

    def fname(self, kyes):
        """
        Name: meni rotblat\n
        Description: collect input element first name and send vals\n
        Date: 21.2.23\n
        :param kyes:
        """
        try:
            # print()
            input = self.driver.find_element(*PersonalDetailsLocator.check_fname)
            input.clear()
            input.send_keys(kyes)
            if input.get_attribute("valitation_message") == "":
                raise AssertionError
            time.sleep(1)
        except Exception as e:
            self.log.send(e=self.config["TEST_FAIL"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def lname(self, kyes):
        """
        Name: meni rotblat\n
        Description: collect input element last name and send vals\n
        :param kyes: \n
        Date: 21.2.23\n
        """
        try:
            input = self.driver.find_element(*PersonalDetailsLocator.check_lname)
            input.clear()
            input.send_keys(kyes)
            if input.get_attribute("valitation_message") == "":
                raise AssertionError
            time.sleep(1)
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send( e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(
                                     time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def city(self, city):
        """
        Name: meni rotblat\n
        Description: collect downdrop element of city and send pick city val\n
        :param city: \n
        Date: 21.2.23\n
        """
        try:
            drop = self.driver.find_element(*PersonalDetailsLocator.check_city)
            dropdown = select(drop)
            dropdown.select_by_visible_text(city)
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send( e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def email(self, Email):
        """
        Name: meni rotblat\n
        Description: collect input element of email and send it val\n
        :param Email: \n
        Date: 21.2.23\n
        """
        try:
            email = self.driver.find_element(*PersonalDetailsLocator.check_email)
            email.clear()
            email.send_keys(Email)
            if input.get_attribute("valitation_message") == "":
                raise AssertionError
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send(e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def areaCode(self,areaCode):
        """
        Name: meni rotblat\n
        Description: collect select element of areaCode and pick from it val\n
        :param areaCode: \n
        Date: 21.2.23\n
        """
        try:
            drop = self.driver.find_element(*PersonalDetailsLocator.check_areaCode)
            dropdown = select(drop)
            dropdown.select_by_visible_text(areaCode)
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send( e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def sel(self,Phone):
        """
        Name: meni rotblat\n
        Description: collect input element of phone number and put on it val\n
        :param Phone:\n
        Date: 21.2.23\n
        """
        try:
            phone = self.driver.find_element(*PersonalDetailsLocator.check_sel)
            phone.clear()
            phone.send_keys(Phone)
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send( e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def checkbox_Female(self):
        """
        Name: meni rotblat\n
        Description: collect checkbox input Female element and checking it\n
        Date: 21.2.23\n
        """
        try:
            checkbox = self.driver.find_element(*PersonalDetailsLocator.check_checkbox_Female)
            checkbox.click()
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send( e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def checkbox_Male(self):
        """
        Name: meni rotblat\n
        Description: collect checkbox input Male element and checking it\n
        Date: 21.2.23\n
        """
        try:
            checkbox = self.driver.find_element(*PersonalDetailsLocator.check_checkbox_Male)
            checkbox.click()
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send( e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def checkbox_Other(self):
        """
        Name: meni rotblat\n
        Description: collect checkbox Other Male element and checking it\n
        Date: 21.2.23\n
        """
        try:
            checkbox = self.driver.find_element(*PersonalDetailsLocator.check_checkbox_Other)
            checkbox.click()
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send( e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def checkbox_Math(self):
        """
        Name: meni rotblat\n
        Description: collect checkbox Math Male element and checking it\n
        Date: 21.2.23\n
        """
        try:
            checkbox = self.driver.find_element(*PersonalDetailsLocator.check_checkbox_Math)
            checkbox.click()
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send( e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def checkbox_Physics(self):
        """
        Name: meni rotblat\n
        Description: collect checkbox Physics Male element and checking it\n
        Date: 21.2.23\n
        """
        try:
            checkbox = self.driver.find_element(*PersonalDetailsLocator.check_checkbox_Physics)
            checkbox.click()
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send(e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def checkbox_POP(self):
        """
        Name: meni rotblat\n
        Description: collect checkbox POP element and checking it\n
        Date: 21.2.23\n
        """
        try:
            checkbox = self.driver.find_element(*PersonalDetailsLocator.check_checkbox_POP)
            checkbox.click()
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send(e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def checkbox_DUD(self):
        """
        Name: meni rotblat\n
        Description: collect checkbox DUD element and checking it\n
        Date: 21.2.23\n
        """
        try:
            checkbox = self.driver.find_element(*PersonalDetailsLocator.check_checkbox_DUD)
            checkbox.click()
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send(e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def checkbox_Biology(self):
        """
        Name: meni rotblat\n
        Description: collect checkbox Biology element and checking it\n
        Date: 21.2.23\n
        """
        try:
            checkbox = self.driver.find_element(*PersonalDetailsLocator.check_checkbox_Biology)
            checkbox.click()
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send(e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def checkbox_Chemistry(self):
        """
        Name: meni rotblat\n
        Description: collect checkbox Chemistry element and checking it\n
        Date: 21.2.23\n
        """
        try:
            checkbox = self.driver.find_element(*PersonalDetailsLocator.check_checkbox_Chemistry)
            checkbox.click()
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send(e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def checkbox_English(self):
        """
        Name: meni rotblat\n
        Description: collect checkbox English element and checking it\n
        Date: 21.2.23\n
        """
        try:
            checkbox = self.driver.find_element(*PersonalDetailsLocator.check_checkbox_English)
            checkbox.click()
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send( e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    # buttons
    def clear_button(self):
        """
        Name: meni rotblat\n
        Description: collect clear button element and click on it\n
        Date: 21.2.23\n
        """
        try:
            checkbox = self.driver.find_element(*PersonalDetailsLocator.check_clear_b)
            checkbox.click()
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send(e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def send_button(self):
        """
        Name: meni rotblat\n
        Description: collect sent button element and click on it\n
        Date: 21.2.23\n
        """
        try:
            checkbox = self.driver.find_element(*PersonalDetailsLocator.check_send_b)
            checkbox.click()
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send( e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

#  JS buttons

    def stext(self, val):
        """
        Name: meni rotblat\n
        Description: collect text area and alert elements and click on it, fill an alert element and accept on it\n
        Date: 21.2.23\n
        """
        try:
            alert = self.driver.find_element(*PersonalDetailsLocator.check_stext_alert)
            alert.click()
            time.sleep(0.5)

            alert = Alert(self.driver)
            time.sleep(0.5)

            alert.send_keys(str(val))
            time.sleep(0.5)

            alert.accept()
            time.sleep(0.5)

        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send( e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def loading(self):
        """
        Name: meni rotblat\n
        Description: collect loading button element and click on it\n
        Date: 21.2.23\n
        """
        try:
            loading = self.driver.find_element(*PersonalDetailsLocator.check_loading)
            loading.click()
            time.sleep(3)
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send(e=self.config["GENERAL_ERR"].format("loading", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

#  links

    def nextPage(self):
        """
        Name: meni rotblat\n
        Description: collect link element and click on it\n
        Date: 21.2.23\n
        """
        try:
            snext_link = self.driver.find_element(*PersonalDetailsLocator.nextPage).get_attribute("href")
            parent_handle = self.driver.current_window_handle
            self.driver.switch_to.new_window('new_tab')
            self.driver.get(snext_link)
            time.sleep(3)
            title = self.driver.title
            self.driver.close()
            self.driver.switch_to.window(parent_handle)
            return title
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send( e=self.config["GENERAL_ERR"].format("Exception_nextPage", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def Windy(self):
        """
        Name: meni rotblat\n
        Description: collect link element and click on it\n
        Date: 21.2.23\n
        """
        try:
            windy_link = self.driver.find_element(*PersonalDetailsLocator.Windy).get_attribute("href")
            parent_handle = self.driver.current_window_handle
            self.driver.switch_to.new_window('new_tab')
            self.driver.get(windy_link)
            time.sleep(3)
            title = self.driver.title
            self.driver.close()
            self.driver.switch_to.window(parent_handle)
            return title
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send(e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def TeraSanta(self):
        """
        Name: meni rotblat\n
        Description: collect link element and click on it\n
        Date: 21.2.23\n
        """
        try:
            tera_link = self.driver.find_element(*PersonalDetailsLocator.TeraSanta).get_attribute("href")
            parent_handle = self.driver.current_window_handle
            self.driver.switch_to.new_window('new_tab')
            self.driver.get(tera_link)
            time.sleep(3)
            title = self.driver.title
            self.driver.close()
            self.driver.switch_to.window(parent_handle)
            return title
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send(e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(
                                     time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))

    def JavaBook(self):
        """
        Name: meni rotblat\n
        Description: collect link element and click on it\n
        Date: 21.2.23\n
        """
        try:
            java_link = self.driver.find_element(*PersonalDetailsLocator.JavaBook).get_attribute("href")
            parent_handle = self.driver.current_window_handle
            self.driver.switch_to.new_window('new_tab')
            self.driver.get(java_link)
            time.sleep(3)
            title = self.driver.title
            self.driver.close()
            self.driver.switch_to.window(parent_handle)
            return title
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send(e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(
                                     time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))
            assert False

    def youTube(self):
        """
        Name: meni rotblat\n
        Description: collect link element and click on it\n
        Date: 21.2.23\n
        """
        try:
            yt_link = self.driver.find_element(*PersonalDetailsLocator.YouTube).get_attribute("href")
            parent_handle = self.driver.current_window_handle
            self.driver.switch_to.new_window('new_tab')
            self.driver.get(yt_link)
            time.sleep(3)
            title = self.driver.title
            self.driver.close()
            self.driver.switch_to.window(parent_handle)
            return title
        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            self.log.send( e=self.config["GENERAL_ERR"].format("Exception_test_general", "", e),
                                 pic_name=self.img_name.format(
                                     time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))
