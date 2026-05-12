"""
Login Page Module
==================
Page Object for the SauceDemo login page.
Handles user authentication as a prerequisite step for tests.
"""

from pages.base_page import BasePage
from utilities.config_reader import ConfigReader


class LoginPage(BasePage):
    """Page Object for the SauceDemo login page (https://www.saucedemo.com/)."""

    # ---- Locators ----
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"

    # ---- Page Actions ----

    def open_login_page(self):
        """Navigate to the SauceDemo login page."""
        self.navigate(ConfigReader.get_base_url())
        self.logger.info("Opened SauceDemo login page.")

    def enter_username(self, username):
        """Enter username into the username field."""
        self.type_text(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        """Enter password into the password field."""
        self.type_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        """Click the Login button."""
        self.click(self.LOGIN_BUTTON)

    def login(self, username=None, password=None):
        """
        Perform a complete login with the given or default credentials.

        Args:
            username: Username string (defaults to config value)
            password: Password string (defaults to config value)
        """
        username = username or ConfigReader.get_username()
        password = password or ConfigReader.get_password()

        self.open_login_page()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        self.logger.info(f"Logged in as '{username}'.")

    def get_error_message(self):
        """Get the text of the login error message."""
        return self.get_text(self.ERROR_MESSAGE)
