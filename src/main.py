from readers.csv_reader import read_employees
from services.onboarding import get_new_employees, save_processed


def main():
    employees = read_employees("data/employees.csv")
    new_employees = get_new_employees(employees)

    if not new_employees:
        print("Nenhum novo funcionário para onboarding.")
        return

    processed_ids = set()

    for emp in new_employees:
        print(f"Iniciando onboarding para: {emp['name']}")
        processed_ids.add(emp["employee_id"])

    save_processed(processed_ids)


if __name__ == "__main__":
    main()
