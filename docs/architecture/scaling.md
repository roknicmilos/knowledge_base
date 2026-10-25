# Scaling systems

## Vertical scaling (scale up)

Add resources (CPU, RAM, storage) to an existing machine, e.g. 16 GB/4 CPU → 64 GB/16 CPU.

- Single machine, simple to implement (resize hardware/cloud instance).
- Limited by hardware; may need downtime; single point of failure.
- Good for monoliths and systems with little parallelism.

## Horizontal scaling (scale out)

Add more machines/instances and spread the load (cluster, load-balanced cloud instances).

- **Pros:** very high scalability, high availability/fault tolerance through redundancy, elastic (add/remove nodes),
  fits microservices/cloud-native apps.
- **Cons:** more complex (load balancing, replication, distributed-systems knowledge), harder data consistency, network
  latency between nodes. Services should be stateless (or externalize state, e.g. sessions in Redis).

## Horizontal scaling vs distributed systems / microservices

Related but not the same: microservices/distributed systems are an *architecture*, horizontal scaling is a *scaling
strategy*
applied inside them (or inside a monolith).

- **Horizontal scaling:** run many identical instances of one service, e.g. a stateless checkout service ×20 behind a
  load
  balancer.
- **Distributed system (microservices):** split into services with different responsibilities (`user-service`,
  `order-service`, `inventory-service`), talking via APIs/messaging, possibly with their own data stores. Each service
  can then
  be scaled independently (e.g. scale `order-service` for high order traffic).

## Single vs multiple databases in distributed systems

| Criteria                   | Single database                 | Multiple databases                   |
|----------------------------|---------------------------------|--------------------------------------|
| Scalability                | Limited by one DB               | Independently scalable per service   |
| Fault isolation            | DB failure affects all services | Only the related service is impacted |
| Data consistency           | Strong by default               | Needs eventual-consistency patterns  |
| Operational complexity     | Easier                          | More tooling and expertise           |
| Flexibility                | One DB technology               | Best DB per service                  |
| Cross-service transactions | Simple, ACID                    | Complex, often avoided (sagas)       |

- **Single DB:** small apps with tightly coupled services; performance not yet a bottleneck; simplicity first.
- **Multiple DBs:** large microservice systems, differing performance/scaling needs, high availability, strong DDD
  boundaries.
- **Hybrid:** start with one DB, split as you grow; keep core transactional data (orders, payments) together and move
  logs,
  analytics, search to specialized stores.

Related: [load balancer](load-balancer.md), [monolith vs microservices](monolith-vs-microservices.md).
