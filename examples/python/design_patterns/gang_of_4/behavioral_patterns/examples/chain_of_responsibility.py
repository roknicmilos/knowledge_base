"""
Chain of Responsibility Pattern

What it does:
    Avoids coupling the sender of a request to its receiver by giving more
    than one object a chance to handle the request. The request is passed
    along a chain of handlers until one of them handles it.

Non-pattern alternative: Conditional statements
    Without the Chain of Responsibility pattern, a client would need to use
    conditional statements (like if-else or switch-case) to determine which
    handler should process a request. This approach leads to tight coupling
    between the client and the handlers, making it difficult to add or
    remove handlers without modifying the client code.
"""
from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self, successor=None):
        self._successor = successor

    def handle(self, request):
        # Option #1: Call all handlers in the chain
        self._handle(request)
        if self._successor:
            self._successor.handle(request)

        # Option #2: Stop at the first handler that handles the request
        # handled = self._handle(request)
        # if not handled and self._successor:
        #     return self._successor.handle(request)

        print(f"{self.__class__.__name__}: handled {request}")

        # return handled # Uncomment if using Option #2

    @abstractmethod
    def _handle(self, request): ...


class NegativeHandler(Handler):
    def _handle(self, request):
        if request < 0:
            return True
        return False


class ZeroHandler(Handler):
    def _handle(self, request):
        if request == 0:
            return True
        return False


class PositiveHandler(Handler):
    def _handle(self, request):
        if request > 0:
            return True
        return False


if __name__ == "__main__":
    # Build the chain: Negative -> Zero -> Positive
    chain = NegativeHandler(ZeroHandler(PositiveHandler()))

    inputs = [-5, 0, 7, -1, 42]
    for i in inputs:
        # Option #1:
        chain.handle(i)

        # Option #2:
        # _handled = chain.handle(i)
        # if not _handled:
        #     print(f"No handler processed: {i}")

        print("-------------------------------------")
