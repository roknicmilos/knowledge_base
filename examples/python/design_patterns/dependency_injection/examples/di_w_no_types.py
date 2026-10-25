"""
Dependency Injection (DI) + Dependency Inversion Principle (DIP):
    > Injecting dependency without specifying concrete implementation

In this example, we are injecting the EmailService dependency into the
UserService without specifying the concrete implementation of EmailService
inside UserService. This way, we are adhering to the DIP by depending on
abstractions rather than concrete implementations.
"""


class UserService:

    # Injecting the EmailService dependency without
    # specifying its concrete implementation:
    def __init__(self, email_service):
        self._email_service = email_service

    def send_email(self, to_address: str, subject: str, body: str) -> None:
        self._email_service.send_email(to_address, subject, body)


if __name__ == "__main__":
    from helpers.email_service import EmailService

    _email_service = EmailService(from_address="sender@example.com")
    user_service = UserService(email_service=_email_service)
    user_service.send_email(
        to_address="recipient@example.com",
        subject="Hello from DI + DIP",
        body=(
            "\n\tThis email is sent using Dependency Injection and "
            "\n\tadheres to the Dependency Inversion Principle by "
            "\n\tinjecting the EmailService dependency without specifying "
            "\n\tits concrete implementation inside UserService."
        )
    )
