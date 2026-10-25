"""
Abstract Factory Pattern

What it does:
    Provides an interface for creating families of related
    or dependent objects without specifying their concrete classes.
"""

from abc import abstractmethod, ABC


class Payment(ABC):
    @abstractmethod
    def pay(self, amount): ...


class Validator(ABC):
    @abstractmethod
    def validate(self, data): ...


class FeeCalculator(ABC):
    @abstractmethod
    def fee(self, amount): ...


class PayPalPayment(Payment):
    def pay(self, amount):
        return f"Paid {amount} via PayPal"


class PayPalValidator(Validator):
    def validate(self, data):
        return True


class PayPalFeeCalculator(FeeCalculator):
    def fee(self, amount):
        return amount * 0.03


class PaymentProviderFactory(ABC):
    @abstractmethod
    def create_payment(self) -> Payment: ...

    @abstractmethod
    def create_validator(self) -> Validator: ...

    @abstractmethod
    def create_fee_calculator(self) -> FeeCalculator: ...


class PayPalFactory(PaymentProviderFactory):
    def create_payment(self):
        return PayPalPayment()

    def create_validator(self):
        return PayPalValidator()

    def create_fee_calculator(self):
        return PayPalFeeCalculator()


factory = PayPalFactory()

payment = factory.create_payment()
validator = factory.create_validator()
fees = factory.create_fee_calculator()

print(payment.pay(300))
print(validator.validate({"card": "123"}))
print(fees.fee(300))
