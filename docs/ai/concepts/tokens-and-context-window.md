# Tokens and the context window

The units an LLM works in and the budget it has to work with.

## Token

The unit a model reads and writes: usually a word-piece (a few characters), not a whole word. Everything is measured and
billed in tokens, and limits such as the context window are counted in them.

Rough estimate for English: 1 token ≈ 4 characters ≈ ¾ of a word. Good enough for back-of-envelope cost and
context-budget maths before reaching for a real tokenizer.

## Context window

The maximum amount of text (in tokens) the model can "see" at once: your prompt plus its own reply. Anything outside it
is invisible to the model. Think of it as the model's desk space (short-term memory).

- Manage it by trimming old turns, summarizing, or retrieving only what's relevant ([RAG](../rag.md)) instead of pasting
  a whole knowledge base into every prompt.
- Every request re-sends the **entire** conversation – the API is stateless (see [no persistent
  memory](../limitations.md#no-persistent-memory)).
- Quality degrades well before the limit is reached: see [attention dilution](../limitations.md#attention-dilution) and
  [lost in the middle](../limitations.md#lost-in-the-middle-effect). A window that technically fits the input is not one
  that reasons well over all of it.

Cost side of a growing context in Claude Code: [Context management](../claude/claude-code/context-management.md).
Provider-side reuse of a repeated prefix: [Prompt caching](prompt-caching.md).
