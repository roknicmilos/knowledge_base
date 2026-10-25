# Automation: print mode, GitHub Actions, scheduled tasks

Running Claude Code without sitting at an interactive session.

## Print mode (`claude -p`)

Runs non-interactively: executes one prompt and exits. This makes Claude Code scriptable (pipelines, CI, scheduled
scripts).

```bash
cat build-error.txt | claude -p "explain this error"
claude -p "query" --output-format json | jq -r '.result'
```

- `--continue` resumes the most recent conversation; `--resume <session_id>` a specific one, so multi-turn scripted
  workflows are possible.
- `--output-format`: `text` (default), `json` (one object per run with `result`, `session_id`, `total_cost_usd`; handy
  to
  log cost per call), `stream-json` (newline-delimited events for real-time consumption).
- **Gotcha:** print mode skips interactive-only UX such as the workspace trust dialog, so only run it in directories you
  already trust.

## GitHub Actions integration

`anthropics/claude-code-action` runs Claude Code inside a workflow (`.github/workflows/*.yml`): respond to `@claude`
mentions on issues/PRs, review every PR, or run on a `schedule:` cron, entirely outside your machine.

**Gotcha:** it is a separate environment and doesn't inherit your local `CLAUDE.md`, hooks or permissions unless those
files are committed and picked up by the action.

## Scheduled tasks (`/loop`, `/schedule`)

- `/loop` re-runs a prompt on a session-scoped timer (or lets Claude self-pace), e.g. `/loop 5m check if CI is green`.
- `/schedule` has **two different modes** that look the same:

| Mode                    | Runs on                                    | Survives closing the terminal?                                                                    |
|-------------------------|--------------------------------------------|---------------------------------------------------------------------------------------------------|
| Session-scoped reminder | Local `CronCreate`/`CronList`/`CronDelete` | No: only fires while Claude Code is running and idle (an unexpired one can return via `--resume`) |
| Cloud routine           | Anthropic-managed infrastructure           | Yes, even if the machine is off                                                                   |

If a task must fire even when everything is closed, confirm it was created as a **cloud routine**.
