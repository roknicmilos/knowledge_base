from helpers.email_service_interface import EmailServiceInterface


class EmailService(EmailServiceInterface):
    def __init__(self, from_address: str):
        self._from_address = from_address

    def send_email(self, to_address: str, subject: str, body: str) -> None:
        print(
            f"From: {self._from_address}\n"
            f"Recipient: {to_address}\n"
            f"Subject: {subject}\n"
            f"Body: {body}\n"
        )
