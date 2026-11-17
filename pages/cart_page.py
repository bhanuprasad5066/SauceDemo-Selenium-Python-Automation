from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from utils.logger import get_logger


logger = get_logger(__name__)


# ==========================================
# CART PAGE
# ==========================================

class CartPage(BasePage):

    # ==========================================
    # LOCATORS
    # ==========================================

    CART_LIST = (
        By.CLASS_NAME,
        "cart_list"
    )

    CART_ITEMS = (
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

    CONTINUE_SHOPPING = (
        By.ID,
        "continue-shopping"
    )

    CHECKOUT_BUTTON = (
        By.ID,
        "checkout"
    )

    # ==========================================
    # INITIALIZATION
    # ==========================================

    def __init__(self, driver):

        super().__init__(driver)

        logger.info("CartPage initialized")

    # ==========================================
    # WAIT FOR CART PAGE
    # ==========================================

    def wait_for_page(self):

        logger.info("Waiting for cart page")

        self.wait.until(
            EC.visibility_of_element_located(
                self.CART_LIST
            )
        )

        logger.info("Cart page loaded successfully")

    # ==========================================
    # GET CART PRODUCTS
    # ==========================================

    def get_cart_products(self):

        items = self.driver.find_elements(
            *self.CART_ITEMS
        )

        products = [
            item.find_element(
                *self.PRODUCT_NAMES
            ).text
            for item in items
        ]

        logger.info(
            f"Cart products retrieved: {products}"
        )

        return products

    # ==========================================
    # GET CART PRODUCT PRICES
    # ==========================================

    def get_cart_prices(self):

        items = self.driver.find_elements(
            *self.CART_ITEMS
        )

        prices = [
            float(
                item.find_element(
                    *self.PRODUCT_PRICES
                ).text.replace("$", "")
            )
            for item in items
        ]

        logger.info(
            f"Cart product prices: {prices}"
        )

        return prices

    # ==========================================
    # GET CART ITEM COUNT
    # ==========================================

    def get_cart_item_count(self):

        count = len(
            self.driver.find_elements(
                *self.CART_ITEMS
            )
        )

        logger.info(
            f"Total cart items: {count}"
        )

        return count

    # ==========================================
    # REMOVE PRODUCT BY NAME
    # ==========================================

    def remove_product(self, product_name):

        logger.info(
            f"Removing product from cart: {product_name}"
        )

        items = self.driver.find_elements(
            *self.CART_ITEMS
        )

        for item in items:

            name = item.find_element(
                *self.PRODUCT_NAMES
            ).text

            if name == product_name:

                remove_button = item.find_element(
                    By.CSS_SELECTOR,
                    "button[data-test^='remove-']"
                )

                self.wait.until(
                    EC.element_to_be_clickable(
                        remove_button
                    )
                )

                remove_button.click()

                logger.info(
                    f"Product removed successfully: {product_name}"
                )

                return

        logger.error(
            f"Product not found in cart: {product_name}"
        )

        raise AssertionError(
            f"Product not found in cart: {product_name}"
        )

    # ==========================================
    # CONTINUE SHOPPING
    # ==========================================

    def continue_shopping(self):

        logger.info("Continuing shopping")

        self.wait.until(
            EC.element_to_be_clickable(
                self.CONTINUE_SHOPPING
            )
        ).click()

        logger.info(
            "Navigated back to inventory"
        )

    # ==========================================
    # PROCEED TO CHECKOUT
    # ==========================================

    def click_checkout(self):

        logger.info("Proceeding to checkout")

        self.wait.until(
            EC.element_to_be_clickable(
                self.CHECKOUT_BUTTON
            )
        ).click()

        logger.info(
            "Checkout button clicked successfully"
        )