from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from page.base_page import BasePage

class LoginPage(BasePage):
    LOGIN=(By.ID,"loginBtn")
    EMAIL=(By.ID,"Email")
    PASSWORD=(By.ID,"Password")
    LOGIN_BUTTON=(By.CSS_SELECTOR ,'span[class="MuiButton-label"]')

    def open_login_page(self,base_url):
        self.get_url(f"{base_url}/practice-test-login/")

    def click_login(self):
        self.find_element(self.LOGIN).click()

    def enter_email(self,email):
        self.send_keys(self.EMAIL,email)
        print(f"Username entered : {email}")

    def enter_password(self,password):
        self.send_keys(self.PASSWORD,password)
        print(f"Username entered : {password}")

    def click_login_button(self):
        self.find_element(self.LOGIN_BUTTON).click()

    def login(self,email,password):
        self.click_login()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

