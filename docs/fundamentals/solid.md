# SOLID

Five object-oriented design principles.

| Principle                 | Statement                                                                                           | Benefit                                                 | Tiny example                                                               |
|---------------------------|-----------------------------------------------------------------------------------------------------|---------------------------------------------------------|----------------------------------------------------------------------------|
| **S**ingle Responsibility | A class has one job – one reason to change                                                          | Easier to test, less complexity                         | `Invoice` calculates totals; `InvoicePrinter` prints them                  |
| **O**pen/Closed           | Open for extension, closed for modification                                                         | Stability – new behavior doesn't risk existing behavior | Add a new `DiscountStrategy` class instead of another `if` in `checkout()` |
| **L**iskov Substitution   | Subclass objects can replace superclass objects without breaking correctness                        | Reliable inheritance hierarchies                        | `Square` that extends `Rectangle` but breaks `set_width` violates LSP      |
| **I**nterface Segregation | Clients shouldn't depend on interfaces they don't use; prefer several small interfaces              | Decoupling, flexibility                                 | Split `Machine` into `Printer`, `Scanner`                                  |
| **D**ependency Inversion  | High-level modules depend on abstractions, not on low-level modules; details depend on abstractions | Decoupling, easier refactoring/testing                  | `OrderService` takes a `PaymentGateway` interface, not `StripeClient`      |

Related: [dependency injection](dependency-injection.md) (a technique that implements DIP), [OOP](oop.md).
