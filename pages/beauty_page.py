from pages.base_page import BasePage

class BeautyPage(BasePage):
    BEAUTY_MENU = ("id", "beauty")

    BEAUTY_OPTIONS = {
        "beauty": ("css selector", "ul>li:nth-of-type(2)>a[href='/beauty']"),
        "makeup": ("css selector", "a[href='/sub-category/makeup']"),
        "skincare": ("css selector", "a[href='/sub-category/skincare']"),

    }

    FIRST_PRODUCT = ("css selector", "div.MuiPaper-root:nth-of-type(1)")
    PRODUCT_NAME = ("css selector", "div[class^='ProductDisplay_productBrand']")
    ADD_TO_CART_BUTTON = ("id", "Add To Cart")

    def open_url(self, base_url):
        self.get_url(base_url)

    def hover_beauty_menu(self):
        self.move_to_element(self.BEAUTY_MENU)

    def click_first_product(self):
        self.click_element(self.FIRST_PRODUCT)

    def click_beauty_options(self):
        for option_name, locator in self.BEAUTY_OPTIONS.items():
            self.click_element(locator)
            assert self.find_element(self.FIRST_PRODUCT).is_displayed(), \
                f"No products displayed for option: {option_name}"

    def click_add_to_cart_button(self):
        self.click_element(self.ADD_TO_CART_BUTTON)