# Behavioral Design Patterns

Behavioral design patterns are concerned with algorithms and the assignment of
responsibilities between objects. They describe patterns of communication
between objects.

---

## Observer Design Pattern

**What It Is**: A behavioral pattern that defines a one-to-many dependency
between objects, where when one object (the subject) changes state, all
dependent objects (observers) are automatically notified and updated.

**Purpose**: Solves the problem of keeping multiple objects synchronized without
tight coupling. It lets objects subscribe to events happening in another object
without the subject needing to know concrete observer implementations.

**Benefits**:

* Promotes loose coupling between subjects and observers.
* Supports dynamic subscription — observers can be added or removed at runtime.
* Enables broadcast communication: one change notifies many observers.
* Follows the Open/Closed Principle — add new observers without modifying the
  subject.
* Simplifies event-driven and reactive architectures where UI or other systems
  update automatically when data changes.

**Common Use Cases You've Seen**: Django signals (post_save, pre_delete), event
listeners in JavaScript, pub/sub messaging systems, real-time notifications, and
reactive frameworks where UI updates automatically when underlying data changes.

[Example in Python](examples/observer.py)

---

## Strategy Design Pattern

**What It Is**: A behavioral pattern that defines a family of interchangeable
algorithms or behaviors, encapsulates each one, and makes them interchangeable
at runtime. The client can choose which algorithm to use without knowing
implementation details.

**Purpose**: Solves the problem of having multiple ways to perform a task by
allowing you to select the algorithm or behavior at runtime. Eliminates complex
conditional statements by replacing them with separate strategy classes.

**Benefits**:

* Eliminates complex if/else or switch statements for different behaviors.
* Makes algorithms interchangeable and easy to swap at runtime.
* Promotes the Open/Closed Principle — add new strategies without modifying
  existing code.
* Encapsulates algorithm details, keeping client code clean and simple.
* Makes testing easier by allowing strategies to be tested independently.
* Supports dependency injection — strategies can be injected from outside.

**Common Use Cases You've Seen**: Django's authentication backends (different
login strategies), payment processing methods (credit card, PayPal, crypto),
sorting algorithms, validation strategies, serialization formats (JSON, XML),
and caching backends (Redis, Memcached, file-based).

[Example in Python](examples/strategy.py)

---

## Chain of Responsibility Design Pattern

**What It Is**: A behavioral pattern that passes a request along a chain of
handler objects. Each handler can either process the request or forward it to
the next handler in the chain until one of them handles it.

**Purpose**: Solves the problem of decoupling the sender of a request from its
receivers by allowing multiple objects a chance to handle the request. It
removes direct coupling between caller and handler and makes the chain
configurable at runtime.

**Benefits**:

* Decouples request senders from receivers, improving modularity.
* Supports dynamic composition of handlers — add, remove, or reorder handlers at
  runtime.
* Promotes Single Responsibility — each handler focuses on one kind of
  processing.
* Makes it easy to extend processing steps without changing existing handlers.
* Enables fallback processing: if one handler can't handle a request, another
  may.

**Common Use Cases You've Seen**: Web framework middleware (Django, FastAPI),
request/response pipelines, validation chains, logging filters,
authentication/authorization chains, and layered processing where different
components handle different aspects of a request.

[Example in Python](./examples/chain_of_responsibility.py)

---

## TODO: Command Design Pattern

---

## TODO: Iterator Design Pattern

---

## TODO: Mediator Design Pattern

---

## TODO: State Design Pattern

---

## TODO: Template Method Design Pattern

---

## TODO: Visitor Design Pattern

---

## TODO: Memento Design Pattern