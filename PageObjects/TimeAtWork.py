from selenium.webdriver.common.by import By


class Time_at_work:
    heading = "//p[normalize-space()='Time at Work']"
    bi_stopwatch = "//button[@class='oxd-icon-button oxd-icon-button--solid-main orangehrm-attendance-card-action']"
    heading_punch_in = "//h6[normalize-space()='Punch In']"
    punch_date_input = "//input[@placeholder='yyyy-mm-dd']"
    calender = "//div[@class='oxd-date-input']"
    punch_time_input = "//i[@class='oxd-icon bi-clock oxd-time-input--clock']"
    time_hour = "//input[@class='oxd-input oxd-input--active oxd-time-hour-input-text']"
    time_minute = "//input[@class='oxd-input oxd-input--active oxd-time-minute-input-text']"
    time_hour_max_btn = "//i[@class='oxd-icon bi-chevron-up oxd-icon-button__icon oxd-time-hour-input-up']"
    time_minute_max_btn = "//i[@class='oxd-icon bi-chevron-up oxd-icon-button__icon oxd-time-minute-input-up']"
    note_input = "//textarea[@placeholder='Type here']"
    in_btn = "//button[normalize-space()='In']"
    out_btn = "//button[normalize-space()='Out']"
    heading_punch_out = "//h6[normalize-space()='Punch Out']"
    in_time="//body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-paper-container']/form[@class='oxd-form']/div[1]/div[1]/div[1]/div[1]/div[1]"

    def __init__(self, driver):
        self.driver = driver

    def heading(self):
        title_heading = self.driver.find_element(By.XPATH, self.heading).text
        assert title_heading == "Time at Work"
        print(title_heading)

    def stopwatch_button(self):
        self.driver.find_element(By.XPATH, self.bi_stopwatch).click()

    def attendance_punch_in(self):
        punch_in = self.driver.find_element(By.XPATH, self.heading_punch_in).text()
        print(punch_in)
        # self.driver.find_element(By.XPATH, self.punch_date_input).send_keys("2023-06-16")
        # self.driver.find_element(By.XPATH, self.punch_time_input).click()
        # self.driver.find_element(By.XPATH, self.time_hour_max_btn).click()
        # self.driver.find_element(By.XPATH, self.time_minute_max_btn).click()
        self.driver.find_element(By.XPATH, self.note_input).send_keys("My time input is current time")
        self.driver.find_element(By.XPATH, self.in_btn).click()

    def attendance_punch_out(self):
        punch_out = self.driver.find_element(By.XPATH, self.heading_punch_out).text()
        print(punch_out)
        self.driver.find_element(By.XPATH, self.punch_date_input).send_keys("2023-06-16")
        self.driver.find_element(By.XPATH, self.time_minute_max_btn).click()
        self.driver.find_element(By.XPATH, self.time_minute_max_btn).click()
        self.driver.find_element(By.XPATH, self.note_input).send_keys("My time input is current time")
        self.driver.find_element(By.XPATH, self.out_btn).click()
