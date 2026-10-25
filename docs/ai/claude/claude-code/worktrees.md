# Parallel sessions with git worktrees

Run several Claude Code instances on different branches *at the same time*, each in its own working directory via `git
worktree`, instead of one instance repeatedly stashing and switching branches.

```bash
claude -w feature-1            # native: runs `git worktree add` for you
# or manually
git worktree add ../feature-1 feature-1 && cd ../feature-1 && claude
```

Use it for genuinely independent branches, e.g. one instance fixing `hotfix/x` while another builds `feature/y`: each
worktree has its own checked-out files, so there are no file-state collisions.

**Gotchas**

- Worktrees share the same `.git` directory, so operations on shared git state can still interact (e.g. deleting a
  branch another worktree has checked out).
- The isolation is at the filesystem level, not the history level: reconverging the work still needs the usual
  merge/rebase.
