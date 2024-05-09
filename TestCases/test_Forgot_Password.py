import time

import pytest
from PageObjects.ForgotPassword import ForgotPassword


class Test_Forgot_Password:
    @pytest.fixture(scope="function")
    def setup(self, browser):
        self.driver = browser

    def test_Forgot_Password(self, setup):
        self.fp = ForgotPassword(self.driver)
        self.fp.click_Forgot_Password()
        time.sleep(5)
        self.fp.forgot_Farm_Username_Field()
        time.sleep(2)
        self.fp.reset_Password_button()
        time.sleep(2)
        self.fp.reset_Password_output()
        # self.fp.cancel_button_click()