# Welcome to Ezpl Documentation

[![PyPI](https://img.shields.io/badge/PyPI-ezplog-orange.svg)](https://pypi.org/project/ezplog/)
[![PyPI version](https://img.shields.io/pypi/v/ezplog)](https://pypi.org/project/ezplog/)
[![Python versions](https://img.shields.io/pypi/pyversions/ezplog)](https://pypi.org/project/ezplog/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/neuraaak/ezplog/blob/main/LICENSE)

![Ezpl Logo](https://raw.githubusercontent.com/neuraaak/ezplog/refs/heads/main/docs/assets/logo-min.png)

**Ezpl** is a modern Python logging framework with **Rich** console output and **loguru** file logging, featuring advanced display capabilities, configuration management, and a simple typed API suitable for professional and industrial applications.

## ✨ Key Features

- **✅ Singleton Pattern**: One global instance for the whole application
- **✅ Rich Console Output**: Beautiful formatting with colors, panels, tables, and progress bars
- **✅ File Logging**: Structured logs with rotation, retention, and compression
- **✅ RichWizard**: Advanced display capabilities (panels, tables, JSON, dynamic progress bars)
- **✅ Configuration Management**: JSON config, environment variables, and runtime configuration
- **✅ CLI Tools**: Command-line interface for logs, config, and statistics
- **✅ Full Type Hints**: Complete typing support for IDEs and linters
- **✅ Robust Error Handling**: Never crashes, even with problematic input

## 🚀 Quick Start

### Installation

```bash
pip install ezplog
```

Or from source:

```bash
git clone https://github.com/neuraaak/ezplog.git
cd ezplog && pip install .
```

### Basic Usage

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

## 📚 Documentation Structure

| Section                               | Description                                |
| ------------------------------------- | ------------------------------------------ |
| [Getting Started](getting-started.md) | Installation, basic usage, and first steps |
| [API Reference](api/index.md)         | Complete API documentation with examples   |
| [CLI Reference](cli/index.md)         | Command-line interface documentation       |
| [User Guides](guides/index.md)        | In-depth guides and tutorials              |
| [Examples](examples/index.md)         | Practical examples and use cases           |

## 🎯 Main Components

- **`Ezpl`**: Singleton main class for centralized logging management
- **`EzPrinter`** (alias: `Printer`): Rich-based console output with pattern format
- **`EzLogger`** (alias: `Logger`): loguru-based file logging with rotation support
- **`RichWizard`**: Advanced Rich display (panels, tables, JSON, progress bars)
- **`ConfigurationManager`**: Centralized configuration management

## 📦 Core Dependencies

- **rich>=13.0.0** – Beautiful console output and formatting
- **loguru>=0.7.2** – Modern and powerful file logging
- **click>=8.0.0** – CLI framework

## 🧪 Testing

Comprehensive test suite with **377 tests** covering unit, integration, and robustness scenarios — **65% code coverage**.

| Metric      | Value                         |
| ----------- | ----------------------------- |
| Total tests | 377                           |
| Passing     | 377 (100%)                    |
| Coverage    | 65%                           |
| Test types  | Unit, Integration, Robustness |

## 🛡️ Robustness

Ezpl is designed to never crash, even with problematic input:

- Automatic string conversion for non-string messages
- Robust error handling in formatters
- Safe handling of special characters and Unicode
- Graceful fallbacks for all error cases

## 📝 License

MIT License – See [LICENSE](https://github.com/neuraaak/ezplog/blob/main/LICENSE) file for details.

## 🔗 Links

- **Repository**: [https://github.com/neuraaak/ezplog](https://github.com/neuraaak/ezplog)
- **PyPI**: [https://pypi.org/project/ezplog/](https://pypi.org/project/ezplog/)
- **Issues**: [https://github.com/neuraaak/ezplog/issues](https://github.com/neuraaak/ezplog/issues)

---

**Ezpl** – Modern, typed, robust and beautiful logging for Python. 🚀
