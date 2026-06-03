# Ezplog

[![PyPI version](https://img.shields.io/pypi/v/ezplog?style=flat&logo=pypi&logoColor=white)](https://pypi.org/project/ezplog/)
[![Python versions](https://img.shields.io/pypi/pyversions/ezplog?style=flat&logo=python&logoColor=white)](https://pypi.org/project/ezplog/)
[![PyPI status](https://img.shields.io/pypi/status/ezplog?style=flat&logo=pypi&logoColor=white)](https://pypi.org/project/ezplog/)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat&logo=github&logoColor=white)](https://github.com/neuraaak/ezplog/blob/main/LICENSE)
[![CI](https://img.shields.io/github/actions/workflow/status/neuraaak/ezplog/ci.yml?style=flat&label=ci&logo=githubactions&logoColor=white)](https://github.com/neuraaak/ezplog/actions/workflows/ci.yml)
[![Docs](https://img.shields.io/badge/docs-GitHub%20Pages-blue?style=flat&logo=materialformkdocs&logoColor=white)](https://neuraaak.github.io/ezplog/)
[![uv](https://img.shields.io/badge/package%20manager-uv-DE5FE9?style=flat&logo=uv&logoColor=white)](https://github.com/astral-sh/uv)
[![linter](https://img.shields.io/badge/linter-ruff-D7FF64?style=flat&logo=ruff&logoColor=white)](https://github.com/astral-sh/ruff)
[![type checker](https://img.shields.io/badge/type%20checker-ty-261230?style=flat&logo=astral&logoColor=white)](https://github.com/astral-sh/ty)
[![tests](https://img.shields.io/badge/tests-pytest-0A9EDC?style=flat&logo=pytest&logoColor=white)](https://github.com/pytest-dev/pytest)

![Ezplog Logo](https://raw.githubusercontent.com/neuraaak/ezplog/refs/heads/main/docs/assets/logo-min.png)

**ezplog** is a modern Python logging framework combining Rich console rendering and loguru file logging with an explicit app/lib compatibility model.

## 🚀 Quick start

=== "pip"

    ```bash
    pip install ezplog
    ```

=== "uv"

    ```bash
    uv add ezplog
    ```

```python
from ezplog import Ezpl

ezpl = Ezpl(log_file="app.log", hook_logger=True)  # (1)!
ezpl.info("Application started")
ezpl.get_printer().success("Ready")  # (2)!
```

1. Enables stdlib logger interception for consistent app and library pipelines.
2. Uses Rich console rendering while the file logger writes to disk.

## ✨ Key features

- Unified singleton API for console and file logging.
- Rich output patterns, JSON, tables, panels, and progress tools.
- Loguru file sink with rotation, retention, and compression.
- Explicit compatibility hooks between app mode and lib mode.
- Configuration priority: arguments, environment, file, defaults.

## 📚 Documentation

| Section                               | Description                                             |
| :------------------------------------ | :------------------------------------------------------ |
| [Getting Started](getting-started.md) | Tutorial for a working setup in a few minutes.          |
| [User Guides](guides/index.md)        | Task-focused configuration and operational recipes.     |
| [Concepts](concepts/index.md)         | Architecture rationale and mode interactions.           |
| [API Reference](api/index.md)         | Curated API map and auto-generated technical reference. |
| [CLI Reference](cli/index.md)         | Command and option reference for the CLI.               |
| [Examples](examples/index.md)         | Copy-paste runnable scenarios.                          |

## 📋 Requirements

- Python >= 3.11
- `rich >= 13.0.0`
- `loguru >= 0.7.2`
- `click >= 8.0.0`

## ⚖️ License

MIT. See [LICENSE](https://github.com/neuraaak/ezplog/blob/main/LICENSE).
