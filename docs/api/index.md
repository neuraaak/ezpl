# API Reference

Complete API reference for **Ezpl** logging framework.

## Overview

The Ezpl API is organized into several key components, each serving a specific purpose in the logging ecosystem.

## Quick Reference

| Component                                            | Description          | Documentation                       |
| ---------------------------------------------------- | -------------------- | ----------------------------------- |
| [`Ezpl`](reference/ezpl.md)                          | Main singleton class | Core logging management             |
| [`EzPrinter`](reference/printer.md)                  | Console output       | Rich-formatted console logging      |
| [`EzLogger`](reference/logger.md)                    | File logging         | Loguru-based file logging           |
| [`RichWizard`](reference/wizard.md)                  | Advanced display     | Panels, tables, JSON, progress bars |
| [`ConfigurationManager`](reference/configuration.md) | Configuration        | Centralized config management       |
| [Types & Enums](reference/types.md)                  | LogLevel, Pattern    | Type definitions and enums          |
| [Exceptions](reference/exceptions.md)                | Error handling       | Custom exception hierarchy          |

## Main Components

### Core Classes

- **[`Ezpl`](reference/ezpl.md)** - The main singleton class that manages the logging system
- **[`EzPrinter`](reference/printer.md)** (alias: `Printer`) - Console output handler with Rich formatting
- **[`EzLogger`](reference/logger.md)** (alias: `Logger`) - File logging handler with loguru
- **[`RichWizard`](reference/wizard.md)** - Advanced Rich display capabilities

### Configuration & Types

- **[`ConfigurationManager`](reference/configuration.md)** - Manages configuration from multiple sources
- **[`LogLevel`](reference/types.md#loglevel)** - Enum for log levels (DEBUG, INFO, SUCCESS, WARNING, ERROR, CRITICAL)
- **[`Pattern`](reference/types.md#pattern)** - Enum for contextual patterns (SUCCESS, ERROR, WARN, TIP, etc.)

### Error Handling

- **[Exception Hierarchy](reference/exceptions.md)** - Custom exceptions for robust error handling

## Type System

Ezpl provides comprehensive type hints for better IDE support:

```python
from ezplog import Ezpl, Printer, Logger, LogLevel, Pattern
from typing import TYPE_CHECKING

# Full type annotations
ezpl: Ezpl = Ezpl()
printer: Printer = ezpl.get_printer()
logger: Logger = ezpl.get_logger()

# Enum types
level: LogLevel = LogLevel.INFO
pattern: Pattern = Pattern.SUCCESS
```

## API Design Principles

### Singleton Pattern

The `Ezpl` class follows the singleton pattern with thread-safe double-checked locking:

- Only one instance exists across the application
- Configuration set at the root level propagates to all modules
- Thread-safe initialization

### Type Safety

- Full type hints throughout the codebase
- Type aliases for better readability (`Printer`, `Logger`)
- Protocol-based interfaces for extensibility

### Configuration Priority

Configuration follows a clear priority order:

1. **Direct arguments** to `Ezpl()`
2. **Environment variables** (`EZPL_*` prefix)
3. **Configuration file** (`~/.ezpl/config.json`)
4. **Default values**

### Exception Safety

- Never crashes, even with invalid input
- Automatic type conversion and sanitization
- Custom exception hierarchy for precise error handling
- Graceful fallbacks for all error cases

## Quick Start Examples

### Basic Usage

```python
from ezplog import Ezpl

# Initialize
ezpl = Ezpl(log_file="app.log")
printer = ezpl.get_printer()
logger = ezpl.get_logger()

# Console logging
printer.info("Information message")
printer.success("Operation completed!")
printer.warning("Warning message")

# File logging
logger.info("Logged to file")
```

### Advanced Features

```python
from ezplog import Ezpl

ezpl = Ezpl()
printer = ezpl.get_printer()

# Pattern-based logging
printer.tip("Pro tip: Use type hints!")
printer.system("System message")
printer.install("Installing package...")

# RichWizard features
printer.wizard.success_panel("Success", "Operation completed")
printer.wizard.table([{"Name": "Alice", "Age": 30}], title="Users")
printer.wizard.json({"config": "value"})
```

### Configuration

```python
from ezplog import Ezpl

# Direct configuration
ezpl = Ezpl(
    log_file="app.log",
    log_level="DEBUG",
    log_rotation="10 MB",
    log_retention="7 days",
    log_compression="zip"
)

# Runtime reconfiguration
ezpl.configure(
    printer_level="INFO",
    logger_level="DEBUG"
)

# Reload from file and environment
ezpl.reload_config()
```

## Detailed Documentation

Select a component from the navigation menu or the table above to view detailed documentation with:

- Complete method signatures
- Parameter descriptions
- Return types
- Usage examples
- Best practices

## Auto-Generated API Documentation

For auto-generated API documentation from source code docstrings:

| Module                                      | Description               |
| ------------------------------------------- | ------------------------- |
| [Ezpl](reference/ezpl.md)                   | Main singleton class      |
| [EzPrinter](reference/printer.md)           | Console output handler    |
| [EzLogger](reference/logger.md)             | File logging handler      |
| [RichWizard](reference/wizard.md)           | Advanced display features |
| [Configuration](reference/configuration.md) | Configuration management  |
| [Types & Enums](reference/types.md)         | Type definitions          |
| [Exceptions](reference/exceptions.md)       | Exception hierarchy       |

Or browse the [Full Reference Index](reference/index.md).

## Need Help?

- **Quick Start**: See [Getting Started](../getting-started.md)
- **Examples**: Check out [Examples](../examples/index.md)
- **Guides**: Read [User Guides](../guides/index.md)
- **Issues**: Report bugs on [GitHub](https://github.com/neuraaak/ezplog/issues)
