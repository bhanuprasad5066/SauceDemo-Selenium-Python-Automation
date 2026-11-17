# 🚀 SauceDemo Selenium Python Automation Framework

[![Python](https://img.shields.io/badge/Python-3.15%2B-blue.svg)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.x-green.svg)](https://www.selenium.dev/)
[![Pytest](https://img.shields.io/badge/Pytest-9.x-orange.svg)](https://docs.pytest.org/)
[![Framework](https://img.shields.io/badge/Framework-Page%20Object%20Model-purple.svg)](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/)

A professional Python-based UI automation framework for the [SauceDemo](https://www.saucedemo.com/) e-commerce application.

Built using Selenium WebDriver, Pytest, Page Object Model (POM), data-driven testing, browser factory, centralized configuration, logging, and HTML reporting.

---

## 📌 Project Overview

This project automates important e-commerce workflows to demonstrate maintainable and reusable UI test automation.

The framework follows industry-standard automation practices, separating test logic, page interactions, configuration, test data, and reporting.

### Key Features

- Page Object Model (POM) architecture.
- Reusable BasePage implementation.
- Centralized Browser Factory.
- Chrome, Edge, and Firefox browser support.
- INI-based configuration management.
- Environment-variable configuration overrides.
- Explicit waits and expected conditions.
- Pytest fixtures and parametrization.
- CSV, JSON, and Excel data-driven testing.
- Centralized logging.
- Automatic failure screenshot capture.
- Self-contained HTML test reports.

---

## 🛠 Technology Stack

| Technology | Purpose |
|---|---|
| Python | Automation programming |
| Selenium WebDriver | Browser automation |
| Pytest | Test execution |
| pytest-html | HTML reporting |
| OpenPyXL | Excel test data |
| ConfigParser | Configuration management |
| Chrome | Browser automation |
| Microsoft Edge | Browser automation |
| Firefox | Browser automation |
| Git | Version control |
| GitHub | Source code hosting |
| PyCharm | Development environment |

---

## 🧪 Automation Test Coverage

### 1. Login Testing

- Valid user login.
- Invalid username validation.
- Invalid password validation.
- Locked-out user validation.
- Empty username validation.
- Empty password validation.
- Empty credentials validation.
- CSV-driven login testing.
- JSON-driven login testing.
- Excel-driven login testing.

### 2. Inventory Testing

- Inventory page loading.
- Product count verification.
- Product name verification.
- Product price verification.
- Product description verification.
- Product image loading.
- Product sorting A–Z.
- Product sorting Z–A.
- Price sorting low to high.
- Price sorting high to low.

### 3. Shopping Cart Testing

- Add single product.
- Add multiple products.
- Verify cart badge count.
- Verify product names.
- Verify product prices.
- Remove individual products.
- Remove all products.
- Verify empty cart.
- Continue shopping.
- Navigate to checkout.

### 4. Checkout Testing

- Checkout page loading.
- First name validation.
- Last name validation.
- Postal code validation.
- Valid customer information.
- Order product verification.
- Subtotal verification.
- Tax calculation.
- Total calculation.
- Complete order.
- Order confirmation.
- Return to inventory.

---

## 🏗 Framework Architecture

```text
SauceDemo-Selenium-Python-Automation/
│
├── config/
│   └── config.ini
│
├── data/
│   ├── login_test_data.csv
│   ├── login_test_data.json
│   ├── login_test_data.xlsx
│   └── create_excel_data.py
│
├── logs/
│   ├── automation.log
│   └── pytest_execution.log
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── reports/
│
├── screenshots/
│
├── tests/
│   ├── test_login.py
│   ├── test_login_data_driven.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   ├── test_parametrize_demo.py
│   └── test_products_cart_checkout.py
│
├── utils/
│   ├── config_reader.py
│   ├── driver_factory.py
│   ├── logger.py
│   └── test_data_reader.py
│
├── conftest.py
├── main.py
├── pytest.ini
├── pyproject.toml
├── requirements.txt
├── uv.lock
└── .gitignore
```

### Architecture Components

**BasePage**
- Reusable Selenium interactions.
- Element clicking and text entry.
- Explicit wait handling.
- Common browser operations.

**DriverFactory**
- Centralized browser initialization.
- Chrome, Edge and Firefox support.
- Headless execution configuration.
- Browser window configuration.

**ConfigReader**
- Reads INI configuration.
- Provides environment-variable overrides.
- Centralizes browser and timeout settings.

**conftest.py**
- Shared WebDriver fixture.
- Browser initialization and teardown.
- Failure screenshot capture.
- HTML report integration.

**Test Data Reader**
- CSV data loading.
- JSON data loading.
- Excel data loading.

---

## 💻 Installation and Setup

### Prerequisites

- Python 3.15+
- Google Chrome / Microsoft Edge / Firefox
- Git
- PyCharm IDE

### 1. Clone Repository

```bash
git clone https://github.com/bhanuprasad5066/SauceDemo-Selenium-Python-Automation.git

cd SauceDemo-Selenium-Python-Automation
```

### 2. Create Virtual Environment

Windows:

```powershell
python -m venv .venv
```

Activate:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip

pip install -r requirements.txt

pip install openpyxl
```

---

## ⚙️ Configuration Management

Configuration is maintained in:

`config/config.ini`

Example:

```ini
[application]

base_url = https://www.saucedemo.com/
browser = chrome


[browser]

headless = false
window_width = 1920
window_height = 1080


[timeouts]

implicit_wait = 0
explicit_wait = 15
page_load_timeout = 30
```

### Environment Variable Overrides

Example using PowerShell:

```powershell
$env:SAUCEDEMO_BROWSER = "edge"

$env:SAUCEDEMO_HEADLESS = "true"

pytest
```

---

## ▶️ Test Execution

### Run Complete Test Suite

```bash
pytest
```

### Run with Verbose Output

```bash
pytest -v -s
```

### Run Login Tests

```bash
pytest tests/test_login.py -v
```

### Run Inventory Tests

```bash
pytest tests/test_inventory.py -v
```

### Run Cart Tests

```bash
pytest tests/test_cart.py -v
```

### Run Checkout Tests

```bash
pytest tests/test_checkout.py -v
```

### Run Data-Driven Tests

```bash
pytest tests/test_login_data_driven.py -v
```

---

## 📊 HTML Reporting

Generate a self-contained HTML report:

```bash
pytest -v -s --html=reports/pytest_report.html --self-contained-html
```

Generated report:

```text
reports/
└── pytest_report.html
```

### Failure Screenshot Capture

When a test fails, the framework attempts to:

1. Capture the browser screenshot.
2. Save the screenshot inside the screenshots directory.
3. Attach the screenshot to the HTML report.
4. Record failure details in the logs.

---

## 📝 Logging

Logging is centralized through:

`utils/logger.py`

Generated log files:

```text
logs/
├── automation.log
└── pytest_execution.log
```

Logs help identify test failures, browser issues, and execution details.

---

## 🌐 Browser Support

| Browser | Support |
|---|---|
| Google Chrome | Implemented |
| Microsoft Edge | Implemented |
| Mozilla Firefox | Implemented |

Browser selection is controlled through `config/config.ini`.

---

## 🔄 Git Workflow

```bash
git status

git add .

git commit -m "Update automation framework"

git push origin main
```

---

## 🚧 Future Enhancements

- GitHub Actions CI/CD integration.
- Automated test execution on every push.
- Pull request validation.
- CI artifact uploads.
- Advanced test execution analytics.

GitHub Actions integration will be added and verified in the next development phase.

---

## 👨‍💻 Author

**Bhanu Prasad Pitla**

GitHub: [@bhanuprasad5066](https://github.com/bhanuprasad5066)

Project Repository:

[SauceDemo Selenium Python Automation](https://github.com/bhanuprasad5066/SauceDemo-Selenium-Python-Automation)

---

⭐ If you find this project useful, consider giving the repository a star!