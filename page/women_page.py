from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class WomenPage(BasePage):

    WOMEN_TAB = (By.XPATH, "//a[text()='Women']")
    FIRST_PRODUCT = (By.XPATH, "(//div[contains(@class,'product-card')])[1]")
    ADD_TO_CART = (By.XPATH, "//button[text()='Add to cart']")
    CART_ICON = (By.XPATH, "//span[contains(@class,'cart')]")
    CART_PRODUCT = (By.XPATH, "//div[contains(@class,'cart-product')]")

    def open_women_section(self):
        self.click(self.WOMEN_TAB)

    def select_first_product(self):
        self.click(self.FIRST_PRODUCT)

    def add_to_cart(self):
        self.click(self.ADD_TO_CART)

    def open_cart(self):
        self.click(self.CART_ICON)

    def verify_product_added(self):
        return self.get_text(self.CART_PRODUCT)
