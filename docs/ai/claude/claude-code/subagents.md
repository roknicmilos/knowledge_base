# Subagents and forked sessions

## Subagent

A separate assistant instance spun up for a focused sub-task in its own context, which reports a result back to the main
agent. It keeps the main conversation uncluttered and allows specialized roles (reviewer, researcher). Same underlying
model and harness, just narrower: cold context, sometimes a restricted tool allowlist, one task.

- Use it to parallelize or isolate work, e.g. searching a large codebase so noisy intermediate results don't pollute the
  main context.
- Model, reasoning effort, tool access and permission mode are **inherited** from the main conversation unless the agent
  definition overrides them (e.g. a cheaper model for a narrow lookup).
- Built-in types: `Explore` (read-only code search), `Plan` (designs implementation plans, writes no code),
  `general-purpose` (multi-step research/execution), `claude-code-guide` (questions about Claude Code/API/Agent SDK),
  `statusline-setup`, `claude` (catch-all).

**Gotchas**

- A subagent doesn't inherit what you know unless the prompt hands it over; a cold start is wasteful for trivial work.
  Worth it when the output matters more than the intermediate steps.
- It isn't sealed off: it can ask you clarifying questions mid-task (auto-continuing after a timeout) and its permission
  prompts still reach you, governed by the active permission mode.
- It reports back on the normal completion path, not as a hard guarantee.

Multi-agent orchestration
theory: [coordinator pattern](../../concepts/agents-and-workflows.md#coordinator-hub-and-spoke).

## Forked session (`context: fork`)

A `context: fork` field in the YAML frontmatter of a `SKILL.md` or slash command runs it in an isolated, subagent-like
context instead of inline. Each invocation starts clean and only the finished result returns to the main conversation,
not
the intermediate reasoning or tool output.

- Use for skills/commands with concrete actionable steps (a deploy skill) whose execution noise you don't want to keep.
- Same trade-off as a subagent: lean main context, but nothing is inherited beyond what the skill tells it.
- **Gotcha:** it only pays off when the skill contains a task. A pure reference skill ("our API conventions", no ask)
  gives the fork nothing to do and wastes it.
