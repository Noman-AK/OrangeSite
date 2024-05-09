import time

import pytest

from PageObjects.TimeAtWork import Time_at_work


class test_TimeAtWork:
    @pytest.fixture(scope="function")
    def setup(self, browser):
        self.driver = browser

    def test_Timeatwork(self, setup):
        self.taw = Time_at_work(self.driver)
        self.taw.heading()
        self.taw.stopwatch_button()
        time.sleep(3)
        self.taw.attendance_punch_in()
        time.sleep(3)
        self.taw.attendance_punch_out()