import pytest

from pages.login_page import LoginPage
from utils.logger import get_logger
from utils.test_data_reader import load_csv_data, load_excel_data, load_json_data

# ==================================================
# PYTEST MARKERS
# ==================================================

pytestmark = [
    pytest.mark.regression,
    pytest.mark.login
]


logger = get_logger(__name__)


# ==================================================
# CSV DATA-DRIVEN LOGIN TESTING
# ==================================================

@pytest.mark.parametrize(
    "test_data",
    load_csv_data("login_test_data.csv"),
    ids=lambda data: data["case_id"]
)
def test_login_with_csv_data(driver, test_data):

    logger.info(
        f"Starting CSV test case: {test_data['case_id']}"
    )

    login = LoginPage(driver)

    login.open()

    login.login(
        test_data["username"],
        test_data["password"]
    )

    if test_data["expected_success"]:

        assert login.is_login_successful(), (
            f"Login failed for {test_data['case_id']}"
        )

        logger.info(
            f"CSV test passed: {test_data['case_id']}"
        )

    else:

        actual_error = login.get_error_message()

        assert (
            test_data["expected_error"].lower()
            in actual_error.lower()
        ), (
            f"Unexpected error for {test_data['case_id']}: "
            f"{actual_error}"
        )

        logger.info(
            f"CSV validation passed: {test_data['case_id']}"
        )


# ==================================================
# JSON DATA-DRIVEN LOGIN TESTING
# ==================================================

@pytest.mark.parametrize(
    "test_data",
    load_json_data("login_test_data.json"),
    ids=lambda data: data["case_id"]
)
def test_login_with_json_data(driver, test_data):

    logger.info(
        f"Starting JSON test case: {test_data['case_id']}"
    )

    login = LoginPage(driver)

    login.open()

    login.login(
        test_data["username"],
        test_data["password"]
    )

    if test_data["expected_success"]:

        assert login.is_login_successful(), (
            f"Login failed for {test_data['case_id']}"
        )

        logger.info(
            f"JSON test passed: {test_data['case_id']}"
        )

    else:

        actual_error = login.get_error_message()

        assert (
            test_data["expected_error"].lower()
            in actual_error.lower()
        ), (
            f"Unexpected error for {test_data['case_id']}: "
            f"{actual_error}"
        )

        logger.info(
            f"JSON validation passed: {test_data['case_id']}"
        )


# ==================================================
# EXCEL DATA-DRIVEN LOGIN TESTING
# ==================================================

@pytest.mark.parametrize(
    "test_data",
    load_excel_data("login_test_data.xlsx"),
    ids=lambda data: data["case_id"]
)
def test_login_with_excel_data(driver, test_data):

    logger.info(
        f"Starting Excel test: {test_data['case_id']}"
    )

    login = LoginPage(driver)

    login.open()

    login.login(
        test_data["username"],
        test_data["password"]
    )

    if test_data["expected_success"]:

        assert login.is_login_successful(), (
            f"Login failed: {test_data['case_id']}"
        )

        logger.info(
            f"Excel test passed: {test_data['case_id']}"
        )

    else:

        actual_error = login.get_error_message()

        assert (
            test_data["expected_error"].lower()
            in actual_error.lower()
        ), (
            f"Unexpected error: {actual_error}"
        )

        logger.info(
            f"Excel validation passed: {test_data['case_id']}"
        )