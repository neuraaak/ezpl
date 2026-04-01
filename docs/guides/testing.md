# How to run and extend tests

Run existing tests and add focused coverage for new behavior.

## 🔧 Prerequisites

- Development dependencies installed
- A clean working tree or isolated branch for test changes

## 📝 Steps

1. Run the full test suite.

```bash
pytest
```

1. Run a focused subset while iterating.

```bash
pytest tests/unit/test_ezpl.py
pytest tests/unit/test_printer.py
pytest tests/unit/test_logger.py
```

1. Run marker-based subsets when needed.

```bash
pytest -m "not slow"
pytest -m "cli"
```

1. Generate coverage output.

```bash
pytest --cov=src/ --cov-report=term --cov-report=html
```

1. Add tests for your change close to the impacted module.

```python
from ezplog import Ezpl


def test_should_apply_named_logger_hooks_when_configured() -> None:
    ezpl = Ezpl(hook_logger=False, hook_printer=False)
    ezpl.set_compatibility_hooks(hook_logger=True, logger_names=["vendor.api"])

    assert Ezpl._instance is ezpl
```

## ✅ Result

You can validate regressions quickly and expand test coverage with reproducible commands.
