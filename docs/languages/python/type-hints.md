# Type hints (annotations)

Using type hints is recommended for most projects and is standard in modern Python.

## Benefits

- **Readability** – easier for other developers (and future you).
- **Catches errors early** – a static checker flags mismatches (e.g. a `str` passed where an `int` is expected).
- **IDE support** – better autocompletion, inline errors and navigation (PyCharm, VS Code).
- **Safer refactoring** – you can trace where a type is used.
- **Documentation** – inline documentation of signatures and attributes.

## When you might skip them

Quick throwaway scripts; early prototyping while types change constantly.

## Tools

Type hints are **not enforced at runtime** – a separate static checker validates them.

- **mypy** – the reference static type checker. Checks annotations without running the code; by default it skips
  functions
  that have no annotations (use `--check-untyped-defs` / `--strict` to be stricter).
- **Pyright** (Pylance in VS Code) – fast checker with incremental checks and strong type inference.
- **ty** (Astral) and **Pyrefly** (Meta) – newer Rust-based checkers. *Verify their maturity before adopting.*
- **Ruff** is a **linter/formatter, not a type checker**. It can *require* annotations (the `ANN` rules) but doesn't
  verify
  types – see [tooling](tooling.md).
