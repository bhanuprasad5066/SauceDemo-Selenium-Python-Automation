from decimal import Decimal
from pathlib import Path

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from utils.logger import get_logger


logger = get_logger(__name__)


# ==========================================
# CHECKOUT PAGE
# ==========================================

class CheckoutPage(BasePage):

    # ==========================================
    # CUSTOMER INFORMATION LOCATORS
    # ==========================================

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

    # ==========================================
    # CHECKOUT OVERVIEW LOCATORS
    # ==========================================

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

    # ==========================================
    # ORDER CONFIRMATION LOCATORS
    # ==========================================

    COMPLETE_HEADER = (
        By.CLASS_NAME,
        "complete-header"
    )

    BACK_HOME_BUTTON = (
        By.ID,
        "back-to-products"
    )

    # ==========================================
    # INITIALIZATION
    # ==========================================

    def __init__(self, driver):

        super().__init__(driver)

        logger.info("CheckoutPage initialized")

    # ==========================================
    # ENTER CUSTOMER INFORMATION
    # ==========================================

    def enter_customer_information(
        self,
        first_name,
        last_name,
        postal_code
    ):

        logger.info(
            "Entering customer information"
        )

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

        logger.info(
            "Customer information entered successfully"
        )

    # ==========================================
    # CLICK CONTINUE
    # ==========================================

    def click_continue(self):

        logger.info(
            "Clicking checkout continue button"
        )

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.CONTINUE_BUTTON
            )
        )

        button.click()

        logger.info(
            "Continue button clicked successfully"
        )

    # ==========================================
    # COMPLETE CUSTOMER INFORMATION
    # ==========================================

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

    # ==========================================
    # GET VALIDATION ERROR
    # ==========================================

    def get_error_message(self):

        error = self.wait.until(
            EC.visibility_of_element_located(
                self.ERROR_MESSAGE
            )
        )

        message = error.text

        logger.info(
            f"Checkout validation message: {message}"
        )

        return message

    # ==========================================
    # WAIT FOR CHECKOUT OVERVIEW
    # ==========================================

    def wait_for_overview(self):

        logger.info(
            "Waiting for checkout overview"
        )

        self.wait.until(
            EC.url_contains(
                "checkout-step-two.html"
            )
        )

        self.wait.until(
            EC.visibility_of_element_located(
                self.OVERVIEW_CONTAINER
            )
        )

        logger.info(
            "Checkout overview loaded successfully"
        )

    # ==========================================
    # GET OVERVIEW PRODUCTS
    # ==========================================

    def get_overview_products(self):

        items = self.driver.find_elements(
            *self.OVERVIEW_PRODUCTS
        )

        products = [
            item.find_element(
                *self.PRODUCT_NAMES
            ).text
            for item in items
        ]

        logger.info(
            f"Checkout products retrieved: {products}"
        )

        return products

    # ==========================================
    # GET PRODUCT PRICES
    # ==========================================

    def get_product_prices(self):

        items = self.driver.find_elements(
            *self.OVERVIEW_PRODUCTS
        )

        prices = [
            Decimal(
                item.find_element(
                    *self.PRODUCT_PRICES
                ).text.replace("$", "")
            )
            for item in items
        ]

        logger.info(
            f"Checkout product prices: {prices}"
        )

        return prices

    # ==========================================
    # EXTRACT MONETARY AMOUNT
    # ==========================================

    def get_amount(self, locator):

        element = self.wait.until(
            EC.visibility_of_element_located(
                locator
            )
        )

        amount = Decimal(
            element.text.split("$")[-1]
        )

        return amount

    # ==========================================
    # GET SUBTOTAL
    # ==========================================

    def get_subtotal(self):

        subtotal = self.get_amount(
            self.SUBTOTAL
        )

        logger.info(
            f"Order subtotal: {subtotal}"
        )

        return subtotal

    # ==========================================
    # GET TAX
    # ==========================================

    def get_tax(self):

        tax = self.get_amount(
            self.TAX
        )

        logger.info(
            f"Order tax: {tax}"
        )

        return tax

    # ==========================================
    # GET TOTAL
    # ==========================================

    def get_total(self):

        total = self.get_amount(
            self.TOTAL
        )

        logger.info(
            f"Order total: {total}"
        )

        return total

    # ==========================================
    # CALCULATE SUBTOTAL
    # ==========================================

    def calculate_subtotal(self):

        prices = self.get_product_prices()

        subtotal = sum(
            prices,
            Decimal("0.00")
        )

        logger.info(
            f"Calculated subtotal: {subtotal}"
        )

        return subtotal

    # ==========================================
    # FINISH ORDER
    # ==========================================

    def finish_order(self):

        logger.info(
            "Completing customer order"
        )

        button = self.wait.until(
            EC.element_to_be_clickable(
                self.FINISH_BUTTON
            )
        )

        button.click()

        logger.info(
            "Order submitted successfully"
        )

    # ==========================================
    # GET ORDER CONFIRMATION
    # ==========================================

    def get_confirmation_message(self):

        header = self.wait.until(
            EC.visibility_of_element_located(
                self.COMPLETE_HEADER
            )
        )

        message = header.text

        logger.info(
            f"Order confirmation: {message}"
        )

        return message

    # ==========================================
    # RETURN TO INVENTORY
    # ==========================================

    def back_home(self):

        logger.info(
            "Navigating back to inventory"
        )

        self.wait.until(
            EC.element_to_be_clickable(
                self.BACK_HOME_BUTTON
            )
        ).click()

        logger.info(
            "Returned to inventory successfully"
        )

    # ==========================================
    # CANCEL CHECKOUT
    # ==========================================

    def cancel_checkout(self):

        logger.info(
            "Cancelling checkout"
        )

        self.wait.until(
            EC.element_to_be_clickable(
                self.CANCEL_BUTTON
            )
        ).click()

        logger.info(
            "Checkout cancelled successfully"
        )

    # ==========================================
    # WAIT FOR INFORMATION PAGE
    # ==========================================

    def wait_for_information_page(self):

        logger.info(
            "Waiting for checkout information page"
        )

        self.wait.until(
            EC.url_contains(
                "checkout-step-one.html"
            )
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

        logger.info(
            "Checkout information page loaded successfully"
        )

    # ==========================================
    # DEBUG BROWSER STATE
    # ==========================================

    def debug_browser_state(self):

        print(
            "\n========== DEBUG INFORMATION =========="
        )

        print(
            "Current URL:",
            self.driver.current_url
        )

        print(
            "Page title:",
            self.driver.title
        )

        print(
            "Page text:",
            self.driver.find_element(
                By.TAG_NAME,
                "body"
            ).text[:2000]
        )

        screenshot_dir = Path("screenshots")

        screenshot_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        self.driver.save_screenshot(
            str(screenshot_dir / "checkout_debug.png")
        )

        print(
            "Screenshot saved"
        )