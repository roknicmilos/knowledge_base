# Built-in tools

The native, always-available tools of the Claude Code harness, as opposed to anything added later via
[MCP](../../concepts/tool-use-and-mcp.md#mcp--model-context-protocol) or a [skill](skills-and-commands.md). No setup or
connection step.

Core set:

- `Bash` (shell), `Read` / `Write` / `Edit` (files), `Glob` / `Grep` (file search), `NotebookEdit` (Jupyter cells)
- `Agent` (spawn [subagents](subagents.md)), `Skill` (invoke a packaged skill)
- `AskUserQuestion` (structured clarifying questions), `WebFetch` / `WebSearch`
- orchestration tools: scheduling, cross-agent messaging

**Gotchas**

- Core file/shell operations are native, not MCP-provided. Don't assume a capability comes from an MCP server because it
  "feels" like an integration.
- The tools available can be a subset: a subagent definition can restrict which ones it gets.

> **Verify:** the tool list changes between Claude Code versions.
