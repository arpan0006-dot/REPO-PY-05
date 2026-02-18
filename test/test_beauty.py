

from page.beauty_page import BeautyPage
from test.base_test import BaseTest
from time import sleep

class TestBeauty(BaseTest):

    def test_all_beauty_options_display_products(self):
        beauty_page = BeautyPage(self.driver)
        beauty_page.open_url(self.config["base_url"])
        sleep(10)
        beauty_page.click_all_beauty_options()

    # def test_first_beauty_product_info_visible(self):
    #     beauty_page = BeautyPage(self.driver)
    #     beauty_page.open_url(self.config["base_url"])
    #     sleep(10)
    #     beauty_page.click_first_product_of_all_options()