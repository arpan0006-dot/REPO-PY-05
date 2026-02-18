from selenium.webdriver.common.by import By
from page.base_page import BasePage

class Kids_Page(BasePage):
    KIDS=(By.CSS_SELECTOR,'a[href="/kids"]')
    JEANS=(By.LINK_TEXT,"Jeans")
    BLOCKS=(By.XPATH,"//span[contains(text(),'Building Blocks for Kids')]")
    ADD_TO_CART=(By.ID,"Add To Cart")
    CART_ICON=(By.ID,"cartIcon")
    CART_BLOCK=(By.XPATH,"//p[contains(text(),'Building Blocks for Kids')]")
    JEAN_ADD_TO_CART=(By.CSS_SELECTOR,'button[type="button"]')


    def click_kids(self):
        self.find_element(self.KIDS).click()

    def move_to_kids(self):
        self.move_to_element(self.KIDS).click()

    def select_block(self):
        self.find_element(self.BLOCKS).click()

    def select_add_to_cart(self):
        self.find_element(self.ADD_TO_CART).click()

    def add_to_cart(self):
        self.select_block()
        self.select_add_to_cart()

    def click_cart_icon(self):
        self.find_element(self.CART_ICON).click()

    def verify_cart(self):
        return self.find_element(self.CART_BLOCK).text

    def jean_add_to_cart(self):
        self.find_element(self.JEAN_ADD_TO_CART).click()

    def move_to_jeans(self):
        element = self.find_element(self.JEANS)
        self.move_to_element(element).click().perform()

