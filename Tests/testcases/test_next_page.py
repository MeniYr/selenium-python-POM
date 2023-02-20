import json
import time

import dotenv
import pytest

from Tests.Pages.base_page import BasePage
from Tests.Pages.next_page import NextPage
from Utills.exceptions_loging import Exceptions_logs


@pytest.mark.usefixtures("setup")
class TestNextPage():
    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.config = dotenv.dotenv_values(dotenv_path=dotenv.find_dotenv("C:/Python/AutomationProject/Tests/.env"))
        self.data = json.load(open(self.config["DATA"]))
        self.np = NextPage(self.driver)

    @pytest.mark.dm
    def test_change_me_btn(self):
        img_name = self.config["IMG_LOCATION"].format(time.strftime("%m.%d.%Y_%H-%M-%S", time.localtime()))
        try:
            assert self.np.change_title(self.data["data"]["links"]["nextPage"]["finalVal"])
            self.log.send(e=self.config["TEST_PASS"].format("test_change_me_btn",
                                                                         self.data["data"]["links"]["nextPage"]["finalVal"]),
                                 pic_name=None)
        except Exception as e:
            self.driver.save_screenshot(filename=img_name)
            self.log.send( e=self.config["TEST_FAIL"].format("test_links",
                                                                         self.data["data"]["links"]["nextPage"]["finalVal"], e),
                                 pic_name=img_name)
            assert False, e
        except AssertionError as ae:
            self.driver.save_screenshot(filename=img_name)
            self.log.send(e=self.config["ASSERT_FAIL"].format("test_links",
                                                                           self.data["data"]["links"]["nextPage"]["finalVal"], ae),
                                 pic_name=img_name)
            assert False, ae
