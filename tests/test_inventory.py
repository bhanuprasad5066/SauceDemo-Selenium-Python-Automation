import pytest

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


# TC_INV_001: Verify inventory page loads
@pytest.mark.smoke
@pytest.mark.sanity
@pytest.mark.inventory
def test_inventory_page_loads(driver):

    login_as_standard_user(driver)

    assert "inventory.html" in driver.current_url

    print("\nPASS: Inventory page loaded successfully")


# TC_INV_002: Verify product count
@pytest.mark.smoke
@pytest.mark.inventory
def test_product_count(driver):

    inventory = login_as_standard_user(driver)

    count = inventory.get_product_count()

    assert count == 6

    print("\nPASS: Six products displayed")


# TC_INV_003: Verify product names
@pytest.mark.regression
@pytest.mark.inventory
def test_product_names(driver):

    inventory = login_as_standard_user(driver)

    names = inventory.get_product_names()

    assert len(names) == 6

    assert all(name.strip() for name in names)

    print("\nPASS: Product names verified")

    print("Products:", names)


# TC_INV_004: Verify product prices
@pytest.mark.regression
@pytest.mark.inventory
def test_product_prices(driver):

    inventory = login_as_standard_user(driver)

    prices = inventory.get_product_prices()

    assert len(prices) == 6

    assert all(price > 0 for price in prices)

    print("\nPASS: Product prices verified")

    print("Prices:", prices)


# TC_INV_005: Sort A-Z
@pytest.mark.regression
@pytest.mark.inventory
def test_sort_products_a_to_z(driver):

    inventory = login_as_standard_user(driver)

    inventory.sort_a_to_z()

    names = inventory.get_product_names()

    assert names == sorted(names)

    print("\nPASS: Products sorted A-Z")


# TC_INV_006: Sort Z-A
@pytest.mark.regression
@pytest.mark.inventory
def test_sort_products_z_to_a(driver):

    inventory = login_as_standard_user(driver)

    inventory.sort_z_to_a()

    names = inventory.get_product_names()

    assert names == sorted(names, reverse=True)

    print("\nPASS: Products sorted Z-A")


# TC_INV_007: Price Low-High
@pytest.mark.regression
@pytest.mark.inventory
def test_sort_price_low_to_high(driver):

    inventory = login_as_standard_user(driver)

    inventory.sort_price_low_to_high()

    prices = inventory.get_product_prices()

    assert prices == sorted(prices)

    print("\nPASS: Prices sorted Low-High")


# TC_INV_008: Price High-Low
@pytest.mark.regression
@pytest.mark.inventory
def test_sort_price_high_to_low(driver):

    inventory = login_as_standard_user(driver)

    inventory.sort_price_high_to_low()

    prices = inventory.get_product_prices()

    assert prices == sorted(prices, reverse=True)

    print("\nPASS: Prices sorted High-Low")


# TC_INV_009: Verify product images
@pytest.mark.regression
@pytest.mark.inventory
def test_product_images(driver):

    inventory = login_as_standard_user(driver)

    image_count = inventory.get_loaded_image_count()

    assert image_count == 6

    print("\nPASS: All six product images loaded")


# TC_INV_010: Verify product descriptions
@pytest.mark.regression
@pytest.mark.inventory
def test_product_descriptions(driver):

    inventory = login_as_standard_user(driver)

    assert inventory.are_descriptions_available()

    print("\nPASS: All product descriptions available")