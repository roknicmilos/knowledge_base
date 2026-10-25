# Monolith vs modular monolith vs microservices

|                   | Monolith                                            | Modular monolith                     | Microservices                |
|-------------------|-----------------------------------------------------|--------------------------------------|------------------------------|
| Code organization | Single codebase                                     | Single codebase divided into modules | Typically multiple codebases |
| Deployment        | Single unit                                         | Single unit                          | Independent services         |
| Coupling          | Tight                                               | Loose between modules                | Loose                        |
| Scalability       | Scales as a whole (identical instances behind a LB) | Same                                 | Per-service, independent     |
| Complexity        | Low                                                 | Medium                               | High                         |
| Team structure    | Single team                                         | One or several teams                 | Multiple teams               |
| Use case          | Small/medium projects                               | Medium, growing projects             | Large/complex projects       |

## When to use which

- **Monolith:** small teams/limited scope, fast time-to-market, no significant scaling needs.
- **Modular monolith:** growing complexity; better maintainability without microservice overhead; possible future
  migration to microservices.
- **Microservices:** large complex systems, multiple teams, independent scaling, and the infrastructure + expertise to
  run distributed systems.

## Monolith

- Single, tightly coupled codebase (UI, business logic, data access) deployed as one unit; typically one database.
- **Pros:** simple to develop, test, deploy and debug; no network overhead between components.
- **Cons:** can't scale/deploy parts independently; coupling makes maintenance harder as it grows; slower development as
  the team grows.
- Example: basic e-commerce site with one codebase for frontend, backend and database.

## Modular monolith

- Logically divided into modules (by feature/domain) with well-defined interfaces; still one deployable.
- Single DB or one schema/DB per module.
- **Pros:** easier to understand/maintain, encourages separation of concerns, stepping stone to microservices.
- **Cons:** one deployment unit; needs discipline to keep modules decoupled.
- Example: e-commerce platform with user, catalog and order modules in one codebase.

## Microservices

- Small independent services, each for one business capability, communicating over APIs (REST, gRPC) or messaging; each
  usually has its own codebase, database and pipeline; can use different technologies.
- **Pros:** scalable and fault-tolerant, teams work independently, easy to adopt new tech per service.
- **Cons:** deployment/monitoring/debugging complexity, needs robust DevOps, network latency and communication overhead,
  distributed data consistency.
- Example: Netflix (authentication, recommendations, streaming as separate services).

## ESB vs microservices

An **ESB (Enterprise Service Bus)** is middleware providing a centralized communication layer – integration, data
transformation and routing between enterprise systems. Microservices structure an app as independently deployable
services.

| Aspect               | ESB                           | Microservices                     |
|----------------------|-------------------------------|-----------------------------------|
| Communication        | Centralized through the ESB   | Decentralized, service-to-service |
| Integration          | Central hub                   | Service-specific                  |
| Scalability          | Limited by the central ESB    | Per service                       |
| Flexibility          | More rigid                    | Highly flexible                   |
| Fault tolerance      | Single point of failure       | Failure isolated per service      |
| Development speed    | Slower (central control)      | Faster, independent               |
| Technology diversity | Limited, often homogeneous    | High                              |
| Complexity           | Complex to configure/maintain | Complex to manage many services   |

- **ESB:** enterprises with many legacy systems to integrate, complex orchestration/transformation.
- **Microservices:** modern cloud-native apps needing scalability and rapid development; usually the better choice for
  new projects without legacy integration.
- They can coexist: use the ESB judiciously for legacy integration/orchestration while new functionality runs as
  independent services – a gradual modernization path. (SOA is the older ESB-centred style; see [Python project
  architectures](../languages/python/frameworks/fastapi.md#project-architectures).)

See also: [layered vs vertical slices](layered-vs-vertical.md), [event-driven vs
request-response](event-driven-vs-request-response.md).
