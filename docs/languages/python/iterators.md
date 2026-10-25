# Iterators and iterables

Iterators power and control the iteration process; iterables typically hold the data you iterate over.
Source: [Iterators and Iterables in Python (Real Python)](https://realpython.com/python-iterators-iterables/).

## Iterables

An object you can iterate over (typically with a `for` loop): lists, tuples, dicts, sets, strings…

- **Iterable protocol:** one magic method, `__iter__()`, returning an iterator.
- Check whether something is iterable by passing it to `iter()` – `TypeError: 'int' object is not iterable` otherwise.
- **Sequence protocol** (`__len__` + `__getitem__`) is an alternative: even without `__iter__`, `iter()` builds an
  iterator from it.
- `for` loops always call `iter()` on the target to get an iterator.
- Passing an iterable that isn't an iterator to `next()` raises `TypeError: 'list' object is not an iterator`.
- `reversed()` uses `__reversed__()` if present, otherwise `__len__` + `__getitem__`.

## Iterators

Objects that return data from a stream/container one item at a time and keep track of the current position.

- **Iterator protocol:** `__iter__()` (usually `return self`) and `__next__()`, which raises `StopIteration` when
  exhausted.
- Iterators can: yield items from existing data, transform items, or generate new data from computation.
- **Infinite iterators** (never raise `StopIteration`) run forever in a `for` loop and make `sum()`, `max()`, `min()`
  hang.
- **Generator iterators** – generator functions/expressions give the same thing with far less code
  (see [functions](functions.md#yield-and-generators)).

### Async iterators

`__iter__` → `__aiter__` (not itself async), `__next__` → `__anext__` (awaitable), `StopIteration` →
`StopAsyncIteration`.

### Constraints of iterators

- can't be iterated more than once; exhausted ones can't be reset,
- only forward – no going back,
- no length, no indexing or slicing.

## Iterators vs iterables

| Feature                        | Iterators | Iterables |
|--------------------------------|-----------|-----------|
| Usable directly in `for` loops | ✅        | ✅        |
| Can be iterated many times     | ❌        | ✅        |
| Support `iter()`               | ✅        | ✅        |
| Support `next()`               | ✅        | ❌        |
| Keep iteration state           | ✅        | ❌        |
| Optimize memory use            | ✅        | ❌        |

All iterators are iterables (they implement `__iter__`), but not all iterables are iterators (only those with
`__next__`).
Lists/tuples/dicts/sets/strings are iterables, **not** iterators.

## Memory efficiency

Iterators and generators keep one item in memory at a time and compute the next on demand. They decouple iteration from
processing, so you can chain stages into memory-efficient pipelines, and they are the only way to process infinite
streams.
For custom container classes implement the iterable protocol so they work in `for` loops.

Examples: [`examples/python/iterations`](../../../examples/python/iterations/README.md).
