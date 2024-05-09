from selenium.webdriver.common.by import By


class LoginPage:
    username_field_name = "username"
    password_field_name = "password"
    login_button_xpath = "//button[normalize-space()='Login']"
    logout_button_xpath = "//a[normalize-space()='Logout']"
    profile_dropdown = "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']"
    toast_for_error = "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']"
    dashboard_title_xpath = "//h6"
    login_page_title_xpath = "//h5"

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.NAME, self.username_field_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.NAME, self.password_field_name).send_keys(password)

    def login(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def dashboard(self):
        title = self.driver.find_element(By.XPATH, self.dashboard_title_xpath).text
        print(title)
        return title

    def loginPage(self):
        loginPage_title = self.driver.find_element(By.XPATH, self.login_page_title_xpath).text
        return loginPage_title
