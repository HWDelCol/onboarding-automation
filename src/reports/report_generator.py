from datetime import datetime
from pathlib import Path


REPORTS_DIR = Path("reports")
REPORTS_DIR.mkdir(exist_ok=True)


def generate_onboarding_report(processed_employees: list[dict]) -> Path:
    """
    Gera um relatório simples de onboarding e retorna o caminho do arquivo.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_path = REPORTS_DIR / f"onboarding_report_{timestamp}.txt"

    with report_path.open("w", encoding="utf-8") as file:
        file.write("RELATÓRIO DE ONBOARDING\n")
        file.write("=" * 30 + "\n\n")
        file.write(f"Data/Hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"Total processados: {len(processed_employees)}\n\n")

        if not processed_employees:
            file.write("Nenhum funcionário processado nesta execução.\n")
        else:
            file.write("Funcionários onboardados:\n")
            for emp in processed_employees:
                file.write(
                    f"- {emp['name']} | "
                    f"{emp['department']} | "
                    f"{emp['email']}\n"
                )

    return report_path
