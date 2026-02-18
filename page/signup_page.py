import time
from selenium.webdriver.common.by import By

class SignupPage:

    def __init__(self, driver):
        self.driver = driver

        # ⚠ These locators must match actual website (inspect and adjust if needed)
        self.first_name = (By.XPATH, "//input[@name='First Name']")
        self.last_name = (By.XPATH, "////input[@name='Last Name']")
        self.email = (By.XPATH, "//input[@type='email']")
        self.phone = (By.XPATH, "//input[@type='tel']")
        self.password = (By.XPATH, "(//input[@type='password'])[1]")
        self.confirm_password = (By.XPATH, "(//input[@type='password'])[2]")

        self.gender_male = (By.XPATH, "//input[@value='Male']")
        self.gender_female = (By.XPATH, "//input[@value='Female']")

        self.terms_checkbox = (By.XPATH, "//input[@type='checkbox']")
        self.signup_button = (By.XPATH, "//button[contains(text(),'Sign Up')]")

    def load(self):
        self.driver.get("https://www.shoppersstack.com/signup")
        time.sleep(3)

    def enter_first_name(self, value):
        self.driver.find_element(*self.first_name).send_keys(value)
        time.sleep(1)

    def enter_last_name(self, value):
        self.driver.find_element(*self.last_name).send_keys(value)
        time.sleep(1)

    def enter_email(self, value):
        self.driver.find_element(*self.email).send_keys(value)
        time.sleep(1)

    def enter_phone(self, value):
        self.driver.find_element(*self.phone).send_keys(value)
        time.sleep(1)

    def enter_password(self, value):
        self.driver.find_element(*self.password).send_keys(value)
        time.sleep(1)

    def enter_confirm_password(self, value):
        self.driver.find_element(*self.confirm_password).send_keys(value)
        time.sleep(1)

    def select_gender(self, gender):
        if gender.lower() == "male":
            self.driver.find_element(*self.gender_male).click()
        elif gender.lower() == "female":
            self.driver.find_element(*self.gender_female).click()
        time.sleep(1)

    def accept_terms(self):
        self.driver.find_element(*self.terms_checkbox).click()
        time.sleep(1)

    def click_signup(self):
        self.driver.find_element(*self.signup_button).click()
        time.sleep(3)