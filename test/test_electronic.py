import pytest
from page.electronic_page import ElectronicPage
from test.base_test import BaseTest
from time import sleep


class TestElectronic(BaseTest):

    def test_all_electronic_options_display_products(self):
        electronic_page = ElectronicPage(self.driver)
        electronic_page.open_url(self.config["base_url"])
        sleep(10)
        electronic_page.click_all_electronic_options()

    def test_first_electronic_product_info_visible(self):
        electronic_page = ElectronicPage(self.driver)
        electronic_page.open_url(self.config["base_url"])
        sleep(10)
        electronic_page.click_fist_product_of_all_options()

    def test_add_to_cart_without_login(self):
        electronic_page = ElectronicPage(self.driver)
        electronic_page.open_url(self.config["base_url"])
        sleep(10)
        electronic_page.click_electronic_menu()
        electronic_page.click_camera_option()
        electronic_page.click_first_product()
        electronic_page.click_add_to_cart_button()
        assert "user-signin" in self.driver.current_url, "Electronic product was not added to cart"

    def test_every_product_of_camera(self):
        electronic_page = ElectronicPage(self.driver)
        electronic_page.open_url(self.config["base_url"])
        sleep(10)
        electronic_page.click_all_product_of_camera()
