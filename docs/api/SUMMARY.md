# API Summary

**Ezpl** - Modern Python logging framework with Rich console output and loguru file logging.

## 📖 Complete Documentation

For detailed API documentation, see **[API_DOCUMENTATION.md](API_DOCUMENTATION.md)**.

---

## Quick Overview

### Main Components

- **`Ezpl`**: Singleton for centralized logging management
- **`ConsolePrinterWrapper` (Printer)**: Rich-based console output with pattern format
- **`FileLogger`**: loguru-based file logging with rotation support
- **`RichWizard`**: Advanced Rich display capabilities (panels, tables, JSON, progress bars, dynamic layered progress)
- **`LogLevel`**: Custom log levels (DEBUG, INFO, SUCCESS, WARNING, ERROR, CRITICAL)
- **`Pattern`**: Contextual patterns (SUCCESS, ERROR, WARN, TIP, SYSTEM, INSTALL, etc.)
- **`ConfigurationManager`**: Centralized configuration management
- **Custom Exceptions**: `ValidationError`, `FileOperationError`, `LoggingError`, etc.

### Quick Start

```python
from ezpl import Ezpl, Printer
from loguru import Logger

# Initialize
ezpl = Ezpl()

# Get typed instances
printer: Printer = ezpl.get_printer()
logger: Logger = ezpl.get_logger()

# Console (pattern format: • PATTERN :: message)
printer.info("Information")
printer.success("Done!")
printer.tip("Pro tip")
printer.print_json({"key": "value"})

# RichWizard (advanced display)
printer.wizard.success_panel("Success", "Operation completed")
printer.wizard.table([{"Name": "Alice", "Age": 30}], title="Users")
printer.wizard.json({"config": "value"}, title="Config")

# File (structured format: timestamp | level | module:function:line - message)
logger.info("Logged to file")
```

### Key Features

**ConsolePrinter:**

- Pattern-based format: `• PATTERN :: message`
- Pattern methods: `tip()`, `system()`, `install()`, `detect()`, `config()`, `deps()`
- Indentation management with context managers

**RichWizard (via `printer.wizard`):**

- **Panels**: Info, success, error, warning, installation panels with icons
- **Tables**: Generic, status, dependency, command tables
- **JSON**: Syntax-highlighted JSON display with optional panel wrapping
- **Progress Bars**: Generic, spinner, download, installation, layered progress bars
- **Dynamic Layered Progress**: Multi-level progress bars with automatic layer management

**FileLogger:**

- Structured log format with timestamps
- File rotation, retention, and compression
- Session separators
- Robust error handling

**Configuration:**

- JSON file configuration (`~/.ezpl/config.json`)
- Environment variables support (`EZPL_*`)
- Runtime configuration via `configure()`
- Priority order: arg > env > config file > default
- Singleton propagation: configuration set at root propagates to all libraries

**Type Safety:**

- Type aliases: `Printer` (alias for `ConsolePrinterWrapper`)
- Full type hints for IDE autocompletion
- Explicit return types for all methods

### Main Methods

**Ezpl:**

- `Ezpl(log_file, log_level, printer_level, file_logger_level, log_rotation, log_retention, log_compression, indent_step, indent_symbol, base_indent_symbol) -> Ezpl`
  - Priority: arg > env > config file > default
- `get_printer() -> ConsolePrinterWrapper`
- `get_logger() -> Logger`
- `set_level(level: str) -> None`
- `configure(**kwargs) -> None`
- `reload_config() -> None` - Reload from file/env vars
- `manage_indent() -> Generator` (context manager)

**Printer (ConsolePrinterWrapper):**

- Standard: `info()`, `debug()`, `success()`, `warning()`, `error()`, `critical()`
- Patterns: `tip()`, `system()`, `install()`, `detect()`, `config()`, `deps()`
- Rich: `print_table()`, `print_panel()`, `print_json()` (delegates to `wizard`)
- Wizard: `printer.wizard` - Access to all RichWizard features

**FileLogger:**

- `get_logger() -> Logger`
- `set_level(level: str) -> None`
- `add_separator() -> None`
- `get_file_size() -> int`

### Exceptions

- `EzplError`: Base exception
- `ValidationError`: Input validation errors
- `FileOperationError`: File operation errors
- `LoggingError`: Logging operation errors
- `ConfigurationError`: Configuration errors
- `InitializationError`: Initialization errors
- `HandlerError`: Handler-related errors

---

**For complete API documentation with examples, see [API_DOCUMENTATION.md](API_DOCUMENTATION.md).**
