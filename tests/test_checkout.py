from decimal import Decimal

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


# Reusable login and cart preparation
def prepare_checkout(driver):

    # Login
    login = LoginPage(driver)

    login.open()

    login.login(
        "standard_user",
        "secret_sauce"
    )

    # Open inventory
    inventory = InventoryPage(driver)

    inventory.wait_for_page()

    # Add product
    inventory.add_product_to_cart(
        "Sauce Labs Backpack"
    )

    # Open cart
    inventory.open_cart()

    cart = CartPage(driver)

    cart.wait_for_page()

    # Open checkout
    cart.click_checkout()

    return CheckoutPage(driver)


# TC_CHECKOUT_001: Verify checkout page
def test_checkout_page_loads(driver):

    checkout = prepare_checkout(driver)

    checkout.wait_for_information_page()

    assert "checkout-step-one.html" in driver.current_url

    print("PASS: Checkout information page loaded")


# TC_CHECKOUT_002: Empty first name
def test_empty_first_name(driver):

    checkout = prepare_checkout(driver)

    checkout.continue_checkout(
        "",
        "Tester",
        "500001"
    )

    error = checkout.get_error_message()

    assert "First Name is required" in error

    print("\nPASS: Empty first name validation")


# TC_CHECKOUT_003: Empty last name
def test_empty_last_name(driver):

    checkout = prepare_checkout(driver)

    checkout.continue_checkout(
        "Bhanu",
        "",
        "500001"
    )

    error = checkout.get_error_message()

    assert "Last Name is required" in error

    print("\nPASS: Empty last name validation")


# TC_CHECKOUT_004: Empty postal code
def test_empty_postal_code(driver):

    checkout = prepare_checkout(driver)

    checkout.continue_checkout(
        "Bhanu",
        "Tester",
        ""
    )

    error = checkout.get_error_message()

    assert "Postal Code is required" in error

    print("\nPASS: Empty postal code validation")


# TC_CHECKOUT_005: Valid customer information
def test_valid_customer_information(driver):

    checkout = prepare_checkout(driver)

    checkout.continue_checkout(
        "Bhanu",
        "Tester",
        "500001"
    )

    checkout.wait_for_overview()

    assert "checkout-step-two.html" in driver.current_url

    print("\nPASS: Customer information accepted")


# TC_CHECKOUT_006: Verify order products
def test_order_products(driver):

    checkout = prepare_checkout(driver)

    checkout.continue_checkout(
        "Bhanu",
        "Tester",
        "500001"
    )

    checkout.wait_for_overview()

    products = checkout.get_overview_products()

    assert "Sauce Labs Backpack" in products

    print("\nPASS: Order product verified")


# TC_CHECKOUT_007: Verify subtotal
def test_order_subtotal(driver):

    checkout = prepare_checkout(driver)

    checkout.continue_checkout(
        "Bhanu",
        "Tester",
        "500001"
    )

    checkout.wait_for_overview()

    expected_subtotal = checkout.calculate_subtotal()

    actual_subtotal = checkout.get_subtotal()

    assert actual_subtotal == expected_subtotal

    print("\nPASS: Order subtotal verified")

    print("Subtotal:", actual_subtotal)


# TC_CHECKOUT_008: Verify tax and total
def test_order_tax_and_total(driver):

    checkout = prepare_checkout(driver)

    checkout.continue_checkout(
        "Bhanu",
        "Tester",
        "500001"
    )

    checkout.wait_for_overview()

    subtotal = checkout.get_subtotal()

    tax = checkout.get_tax()

    total = checkout.get_total()

    expected_tax = (
        subtotal * Decimal("0.08")
    ).quantize(Decimal("0.01"))

    expected_total = subtotal + expected_tax

    assert tax == expected_tax

    assert total == expected_total

    print("\nPASS: Tax and total calculations verified")

    print("Subtotal:", subtotal)

    print("Tax:", tax)

    print("Total:", total)


# TC_CHECKOUT_009: Complete order
def test_complete_order(driver):

    checkout = prepare_checkout(driver)

    checkout.continue_checkout(
        "Bhanu",
        "Tester",
        "500001"
    )

    checkout.wait_for_overview()

    checkout.finish_order()

    confirmation = checkout.get_confirmation_message()

    assert confirmation == "Thank you for your order!"

    print("\nPASS: Order completed successfully")


# TC_CHECKOUT_010: Return to inventory
def test_back_to_inventory(driver):

    checkout = prepare_checkout(driver)

    checkout.continue_checkout(
        "Bhanu",
        "Tester",
        "500001"
    )

    checkout.wait_for_overview()

    checkout.finish_order()

    checkout.get_confirmation_message()

    checkout.back_home()

    assert "inventory.html" in driver.current_url

    print("\nPASS: Returned to inventory page")