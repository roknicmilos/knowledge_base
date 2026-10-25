# Python web frameworks: Django vs FastAPI vs Flask

Most popular Python web frameworks. Ratings are qualitative and depend on the project.

| Criteria            | Django                                                                  | FastAPI                                                           | Flask                                                                                             |
|---------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| Enterprise projects | Excellent – full-stack, ORM, admin, auth, security out of the box       | Good and growing; fewer built-ins, more assembly needed           | Possible with lots of customization; better for small/medium projects                             |
| Batteries included  | Most – ORM, auth, forms, admin, migrations                              | API-focused; no forms/auth/admin                                  | Minimal – add libraries as needed                                                                 |
| Microservices       | Heavy for small services                                                | Excellent – lightweight, async, fast                              | Good (lightweight), FastAPI is now more popular for this                                          |
| Performance         | Sync-first (async views since 3.1); fine for most apps, DB/IO dominates | Very high among Python frameworks – async ASGI, Starlette/Uvicorn | Sync WSGI by default; `async` views supported since 2.0 (run per request, not a true async stack) |
| Learning curve      | Steepest – conventions, ORM, templates                                  | Moderate – needs type hints and async concepts                    | Gentlest                                                                                          |
| Community           | Very large and mature                                                   | Large and fast-growing                                            | Large and mature                                                                                  |
| Scalability         | Scales well with caching, load balancing, DB tuning                     | Designed for many concurrent connections; scales horizontally     | Same horizontal scaling as any stateless app, but you assemble the pieces yourself                |

Summary:

- **Django** – enterprise/full-stack apps needing lots of built-in functionality.
- **FastAPI** – high-performance APIs and microservices, async, auto-docs.
- **Flask** – minimalist, easy to learn, flexible; you piece libraries together.

The best choice depends on the project's requirements.

See [deployment setups](deployment.md), [FastAPI](fastapi.md), [Django](django.md).
