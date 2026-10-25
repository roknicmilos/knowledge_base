# Dependency Injection (DI) Pattern

DI is a design pattern where a class/function doesn’t create its own
dependencies, but instead receives them from the outside (injected).

**DI and interfaces**: DI does not require interfaces. You can use DI and you
can achieve the Dependency Inversion Principle (DIP, one of the SOLID
principles) without interfaces! Interfaces just make it cleaner, especially in
strongly typed languages (Java, C#).

## Dependency Injection vs Dependency Inversion Principle

While DI is a design pattern, **DIP is an architectural principle** rather than
a pattern. DIP prescribes how high-level and low-level modules should relate
through abstractions, fundamentally shaping the dependency flow and layer
structure across the entire system. DI is one of the primary techniques used to
implement DIP in practice.

* DI: “Here’s how you provide dependencies from the outside”
* DIP: “Depend on abstraction”

### DI with and without DIP

| Method                 | DI | DIP |
|------------------------|----|-----|
| DI without types       | ✓  | ✓   |
| DI with interfaces     | ✓  | ✓   |
| DI with concrete impl. | ✓  | ❌   |

* **DI without types**: Dependencies are injected from outside, but
  no type annotations are used (common in dynamic languages like Python,
  JavaScript). [Example in Python](./examples/di_w_no_types.py)
* **DI with interfaces**: Dependencies are injected and typed with
  abstract interfaces/protocols (e.g., `Protocol` in Python, interfaces in
  Java/C#). High-level modules depend on abstractions, not concrete
  implementations. [Example in Python](./examples/di_w_interfaces.py)
* **DI with concrete implementations**: Dependencies are injected but typed
  with concrete classes rather than abstractions, creating tight coupling.
  [Example in Python](./examples/di_w_concrete_impl.py)

## Benefits of DI

* Decouples components, making them easier to test and maintain.
* Promotes adherence to DIP by allowing high-level modules to depend on
  abstractions.
* Enhances flexibility and configurability of components.

## Drawbacks of DI

* Increases complexity due to additional layers of abstraction.
* Can lead to over-engineering if not used judiciously.
* May introduce performance overhead in some scenarios.