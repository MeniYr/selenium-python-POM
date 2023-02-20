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
            gettitle = self.driver.title
            return gettitle == title

