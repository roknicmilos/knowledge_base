# CSRF

**Cross-Site Request Forgery**: an attacker tricks an authenticated user's browser into sending a state-changing request
to a site the user is logged in to. It works because browsers attach cookies automatically.

## How it works

1. **Authentication** – the user logs into `bank.com` and gets a session cookie.
2. **Malicious request** – the user visits an attacker's page (or clicks a link) that contains a hidden form:

   ```html
   <form action="https://bank.com/transfer" method="POST">
     <input type="hidden" name="amount" value="1000">
     <input type="hidden" name="toAccount" value="attackerAccount">
   </form>
   <script>document.forms[0].submit();</script>
   ```

3. **Automatic execution** – the browser sends the request with the user's session cookie.
4. **Unauthorized action** – the bank thinks the user made the request and transfers the money.

## Prevention

1. **CSRF tokens** – a unique, unpredictable token per session/request, embedded in forms (or sent in a header) and
   validated by the server. Variant: double-submit cookie.
2. **SameSite cookies** – `Set-Cookie: sessionId=abc123; SameSite=Lax` (or `Strict`) stops the cookie being sent on
   cross-site requests. Chromium browsers default to `Lax` when the attribute is missing; don't rely on that alone.
3. **Check `Origin`** (fall back to `Referer`) on state-changing requests. `Referer` can be stripped, so it isn't enough
   on its own.
4. **Re-authentication / MFA** for sensitive actions.
5. APIs that authenticate with an `Authorization: Bearer …` header (not cookies) aren't CSRF-prone, because the browser
   doesn't add that header automatically.
6. Never change state with `GET`.

Framework notes: [Django CSRF](../languages/python/frameworks/django.md#csrf). Related: [cookies &
CORS](../web/cors.md#cookies-and-cors), [frontend auth with HTTP-only cookies](../frontend/nextjs-auth.md).
