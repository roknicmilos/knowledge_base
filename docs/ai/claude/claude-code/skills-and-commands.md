# Skills and commands

Two ways to package instructions for reuse in Claude Code.

## Skill

A reusable capability authored as a folder with a `SKILL.md` (instructions plus optional scripts/resources), part of
Anthropic Agent Skills. The model loads it **on demand** when a task matches the skill's description, keeping the base
context lean. Use it for repeatable know-how ("how we build a feature", "how to format our reports").

**Gotcha:** matching happens against the *description alone*, before the skill content is in context. A vague
description
means the skill is never loaded. Write it like a search query someone would type for this exact task, not a summary.

```markdown
---
name: publish-task
description: Publish/create a new task via the mcp-tasks-server create-task tool. Use when the user says "publish a task".
---
Steps: 1. determine the task name ... 2. call `mcp__mcp-tasks-server__create-task` ... 3. report the result.
```

Example from the practice repo:
[`.claude/skills/publish-task`](https://github.com/roknicmilos/learn_claude_code/tree/main/.claude/skills/publish-task)
(drives the [MCP example](mcp-example.md)).

## Commands

Saved, named prompts triggered with `/name` (markdown files, often in `.claude/commands`), optionally with arguments.
They
turn a repeated instruction into a one-word invocation, e.g. `/feature:plan`.

## Skill vs command

- A **command** is *invoked*: you type `/name` to fire a saved prompt on purpose ("do this exact thing now").
- A **skill** is *summoned*: the model pulls it in when a task matches ("know how to do this whenever it comes up").

Progression: [prompt](../../concepts/prompt-engineering.md#prompt) (ad hoc) → command (you reuse it) → skill (the model
reuses it for you).

## Skill vs subagent

A skill adds *knowledge/procedure* to the current worker; a [subagent](subagents.md) adds a *separate worker* with its
own
context. Use a skill to standardize *how* something is done, a subagent to offload a chunk of work. They combine: a
subagent can use skills.
