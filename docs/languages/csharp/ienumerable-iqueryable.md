# C#: IEnumerable, enumeration, IQueryable

## `IEnumerable<T>`

- Interface (`System.Collections.Generic`; non-generic version in `System.Collections`) for a collection of objects that
  can be enumerated (iterated).
- Supports `foreach`; exposes `GetEnumerator()`, which returns an enumerator.
- Read-only view – you can't add/remove items through it.
- Used for arrays, lists and any custom collection you want to make enumerable.

## Enumeration (IEnumerator)

`foreach` calls `GetEnumerator()` and uses the enumerator's members:

- `MoveNext()` – advance to the next element (returns `false` at the end),
- `Current` – the current element,
- `Reset()` – back to before the first element (rarely used; compiler-generated iterators throw
  `NotSupportedException`).

With `foreach`:

```csharp
IEnumerable<int> numbers = new List<int> { 1, 2, 3, 4, 5 };
foreach (var num in numbers)      // uses GetEnumerator() under the hood
{
    Console.WriteLine(num);
}
```

Manually:

```csharp
IEnumerator<int> enumerator = numbers.GetEnumerator();
while (enumerator.MoveNext())
{
    Console.WriteLine(enumerator.Current);
}
```

## `.ToList()`

A LINQ extension (`System.Linq`) that converts an `IEnumerable<T>` into a `List<T>`. It **always enumerates the whole
sequence** (materializes it), so watch performance. Use it when you need a mutable, indexable collection or want to run
a deferred query exactly once.

## IEnumerable vs IQueryable

| Feature           | `IEnumerable<T>`               | `IQueryable<T>`                                |
|-------------------|--------------------------------|------------------------------------------------|
| Namespace         | `System.Collections.Generic`   | `System.Linq`                                  |
| Execution         | Client-side, in memory         | Server-side, in the data source                |
| Query execution   | Deferred (LINQ to Objects)     | Deferred                                       |
| Query translation | None – delegates run in memory | Expression trees translated, e.g. to SQL       |
| Performance       | Processes the whole collection | Fetches only the necessary data                |
| Use case          | In-memory collections          | External data sources like databases (EF Core) |

- Both defer execution until enumerated (`foreach`, `.ToList()`…). That is **deferred execution** – not to be confused
  with ORM "lazy loading". Not every `IEnumerable` is deferred: an in-memory `List<T>` or array already holds all its
  data.
- `IEnumerable` – small data already in memory; `IQueryable` – large datasets from a database.
- Pitfall: calling `AsEnumerable()` / `ToList()` **before** `Where(...)` on an EF Core query pulls the entire table into
  memory and filters there.
