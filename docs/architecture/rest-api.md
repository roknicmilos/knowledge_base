# API and REST

## API

**Application Programming Interface** – a software intermediary that lets two applications talk to each other; often
described
as a contract between an information provider and a consumer.

*Waiter analogy:* the API takes your order (request) to the kitchen and brings the food (response) back.
Architecture is usually explained as client (sends the request) and server (sends the response).

## REST

**Representational State Transfer** – an architectural style for web APIs; the most common API style today. The client
sends requests, the server runs internal functions and returns data.

Features:

- Separation of client and server.
- **Stateless** – the server stores no client state between requests.
- Uses HTTP methods and status codes ([HTTP](../web/http.md)).
- Operates on **resources** (CRUD).
- **Cacheable** – the server can say what may be cached and for how long.
- Uniform interface and layered system (proxies, gateways, CDNs in between).

### Securing REST APIs

HTTPS everywhere · authentication (OAuth2/OIDC, JWT or API keys) · authorization checks per resource · rate limiting ·
input validation · correct CORS configuration · least-privilege credentials · audit logging.
