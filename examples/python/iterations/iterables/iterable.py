from iterations.iterators.sequence_iterator import SequenceIterator


class Iterable:

    def __init__(self, sequence):
        self.sequence = sequence

    def __iter__(self):
        return SequenceIterator(self.sequence)
