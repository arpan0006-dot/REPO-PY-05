from page.base_page import BasePage
from time import sleep


class ElectronicPage(BasePage):
    ELECTRONIC_MENU = ("id", "electronics")
    ELECTRONICS_OPTIONS = {
        # "electronics": ("css selector", "ul>li:nth-of-type(1)>a[href='/electronics']"),
        "camera": ("css selector", "a[href='/sub-category/camera']"),
        "usb_and_accessories": ("css selector", "a[href='/sub-category/electronic-accessories']"),
        "watch": ("css selector", "a[href='/sub-category/watch']"),
        # "hard_drive": ("css selector", "a[href='/sub-category/hard-drive']"),
        "headphones": ("css selector", "a[href='/sub-category/headphones']"),
        "laptop": ("css selector", "a[href='/sub-category/laptop']"),
        "mobile": ("css selector", "a[href='/sub-category/mobile']"),
        "power_bank": ("css selector", "a[href='/sub-category/power-bank']")
    }

    FIRST_PRODUCT = ("css selector", "div.MuiPaper-root:nth-of-type(1)")
    ALL_PRODUCT = ("css selector", "div.MuiPaper-root")
    PRODUCT_NAME = ("css selector", "div[class^='ProductDisplay_productBrand']")
    ADD_TO_CART_BUTTON = ("id", "Add To Cart")

    def open_url(self, base_url):
        self.get_url(base_url)

    def hover_electronic_menu(self):
        self.move_to_element(self.ELECTRONIC_MENU)

    def click_electronic_menu(self):
        self.click_element(self.ELECTRONIC_MENU)

    def click_camera_option(self):
        self.click_element(self.ELECTRONICS_OPTIONS["camera"])

    def click_first_product(self):
        self.click_element(self.FIRST_PRODUCT)

    def click_add_to_cart_button(self):
        self.click_element(self.ADD_TO_CART_BUTTON)

    def click_all_electronic_options(self):
        for option_name, locator in self.ELECTRONICS_OPTIONS.items():
            sleep(1)
            self.hover_electronic_menu()
            sleep(1)
            self.click_element(locator)
            assert self.find_element(
                self.FIRST_PRODUCT).is_displayed(), f"No products displayed for option: {option_name}"

    def click_fist_product_of_all_options(self):
        for option_name, locator in self.ELECTRONICS_OPTIONS.items():
            sleep(1)
            self.hover_electronic_menu()
            sleep(1)
            self.click_element(locator)
            assert self.find_element(
                self.FIRST_PRODUCT).is_displayed(), f"No products displayed for option: {option_name}"
            self.click_first_product()
            sleep(1)
            product_name = self.get_text(ElectronicPage.PRODUCT_NAME)
            assert product_name.strip() != "", f"First {option_name} product info is not visible"

    def click_all_product_of_camera(self):
        self.click_electronic_menu()
        self.click_camera_option()
        assert self.find_element(self.FIRST_PRODUCT).is_displayed(), f"No products displayed for option Camera"
        cameras_count = len(self.find_elements(self.ALL_PRODUCT))
        for i in range(cameras_count):
            all_cameras = self.find_elements(self.ALL_PRODUCT)
            camera = all_cameras[i]
            if camera.is_enabled():
                camera.click()
                product_name = self.get_text(ElectronicPage.PRODUCT_NAME)
                assert product_name.strip() != "", "Product info is not visible"
                self.driver.back()
