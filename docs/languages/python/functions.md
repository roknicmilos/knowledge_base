# Functions, lambdas, decorators, generators

## Functions are first-class objects

Everything in Python is an object, including functions. They can be assigned to variables, passed as arguments, returned
from other functions and stored in data structures. This enables decorators, higher-order functions and dynamic function
generation, and suits functional programming patterns.

## Lambda functions

- Anonymous function defined with `lambda`; still an ordinary function object.
- `__name__` is always `<lambda>`; you can't write a docstring (`__doc__` is `None`).
- **Limitations:** a single expression only (no statements), no annotations, poor readability beyond simple expressions.
- **Use for** short throwaway callbacks – `map()`, `filter()`, `sorted(key=...)` – when naming the function adds
  nothing.

## Decorators

A decorator is a function that takes a function, adds behavior and returns a new function (usually a `wrapper`).
`@decorator_name` is syntactic sugar for `func = decorator_name(func)`. Use `functools.wraps` inside to preserve the
wrapped function's name and docstring.

Use cases: logging, access control, caching, performance monitoring, reusable cross-cutting concerns (validation).

```python
import functools, time

def timed(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            print(f"{func.__name__} took {time.perf_counter() - start:.3f}s")
    return wrapper

@timed
def work(): ...
```

### Class decorators

A decorator can take a **class** and return a modified (or new) class – possible because classes are objects too.

## `yield` and generators

`yield` creates a **generator**: an iterable that produces values lazily, one at a time, instead of building everything
in memory.

- A function containing `yield` is a generator function; calling it returns a generator object without running the body.
- `yield` **pauses** the function and saves its state; the next iteration resumes there (unlike `return`, which ends
  it).
- Lazy evaluation – values only on request.

```python
def generate_numbers():
    for i in range(5):
        yield i

gen = generate_numbers()
print(next(gen))  # 0
print(next(gen))  # 1
```

```python
def return_example():
    return 1
    return 2      # never reached

def yield_example():
    yield 1
    yield 2

print(list(yield_example()))   # [1, 2]
```

**Use cases:** processing large files/datasets without loading them whole, infinite sequences, streaming data.
**Advantages:** memory efficiency, simpler code than hand-written iterators, values computed on demand. See
[iterators](iterators.md).

## Comprehensions

Concise constructs for creating collections by transforming/filtering others: list comprehension, dict comprehension,
set comprehension and generator expressions. Advantages: conciseness, readability, often faster than the equivalent
loop.

```python
squares = [n * n for n in range(10) if n % 2 == 0]
lookup = {u.id: u for u in users}
unique = {s.lower() for s in names}
lazy = (n * n for n in range(10**9))   # generator expression – nothing computed yet
```
