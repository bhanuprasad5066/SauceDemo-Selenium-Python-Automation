from decimal import Decimal

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class CheckoutPage:

    # Customer information locators
    FIRST_NAME = (
        By.ID,
        "first-name"
    )

    LAST_NAME = (
        By.ID,
        "last-name"
    )

    POSTAL_CODE = (
        By.ID,
        "postal-code"
    )

    CONTINUE_BUTTON = (
        By.ID,
        "continue"
    )

    CANCEL_BUTTON = (
        By.ID,
        "cancel"
    )

    ERROR_MESSAGE = (
        By.CSS_SELECTOR,
        "[data-test='error']"
    )

    # Checkout overview locators
    OVERVIEW_CONTAINER = (
        By.ID,
        "checkout_summary_container"
    )

    OVERVIEW_PRODUCTS = (
        By.CLASS_NAME,
        "cart_item"
    )

    PRODUCT_NAMES = (
        By.CLASS_NAME,
        "inventory_item_name"
    )

    PRODUCT_PRICES = (
        By.CLASS_NAME,
        "inventory_item_price"
    )

    SUBTOTAL = (
        By.CLASS_NAME,
        "summary_subtotal_label"
    )

    TAX = (
        By.CLASS_NAME,
        "summary_tax_label"
    )

    TOTAL = (
        By.CLASS_NAME,
        "summary_total_label"
    )

    FINISH_BUTTON = (
        By.ID,
        "finish"
    )

    # Order confirmation locators
    COMPLETE_HEADER = (
        By.CLASS_NAME,
        "complete-header"
    )

    BACK_HOME_BUTTON = (
        By.ID,
        "back-to-products"
    )

    class Checkoutpage(BasePage):

        def __init__(self, driver):
            super().__init__(driver)

    # Enter customer information
    def enter_customer_information(
            self,
            first_name,
            last_name,
            postal_code
    ):
        first = self.wait.until(
            EC.element_to_be_clickable(
                self.FIRST_NAME
            )
        )

        last = self.wait.until(
            EC.element_to_be_clickable(
                self.LAST_NAME
            )
        )

        postal = self.wait.until(
            EC.element_to_be_clickable(
                self.POSTAL_CODE
            )
        )

        first.clear()
        first.send_keys(first_name)

        last.clear()
        last.send_keys(last_name)

        postal.clear()
        postal.send_keys(postal_code)

        print("Customer information entered")

    # Click continue
    def click_continue(self):
        button = self.wait.until(
            EC.element_to_be_clickable(
                self.CONTINUE_BUTTON
            )
        )

        button.click()

        print("Continue button clicked")

    # Complete customer information
    def continue_checkout(
        self,
        first_name,
        last_name,
        postal_code
    ):

        self.enter_customer_information(
            first_name,
            last_name,
            postal_code
        )

        self.click_continue()

    # Get validation error
    def get_error_message(self):

        error = self.wait.until(
            EC.visibility_of_element_located(
                self.ERROR_MESSAGE
            )
        )

        return error.text

    # Wait for overview page
    def wait_for_overview(self):
        self.wait.until(
            EC.url_contains("checkout-step-two.html")
        )

        self.wait.until(
            EC.visibility_of_element_located(
                self.OVERVIEW_CONTAINER
            )
        )

        print("Checkout overview loaded")

    # Get overview products
    def get_overview_products(self):

        items = self.driver.find_elements(
            *self.OVERVIEW_PRODUCTS
        )

        return [
            item.find_element(
                *self.PRODUCT_NAMES
            ).text
            for item in items
        ]

    # Get product prices
    def get_product_prices(self):

        items = self.driver.find_elements(
            *self.OVERVIEW_PRODUCTS
        )

        return [
            Decimal(
                item.find_element(
                    *self.PRODUCT_PRICES
                ).text.replace("$", "")
            )
            for item in items
        ]

    # Extract monetary amount
    def get_amount(self, locator):

        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        return Decimal(
            element.text.split("$")[-1]
        )

    # Get subtotal
    def get_subtotal(self):

        return self.get_amount(
            self.SUBTOTAL
        )

    # Get tax
    def get_tax(self):

        return self.get_amount(
            self.TAX
        )

    # Get total
    def get_total(self):

        return self.get_amount(
            self.TOTAL
        )

    # Verify calculated subtotal
    def calculate_subtotal(self):

        prices = self.get_product_prices()

        return sum(
            prices,
            Decimal("0.00")
        )

    # Finish order
    def finish_order(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.FINISH_BUTTON
            )
        ).click()

    # Get order confirmation
    def get_confirmation_message(self):

        header = self.wait.until(
            EC.visibility_of_element_located(
                self.COMPLETE_HEADER
            )
        )

        return header.text

    # Return to inventory
    def back_home(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.BACK_HOME_BUTTON
            )
        ).click()

    # Cancel checkout
    def cancel_checkout(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.CANCEL_BUTTON
            )
        ).click()

    def wait_for_information_page(self):
        self.wait.until(
            EC.url_contains("checkout-step-one.html")
        )

        self.wait.until(
            EC.visibility_of_element_located(
                self.FIRST_NAME
            )
        )

        self.wait.until(
            EC.visibility_of_element_located(
                self.LAST_NAME
            )
        )

        self.wait.until(
            EC.visibility_of_element_located(
                self.POSTAL_CODE
            )
        )

    def debug_browser_state(self):
        print("\n========== DEBUG INFORMATION ==========")

        print("Current URL:", self.driver.current_url)

        print("Page title:", self.driver.title)

        print(
            "Page text:",
            self.driver.find_element(
                By.TAG_NAME,
                "body"
            ).text[:2000]
        )

        self.driver.save_screenshot(
            "screenshots/checkout_debug.png"
        )

        print("Screenshot saved")

        print("========================================")