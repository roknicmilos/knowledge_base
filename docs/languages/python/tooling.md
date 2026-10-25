# Python tooling: package managers, linters, formatters

## Package managers

|                       | pip                           | Poetry          | Conda            | Pipenv           | PDM         | Hatch                | uv                         |
|-----------------------|-------------------------------|-----------------|------------------|------------------|-------------|----------------------|----------------------------|
| Use case              | General installer             | Modern projects | Data science     | virtualenv + pip | Lightweight | Packaging/build      | All-in-one project manager |
| Env management        | No (use `venv`)               | Yes             | Yes              | Yes              | Optional    | Yes                  | Yes                        |
| Dependency resolution | Yes (resolver since pip 20.3) | Yes             | Yes              | Yes              | Yes         | Limited              | Yes                        |
| Lockfile              | No (`pip freeze`)             | Yes             | Yes (env export) | Yes              | Yes         | No (without plugins) | Yes (`uv.lock`)            |
| Non-Python packages   | No                            | No              | **Yes**          | No               | No          | No                   | No                         |
| Speed                 | Fast                          | Moderate        | Moderate         | Moderate         | Fast        | Moderate             | **Very fast** (Rust)       |

Choosing:

1. **New general project → `uv`** ([docs](https://docs.astral.sh/uv/)): extremely fast package and project manager
   written in
   Rust by Astral (the Ruff authors); manages venvs, lockfiles, scripts and Python versions.
2. Poetry – mature alternative with good community support.
3. Data science / non-Python dependencies → Conda (or Pixi).
4. Simplicity → `pip` + `venv`.
5. PDM or Hatch for lightweight/packaging-centric workflows.

> **Verify:** this space moves quickly – re-check recommendations once a year.

### Python vs JavaScript package managers

|          | JavaScript                                             | Python                                                   |
|----------|--------------------------------------------------------|----------------------------------------------------------|
| Tools    | npm (default), Yarn (Classic/Berry), pnpm, bun         | pip (default), uv, Poetry, Pipenv, conda                 |
| Registry | npm registry (+ private, e.g. GitHub Packages)         | PyPI (+ conda-forge for conda)                           |
| Focus    | Fast installs, dependency resolution, Node integration | Virtual environments, resolution, cross-platform compat. |

JavaScript installs into a project-local `node_modules`, so it doesn't need a virtual environment; Python installs into
an
environment – use one per project.

## Linters, formatters, type checkers

| Tool       | Type                         | Focus                                                             | Speed        | Use                     |
|------------|------------------------------|-------------------------------------------------------------------|--------------|-------------------------|
| Flake8     | Linter                       | Style, PEP 8, errors                                              | Fast         | General linting         |
| Pylint     | Linter                       | Detailed quality checks                                           | Moderate     | Comprehensive feedback  |
| **Ruff**   | Linter + formatter + autofix | All-in-one (replaces Flake8, isort, Black-style formatting, more) | Blazing fast | Modern default          |
| Black      | Formatter                    | Code formatting                                                   | Fast         | Consistent style        |
| isort      | Import sorter                | Import order                                                      | Fast         | Managing imports        |
| Bandit     | Security linter              | Security issues                                                   | Fast         | Finding vulnerabilities |
| Pyright    | Type checker                 | Type hint compliance                                              | Fast         | Type-safe codebases     |
| mypy       | Type checker                 | Type annotations validation                                       | Moderate     | Type-safe codebases     |
| Pyflakes   | Minimal linter               | Error detection                                                   | Very fast    | Simple checks           |
| Prospector | Aggregator                   | Combines several tools                                            | Moderate     | All-in-one              |

When to use which:

1. General linting: Ruff (or Flake8).
2. Comprehensive quality checks: Pylint.
3. Type checking: Pyright or mypy.
4. Formatting: Ruff format, or Black + isort.
5. Security audits: Bandit.
6. Speed/coverage: Ruff.

For most modern projects Ruff replaces Black, Flake8, isort and more in one fast tool
([docs](https://docs.astral.sh/ruff/)).

### Linting vs type checking

Both are forms of static analysis.

|                     | Type checking (mypy)                                   | Linting (Ruff)                                      |
|---------------------|--------------------------------------------------------|-----------------------------------------------------|
| Purpose             | Verify type correctness and consistency                | Enforce style, find coding errors, maintain quality |
| Focus               | Type hints and type safety                             | Style, best practices, common bugs                  |
| Checks type hints   | Yes                                                    | No (can *require* annotations via `ANN` rules)      |
| Enforces type hints | No – only checks those present                         | Can flag missing annotations                        |
| Code style          | Doesn't enforce                                        | PEP 8 and other style guides                        |
| Speed               | Slower on large projects                               | Extremely fast                                      |
| Typical findings    | Incompatible argument types, missing return annotation | Unused imports, whitespace, naming convention       |
