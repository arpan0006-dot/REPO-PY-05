from page.base_page import BasePage
from time import sleep


class BeautyPage(BasePage):

    BEAUTY_MENU = ("id", "beauty")

    BEAUTY_OPTIONS = {
        "beauty": ("css selector", "a[href='/beauty']"),
        "makeup": ("css selector", "a[href='/sub-category/makeup']"),
        "skincare": ("css selector", "a[href='/sub-category/skincare']")
    }

    FIRST_PRODUCT = ("css selector", "div.MuiPaper-root:nth-of-type(1)")
    ALL_PRODUCT = ("css selector", "div.MuiPaper-root")
    PRODUCT_NAME = ("css selector", "div[class^='ProductDisplay_productBrand']")
    ADD_TO_CART_BUTTON = ("id", "Add To Cart")

    def open_url(self, base_url):
        self.get_url(base_url)

    def hover_beauty_menu(self):
        self.move_to_element(self.BEAUTY_MENU)

    def click_first_product(self):
        self.click_element(self.FIRST_PRODUCT)

    def click_add_to_cart_button(self):
        self.click_element(self.ADD_TO_CART_BUTTON)

    # -----------------------------------------

    def click_all_beauty_options(self):
        for option_name, locator in self.BEAUTY_OPTIONS.items():

            sleep(1)
            self.hover_beauty_menu()

            sleep(1)
            self.click_element(locator)

            sleep(2)  # give unstable site time to load products

            assert self.find_element(
                self.FIRST_PRODUCT
            ).is_displayed(), f"No products displayed for option: {option_name}"

    # -----------------------------------------

    def click_first_product_of_all_options(self):
        for option_name, locator in self.BEAUTY_OPTIONS.items():

            sleep(1)
            self.hover_beauty_menu()

            sleep(1)
            self.click_element(locator)

            sleep(2)

            assert self.find_element(
                self.FIRST_PRODUCT
            ).is_displayed(), f"No products displayed for option: {option_name}"

            self.click_first_product()

            sleep(2)

            product_name = self.get_text(self.PRODUCT_NAME)

            assert product_name.strip() != "", \
                f"First {option_name} product info is not visible"

            sleep(1)
            self.driver.back()
            sleep(2)