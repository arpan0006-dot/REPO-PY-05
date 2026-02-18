from selenium.webdriver.common.by import By
from page.base_page import BasePage

class WishlistPage(BasePage):

    ADD_TO_WISHLIST = (By.ID, "addToWishlist")
    WISHLIST_ICON = (By.ID, "wishlistIcon")
    REMOVE_FROM_WISHLIST = (By.CLASS_NAME, "remove-wishlist")
    EMPTY_WISHLIST_MSG = (By.CLASS_NAME, "empty-wishlist")
    MOVE_TO_CART = (By.CLASS_NAME, "move-to-cart")

    def add_to_wishlist(self):
        self.click(self.ADD_TO_WISHLIST)

    def open_wishlist(self):
        self.click(self.WISHLIST_ICON)

    def remove_from_wishlist(self):
        self.click(self.REMOVE_FROM_WISHLIST)

    def move_product_to_cart(self):
        self.click(self.MOVE_TO_CART)

    def is_wishlist_empty(self):
        return self.is_visible(self.EMPTY_WISHLIST_MSG)
