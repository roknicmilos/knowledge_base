# Prompt caching

Reusing a previously processed *prefix* of a prompt (long system prompt, big document, tool definitions) across calls,
so the provider skips re-running [inference](training-and-inference.md#inference) over it. Cuts latency and cost for
repeated or multi-turn calls that share the same leading content.

Mark the stable part as cacheable and put the part that changes per call (the user question) after it. It matters most
for agents and chat apps that resend the whole history every turn.

## On the Claude API

- **Prefix match:** everything from the start of the prompt up to a `cache_control` marker must be byte-identical to hit
  the cache. Render order is `tools` → `system` → `messages`; a marker on the last stable block caches everything before
  it. Up to 4 breakpoints per request.
- **TTL:** default 5 minutes, or an explicit 1 hour for bursty traffic. A cache read refreshes the timer at no extra
  cost.
- **Pricing:** a cache write costs *more* than an uncached call (≈1.25× for 5 min, ≈2× for 1 h); a cache read is far
  cheaper (≈0.1× base input price, lower on some newer models). It only pays off once the prefix is reused enough to
  earn back the write premium, not on a one-off call.

> **Verify:** multipliers, TTLs and breakpoint limits change; check the current pricing page.

## In Claude Code

The harness caches its own system prompt and tool schemas automatically; you don't place markers yourself. The mechanics
still explain behaviors such as `/compact` costing a cache miss on the next request (the summary rewrites the prefix) –
see [Context management](../claude/claude-code/context-management.md).

## Gotchas

- A small edit near the start of a long prompt (a timestamp, a reordered JSON key, a different tool list) invalidates
  the whole cache, not just the changed part. Keep the stable part first and stable.
- It is a provider/API-level feature; whether and how it is exposed differs per product.
