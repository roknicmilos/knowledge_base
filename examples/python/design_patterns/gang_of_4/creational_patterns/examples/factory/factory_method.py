"""
Factory Method Pattern

What it does:
    Base class defines a method, subclasses decide
    the concrete implementation.
"""

from abc import abstractmethod, ABC


class PaymentProvider(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class PayPal(PaymentProvider):

    def pay(self, amount):
        return f"Paid {amount} via PayPal"


class Crypto(PaymentProvider):

    def pay(self, amount):
        return f"Paid {amount} in crypto"


class PaymentService(ABC):
    _provider: PaymentProvider = None

    @abstractmethod
    def create_provider(self) -> PaymentProvider:
        pass

    @property
    def provider(self) -> PaymentProvider:
        if not self._provider:
            self._provider = self.create_provider()
        return self._provider

    def checkout(self, amount):
        return self.provider.pay(amount)


class PayPalService(PaymentService):

    def create_provider(self):
        return PayPal()


class CryptoService(PaymentService):

    def create_provider(self):
        return Crypto()


service = CryptoService()
print(service.checkout(200))
