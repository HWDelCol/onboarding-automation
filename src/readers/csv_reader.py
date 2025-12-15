import csv
from pathlib import Path


def read_employees(csv_path: str) -> list[dict]:
    """
    Lê o arquivo CSV de funcionários e retorna uma lista de dicionários.
    """
    path = Path(csv_path)

    if not path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {csv_path}")

    employees = []

    with path.open(newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            employees.append({
                "employee_id": row["employee_id"],
                "name": row["name"],
                "email": row["email"],
                "department": row["department"],
                "start_date": row["start_date"],
                "status": row["status"]
            })

    return employees
