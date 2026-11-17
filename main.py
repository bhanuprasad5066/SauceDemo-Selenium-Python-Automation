
from selenium import webdriver

# Initialize Chrome browser
driver = webdriver.Chrome()

try:
    # Open SauceDemo
    driver.get("https://www.saucedemo.com/")

    # Maximize browser
    driver.maximize_window()

    # Print browser details
    print("Browser:", driver.capabilities["browserName"])
    print("Website:", driver.current_url)
    print("Page Title:", driver.title)

    # Validate page title
    assert "Swag Labs" in driver.title

    print("SUCCESS: SauceDemo website opened!")

finally:
    driver.quit()
