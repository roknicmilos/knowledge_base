# Anthropic products and models

A quick map of the lineup so tool-specific terms elsewhere have somewhere to point back to.

> **Verify:** written as of 2026-09-02; the lineup and model names change quickly.

| Product                            | What it is                                                                                              |
|------------------------------------|---------------------------------------------------------------------------------------------------------|
| **Claude.ai**                      | Consumer/web chat app (plus iOS/Android) for one-off questions, drafting, general assistance            |
| **[Claude Code](claude-code/README.md)** | CLI/IDE agent for software engineering: terminal CLI, desktop app (Mac/Windows), web app (claude.ai/code), IDE extensions (VS Code, JetBrains) |
| **[Claude API](api/README.md)**    | Developer access to Claude models via the Messages API, for custom apps and agents                      |
| **Claude Agent SDK**               | Claude Code's agent harness as a library (`claude-agent-sdk` on PyPI, `@anthropic-ai/claude-agent-sdk` on npm)  |
| **Claude for Enterprise / Work**   | Enterprise plans: admin controls, SSO, higher limits                                                    |
| **Claude for Financial Services / Life Sciences** | Industry-specific offerings with domain tooling and integrations                         |
| **Claude in Slack (Claude Tag)**   | Claude inside a Slack workspace (channels and DMs)                                                      |

## Agent SDK vs API tool loop vs Managed Agents

- **Claude API tool-use loop:** you get *no* built-in tools, you define every tool yourself.
- **Agent SDK:** the full Claude Code harness (tool loop, context management, permissions, built-ins such as
  Read/Write/Edit, Bash, Glob/Grep, WebSearch/WebFetch, MCP, subagents, hooks) embedded in your Python/TypeScript app via
  `query(prompt, options)`. You host and deploy it yourself.
- **Managed Agents:** Anthropic hosts both the loop *and* the execution sandbox.

The SDK sits in between: full built-in harness, self-hosted deployment.

## Model family

Opus, Sonnet and Haiku, each released in generations (the notes list generation 5, e.g. Opus 5, Sonnet 5, plus
experimental releases like Fable 5.1).

Product names (Claude Code, Claude.ai) and model names are different axes: any product can run on any of several models.
