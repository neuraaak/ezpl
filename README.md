# 🚀 Ezpl

[![Version](https://img.shields.io/badge/Version-1.0.0-blue?style=for-the-badge)](https://github.com/neuraaak/ezpl)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

**Ezpl** is a modern Python logging framework with **Rich** console output and **loguru** file logging, featuring advanced display capabilities, configuration management, and a simple typed API suitable for professional and industrial applications.

## 📦 Installation

```bash
pip install ezpl
```

Or from source:

```bash
git clone https://github.com/neuraaak/ezpl.git
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

- **[📖 Complete API Documentation](docs/api/API_DOCUMENTATION.md)** – Full API reference with examples
- **[📋 API Summary](docs/api/SUMMARY.md)** – Quick API overview
- **[🖥️ CLI Documentation](docs/cli/CLI_DOCUMENTATION.md)** – Command-line interface guide
- **[⚙️ Configuration Guide](docs/cli/CONFIG_GUIDE.md)** – Configuration management

## 🧪 Testing

**Note**: Comprehensive test suite will be implemented in a future update. The library is currently in active development with focus on API stability and feature completeness.

For development testing:

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run tests (when available)
pytest tests/
```

## 🎨 Main Components

- **`Ezpl`**: Singleton main class for centralized logging management
- **`Printer`** (ConsolePrinterWrapper): Rich-based console output with pattern format
- **`FileLogger`**: loguru-based file logging with rotation support
- **`RichWizard`**: Advanced Rich display (panels, tables, JSON, progress bars)
- **`ConfigurationManager`**: Centralized configuration management

## 📦 Dependencies

- **rich>=13.0.0** – Beautiful console output and formatting
- **loguru>=0.7.2** – Modern and powerful file logging
- **click>=8.0.0** – CLI framework

## 🔧 Quick API Reference

```python
from ezpl import Ezpl, Printer
from loguru import Logger

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

- **Repository**: [https://github.com/neuraaak/ezpl](https://github.com/neuraaak/ezpl)
- **Issues**: [GitHub Issues](https://github.com/neuraaak/ezpl/issues)
- **Documentation**: [Complete API Docs](docs/api/API_DOCUMENTATION.md)

---

**Ezpl** – Modern, typed, robust and beautiful logging for Python. 🚀
