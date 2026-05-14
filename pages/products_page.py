"""
Products Page Module
=====================
Page Object for the SauceDemo products/inventory page.
Handles product listing, sorting, adding to cart, and cart badge interactions.
"""

from pages.base_page import BasePage


class ProductsPage(BasePage):
    """Page Object for the SauceDemo products page (/inventory.html)."""

    # ---- Locators ----
    PAGE_TITLE = "[data-test='title']"
    SORT_DROPDOWN = "[data-test='product-sort-container']"
    PRODUCT_NAMES = "[data-test='inventory-item-name']"
    PRODUCT_PRICES = "[data-test='inventory-item-price']"
    ADD_TO_CART_BUTTONS = "button[data-test^='add-to-cart']"
    REMOVE_BUTTONS = "button[data-test^='remove']"
    CART_BADGE = "[data-test='shopping-cart-badge']"
    CART_LINK = "[data-test='shopping-cart-link']"
    INVENTORY_ITEMS = "[data-test='inventory-item']"

    # ---- Sorting Methods ----

    def select_sort_option(self, option_text):
        """
        Select a sorting option from the sort dropdown.

        Args:
            option_text: Visible text of the option, e.g. "Name (A to Z)"
        """
        self.page.locator(self.SORT_DROPDOWN).select_option(label=option_text)
        self.logger.info(f"Selected sort option: '{option_text}'")

    def get_product_names(self):
        """
        Get the names of all products currently displayed.

        Returns:
            list: List of product name strings
        """
        return self.get_texts(self.PRODUCT_NAMES)

    def get_product_prices(self):
        """
        Get the prices of all products currently displayed.
        Prices are returned as float values (without the '$' sign).

        Returns:
            list: List of product prices as floats
        """
        price_texts = self.get_texts(self.PRODUCT_PRICES)
        # Remove the '$' sign and convert to float
        return [float(price.replace("$", "")) for price in price_texts]

    # ---- Cart Interaction Methods ----

    def add_product_to_cart_by_index(self, index=0):
        """
        Add a product to the cart by its index position on the page.

        Args:
            index: Zero-based index of the product (default: 0 = first product)
        """
        add_buttons = self.page.locator(self.ADD_TO_CART_BUTTONS)
        if index < add_buttons.count():
            add_buttons.nth(index).click()
            self.logger.info(f"Added product at index {index} to cart.")
        else:
            self.logger.error(f"No 'Add to Cart' button found at index {index}.")

    def get_product_button_text_by_index(self, index=0):
        """
        Get the text of the button (Add to cart / Remove) for a product.
        
        Args:
            index: Zero-based index of the product
        Returns:
            str: The button text
        """
        button = self.page.locator(self.INVENTORY_ITEMS).nth(index).locator("button")
        return button.inner_text()

    def add_multiple_products_to_cart(self, count=2):
        """
        Add multiple products to the cart.

        Args:
            count: Number of products to add (default: 2)
        """
        for i in range(count):
            add_button = self.page.locator(self.ADD_TO_CART_BUTTONS).first
            if add_button.is_visible():
                add_button.click()
                self.logger.info(f"Added product #{i + 1} to cart.")
            else:
                self.logger.warning(f"No more 'Add to Cart' buttons available after {i} products.")
                break

    def remove_product_by_index(self, index=0):
        """
        Remove a product from the cart by clicking its Remove button.

        Args:
            index: Zero-based index of the Remove button (default: 0)
        """
        remove_buttons = self.page.locator(self.REMOVE_BUTTONS)
        if index < remove_buttons.count():
            remove_buttons.nth(index).click()
            self.logger.info(f"Removed product at index {index} from cart.")
        else:
            self.logger.error(f"No 'Remove' button found at index {index}.")

    def remove_all_products_from_cart(self):
        """Remove all products that have been added to the cart."""
        remove_buttons = self.page.locator(self.REMOVE_BUTTONS)
        while remove_buttons.count() > 0:
            remove_buttons.first.click()
            self.logger.info("Removed a product from cart.")
        self.logger.info("All products removed from cart.")

    def get_cart_badge_count(self):
        """
        Get the number displayed on the cart badge.

        Returns:
            int: Number of items shown on the cart badge, or 0 if badge is not visible
        """
        if self.is_cart_badge_displayed():
            badge_text = self.get_text(self.CART_BADGE)
            return int(badge_text)
        return 0

    def is_cart_badge_displayed(self):
        """
        Check if the cart badge is visible.

        Returns:
            bool: True if cart badge is displayed
        """
        return self.is_element_displayed(self.CART_BADGE, timeout=500)

    def go_to_cart(self):
        """Click the cart icon to navigate to the cart page."""
        self.click(self.CART_LINK)
        self.logger.info("Navigated to cart page.")

    def get_page_header_text(self):
        """Get the text of the page title/header."""
        return self.get_text(self.PAGE_TITLE)
