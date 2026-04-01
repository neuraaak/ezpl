# How to contribute changes locally

Set up a local development workflow for implementing and validating changes in ezplog.

## 🔧 Prerequisites

- Python 3.11+
- Git
- A local clone of the repository

## 📝 Steps

1. Create and activate a virtual environment, then install development dependencies.

```bash
python -m venv .venv
. .venv/Scripts/activate
pip install -e ".[dev,docs,test]"
```

1. Apply formatting and linting checks.

```bash
ruff format src tests
ruff check src tests
```

1. Run type checking.

```bash
ty check
```

1. Run the test suite.

```bash
pytest
```

1. Build the documentation in strict mode.

```bash
mkdocs build --strict
```

## ✅ Result

Your local environment is ready for safe contributions with formatting, typing, tests, and docs checks.
