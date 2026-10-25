# Claude Code

Claude Code is Anthropic's agentic CLI/IDE tool for software engineering (see [products](../products.md)). Its
customization
features and how to combine them.

## Customizing the agent

- [Skills and commands](skills-and-commands.md) – reusable know-how (model-summoned) and saved prompts (user-invoked)
- [Subagents](subagents.md) – isolated workers, plus `context: fork`
- [Hooks](hooks.md) – deterministic scripts on lifecycle events, with a worked example
- [Memory and rules](memory-and-rules.md) – `CLAUDE.md` hierarchy and `.claude/rules/`
- [MCP server example](mcp-example.md) – a tasks API exposed as MCP tools
- [Built-in tools](built-in-tools.md)

## Running it

- [Automation: print mode, GitHub Actions, scheduled tasks](automation.md)
- [Parallel sessions with git worktrees](worktrees.md)
- [Context management: `/clear` vs `/compact`](context-management.md)
- [Artifacts](artifacts.md)

## Design

- [Workflow primitives: which feature for which trigger](workflow-primitives.md)
