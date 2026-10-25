# Hooks

Scripts (or HTTP/MCP/prompt/agent calls) that Claude Code runs automatically when a named **event** happens: a tool is
about to run, the session starts, Claude finishes responding. They make behavior deterministic and guaranteed (e.g. run
the linter after every edit) instead of hoping the model remembers.

**Gotcha:** a hook fires on *every* matching event, including ones you didn't have in mind. Scope the matcher as
narrowly as the policy requires.

Working example:
[`practical/hooks_example`](https://github.com/roknicmilos/learn_claude_code/tree/main/practical/hooks_example) in the
practice repo (Python scripts wired into that repo's `.claude/settings.json`).

## Protocol

The hook receives a JSON payload on stdin (at least `session_id`, `hook_event_name`, `cwd`) and influences what happens
through its **exit code** and/or JSON on **stdout**:

- **Exit 0:** normal completion. Plain stdout is added to context on a few events (`SessionStart`, `UserPromptSubmit`);
  JSON stdout can carry a structured decision.
- **Exit 2:** blocking error on events that support blocking (e.g. `PreToolUse`, `UserPromptSubmit`). The action is
  stopped and stderr is shown to Claude as the reason.
- **JSON output** keys:
    - `hookSpecificOutput.additionalContext` – inject extra text into Claude's context
    - `hookSpecificOutput.permissionDecision` – `allow` / `deny` / `ask` for `PreToolUse`
    - `hookSpecificOutput.decision.behavior` – `allow` for `PermissionRequest`, skipping the prompt
    - `decision: "block"` + `reason` – `PostToolUse` and `Stop`, to send Claude back to fix something
    - `systemMessage` – a note appended to the system prompt

Each event can declare a **matcher** (tool name, notification type, ...) and, for `PreToolUse`/`PostToolUse`, an `if`
filter in permission-rule syntax (e.g. `"Bash(rm *)"`). `/hooks` lists what is registered; `"disableAllHooks": true` in
`settings.json` turns them all off.

## Wiring (settings.json)

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          { "type": "command", "command": "python",
            "args": ["${CLAUDE_PROJECT_DIR}/hooks/bash_git_guard.py"] },
          { "type": "prompt", "if": "Bash(rm *)", "model": "claude-haiku-4-5", "timeout": 30,
            "prompt": "A Bash command is about to run: $ARGUMENTS. If it could delete something important, respond {\"ok\": false, \"reason\": \"...\"}; otherwise {\"ok\": true}." }
        ]
      }
    ]
  }
}
```

## Example script: guard state-changing git commands

```python
import re, sys
from _common import read_input, ask   # tiny stdin/stdout helpers

STATE_CHANGING = re.compile(
    r"\bgit\s+(add|commit|push|pull|reset|checkout|rebase|merge|clean|stash\s+(drop|clear))\b"
)

data = read_input()
command = data.get("tool_input", {}).get("command", "")
if STATE_CHANGING.search(command):
    ask("State-changing git command detected; confirm before running it.")   # permissionDecision: "ask"
sys.exit(0)
```

It enforces, at harness level, the "no unsolicited git" rule from [`CLAUDE.md`](memory-and-rules.md): a hook is
guaranteed, a memory instruction is only followed.

## Practical hooks in the example

| Event                | Matcher                          | Script                    | Behavior                                                                                                          |
|----------------------|----------------------------------|---------------------------|-------------------------------------------------------------------------------------------------------------------|
| `SessionStart`       | all                              | `session_start_context`   | Injects current git branch and dirty-file count as context                                                        |
| `UserPromptSubmit`   | –                                | `block_secrets_in_prompt` | Blocks (exit 2) a prompt that looks like it contains an API key/secret                                            |
| `PreToolUse`         | `Bash`                           | `bash_git_guard`          | Forces `ask` on state-changing git commands                                                                       |
| `PreToolUse`         | `Bash`, `if: Bash(rm *)`         | inline `prompt` hook      | Cheap model judges whether an `rm` looks safe                                                                     |
| `PreToolUse`         | `Edit\|Write`                    | `protect_files`           | Denies edits to `.env*`, `package-lock.json`, `.venv/`                                                            |
| `PermissionRequest`  | `Bash`                           | `allow_readonly_git`      | Auto-approves read-only git (`status`, `log`, `diff`, `show`, `branch`)                                           |
| `PostToolUse`        | `Edit\|Write`                    | `validate_edit`           | Compiles/parses just-written `.py`/`.json`/`.ipynb`; blocks with the error                                        |
| `PostToolUseFailure` | –                                | `log_tool_failure`        | Logs failed tool calls to `logs/tool_failures.jsonl`                                                              |
| `Notification`       | `permission_prompt\|idle_prompt` | `notify`                  | Beeps when Claude waits for you                                                                                   |
| `Stop`               | –                                | `stop_no_em_dash`         | Reads the last assistant message, blocks if it breaks a style rule; guards on `stop_hook_active` to avoid looping |
| `StopFailure`        | –                                | `stop_failure_log`        | Beeps and logs the API error type (`rate_limit`, `overloaded`, ...)                                               |
| `PreCompact`         | –                                | `precompact_backup`       | Copies the transcript to `logs/transcripts/` before compaction                                                    |
| `SessionEnd`         | –                                | `session_end_summary`     | Appends a one-line session summary to `logs/sessions.jsonl`                                                       |
| `FileChanged`        | `.env`                           | `file_changed_env`        | Tells Claude a `.env` changed on disk, so it doesn't rely on a stale read                                         |
| `ConfigChange`       | `project_settings`               | `config_change_warn`      | Warns (`systemMessage`) and logs when `settings.json` changes mid-session                                         |

## Observe-only events

`Setup`, `UserPromptExpansion`, `PermissionDenied`, `PostToolBatch`, `MessageDisplay`, `SubagentStart`, `SubagentStop`,
`TaskCreated`, `TaskCompleted`, `TeammateIdle`, `InstructionsLoaded`, `CwdChanged`, `DirectoryAdded`, `WorktreeRemove`,
`PostCompact`, `PreModelSwitch`, `PostModelSwitch`, `Elicitation`, `ElicitationResult` are all wired to one generic
`log_event.py`, run `async`, that appends the full payload to `logs/events.jsonl` so you can see what each event
delivers. `WorktreeCreate` is intentionally left unwired: a hook on it can take over worktree creation, so a plain
logger could interfere.

> **Verify:** the event list grows between Claude Code versions.

## Other hook types

All of the above use `"type": "command"`. Others:

- **`prompt`** – sends the input to a cheap model (default Haiku) and acts on `{"ok": true/false, "reason": ...}`.
- **`agent`** – like `prompt` but runs a full agentic loop with tools (e.g. "run the tests and confirm they pass"); slow
  and costly per trigger. `{ "type": "agent", "prompt": "Run the test suite and confirm it passes. $ARGUMENTS",
  "timeout": 120 }`
- **`http`** – POSTs the payload to a URL and acts on the response. `{ "type": "http", "url":
  "http://localhost:8080/hooks/pre-tool-use", "timeout": 30 }`
- **`mcp_tool`** – calls a tool on a registered [MCP server](mcp-example.md). `{ "type": "mcp_tool", "server":
  "mcp-tasks-server", "tool": "create-task", "input": {...} }`
