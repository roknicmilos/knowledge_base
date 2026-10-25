# LLM limitations

Structural weaknesses shared by all large language models: not bugs in one product, but consequences of how LLMs are
trained and run. Knowing them is the **Discernment** part of [AI fluency](ai-fluency.md): when to trust output and when
to verify it.

Each entry: what it is, why it happens, how to handle it.

## Knowledge cutoff

- **What:** the model only knows what existed in its training data; newer events, libraries and APIs are invisible
  unless supplied at query time.
- **Why:** training is a one-time (or periodic) pass over a fixed snapshot, not continuous learning
  ([pre-training](concepts/training-and-inference.md#pre-training)).
- **Handle:** don't trust unaided memory for anything that changes (versions, prices, news, "latest" APIs). Ground it
  with a web search tool, [RAG](rag.md), or pasted current docs. Ask the model for its cutoff and treat time-sensitive
  claims as unverified.

## Hallucination

- **What:** false, fabricated or unsupported statements delivered with the same fluent confidence as correct ones: a
  citation that doesn't exist, a function never in that library, an invented statistic.
- **Why:** the model predicts plausible next tokens; it doesn't look facts up. Fluent, plausible text is what it was
  trained to produce, not verified text.
- **Handle:** confident tone is no signal of correctness. Verify anything checkable (citations, exact numbers, API
  names, quotes). Ground with RAG or tools (search, docs, code execution). Run the code; check that the cited source
  really says that.

## Context window limits

- **What:** only a bounded number of [tokens](concepts/tokens-and-context-window.md) is visible at once, and quality
  degrades before the limit.
- **Why:** fixed maximum input size, and attending well to every token gets harder as text grows.
- **Handle:** keep prompts focused: trim old turns, summarize, retrieve only what's relevant. For long work, split into
  stages and carry forward only what the next stage needs. See [Context
  management](claude/claude-code/context-management.md).

## Attention dilution

- **What:** the mechanism behind the "degrades before the limit" part: as more tokens are packed in, attention on any
  single one, including relevant ones, is spread thinner.
- **Why:** attention weights are normalized to a fixed total (softmax). Every irrelevant token still claims a slice, so
  the weight left for the tokens that matter shrinks as context grows.
- **Handle:** "inside the window" ≠ "attended to well". Keep signal-to-noise high, summarize instead of accumulating raw
  turns, retrieve selectively, and put load-bearing instructions near where they are used.

## Lost-in-the-middle effect

- **What:** the empirically observed shape of dilution over long inputs: information at the very start or end is used
  better than information in the middle, even well within the window.
- **Why:** consistently reproduced across models; the leading explanation is a primacy/recency bias in attention and
  positional encodings (like the human serial-position effect). No single confirmed root cause.
- **Handle:** put the most important instructions/facts at the start or end of a long prompt. When ordering RAG results,
  put the most relevant first or last. Keep load-bearing content short enough to sit near an edge.

## Non-determinism

- **What:** the same question twice can give different answers, even at temperature 0.
- **Why:** sampling is random by design, and batching/floating-point effects add variation.
- **Handle:** don't assume byte-identical output; constrain the format, verify properties of the output, add a check for
  critical steps. See [Sampling and determinism](concepts/sampling-and-determinism.md).

## No persistent memory

- **What:** by default a model remembers nothing across conversations.
- **Why:** the model is stateless and re-run per request; "memory" is the application re-injecting prior context.
- **Handle:** re-supply context that matters, or use the product's memory mechanism (e.g. `CLAUDE.md`, see [Memory and
  rules](claude/claude-code/memory-and-rules.md)) for standing facts.

## Lack of real-world grounding

- **What:** the model only knows its training data and the current context; it has no access to live systems or the
  physical world and can't confirm a claim beyond pattern matching.
- **Why:** it is a text-in/text-out predictor. Outside connections (search, DB, live API) are bolted on via [tool use or
  MCP](concepts/tool-use-and-mcp.md).
- **Handle:** for current or verifiable state (balances, live prices, system status) give it a tool to check. Treat
  claims about "what's currently true" as hypotheses.

## Sycophancy

- **What:** a tendency to agree with, validate or flatter the user's framing even when wrong: confirming a flawed
  premise, softening pushback, reversing a correct answer after the user shows doubt.
- **Why:** training that optimizes for human approval (including RLHF) can reward agreeable answers over correct but
  unwelcome ones.
- **Handle:** explicitly ask for pushback ("tell me if this is wrong", "argue the other side"). Be suspicious of a
  sudden reversal right after you express doubt; ask the model to justify its position independently.

## Weak numeric / exact computation

- **What:** unreliable at precise arithmetic, large numbers and exact counting (characters in a word), especially
  without help.
- **Why:** it predicts plausible tokens from text patterns rather than running a calculator, so it approximates.
- **Handle:** give it a tool (code execution, calculator, script) and treat mentally computed numbers as estimates until
  verified.
