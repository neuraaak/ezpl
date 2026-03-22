# Ezplog

[![PyPI version](https://img.shields.io/pypi/v/ezplog?style=flat&logo=pypi&logoColor=white)](https://pypi.org/project/ezplog/)
[![Python versions](https://img.shields.io/pypi/pyversions/ezplog?style=flat&logo=python&logoColor=white)](https://pypi.org/project/ezplog/)
[![PyPI status](https://img.shields.io/pypi/status/ezplog?style=flat&logo=pypi&logoColor=white)](https://pypi.org/project/ezplog/)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat&logo=github&logoColor=white)](https://github.com/neuraaak/ezplog/blob/main/LICENSE)
[![CI](https://img.shields.io/github/actions/workflow/status/neuraaak/ezplog/publish-pypi.yml?style=flat&label=publish&logo=githubactions&logoColor=white)](https://github.com/neuraaak/ezplog/actions/workflows/publish-pypi.yml)
[![Docs](https://img.shields.io/badge/docs-Github%20Pages-blue?style=flat&logo=materialformkdocs&logoColor=white)](https://neuraaak.github.io/ezplog/)
[![uv](https://img.shields.io/badge/package%20manager-uv-DE5FE9?style=flat&logo=uv&logoColor=white)](https://github.com/astral-sh/uv)
[![linter](https://img.shields.io/badge/linter-ruff-orange?style=flat&logo=ruff&logoColor=white)](https://github.com/astral-sh/ruff)
[![type checker](https://img.shields.io/badge/type%20checker-ty-orange?style=flat&logo=astral&logoColor=white)](https://github.com/astral-sh/ty)

![Ezpl Logo](https://raw.githubusercontent.com/neuraaak/ezplog/refs/heads/main/docs/assets/logo-min.png)

**ezplog** is a modern Python logging framework combining **Rich** console output with **loguru** file logging. It provides a single, thread-safe entry point for both console and file logging, with advanced display features and a simple typed API.

```bash
pip install ezplog
```

```python
from ezplog import Ezpl

ezpl = Ezpl(log_file="app.log")
ezpl.info("Application started")
ezpl.get_printer().success("Ready")
ezpl.get_logger().info("Saved to file")
```

## Key Features

- **Singleton pattern**: one `Ezpl` instance manages both console and file output across your entire app
- **Rich console output**: color-coded messages, panels, tables, JSON, and progress bars via `EzPrinter`
- **loguru file logging**: structured logs with rotation, retention, and compression via `EzLogger`
- **Dual-mode support**: app mode for applications, lib mode for library authors (silent by default)
- **Configuration cascade**: constructor arguments > environment variables > config file > defaults
- **Config lock**: prevent libraries from reconfiguring your logging after startup
- **Full type hints**: PEP 561 compliant (`py.typed` marker included)
- **Robust by design**: never raises on logging failures, safe fallbacks for all edge cases

## Documentation

| Section                                   | Description                                               |
| ----------------------------------------- | --------------------------------------------------------- |
| [Getting Started](getting-started.md)     | Install, first steps, and quickstart in under 5 minutes   |
| [API Reference](api/index.md)             | Complete class and method reference generated from source |
| [CLI Reference](cli/index.md)             | Command-line interface for logs and configuration         |
| [User Guides](guides/index.md)            | Task-oriented guides for common scenarios                 |
| [Explanations](explanations/dual-mode.md) | Concepts: app mode vs lib mode                            |

## Main Components

| Class                  | Alias     | Purpose                                               |
| ---------------------- | --------- | ----------------------------------------------------- |
| `Ezpl`                 | —         | Singleton facade — the single entry point             |
| `EzPrinter`            | `Printer` | Rich console output with pattern formatting           |
| `EzLogger`             | `Logger`  | loguru file logging with rotation support             |
| `RichWizard`           | —         | Advanced Rich display: panels, tables, JSON, progress |
| `ConfigurationManager` | —         | Configuration from args, env vars, file, or defaults  |

## Requirements

- Python >= 3.11
- `rich >= 13.0.0`
- `loguru >= 0.7.2`
- `click >= 8.0.0`

## License

MIT — see [LICENSE](https://github.com/neuraaak/ezplog/blob/main/LICENSE)
