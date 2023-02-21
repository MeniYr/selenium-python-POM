import re
import time
import dotenv
import pytest
import json
from Tests.Pages.automation import AutomationPage
from Tests.Pages.automation_resualts import AutomationResPage
from Utills.exceptions_loging import Exceptions_logs


@pytest.mark.usefixtures("setup")
class TestAutomation():
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.config = dotenv.dotenv_values(dotenv_path=dotenv.find_dotenv("C:/Python/AutomationProject/Tests/.env"))
        self.data = json.load(open(self.config["DATA"]))
        self.au = AutomationPage(self.driver, self.log)
        self.res = AutomationResPage(self.driver, self.log)

#  general title
    @pytest.mark.general_title
    def test_general_title(self):
        img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
        try:
            gettitle = self.au.check_title(self.data["data"]["general"]["title"])
            # print(*PersonalDetailsLocator.check_title)
            assert gettitle is True
            self.log.send(e=self.config["TEST_PASS"].format("check_title",
                                                                         self.data["data"]["general"]["title"]),
                                 pic_name=None)

        except AssertionError as ae:
            self.driver.save_screenshot(filename=img_name)
            self.log.send( e=self.config["ASSERT_FAIL"].format("AssertionError_test_general", "", ae),
                                 pic_name=img_name)
        except Exception as e:
            self.driver.save_screenshot(filename=img_name)
            self.log.send( e=self.config["TEST_FAIL"].format("Exception_test_general", "", e),
                                 pic_name=img_name)

#  personal details
    @pytest.mark.personals_fname
    def test_personals_fname(self):
        """
        Name: meni rotblat\n
        Description: tests first name input\n
        Date: 21.2.23\n
        """
        img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
        for i in self.data["data"]["pesonal_details"]["firstName"]["trueVal"]:
            try:
                self.au.fname(i)
                assert self.res.fname() == i
                self.log.send(e=self.config["TEST_PASS"].format("test_personals_fname",
                                                                self.data["data"]["pesonal_details"][
                                                                    "firstName"]["trueVal"]), pic_name=None)
            except Exception as e:
                self.driver.save_screenshot(filename=img_name)
                self.log.send(e=self.config["TEST_FAIL"].format("test_personals_fname",
                                                            self.data["data"]["pesonal_details"][
                                                                "firstName"]["trueVal"], e),
                          pic_name=img_name)

        for i in self.data["data"]["pesonal_details"]["firstName"]["wrongValues"]:
            try:
                self.au.fname(i)
                assert self.res.fname() == ''
                self.log.send(e=self.config["TEST_PASS"].format("test_personals_fname",
                                                                self.data["data"]["pesonal_details"][
                                                                    "firstName"]["wrongValues"]), pic_name=None)
            except AssertionError as a:
                self.driver.save_screenshot(filename=img_name)
                self.log.send(e=self.config["ASSERT_FAIL"].format("test_personals_fname",
                                                                  self.data["data"]["pesonal_details"][
                                                                      "firstName"]["wrongValues"], a),
                              pic_name=img_name)




            # assert False, e

    @pytest.mark.personals_lname
    def test_personals_lname(self):
        """
        Name: meni rotblat\n
        Description: tests last name input\n
        Date: 21.2.23\n
        """
        img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
        for i in self.data["data"]["pesonal_details"]["lastName"]["trueVal"]:
            try:
                self.au.lname(i)
                time.sleep(1)
                assert self.res.lname() == i
                self.log.send( e=self.config["TEST_PASS"].format("test_personals_lname",
                                                                         self.data["data"]["pesonal_details"][
                                                                             "lastName"]["trueVal"]), pic_name=None)
            except Exception as e:
                self.driver.save_screenshot(filename=img_name)
                self.log.send(e=self.config["TEST_FAIL"].format("test_personals_lname",
                                                                self.data["data"]["pesonal_details"][
                                                                    "lastName"]["trueVal"], e),
                              pic_name=img_name)

        for i in self.data["data"]["pesonal_details"]["lastName"]["wrongValues"]:
            try:
                self.au.lname(i)
                time.sleep(1)
                assert self.res.lname() == ''
                self.log.send( e=self.config["TEST_PASS"].format("test_personals_lname",
                                                                         self.data["data"]["pesonal_details"][
                                                                             "lastName"]["trueVal"]), pic_name=None)
            except AssertionError as ae:
                self.driver.save_screenshot(filename=img_name)
                self.log.send(e=self.config["ASSERT_FAIL"].format("test_personals_lname",
                                                                  self.data["data"]["pesonal_details"][
                                                                      "lastName"]["trueVal"], ae),pic_name=img_name)


    @pytest.mark.personals_city
    def test_personals_city(self):
        """
        Name: meni rotblat\n
        Description: tests city dropdown\n
        Date: 21.2.23\n
        """
        img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))

        for i in self.data["data"]["pesonal_details"]["city"]["trueVal"]:
            try:
                self.au.city(i)
                time.sleep(1)
                assert self.res.city(i) == i
                self.log.send(e=self.config["TEST_PASS"].format("test_personals_fname",
                                                                self.data["data"]["pesonal_details"][
                                                                    "city"]["trueVal"]), pic_name=None)
            except AssertionError as ae:
                self.driver.save_screenshot(filename=img_name)
                self.log.send(e=self.config["ASSERT_FAIL"].format("test_personals_lname",
                                                                  self.data["data"]["pesonal_details"][
                                                                      "city"]["trueVal"], ae),
                              pic_name=img_name)





    @pytest.mark.personals_email
    def test_personals_email(self):
        """
        Name: meni rotblat\n
        Description: tests email input\n
        Date: 21.2.23\n
        """
        img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
        try:
            rule = r"[a-z]*@[a-z]+\.[a-z]+"
            for i in self.data["data"]["pesonal_details"]["email"]["trueVal"]:
                self.au.email(i)
                time.sleep(1)
                assert re.match(rule, i)
                assert self.res.email() == i
                Exceptions_logs.send(self, e=self.config["TEST_PASS"].format("test_personals_fname",
                                                                             self.data["data"]["pesonal_details"][
                                                                                 "email"]["trueVal"]), pic_name=None)

        except Exception as e:
            self.driver.save_screenshot(filename=img_name)
            self.log.send(e=self.config["TEST_FAIL"].format("test_personals_lname",
                                                                         self.data["data"]["pesonal_details"][
                                                                             "email"]["trueVal"], e),
                                 pic_name=img_name)
            assert False, e
        except AssertionError as ae:
            self.driver.save_screenshot(filename=img_name)
            self.log.send(e=self.config["ASSERT_FAIL"].format("test_personals_lname",
                                                                           self.data["data"]["pesonal_details"][
                                                                               "email"]["trueVal"], ae),
                                 pic_name=img_name)
            assert False, ae

    @pytest.mark.personals_area
    def test_personals_areaCode(self):
        """
        Name: meni rotblat\n
        Description: tests erea code dropdown dropdown\n
        Date: 21.2.23\n
        """
        img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
        try:
            for i in self.data["data"]["pesonal_details"]["phone"]["area_Code"]:
                self.au.areaCode(i)
                time.sleep(1)
                assert self.res.areaCode(i) == i
                self.log.send( e=self.config["TEST_PASS"].format("test_personals_areaCode",
                                                                             self.data["data"]["pesonal_details"][
                                                                                 "phone"]["area_Code"]),
                                     pic_name=None)
        except Exception as e:
            self.driver.save_screenshot(filename=img_name)
            self.log.send( e=self.config["TEST_FAIL"].format("test_personals_areaCode",
                                                                         self.data["data"]["pesonal_details"]["phone"][
                                                                             "area_Code"], e), pic_name=img_name)
            assert False, e
        except AssertionError as ae:
            self.driver.save_screenshot(filename=img_name)
            self.log.send(e=self.config["ASSERT_FAIL"].format("test_personals_areaCode",
                                                                           self.data["data"]["pesonal_details"][
                                                                               "phone"]["area_Code"], ae),
                                 pic_name=img_name)
            assert False, ae

    @pytest.mark.personals_sel
    def test_personals_sel(self):
        """
        Name: meni rotblat\n
        Description: tests selephon input\n
        Date: 21.2.23\n
        """
        img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
        try:
            # true vals
            for i in self.data["data"]["pesonal_details"]["phone"]["trueVal"]:
                self.au.sel(i)
                time.sleep(1)
                assert self.res.sel() == i

            # wrong vals
            for i in self.data["data"]["pesonal_details"]["phone"]["wrongValues"]:
                self.au.sel(i)
                time.sleep(1)
                assert self.res.sel() != i
                self.log.send(e=self.config["TEST_PASS"].format("test_personals_areaCode",
                                                                             self.data["data"][
                                                                                 "pesonal_details"][
                                                                                 "phone"]["wrongValues"]),
                                     pic_name=None)
        except Exception as e:
            self.driver.save_screenshot(filename=img_name)
            self.log.send(e=self.config["TEST_FAIL"].format("test_personals_areaCode",
                                                                         self.data["data"]["pesonal_details"][
                                                                             "phone"]["wrongValues"], e),
                                 pic_name=img_name)
            assert False, e
        except AssertionError as ae:
            self.driver.save_screenshot(filename=img_name)
            self.log.send( e=self.config["ASSERT_FAIL"].format("test_personals_areaCode",
                                                                           self.data["data"]["pesonal_details"][
                                                                               "phone"]["wrongValues"], ae),
                                 pic_name=img_name)
            assert False, ae

    @pytest.mark.personals_checkbox
    def test_personals_chekbox(self):
        """
        Name: meni rotblat\n
        Description: tests checkboxes\n
        Date: 21.2.23\n
        """
        img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
        try:
            self.au.checkbox_Female()
            time.sleep(1)
            assert self.res.checkbox_Female()
            time.sleep(1)
            self.au.checkbox_Male()
            assert self.res.checkbox_Male()
            time.sleep(1)
            self.au.checkbox_Other()
            assert self.res.checkbox_Other()
            time.sleep(1)
            self.au.checkbox_Math()
            assert self.res.checkbox_Math()
            time.sleep(1)
            self.au.checkbox_Physics()
            assert self.res.checkbox_Physics()
            time.sleep(1)
            self.au.checkbox_POP()
            assert self.res.checkbox_POP()
            time.sleep(1)
            self.au.checkbox_DUD()
            assert self.res.checkbox_DUD()
            time.sleep(1)
            self.au.checkbox_Biology()
            assert self.res.checkbox_Biology()
            time.sleep(1)
            self.au.checkbox_Chemistry()
            assert self.res.checkbox_Chemistry()
            time.sleep(1)
            self.au.checkbox_English()
            assert self.res.checkbox_English()
            time.sleep(1)
            # check if selected

            self.log.send( e=self.config["TEST_PASS"].format("test_personals_areaCode",
                                                                         self.data["data"][
                                                                             "pesonal_details"][
                                                                             "checkbocks"]["trueVal"]),
                                 pic_name=None)
        except Exception as e:
            self.driver.save_screenshot(filename=img_name)
            self.log.send(e=self.config["TEST_FAIL"].format("test_personals_areaCode",
                                                                         self.data["data"]["pesonal_details"][
                                                                             "checkbocks"]["trueVal"], e),
                                 pic_name=img_name)
            assert False, e
        except AssertionError as ae:
            self.driver.save_screenshot(filename=img_name)
            self.log.send(e=self.config["ASSERT_FAIL"].format("test_personals_areaCode",
                                                                           self.data["data"]["pesonal_details"][
                                                                               "checkbocks"]["trueVal"], ae),
                                 pic_name=img_name)
            assert False, ae

    @pytest.mark.personals_clear
    def test_personals_clear_button(self):
        """
        Name: meni rotblat\n
        Description: tests the clear btn aster fill some inputs\n
        Date: 21.2.23\n
        """
        img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
        try:
            self.au.checkbox_Female()
            self.au.checkbox_Male()
            self.au.checkbox_Other()
            self.au.checkbox_Math()
            self.au.checkbox_Physics()
            self.au.checkbox_POP()
            self.au.checkbox_DUD()
            self.au.checkbox_Biology()
            self.au.checkbox_Chemistry()
            self.au.checkbox_English()

            self.au.clear_button()
            time.sleep(1)
            # check for example
            assert not self.res.checkbox_Female()
            assert not self.res.checkbox_Male()
            assert not self.res.checkbox_Other()
            assert not self.res.checkbox_Math()
            assert not self.res.checkbox_Physics()
            assert not self.res.checkbox_POP()
            assert not self.res.checkbox_DUD()
            assert not self.res.checkbox_Biology()
            assert not self.res.checkbox_Chemistry()
            assert not self.res.checkbox_English()

            self.log.send(
                                 e=self.config["TEST_PASS"].format("test_personals_clear_button", self.data["data"][
                                     "pesonal_details"][
                                     "checkbocks"]["trueVal"]),
                                 pic_name=None)
        except Exception as e:
            self.driver.save_screenshot(filename=img_name)
            self.log.send(
                                 e=self.config["TEST_FAIL"].format("test_personals_clear_button", self.data["data"][
                                     "pesonal_details"][
                                     "checkbocks"]["trueVal"], e),
                                 pic_name=img_name)
            assert False, e
        except AssertionError as ae:
            self.driver.save_screenshot(filename=img_name)
            self.log.send(
                                 e=self.config["ASSERT_FAIL"].format("test_personals_clear_button", self.data["data"][
                                     "pesonal_details"][
                                     "checkbocks"]["trueVal"], ae),
                                 pic_name=img_name)
            assert False, ae

    @pytest.mark.personals_send
    def test_personals_send_button(self):
        """
        Name: meni rotblat\n
        Description: tests sent btn after fiiling some inputs\n
        Date: 21.2.23\n
        """
        img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
        try:
            email = self.data["data"]["pesonal_details"]["email"]["trueVal"][0]
            fname = self.data["data"]["pesonal_details"]["firstName"]["trueVal"][0]
            lname = self.data["data"]["pesonal_details"]["lastName"]["trueVal"][0]
            self.au.email(email)
            self.au.fname(fname)
            self.au.lname(lname)
            params = "email: " + email + " fname: " + fname + " lname: " + lname
            time.sleep(1)
            self.au.send_button()
            time.sleep(1)

            self.log.send( e=self.config["TEST_PASS"].format("test_personals_send_button", params),
                                 pic_name=None)
        except Exception as e:
            self.driver.save_screenshot(filename=img_name)
            self.log.send(e=self.config["TEST_FAIL"].format("test_personals_send_button", params, e),
                                 pic_name=img_name)
            assert False, e
        except AssertionError as ae:
            self.driver.save_screenshot(filename=img_name)
            self.log.send(e=self.config["ASSERT_FAIL"].format("test_personals_send_button", params, ae),
                                 pic_name=img_name)
            assert False, ae

#  js buttons
    @pytest.mark.jsbtns_stext
    def test_jsbtns_stext(self):
        """
        Name: meni rotblat\n
        Description: tests js button alert text\n
        Date: 21.2.23\n
        """
        img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
        try:
            for i in self.data["data"]["buttons"]["setText"]["trueVal"]:
                self.au.stext(i)
                time.sleep(1)
                print(i)
                assert self.res.stext(i)
            self.log.send(e=self.config["TEST_PASS"].format("test_jsbtns_stext",self.data["data"]["buttons"]["setText"]["trueVal"]),
                                 pic_name=None)
        except Exception as e:
            self.driver.save_screenshot(filename=img_name)
            self.log.send(e=self.config["TEST_FAIL"].format(
                self.data["data"]["buttons"]["setText"]["trueVal"], e),
                                 pic_name=img_name)
            assert False, e
        except AssertionError as ae:
            self.driver.save_screenshot(filename=img_name)
            self.log.send( e=self.config["ASSERT_FAIL"].format(
                self.data["data"]["buttons"]["setText"]["trueVal"], ae),
                                 pic_name=img_name)
            assert False, ae

    @pytest.mark.jsbtns_l
    def test_jsbtns_loading(self):
        """
        Name: meni rotblat\n
        Description: tests loading btn so that after waiting, check if value is changed\n
        Date: 21.2.23\n
        """
        img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
        try:
            self.au.loading()
            time.sleep(1)
            assert self.res.loading(self.data["data"]["buttons"]["loading"]["trueVal"])

            self.log.send(e=self.config["TEST_PASS"].format("test_jsbtns_loading",self.data["data"]["buttons"]["loading"]["trueVal"]),
                                 pic_name=None)
        except Exception as e:
            self.driver.save_screenshot(filename=img_name)
            self.log.send(e=self.config["TEST_FAIL"].format("test_jsbtns_loading",
                self.data["data"]["buttons"]["loading"]["trueVal"], e),
                                 pic_name=img_name)
            assert False, e
        except AssertionError as ae:
            self.driver.save_screenshot(filename=img_name)
            self.log.send(e=self.config["ASSERT_FAIL"].format("test_jsbtns_loading",
                self.data["data"]["buttons"]["loading"]["trueVal"], ae),
                                 pic_name=img_name)
            assert False, ae

#  links
    @pytest.mark.np
    def test_next_page(self):
        """
        Name: meni rotblat\n
        Description: tests next page link\n
        Date: 21.2.23\n
        """
        img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
        try:
            title = self.au.nextPage()
            assert self.data["data"]["links"]["nextPage"]["initVal"] == title
            time.sleep(1)
            self.log.send( e=self.config["TEST_PASS"].format("test_next_page",
                                                                         self.data["data"]["links"]["nextPage"]["initVal"]),
                                 pic_name=None)
        except Exception as e:
            self.driver.save_screenshot(filename=img_name)
            self.log.send(e=self.config["TEST_FAIL"].format("test_next_page",
                self.data["data"]["links"]["nextPage"]["initVal"], e),
                                 pic_name=img_name)
            assert False, e
        except AssertionError as ae:
            self.driver.save_screenshot(filename=img_name)
            self.log.send(e=self.config["ASSERT_FAIL"].format("test_next_page",
                self.data["data"]["links"]["nextPage"]["initVal"], ae),
                                 pic_name=img_name)
            assert False, ae

    @pytest.mark.win
    def test_windy(self):
        """
        Name: meni rotblat\n
        Description: tests windy link\n
        Date: 21.2.23\n
        """
        img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
        try:
            title = self.au.Windy()
            assert self.data["data"]["links"]["Windy"]["trueVal"] == title
            time.sleep(1)

            self.log.send(e=self.config["TEST_PASS"].format("test_windy",
                                                                         self.data["data"]["links"]["Windy"]["trueVal"] ),
                                 pic_name=None)
        except Exception as e:
            self.driver.save_screenshot(filename=img_name)
            self.log.send(e=self.config["TEST_FAIL"].format("test_windy",
                                                                         self.data["data"]["links"]["Windy"]["trueVal"] , e),
                                 pic_name=img_name)
            assert False, e
        except AssertionError as ae:
            self.driver.save_screenshot(filename=img_name)
            self.log.send( e=self.config["ASSERT_FAIL"].format("test_windy",
                                                                           self.data["data"]["links"]["Windy"][
                                                                               "trueVal"], ae),
                                 pic_name=img_name)
            assert False, ae

    @pytest.mark.ts
    def test_terasenta(self):
        """
        Name: meni rotblat\n
        Description: tests terasenta link\n
        Date: 21.2.23\n
        """
        img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
        try:
            title = self.au.TeraSanta()
            assert self.data["data"]["links"]["TeraSanta"]["trueVal"] == title
            time.sleep(1)

            self.log.send(e=self.config["TEST_PASS"].format("test_terasenta",
                                                                         self.data["data"]["links"]["TeraSanta"]["trueVal"]),
                                 pic_name=None)
        except Exception as e:
            self.driver.save_screenshot(filename=img_name)
            self.log.send(e=self.config["TEST_FAIL"].format("test_terasenta",
                                                                         self.data["data"]["links"]["TeraSanta"]["trueVal"], e),
                                 pic_name=img_name)
            assert False, e
        except AssertionError as ae:
            self.driver.save_screenshot(filename=img_name)
            self.log.send(e=self.config["ASSERT_FAIL"].format("test_terasenta",
                                                                           self.data["data"]["links"]["TeraSanta"]["trueVal"], ae),
                                 pic_name=img_name)
            assert False, ae

    @pytest.mark.jb
    def test_javabook(self):
        """
        Name: meni rotblat\n
        Description: tests javabook link\n
        Date: 21.2.23\n
        """
        img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
        try:

            title = self.au.JavaBook()
            assert not title.__contains__("404")
            time.sleep(1)

            self.log.send(e=self.config["TEST_PASS"].format("test_javsbook",
                                                                         ""),
                                 pic_name=None)
        except Exception as e:
            self.driver.save_screenshot(filename=img_name)
            self.log.send(e=self.config["TEST_FAIL"].format("test_javsbook",
                                                                         "", e),
                                 pic_name=img_name)
            assert False, e
        except AssertionError as ae:
            self.driver.save_screenshot(filename=img_name)
            self.log.send(e=self.config["ASSERT_FAIL"].format("test_javsbook",
                                                                           "", ae),
                                 pic_name=img_name)
            assert False, ae

    @pytest.mark.yt
    def test_youtube(self):
        """
        Name: meni rotblat\n
        Description: tests youtube link\n
        Date: 21.2.23\n
        """
        img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
        try:
            title = self.au.youTube()
            assert self.data["data"]["links"]["YouTube"]["trueVal"] == title
            time.sleep(1)

            self.log.send(e=self.config["TEST_PASS"].format("test_youtube",
                                                                         self.data["data"]["links"]["YouTube"]["trueVal"]),
                                 pic_name=None)
        except Exception as e:
            self.driver.save_screenshot(filename=img_name)
            self.log.send(e=self.config["TEST_FAIL"].format("test_youtube",
                                                                         self.data["data"]["links"]["YouTube"]["trueVal"], e),
                                 pic_name=img_name)
            assert False, e
        except AssertionError as ae:
            self.driver.save_screenshot(filename=img_name)
            self.log.send(e=self.config["ASSERT_FAIL"].format("test_youtube",
                                                                           self.data["data"]["links"]["YouTube"]["trueVal"], ae),
                                 pic_name=img_name)
            assert False, ae