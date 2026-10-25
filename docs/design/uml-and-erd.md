# Modeling: UML, ERD, class diagrams

## UML – Unified Modeling Language

A general-purpose modeling language giving a standard way to visualize the design of a software system and to model OOP
concepts. Common diagrams:

- **Class diagram** – classes, interfaces and their relationships
- **Object diagram** – objects and their relationships
- **Component diagram** – components and their associations
- **Deployment diagram** – nodes and their relationships
- **Use case diagram** – use cases, actors and associations
- **Sequence diagram** – message flow between objects
- **State machine diagram** – state changes (see [FSM](../fundamentals/finite-state-machine.md))
- **Activity diagram** – activity flow

## ERD – Entity-Relationship Diagram

A visual representation of entities and their relationships in a **database**. It is **not** part of UML (it predates
it –
Chen, 1976), though the two are often used together.

### Crow's foot notation

Each relationship line has two indicators:

- **Cardinality** – the *maximum* number of times an instance can be associated with instances of the other entity.
- **Modality (ordinality)** – the *minimum* number.

Most of the time people just say "cardinality".

| Symbol meaning     |                      |
|--------------------|----------------------|
| One                | single bar           |
| Many               | crow's foot          |
| One (and only one) | double bar           |
| Zero or one        | circle + bar         |
| One or many        | bar + crow's foot    |
| Zero or many       | circle + crow's foot |

**Chen notation** is the other common ERD style (entities as rectangles, relationships as diamonds, attributes as
ovals).

## Class diagram vs ERD

- ERD building blocks: entities, relationships, attributes → map to **database tables**.
- Class diagram building blocks: classes, relationships, attributes (+ methods) → map to **real-world objects/code**.

### Class diagram relationships

| Relationship | Meaning                                        | Arrow                        |
|--------------|------------------------------------------------|------------------------------|
| Inheritance  | Child inherits attributes/behavior from parent | Solid line, hollow triangle  |
| Association  | Classes are related, no ownership              | Solid line                   |
| Dependency   | One class uses another                         | Dashed arrow                 |
| Aggregation  | Part can exist outside the whole               | Hollow diamond               |
| Composition  | Part cannot exist outside the whole            | Filled diamond               |
| Realization  | Class implements an interface                  | Dashed line, hollow triangle |

## References

- [Lucidchart] [Class diagram tutorial](https://www.youtube.com/watch?v=UI6lqHOVHic),
  [ERD tutorial I](https://www.youtube.com/watch?v=QpdhBUYk7Kk), [ERD tutorial II](https://www.youtube.com/watch?v=-CuY5ADwn24)
- [Crow's foot notation in ERDs](https://www.gleek.io/blog/crows-foot-notation.html)
- [Online ER diagram tool (Chen and crow's foot)](https://www.gleek.io/er-diagrams.html)
- [Difference between UML and ERD](https://pediaa.com/what-is-the-difference-between-uml-and-erd/)
- [Class diagram vs ERD](https://www.differencebetween.com/difference-between-er-diagram-and-vs-class-diagram/)
- [UML tutorial](https://www.tutorialspoint.com/uml/index.htm)
