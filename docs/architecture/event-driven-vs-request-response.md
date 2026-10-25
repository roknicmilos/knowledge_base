# Event-driven vs request-response

Two fundamental communication patterns in distributed systems and microservices.

| Aspect        | Request-response                                | Event-driven                                  |
|---------------|-------------------------------------------------|-----------------------------------------------|
| Communication | Synchronous                                     | Asynchronous                                  |
| Coupling      | Tighter (caller depends on the callee being up) | Loose (producers don't know consumers)        |
| Consistency   | Easier to keep strong                           | Typically eventual                            |
| Latency       | Immediate answer                                | Processing happens later                      |
| Resilience    | Caller affected by callee failures              | Events can be queued and retried              |
| Scaling       | Caller and callee scale together                | Producers/consumers scale independently       |
| Complexity    | Simpler                                         | More (broker, ordering, idempotency, retries) |
| Use case      | Real-time feedback                              | Background processing, decoupled workflows    |

(These are tendencies, not guarantees.)

**Use request-response when** you need immediate feedback (authentication, fetching data), the interaction is simple and
needs strong consistency.

**Use event-driven when** you want to decouple services and scale, the work is long-running/background, eventual
consistency
is acceptable (e.g. updating inventory after an order), or you handle high volumes of events.

**Hybrid:** request-response for real-time synchronous interactions, events for asynchronous decoupled workflows.

Tools: [Kafka](../devops/kafka.md), SQS/SNS/EventBridge ([Lambda & EDA](../devops/cloud/aws/lambda.md)).
