# Complete API Documentation – Ezpl

## Overview

This documentation presents all the components available in the **Ezpl** library, organized by functional modules. Each component is designed to offer specialized functionality while ensuring API and design consistency.

## Table of Contents

- [Complete API Documentation – Ezpl](#complete-api-documentation--ezpl)
  - [Overview](#overview)
  - [Table of Contents](#table-of-contents)
  - [🧠 Main Module (`ezpl`)](#-main-module-ezpl)
    - [Singleton Ezpl](#singleton-ezpl)
      - [Initialization](#initialization)
      - [Getters](#getters)
      - [Level Management](#level-management)
      - [File Operations](#file-operations)
      - [Indentation](#indentation)
      - [Configuration](#configuration)
      - [Utilities](#utilities)
    - [ConsolePrinterWrapper (Printer)](#consoleprinterwrapper-printer)
    - [ConsolePrinter](#consoleprinter)
    - [FileLogger](#filelogger)
    - [RichWizard](#richwizard)
      - [Panels](#panels)
      - [Tables](#tables)
      - [JSON](#json)
      - [Progress Bars](#progress-bars)
      - [Dynamic Layered Progress](#dynamic-layered-progress)
    - [LogLevel](#loglevel)
    - [Pattern](#pattern)
    - [ConfigurationManager](#configurationmanager)
    - [Exceptions](#exceptions)
  - [🧪 Usage Examples](#-usage-examples)
    - [Basic Usage](#basic-usage)
    - [Advanced Console Features](#advanced-console-features)
    - [RichWizard Usage](#richwizard-usage)
    - [File Logger with Rotation](#file-logger-with-rotation)
    - [Configuration Management](#configuration-management)
    - [Handling Special Characters](#handling-special-characters)
    - [Type Hints for Better IDE Support](#type-hints-for-better-ide-support)
  - [🎯 Best Practices](#-best-practices)
    - [Type Safety](#type-safety)
    - [Logging Levels](#logging-levels)
    - [Console Output](#console-output)
    - [File Logging](#file-logging)
    - [Error Handling](#error-handling)
    - [Configuration](#configuration-1)
    - [Testing](#testing)
    - [Performance](#performance)
  - [📝 Type Reference](#-type-reference)
    - [Type Aliases](#type-aliases)
    - [Return Types](#return-types)

---

## 🧠 Main Module (`ezpl`)

### Singleton Ezpl

**File:** `ezpl/ezpl.py`

The main entry point of the library. Provides a singleton for centralized logging management (console and file).

**Type Hints:**

```python
from ezpl import Ezpl, Printer
from loguru import Logger

ezpl = Ezpl()
printer: Printer = ezpl.get_printer()  # Type: ConsolePrinterWrapper
logger: Logger = ezpl.get_logger()     # Type: loguru.Logger
```

**Main methods:**

#### Initialization

- `Ezpl(
    log_file: Path | str = None,
    log_level: str = None,
    printer_level: str = None,
    file_logger_level: str = None,
    log_rotation: str = None,
    log_retention: str = None,
    log_compression: str = None,
    indent_step: int = None,
    indent_symbol: str = None,
    base_indent_symbol: str = None,
) -> Ezpl`: Creates or retrieves the singleton instance

**Configuration Priority Order (for each parameter):**

1. **Arguments passed directly** (highest priority)
2. **Environment variables** (`EZPL_*`)
3. **Configuration file** (`~/.ezpl/config.json`)
4. **Default values** (lowest priority)

**Parameters:**

- `log_file`: Path to the log file
- `log_level`: Global log level (applies to both printer and logger)
- `printer_level`: Printer log level only
- `file_logger_level`: File logger level only
- `log_rotation`: Rotation setting (e.g., "10 MB", "1 day", "12:00")
- `log_retention`: Retention period (e.g., "7 days", "10 files")
- `log_compression`: Compression format (e.g., "zip", "gz")
- `indent_step`: Indentation step size
- `indent_symbol`: Symbol for indentation
- `base_indent_symbol`: Base indentation symbol

**Singleton Behavior:**

- Only one instance exists across all modules
- Configuration set at root level propagates to all libraries using Ezpl
- First initialization determines the base configuration
- Use `configure()` or `reload_config()` to update after initialization

#### Getters

- `get_printer() -> ConsolePrinterWrapper`: Returns the console printer wrapper instance
- `get_logger() -> Logger`: Returns the loguru Logger instance for file logging
- `get_config() -> ConfigurationManager`: Get the current configuration manager

#### Level Management

- `set_level(level: str) -> None`: Sets the log level for both printer and logger
- `set_printer_level(level: str) -> None`: Sets the printer level only
- `set_logger_level(level: str) -> None`: Sets the logger level only

#### File Operations

- `set_log_file(log_file: Path | str) -> None`: Change the log file path
- `add_separator() -> None`: Adds a separator in the log file

#### Indentation

- `manage_indent() -> Generator[None, None, None]`: Context manager for console indentation

#### Configuration

- `configure(config_dict: Dict[str, Any] = None, **kwargs) -> None`: Configure Ezpl dynamically
  - Supports: `log_file`, `printer_level`, `logger_level`, `level`, `log_rotation`, `log_retention`, `log_compression`, `indent_step`, `indent_symbol`, `base_indent_symbol`
  - Changes are persisted to the configuration file
  - Handlers are reinitialized with new settings
- `reload_config() -> None`: Reload configuration from file and environment variables
  - Useful when environment variables or config file have changed after initialization
  - Reinitializes handlers with reloaded configuration

#### Utilities

- `reset() -> None`: Reset singleton (for testing)

---

### ConsolePrinterWrapper (Printer)

**File:** `ezpl/handlers/console.py`

Wrapper class that provides the main API for console logging. Returned by `Ezpl.get_printer()`.

**Type Alias:**

```python
from ezpl import Printer  # Alias for ConsolePrinterWrapper
```

**Pattern Format:**
All messages use the pattern format: `• PATTERN :: message`

**Standard Logging Methods:**

- `info(message: Any) -> None`: Log an info message
- `debug(message: Any) -> None`: Log a debug message
- `success(message: Any) -> None`: Log a success message
- `warning(message: Any) -> None`: Log a warning message
- `warn(message: Any) -> None`: Alias for `warning()`
- `error(message: Any) -> None`: Log an error message
- `critical(message: Any) -> None`: Log a critical message

**Additional Pattern Methods:**

- `tip(message: Any) -> None`: Display a tip message (Pattern.TIP)
- `system(message: Any) -> None`: Display a system message (Pattern.SYSTEM)
- `install(message: Any) -> None`: Display an installation message (Pattern.INSTALL)
- `detect(message: Any) -> None`: Display a detection message (Pattern.DETECT)
- `config(message: Any) -> None`: Display a configuration message (Pattern.CONFIG)
- `deps(message: Any) -> None`: Display a dependencies message (Pattern.DEPS)

**Generic Pattern Method:**

- `print_pattern(pattern: str | Pattern, message: Any, level: str = "INFO") -> None`: Display a message with a custom pattern

**Rich Features:**

- `print_table(data: List[Dict[str, Any]], title: Optional[str] = None) -> None`: Display a table using Rich
- `print_panel(content: str, title: Optional[str] = None, style: str = "blue") -> None`: Display a panel using Rich
- `print_json(data: str | Dict | List, title: Optional[str] = None, indent: Optional[int] = None, highlight: bool = True) -> None`: Display JSON data with syntax highlighting

**Example:**

```python
from ezpl import Ezpl, Printer

ezpl = Ezpl()
printer: Printer = ezpl.get_printer()

# Standard methods
printer.info("Information message")
printer.success("Operation completed!")
printer.warning("This is a warning")
printer.error("An error occurred")

# Pattern methods
printer.tip("Pro tip: Use context managers")
printer.system("System check completed")
printer.install("Installing package...")
printer.detect("Detected configuration")
printer.config("Configuration loaded")
printer.deps("Checking dependencies...")

# Rich features
printer.print_table([
    {"Name": "Alice", "Age": 30},
    {"Name": "Bob", "Age": 25}
])

printer.print_json({"key": "value", "nested": {"a": 1}}, title="Config")
```

---

### ConsolePrinter

**File:** `ezpl/handlers/console.py`

Internal console printer handler. Use `ConsolePrinterWrapper` (via `Ezpl.get_printer()`) for most use cases.

**Key Features:**

- Uses Rich for console output
- Pattern-based formatting: `• PATTERN :: message`
- Automatic handling of special characters
- Robust error handling (never crashes)
- Unicode support
- Maximum indentation limit (10 levels)
- Context manager support

**Indentation Management:**

- `get_indent() -> str`: Get the current indentation string
- `add_indent() -> None`: Increase indentation level
- `del_indent() -> None`: Decrease indentation level
- `reset_indent() -> None`: Reset indentation to zero
- `manage_indent() -> Generator[None, None, None]`: Context manager for temporary indentation

---

### FileLogger

**File:** `ezpl/handlers/file.py`

Robust file logger using **loguru**, with advanced formatting, separator management, file rotation, and error tolerance.

**Initialization:**

```python
from ezpl.handlers import FileLogger

logger_handler = FileLogger(
    log_file: Path | str,
    level: str = "INFO",
    rotation: Optional[str] = None,      # e.g., "10 MB", "1 day"
    retention: Optional[str] = None,       # e.g., "7 days", "1 month"
    compression: Optional[str] = None     # e.g., "zip", "gz", "tar.gz"
)
```

**Main methods:**

- `set_level(level: str) -> None`: Changes the file log level
- `get_logger() -> Logger`: Returns the configured loguru Logger instance
- `add_separator() -> None`: Adds a separator in the log file
- `get_log_file() -> Path`: Get the current log file path
- `get_file_size() -> int`: Get current log file size in bytes

**Log Format:**

```
YYYY-MM-DD HH:MM:SS | LEVEL      | module:function:line - message
```

**Key Features:**

- Uses loguru for file logging
- File rotation, retention, and compression support
- Structured log format with timestamp, level, location, and message
- Session separators
- Robust error handling
- Path validation and automatic directory creation
- Safe message sanitization for file output

**Example:**

```python
from ezpl.handlers import FileLogger

# File logger with rotation
logger_handler = FileLogger(
    "app.log",
    level="INFO",
    rotation="10 MB",      # Rotate at 10 MB
    retention="7 days",    # Keep logs for 7 days
    compression="zip"      # Compress old logs
)

logger = logger_handler.get_logger()
logger.info("This will be rotated when file reaches 10 MB")
```

---

### RichWizard

**File:** `ezpl/handlers/wizard/`

Advanced Rich-based display capabilities for panels, tables, JSON, progress bars, and dynamic layered progress bars. Accessible via `printer.wizard`.

**Access:**

```python
from ezpl import Ezpl

ezpl = Ezpl()
printer = ezpl.get_printer()
wizard = printer.wizard  # RichWizard instance
```

**Key Features:**

- **Panels**: Info, success, error, warning, installation panels
- **Tables**: Generic tables, status tables, dependency tables, command tables
- **JSON**: Syntax-highlighted JSON display with optional panel wrapping
- **Progress Bars**: Generic progress, spinners, download progress, installation progress, layered progress
- **Dynamic Layered Progress**: Multi-level progress bars with layers that appear, progress, and disappear automatically

---

#### Panels

Display Rich panels with various styles and icons.

**Methods:**

- `panel(content, title=None, border_style="blue", width=None, **kwargs) -> None`
  - Generic panel with custom content

- `info_panel(title, content, style="cyan", border_style="cyan", width=None, **kwargs) -> None`
  - Info panel with ℹ️ icon

- `success_panel(title, content, border_style="green", width=None, **kwargs) -> None`
  - Success panel with ✅ icon

- `error_panel(title, content, border_style="red", width=None, **kwargs) -> None`
  - Error panel with ❌ icon

- `warning_panel(title, content, border_style="yellow", width=None, **kwargs) -> None`
  - Warning panel with ⚠️ icon

- `installation_panel(step, description, status="pending", border_style="blue", width=None, **kwargs) -> None`
  - Installation step panel with dynamic status icons (⏳ pending, ✅ success, ❌ error, ⚠️ warning)

**Example:**

```python
printer.wizard.success_panel("Installation", "Package installed successfully")
printer.wizard.error_panel("Error", "Failed to connect to server")
printer.wizard.installation_panel("Step 1", "Installing dependencies", status="success")
```

---

#### Tables

Display Rich tables from various data structures.

**Methods:**

- `table(data, title=None, show_header=True, **kwargs) -> None`
  - Display table from list of dictionaries

- `table_from_columns(title, columns, rows, show_header=True, **kwargs) -> None`
  - Display table with explicit columns and rows

- `status_table(title, data, status_column="Status", **kwargs) -> None`
  - Status table with colored status indicators (✅ success, ❌ error, ⚠️ warning, ℹ️ info)

- `dependency_table(dependencies) -> None`
  - Dependency table showing tool names, versions, and availability status

- `command_table(commands) -> None`
  - Command table with command, description, and category columns

**Example:**

```python
# Generic table
data = [{"Name": "Alice", "Age": 30}, {"Name": "Bob", "Age": 25}]
printer.wizard.table(data, title="Users")

# Status table
status_data = [
    {"Service": "API", "Status": "success"},
    {"Service": "DB", "Status": "error"},
]
printer.wizard.status_table("Services", status_data)

# Dependency table
deps = {"requests": "2.31.0", "click": "8.1.0", "missing": ""}
printer.wizard.dependency_table(deps)
```

---

#### JSON

Display JSON data with syntax highlighting.

**Methods:**

- `json(data, title=None, indent=None, highlight=True) -> None`
  - Display JSON data (dict, list, or JSON string) with optional title panel

**Example:**

```python
printer.wizard.json({"name": "Alice", "age": 30})
printer.wizard.json('{"key": "value"}', title="Config")
printer.wizard.json([1, 2, 3], indent=4)
```

---

#### Progress Bars

Context managers for various types of progress bars.

**Methods:**

- `progress(description="Working...", total=None, transient=False) -> Generator[Tuple[Progress, int], None, None]`
  - Generic progress bar

- `spinner(description="Working...") -> Generator[Tuple[Progress, int], None, None]`
  - Simple spinner

- `spinner_with_status(description="Working...") -> Generator[Tuple[Progress, int], None, None]`
  - Spinner with status messages

- `download_progress(description="Downloading...") -> Generator[Tuple[Progress, int], None, None]`
  - Download progress with speed and size

- `file_download_progress(filename, total_size, description="Downloading file...") -> Generator[Tuple[Progress, int], None, None]`
  - File download progress

- `dependency_progress(dependencies, description="Installing dependencies...") -> Generator[Tuple[Progress, int, str], None, None]`
  - Dependency installation progress

- `package_install_progress(packages, description="Installing packages...") -> Generator[Tuple[Progress, int, str, str], None, None]`
  - Package installation with version info

- `step_progress(steps, description="Processing...", show_step_numbers=True, show_time=True) -> Generator[Tuple[Progress, int, List[str]], None, None]`
  - Step-based progress bar

- `file_copy_progress(files, description="Copying files...") -> Generator[Tuple[Progress, int, List[str]], None, None]`
  - File copying progress

- `installation_progress(steps, description="Installation in progress...") -> Generator[Tuple[Progress, int, str, str], None, None]`
  - Installation process with step details

- `build_progress(phases, description="Building project...") -> Generator[Tuple[Progress, int, str, int], None, None]`
  - Build process with weighted phases

- `deployment_progress(stages, description="Deploying...") -> Generator[Tuple[Progress, int, str], None, None]`
  - Deployment process progress

- `layered_progress(layers, show_time=True) -> Generator[Tuple[Progress, Dict[str, int]], None, None]`
  - Multi-level progress bar with dynamic layers

**Example:**

```python
# Generic progress
with printer.wizard.progress("Processing...", total=100) as (progress, task):
    for i in range(100):
        progress.update(task, advance=1)

# Spinner
with printer.wizard.spinner("Loading...") as (progress, task):
    # Do work
    pass

# Download progress
with printer.wizard.file_download_progress("file.zip", 1024000) as (progress, task):
    progress.update(task, advance=512000)

# Dependency installation
deps = ["requests", "click", "rich"]
with printer.wizard.dependency_progress(deps) as (progress, task, dep):
    # Install dependency
    progress.advance(task)
```

---

#### Dynamic Layered Progress

Advanced multi-level progress bars where layers can appear, progress, and disappear automatically.

**Methods:**

- `dynamic_layered_progress(stages, show_time=True) -> Generator[DynamicLayeredProgress, None, None]`
  - Create a dynamic layered progress bar context manager

**Layer Types:**

- `"progress"`: Classic progress bar with total
- `"steps"`: Progress by steps (list of step names)
- `"spinner"`: Indeterminate spinner
- `"download"`: Download progress with speed/size
- `"main"`: Main layer (stays visible, auto-updates from sub-layers)

**DynamicLayeredProgress Methods:**

- `update_layer(layer_name, progress, details="") -> None`: Update a layer's progress
- `complete_layer(layer_name) -> None`: Mark a layer as completed (with animation)
- `handle_error(layer_name, error) -> None`: Handle errors in a layer
- `emergency_stop(message="Critical error occurred") -> None`: Emergency stop all layers

**Example:**

```python
stages = [
    {"name": "main", "type": "main", "description": "Overall Progress"},
    {"name": "step1", "type": "progress", "description": "Step 1", "total": 100},
    {"name": "step2", "type": "steps", "description": "Step 2", "steps": ["A", "B", "C"]},
    {"name": "download", "type": "download", "description": "Downloading", "total_size": 1024000, "filename": "file.zip"},
]

with printer.wizard.dynamic_layered_progress(stages) as progress:
    # Update step1
    progress.update_layer("step1", 50, "Processing...")
    progress.complete_layer("step1")  # Layer disappears with animation
    
    # Update step2
    progress.update_layer("step2", 1, "Step B")
    progress.complete_layer("step2")  # Layer disappears
    
    # Update download
    progress.update_layer("download", 512000, "Downloading...")
    progress.complete_layer("download")
    
    # Main layer auto-updates as sub-layers complete
```

**Hierarchy:**

When a layer has `type="main"`, the system automatically:
- Creates the main layer first
- Creates sub-layers with indentation (`├─`)
- Auto-configures main layer steps from sub-layers if not provided
- Updates main layer progress as sub-layers complete
- Keeps main layer visible while sub-layers disappear after completion

**Error Handling:**

```python
with printer.wizard.dynamic_layered_progress(stages) as progress:
    try:
        # Do work
        progress.update_layer("step1", 50)
    except Exception as e:
        progress.handle_error("step1", str(e))
        # Or emergency stop
        progress.emergency_stop("Critical failure")
```

---

### LogLevel

**File:** `ezpl/types/log_level.py`

Enumeration of custom log levels with associated colors, styles, and mappings for both Rich and loguru.

**Main members:**

- `DEBUG`, `INFO`, `SUCCESS`, `WARNING`, `ERROR`, `CRITICAL`

**Attributes:**

- `label: str`: Human-readable name
- `no: int`: Numeric level for comparison
- `fg: str`: Foreground color code
- `bg: str`: Background color code

**Class Methods:**

- `get_attribute(level: str, attribute: str) -> Any`: Get a specific attribute
- `get_label(level: str) -> str`: Get the label for a level
- `get_no(level: str) -> int`: Get the numeric level
- `get_fgcolor(level: str) -> str`: Get foreground color
- `get_bgcolor(level: str) -> str`: Get background color
- `is_valid_level(level: str) -> bool`: Check if a level is valid
- `get_all_levels() -> list[str]`: Get all available levels

**Instance Methods:**

- `get_rich_style() -> str`: Returns Rich style string

**Rich Styles:**

- `DEBUG`: "cyan"
- `INFO`: "blue"
- `SUCCESS`: "bold green"
- `WARNING`: "bold yellow"
- `ERROR`: "bold red"
- `CRITICAL`: "bold magenta on red"

---

### Pattern

**File:** `ezpl/types/patterns.py`

Enumeration of contextual patterns for enhanced console output. Patterns provide semantic meaning beyond log levels.

**Main Patterns:**

- `SUCCESS`: Success operations (bright_green)
- `ERROR`: Error conditions (bright_red)
- `WARN`: Warnings (bright_yellow)
- `TIP`: Tips and hints (bright_magenta)
- `DEBUG`: Debug information (dim white)
- `INFO`: General information (bright_blue)

**System Patterns:**

- `SYSTEM`: System operations (bright_blue)
- `INSTALL`: Installation messages (bright_green)
- `DETECT`: Detection/analysis (bright_blue)
- `CONFIG`: Configuration (bright_green)
- `DEPS`: Dependencies (bright_cyan)

**Functions:**

- `get_pattern_color(pattern: Pattern) -> str`: Get Rich color for a pattern
- `get_pattern_color_by_name(pattern_name: str) -> str`: Get color by pattern name

**Pattern Colors Dictionary:**

- `PATTERN_COLORS: Dict[Pattern, str]`: Mapping of patterns to Rich color names

---

### ConfigurationManager

**File:** `ezpl/config/manager.py`

Centralized configuration manager for Ezpl. Handles loading, saving, and merging configuration from multiple sources.

**Priority Order (when accessed via ConfigurationManager):**

1. Environment variables (`EZPL_*`) - highest priority
2. Configuration file (`~/.ezpl/config.json`)
3. Default values - lowest priority

**Note:** When using `Ezpl()` constructor, arguments passed directly have the highest priority, followed by environment variables, then config file, then defaults.

**Main Methods:**

- `get(key: str, default: Any = None) -> Any`: Get a configuration value
- `set(key: str, value: Any) -> None`: Set a configuration value
- `update(config_dict: Dict[str, Any]) -> None`: Update multiple values
- `save() -> None`: Save configuration to file
- `reset_to_defaults() -> None`: Reset to default values
- `get_all() -> Dict[str, Any]`: Get all configuration values
- `export_to_script(output_file: Path | str, platform: str = None) -> None`: Export as environment variables script

**Getter Methods:**

- `get_log_level() -> str`
- `get_log_file() -> Path`
- `get_printer_level() -> str`
- `get_file_logger_level() -> str`
- `get_indent_step() -> int`
- `get_indent_symbol() -> str`
- `get_base_indent_symbol() -> str`
- `get_log_format() -> str`
- `get_log_rotation() -> Optional[str]`
- `get_log_retention() -> Optional[str]`
- `get_log_compression() -> Optional[str]`

**Environment Variables:**

- `EZPL_LOG_LEVEL`: Global log level (applies to both printer and logger)
- `EZPL_LOG_FILE`: Log file name
- `EZPL_LOG_DIR`: Log directory path
- `EZPL_PRINTER_LEVEL`: Printer log level
- `EZPL_FILE_LOGGER_LEVEL`: File logger level
- `EZPL_INDENT_STEP`: Indentation step size (integer)
- `EZPL_INDENT_SYMBOL`: Symbol for indentation
- `EZPL_BASE_INDENT_SYMBOL`: Base indentation symbol
- `EZPL_LOG_FORMAT`: Log format string
- `EZPL_LOG_ROTATION`: Rotation setting (e.g., "10 MB", "1 day")
- `EZPL_LOG_RETENTION`: Retention period (e.g., "7 days", "10 files")
- `EZPL_LOG_COMPRESSION`: Compression format (e.g., "zip", "gz")

**Priority Order:**
When initializing `Ezpl()`, the priority order for each parameter is:

1. **Arguments passed directly** (if provided in constructor)
2. **Environment variables** (`EZPL_*`)
3. **Configuration file** (`~/.ezpl/config.json`)
4. **Default values**

---

### Exceptions

**File:** `ezpl/core/exceptions.py`

Custom exception classes for better error handling and debugging.

**Base Exception:**

- `EzplError(message: str, error_code: str = None)`: Base exception class

**Specific Exceptions:**

- `ConfigurationError(message: str, config_key: str = None)`: Configuration-related errors
- `LoggingError(message: str, handler_type: str = None)`: Logging operation errors
- `ValidationError(message: str, field_name: str = None, value: str = None)`: Input validation errors
- `InitializationError(message: str, component: str = None)`: Initialization errors
- `FileOperationError(message: str, file_path: str = None, operation: str = None)`: File operation errors
- `HandlerError(message: str, handler_name: str = None)`: Handler-related errors

**Example:**

```python
from ezpl import Ezpl, ValidationError

try:
    ezpl = Ezpl()
    ezpl.set_level("INVALID_LEVEL")
except ValidationError as e:
    print(f"Validation error: {e}")
    print(f"Field: {e.field_name}")
    print(f"Value: {e.value}")
```

---

## 🧪 Usage Examples

### Basic Usage

```python
from pathlib import Path
from ezpl import Ezpl, Printer
from loguru import Logger

# Get the singleton
ezpl = Ezpl(log_file=Path("app.log"))

# Get typed instances
printer: Printer = ezpl.get_printer()
logger: Logger = ezpl.get_logger()

# Console log (printer with Rich - pattern format)
printer.info("Information message")        # • INFO     :: Information message
printer.success("Success!")                   # • SUCCESS  :: Success!
printer.warning("Warning!")                   # • WARN     :: Warning!
printer.error("Critical error")               # • ERROR    :: Critical error
printer.debug("Debug message")                # • DEBUG    :: Debug message

# Pattern methods
printer.tip("Pro tip: Use type hints")
printer.system("System check completed")
printer.install("Installing dependencies...")
printer.detect("Configuration detected")
printer.config("Config loaded")
printer.deps("Dependencies resolved")

# File log (logger with loguru - structured format)
logger.info("Message in the log file")
logger.error("Error in the log file")
# Output: 2024-01-15 10:30:45 | INFO      | module:function:42 - Message in the log file
```

### Advanced Console Features

```python
from ezpl import Ezpl, Printer

ezpl = Ezpl()
printer: Printer = ezpl.get_printer()

# Rich tables
printer.print_table([
    {"Name": "Alice", "Age": 30, "City": "Paris"},
    {"Name": "Bob", "Age": 25, "City": "London"}
], title="Users")

# Rich panels
printer.print_panel("Important message", title="Alert", style="red")

# JSON display with syntax highlighting
printer.print_json({
    "name": "Ezpl",
    "version": "1.0.0",
    "features": ["Rich", "loguru", "typing"]
}, title="Configuration")

# Contextual indentation
with ezpl.manage_indent():
    printer.info("Indented message")
    printer.success("Another indented message")
```

### RichWizard Usage

**Panels:**

```python
from ezpl import Ezpl

ezpl = Ezpl()
printer = ezpl.get_printer()

# Display panels
printer.wizard.success_panel("Success", "Operation completed successfully")
printer.wizard.error_panel("Error", "Failed to connect to database")
printer.wizard.info_panel("Info", "Processing your request...")
printer.wizard.installation_panel("Step 1", "Installing dependencies", status="success")
```

**Tables:**

```python
# Status table
data = [
    {"Service": "API", "Status": "success", "Uptime": "99.9%"},
    {"Service": "DB", "Status": "error", "Uptime": "95.2%"},
]
printer.wizard.status_table("Service Status", data)

# Dependency table
deps = {"requests": "2.31.0", "click": "8.1.0", "missing": ""}
printer.wizard.dependency_table(deps)

# Command table
commands = [
    {"command": "install", "description": "Install package", "category": "Package"},
    {"command": "update", "description": "Update package", "category": "Package"},
]
printer.wizard.command_table(commands)
```

**JSON:**

```python
# Simple JSON
printer.wizard.json({"name": "Alice", "age": 30})

# JSON with title panel
printer.wizard.json({"config": "value"}, title="Configuration")
```

**Progress Bars:**

```python
# Simple progress
with printer.wizard.progress("Processing files...", total=100) as (progress, task):
    for i in range(100):
        progress.update(task, advance=1)

# Spinner
with printer.wizard.spinner("Loading...") as (progress, task):
    # Do work
    time.sleep(2)

# Download progress
with printer.wizard.file_download_progress("file.zip", 1024000) as (progress, task):
    progress.update(task, advance=512000)

# Installation progress
steps = [("Init", "Initializing..."), ("Install", "Installing..."), ("Config", "Configuring...")]
with printer.wizard.installation_progress(steps) as (progress, task, name, desc):
    for step_name, step_desc in steps:
        # Process step
        progress.advance(task)
```

**Dynamic Layered Progress:**

```python
stages = [
    {"name": "main", "type": "main", "description": "Installation"},
    {"name": "download", "type": "download", "description": "Downloading", "total_size": 1024000, "filename": "file.zip"},
    {"name": "extract", "type": "progress", "description": "Extracting", "total": 100},
    {"name": "install", "type": "steps", "description": "Installing", "steps": ["Deps", "Config", "Verify"]},
]

with printer.wizard.dynamic_layered_progress(stages) as progress:
    # Download
    progress.update_layer("download", 512000, "Downloading...")
    progress.complete_layer("download")  # Disappears with animation
    
    # Extract
    progress.update_layer("extract", 50, "Extracting files...")
    progress.complete_layer("extract")  # Disappears
    
    # Install
    progress.update_layer("install", 1, "Configuring...")
    progress.complete_layer("install")  # Disappears
    
    # Main layer auto-updates and stays visible
```

### File Logger with Rotation

```python
from ezpl.handlers import FileLogger

# File logger with rotation
logger_handler = FileLogger(
    "app.log",
    level="INFO",
    rotation="10 MB",      # Rotate at 10 MB
    retention="7 days",    # Keep logs for 7 days
    compression="zip"      # Compress old logs
)

logger = logger_handler.get_logger()
logger.info("This will be rotated when file reaches 10 MB")

# Get file size
size = logger_handler.get_file_size()
print(f"Log file size: {size} bytes")
```

### Configuration Management

```python
from ezpl import Ezpl
from pathlib import Path
import os

# Method 1: Direct arguments (highest priority)
ezpl = Ezpl(
    log_file=Path("app.log"),
    log_level="DEBUG",
    log_rotation="10 MB",
    log_retention="7 days"
)

# Method 2: Environment variables (automatic)
os.environ["EZPL_LOG_LEVEL"] = "DEBUG"
os.environ["EZPL_LOG_ROTATION"] = "10 MB"
ezpl = Ezpl()  # Will use environment variables

# Method 3: Configuration file
# ~/.ezpl/config.json contains: {"log-level": "DEBUG", "log-rotation": "10 MB"}
ezpl = Ezpl()  # Will use config file

# Method 4: Configure dynamically after initialization
ezpl = Ezpl()
ezpl.configure(
    level="DEBUG",
    log_rotation="10 MB",
    log_retention="7 days",
    indent_step=4
)

# Method 5: Reload configuration from file/env vars
ezpl.reload_config()  # Useful if env vars changed after initialization

# Or use the configuration manager directly
config = ezpl.get_config()
config.set("printer-level", "WARNING")
config.save()
```

### Handling Special Characters

```python
from ezpl import Ezpl, Printer

ezpl = Ezpl()
printer: Printer = ezpl.get_printer()

# Ezpl handles special characters robustly

# Windows paths with backslashes
printer.error("Path: C:\\Users\\Test\\file.txt")

# Messages with braces
printer.error("Error in {function}")

# Unicode characters
printer.info("Unicode: éèàçô 漢字 🚀")

# Exception objects (auto-converted to string)
try:
    1 / 0
except Exception as e:
    printer.error(e)  # Automatically converted to string

# Complex objects
printer.info({"key": "value", "nested": {"a": 1}})
```

### Type Hints for Better IDE Support

```python
from ezpl import Ezpl, Printer
from loguru import Logger

ezpl = Ezpl()

# Type hints enable full IDE autocompletion
printer: Printer = ezpl.get_printer()
logger: Logger = ezpl.get_logger()

# IDE will suggest all available methods
printer.info("...")      # Autocompletion works!
printer.print_json(...)  # Autocompletion works!
logger.info("...")       # Autocompletion works!
```

---

## 🎯 Best Practices

### Type Safety

- **Use type hints**: Import `Printer` from `ezpl` for better IDE support
- **Type your variables**: `printer: Printer = ezpl.get_printer()` enables full autocompletion
- **Import Logger from loguru**: `from loguru import Logger` for file logger type hints

### Logging Levels

- Use `set_printer_level()` and `set_logger_level()` to adjust verbosity independently
- Use `set_level()` to change both at once
- Set appropriate levels for production vs development

### Console Output

- Use context managers (`manage_indent()`) for console indentation
- Leverage Rich features (tables, panels, JSON) for better console output
- Use pattern methods (`tip()`, `system()`, etc.) for semantic meaning

### File Logging

- Configure file rotation for production applications
- Use retention policies to manage disk space
- Enable compression for archived logs
- Use separators to distinguish sessions

### Error Handling

- Ezpl is designed to never crash, even with problematic input
- All exceptions are custom and provide detailed error information
- Catch specific exceptions (`ValidationError`, `FileOperationError`, etc.) for better error handling

### Configuration

**Priority Order:**

1. **Arguments in `Ezpl()`** - Use for explicit, code-level configuration
2. **Environment variables (`EZPL_*`)** - Use for deployment-specific settings
3. **Configuration file (`~/.ezpl/config.json`)** - Use for user preferences
4. **Default values** - Fallback when nothing else is specified

**Best Practices:**

- Configure Ezpl **before** importing libraries that use it (for Singleton propagation)
- Use environment variables for sensitive or environment-specific settings
- Use `configure()` for runtime configuration changes
- Use `reload_config()` if environment variables change after initialization
- Configuration changes are automatically propagated to all libraries using the Singleton

**Singleton Propagation Example:**

```python
# In root project (project_test/main.py)
from ezpl import Ezpl

# Configure BEFORE importing libraries
ezpl = Ezpl(log_level="DEBUG", log_rotation="10 MB")

# Now import libraries - they will use the same configuration
import lib_a  # Uses the configured Ezpl instance
import lib_b  # Uses the same configured Ezpl instance
```

### Testing

- Use `reset()` method in tests to ensure clean state
- Test robustness by passing exceptions or unexpected objects to log methods
- Verify both console and file output in tests

### Performance

- **Rich for console**: Slightly slower than loguru but more robust and beautiful
- **loguru for files**: Excellent performance and features for file logging
- **Indentation limit**: Maximum 10 levels to prevent performance issues

---

## 📝 Type Reference

### Type Aliases

```python
from ezpl import Printer  # Alias for ConsolePrinterWrapper
from loguru import Logger  # For file logger type hints
```

### Return Types

```python
# Ezpl methods
ezpl.get_printer() -> ConsolePrinterWrapper
ezpl.get_logger() -> Logger  # loguru.Logger
ezpl.get_config() -> ConfigurationManager

# ConsolePrinter methods
printer.get_printer() -> ConsolePrinterWrapper
printer.wizard -> RichWizard  # Access to wizard features

# FileLogger methods
logger_handler.get_logger() -> Logger  # loguru.Logger
logger_handler.get_log_file() -> Path
logger_handler.get_file_size() -> int

# RichWizard methods
wizard.panel(...) -> None
wizard.table(...) -> None
wizard.json(...) -> None
wizard.progress(...) -> Generator[Tuple[Progress, int], None, None]
wizard.dynamic_layered_progress(...) -> Generator[DynamicLayeredProgress, None, None]
```

---

**Ezpl – Complete API documentation for professional and robust logging integration in your Python projects.**
