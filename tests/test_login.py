import pytest

from pages.login_page import LoginPage


# TC_LOGIN_001: Valid login
@pytest.mark.smoke
@pytest.mark.sanity
@pytest.mark.login
def test_valid_login(driver):

    login = LoginPage(driver)

    login.open()

    login.login("standard_user", "secret_sauce")

    assert login.is_login_successful()

    print("\nPASS: Valid login successful")


# TC_LOGIN_002: Invalid username
@pytest.mark.regression
@pytest.mark.login
def test_invalid_username(driver):

    login = LoginPage(driver)

    login.open()

    login.login("wrong_user", "secret_sauce")

    error = login.get_error_message()

    assert "do not match" in error.lower()

    print("\nPASS: Invalid username validation successful")


# TC_LOGIN_003: Invalid password
@pytest.mark.regression
@pytest.mark.login
def test_invalid_password(driver):

    login = LoginPage(driver)

    login.open()

    login.login("standard_user", "wrong_password")

    error = login.get_error_message()

    assert "do not match" in error.lower()

    print("\nPASS: Invalid password validation successful")


# TC_LOGIN_004: Locked-out user
@pytest.mark.regression
@pytest.mark.login
def test_locked_out_user(driver):

    login = LoginPage(driver)

    login.open()

    login.login("locked_out_user", "secret_sauce")

    error = login.get_error_message()

    assert "locked out" in error.lower()

    print("\nPASS: Locked-out user validation successful")


# TC_LOGIN_005: Empty username
@pytest.mark.regression
@pytest.mark.login
def test_empty_username(driver):

    login = LoginPage(driver)

    login.open()

    login.login("", "secret_sauce")

    error = login.get_error_message()

    assert "Username is required" in error

    print("\nPASS: Empty username validation successful")


# TC_LOGIN_006: Empty password
@pytest.mark.regression
@pytest.mark.login
def test_empty_password(driver):

    login = LoginPage(driver)

    login.open()

    login.login("standard_user", "")

    error = login.get_error_message()

    assert "Password is required" in error

    print("\nPASS: Empty password validation successful")


# TC_LOGIN_007: Both fields empty
@pytest.mark.regression
@pytest.mark.login
def test_both_fields_empty(driver):

    login = LoginPage(driver)

    login.open()

    login.login("", "")

    error = login.get_error_message()

    assert "Username is required" in error

    print("\nPASS: Empty credentials validation successful")