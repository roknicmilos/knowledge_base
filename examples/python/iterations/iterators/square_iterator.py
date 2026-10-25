class SquareIterator:
    """
    Iterator that is TRANSFORMING the input data. Takes a data stream,
    transform each item, and yield transformed items. Computes items on
    demand (one at a time) without storing them in memory. In this regard,
    iterators are lazy objects.
    """

    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._sequence):
            square = self._sequence[self._index] ** 2
            self._index += 1
            return square
        else:
            raise StopIteration
