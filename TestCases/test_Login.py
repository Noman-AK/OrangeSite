import time
import pytest
from selenium.common import NoSuchElementException

from Logs import Excel_data_managers
from PageObjects.LoginPage import LoginPage
from TestCases.test_dashboard import test_dashboard

# Excel file data count
file = "C://Users//nomia//OneDrive//Desktop//Orange HRM Data.xlsx"
total_rows = Excel_data_managers.getRowCount(file, 'Login')
total_column = Excel_data_managers.getColumnCount(file, 'Login')


class Test_Login:
    @pytest.fixture(scope="function")
    def setup(self, browser):
        self.driver = browser

    def test_verify_title(self, browser):
        assert browser.title == "OrangeHRM"

    def test_login(self, setup):
        self.lp = LoginPage(self.driver)

        for r in range(2, total_rows + 1):
            username = Excel_data_managers.readData(file, 'Login', r, 1)
            password = Excel_data_managers.readData(file, 'Login', r, 2)
            time.sleep(2)
            self.lp.enter_username(username)
            self.lp.enter_password(password)
            self.lp.login()
            time.sleep(2)
            try:
                title = self.lp.loginPage()
                if title == "Login":
                    print("Test Failed")
                    Excel_data_managers.writeData(file, 'Login', r, 3, "Failed")
            except NoSuchElementException:
                print("Test Passed")
                Excel_data_managers.writeData(file, 'Login', r, 3, "Passed")

                testSidebar=test_dashboard()
                testSidebar.options(self)
            time.sleep(2)

