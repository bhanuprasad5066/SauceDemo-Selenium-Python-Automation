import pytest

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def login_as_standard_user(driver):

    login = LoginPage(driver)

    login.open()

    login.login(
        "standard_user",
        "secret_sauce"
    )

    inventory = InventoryPage(driver)

    inventory.wait_for_page()

    return inventory


# TC_CART_001: Add single product
@pytest.mark.smoke
@pytest.mark.critical
@pytest.mark.cart
def test_add_single_product(driver):

    inventory = login_as_standard_user(driver)

    inventory.add_product_to_cart(
        "Sauce Labs Backpack"
    )

    assert inventory.get_cart_badge_count() == 1

    print("\nPASS: Single product added")


# TC_CART_002: Verify cart badge
@pytest.mark.sanity
@pytest.mark.cart
def test_cart_badge_count(driver):

    inventory = login_as_standard_user(driver)

    inventory.add_product_to_cart(
        "Sauce Labs Backpack"
    )

    assert inventory.get_cart_badge_count() == 1

    print("\nPASS: Cart badge count verified")


# TC_CART_003: Add multiple products
@pytest.mark.regression
@pytest.mark.cart
def test_add_multiple_products(driver):

    inventory = login_as_standard_user(driver)

    inventory.add_product_to_cart(
        "Sauce Labs Backpack"
    )

    inventory.add_product_to_cart(
        "Sauce Labs Bike Light"
    )

    inventory.add_product_to_cart(
        "Sauce Labs Bolt T-Shirt"
    )

    assert inventory.get_cart_badge_count() == 3

    print("\nPASS: Three products added")


# TC_CART_004: Verify product names
@pytest.mark.regression
@pytest.mark.cart
def test_verify_cart_product_names(driver):

    inventory = login_as_standard_user(driver)

    inventory.add_product_to_cart(
        "Sauce Labs Backpack"
    )

    inventory.add_product_to_cart(
        "Sauce Labs Bike Light"
    )

    inventory.open_cart()

    cart = CartPage(driver)

    cart.wait_for_page()

    products = cart.get_cart_products()

    assert "Sauce Labs Backpack" in products

    assert "Sauce Labs Bike Light" in products

    print("\nPASS: Cart product names verified")


# TC_CART_005: Verify product prices
@pytest.mark.regression
@pytest.mark.cart
def test_verify_cart_product_prices(driver):

    inventory = login_as_standard_user(driver)

    inventory.add_product_to_cart(
        "Sauce Labs Backpack"
    )

    inventory.open_cart()

    cart = CartPage(driver)

    cart.wait_for_page()

    prices = cart.get_cart_prices()

    assert len(prices) == 1

    assert prices[0] == 29.99

    print("\nPASS: Cart product price verified")


# TC_CART_006: Remove single product
@pytest.mark.regression
@pytest.mark.cart
def test_remove_single_product(driver):

    inventory = login_as_standard_user(driver)

    inventory.add_product_to_cart(
        "Sauce Labs Backpack"
    )

    inventory.open_cart()

    cart = CartPage(driver)

    cart.wait_for_page()

    cart.remove_product(
        "Sauce Labs Backpack"
    )

    assert cart.get_cart_item_count() == 0

    print("\nPASS: Product removed successfully")


# TC_CART_007: Remove all products
@pytest.mark.regression
@pytest.mark.cart
def test_remove_all_products(driver):

    inventory = login_as_standard_user(driver)

    inventory.add_product_to_cart(
        "Sauce Labs Backpack"
    )

    inventory.add_product_to_cart(
        "Sauce Labs Bike Light"
    )

    inventory.open_cart()

    cart = CartPage(driver)

    cart.wait_for_page()

    cart.remove_product("Sauce Labs Backpack")

    cart.remove_product("Sauce Labs Bike Light")

    assert cart.get_cart_item_count() == 0

    print("\nPASS: All products removed")


# TC_CART_008: Verify empty cart
@pytest.mark.regression
@pytest.mark.cart
def test_empty_cart(driver):

    inventory = login_as_standard_user(driver)

    inventory.open_cart()

    cart = CartPage(driver)

    cart.wait_for_page()

    assert cart.get_cart_item_count() == 0

    print("\nPASS: Empty cart verified")


# TC_CART_009: Continue shopping
@pytest.mark.regression
@pytest.mark.cart
def test_continue_shopping(driver):

    inventory = login_as_standard_user(driver)

    inventory.add_product_to_cart(
        "Sauce Labs Backpack"
    )

    inventory.open_cart()

    cart = CartPage(driver)

    cart.wait_for_page()

    cart.continue_shopping()

    assert "inventory.html" in driver.current_url

    print("\nPASS: Continue shopping successful")


# TC_CART_010: Proceed to checkout
@pytest.mark.smoke
@pytest.mark.critical
@pytest.mark.cart
def test_proceed_to_checkout(driver):

    inventory = login_as_standard_user(driver)

    inventory.add_product_to_cart(
        "Sauce Labs Backpack"
    )

    inventory.open_cart()

    cart = CartPage(driver)

    cart.wait_for_page()

    cart.click_checkout()

    assert "checkout-step-one.html" in driver.current_url

    print("\nPASS: Checkout navigation successful")