# Dependency Injection

**Dependency Injection (DI)** is a pattern where the dependencies of a class/function (services, DB connections,
configuration) are *provided* to it instead of being created inside it. Makes code more modular, testable (dependencies
can be mocked) and maintainable.

Not to be confused with:

- **IoC (Inversion of Control)** – the general idea that a framework/container calls your code and wires things.
- **Dependency Inversion Principle** – the "D" in [SOLID](solid.md); DI is one way to follow it.

## .NET / ASP.NET Core

ASP.NET Core ships with a built-in DI container. When registering a service you choose its **lifetime**:

| Lifetime      | Instance                                  | Good for                                            |
|---------------|-------------------------------------------|-----------------------------------------------------|
| **Transient** | New instance every time it's requested    | Lightweight, stateless services                     |
| **Scoped**    | One instance per scope (per HTTP request) | Services tied to a request – e.g. DB context        |
| **Singleton** | One instance for the whole application    | Caches, configuration, logging; must be thread-safe |

Pitfall: a singleton that depends on a scoped/transient service captures it for the app's lifetime (**captive
dependency**). ASP.NET Core throws on this in Development when scope validation is enabled.

## FastAPI

FastAPI does DI with `Depends` – see [FastAPI dependency
injection](../languages/python/frameworks/fastapi.md#dependency-injection).

More Python examples:
[`examples/python/design_patterns/dependency_injection`](../../examples/python/design_patterns/dependency_injection/README.md)
