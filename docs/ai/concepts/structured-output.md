# Structured output and JSON extraction

Getting machine-parseable output (usually JSON) from a model.

## Prompt-based JSON

Ask in the prompt ("respond with only valid JSON matching this shape"). Cheap and zero setup, but **no guarantee**: the
model may wrap the JSON in prose, truncate it, or emit almost-valid JSON. Fine for low-stakes or exploratory use; for
production add a parser plus a retry/validation step.

## Schema-constrained extraction

Shape the output with a [tool call](tool-use-and-mcp.md#tool-use) whose input schema is the JSON schema you want, or with
a dedicated structured-output parameter. This removes syntax errors (missing brackets, trailing commas, unquoted keys)
by construction. Prefer it for anything a downstream system parses automatically.

Forcing the call is done with [`tool_choice`](tool-use-and-mcp.md#tool-choice).

## Missing information

A schema doesn't fix *missing information*. Required fields pressure the model into fabricating a plausible value
instead of admitting it doesn't know. Make fields optional/nullable where the answer may genuinely be absent so the
model can return `null` instead of [hallucinating](../limitations.md#hallucination) to satisfy the shape.

## Confidence scores

Asking the model to report its own confidence ("0–100", "low/medium/high") next to the answer is a weak triage signal:
auto-accept high-confidence results, route low-confidence ones to a human or a stronger model. It correlates only
loosely with correctness (the same fluency that drives hallucination produces a confident "95% sure" on wrong answers),
so combine it with real verification: run the code, check a source, sample several times and compare. See
[AI fluency](../ai-fluency.md).
