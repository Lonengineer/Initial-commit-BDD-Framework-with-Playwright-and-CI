"""
Checkout Page Module
=====================
Page Object for the SauceDemo checkout pages.
Handles the multi-step checkout process: information, overview, and completion.
"""

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    """Page Object for the SauceDemo checkout pages."""

    # ---- Step One: Your Information ----
    FIRST_NAME_INPUT = "[data-test='firstName']"
    LAST_NAME_INPUT = "[data-test='lastName']"
    POSTAL_CODE_INPUT = "[data-test='postalCode']"
    CONTINUE_BUTTON = "[data-test='continue']"
    CANCEL_BUTTON = "[data-test='cancel']"
    CHECKOUT_ERROR = "[data-test='error']"

    # ---- Step Two: Overview ----
    FINISH_BUTTON = "[data-test='finish']"
    SUMMARY_TOTAL = "[data-test='total-label']"

    # ---- Complete ----
    COMPLETE_HEADER = "[data-test='complete-header']"
    COMPLETE_TEXT = "[data-test='complete-text']"
    BACK_HOME_BUTTON = "[data-test='back-to-products']"

    # ---- Page Title ----
    PAGE_TITLE = "[data-test='title']"

    # ---- Step One Actions ----

    def enter_first_name(self, first_name):
        """Enter first name in the checkout form."""
        self.type_text(self.FIRST_NAME_INPUT, first_name)

    def enter_last_name(self, last_name):
        """Enter last name in the checkout form."""
        self.type_text(self.LAST_NAME_INPUT, last_name)

    def enter_postal_code(self, postal_code):
        """Enter postal/zip code in the checkout form."""
        self.type_text(self.POSTAL_CODE_INPUT, postal_code)

    def fill_checkout_information(self, first_name, last_name, postal_code):
        """
        Fill in all checkout information fields.

        Args:
            first_name: Customer first name
            last_name: Customer last name
            postal_code: Customer postal/zip code
        """
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)
        self.logger.info("Filled checkout information form.")

    def click_continue(self):
        """Click the Continue button to proceed to overview."""
        self.click(self.CONTINUE_BUTTON)
        self.logger.info("Clicked Continue on checkout form.")

    def click_cancel(self):
        """Click the Cancel button to go back."""
        self.click(self.CANCEL_BUTTON)
        self.logger.info("Clicked Cancel on checkout form.")

    def get_checkout_error_message(self):
        """
        Get the error message displayed on the checkout form.

        Returns:
            str: Error message text
        """
        return self.get_text(self.CHECKOUT_ERROR)

    # ---- Step Two Actions ----

    def click_finish(self):
        """Click the Finish button to complete the order."""
        self.click(self.FINISH_BUTTON)
        self.logger.info("Clicked Finish to complete order.")

    # ---- Complete Page Actions ----

    def get_complete_header(self):
        """
        Get the order completion header text.

        Returns:
            str: Completion header text (e.g., "Thank you for your order!")
        """
        return self.get_text(self.COMPLETE_HEADER)

    def get_complete_text(self):
        """
        Get the order completion description text.

        Returns:
            str: Completion description text
        """
        return self.get_text(self.COMPLETE_TEXT)

    def is_checkout_complete(self):
        """
        Check if the checkout has been completed successfully.

        Returns:
            bool: True if the completion header is displayed
        """
        return self.is_element_displayed(self.COMPLETE_HEADER, timeout=10000)

    def click_back_home(self):
        """Click Back Home button to return to products page."""
        self.click(self.BACK_HOME_BUTTON)
        self.logger.info("Clicked Back Home button.")
