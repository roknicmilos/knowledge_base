# MCP server example: a tasks API as tools

A practice project showing the [Model Context Protocol](../../concepts/tool-use-and-mcp.md#mcp--model-context-protocol):
a small MCP server that
wraps a REST API and exposes it as tools Claude Code can call. Source:
[`practical/mcp_example`](https://github.com/roknicmilos/learn_claude_code/tree/main/practical/mcp_example).

```
Claude Code ──MCP (stdio)──▶ mcp_tasks_server (Node/TS) ──HTTP──▶ example_api (FastAPI, in-memory)
```

The server has no logic beyond translating tool calls into HTTP requests, so the API must be running first.

## The API (FastAPI)

| Endpoint      | Purpose                                                                                        |
|---------------|------------------------------------------------------------------------------------------------|
| `GET /`       | API description and schema                                                                     |
| `GET /tasks`  | List tasks                                                                                     |
| `POST /tasks` | Create a task. Body `{"name": "...", "is_completed": false}`; `201`, or `400` on invalid input |

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/uvicorn main:app --reload --port 8000
curl -s -X POST localhost:8000/tasks -H 'Content-Type: application/json' -d '{"name": "Write docs"}'
```

## The MCP server (TypeScript SDK)

Tools exposed: `get-root`, `list-tasks`, `create-task` (params `name`, `is_completed`).

```ts
const server = new McpServer({ name: "mcp-tasks-server", version: "1.0.0" });

server.registerTool(
  "create-task",
  {
    title: "Create task",
    description: "Calls POST /tasks/ to create a new task",
    inputSchema: { name: z.string(), is_completed: z.boolean() },
  },
  async ({ name, is_completed }) => {
    const res = await fetch(`${BASE_URL}/tasks/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name, is_completed }),
    });
    return { content: [{ type: "text", text: `Status ${res.status}: ${await res.text()}` }] };
  }
);

await server.connect(new StdioServerTransport());
```

## Register it with Claude Code

```bash
cd mcp_tasks_server && npm install && npm run build
claude mcp add mcp-tasks-server -- node /absolute/path/to/mcp_tasks_server/build/index.js
```

Restart Claude Code (or run `/mcp`). Tools appear as `mcp__mcp-tasks-server__list-tasks` etc. Other registration ways:
`--scope user`, or editing `.mcp.json` directly. A [skill](skills-and-commands.md) can then wrap a tool, e.g. "publish a
task".

## Prompts

MCP servers can also expose **prompts**: user-invoked templates (vs tools, which the model decides to call). This server
exposes `task-status-report` (optional `audience` argument).

Claude Code discovers MCP prompts but, as noted in the example, has no documented way to invoke them as slash commands
(upstream issue closed as not planned). Try them with the
[MCP Inspector](https://github.com/modelcontextprotocol/inspector)
(`npx @modelcontextprotocol/inspector node build/index.js`,
"Prompts" tab); in Claude Code prefer a skill or project slash command for this kind of template.

> **Verify:** the MCP prompts limitation reflects the state when the example was written.
