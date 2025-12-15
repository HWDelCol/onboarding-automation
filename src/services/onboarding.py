import json
from pathlib import Path


PROCESSED_PATH = Path("data/processed.json")


def load_processed() -> set[str]:
    if not PROCESSED_PATH.exists():
        return set()

    with PROCESSED_PATH.open(encoding="utf-8") as file:
        data = json.load(file)
        return set(data.get("processed_employees", []))


def save_processed(processed_ids: set[str]) -> None:
    with PROCESSED_PATH.open("w", encoding="utf-8") as file:
        json.dump(
            {"processed_employees": list(processed_ids)},
            file,
            indent=2
        )


def get_new_employees(employees: list[dict]) -> list[dict]:
    processed = load_processed()

    new_employees = [
        emp for emp in employees
        if emp["status"] == "active"
        and emp["employee_id"] not in processed
    ]

    return new_employees
