# SQL vs NoSQL

| Aspect            | SQL (relational)                                                                                                                           | NoSQL (non-relational)                                                                                                  |
|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Data model        | Tables of rows and columns; relations via foreign keys                                                                                     | Key-value, document, graph or wide-column                                                                               |
| Schema            | Fixed, predefined                                                                                                                          | Dynamic/flexible                                                                                                        |
| Scaling           | Traditionally vertical; horizontal possible but harder (read replicas, sharding, distributed SQL such as CockroachDB/Spanner/Citus/Vitess) | Designed to distribute data across servers                                                                              |
| Query language    | SQL (standardized, powerful joins)                                                                                                         | No standard; per database (e.g. MongoDB's JSON-like queries)                                                            |
| Transactions      | ACID by default                                                                                                                            | Varies: often BASE / eventual consistency, but many support ACID (MongoDB multi-document, DynamoDB transactions, Neo4j) |
| Typical strengths | Complex queries/joins, integrity                                                                                                           | High-speed reads/writes at large scale, flexible data                                                                   |
| Use cases         | Financial systems, ERP, CRM, anything with strong relationships                                                                            | Real-time apps, big data, IoT, content, caching                                                                         |
| Examples          | MySQL, PostgreSQL, Oracle, SQL Server, SQLite                                                                                              | MongoDB (document), Redis (key-value), Cassandra (wide-column), Neo4j (graph), Couchbase                                |

## Notes

- **CAP theorem** applies to any distributed data store: during a network partition you must choose consistency or
  availability. NoSQL systems are often tuned towards availability (eventual consistency), but it isn't a property of
  "NoSQL" as such; many let you choose per operation.
- The old rule "SQL = vertical, NoSQL = horizontal" is only a tendency today.
- Performance is workload dependent – SQL engines are very fast at joins and aggregations; NoSQL shines at simple access
  patterns by key at massive scale.

**Choose SQL if** data is structured and relational, you need complex queries and transactions, integrity is critical.
**Choose NoSQL if** data is unstructured/semi-structured, you need very high scalability/flexibility, large volumes or
real-time workloads.

Related: [ACID](transactions.md), [scaling](../architecture/scaling.md).
