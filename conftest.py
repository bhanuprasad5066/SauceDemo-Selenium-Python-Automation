import re
from datetime import datetime
from pathlib import Path

import pytest
import pytest_html

from utils.driver_factory import DriverFactory
from utils.config_reader import config
from utils.logger import get_logger


logger = get_logger(__name__)

PROJECT_ROOT = Path(__file__).resolve().parent
SCREENSHOT_DIR = PROJECT_ROOT / "screenshots"


# ==========================================
# BROWSER FIXTURE
# ==========================================

@pytest.fixture
def driver():

    browser = DriverFactory.create_driver()

    logger.info("Browser session started")

    try:
        yield browser

    finally:
        logger.info("Closing browser session")
        browser.quit()


# ==========================================
# PYTEST TEST RESULT HOOK
# ==========================================

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    setattr(item, "rep_" + report.when, report)

    # Capture screenshot when a test fails
    if report.when == "call" and report.failed:

        browser = item.funcargs.get("driver")

        if browser is None:
            return

        SCREENSHOT_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

        safe_name = re.sub(
            r"[^A-Za-z0-9_.-]+",
            "_",
            item.nodeid
        )

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S_%f"
        )

        screenshot_path = (
            SCREENSHOT_DIR /
            f"{safe_name}_{timestamp}.png"
        )

        try:

            # Save screenshot locally
            browser.save_screenshot(
                str(screenshot_path)
            )

            logger.error(
                f"Test failed: {item.nodeid}"
            )

            logger.error(
                f"Screenshot saved: {screenshot_path}"
            )

            # Attach screenshot to HTML report
            screenshot_base64 = (
                browser.get_screenshot_as_base64()
            )

            extras = getattr(
                report,
                "extras",
                []
            )

            extras.append(
                pytest_html.extras.image(
                    screenshot_base64,
                    mime_type="image/png",
                    name="Failure Screenshot"
                )
            )

            report.extras = extras

        except Exception:

            logger.exception(
                "Unable to capture failure screenshot"
            )


# ==========================================
# HTML REPORT METADATA
# ==========================================

def pytest_configure(config):

    metadata = config.stash.get(
        pytest.MetadataKey, None
    ) if hasattr(pytest, "MetadataKey") else None

    # Compatible with pytest-metadata plugin
    try:
        from pytest_metadata.plugin import metadata_key

        metadata = config.stash[metadata_key]

    except (ImportError, KeyError):
        metadata = None

    if metadata is not None:

        metadata["Project"] = (
            "SauceDemo Automation Framework"
        )

        metadata["Automation Tool"] = (
            "Selenium + Python + Pytest"
        )

        metadata["Browser"] = (
            config_reader_browser()
        )

        metadata["Framework"] = (
            "Advanced Page Object Model"
        )

        metadata["Environment"] = (
            "Windows 11"
        )


def config_reader_browser():

    return config.get(
        "application",
        "browser"
    ).upper()


# ==========================================
# HTML REPORT TITLE
# ==========================================

def pytest_html_report_title(report):

    report.title = (
        "SauceDemo Professional QA Automation Report"
    )