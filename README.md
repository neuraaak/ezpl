# 🚀 Ezpl

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/OS-Independent-lightgray.svg?style=for-the-badge)](https://pypi.org/project/ezpl/)
[![Version](https://img.shields.io/badge/Version-1.5.3-orange.svg?style=for-the-badge)](https://github.com/neuraaak/ezplog)
[![PyPI](https://img.shields.io/badge/PyPI-ezplog-green.svg?style=for-the-badge&logo=pypi)](https://pypi.org/project/ezplog/)
[![Docs](https://img.shields.io/badge/Docs-Online-blue.svg?style=for-the-badge&logo=readthedocs)](https://neuraaak.github.io/ezplog/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-success.svg?style=for-the-badge)](https://github.com/neuraaak/ezplog)
[![Tests](https://img.shields.io/badge/Tests-377%2F377%20passing-success.svg?style=for-the-badge)](https://github.com/neuraaak/ezplog)
[![Coverage](https://img.shields.io/badge/Coverage-65%25-yellow.svg?style=for-the-badge)](https://github.com/neuraaak/ezplog)

![Logo](docs/assets/logo-min.png)

**Ezpl** is a modern Python logging framework with **Rich** console output and **loguru** file logging, featuring advanced display capabilities, configuration management, and a simple typed API suitable for professional and industrial applications.

## 📦 Installation

```bash
pip install ezpl
```

Or from source:

```bash
git clone https://github.com/neuraaak/ezplog.git
cd ezpl && pip install .
```

## 🚀 Quick Start

```python
from ezpl import Ezpl

# Initialize
ezpl = Ezpl(log_file="app.log")
printer = ezpl.get_printer()
logger = ezpl.get_logger()

# Console output (Rich formatting)
printer.info("Information message")
printer.success("Operation completed!")
printer.warning("Warning message")

# File logging (loguru)
logger.info("Logged to file")

# Advanced features
printer.wizard.success_panel("Success", "Operation completed")
printer.wizard.table([{"Name": "Alice", "Age": 30}], title="Users")
```

## 🎯 Key Features

- **✅ Singleton Pattern**: One global instance for the whole application
- **✅ Rich Console Output**: Beautiful formatting with colors, panels, tables, and progress bars
- **✅ File Logging**: Structured logs with rotation, retention, and compression
- **✅ RichWizard**: Advanced display capabilities (panels, tables, JSON, dynamic progress bars)
- **✅ Configuration Management**: JSON config, environment variables, and runtime configuration
- **✅ CLI Tools**: Command-line interface for logs, config, and statistics
- **✅ Full Type Hints**: Complete typing support for IDEs and linters
- **✅ Robust Error Handling**: Never crashes, even with problematic input

## 📚 Documentation

Complete documentation is available at **[neuraaak.github.io/ezplog](https://neuraaak.github.io/ezplog/)**

| Section                                                                   | Description                                    |
| ------------------------------------------------------------------------- | ---------------------------------------------- |
| **[Getting Started](https://neuraaak.github.io/ezplog/getting-started/)** | Installation, basic usage, and first steps     |
| **[API Reference](https://neuraaak.github.io/ezplog/api/)**               | Complete API documentation with examples       |
| **[CLI Reference](https://neuraaak.github.io/ezplog/cli/)**               | Command-line interface guide                   |
| **[User Guides](https://neuraaak.github.io/ezplog/guides/)**              | Configuration, development, and testing guides |
| **[Examples](https://neuraaak.github.io/ezplog/examples/)**               | Practical examples and demonstrations          |

## 🧪 Testing

Comprehensive test suite with **377 tests** covering unit, integration, and robustness scenarios — **65% code coverage**.

| Metric      | Value                         |
| ----------- | ----------------------------- |
| Total tests | 377                           |
| Passing     | 377 (100%)                    |
| Coverage    | 65%                           |
| Test types  | Unit, Integration, Robustness |

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run all tests
pytest tests/

# Run specific test types
python tests/run_tests.py --type unit
python tests/run_tests.py --type integration
python tests/run_tests.py --type robustness

# With coverage
python tests/run_tests.py --coverage
```

See **[Testing Guide](https://neuraaak.github.io/ezplog/guides/testing/)** for complete details.

## 🛠️ Development Setup

For contributors and developers:

```bash
# Install in development mode with all dependencies
pip install -e ".[dev]"

# Install pre-commit hooks (code formatting, linting)
pip install pre-commit
pre-commit install

# Install Git hooks (auto-formatting, auto-tagging)
# Linux/macOS:
./.hooks/install.sh

# Windows:
.hooks\install.bat

# Or manually:
git config core.hooksPath .hooks
```

**Git Hooks:**

- **pre-commit**: Automatically formats code (black, isort, ruff) before commit
- **post-commit**: Automatically creates version tags after commit

See **[Development Guide](https://neuraaak.github.io/ezplog/guides/development/)** and **[.hooks/README.md](.hooks/README.md)** for detailed hook documentation.

## 🎨 Main Components

- **`Ezpl`**: Singleton main class for centralized logging management
- **`EzPrinter`** (alias: `Printer`): Rich-based console output with pattern format
- **`EzLogger`** (alias: `Logger`): loguru-based file logging with rotation support
- **`RichWizard`**: Advanced Rich display (panels, tables, JSON, progress bars)
- **`ConfigurationManager`**: Centralized configuration management

## 📦 Dependencies

- **rich>=13.0.0** – Beautiful console output and formatting
- **loguru>=0.7.2** – Modern and powerful file logging
- **click>=8.0.0** – CLI framework

## 🔧 Quick API Reference

```python
from ezpl import Ezpl, Printer, Logger

ezpl = Ezpl()
printer: Printer = ezpl.get_printer()
logger: Logger = ezpl.get_logger()

# Console methods
printer.info(), printer.success(), printer.warning(), printer.error()
printer.tip(), printer.system(), printer.install()  # Pattern methods
printer.wizard.panel(), printer.wizard.table(), printer.wizard.json()

# File logging
logger.info(), logger.debug(), logger.warning(), logger.error()

# Configuration
ezpl.set_level("DEBUG")
ezpl.configure(log_rotation="10 MB", log_retention="7 days")
```

## 🛡️ Robustness

Ezpl is designed to never crash, even with problematic input:

- Automatic string conversion for non-string messages
- Robust error handling in formatters
- Safe handling of special characters and Unicode
- Graceful fallbacks for all error cases

## 📝 License

MIT License – See [LICENSE](LICENSE) file for details.

## 🔗 Links

- **Documentation**: [https://neuraaak.github.io/ezplog/](https://neuraaak.github.io/ezplog/)
- **Repository**: [https://github.com/neuraaak/ezplog](https://github.com/neuraaak/ezplog)
- **PyPI**: [https://pypi.org/project/ezplog/](https://pypi.org/project/ezplog/)
- **Issues**: [GitHub Issues](https://github.com/neuraaak/ezplog/issues)

---

**Ezpl** – Modern, typed, robust and beautiful logging for Python. 🚀
