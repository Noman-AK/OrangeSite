import pytest
import self as self
from selenium.webdriver.common.by import By

from Logs import Excel_data_managers


class TestSidebar:
    sideBarOptionsXpath = "//ul[@class='oxd-main-menu']//li"

    def __init__(self, driver):
        self.driver = driver

    def sideBar(self):
        sideBar = self.driver.find_element(By.XPATH, self.sideBarOptionsXpath).text
        return sideBar
