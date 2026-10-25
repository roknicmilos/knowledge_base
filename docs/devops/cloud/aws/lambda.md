# AWS Lambda

Serverless compute service that runs your code **in response to events**, without provisioning or managing servers. It
scales
automatically, executes code only when needed and bills only for compute time used – a cornerstone of serverless and
event-driven systems.

## Serverless architecture

A cloud model where the provider dynamically allocates and manages servers. Characteristics: no server management,
pay-as-you-go, automatic scaling, event-driven functions. Lambda embodies it: you write the function, AWS handles
execution,
scaling and billing.

## Event-driven architecture (EDA)

Actions are triggered by **events** (file uploaded, DB row changed, user action).

- **Producers** generate events (S3 uploads, DynamoDB updates).
- **Routers** direct events to consumers (EventBridge, SNS, SQS).
- **Consumers** react (Lambda functions).

Lambda is mostly an event **consumer** (S3 upload, SQS message, EventBridge schedule), but it can also be a
**producer**:
in simple workflows it's the final consumer; in multistep workflows and microservice/EDA-heavy systems it often consumes
*and*
publishes events to orchestrate other services.
See [event-driven vs request-response](../../../architecture/event-driven-vs-request-response.md), [Kafka](../../kafka.md).

## Core concepts

1. **Function** – self-contained unit of code (Python, Node.js, Java, Go, .NET, Ruby, or custom runtime/container
   image).
2. **Event source** – what invokes it: S3, DynamoDB, SNS, SQS, EventBridge, API Gateway, or custom events.
3. **Execution environment** – isolated runtime with fixed memory/CPU limits and ephemeral `/tmp` storage (512 MB by
   default,
   configurable up to 10 GB).
4. **Invocation models**
    - *Synchronous* – Lambda waits and returns the result (e.g. API Gateway).
    - *Asynchronous* – events are queued and processed in the background (e.g. S3 triggers).
    - *Event source mapping / stream* – Lambda polls sources like SQS, DynamoDB streams, Kinesis.
5. **Cold starts** – see below.

## Configuration

- **Runtime** – chosen when creating the function.
- **Memory** – 128 MB to 10 GB; **CPU scales with memory** (≈1 vCPU at ~1.8 GB).
- **Timeout** – 1 second to 15 minutes.
- **Environment variables.**
- AWS handles isolation, sandboxing and networking.

## Runtimes

Managed runtimes exist for Node.js, Python, Java, .NET, Ruby; Go and other languages run on the OS-only
`provided.al2023`
runtime (or a container image). Each runtime has an identifier (e.g. `python3.13`); moving to a new language version
means
changing the identifier. Lambda patches runtimes automatically (configurable). Custom runtimes implement the Runtime
API.

> **Verify:** the list of supported runtimes changes constantly (older ones are deprecated). Check the
> [official runtimes page](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html) instead of copying a list
> here.
> (The original note listed `go1.x`, `dotnet6/7` and `ruby2.7`, which had already been deprecated.)

## Dependencies

Bundle packages (e.g. Pydantic) with your code; share common ones via **Lambda Layers**; or ship a container image (up
to 10 GB).

## Cold vs warm start

- **Cold start** – Lambda initializes a new execution environment for a request: first invocation, after inactivity
  (minutes to
  hours), when scaling out for concurrent requests, or after deploying/updating the function. Adds latency.
- **Warm start** – the environment is reused for subsequent requests for a while.
- **Factors:** memory (more memory = more CPU = often shorter cold start), concurrency spikes, deployments,
  package/runtime size.
- **Concurrency limits** – accounts have a limit; beyond it invocations are throttled (or queued for async).
- **Mitigation:** *Provisioned Concurrency*, *SnapStart* (Java, Python, .NET), smaller packages. (Pinging the function
  on a
  schedule via EventBridge is an old workaround that doesn't help under concurrent load.)

## Pros and cons

**Pros:** automatic scaling · pay only for run time · integrates with many AWS services, multiple languages · fits
microservices
and EDA. **Cons:** cold starts · max 15 min execution · limited memory (10 GB) and ephemeral storage.

> **TODO:** how to test, debug and monitor Lambdas · error handling and retries (DLQ, on-failure destinations) · how
> Lambda
> uses execution roles/IAM to access other AWS resources.
