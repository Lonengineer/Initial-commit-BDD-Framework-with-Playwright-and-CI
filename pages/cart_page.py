"""
Cart Page Module
=================
Page Object for the SauceDemo shopping cart page.
Handles viewing cart items, removing items, and proceeding to checkout.
"""

from pages.base_page import BasePage


class CartPage(BasePage):
    """Page Object for the SauceDemo cart page (/cart.html)."""

    # ---- Locators ----
    CART_ITEMS = "[data-test='inventory-item']"
    CART_ITEM_NAMES = "[data-test='inventory-item-name']"
    REMOVE_BUTTONS = "button[data-test^='remove']"
    CHECKOUT_BUTTON = "[data-test='checkout']"
    CONTINUE_SHOPPING_BUTTON = "[data-test='continue-shopping']"
    PAGE_TITLE = "[data-test='title']"

    # ---- Page Actions ----

    def get_cart_item_names(self):
        """
        Get the names of all items in the cart.

        Returns:
            list: List of item name strings
        """
        return self.get_texts(self.CART_ITEM_NAMES)

    def get_cart_item_count(self):
        """
        Get the number of items currently in the cart.

        Returns:
            int: Number of items in the cart
        """
        return self.page.locator(self.CART_ITEMS).count()

    def remove_item_by_index(self, index=0):
        """
        Remove an item from the cart by index.

        Args:
            index: Zero-based index of the item to remove (default: 0)
        """
        remove_buttons = self.page.locator(self.REMOVE_BUTTONS)
        if index < remove_buttons.count():
            remove_buttons.nth(index).click()
            self.logger.info(f"Removed cart item at index {index}.")

    def remove_all_items(self):
        """Remove all items from the cart one by one."""
        remove_buttons = self.page.locator(self.REMOVE_BUTTONS)
        while remove_buttons.count() > 0:
            remove_buttons.first.click()
            self.logger.info("Removed an item from cart.")
            
        self.logger.info("All items removed from cart.")

    def is_cart_empty(self):
        """
        Check if the cart has no items.

        Returns:
            bool: True if cart is empty
        """
        return self.get_cart_item_count() == 0

    def click_checkout(self):
        """Click the Checkout button to proceed to checkout."""
        self.click(self.CHECKOUT_BUTTON)
        self.logger.info("Clicked Checkout button.")

    def click_continue_shopping(self):
        """Click Continue Shopping to go back to products page."""
        self.click(self.CONTINUE_SHOPPING_BUTTON)
        self.logger.info("Clicked Continue Shopping.")
