import os

from selenium import webdriver

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from utils.config_reader import config
from utils.logger import get_logger


logger = get_logger(__name__)


class DriverFactory:

    @staticmethod
    def create_driver(browser=None):

        browser = (
            browser or config.get("application", "browser")
        ).lower()

        # Detect GitHub Actions environment
        is_ci = os.getenv("CI", "").lower() == "true"

        # Automatically enable headless mode in CI
        headless = (
            config.get_bool("browser", "headless")
            or is_ci
        )

        width = config.get_int(
            "browser",
            "window_width"
        )

        height = config.get_int(
            "browser",
            "window_height"
        )

        driver = None

        logger.info(
            f"Starting {browser.upper()} browser | "
            f"Headless={headless} | CI={is_ci}"
        )

        try:

            # ======================================
            # CHROME
            # ======================================

            if browser == "chrome":

                options = ChromeOptions()

                options.add_argument(
                    f"--window-size={width},{height}"
                )

                options.add_argument("--disable-notifications")
                options.add_argument("--incognito")
                options.add_argument("--disable-gpu")

                prefs = {
                    "credentials_enable_service": False,
                    "profile.password_manager_enabled": False
                }

                options.add_experimental_option(
                    "prefs",
                    prefs
                )

                options.add_argument(
                    "--disable-features=PasswordLeakDetection"
                )

                if is_ci:
                    options.add_argument("--no-sandbox")
                    options.add_argument("--disable-dev-shm-usage")

                if headless:
                    options.add_argument("--headless=new")

                driver = webdriver.Chrome(options=options)

            # ======================================
            # EDGE
            # ======================================

            elif browser == "edge":

                options = EdgeOptions()

                options.add_argument(
                    f"--window-size={width},{height}"
                )

                if headless:
                    options.add_argument("--headless=new")

                if is_ci:
                    options.add_argument("--no-sandbox")
                    options.add_argument("--disable-dev-shm-usage")

                driver = webdriver.Edge(options=options)

            # ======================================
            # FIREFOX
            # ======================================

            elif browser == "firefox":

                options = FirefoxOptions()

                if headless:
                    options.add_argument("-headless")

                driver = webdriver.Firefox(options=options)

                driver.set_window_size(width, height)

            else:

                raise ValueError(
                    f"Unsupported browser: {browser}"
                )

            # ======================================
            # COMMON CONFIGURATION
            # ======================================

            driver.implicitly_wait(
                config.get_int("timeouts", "implicit_wait")
            )

            driver.set_page_load_timeout(
                config.get_int("timeouts", "page_load_timeout")
            )

            logger.info(
                f"{browser.upper()} browser launched successfully"
            )

            return driver

        except Exception:

            logger.exception(
                f"Failed to initialize {browser.upper()} browser"
            )

            if driver is not None:
                driver.quit()

            raise