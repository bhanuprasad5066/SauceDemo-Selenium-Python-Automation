from pages.login_page import LoginPage


def test_valid_login(driver):

    login = LoginPage(driver)

    login.open()

    login.login("standard_user", "secret_sauce")

    assert login.is_login_successful()

    print("\nPASS: Valid login successful")


def test_invalid_username(driver):

    login = LoginPage(driver)

    login.open()

    login.login("wrong_user", "secret_sauce")

    error = login.get_error_message()

    assert "do not match" in error.lower()

    print("\nPASS: Invalid username validation successful")


def test_invalid_password(driver):

    login = LoginPage(driver)

    login.open()

    login.login("standard_user", "wrong_password")

    error = login.get_error_message()

    assert "do not match" in error.lower()

    print("\nPASS: Invalid password validation successful")


def test_locked_out_user(driver):

    login = LoginPage(driver)

    login.open()

    login.login("locked_out_user", "secret_sauce")

    error = login.get_error_message()

    assert "locked out" in error.lower()

    print("\nPASS: Locked-out user validation successful")


def test_empty_username(driver):

    login = LoginPage(driver)

    login.open()

    login.login("", "secret_sauce")

    error = login.get_error_message()

    assert "Username is required" in error

    print("\nPASS: Empty username validation successful")


def test_empty_password(driver):

    login = LoginPage(driver)

    login.open()

    login.login("standard_user", "")

    error = login.get_error_message()

    assert "Password is required" in error

    print("\nPASS: Empty password validation successful")


def test_both_fields_empty(driver):

    login = LoginPage(driver)

    login.open()

    login.login("", "")

    error = login.get_error_message()

    assert "Username is required" in error

    print("\nPASS: Empty credentials validation successful")