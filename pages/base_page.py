from datetime import datetime
from pathlib import Path

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

from utils.config_reader import config
from utils.logger import get_logger

logger = get_logger(__name__)


class BasePage:

    """
    BasePage provides reusable Selenium operations
    for all page objects.
    """

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(
            self.driver,
            config.get_int("timeouts", "explicit_wait")
        )

    # ==========================================
    # FIND ELEMENT
    # ==========================================

    def find_element(self, locator):

        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

    # ==========================================
    # FIND MULTIPLE ELEMENTS
    # ==========================================

    def find_elements(self, locator):

        return self.driver.find_elements(*locator)

    # ==========================================
    # WAIT FOR VISIBILITY
    # ==========================================

    def wait_for_visible(self, locator):

        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    # ==========================================
    # CLICK ELEMENT
    # ==========================================

    def click(self, locator):

        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        element.click()

        logger.info(f"Clicked element: {locator}")

    # ==========================================
    # ENTER TEXT
    # ==========================================

    def type_text(self, locator, text, clear=True):

        element = self.wait_for_visible(locator)

        if clear:
            element.clear()

        element.send_keys(text)

        logger.info(f"Entered text into: {locator}")

    # ==========================================
    # GET TEXT
    # ==========================================

    def get_text(self, locator):

        element = self.wait_for_visible(locator)

        return element.text

    # ==========================================
    # GET ATTRIBUTE
    # ==========================================

    def get_attribute(self, locator, attribute):

        element = self.find_element(locator)

        return element.get_attribute(attribute)

    # ==========================================
    # CHECK ELEMENT DISPLAYED
    # ==========================================

    def is_displayed(self, locator):

        try:

            return self.wait_for_visible(locator).is_displayed()

        except TimeoutException:

            return False

    # ==========================================
    # SELECT DROPDOWN
    # ==========================================

    def select_by_value(self, locator, value):

        dropdown = self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        Select(dropdown).select_by_value(value)

        logger.info(f"Selected dropdown value: {value}")

    # ==========================================
    # WAIT FOR URL
    # ==========================================

    def wait_for_url(self, url):

        return self.wait.until(
            EC.url_contains(url)
        )

    # ==========================================
    # SCROLL ELEMENT
    # ==========================================

    def scroll_into_view(self, locator):

        element = self.find_element(locator)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

    # ==========================================
    # TAKE SCREENSHOT
    # ==========================================

    def take_screenshot(self, name):

        screenshot_dir = Path("screenshots")

        screenshot_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        file_path = screenshot_dir / f"{name}_{timestamp}.png"

        self.driver.save_screenshot(str(file_path))

        logger.info(f"Screenshot saved: {file_path}")

        return file_path

    # ==========================================
    # REFRESH PAGE
    # ==========================================

    def refresh_page(self):

        self.driver.refresh()

        logger.info("Browser page refreshed")

    # ==========================================
    # NAVIGATE BACK
    # ==========================================

    def navigate_back(self):

        self.driver.back()

        logger.info("Browser navigated back")