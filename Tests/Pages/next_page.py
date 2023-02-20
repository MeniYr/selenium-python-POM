import json
import time

import dotenv
from selenium.common import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Locators.locators import NextPageLocators
from Tests.Pages.base_page import BasePage
from Utills.exceptions_loging import Exceptions_logs


class NextPage(BasePage):

    def __init__(self, driver: WebDriver):
        self.driver = driver
        super().__init__(self.driver)
        self.config = dotenv.dotenv_values(
            dotenv_path=dotenv.find_dotenv("C:/Python/AutomationProject/Tests/.env"))
        self.data = json.load(open(self.config["DATA"]))
        self.img_name = self.config["IMG_LOCATION"]

    def change_title(self, val):
        try:
            npage = self.driver.find_element(*NextPageLocators.nextPage)
            npage.click()

            btn = self.driver.find_element(*NextPageLocators.check_link)
            btn.click()
            time.sleep(1)
            wait = WebDriverWait(self.driver, timeout=5, poll_frequency=1,
                                 ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
            changed = wait.until(ec.title_is(val))
            return changed

        except Exception as e:
            img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
            self.driver.save_screenshot(img_name)
            Exceptions_logs.send(self, e=self.config["GENERAL_ERR"].format("Exception_nextPage", "", e),
                                 pic_name=self.img_name.format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime())))
