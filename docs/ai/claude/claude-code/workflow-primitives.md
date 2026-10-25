# Workflow primitives: which feature for which trigger

A [workflow](../../concepts/agents-and-workflows.md#workflow) is a concept (a fixed sequence of steps), and Claude Code
has
no single feature called "workflow". Build one from whichever primitive matches the trigger and the reliability you
need:

| If the trigger is...                              | Reach for...                                                                          |
|---------------------------------------------------|---------------------------------------------------------------------------------------|
| "I keep retyping this multi-step procedure"       | [Skill](skills-and-commands.md)                                                       |
| "this step needs isolated context or fewer tools" | [Subagent](subagents.md)                                                              |
| "this must happen every time, no exceptions"      | [Hooks](hooks.md)                                                                     |
| "Claude should always know this, every session"   | [Memory](memory-and-rules.md) (`CLAUDE.md`)                                           |
| "this must react to PRs/issues, even offline"     | [GitHub Actions integration](automation.md#github-actions-integration)                |
| "this must run repeatedly on a timer"             | [Scheduled tasks](automation.md#scheduled-tasks-loop-schedule) (`/loop`, `/schedule`) |

They compose freely: a hook can call a skill, a GitHub Actions run can invoke a subagent, a scheduled task can run a
skill
on a timer. There is no "correct" one; the right mix makes the fixed steps reliable without over-constraining the parts
that need judgment.
