
from page.beauty_page import BeautyPage
from test.base_test import BaseTest

class TestBeauty(BaseTest):

    def test_all_beauty_options_display_products(self):
        beauty_page = BeautyPage(self.driver)
        beauty_page.open_url(self.config["base_url"])
        beauty_page.hover_beauty_menu()
        beauty_page.click_beauty_options()

    def test_first_beauty_product_info_visible(self):
        beauty_page = BeautyPage(self.driver)
        beauty_page.open_url(self.config["base_url"])
        beauty_page.hover_beauty_menu()
        beauty_page.click_first_product()
        product_name = beauty_page.get_text(BeautyPage.PRODUCT_NAME)
        assert product_name.strip() != "", "First beauty product info is not visible"

    def test_add_to_cart(self):
        beauty_page = BeautyPage(self.driver)
        beauty_page.open_url(self.config["base_url"])
        beauty_page.hover_beauty_menu()
        beauty_page.click_first_product()
        beauty_page.click_add_to_cart_button()
        cart_badge = beauty_page.find_element(("css selector", "span.cart-count"))
        assert int(cart_badge.text) > 0, "Beauty product was not added to cart"