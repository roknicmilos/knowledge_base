# Exception handling

Languages use `try/catch/finally` (C#, Java, JS, PHP) or `try/except/else/finally` (Python).

- Put code that may raise inside `try`; handle general or specific exceptions in `catch`/`except`.
- Several handlers can follow; put **specific** exception types first and general ones last.
- A `catch` block is optional **if** a `finally` block is present (`try-finally`).
- `finally` runs whether or not an exception occurred – use it for cleanup (closing files/connections).
  Prefer language constructs that do this for you: Python [`with`](../languages/python/context-managers.md), Java
  [try-with-resources](../languages/java/try-with-resources.md), C# [
  `using`/IDisposable](../languages/csharp/idisposable.md).
- Python only: `else` runs when the `try` block raised nothing.
- Variations: `try-catch-finally`, `try-catch` (no cleanup needed), `try-finally` (cleanup only).

## Re-throwing

|                       | Preserves original stack trace?                                            | Notes                             |
|-----------------------|----------------------------------------------------------------------------|-----------------------------------|
| C# `throw;`           | Yes                                                                        | Use this almost always            |
| C# `throw ex;`        | **No** – trace restarts at the `throw ex` line                             | Almost never use                  |
| Python `raise` (bare) | Yes                                                                        | Preferred way to re-raise         |
| Python `raise ex`     | Mostly yes – the original traceback is kept and the re-raise line is added | Not worth using over bare `raise` |

### Python exception chaining

```python
try:
    low_level()
except OSError as ex:
    raise DomainError("could not load config") from ex   # explicit cause → __cause__
```

- `raise X from ex` – traceback says *"The above exception was the direct cause of the following exception"*.
- `raise X` inside an `except` block – implicit chaining (`__context__`): *"During handling of the above exception,
  another exception occurred"*.
- `raise X from None` – suppress the chain.

## Handling several specific types

Python:

```python
try:
    risky_code()
except (ValueError, KeyError) as e:
    print(f"Caught an exception: {e}")
```

C# (exception filter):

```csharp
try
{
    RiskyCode();
}
catch (Exception e) when (e is FormatException || e is ArgumentException)
{
    Console.WriteLine($"Caught an exception: {e.Message}");
}
```
