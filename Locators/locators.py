from selenium.webdriver.common.by import By


class PersonalDetailsLocator(object):
    check_fname = (By.XPATH, "//input[@name='fname']")
    check_lname = (By.XPATH, "//input[@name='lname']")

