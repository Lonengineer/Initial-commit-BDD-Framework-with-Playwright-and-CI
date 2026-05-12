"""
Configuration Reader Module
============================
Reads configuration settings from the config/config.json file.
Provides easy access to all framework settings like URLs, timeouts, and credentials.
"""

import json
import os


class ConfigReader:
    """
    Reads and provides access to configuration settings.
    Uses a class-level cache so the config file is only read once.
    """

    _config = None
    _config_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "config",
        "config.json"
    )

    @classmethod
    def _load_config(cls):
        """Load configuration from JSON file (cached after first read)."""
        if cls._config is None:
            with open(cls._config_path, "r") as config_file:
                cls._config = json.load(config_file)
        return cls._config

    @classmethod
    def get_base_url(cls):
        """Get the base URL of the application."""
        return cls._load_config()["base_url"]

    @classmethod
    def get_browser(cls):
        """Get the browser type (e.g., 'chrome')."""
        return cls._load_config()["browser"]

    @classmethod
    def get_implicit_wait(cls):
        """Get implicit wait timeout in seconds."""
        return cls._load_config()["implicit_wait"]

    @classmethod
    def get_explicit_wait(cls):
        """Get explicit wait timeout in seconds."""
        return cls._load_config()["explicit_wait"]

    @classmethod
    def get_username(cls):
        """Get default username for login."""
        return cls._load_config()["username"]

    @classmethod
    def get_password(cls):
        """Get default password for login."""
        return cls._load_config()["password"]

    @classmethod
    def is_screenshot_on_failure(cls):
        """Check if screenshots should be taken on failure."""
        return cls._load_config()["screenshot_on_failure"]

    @classmethod
    def is_headless(cls):
        """Check if browser should run in headless mode."""
        return cls._load_config()["headless"]

    @classmethod
    def get_config(cls):
        """Get the full configuration dictionary."""
        return cls._load_config()
