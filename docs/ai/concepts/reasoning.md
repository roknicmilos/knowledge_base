# Reasoning, scratchpad and extended thinking

Getting a model to work through a problem before committing to an answer.

## Scratchpad

A space where the model writes intermediate notes, calculations and plans before the final answer. Exposing this
"thinking out loud" improves accuracy on hard tasks. It is a prompting technique, not a product feature: "think step by
step before answering" works with any model.

- It is just tokens generated into the same context window. Once the answer is given it disappears unless the app saves
  or re-feeds it (some multi-turn tool-use setups do).
- Products differ on whether they show it or strip it, even though the tokens were generated (and billed).

## Reasoning

Explicit step-by-step work (chain-of-thought) before answering. Improves math, logic and multi-step tasks. Turn it on
for
real chains of logic (math, debugging, planning); skip it for lookups and formatting, where it only adds latency and
cost.

## Extended thinking (Claude)

Claude's productized reasoning mode: the model produces a "thinking" block, then the answer. Chain-of-thought made
native
and controllable instead of a prompting trick. Available in the API and Claude apps; whether it is on by default, and
whether it can be turned off, differs per model.

- A visible thinking block is not guaranteed to be the raw chain of thought; products may summarize or omit it.
- *Legacy:* on older models using `budget_tokens`, flagged reasoning came back as an encrypted `redacted_thinking` block
  that had to be passed back unchanged. Current models (adaptive thinking) never return raw reasoning, only a summarized
  or omitted block, so there is no redacted type to handle.

## Scratchpad vs context window vs memory

Three kinds of "remembering":

- **Scratchpad** – this task's working notes (thinking before answering).
- **[Context window](tokens-and-context-window.md)** – everything currently visible to the model.
- **[Memory](../claude/claude-code/memory-and-rules.md)** – persistent context reloaded across turns/sessions.
