# Agents, workflows and multi-agent patterns

Ways to orchestrate model calls: from a fixed pipeline to a free-running agent.

## Model vs agent

The **model** thinks; the **agent** acts. A model takes text in and gives text out. An agent wraps it in a loop with
tools so it can gather input, take steps and pursue a goal. Every agent contains a model; not every model use is an
agent.

## Agent

A model in a loop: it decides a step, calls a tool, reads the result, repeats until the goal is met. Use it when a task
needs several dynamic steps that can't be scripted in advance.

**How the loop works:** the model only outputs a *request* to call a tool. A surrounding program (the **harness**, e.g.
Claude Code) runs it and appends the result to the conversation. Each turn the harness sends the full conversation plus
the catalog of tools (name/description/schema); the model replies with another tool call or a final answer. The model
*decides*, the harness *executes*.

- Agent task: "fix the failing tests in this repo" (it must read, run and adapt).
- Not an agent task: "extract the invoice number from this PDF" (a single call).

## Workflow

A predefined sequence of steps orchestrating one or more model calls along a fixed path (*summarize → classify →
route*). Use it when steps are known and repeatable and you want reliability over improvisation. A support pipeline
*classify → look up account → draft reply* is a workflow: fixed code with a model call per stage.

## Agent vs workflow

|               | Workflow                           | Agent                           |
|---------------|------------------------------------|---------------------------------|
| Path          | Fixed, author-decided              | Decided at runtime              |
| Strength      | Reliability, predictability, cost  | Flexibility on open-ended tasks |
| Rule of thumb | Use if you can enumerate the steps | Use when you can't              |

Reaching for an agent when a workflow would do costs reliability and money: an open-ended loop can take a different path
every run.

## Task decomposition

How a large goal is split into steps:

- **Static upfront (prompt chaining / pipeline):** the whole sequence is fixed before execution; each stage's output
  feeds the next. Use when the work's shape is known (billing dispute: *verify identity → fetch invoice → check policy →
  propose adjustment*).
- **Dynamic adaptive:** start from a high-level goal, investigate, then generate/revise subtasks as dependencies and
  blockers are discovered (e.g. "add tests to a legacy codebase": map it, find high-impact areas, plan, adapt).

It is the same split as workflow vs agent, applied to task breakdown. Dynamic decomposition trades predictability for
coverage (time and cost vary), so don't use it just because a task feels complex.

## Coordinator (hub-and-spoke)

The central agent in a multi-agent setup: it receives the task, decomposes it, decides which
[subagents](../claude/claude-code/subagents.md) to invoke, passes them context and aggregates results. All communication
goes through it; subagents don't talk to each other.

- Use when a task splits into independent sub-investigations that would clutter one agent's context.
- If the final output is incomplete in *scope* (a piece missing entirely), the coordinator's decomposition is almost
  always the root cause.
- **Gotcha:** forwarding only a *summary* of one subagent's findings to another loses detail, and the receiver may
  "correct" it from stale training knowledge. Whether full detail or a summary crosses the boundary is the coordinator's
  prompt/logic, not a guarantee of the pattern: verify what actually gets passed.

## Building a workflow in Claude Code

There is no single "workflow" feature. Pick the primitive that matches the trigger: see
[Workflow primitives](../claude/claude-code/workflow-primitives.md).
