class FibonacciIterator:
    """
    Iterator that is GENERATING new data (Fibonacci numbers). Takes no input
    data, generating new data as a result of some computation to finally yield
    the generated items.
    Note that the Fibonacci sequence is infinite, so we need to specify a
    stopping condition to avoid running forever. This is done by setting a
    stopping condition in the constructor.
    """

    def __init__(self, stop: int | None = 10):
        self._stop = stop
        self._index = 0
        self._current = 0
        self._next = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._stop is None or self._index < self._stop:
            self._index += 1
            fib_number = self._current
            self._current, self._next = (
                self._next,
                self._current + self._next,
            )
            return fib_number
        else:
            raise StopIteration
