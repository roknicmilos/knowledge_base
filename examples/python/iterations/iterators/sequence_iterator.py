from collections.abc import Iterator


class SequenceIterator(Iterator):
    """
    Iterator that is YIELDING the ORIGINAL data. Takes a stream of data and
    yields data items as they appear in the original data.
    """

    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0

    # Because we are inheriting from `Iterator` we don't need to implement
    # the required `__iter__` method. The `Iterator` class already has it
    # implemented.

    def __next__(self):
        if self._index < len(self._sequence):
            item = self._sequence[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration
