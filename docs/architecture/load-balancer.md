# Load balancer

Distributes incoming network traffic across multiple servers so none is overwhelmed. Key to availability, reliability
and scalability.

**Purpose:** distribute traffic evenly · ensure availability (route only to healthy servers) · improve performance ·
enable scalability (add servers behind it) · provide redundancy (re-route on failure).

## How it works

It sits between clients and the backend pool (as a reverse proxy at L7; at L4 it forwards connections/packets) and picks
a backend per request/connection:

1. **Health checks** – periodically probe backends; send traffic only to healthy ones.
2. **Algorithms** – *Round robin* (sequential), *Least connections* (fewest active connections), *IP hash* (same client
   IP → same server), plus weighted variants.
3. **Session persistence (sticky sessions)** – same client → same server for stateful apps (cookie or IP hash). Prefer
   stateless backends where possible.

## Layer 4 vs Layer 7 (OSI model)

| Feature            | Layer 4 (transport)                                                                      | Layer 7 (application)                                             |
|--------------------|------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| Decision basis     | IP address, port, TCP/UDP                                                                | URL, headers, cookies, query string, body                         |
| Protocol awareness | Protocol-agnostic – can *carry* HTTP, SMTP, FTP, DB protocols without understanding them | Protocol-specific: HTTP(S), WebSocket, gRPC                       |
| Performance        | Faster, less CPU                                                                         | More processing                                                   |
| TLS                | Can pass through or terminate (e.g. AWS NLB TLS listeners)                               | Terminates TLS and inspects traffic                               |
| Features           | Basic routing                                                                            | Content routing, caching, compression, rewriting, sticky sessions |
| Typical use        | Databases, gaming, streaming, SMTP                                                       | Web apps, APIs, microservice routing                              |
| Examples           | AWS NLB, Azure Load Balancer, HAProxy (L4 mode), NGINX `stream`                          | NGINX, Traefik, AWS ALB, HAProxy (L7), F5 BIG-IP (both)           |

Example L4: client → `10.0.0.1:443` → forwarded to `10.0.0.5:443` purely by IP/port. Example L7: `GET /api/v1/users`
routed to server A, `/api/v2` to server B.

**Choose L4** for raw TCP/UDP routing and lowest latency (database connections, video streams). **Choose L7** for
content-aware routing, TLS termination, URL-based routing (API requests → microservices, routing by user location).

See also [API gateway](api-gateway.md) and [scaling](scaling.md).
