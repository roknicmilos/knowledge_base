# Context management: `/clear` vs `/compact`

When these commands actually save tokens and cost, and when growing context degrades answers. The commands and the
auto-compact buffer are Claude Code-specific; the cost, caching and degradation ideas apply to any LLM conversation (see
[context window](../../concepts/tokens-and-context-window.md)).

## How context cost works

- Every request re-sends the **entire** history; there is no server-side memory between calls. A bigger context in use
  means more billed tokens on every later request.
- [Prompt caching](../../concepts/prompt-caching.md) softens this but doesn't remove it: cached tokens are discounted, not
  free. A session at 50% of a large window still pays for about that much on every turn.
- 10 prompts from a 50%-full context cost noticeably more than 10 from a 7%-full one, even with caching.

## When auto-compact triggers

Not at a fixed absolute size. It is a reserved buffer near the **top** of the window: compaction triggers when free space
shrinks to that buffer, around 96–97% used. Sitting at 50–80% is still well before auto-compact.

> **Verify:** the threshold is an implementation detail and may change.

## `/compact`: costs before it saves

- It **costs tokens**: it reads the full history and generates a summary (a real API call).
- It **breaks prompt caching**: the next request(s) lose the discount.
- It **only pays off if a lot of conversation is still ahead**: a one-time cost (summary + cache miss) buys a smaller
  history on every future turn.

Rule of thumb: compact when the context is large *and* much more related work is ahead, not reflexively after every task.

## `/clear`: the clearer win

Between **unrelated** tasks it is close to free: no summarization (it just drops history), and little cache value is lost
because the next task wouldn't reuse the old context anyway.

## Degraded quality as context grows

Independent of cost, a large context can degrade answers before the limit
([attention dilution](../../limitations.md#attention-dilution), "needle in a haystack"):

- This is a reason to clear/compact on its own: a long multi-topic history can hurt quality while well within limits.
- There is **no fixed percentage** where it starts. It depends on *relevance density*, not raw size: one continuous,
  relevant task holds up far better than the same token count spread over unrelated tangents.

## Summary

| Action    | When it helps                                           | Why                                                                |
|-----------|---------------------------------------------------------|--------------------------------------------------------------------|
| `/clear`  | Switching to an unrelated task                          | Drops stale context at ~no cost; nothing valuable was cached       |
| `/compact`| Long session, large context, more related work ahead    | Shrinks what's resent each turn, but costs tokens and a cache hit  |
| Neither   | Short session, small context, task in progress          | Free space costs nothing per request; compacting is pure overhead  |
