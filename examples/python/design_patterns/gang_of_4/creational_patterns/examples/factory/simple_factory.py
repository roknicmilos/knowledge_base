"""
Simple Factory Pattern

What it does:
    A single factory class with a method that
    creates different types of objects based on input.

Non-pattern alternative: Direct instantiation
    Directly instantiating objects throughout the codebase
    can lead to scattered and duplicated object creation logic.
    The Simple Factory pattern centralizes this logic in one place,
    making it easier to manage and modify object creation.
"""


class PayPalPayment:
    def pay(self, amount):
        return f"Paid {amount} via PayPal"


class CryptoPayment:
    def pay(self, amount):
        return f"Paid {amount} in crypto"


class CreditCardPayment:
    def pay(self, amount):
        return f"Paid {amount} with credit card"


class PaymentFactory:
    @staticmethod
    def create(method: str):
        match method:
            case "paypal":
                return PayPalPayment()
            case "crypto":
                return CryptoPayment()
            case "card":
                return CreditCardPayment()
            case _:
                raise ValueError("Unknown payment method")


p = PaymentFactory.create("crypto")
print(p.pay(100))
