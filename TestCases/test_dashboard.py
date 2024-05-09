import pytest

from Logs import Excel_data_managers

file = "C://Users//nomia//OneDrive//Desktop//Orange HRM Data.xlsx"
total_rows = Excel_data_managers.getRowCount(file, 'Sidebar')
total_column = Excel_data_managers.getColumnCount(file, 'Sidebar')


class test_dashboard:
    @pytest.fixture(scope="function")
    def setup(self, browser):
        self.driver = browser

    def options(self, setup):
        for n in range(2, total_rows + 1):
            sideBarOptions = Excel_data_managers.readData(file, 'Sidebar', n, 1)
            print(sideBarOptions)
        for n in range(2, total_rows + 1):
            sideBarOptions = Excel_data_managers.readData(file, 'Sidebar', n, 1)
            print(sideBarOptions)
