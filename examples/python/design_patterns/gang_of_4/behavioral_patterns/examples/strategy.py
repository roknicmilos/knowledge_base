"""
Strategy Pattern

What it does:
    Defines a family of algorithms, encapsulates each one,
    and makes them interchangeable. Strategy lets the algorithm
    vary independently from clients that use it.

Non-pattern alternative: Conditional statements
    Without the Strategy pattern, you might use conditional statements
    (like if-else or switch-case) to select different algorithms
    at runtime. This approach can lead to code that is hard to maintain
    and extend, as adding new algorithms would require modifying
    existing code, violating the Open-Closed Principle (OCP).
    The Strategy pattern encapsulates each algorithm in its own class,
    allowing you to add new algorithms without changing existing code.
"""

from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        pass


class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str, name: str):
        self.card_number = card_number
        self.name = name

    def pay(self, amount: float) -> str:
        return (
            f"Paid {amount:.2f} using Credit Card {self.card_number[-4:]} "
            f"({self.name})"
        )


class PayPalPayment(PaymentStrategy):
    def __init__(self, email: str):
        self.email = email

    def pay(self, amount: float) -> str:
        return f"Paid {amount:.2f} using PayPal account {self.email}"


class BitcoinPayment(PaymentStrategy):
    def __init__(self, wallet_address: str):
        self.wallet_address = wallet_address

    def pay(self, amount: float) -> str:
        return f"Paid {amount:.2f} BTC to wallet {self.wallet_address[:10]}..."


# Context that uses a strategy
class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy) -> None:
        """Allow changing strategy at runtime"""
        self._strategy = strategy

    def process_payment(self, amount: float) -> str:
        return self._strategy.pay(amount)


if __name__ == "__main__":
    # Create different strategies
    credit_card = CreditCardPayment("1234-5678-9012-3456", "John Doe")
    paypal = PayPalPayment("john@example.com")
    bitcoin = BitcoinPayment("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")

    # Start with credit card
    processor = PaymentProcessor(credit_card)

    print("--- Using Credit Card ---")
    print(processor.process_payment(250.00))

    # Switch to PayPal at runtime
    processor.set_strategy(paypal)
    print("\n--- Switched to PayPal ---")
    print(processor.process_payment(150.50))

    # Switch to Bitcoin
    processor.set_strategy(bitcoin)
    print("\n--- Switched to Bitcoin ---")
    print(processor.process_payment(0.05))  # Small BTC amount
