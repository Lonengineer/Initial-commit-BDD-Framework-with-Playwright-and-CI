"""
Screenshot Helper Module
=========================
Captures and saves screenshots for test reporting.
Screenshots are saved to the screenshots/ directory with timestamps.
"""

import os
from datetime import datetime
from utilities.logger import Logger


class ScreenshotHelper:
    """Utility class for capturing browser screenshots."""

    logger = Logger.get_logger()

    # Screenshots directory path
    SCREENSHOT_DIR = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "screenshots"
    )

    @classmethod
    def take_screenshot(cls, driver, name="screenshot"):
        """
        Capture a screenshot and save it to the screenshots directory.

        Args:
            driver: WebDriver instance
            name: Name for the screenshot file

        Returns:
            str: Full path to the saved screenshot
        """
        # Create screenshots directory if it doesn't exist
        os.makedirs(cls.SCREENSHOT_DIR, exist_ok=True)

        # Create filename with timestamp to avoid overwrites
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        # Clean the name to remove invalid filename characters
        clean_name = "".join(c if c.isalnum() or c in "_-" else "_" for c in name)
        filename = f"{clean_name}_{timestamp}.png"
        filepath = os.path.join(cls.SCREENSHOT_DIR, filename)

        try:
            driver.save_screenshot(filepath)
            cls.logger.info(f"Screenshot saved: {filepath}")
            return filepath
        except Exception as e:
            cls.logger.error(f"Failed to capture screenshot: {e}")
            return None
