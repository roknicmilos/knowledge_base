# CORS

Cross-Origin Resource Sharing: a mechanism that lets a server declare which **other origins** (scheme + host + port) may
read its responses from a browser. It is a controlled relaxation of the Same-Origin Policy (SOP).

- **The browser enforces the rules** – CORS does not protect a server from curl, scripts or other non-browser clients.
- Response headers: `Access-Control-Allow-Origin`, `-Allow-Methods`, `-Allow-Headers`, `-Allow-Credentials`,
  `-Expose-Headers`, `-Max-Age`.
- If the server sets no CORS headers, only same-origin access is allowed. That is why a frontend on `localhost:3000`
  calling a backend on `localhost:8000` gets a CORS error (different port = different origin).
- For a **simple request** the server still responds with the data, but the browser refuses to expose it to the page if
  the origin isn't allowed. For a **preflighted** request the real request is never sent if the preflight fails.

## Preflight

A request is *simple* only if it uses GET/HEAD/POST, no custom headers, and a `Content-Type` of
`application/x-www-form-urlencoded`, `multipart/form-data` or `text/plain`. Anything else is preflighted: the browser
first sends an automatic `OPTIONS` request and checks `Allow-Methods`/`Allow-Headers`. This includes:

- PUT, PATCH, DELETE,
- **POST with `Content-Type: application/json`**,
- requests with custom headers such as `Authorization`.

`Access-Control-Max-Age` lets the browser cache the preflight result.

> Defaults differ per library (e.g. Starlette/FastAPI `CORSMiddleware` allows only `GET` unless `allow_methods` is set).
> Always configure origins, methods and headers explicitly.

## Cookies and CORS

- Cookies are scoped by domain/path (site), not by origin, and are sent with requests to the domain that set them.
- For a cross-origin request to send/accept cookies:
    - client: `fetch(url, { credentials: 'include' })` (or `withCredentials = true` for XMLHttpRequest),
    - server: `Access-Control-Allow-Credentials: true` **and** an explicit `Access-Control-Allow-Origin` (not `*`;
      `Allow-Headers`/`Allow-Methods` can't be `*` either),
    - cookie: `Secure` and, for cross-*site* use, `SameSite=None` (Chrome and Edge default to `SameSite=Lax`; other
      browsers differ).
- Mark session cookies `HttpOnly` (not readable by JavaScript) and `Secure` (HTTPS only) to reduce XSS and
  man-in-the-middle risk.
- A credentialed request that changes headers/methods/content type triggers a preflight too.
- Cookie-based auth across origins needs [CSRF protection](../security/csrf.md).
