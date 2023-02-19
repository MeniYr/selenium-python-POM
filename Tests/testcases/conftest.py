import time

import dotenv
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="class")
def setup(request):
    config = dotenv.dotenv_values(dotenv_path=dotenv.find_dotenv("C:/Python/AutomationProject/Tests/.env"))
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    fluent_wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=["ElementNotVisibleException", "ElementNotSelectableException"])
    driver.get(config["URL"])
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.fluent_wait = fluent_wait

    yield  # tear down
    driver.close()
