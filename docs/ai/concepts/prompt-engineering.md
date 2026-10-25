# Prompt engineering

Structuring a prompt so a model reliably gives better output, without touching the model itself. It is the cheapest,
fastest lever, so try it before [RAG or fine-tuning](../fine-tuning-prompting-rag.md).

## Prompt

The instruction and context sent to the model.

- **System prompt:** standing rules and role for the whole session (tone, format, constraints).
- **User prompt:** the specific request.

Put durable instructions in the system prompt so they aren't restated every turn. In Claude Code the reuse progression
is: prompt (ad hoc) → [command](../claude/claude-code/skills-and-commands.md) (you reuse it) →
[skill](../claude/claude-code/skills-and-commands.md) (the model reuses it for you).

## Six techniques

1. **Provide context** – background, constraints, goal, what already failed, what "done" looks like. A model guessing
   at intent is guessing at the answer.
2. **Offer examples (few-shot)** – show one or two input → desired-output pairs; resolves ambiguity about format and
   tone that a description leaves open.
3. **Specify output constraints** – length, format (JSON, table, prose), what to include or exclude. Unstated format
   means the model picks one.
4. **Break down complex tasks** – ordered smaller instructions instead of one dense paragraph (the single-prompt version
   of a [workflow](agents-and-workflows.md#workflow)).
5. **Give the model space to think** – ask for step-by-step reasoning before the answer; see
   [Reasoning](reasoning.md).
6. **Define roles** – "you are a senior security reviewer" steers tone, priorities and vocabulary.

Iterate one technique at a time and compare outputs (like debugging code), and judge changes with
[Prompt evaluation](prompt-evaluation.md) instead of eyeballing a few outputs.

## Limits

Prompting has a ceiling. If the model lacks the knowledge or capability, no wording fixes it reliably: use
[RAG](../rag.md) for missing knowledge or [fine-tuning](training-and-inference.md#fine-tuning) for missing
behavior/style.

## Stop sequences and prefilling (Claude API)

Two request-level techniques for controlling *where a response ends* and *how it begins*. Both are API parameters, not
Claude Code / claude.ai features. Details: [Stop sequences and prefilling](../claude/api/stop-sequences-and-prefilling.md).
