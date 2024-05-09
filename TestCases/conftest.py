from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture(scope="function")
def browser():
    # driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver = webdriver.Chrome('C://Users//nomia//OneDrive//Desktop//chromedriver-win64//chromedriver.exe')
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    yield driver
    driver.quit()
