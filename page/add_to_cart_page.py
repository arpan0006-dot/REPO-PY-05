from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # Locators
    CART_ICON = (By.ID, "cart-icon")
    CART_ITEM_NAME = (By.CSS_SELECTOR, ".cart-item .name")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, ".checkout-btn")

    # Actions
    def open_cart(self):
        # Click the cart icon/button to open cart
        self.wait.until(EC.element_to_be_clickable(self.CART_ICON)).click()

    def get_cart_item_name(self):
        self.wait.until(EC.visibility_of_element_located(self.CART_ITEM_NAME))
        return self.driver.find_element(*self.CART_ITEM_NAME).text

    def is_checkout_enabled(self):
        return self.driver.find_element(*self.CHECKOUT_BUTTON).is_enabled()