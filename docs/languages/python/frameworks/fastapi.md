# FastAPI

## General

- Built on [Starlette](https://www.starlette.io/) (lightweight ASGI web framework) and
  [Pydantic](https://docs.pydantic.dev/) (the most widely used data-validation library). Relies heavily on Python type
  hints for validation, serialization and documentation.
- Supports concurrency with `async`/`await`; you can define both async and sync routes.
- Generates OpenAPI docs automatically for your routes: `/docs` (Swagger UI) and `/redoc`.
- Runs on any [ASGI](https://asgi.readthedocs.io/) server (Uvicorn, Hypercorn).
- Best-practice reference: [FastAPI Best Practices](https://github.com/zhanymkanov/fastapi-best-practices).

## FastAPI instance

`app = FastAPI()` is the main entry point and central object. It handles:

- **Routing** – maps URLs to handler functions
- **Middleware** – global request/response processing
- **Dependency injection** – for routes and other components
- **Lifecycle events** – startup/shutdown via a `lifespan` context manager (`@app.on_event` is deprecated)
- **Configuration** – CORS, static files…
- **ASGI integration** – it *is* the ASGI application

## APIRouter

- Groups related routes (user router, product router…); built on Starlette's routing.
- Routes use decorators: `@app.get`, `@router.post`, …
- Routers can have a common `prefix`, `tags` (for the docs) and `dependencies`.
- Mounted with `app.include_router(router)`; all routes land in the OpenAPI docs.

|             | `app` (FastAPI)                              | `router` (APIRouter)                  |
|-------------|----------------------------------------------|---------------------------------------|
| Purpose     | Main entry point of the application          | Group related routes for modularity   |
| Usage       | Global routes, middleware, settings          | Routes, prefixes, tags, dependencies  |
| Integration | Central object that ties everything together | Must be mounted with `include_router` |
| Scalability | Smaller apps / overall structure             | Organize and scale large applications |

## Async routes

FastAPI runs **sync** routes (`def`) in a threadpool and **async** routes (`async def`) directly on the event loop.

- Sync route: blocking I/O won't stop the event loop.
- Async route: called with `await`; FastAPI trusts you to do only **non-blocking** I/O.
- ⚠️ Blocking calls inside an `async def` route block the whole event loop.

```python
import asyncio, time
from fastapi import APIRouter

router = APIRouter()


@router.get("/terrible-ping")
async def terrible_ping():
    time.sleep(10)  # blocking I/O in async route – the whole process is blocked
    return {"pong": True}


@router.get("/good-ping")
def good_ping():
    time.sleep(10)  # blocking, but runs in a worker thread – others keep working
    return {"pong": True}


@router.get("/perfect-ping")
async def perfect_ping():
    await asyncio.sleep(10)  # non-blocking
    return {"pong": True}
```

## Middlewares

Code that runs before and/or after every request/response – logging, auth, error handling, CORS, custom headers. Based
on Starlette's middleware ("wrap-around").

```python
from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()


class SimpleMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        print("Before request")
        response = await call_next(request)  # next middleware or the route handler
        print("After response")
        return response


app.add_middleware(SimpleMiddleware)
```

- Implement a class inheriting `BaseHTTPMiddleware`, or a pure ASGI class with `__call__`, or use
  `@app.middleware("http")`. `BaseHTTPMiddleware` has known limitations (context variables, streaming, background tasks)
  – pure ASGI is preferred for library-grade middleware.
- Built-in: `CORSMiddleware`, `TrustedHostMiddleware`, `HTTPSRedirectMiddleware`, `GZipMiddleware`.
- **Order:** the **last middleware added is the outermost** – it sees the request first and the response last. Requests
  flow through middlewares in *reverse* order of `add_middleware` calls; responses flow back in the order they were
  added.
- Avoid heavy logic in middleware (applies to every request); use dependencies for route-specific logic.

## Dependency injection

Dependencies (DB connections, configuration, reusable logic) are provided to routes with `Depends`. General concept:
[dependency injection](../../../fundamentals/dependency-injection.md).

```python
from typing import Annotated
from fastapi import Depends, FastAPI

app = FastAPI()


def common_parameters(q: str | None = None, limit: int = 10):
    return {"q": q, "limit": limit}


@app.get("/items/")
def read_items(params: Annotated[dict, Depends(common_parameters)]):
    return {"params": params}
```

**Resolution order:** before the route, dependencies are evaluated (recursively for nested ones); the values are passed
to the handler; generator dependencies (`yield`) run their cleanup afterwards.
> **Verify:** exactly *when* `yield`-dependency cleanup runs relative to sending the response changed between FastAPI
> versions – check the current docs.

Advanced: class-based dependencies (e.g. query-param classes), `yield` for setup/teardown (DB sessions), nested
dependencies, global dependencies via `FastAPI(dependencies=[...])` / `APIRouter(dependencies=[...])`.

Use cases: DB connections, authentication/authorization, shared validation, environment-specific configuration.
Benefits: reusability, testability (override dependencies in tests), modularity, automatic validation.

## Validation

FastAPI validates automatically using type hints and Pydantic models, before the data reaches your handler, and returns
structured error responses (422) out of the box.

| Input            | Mechanism                          | Example                                           |
|------------------|------------------------------------|---------------------------------------------------|
| Path parameters  | Type annotations                   | `user_id: int`                                    |
| Query parameters | Type annotations, `Query`, `Field` | `q: Annotated[str, Query(min_length=3)]`          |
| Request body     | Pydantic models                    | `item: Item`                                      |
| Headers          | `Header`                           | `x_token: Annotated[str, Header()]`               |
| Dependencies     | Annotations, models, `Depends`     | `params: Annotated[dict, Depends(common_params)]` |

## Project architectures

FastAPI doesn't enforce an architecture. Common choices:

| Architecture           | Best for                                | Advantages                                                                               | Disadvantages                                                              |
|------------------------|-----------------------------------------|------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| Single-file app        | Small/prototype projects                | Quick and simple                                                                         | Hard to scale and maintain                                                 |
| Modular monolith       | Medium projects                         | Better organization (split by business domain)                                           | Can get messy if not truly modular                                         |
| Domain-Driven Design   | Complex, large projects                 | High modularity                                                                          | Initial setup takes time                                                   |
| Service-oriented (SOA) | Preparing for microservices             | Logical separation – independent services talking via public APIs, often sharing code/DB | Slightly more complex than a monolith                                      |
| Microservices          | High-scalability projects               | Independent deployment, own code/repo/DB per service, smaller scope than SOA             | Operational overhead                                                       |
| Layered                | Strict technical separation of concerns | Clear boundaries, testable                                                               | Boilerplate; layers depend heavily on each other; hard to isolate features |

Considerations: **project size** (start simple, refactor as it grows), **team size** (bigger teams → modular/DDD to
avoid conflicts), **future goals** (planning microservices → SOA/DDD early). See [monolith vs
microservices](../../../architecture/monolith-vs-microservices.md) and [layered vs
vertical](../../../architecture/layered-vs-vertical.md).
