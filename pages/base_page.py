"""
Base Page Module
=================
Contains the BasePage class which serves as the parent class for all Page Objects.
It provides common wrapper methods around Playwright Page actions.
Playwright automatically waits for elements to be actionable, drastically simplifying this.
"""

from utilities.logger import Logger
from utilities.config_reader import ConfigReader

class BasePage:
    """
    Base class for all Page Objects.
    Provides common Playwright interaction methods.
    """

    def __init__(self, page):
        """
        Initialize the BasePage with a Playwright Page instance.

        Args:
            page: Playwright Page object
        """
        self.page = page
        self.logger = Logger.get_logger()
        self.base_url = ConfigReader.get_base_url()

    def navigate(self, url):
        """
        Navigate to a specific URL.

        Args:
            url: The URL to navigate to
        """
        self.page.goto(url)
        self.logger.info(f"Navigated to: {url}")

    def find_element(self, selector):
        """
        Find a single element.

        Args:
            selector: CSS or XPath selector string

        Returns:
            Locator: Playwright Locator object
        """
        return self.page.locator(selector).first

    def find_elements(self, selector):
        """
        Find multiple elements.

        Args:
            selector: CSS or XPath selector string

        Returns:
            Locator: Playwright Locator object (can be counted or iterated)
        """
        return self.page.locator(selector)

    def click(self, selector):
        """
        Wait for an element to be actionable and click it.

        Args:
            selector: CSS or XPath selector string
        """
        self.page.locator(selector).first.click()
        self.logger.debug(f"Clicked element: {selector}")

    def type_text(self, selector, text):
        """
        Fill text into an element.

        Args:
            selector: CSS or XPath selector string
            text: Text to type into the element
        """
        self.page.locator(selector).first.fill(text)
        self.logger.debug(f"Typed '{text}' into element: {selector}")

    def get_text(self, selector):
        """
        Get the visible text of an element.

        Args:
            selector: CSS or XPath selector string

        Returns:
            str: Text content of the element
        """
        return self.page.locator(selector).first.text_content().strip()

    def get_texts(self, selector):
        """
        Get the text of all matching elements.

        Args:
            selector: CSS or XPath selector string

        Returns:
            list: List of text strings
        """
        return self.page.locator(selector).all_text_contents()

    def is_element_displayed(self, selector, timeout=3000):
        """
        Check if an element is visible on the page within a timeout.

        Args:
            selector: CSS or XPath selector string
            timeout: Maximum time to wait in milliseconds (default: 3000ms)

        Returns:
            bool: True if element is visible, False otherwise
        """
        try:
            self.page.locator(selector).first.wait_for(state="visible", timeout=timeout)
            return True
        except Exception:
            return False

    def is_element_enabled(self, selector):
        """
        Check if an element is enabled.

        Args:
            selector: CSS or XPath selector string

        Returns:
            bool: True if element is enabled, False otherwise
        """
        return self.page.locator(selector).first.is_enabled()
