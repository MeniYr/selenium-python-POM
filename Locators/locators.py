from selenium.webdriver.common.by import By


class PersonalDetailsLocator(object):
    check_fname = (By.XPATH, "//input[@name='fname']")
    check_lname = (By.XPATH, "//input[@name='lname']")
    check_city = (By.NAME,"City")
    check_email = (By.ID,"email")
    check_areaCode = (By.NAME,"areaCode")
    check_sel = (By.ID,"phone")
    check_stext_alert = (By.XPATH,"//button[contains(text(),'Set Text')]")
    check_stext_res = (By.ID,"pbyuser")
    check_loading = (By.XPATH,"//button[contains(text(),'Start loading')]")
    check_loading_text = (By.ID, "startLoad")
    check_checkbox_Female = (By.XPATH,"//*[@name='gender' and @value='F']")
    check_checkbox_Male = (By.XPATH,"//*[@name='gender' and @value='M']")
    check_checkbox_Other = (By.XPATH,"//*[@name='gender' and @value='O']")
    check_checkbox_Math = (By.XPATH,"//*[@name='math' and @value='M']")
    check_checkbox_Physics = (By.XPATH,"//*[@name='pyhs' and @value='P']")
    check_checkbox_POP = (By.XPATH,"//*[@name='gender' and @value='P']")
    check_checkbox_DUD = (By.XPATH,"//*[@name='gender' and @value='M' and @id = 'o']")
    check_checkbox_Biology = (By.XPATH,"//*[@name='bio' and @value='B']")
    check_checkbox_Chemistry = (By.XPATH,"//*[@name='chem' and @value='C']")
    check_checkbox_English = (By.XPATH,"//*[@name='eng' and @value='E']")
    check_clear_b = (By.ID,"CB")
    check_send_b = (By.ID,"send")
    nextPage = (By.NAME,"nextPage")
    Windy = (By.NAME,"myLink")
    TeraSanta = (By.NAME,"myLinkTS")
    JavaBook = (By.NAME,"notMyLink")
    YouTube = (By.LINK_TEXT,"YouTube")

class NextPageLocators(object):
    check_link = (By.XPATH,"//button[contains(text(),'Change Title')]")
    nextPage = (By.NAME, "nextPage")




