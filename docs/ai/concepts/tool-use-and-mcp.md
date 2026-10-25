# Tool use and MCP

How a text model gets to act on the world and fetch fresh data.

## Tool use

Also called *function calling*. The model is given a menu of functions (search, run code, hit an API) and decides when to
call them and with which arguments. The model never executes anything itself: it outputs a *request* (name +
arguments), the surrounding program runs it and feeds the result back (see
[agent loop](agents-and-workflows.md#agent)).

Write each tool with a tight, unambiguous description and schema: the model chooses *whether* and *which* tool from the
description alone, so a vague one ("does stuff with data") gets picked wrong or skipped.

## Tool choice

The `tool_choice` request parameter controls whether and which tool the model may or must call on this request:

| Value  | Meaning                                                   |
|--------|-----------------------------------------------------------|
| `auto` | Model decides whether to call a tool and which (default)  |
| `any`  | Model must call *some* tool, picks which                  |
| `tool` | Model must call one specific named tool                   |
| `none` | No tool calls this turn, even if tools are defined        |

Defining a tool makes it available; `tool_choice` decides how free the model is to use it on this call. Force a tool in a
pipeline stage that must always produce structured output ([structured output](structured-output.md)); keep `auto` for
open-ended conversational steps.

Since every API request is independent, your own code can send a different `tool_choice` per request (e.g. force
classification on the first request of a turn, then `auto` for the follow-up). That is not a built-in per-turn config.

> **Verify:** forced tool calls (`any`/`tool`) were removed on some newer Claude models (e.g. Fable 5.1, Opus 5.5) and
> return an error. There, use `auto` plus a prompt instruction naming the tool, `strict: true` on the schema, or a
> structured-output parameter.

## Turn

One exchange: a user message and the assistant's response. In an agent loop a single user-visible turn can involve
several API requests (call tool → get result → call another → final text); those are all part of one turn.

## MCP – Model Context Protocol

An open standard for connecting models to external tools and data through a common interface: a tool exposes an **MCP
server**, any MCP-aware client can use it (a USB-C port for AI).

- The **server** is the program/connector; it *exposes* individual **tools** (`create_issue`, `search_repos`) that are
  merged into the model's available tool list next to native built-ins. It can also expose **prompts** (user-invoked
  templates).
- Tool use ≠ MCP: tool use is the *capability* (the model calls functions); MCP is a *standard* for exposing and wiring
  them. You can do tool use with hand-wired functions; MCP makes the wiring reusable across clients.
- MCP is not how every capability arrives. In Claude Code, file and shell operations (Bash, Read, Write, Edit) are native
  [built-in tools](../claude/claude-code/built-in-tools.md); MCP *adds* extras (browser automation, integrations).

Hands-on example: [MCP server example](../claude/claude-code/mcp-example.md).
