# Context managers

Manage resources so they're always acquired and released – even when an error occurs. Typical for files, DB connections
and
locks.

## Concepts

- **`with` statement** – runs setup and cleanup around a block.
- **Context manager protocol** – an object implementing `__enter__` (runs at block start; its return value is bound by
  `as`) and `__exit__` (runs at block end, even on exception; handles cleanup).

```python
# Without a context manager
file = open('example.txt', 'r')
try:
    content = file.read()
finally:
    file.close()

# With a context manager
with open('example.txt', 'r') as file:
    content = file.read()
# file is closed here
```

## Custom context manager

Class-based:

```python
class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")
        if exc_type is not None:
            print(f"An exception occurred: {exc_value}")
        return False   # True would SUPPRESS the exception – only do that deliberately
```

With `contextlib.contextmanager`:

```python
from contextlib import contextmanager

@contextmanager
def my_context_manager():
    print("Entering the context")
    try:
        yield "resource"
    finally:
        print("Exiting the context")

with my_context_manager() as resource:
    print(f"Inside the context with {resource}")
```

Also useful: `contextlib.suppress(...)`, `contextlib.ExitStack`, and `async with` for async resources.

## Benefits

Resource management, error handling (cleanup guaranteed), readability (setup/teardown encapsulated).

## Use cases

File handling, database connections, threading locks, temporary changes of settings/state that are reverted afterwards.
Java equivalent: [try-with-resources](../java/try-with-resources.md); C#: [IDisposable](../csharp/idisposable.md).
