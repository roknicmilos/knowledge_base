# C#: IDisposable, encapsulation, exceptions

## IDisposable

- An interface in .NET for releasing **unmanaged resources** (file handles, DB connections, sockets, native memory) –
  and for
  deterministically releasing managed ones that hold them (e.g. `DbContext`).
- *Deterministic* = cleanup happens at a known, controlled time (when you call `Dispose()` / leave the `using` scope),
  as
  opposed to the garbage collector, which runs non-deterministically.
- Managed memory is reclaimed by the GC; unmanaged resources need explicit cleanup.
- Defines a single method: `void Dispose();`
- Use the `using` statement (or C# 8 `using var x = …;` declaration) so `Dispose` is always called:
  ```csharp
  using (var resource = new ResourceHolder()) { /* ... */ }
  ```
- Related: `IAsyncDisposable` / `await using` for async cleanup; the full dispose pattern with finalizers/`SafeHandle`
  when a
  class directly owns unmanaged handles.

Equivalents: Java [try-with-resources](../java/try-with-resources.md),
Python [context managers](../python/context-managers.md).

## Encapsulation in C#

Achieved with:

- **Access modifiers**
    - `private` – same class only (default for class members)
    - `protected` – same class and derived classes
    - `public` – everywhere
    - `internal` – same assembly (default for top-level types)
    - `protected internal` – protected **or** internal
    - (also `private protected`, `file`)
- **Properties** – controlled access to private fields: `public string Name { get; set; }`
- **Methods** – encapsulate behavior and give indirect access to private data.

General concept: [OOP](../../fundamentals/oop.md).

## Exception handling in C#

`try / catch / finally` (see [exception handling](../../fundamentals/exception-handling.md)):

- `try` – code that might throw.
- `catch` – specific or general exceptions; multiple blocks allowed, **most specific first**; filters with `when (...)`.
- `finally` – always runs; cleanup.
- Variations: `try-catch-finally`, `try-catch`, `try-finally`.
- Re-throw with `throw;` (keeps the stack trace), not `throw ex;`.
