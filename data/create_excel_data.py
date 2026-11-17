from openpyxl import Workbook
from pathlib import Path

# Excel file location
DATA_DIR = Path(__file__).parent

file_path = DATA_DIR / "login_test_data.xlsx"

# Create workbook
workbook = Workbook()

# Create worksheet
sheet = workbook.active
sheet.title = "LoginData"

# Headers
headers = [
    "case_id",
    "username",
    "password",
    "expected_success",
    "expected_error"
]

sheet.append(headers)

# Test data
test_cases = [
    ["XLS001", "standard_user", "secret_sauce", True, ""],
    ["XLS002", "locked_out_user", "secret_sauce", False, "locked out"],
    ["XLS003", "invalid_user", "secret_sauce", False, "do not match"],
    ["XLS004", "problem_user", "secret_sauce", True, ""],
    ["XLS005", "performance_glitch_user", "secret_sauce", True, ""]
]

# Insert test cases
for test_case in test_cases:
    sheet.append(test_case)

# Save workbook
workbook.save(file_path)

print("Excel workbook created successfully!")
print(f"Location: {file_path}")
print(f"Total test cases: {len(test_cases)}")