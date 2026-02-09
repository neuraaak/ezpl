# Getting Started

This guide will help you get started with **Ezpl** quickly and easily.

## Installation

### From PyPI (Recommended)

```bash
pip install ezplog
```

### From Source

```bash
git clone https://github.com/neuraaak/ezplog.git
cd ezplog
pip install .
```

### Development Installation

For contributors and developers:

```bash
pip install -e ".[dev]"
```

This installs Ezpl in editable mode with all development dependencies (testing, linting, formatting tools).

## First Steps

### Basic Console Logging

```python
from ezpl import Ezpl

# Create the singleton instance
ezpl = Ezpl()

# Get the printer (console output)
printer = ezpl.get_printer()

# Log messages with different levels
printer.debug("Debug message")
printer.info("Information message")
printer.success("Success message")
printer.warning("Warning message")
printer.error("Error message")
printer.critical("Critical message")
```

### File Logging

```python
from ezpl import Ezpl

# Initialize with a log file
ezpl = Ezpl(log_file="app.log")

# Get the logger (file output)
logger = ezpl.get_logger()

# Log to file
logger.info("This goes to the file")
logger.debug("Debug information")
logger.error("Error logged to file")
```

### Combined Console and File Logging

```python
from ezpl import Ezpl, Printer, Logger

# Initialize with log file
ezpl = Ezpl(log_file="app.log")

# Get both handlers with type hints
printer: Printer = ezpl.get_printer()
logger: Logger = ezpl.get_logger()

# Log to console
printer.info("Visible in console")

# Log to file
logger.info("Saved in file")

# Log to both
printer.info("Console message")
logger.info("File message with same content")
```

## Configuration

### Direct Configuration

```python
from ezpl import Ezpl

ezpl = Ezpl(
    log_file="app.log",
    log_level="DEBUG",              # Global level
    printer_level="INFO",            # Console level
    file_logger_level="DEBUG",       # File level
    log_rotation="10 MB",            # Rotate at 10 MB
    log_retention="7 days",          # Keep 7 days
    log_compression="zip"            # Compress old logs
)
```

### Environment Variables

Set environment variables with the `EZPL_` prefix:

```bash
# Linux/macOS
export EZPL_LOG_LEVEL=DEBUG
export EZPL_LOG_FILE=app.log
export EZPL_LOG_ROTATION="10 MB"

# Windows
set EZPL_LOG_LEVEL=DEBUG
set EZPL_LOG_FILE=app.log
set EZPL_LOG_ROTATION=10 MB
```

### Configuration File

Create `~/.ezpl/config.json`:

```json
{
  "log_level": "INFO",
  "log_file": "app.log",
  "printer_level": "INFO",
  "file_logger_level": "DEBUG",
  "log_rotation": "10 MB",
  "log_retention": "7 days",
  "log_compression": "zip",
  "indent_step": 3,
  "indent_symbol": ">",
  "base_indent_symbol": "~"
}
```

### Configuration Priority

When multiple configuration sources exist, Ezpl follows this priority order (highest to lowest):

1. **Direct arguments** passed to `Ezpl()`
2. **Environment variables** (`EZPL_*`)
3. **Configuration file** (`~/.ezpl/config.json`)
4. **Default values**

## Pattern-Based Logging

Ezpl provides contextual patterns for common scenarios:

```python
from ezpl import Ezpl

ezpl = Ezpl()
printer = ezpl.get_printer()

# Different patterns
printer.success("Operation completed")
printer.error_msg("Something went wrong")
printer.warn("Warning message")
printer.tip("Pro tip: Use type hints!")
printer.system("System message")
printer.install("Installing package...")
```

## Indentation Management

Ezpl supports contextual indentation for better log readability:

```python
from ezpl import Ezpl

ezpl = Ezpl()
printer = ezpl.get_printer()

printer.info("Starting process")

# Increase indentation
ezpl.increase_indent()
printer.info("Step 1")
printer.info("Step 2")

# Further indentation
ezpl.increase_indent()
printer.info("Substep 2.1")
printer.info("Substep 2.2")

# Decrease indentation
ezpl.decrease_indent()
printer.info("Step 3")

# Reset indentation
ezpl.reset_indent()
printer.info("Process complete")
```

### Context Manager for Indentation

```python
from ezpl import Ezpl

ezpl = Ezpl()
printer = ezpl.get_printer()

printer.info("Main process")

with ezpl.manage_indent():
    printer.info("Indented step 1")
    printer.info("Indented step 2")

    with ezpl.manage_indent():
        printer.info("Double indented")

printer.info("Back to normal")
```

## Advanced Features

### RichWizard - Panels

```python
from ezpl import Ezpl

ezpl = Ezpl()
printer = ezpl.get_printer()

# Display panels
printer.wizard.success_panel("Success", "Operation completed successfully!")
printer.wizard.error_panel("Error", "Something went wrong")
printer.wizard.info_panel("Information", "This is an info message")
```

### RichWizard - Tables

```python
from ezpl import Ezpl

ezpl = Ezpl()
printer = ezpl.get_printer()

# Display table
data = [
    {"Name": "Alice", "Age": 30, "City": "Paris"},
    {"Name": "Bob", "Age": 25, "City": "London"},
    {"Name": "Charlie", "Age": 35, "City": "Berlin"}
]

printer.wizard.table(data, title="Users")
```

### RichWizard - JSON Display

```python
from ezpl import Ezpl

ezpl = Ezpl()
printer = ezpl.get_printer()

# Display JSON
data = {
    "name": "Ezpl",
    "version": "1.5.1",
    "features": ["rich", "loguru", "typed"]
}

printer.wizard.json_display(data)
```

### Progress Bars

```python
from ezpl import Ezpl
import time

ezpl = Ezpl()
printer = ezpl.get_printer()

# Simple progress bar
with printer.wizard.progress() as progress:
    task = progress.add_task("[cyan]Processing...", total=100)

    for i in range(100):
        time.sleep(0.05)
        progress.update(task, advance=1)
```

## Type Hints Support

Ezpl provides full type hints for better IDE support:

```python
from ezpl import Ezpl, Printer, Logger, LogLevel, Pattern

# Type-annotated code
ezpl: Ezpl = Ezpl()
printer: Printer = ezpl.get_printer()
logger: Logger = ezpl.get_logger()

# Using enums
level: LogLevel = LogLevel.INFO
pattern: Pattern = Pattern.SUCCESS
```

## CLI Tools

Ezpl includes a command-line interface:

```bash
# View logs
ezpl logs view --lines 50

# Show configuration
ezpl config show

# Set configuration
ezpl config set log_level DEBUG

# Show statistics
ezpl logs stats

# Display version
ezpl version
```

For more details, see the [CLI Reference](cli/index.md).

## Next Steps

- Explore the [API Reference](api/index.md) for detailed documentation
- Check out [Examples](examples/index.md) for practical use cases
- Read the [User Guides](guides/index.md) for in-depth tutorials
- Learn about [Testing](guides/testing.md) best practices

## Troubleshooting

### Import Error

If you get an import error:

```python
# Make sure you're importing from 'ezpl', not 'ezplog'
from ezpl import Ezpl  # Correct
# from ezplog import Ezpl  # Wrong
```

### Log File Not Created

Check file permissions and path:

```python
from pathlib import Path

log_path = Path("logs/app.log")
log_path.parent.mkdir(parents=True, exist_ok=True)

ezpl = Ezpl(log_file=str(log_path))
```

### Version Mismatch

Check your installed version:

```python
import ezpl
print(ezpl.__version__)
```

Or from command line:

```bash
ezpl version
```

## Need Help?

- **Documentation**: [Full API Reference](api/index.md)
- **Issues**: [GitHub Issues](https://github.com/neuraaak/ezplog/issues)
- **Repository**: [https://github.com/neuraaak/ezplog](https://github.com/neuraaak/ezplog)
