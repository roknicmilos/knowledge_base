# Structural Design Patterns

Structural design patterns focus on how classes and objects are composed to form
larger structures. They help ensure that if one part of a system changes, the
entire structure doesn't need to change.

---

## Adopter Design Pattern

**What It Is**: A structural pattern that allows incompatible interfaces to work
together by wrapping an object with a new interface that translates between the
expected interface and the actual implementation.

**Purpose**: Solves the problem of integrating classes or systems that have
incompatible interfaces. Acts as a translator or converter, allowing you to use
existing code with new systems without modifying the original code.

**Benefits**:

* Enables integration of incompatible interfaces without modifying existing
  code.
* Promotes code reuse by adapting existing classes to new contexts.
* Supports the Single Responsibility Principle by separating interface
  conversion from business logic.
* Makes legacy code work with modern systems with minimal changes.
* Allows swapping implementations easily by changing the adapter rather than
  client code.
* Keeps client code clean and independent of specific implementations.

**Common Use Cases You've Seen**: Django's database backends (adapting different
databases to the ORM interface), payment gateway wrappers (adapting
Stripe/PayPal to your payment interface), and API client libraries that wrap
third-party APIs with a cleaner interface.

[Example in Python](examples/adopter.py)

---

## Proxy Design Pattern

**What It Is**: A structural pattern that provides a surrogate or placeholder
object that controls access to another object, acting as an intermediary between
the client and the real object.

**Purpose**: Solves the problem of controlling access to an object by adding an
extra layer of indirection. The proxy can add functionality like lazy loading,
access control, caching, logging, or remote access handling without changing the
original object.

**Benefits**:

* Enables lazy initialization — create expensive objects only when actually
  needed.
* Controls access through permission checks or validation before delegating to
  the real object.
* Adds caching to improve performance by avoiding repeated expensive operations.
* Provides logging, monitoring, or instrumentation without modifying the
  original object.
* Supplies a local representative for remote or expensive resources (making
  remote resources appear local).
* Protects the real object from direct manipulation by clients.

**Common Use Cases You've Seen**: Django's lazy querysets (delaying database
queries until needed), image lazy loading, authentication/authorization
middleware, ORM lazy relationships, remote stubs/proxies for web services.

[Example in Python](examples/proxy.py)

---

## Decorator Design Pattern

**What It Is**: A structural pattern that lets you add responsibilities to
individual objects dynamically by wrapping them with decorator objects. Each
decorator implements the same interface as the object it wraps and delegates
calls while adding behavior before or after delegation.

**Purpose**: Solves the problem of extending object behavior without creating a
large hierarchy of subclasses. Instead of modifying existing classes, you
compose behavior at runtime by stacking decorators.

**Benefits**:

* Adheres to the Open/Closed Principle — extend behavior without modifying
  existing code.
* Encourages Single Responsibility — each decorator focuses on one concern.
* Supports flexible composition — combine multiple decorators in different
  orders to vary behavior.
* Avoids subclass explosion — no need for many subclasses for every feature
  combination.
* Enables dynamic behavior changes at runtime.

**Common Use Cases You've Seen**: I/O stream wrappers, logging and
authentication middleware, caching wrappers, and function decorators in Python (
e.g., @wraps-based wrappers). Django middleware and WSGI middleware are
real-world examples of decorator-like composition.

[Example in Python](examples/decorator.py)

---

## TODO: Facade Design Pattern

---

## TODO: Composite Design Pattern

---

## TODO: Flyweight Design Pattern

---

## TODO: Bridge Design Pattern
