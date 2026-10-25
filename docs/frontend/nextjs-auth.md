# Frontend authentication with HTTP-only cookies (Next.js)

## Where to keep the JWT / session key

If your backend issues a JWT or session key, the safest way to hand it to the Next.js app:

- Store it in an **HttpOnly** cookie (JavaScript can't read it).
- Mark it `Secure` and `SameSite=Lax` (or `Strict`).
- Let the browser send it automatically to your backend.

```
Set-Cookie: session=eyJhbGci...; HttpOnly; Secure; Path=/; SameSite=Lax
```

This stops malicious JS (XSS) from **stealing** the token (it doesn't stop XSS from making requests as the user).
Cookie-based auth is CSRF-prone → keep `SameSite` and see [CSRF](../security/csrf.md).

## How does the frontend know the user is authenticated?

`document.cookie` can't see an HttpOnly cookie, so rely on the server.

### Option 1 – check server-side (SSR / server components)

```js
// app/dashboard/page.js
import { cookies } from 'next/headers'
import { redirect } from 'next/navigation'

export default async function DashboardPage() {
  const cookieStore = await cookies()           // async in Next.js 15+
  const token = cookieStore.get('session')?.value

  const res = await fetch(`${process.env.API_URL}/me`, {
    headers: { Cookie: `session=${token}` },
  })
  if (!res.ok) redirect('/login')

  const user = await res.json()
  return <Dashboard user={user} />
}
```

✅ Secure, works with SSR, easy to pass user info to components. ⚠️ Server involved for auth-aware pages (no purely
static pages).

### Option 2 – check client-side via an API call

Store no tokens in JS; call an endpoint such as `/api/me` that reads the cookie server-side and returns
`{ isAuthenticated, user, roles }`.

```js
useEffect(() => {
  fetch('/api/me').then(res => res.json()).then(data => setUser(data.user))
}, [])
```

The cookie is sent because the request is same-origin (use `credentials: 'include'` cross-origin).
✅ No tokens in browser storage, easy with React state. ⚠️ Small delay before auth state is known.

### Option 3 – middleware for route protection

Runs before rendering and can redirect early:

```js
// middleware.js
import { NextResponse } from 'next/server'

export function middleware(req) {
  const token = req.cookies.get('session')?.value
  if (!token && req.nextUrl.pathname.startsWith('/dashboard')) {
    return NextResponse.redirect(new URL('/login', req.url))
  }
}
```

This only checks that a cookie **exists** – an optimistic redirect, not authorization. Always verify the session in the
server component/route handler/backend as well (middleware-only auth has been bypassed before, e.g. CVE-2025-29927).

> **Verify:** Next.js 16 renamed `middleware` to `proxy` – check the version you use.

### Option 4 – hybrid for roles/permissions

Fetch user info via SSR or `/api/me`, keep it (not the token) in React context/Zustand/Redux, and toggle UI:
`{user?.role === 'admin' && <AdminPanel />}` – the backend must still enforce permissions.

## TL;DR

1. Store the JWT/session in an HttpOnly cookie.
2. Check auth server-side (SSR/server components; middleware only as an early redirect).
3. Expose `/api/me` for client-side user info.
4. Keep user info (not the token) in React state/context.
5. Use roles/permissions from `/me` for conditional UI – and enforce them on the server.
