
import pytest
from selenium import webdriver
from page.women_page import WomenPage


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get("https://www.shoppersstack.com/")
    driver.maximize_window()
    yield driver
    driver.quit()


def test_women_add_to_cart(setup):
    driver = setup
    women = WomenPage(driver)

    women.open_women_section()
    women.select_first_product()
    women.add_to_cart()
    women.open_cart()

    product_name = women.verify_product_added_to_cart()
    print("Product Added:", product_name)
