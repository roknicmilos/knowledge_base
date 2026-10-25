# Deployment setups for Django, FastAPI and Flask

**WSGI** = synchronous server interface (Gunicorn, uWSGI, mod_wsgi). **ASGI** = async interface (Uvicorn, Daphne,
Hypercorn,
Granian). A *web server / reverse proxy* (Nginx) sits in front and handles TLS, static files and buffering.

| Framework | Default nature                       | Web server      | App server                               | Typical setup                                                                             |
|-----------|--------------------------------------|-----------------|------------------------------------------|-------------------------------------------------------------------------------------------|
| Django    | Sync (async views/ORM since 3.1/4.1) | Nginx           | Gunicorn (WSGI) or Uvicorn/Daphne (ASGI) | Gunicorn + Nginx (sync); Uvicorn/Daphne + Nginx (async)                                   |
| FastAPI   | Async                                | Nginx           | Uvicorn                                  | Uvicorn + Nginx (or `uvicorn --workers`; in containers usually one process per container) |
| Flask     | Sync (WSGI)                          | Nginx or Apache | Gunicorn                                 | Gunicorn + Nginx; Apache + `mod_wsgi`                                                     |

## Django

- Sync by default; async views since 3.1, but the ecosystem is mostly sync.
- Gunicorn (WSGI) behind Nginx is the most common stack. For WebSockets/async views use an ASGI server (Uvicorn,
  Daphne).
- Database: PostgreSQL/MySQL in production (SQLite for development); Redis for cache/sessions.
- Process supervision: systemd/Supervisor, or containers.

## FastAPI

- Async by default; built for concurrency (APIs, microservices).
- Uvicorn (ASGI) behind Nginx is the standard; commonly in Docker. Multiple workers: `uvicorn --workers N` or Gunicorn
  with the
  separate `uvicorn-worker` package (the old `uvicorn.workers` module is deprecated).
- Often paired with async DB drivers (PostgreSQL with asyncpg, MongoDB, …).

## Flask

- WSGI/sync. Gunicorn + Nginx is the most common stack; `mod_wsgi` on Apache is less common.
- Async workloads: Flask supports `async def` views, but each runs in a short-lived event loop; for a true async stack
  use
  Quart or FastAPI. Flask can't be served natively by Uvicorn (it is WSGI; an adapter such as `a2wsgi` is needed and
  doesn't make
  it async). Concurrency via gevent/eventlet workers is possible.
- systemd/Supervisor for process management; Docker for cloud deployments.
