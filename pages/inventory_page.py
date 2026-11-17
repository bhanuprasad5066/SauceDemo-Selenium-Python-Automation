from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from utils.logger import get_logger


logger = get_logger(__name__)


# ==========================================
# INVENTORY PAGE
# ==========================================

class InventoryPage(BasePage):

    # ==========================================
    # PAGE URL
    # ==========================================

    URL = "https://www.saucedemo.com/inventory.html"

    # ==========================================
    # LOCATORS
    # ==========================================

    INVENTORY_CONTAINER = (
        By.ID, "inventory_container"
    )

    PRODUCTS = (
        By.CLASS_NAME, "inventory_item"
    )

    PRODUCT_NAMES = (
        By.CLASS_NAME, "inventory_item_name"
    )

    PRODUCT_PRICES = (
        By.CLASS_NAME, "inventory_item_price"
    )

    PRODUCT_IMAGES = (
        By.CSS_SELECTOR, "img.inventory_item_img"
    )

    PRODUCT_DESCRIPTIONS = (
        By.CLASS_NAME, "inventory_item_desc"
    )

    SORT_DROPDOWN = (
        By.CLASS_NAME, "product_sort_container"
    )

    CART_BADGE = (
        By.CLASS_NAME, "shopping_cart_badge"
    )

    CART_LINK = (
        By.CLASS_NAME, "shopping_cart_link"
    )

    # ==========================================
    # INITIALIZATION
    # ==========================================

    def __init__(self, driver):

        super().__init__(driver)

        logger.info("InventoryPage initialized")

    # ==========================================
    # VERIFY INVENTORY PAGE
    # ==========================================

    def wait_for_page(self):

        logger.info("Waiting for inventory page")

        self.wait.until(
            EC.visibility_of_element_located(
                self.INVENTORY_CONTAINER
            )
        )

        logger.info("Inventory page loaded successfully")

    # ==========================================
    # GET ALL PRODUCTS
    # ==========================================

    def get_products(self):

        return self.driver.find_elements(
            *self.PRODUCTS
        )

    # ==========================================
    # GET PRODUCT COUNT
    # ==========================================

    def get_product_count(self):

        count = len(self.get_products())

        logger.info(
            f"Total products displayed: {count}"
        )

        return count

    # ==========================================
    # GET PRODUCT NAMES
    # ==========================================

    def get_product_names(self):

        elements = self.driver.find_elements(
            *self.PRODUCT_NAMES
        )

        names = [
            element.text for element in elements
        ]

        logger.info(
            f"Product names retrieved: {len(names)}"
        )

        return names

    # ==========================================
    # GET PRODUCT PRICES
    # ==========================================

    def get_product_prices(self):

        elements = self.driver.find_elements(
            *self.PRODUCT_PRICES
        )

        prices = [
            float(element.text.replace("$", ""))
            for element in elements
        ]

        logger.info(
            f"Product prices retrieved: {prices}"
        )

        return prices

    # ==========================================
    # GET PRODUCT DESCRIPTIONS
    # ==========================================

    def get_product_descriptions(self):

        elements = self.driver.find_elements(
            *self.PRODUCT_DESCRIPTIONS
        )

        descriptions = [
            element.text for element in elements
        ]

        logger.info(
            "Product descriptions retrieved"
        )

        return descriptions

    # ==========================================
    # SORT PRODUCTS
    # ==========================================

    def sort_products(self, sort_option):

        logger.info(
            f"Sorting products using option: {sort_option}"
        )

        dropdown = self.wait.until(
            EC.element_to_be_clickable(
                self.SORT_DROPDOWN
            )
        )

        Select(dropdown).select_by_value(
            sort_option
        )

        logger.info(
            f"Product sorting selected: {sort_option}"
        )

    # ==========================================
    # SORT A-Z
    # ==========================================

    def sort_a_to_z(self):

        logger.info("Starting A-Z product sorting")

        self.sort_products("az")

        self.wait.until(
            lambda driver:
            self.get_product_names()
            == sorted(self.get_product_names())
        )

        logger.info("Products successfully sorted A-Z")

    # ==========================================
    # SORT Z-A
    # ==========================================

    def sort_z_to_a(self):

        logger.info("Starting Z-A product sorting")

        self.sort_products("za")

        self.wait.until(
            lambda driver:
            self.get_product_names()
            == sorted(
                self.get_product_names(),
                reverse=True
            )
        )

        logger.info("Products successfully sorted Z-A")

    # ==========================================
    # SORT PRICE LOW-HIGH
    # ==========================================

    def sort_price_low_to_high(self):

        logger.info("Starting price sorting: Low to High")

        self.sort_products("lohi")

        self.wait.until(
            lambda driver:
            self.get_product_prices()
            == sorted(self.get_product_prices())
        )

        logger.info("Prices successfully sorted Low-High")

    # ==========================================
    # SORT PRICE HIGH-LOW
    # ==========================================

    def sort_price_high_to_low(self):

        logger.info("Starting price sorting: High to Low")

        self.sort_products("hilo")

        self.wait.until(
            lambda driver:
            self.get_product_prices()
            == sorted(
                self.get_product_prices(),
                reverse=True
            )
        )

        logger.info("Prices successfully sorted High-Low")

    # ==========================================
    # VERIFY PRODUCT IMAGES
    # ==========================================

    def get_loaded_image_count(self):

        logger.info("Checking product image loading")

        images = self.wait.until(
            lambda driver: (
                driver.find_elements(
                    *self.PRODUCT_IMAGES
                )
                if len(
                    driver.find_elements(
                        *self.PRODUCT_IMAGES
                    )
                ) == 6
                else False
            )
        )

        loaded_count = 0

        for image in images:

            self.driver.execute_script(
                "arguments[0].scrollIntoView({block: 'center'});",
                image
            )

            self.wait.until(
                lambda driver:
                image.get_attribute("complete") == "true"
                and self.driver.execute_script(
                    "return arguments[0].naturalWidth > 0",
                    image
                )
            )

            loaded_count += 1

        logger.info(
            f"Successfully loaded images: {loaded_count}/6"
        )

        return loaded_count

    # ==========================================
    # VERIFY PRODUCT DESCRIPTIONS
    # ==========================================

    def are_descriptions_available(self):

        descriptions = self.get_product_descriptions()

        product_count = self.get_product_count()

        result = (
            len(descriptions) == product_count
            and all(
                description.strip()
                for description in descriptions
            )
        )

        if result:

            logger.info(
                "All product descriptions are available"
            )

        else:

            logger.warning(
                "Some product descriptions are missing"
            )

        return result

    # ==========================================
    # ADD PRODUCT TO CART
    # ==========================================

    def add_product_to_cart(self, product_name):

        logger.info(
            f"Adding product to cart: {product_name}"
        )

        products = self.get_products()

        for product in products:

            name = product.find_element(
                By.CLASS_NAME,
                "inventory_item_name"
            ).text

            if name == product_name:

                button = product.find_element(
                    By.CSS_SELECTOR,
                    "button[data-test^='add-to-cart']"
                )

                self.wait.until(
                    EC.element_to_be_clickable(button)
                )

                button.click()

                logger.info(
                    f"Product added successfully: {product_name}"
                )

                return

        logger.error(
            f"Product not found: {product_name}"
        )

        raise AssertionError(
            f"Product not found: {product_name}"
        )

    # ==========================================
    # GET CART BADGE COUNT
    # ==========================================

    def get_cart_badge_count(self):

        badges = self.driver.find_elements(
            *self.CART_BADGE
        )

        if not badges:

            logger.info("Shopping cart is empty")

            return 0

        count = int(badges[0].text)

        logger.info(
            f"Shopping cart badge count: {count}"
        )

        return count

    # ==========================================
    # OPEN SHOPPING CART
    # ==========================================

    def open_cart(self):

        logger.info("Opening shopping cart")

        cart = self.wait.until(
            EC.element_to_be_clickable(
                self.CART_LINK
            )
        )

        cart.click()

        logger.info(
            "Shopping cart opened successfully"
        )