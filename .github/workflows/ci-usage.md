# CI Workflow

`ci.yml` runs on every push to `main` and on every pull request. It is the primary
quality gate — release workflows never run if this one is red.

## Triggers

| Event               | Branches |
| ------------------- | -------- |
| `push`              | `main`   |
| `pull_request`      | all      |
| `workflow_dispatch` | manual   |

Concurrent runs on the same ref are cancelled automatically (new push supersedes
the old run). Deploy jobs are never affected because they live in separate workflows.

## Jobs

```text
quality ──► test (3.11 / 3.12 / 3.13, parallel)
```

### `quality` — Lint & Type Check

Runs first and gates the test matrix. Steps:

1. `uv sync --frozen --extra dev` — frozen install from `uv.lock`
2. `ruff check .` — lint
3. `ruff format --check .` — format check
4. `uv run ty check` — type check (configured via `[tool.ty]` in `pyproject.toml`)
5. `uv run pyright` — type check complémentaire (configured via `[tool.pyright]`)
6. `PYTHONPATH=src uv run lint-imports` — import-linter contracts (couches hexagonales)

### `test` — pytest matrix

Runs only after `quality` passes. Covers Python 3.11, 3.12, 3.13 in parallel
(`fail-fast: false` so all cells report even if one fails).

Steps:

1. `uv sync --frozen --extra dev`
2. `uv run pytest` — reads `pyproject.toml`, applies `--cov-fail-under=70`
3. Upload `coverage.xml` + `htmlcov/` as artifact (Python 3.11 cell only)

## Local equivalent

```bash
# Quality gate
uv run ruff check .
uv run ruff format --check .
uv run ty check
uv run pyright
PYTHONPATH=src uv run lint-imports

# Tests
uv run pytest
```

## Notes

- The install is always frozen (`uv sync --frozen`). Never mutates `uv.lock`.
- `ruff check` and `ruff format --check` are read-only — they never auto-fix.
- Both `ty` and `pyright` are configured in `pyproject.toml` and run in CI.
- Import contracts are enforced by import-linter against the hexagonal layer
  contracts defined in `[tool.importlinter]`. Adding a cross-layer import
  without updating the contracts will fail this job.
