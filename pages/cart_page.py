from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class CartPage:

    # Locators
    CART_LIST = (By.CLASS_NAME, "cart_list")

    CART_ITEMS = (By.CLASS_NAME, "cart_item")

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

    class Cartpage(BasePage):

        def __init__(self, driver):
            super().__init__(driver)

    # Wait for cart page
    def wait_for_page(self):

        self.wait.until(
            EC.visibility_of_element_located(
                self.CART_LIST
            )
        )

    # Get cart products
    def get_cart_products(self):

        items = self.driver.find_elements(
            *self.CART_ITEMS
        )

        return [
            item.find_element(
                *self.PRODUCT_NAMES
            ).text
            for item in items
        ]

    # Get cart product prices
    def get_cart_prices(self):

        items = self.driver.find_elements(
            *self.CART_ITEMS
        )

        return [
            float(
                item.find_element(
                    *self.PRODUCT_PRICES
                ).text.replace("$", "")
            )
            for item in items
        ]

    # Get cart item count
    def get_cart_item_count(self):

        return len(
            self.driver.find_elements(
                *self.CART_ITEMS
            )
        )

    # Remove product by name
    def remove_product(self, product_name):

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

                remove_button.click()

                return

        raise AssertionError(
            f"Product not found in cart: {product_name}"
        )

    # Continue shopping
    def continue_shopping(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.CONTINUE_SHOPPING
            )
        ).click()

    # Proceed to checkout
    def click_checkout(self):

        self.wait.until(
            EC.element_to_be_clickable(
                self.CHECKOUT_BUTTON
            )
        ).click()