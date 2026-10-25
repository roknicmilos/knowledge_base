# API Gateway

A server/service that acts as the **single entry point** for multiple backend services, routing client requests and
centralizing authentication, rate limiting, load balancing, logging and monitoring. Like a traffic controller directing
requests to the right service while applying security and performance policies.

## How it works

1. Client (mobile/web app, IoT device) sends a request to the gateway.
2. **Routing** – gateway decides which backend service handles it.
3. **Security checks** – authentication and authorization before forwarding.
4. **Transformation** (optional) – modify request/response (e.g. JSON ↔ XML).
5. **Response** – backend answers via the gateway.

## Key features

Request routing · authentication & authorization (OAuth, JWT, API keys) · rate limiting & throttling · load balancing ·
caching · request/response transformation · logging & monitoring · CORS handling.

## When to use

- Microservice architectures (a unified endpoint instead of clients calling many services).
- When you need centralized security, auth and traffic control.

## Challenges

- **Single point of failure** unless deployed redundantly.
- **Latency overhead** from extra processing.
- **Configuration complexity** (routing rules, policies, monitoring).

## API gateway vs reverse proxy vs load balancer

|             | API Gateway                                         | Reverse proxy                            | Load balancer                     |
|-------------|-----------------------------------------------------|------------------------------------------|-----------------------------------|
| Purpose     | Manage API requests and services                    | Route traffic between client and backend | Distribute traffic across servers |
| Focus       | Security, monitoring, transformation                | Caching, security, TLS termination       | Scalability, high availability    |
| Example use | Microservices, API management                       | Web apps, caching                        | Load distribution                 |
| Examples    | Kong, AWS API Gateway, Apigee, Envoy-based gateways | NGINX, Caddy                             | HAProxy, AWS ALB/NLB              |

The categories overlap – NGINX can play all three roles.
