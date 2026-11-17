from selenium.webdriver.common.by import By

from pages.base_page import BasePage

from utils.config_reader import config


class LoginPage(BasePage):

    URL = config.get(
        "application",
        "base_url"
    )

    # ==========================================
    # LOCATORS
    # ==========================================

    USERNAME = (By.ID, "user-name")

    PASSWORD = (By.ID, "password")

    LOGIN_BUTTON = (By.ID, "login-button")

    ERROR_MESSAGE = (
        By.CSS_SELECTOR,
        "[data-test='error']"
    )

    # ==========================================
    # INITIALIZATION
    # ==========================================

    def __init__(self, driver):

        super().__init__(driver)

    # ==========================================
    # OPEN WEBSITE
    # ==========================================

    def open(self):

        self.driver.get(self.URL)

        self.wait_for_visible(self.USERNAME)

    # ==========================================
    # ENTER USERNAME
    # ==========================================

    def enter_username(self, username):

        self.type_text(
            self.USERNAME,
            username
        )

    # ==========================================
    # ENTER PASSWORD
    # ==========================================

    def enter_password(self, password):

        self.type_text(
            self.PASSWORD,
            password
        )

    # ==========================================
    # CLICK LOGIN
    # ==========================================

    def click_login(self):

        self.click(self.LOGIN_BUTTON)

    # ==========================================
    # COMPLETE LOGIN
    # ==========================================

    def login(self, username, password):

        self.enter_username(username)

        self.enter_password(password)

        self.click_login()

    # ==========================================
    # GET ERROR MESSAGE
    # ==========================================

    def get_error_message(self):

        return self.get_text(
            self.ERROR_MESSAGE
        )

    # ==========================================
    # VERIFY SUCCESSFUL LOGIN
    # ==========================================

    def is_login_successful(self):

        return self.wait_for_url(
            "inventory.html"
        )