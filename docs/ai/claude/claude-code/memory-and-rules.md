# Memory and rules

Standing instructions that Claude Code loads automatically.

## Memory (`CLAUDE.md`)

Persistent context loaded into every session: project conventions, structure, standing preferences ("never push without
being asked"). Counters the model's [lack of persistent memory](../../limitations.md#no-persistent-memory).

### File hierarchy

All of these can exist at once and **all are loaded**:

| Level                | Location                                         | Notes                                     |
|----------------------|--------------------------------------------------|-------------------------------------------|
| Organization-managed | Fixed OS path, e.g. `/etc/claude-code/CLAUDE.md` | Admin-controlled enterprise policy        |
| User                 | `~/.claude/CLAUDE.md`                            | Personal preferences across every project |
| Project root         | `./CLAUDE.md`                                    | Repo conventions, normally committed      |
| Subdirectory         | `CLAUDE.md` in a nested folder                   | Rules scoped to that area                 |
| Local overrides      | `CLAUDE.local.md` next to any of the above       | Personal, gitignored tweaks               |

Files are **concatenated, not overridden**: Claude walks from the filesystem root down to the working directory and
loads every `CLAUDE.md`/`CLAUDE.local.md`, with each directory's local file appended after its `CLAUDE.md`. There is no
"closer file wins" rule like CSS specificity; if loaded files conflict, which wins isn't guaranteed. Avoid contradictory
instructions across levels instead of relying on precedence.

**Gotcha:** memory is loaded every session and costs context budget on every turn whether or not it is needed, and every
level adds to the same budget. Keep it to durable, frequently relevant facts, not one-off notes.

Example: the practice repo's hard rule "no unsolicited git actions" plus commit instructions
([`.claude/CLAUDE.md`](https://github.com/roknicmilos/learn_claude_code/blob/main/.claude/CLAUDE.md)), backed up by a
[hook](hooks.md) that enforces it.

## Rules (`.claude/rules/`)

A directory of markdown files, each a scoped chunk of standing instructions, as an alternative to one big `CLAUDE.md`.
YAML frontmatter can scope when a rule applies, usually a glob/path pattern so it loads only when Claude touches
matching files. A rule without a scoping key loads unconditionally, i.e. it is just a fragment of `CLAUDE.md`.

Use it once `CLAUDE.md` outgrows "a few rules everyone needs every time", e.g. `frontend.md` scoped to `src/frontend/**`
and `backend.md` to `src/backend/**`. Files are discovered recursively, so subfolders work.

> **Verify:** the frontmatter key for path scoping has been inconsistent across versions and docs (`paths` vs `globs`),
> with reports of one working and the other silently not. Test on your installed version.
