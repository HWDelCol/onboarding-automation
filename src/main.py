from readers.csv_reader import read_employees
from services.onboarding import get_new_employees, save_processed
from services.email_service import send_welcome_email
from reports.report_generator import generate_onboarding_report


def main():
    employees = read_employees("data/employees.csv")
    new_employees = get_new_employees(employees)

    if not new_employees:
        print("Nenhum novo funcionário para onboarding.")
        generate_onboarding_report([])
        return

    processed_ids = set()

    for emp in new_employees:
        print(f"Iniciando onboarding para: {emp['name']}")
        send_welcome_email(emp)
        processed_ids.add(emp["employee_id"])

    save_processed(processed_ids)

    report_path = generate_onboarding_report(new_employees)
    print(f"Relatório gerado em: {report_path}")


if __name__ == "__main__":
    main()