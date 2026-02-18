import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from page.base_page import BasePage
from page.add_to_cart_page import CartPage

@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()

def test_add_to_cart(driver):
    home = BasePage(driver)
    cart = CartPage(driver)

    # Open site
    home.open()

    # Wait until products are visible
    home.wait_for_products()

    # Capture product title before adding
    product_title = home.get_first_product_title()

    # Add to cart
    home.add_first_product_to_cart()

    # Open cart panel/page
    cart.open_cart()

    # Validate the product in cart matches selected product
    cart_item_name = cart.get_cart_item_name()
    assert product_title == cart_item_name, \
        f"Expected '{product_title}' in cart, but found '{cart_item_name}'"

    # Optional: Assert checkout is available
    assert cart.is_checkout_enabled(), "Checkout button should be enabled after adding to cart"

