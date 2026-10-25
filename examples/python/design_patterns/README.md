# Design Patterns

Design patterns are reusable solutions to common problems that appear over and
over in software development. They aren’t code you copy–paste, but proven ways
of structuring logic, objects, and interactions so your system stays easier to
understand, maintain, and extend. They give developers a shared vocabulary
(“factory,” “observer,” “adapter,” etc.) and help guide good design without
dictating exact implementation.

Keep in mind that design patterns are **not a magic bullet**. They should be
applied judiciously, only when they genuinely improve code clarity,
maintainability, or flexibility.

**Consider these cons before using a design pattern**:

* **Increased complexity** – introduces additional concepts, classes, or layers.
* **More code / boilerplate** – patterns often require extra structure beyond a
  direct solution.
* **Harder readability** – intent may be less obvious to someone unfamiliar with
  the pattern.
* **Indirection** – behavior or control flow is less direct and harder to trace.
* **Overengineering risk** – may solve problems you don’t actually have yet.
* **Learning curve** – requires prior knowledge to understand and maintain
  correctly.
* **Maintenance overhead** – changes may require touching multiple related
  components.
* **Debugging difficulty** – issues can be spread across several abstractions.
* **Misuse potential** – applying a pattern mechanically can worsen design
  instead of improving it.

## Architectural Patterns

Architectural patterns are high-level, structural blueprints that shape how an
entire system is organized. They define how major components interact, how data
flows, and how responsibilities are separated across the whole application.
Unlike design patterns, which solve smaller, localized problems, architectural
patterns guide the overall structure, scalability, and behaviour of the system
from the top down.

## Design Patterns vs Architectural Patterns

_Many patterns sit somewhere in the middle._

**Design Patterns** = patterns inside components (local structure)

* Solve localized problems
* At the class / object level
* Very reusable
* Found in the Gang of Four (GoF) book
* Examples: Singleton, Factory, Strategy, Observer, Decorator, Adapter, Builder,
  etc.
* These don't define how your app is structured, only how individual objects
  interact.

**Architectural Patterns** = patterns of the system as a whole (global
structure)

* Describe the overall structure of an app
* Define layers, modules, flows
* Influence deployment, responsibilities, system boundaries
* Examples: MVC, MVVM, MVP, Clean Architecture, Hexagonal Architecture,
  Monolith, Microservices, Event-driven architecture, etc.
* These patterns shape how your whole application is organized.

## Gang of Four (GoF) Design Patterns

The main design pattern groups are traditionally organized into three
categories, based on the classic book ["Design Patterns: Elements of Reusable
Object-Oriented Software" by "Gang of Four" (GoF)](https://www.digitalocean.com/community/tutorials/gangs-of-four-gof-design-patterns):

* [**Creational Patterns**](gang_of_4/creational_patterns/README.md)
* [**Structural Patterns**](gang_of_4/structural_patterns/README.md)
* [**Behavioral Patterns**](gang_of_4/behavioral_patterns/README.md)

## Dependency Injection (DI) Pattern

The GoF book was written in 1994, and DI as a formalized pattern became popular
later (especially with frameworks like Spring in the early 2000s). So it wasn't
really part of the original GoF classification, but if we had to classify it, DI
is a design pattern that falls primarily under behavioral patterns (with
creational aspects).

[More about Dependency Injection (and Dependency Inversion Principle)](dependency_injection/README.md)
