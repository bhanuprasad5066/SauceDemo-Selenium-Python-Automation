import csv
import json
from pathlib import Path

from openpyxl import load_workbook

DATA_DIR = (
    Path(__file__).resolve().parent.parent / "data"
)


# ==========================================
# READ CSV DATA
# ==========================================

def load_csv_data(filename):

    file_path = DATA_DIR / filename

    with open(
        file_path,
        mode="r",
        encoding="utf-8-sig",
        newline=""
    ) as file:

        reader = csv.DictReader(file)

        data = list(reader)

    for row in data:

        row["expected_success"] = (
            row["expected_success"].lower() == "true"
        )

    return data


# ==========================================
# READ JSON DATA
# ==========================================

def load_json_data(filename):

    file_path = DATA_DIR / filename

    with open(
        file_path,
        mode="r",
        encoding="utf-8"
    ) as file:

        return json.load(file)

# ==========================================
# EXCEL DATA READER
# ==========================================

def load_excel_data(filename):

    file_path = DATA_DIR / filename

    workbook = load_workbook(
        file_path,
        data_only=True,
        read_only=True
    )

    try:

        sheet = workbook["LoginData"]

        rows = list(
            sheet.iter_rows(values_only=True)
        )

        headers = rows[0]

        data = []

        for row in rows[1:]:

            if not any(value is not None for value in row):
                continue

            record = dict(zip(headers, row))

            record["expected_success"] = (
                str(record["expected_success"]).lower()
                == "true"
            )

            record["expected_error"] = (
                record["expected_error"] or ""
            )

            data.append(record)

        return data

    finally:
        workbook.close()