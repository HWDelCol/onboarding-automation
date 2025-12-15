from datetime import datetime


def send_welcome_email(employee: dict) -> None:
    """
    Simula o envio de email de boas-vindas para o funcionário.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(
        f"[{timestamp}] Email enviado para {employee['email']} "
        f"({employee['name']})"
    )