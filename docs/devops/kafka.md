# Apache Kafka

A distributed **event streaming platform** for high volumes of real-time data. Originally developed at LinkedIn, now an
Apache
Software Foundation project. Used for real-time data pipelines, streaming applications and event-driven architectures.

## Key concepts

- **Producer** – publishes (writes) messages to topics.
- **Consumer** – subscribes to topics and reads messages, tracking its position by offset.
- **Consumer group** – consumers that share a topic's partitions: each partition is read by one consumer in the group,
  giving
  parallel processing and scaling.
- **Message (record)** – header (metadata), key and value (payload) (+ timestamp).
- **Topic** – named feed of records; partitioned and replicated across brokers.
- **Partition** – ordered, immutable sequence of records; enables horizontal scaling and parallel consumption.
  **Ordering is
  guaranteed only within a partition** (records with the same key go to the same partition).
- **Broker** – a Kafka server that stores data and serves clients. **Cluster** – brokers working together.
- **Offset** – unique ID of a record within a partition.
- **Replication** – each partition has one *leader* (handles reads/writes) and follower replicas for durability and
  fault tolerance.
- **Metadata management** – ZooKeeper was used in older versions; **Kafka 4.0 (2025) removed ZooKeeper**, KRaft is the
  only mode.
- **Retention / compaction** – records are kept by time/size (or compacted by key), not deleted on consumption.
- **Delivery semantics** – at-most-once, at-least-once, exactly-once (idempotent producers + transactions).

## How it works

1. Producers send messages to topics.
2. Messages are stored in partitions of the topic.
3. Consumers subscribe and read from partitions.
4. Kafka gets throughput, low latency and fault tolerance by distributing data across brokers and replicating
   partitions.

Features: very high throughput (millions of messages/s), horizontal scalability (add brokers), durability (persisted and
replicated), fault tolerance, real-time processing.

## Use cases

Real-time analytics · log aggregation · event sourcing · messaging backbone for microservices · real-time data
integration
pipelines.

## Ecosystem

- **Kafka Connect** – integrate Kafka with external systems (DBs, cloud services).
- **Kafka Streams** – library for stream-processing applications.
- **ksqlDB** (formerly KSQL, from Confluent – not part of Apache Kafka) – SQL-like streaming queries.
- **Schema Registry** (Confluent) – manages schemas for serialization (Avro, JSON Schema, Protobuf).

Related: [event-driven architecture](../architecture/event-driven-vs-request-response.md).
