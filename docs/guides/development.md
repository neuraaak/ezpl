# How to contribute changes locally

Set up a local development workflow for implementing and validating changes in ezplog.

## 🔧 Prerequisites

- Python 3.11+
- Git
- A local clone of the repository

## 📝 Steps

### 1. Create your environment and install dependencies

=== "uv workflow"

    ```bash
    uv sync --extra dev --extra docs --extra test
    ```

=== "pip editable install"

    ```bash
    python -m venv .venv
    . .venv/Scripts/activate
    pip install -e ".[dev,docs,test]"
    ```

### 2. Apply formatting and linting checks

```bash
ruff format src tests
ruff check src tests
```

### 3. Run type checking

```bash
ty check
```

### 4. Run the test suite

```bash
pytest
```

### 5. Build the documentation in strict mode

```bash
mkdocs build --strict
```

## ✅ Quality gate checklist

- [ ] `ruff format src tests` and `ruff check src tests` complete without errors.
- [ ] `ty check` completes with expected diagnostics only.
- [ ] `pytest` passes for impacted modules.
- [ ] `mkdocs build --strict` succeeds with no warnings.
- [ ] Any changed docs remain ==copy-paste runnable==.

## ✅ Result

Your local environment is ready for safe contributions with formatting, typing, tests, and docs checks.
