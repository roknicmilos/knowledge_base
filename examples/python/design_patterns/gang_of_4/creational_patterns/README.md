# Creational Design Patterns

Creational design patterns deal with object creation mechanisms, helping create
objects in a manner suitable to the situation. The goal is to make the system
independent of how its objects are created and represented.

---

## Factory Design Patterns

**What It Is**: A creational pattern that provides an interface or method for
creating objects without specifying their exact classes. Instead of using
constructors directly, you ask a factory to create objects for you.

**Purpose**: Solves the problem of creating objects when you don't know the
exact class needed until runtime, or when object creation logic is complex.
Centralizes and encapsulates the creation logic so client code doesn't need to
know implementation details.

**Benefits**:

* Decouples client code from concrete classes, depending only on interfaces
* Centralizes object creation logic in one place, making it easier to maintain
* Supports Open/Closed Principle - easy to add new types without changing
  existing code
* Makes code more testable by allowing easy injection of mock objects
* Hides complex initialization logic from clients
* Enables runtime decision-making about which class to instantiate

**Common Use Cases You've Seen**: Django's Model.objects.create(), SQLAlchemy's
create_engine(), Python's open() function, and Pydantic's parse_obj() are all
factory patterns.

There are **3 different factory patterns**:

1. **Simple Factory** → “Call this function, and I’ll give you the right
   object.” [Example in Python](./examples/factory/simple_factory.py)
2. **Factory Method** → “Subclass decides what to create.”
   [Example in Python](./examples/factory/factory_method.py)
3. **Abstract Factory** → “Need a whole family of related objects? I’ll create
   them all for you.”
   [Example in Python](./examples/factory/abstract_factory.py)

---

## Singleton Design Pattern

**What It Is**: A creational pattern that ensures a class has only one instance
throughout the application's lifetime and provides a global access point to that
instance.

**Purpose**: Solves the problem of needing exactly one shared instance of a
class across your entire application, such as database connections,
configuration settings, or logging systems. Prevents multiple instances from
being created accidentally.

**Benefits**:

* Guarantees only one instance exists, saving memory and resources.
* Provides a single point of access to shared resources.
* Lazy initialization - instance created only when first needed.
* Thread-safe access to shared state (when implemented properly).
* Useful for managing shared resources like database connection pools, caches,
  or application configuration.

**Cons**:

* **Testing difficulties** - Singletons act as global state, making unit tests
  harder to isolate and mock. Tests can interfere with each other through a
  shared state.
* **Tight coupling** - Code becomes directly dependent on the concrete singleton
  implementation rather than an interface, reducing flexibility and making
  changes harder.

**Common Use Cases You've Seen**: Django's settings module, database connection
pools, application-wide cache instances, and logging systems are typically
implemented as singletons.

[Example in Python](./examples/singleton.py)

---

## Builder Design Pattern

**What It Is**: A creational pattern that constructs complex objects
step-by-step through a builder interface. It separates the construction of a
complex object from its representation so the same construction process can
create different representations.

**Purpose**: Solves the problem of objects with many parameters (especially
optional ones) or complex construction logic by allowing incremental, readable
construction instead of passing everything through a complicated constructor.

**Benefits**:

* Creates highly readable, self-documenting code through method chaining or a
  fluent API.
* Handles many optional parameters without constructor pollution.
* Allows building different variations of the same object type using different
  builders.
* Supports validation and constraints during the construction process.
* Enables immutable object creation by assembling all parts before final
  construction.

[Example in Python](./examples/builder.py)

---

## Prototype Design Pattern

**What It Is**: A creational pattern that creates new objects by copying
(cloning) an existing object, called the prototype, instead of instantiating
them directly through constructors or factories.

**Purpose**: Solves the problem of expensive or complex object creation (for
example, heavy initialization, database lookups, or costly computation) by
duplicating pre-configured prototypes. This allows efficient production of
similar objects while preserving state and avoiding repeated setup logic.

**Benefits**:

* Improves performance for costly object initialization by reusing clones
  instead of re-running expensive setup.
* Hides concrete class details and creation complexity from the client.
* Makes it easy to create variations of objects by modifying clones after
  copying.
* Preserves runtime-configured or pre-initialized state during duplication.
* Reduces the need for subclassing or many factory implementations when
  producing similar objects.

In Python, the `copy` module (copy.copy / copy.deepcopy) is commonly used to
implement prototypes.
