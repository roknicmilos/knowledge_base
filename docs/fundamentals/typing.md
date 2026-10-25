# Typing: dynamic vs static, strong vs weak

Two independent axes.

## Dynamic vs static (when are types checked?)

|                   | Dynamically typed                  | Statically typed                      |
|-------------------|------------------------------------|---------------------------------------|
| Type checking     | At runtime                         | At compile time / by a static checker |
| Error detection   | Later (runtime)                    | Earlier                               |
| Development speed | Faster to write (less boilerplate) | More declarations                     |
| Flexibility       | High (variable types can change)   | Types are fixed                       |
| Large projects    | Needs discipline/tests/type hints  | Types document and protect refactors  |
| Examples          | Python, JavaScript, Ruby, PHP      | C, Java, Rust, C#, TypeScript         |

Performance differences come mostly from compilation/JIT, not typing alone. Gradual typing (Python type hints,
TypeScript, PHP type declarations) sits in the middle – see [Python type hints](../languages/python/type-hints.md).

## Strong vs weak (are implicit conversions allowed?)

- **Strong:** operations on incompatible types raise an error unless you convert explicitly.
  Python: `"5" + 10` → `TypeError`.
- **Weak:** the runtime converts silently. JavaScript: `"5" + 10 === "510"`; PHP converts types when needed (unless
  `declare(strict_types=1)` is used for function signatures).

| Language   | Static/Dynamic | Strong/Weak                |
|------------|----------------|----------------------------|
| Python     | Dynamic        | Strong                     |
| JavaScript | Dynamic        | Weak                       |
| PHP        | Dynamic        | Weak (optionally stricter) |
| Java, C#   | Static         | Strong                     |
| C          | Static         | Weak-ish (implicit casts)  |
