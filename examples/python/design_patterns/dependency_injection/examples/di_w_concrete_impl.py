"""
Dependency Injection (DI) WITHOUT Dependency Inversion Principle (DIP):
    > Injecting dependency with concrete implementation

In this example, we are injecting the EmailService dependency into the
UserService by directly using the concrete implementation of EmailService
inside UserService. This way, we are NOT adhering to the DIP as UserService
depends on a concrete implementation rather than an abstraction.
"""
from helpers.email_service import EmailService


class UserService:

    def __init__(self, email_service: EmailService):
        self._email_service = email_service

    def send_email(self, to_address: str, subject: str, body: str) -> None:
        self._email_service.send_email(to_address, subject, body)


if __name__ == "__main__":
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
