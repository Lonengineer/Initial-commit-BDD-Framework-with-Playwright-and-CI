"""
Behave Environment Hooks
=========================
Contains setup and teardown hooks for the Behave test framework.
Handles Playwright browser lifecycle, screenshot capture, and Allure reporting.
"""

import os
import sys
import allure
from playwright.sync_api import sync_playwright

# Add project root to Python path so imports work correctly
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from utilities.logger import Logger
from utilities.config_reader import ConfigReader


def before_all(context):
    """
    Runs once before all tests.
    Sets up the logger and starts Playwright.
    """
    context.logger = Logger.get_logger()
    context.logger.info("=" * 60)
    context.logger.info("TEST SESSION STARTED")
    context.logger.info("=" * 60)
    
    # Start Playwright globally
    context.playwright_mgr = sync_playwright()
    context.playwright = context.playwright_mgr.__enter__()


def before_scenario(context, scenario):
    """
    Runs before each test scenario.
    Creates a new browser instance for each scenario.
    """
    context.logger.info(f"--- Starting Scenario: {scenario.name} ---")

    config = ConfigReader.get_config()
    browser_name = config.get("browser", "chrome").lower()
    headless = config.get("headless", True)
    
    # Set up slow_mo if slow_mode is enabled
    slow_mo = 0
    if config.get("slow_mode", False):
        # Convert step_delay from seconds to ms, default 1000ms
        slow_mo = int(config.get("step_delay", 1) * 1000)

    context.logger.info(f"Launching {browser_name} (headless={headless}, slow_mo={slow_mo}ms)")
    
    # Launch browser
    # Playwright supports chromium, firefox, webkit. For 'chrome', we use chromium channel.
    if browser_name == "chrome":
        context.browser = context.playwright.chromium.launch(headless=headless, channel="chrome", slow_mo=slow_mo)
    elif browser_name in ["chromium", "firefox", "webkit"]:
        context.browser = getattr(context.playwright, browser_name).launch(headless=headless, slow_mo=slow_mo)
    else:
        context.logger.warning(f"Browser '{browser_name}' not natively supported, defaulting to chromium")
        context.browser = context.playwright.chromium.launch(headless=headless, slow_mo=slow_mo)

    # Create a new incognito browser context and page
    context.browser_context = context.browser.new_context(viewport={"width": 1920, "height": 1080})
    context.page = context.browser_context.new_page()
    context.logger.info("Browser launched for scenario.")


def after_scenario(context, scenario):
    """
    Runs after each test scenario.
    Captures screenshots on failure and closes the browser.
    """
    if scenario.status == "failed":
        context.logger.error(f"SCENARIO FAILED: {scenario.name}")

        if ConfigReader.is_screenshot_on_failure() and hasattr(context, 'page'):
            # Save screenshot to file
            safe_name = scenario.name.replace(" ", "_").replace("/", "_")
            screenshots_dir = os.path.join(project_root, "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshots_dir, f"{safe_name}.png")
            
            try:
                context.page.screenshot(path=screenshot_path, full_page=True)
                
                # Attach screenshot to Allure report
                with open(screenshot_path, "rb") as image_file:
                    allure.attach(
                        image_file.read(),
                        name=f"Failure Screenshot - {scenario.name}",
                        attachment_type=allure.attachment_type.PNG
                    )
                context.logger.info("Screenshot attached to Allure report.")
            except Exception as e:
                context.logger.error(f"Failed to capture screenshot: {e}")
    else:
        context.logger.info(f"SCENARIO PASSED: {scenario.name}")

    # Close the browser after each scenario
    if hasattr(context, 'browser_context'):
        context.browser_context.close()
    if hasattr(context, 'browser'):
        context.browser.close()
        context.logger.info("Browser closed.")

    context.logger.info(f"--- Finished Scenario: {scenario.name} ---\n")


def after_all(context):
    """
    Runs once after all tests are complete.
    Stops Playwright and logs the end.
    """
    if hasattr(context, 'playwright_mgr'):
        context.playwright_mgr.__exit__(None, None, None)
        
    context.logger.info("=" * 60)
    context.logger.info("TEST SESSION COMPLETED")
    context.logger.info("=" * 60)
