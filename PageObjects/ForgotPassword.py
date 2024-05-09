from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class ForgotPassword:
    forgot_password_button = "//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']"
    forgot_password_username = "username"
    reset_Password_XPATH = "//button[normalize-space()='Reset Password']"
    reset_Password_Output_XPATH = "//p[@class='oxd-text oxd-text--p orangehrm-card-note orangehrm-card-note--background orangehrm-forgot-password-card-note']//p[@class='oxd-text oxd-text--p']"
    cancel_Button = "//button[normalize-space()='Cancel']"

    def __init__(self, driver):
        self.driver = driver

    def click_Forgot_Password(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, self.forgot_password_button).click()

    def forgot_Farm_Username_Field(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.NAME, self.forgot_password_username).send_keys("Admin")

    def reset_Password_button(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, self.reset_Password_XPATH).click()

    def reset_Password_output(self):
        self.driver.implicitly_wait(5)
        output = self.driver.find_element(By.XPATH, self.reset_Password_Output_XPATH).text
        assert output == "If the email does not arrive, please contact your OrangeHRM Administrator."

    def cancel_button_click(self):
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.XPATH, self.cancel_Button).click()
