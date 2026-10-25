# Sampling parameters and determinism

How randomness enters an LLM's output, and what that means for building reliable systems on top of it.

## Temperature

A number (typically 0–1, sometimes up to 2) that rescales the next-token probabilities before the model picks one. Low =
focused and repeatable; high = varied and creative.

| Task                                     | Typical value |
|------------------------------------------|---------------|
| Summarizing, extracting structured data  | 0–0.2         |
| Brainstorming names, ad-copy variants    | 0.8–1.0       |

- Many API defaults sit around 1.0, which is often too high for factual/code work – override it explicitly.
- Only applies when calling the API yourself. claude.ai and Claude Code expose no temperature control.
- **Temperature 0 is not fully deterministic**: batching and floating-point non-associativity on the provider's
  hardware still cause small run-to-run variation.

> **Verify:** on current Claude models with adaptive thinking on by default, the API rejects an explicit `temperature`
> (HTTP 400). Check the model's docs before relying on it.

## Top-p (nucleus sampling)

Sample only from the smallest set of tokens whose probabilities add up to `p` (e.g. 0.9); ignore the long tail. Lower
`p` = safer, narrower choices.

**Temperature vs top-p:** temperature reshapes the whole distribution (flatter vs peakier); top-p truncates it. Tune one,
not both, otherwise you can't tell which one moved the result. Temperature for overall "creativity", top-p to cut off
the unlikely tail.

## Deterministic vs probabilistic

- **Deterministic** system: same input → same output (a script, linter, regex, a Claude Code
  [hook](../claude/claude-code/hooks.md)).
- **Probabilistic** system: samples its output from a distribution, so the same input can yield different outputs (an
  LLM choosing each next token).

Deterministic steps are guaranteed, repeatable and easy to test. Probabilistic steps handle ambiguity and judgment but
need property-based checks rather than exact matching (see [Prompt evaluation](prompt-evaluation.md)).

**Rule of thumb:** if a step *must* happen or *must* be exactly right every time, make it deterministic (code, hooks,
code-based graders). Give the model only the parts that need judgment, and wrap its output in deterministic validation
where it matters.

## Handling non-determinism

- Don't build logic that expects byte-identical output (e.g. exact-string match on a response in a test).
- For repeatability: lower temperature/top-p, constrain the format ([structured output](structured-output.md)), and
  verify *properties* of the output rather than its text.
- For safety- or business-critical steps add a human or automated check instead of trusting a single run.

See also [Limitations: non-determinism](../limitations.md#non-determinism).
