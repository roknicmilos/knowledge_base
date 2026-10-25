# Git commit messages (Conventional Commits)

Format:

```
<type>(<scope>): <description>

[optional body]

[optional footer(s)]
```

- `<scope>` is optional (`feat(auth): add login`).
- **Breaking change:** append `!` (`feat(api)!: drop v1 endpoints`) and/or add a `BREAKING CHANGE: …` footer.
- SemVer mapping: `fix` → patch, `feat` → minor, breaking change → major.

The Conventional Commits spec itself only defines `feat` and `fix`; the other types below are the widely used Angular /
`@commitlint/config-conventional` set.

## Common types

| Type       | Meaning                                | Example                                                              |
|------------|----------------------------------------|----------------------------------------------------------------------|
| `feat`     | New feature for the user               | `feat: add custom validation error handler returning 400 status`     |
| `fix`      | Bug fix for the user                   | `fix: resolve timezone issues in due date validation`                |
| `docs`     | Documentation only                     | `docs: add API usage examples to README`                             |
| `style`    | Formatting etc., no behavior change    | `style: format code with black and fix import ordering`              |
| `refactor` | Neither fixes a bug nor adds a feature | `refactor: extract validation logic into separate validators module` |
| `test`     | Add/correct tests                      | `test: add unit tests for todo creation validation`                  |
| `chore`    | Maintenance, tooling                   | `chore: update FastAPI to latest version and refresh dependencies`   |
| `perf`     | Performance improvement                | `perf: optimize error message processing in validation handler`      |
| `ci`       | CI config and scripts                  | `ci: add GitHub Actions workflow for automated testing`              |
| `build`    | Build system / external dependencies   | `build: configure Docker multi-stage build for production`           |
| `revert`   | Reverts a previous commit              | `revert: "feat: add custom validation error handler"`                |

## Non-standard types seen in the wild (use only if your team agrees)

`security`, `deps` (usually written `build(deps): …`), `config`, `init`, `release`, `hotfix` (a branch concept – use
`fix`),
`wip` (don't merge WIP commits into shared branches).
