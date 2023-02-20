import json
import time

import dotenv
from selenium.webdriver.common.by import By

from Locators.locators import PersonalDetailsLocator
from Utills.exceptions_loging import Exceptions_logs


class BasePage:
    def __init__(self, driver):
        self.config = dotenv.dotenv_values(
            dotenv_path=dotenv.find_dotenv("C:/Python/AutomationProject/Tests/.env"))
        self.driver = driver


    def check_title(self, title):
        """
        Name: meni rotblat\n
        Description: check title of correct driver and return is params equals as boolean\n
        Date: 21.2.23\n
        """
        gettitle = self.driver.title
        return gettitle == title

