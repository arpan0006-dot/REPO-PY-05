import pytest
from page.wishlist import WishlistPage
# from page.cart_page import CartPage

@pytest.mark.usefixtures("setup")
class TestWishlist:

    def test_add_product_to_wishlist(self):
        wp = WishlistPage(self.driver)
        wp.add_to_wishlist()
        wp.open_wishlist()
        assert "Wishlist" in self.driver.title

    def test_remove_product_from_wishlist(self):
        wp = WishlistPage(self.driver)
        wp.add_to_wishlist()
        wp.open_wishlist()
        wp.remove_from_wishlist()
        assert wp.is_wishlist_empty()

    # def test_move_wishlist_product_to_cart(self):
    #     wp = WishlistPage(self.driver)
    #     # cp = CartPage(self.driver)
    #
    #     wp.add_to_wishlist()
    #     wp.open_wishlist()
    #     wp.move_product_to_cart()
    #     cp.open_cart()
    #
    #     assert "Cart" in self.driver.title
