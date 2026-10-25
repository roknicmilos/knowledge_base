from abc import ABC, abstractmethod

class EmailServiceInterface(ABC):

    @abstractmethod
    def send_email(self, to_address: str, subject: str, body: str) -> None: ...
