import time

from page.login_page import LoginPage
from test.base_test import BaseTest
from page.kids_page import Kids_Page
import pytest


@pytest.mark.smoke
class Test_Kids(BaseTest):
    def test_add_kids_product_to_cart(self):
        # login-click kids-click block -add to cart- go to cart- verigy
        login_page = LoginPage(self.driver)
        login_page.open_login_page(self.config["base_url"])
        login_page.login(self.config["email"], self.config["password"])
        time.sleep(10)
        kp=Kids_Page(self.driver)
        kp.click_kids()
        time.sleep(5)
        assert "kids" in self.driver.current_url
        kp.add_to_cart()
        kp.click_cart_icon()

    def test_invalid_add_kids_product_to_cart(self):
        # add to cart without login
        login_page = LoginPage(self.driver)
        login_page.open_login_page(self.config["base_url"])
        time.sleep(10)
        kp = Kids_Page(self.driver)
        time.sleep(5)
        kp.move_to_kids()
        kp.move_to_jeans()
        assert "girls-jeans" in self.driver.current_url
        kp.jean_add_to_cart()
        assert kp.click_cart_icon().is_displayed(),"add cart not displayed"












