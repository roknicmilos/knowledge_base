# Browser storage

## Comparison

|                 | Cookies                                     | Local Storage                         | Session Storage               | IndexedDB                                                  |
|-----------------|---------------------------------------------|---------------------------------------|-------------------------------|------------------------------------------------------------|
| Purpose         | Small data, sessions, preferences, tracking | Larger data persisted across sessions | Data for one tab/page session | Large structured data, files, blobs, queries, transactions |
| Capacity        | ~4 KB per cookie; limited number per domain | ~5 MB per origin                      | ~5 MB per origin              | Hundreds of MB to GBs (browser/disk dependent)             |
| Sent to server  | Yes, with every matching request            | No                                    | No                            | No                                                         |
| Expiry          | Session or set date                         | Until deleted                         | Until tab/window closes       | Until deleted                                              |
| API             | Synchronous                                 | Synchronous (can block UI)            | Synchronous (can block UI)    | **Asynchronous**                                           |
| Data types      | Strings                                     | Strings                               | Strings                       | Any structured-cloneable value, Blobs, Files               |
| JS access       | Unless `HttpOnly`                           | Yes                                   | Yes                           | Yes                                                        |
| Sensitive data? | OK only with `HttpOnly; Secure`             | No (readable by any script → XSS)     | No                            | No                                                         |

## Cookies

How they work:

- The server sends a `Set-Cookie` header; the browser stores the cookie according to its attributes (domain, path,
  expiry, flags) and sends it back on matching requests.
- JavaScript can also set cookies via `document.cookie`, but session/auth cookies should be set by the server.

Flags / types:

- **Session cookie** – no expiry; usually gone when the browser closes (session restore can keep it).
- **Persistent cookie** – has `Expires`/`Max-Age`.
- **First-party / third-party** – set by the visited site vs another domain (tracking, ads).
- **Secure** – only sent over HTTPS.
- **HttpOnly** – not readable from JavaScript (mitigates token theft via XSS); still sent with requests.
- **SameSite** (`Strict`/`Lax`/`None`) – restricts cross-site sending; helps against CSRF. Chrome and Edge default to
  `Lax` when the attribute is missing; other browsers differ, so set it explicitly.

> **Verify:** third-party cookies. Safari and Firefox block them by default. Chrome announced a phase-out, then in
> 2024–2025 changed course and kept them (with user controls) and wound down the Privacy Sandbox APIs. Check current
> browser behaviour before relying on them.

See [CORS – cookies](cors.md#cookies-and-cors), [CSRF](../security/csrf.md).
