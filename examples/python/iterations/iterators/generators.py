def sequence_generator_a(sequence):
    """
    Generator that is YIELDING the ORIGINAL data. Takes a stream of data and
    yields data items as they appear in the original data.
    """
    for item in sequence:
        yield item


def sequence_generator_b(sequence):
    """
    Same as `sequence_generator_a` but using the `yield from` statement which
    is a more concise way to yield items from an iterable.
    """
    yield from sequence


generator_expression = (i for i in range(10))
