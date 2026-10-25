# Python

Created by [Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum), first released in 1991. Known for simple,
readable syntax. The reference implementation, **CPython**, is written in C and open source.

- Extensive standard library and ecosystem; large community; multi-paradigm (procedural, OOP, functional).
- Used in web development, data science, ML/AI, automation, scripting – a general-purpose language.
- **Pros:** easy to learn, rapid development, huge community. **Cons:** slower than compiled languages (C++), more
  memory,
  less suited to low-level or very high-performance work.

## Language characteristics

- **Suitable for rapid development** – readable syntax, comprehensive standard library, strong community; fast
  prototyping.
- **Interpreted (bytecode VM)** – CPython compiles source to bytecode and runs it on a virtual machine (not
  line-by-line;
  an experimental JIT exists since 3.13). Great for development speed, slower runtime than compiled languages.
- **Dynamically typed** – types are determined at runtime: flexible and concise, but type errors surface at runtime. See
  [type hints](type-hints.md).
- **Strongly typed** – no implicit conversions between incompatible types:
  ```python
  x = "5"
  y = 10
  z = x + y   # TypeError: can only concatenate str (not "int") to str
  ```
  (a weakly typed language would silently convert). See [typing](../../fundamentals/typing.md).
- **Synchronous by default** – use `asyncio` for async I/O, `threading` for I/O-bound concurrency, `multiprocessing` for
  CPU-bound work: [concurrency](concurrency.md).

## Multi-paradigm

### Object-oriented

Python is OOP at its core – everything (functions, types, integers) is an object. Classes, inheritance, encapsulation,
polymorphism and abstraction are covered in [OOP](../../fundamentals/oop.md) (with Python examples).
See also [MRO](mro.md), [interfaces](interfaces.md), [metaclasses](metaclasses.md).

### Functional

- **First-class and higher-order functions** – functions can be passed and returned.
- **Pure functions** – same output for same arguments and no side effects (not enforced, but encouraged);
  **immutability**
  – data isn't modified after creation (not enforced either).
- Tools: `map()`, `filter()`, `functools.reduce()`, comprehensions, generators. See [functions](functions.md).

### Procedural

Sequences of instructions with functions, loops and conditionals – the simplest style for scripts and small utilities.

## Index of Python notes

| Topic                                      | Page                                                                                     |
|--------------------------------------------|------------------------------------------------------------------------------------------|
| Type hints and checkers                    | [type-hints.md](type-hints.md)                                                           |
| Method Resolution Order                    | [mro.md](mro.md)                                                                         |
| Interfaces: duck typing, ABC, Protocol     | [interfaces.md](interfaces.md)                                                           |
| Functions, lambdas, decorators, generators | [functions.md](functions.md)                                                             |
| Iterators and iterables                    | [iterators.md](iterators.md)                                                             |
| Built-in data structures                   | [data-structures.md](data-structures.md)                                                 |
| Context managers                           | [context-managers.md](context-managers.md)                                               |
| Metaclasses                                | [metaclasses.md](metaclasses.md)                                                         |
| Concurrency, parallelism, GIL              | [concurrency.md](concurrency.md)                                                         |
| Package managers, linters, formatters      | [tooling.md](tooling.md)                                                                 |
| ORMs and migrations                        | [orm-and-migrations.md](orm-and-migrations.md)                                           |
| Frameworks (Django, FastAPI, Flask)        | [frameworks/](frameworks/comparison.md)                                                  |
| Exceptions (generic)                       | [../../fundamentals/exception-handling.md](../../fundamentals/exception-handling.md)     |
| Mocking/patching                           | [../../fundamentals/mocking-and-patching.md](../../fundamentals/mocking-and-patching.md) |

## Additional resources

- [Python docs](https://www.python.org/doc/) · [PEP 8 – style guide](https://peps.python.org/pep-0008/)
- [Python basics (Programiz)](https://www.programiz.com/python-programming/first-program) ·
  [Keywords](https://www.programiz.com/python-programming/keyword-list) ·
  [Operators](https://www.w3schools.com/python/python_operators.asp)
- [Float vs Decimal vs Fraction](https://www.laac.dev/blog/float-vs-decimal-python/)
- [Python Tips book](https://book.pythontips.com/) (older, Python-2-era examples)
- [Python GIL – Real Python](https://realpython.com/python-gil/)

> **TODO:** design patterns in Python (see <https://github.com/roknicmilos/python-stuff/tree/main/design_patterns>) and
> a
> page on built-in data *types*.
