# Stop sequences and assistant message prefilling

Two Claude API request-shaping techniques for controlling *where a response ends* and *how it begins*. Both are
API-level parameters; there is no toggle in a chat UI. Broader context: [prompt
engineering](../../concepts/prompt-engineering.md).

| Technique                 | Controls                  | Status on current models                                                 |
|---------------------------|---------------------------|--------------------------------------------------------------------------|
| Stop sequences            | Where the response *ends* | Fully supported                                                          |
| Assistant message prefill | How the response *begins* | Removed (HTTP 400); use structured outputs or system-prompt instructions |

## Stop sequences

A list of strings (`stop_sequences: [...]`). If the model generates one, generation halts immediately and that string is
*not* included in the returned text. It is a hard exact-match cutoff, not a hint.

Use it to stop at a boundary you control, e.g. a role-play at `"\nHuman:"` so the model doesn't write the other side, or
a list generator at `"\n\n"` once one block is done.

- Matching is exact and case-sensitive; a paraphrase does nothing.
- Check `response.stop_reason`: `"stop_sequence"` (a sequence fired; matched string in `response.stop_sequence`),
  `"end_turn"` (natural finish) or `"max_tokens"` (hit the cap). A short response doesn't prove a stop sequence fired.
- The stop string is consumed, so the cut text is gone from the response.

## Assistant message prefilling

Historically you could seed the start of Claude's reply with a final `assistant` message (no `user` turn after it) and
Claude continued from that text. It was used to force `{` for JSON, skip a "Sure, here's..." preamble, or lock a
persona's first words.

> **Verify:** removed on every current model: it returns HTTP 400 on Claude Opus 5, Sonnet 5, Fable 5, Fable 5.1 and the
> Opus/Sonnet 4.6/4.7/4.8 family. Treat it in old code and tutorials as deprecated, not "old-fashioned but working". A
> prefill pattern from a pre-4.6 model hard-fails on current models. One narrow exception exists (fallback-credit
> redemption with `fallback_has_prefill_claim: true`), not a general reprieve.

**Replacements**

- **Structured outputs** (`output_config: {format: {...}}` on `messages.create()`) to force valid JSON or a schema (see
  [structured output](../../concepts/structured-output.md)).
- **System prompt instructions** for style control (skip the preamble, fixed format).
