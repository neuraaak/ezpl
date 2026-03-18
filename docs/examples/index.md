# Examples

Practical examples and usage demonstrations for **Ezpl** logging framework.

## Overview

This section provides comprehensive examples showcasing all Ezpl features including console logging, file logging, Rich display capabilities, configuration management, and advanced progress bars.

## Example Scripts

The `examples/` directory in the repository contains ready-to-run demonstration scripts:

| Script                                                                                 | Description                    | Level         |
| -------------------------------------------------------------------------------------- | ------------------------------ | ------------- |
| [`demo.py`](https://github.com/neuraaak/ezplog/blob/main/examples/demo.py)             | Complete feature demonstration | Comprehensive |
| [`quick_test.py`](https://github.com/neuraaak/ezplog/blob/main/examples/quick_test.py) | Interactive testing menu       | Interactive   |

## Basic Examples

### Simple Console Logging

```python
from ezplog import Ezpl

# Initialize
ezpl = Ezpl()
printer = ezpl.get_printer()

# Log messages
printer.info("Application started")
printer.success("Operation completed successfully")
printer.warning("Low disk space")
printer.error("Failed to connect to database")
```

**Output:**

```text
• INFO    :: Application started
• SUCCESS :: Operation completed successfully
• WARN    :: Low disk space
• ERROR   :: Failed to connect to database
```

### File Logging

```python
from ezplog import Ezpl

# Initialize with log file
ezpl = Ezpl(log_file="app.log")
logger = ezpl.get_logger()

# Log to file
logger.info("Application started")
logger.debug("Processing item 1")
logger.error("Connection failed")
```

**File output (`app.log`):**

```text
2024-01-15 10:30:45 | INFO    | __main__:main:5 - Application started
2024-01-15 10:30:45 | DEBUG   | __main__:main:6 - Processing item 1
2024-01-15 10:30:46 | ERROR   | __main__:main:7 - Connection failed
```

### Combined Console and File Logging

```python
from ezplog import Ezpl, Printer, Logger

# Initialize with type hints
ezpl = Ezpl(log_file="app.log", log_level="DEBUG")
printer: Printer = ezpl.get_printer()
logger: Logger = ezpl.get_logger()

# Log to both
printer.info("User logged in")  # Console
logger.info("User logged in")   # File

printer.success("Data saved")
logger.info("Data saved to database")
```

## Pattern-Based Logging

### Using Contextual Patterns

```python
from ezplog import Ezpl

ezpl = Ezpl()
printer = ezpl.get_printer()

# Different patterns for different contexts
printer.tip("Pro tip: Use type hints for better IDE support")
printer.system("System check completed")
printer.install("Installing package 'requests'...")
printer.detect("Detected Python 3.11.3")
printer.config("Configuration loaded from ~/.ezpl/config.json")
printer.deps("Dependencies: rich==13.7.0, loguru==0.7.2")
```

**Output:**

```text
• TIP     :: Pro tip: Use type hints for better IDE support
• SYSTEM  :: System check completed
• INSTALL :: Installing package 'requests'...
• DETECT  :: Detected Python 3.11.3
• CONFIG  :: Configuration loaded from ~/.ezpl/config.json
• DEPS    :: Dependencies: rich==13.7.0, loguru==0.7.2
```

### Custom Patterns

```python
from ezplog import Ezpl, Pattern

ezpl = Ezpl()
printer = ezpl.get_printer()

# Use custom pattern
printer.print_pattern(Pattern.SUCCESS, "Deployment successful", level="INFO")
printer.print_pattern("CUSTOM", "Custom pattern message")
```

## Rich Display Features

### Panels

```python
from ezplog import Ezpl

ezpl = Ezpl()
wizard = ezpl.get_printer().wizard

# Success panel
wizard.success_panel("Deployment Complete", "Application deployed to production")

# Error panel
wizard.error_panel("Connection Error", "Failed to connect to database")

# Info panel
wizard.info_panel("System Information", "Python 3.11.3 | Linux x86_64")

# Warning panel
wizard.warning_panel("Disk Space Low", "Only 5% disk space remaining")

# Installation panel
wizard.installation_panel(
    step="Installing dependencies",
    description="pip install -r requirements.txt",
    status="success"  # success, error, warning, in_progress
)
```

### Tables

```python
from ezplog import Ezpl

ezpl = Ezpl()
wizard = ezpl.get_printer().wizard

# Simple table
data = [
    {"Name": "Alice", "Age": 30, "City": "Paris"},
    {"Name": "Bob", "Age": 25, "City": "London"},
    {"Name": "Charlie", "Age": 35, "City": "Berlin"}
]
wizard.table(data, title="Users")

# Status table with colored indicators
status_data = [
    {"Task": "Build", "Status": "success", "Duration": "2m 30s"},
    {"Task": "Test", "Status": "success", "Duration": "1m 15s"},
    {"Task": "Deploy", "Status": "in_progress", "Duration": "..."}
]
wizard.status_table("CI/CD Pipeline", status_data, status_column="Status")

# Dependency table
dependencies = [
    ("rich", "13.7.0", True),
    ("loguru", "0.7.2", True),
    ("missing-package", None, False)
]
wizard.dependency_table(dependencies)

# Command table
commands = [
    ("ezpl logs view", "View log files", "Logs"),
    ("ezpl config show", "Show configuration", "Config"),
    ("ezpl version", "Show version", "Info")
]
wizard.command_table(commands)
```

### JSON Display

```python
from ezplog import Ezpl

ezpl = Ezpl()
wizard = ezpl.get_printer().wizard

# Display JSON
config = {
    "app": "MyApp",
    "version": "1.0.0",
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "mydb"
    },
    "features": ["logging", "caching", "monitoring"]
}

wizard.json(config, title="Configuration")

# From JSON string
json_str = '{"status": "ok", "message": "Success"}'
wizard.json(json_str)
```

## Progress Bars

### Simple Progress

```python
from ezplog import Ezpl
import time

ezpl = Ezpl()
wizard = ezpl.get_printer().wizard

# Simple progress bar
with wizard.progress("[cyan]Processing...", total=100) as (progress, task):
    for _ in range(100):
        time.sleep(0.05)
        progress.update(task, advance=1)
```

### Spinner

```python
from ezplog import Ezpl
import time

ezpl = Ezpl()
wizard = ezpl.get_printer().wizard

# Simple spinner
with wizard.spinner("Loading data..."):
    time.sleep(3)

# Spinner with status updates
with wizard.spinner_with_status("Processing") as (progress, task):
    progress.update(task, status="Loading configuration...")
    time.sleep(1)
    progress.update(task, status="Connecting to database...")
    time.sleep(1)
    progress.update(task, status="Fetching data...")
    time.sleep(1)
```

### Download Progress

```python
from ezplog import Ezpl
import time

ezpl = Ezpl()
wizard = ezpl.get_printer().wizard

# File download with size and speed
with wizard.file_download_progress(
    filename="large-file.zip",
    total_size=104857600,  # 100 MB
    description="Downloading"
) as (progress, task):

    for _ in range(100):
        time.sleep(0.05)
        progress.update(task, advance=1048576)  # 1 MB per iteration
```

### Step Progress

```python
from ezplog import Ezpl
import time

ezpl = Ezpl()
wizard = ezpl.get_printer().wizard

# Step-based progress
steps = [
    "Initializing project",
    "Installing dependencies",
    "Configuring environment",
    "Running tests",
    "Building application",
    "Deployment complete"
]

with wizard.step_progress(steps, "Setup Process") as (progress, task, steps_list):
    for i, step in enumerate(steps_list):
        progress.update(task, completed=i, current_step=step)
        progress.advance(task)
        time.sleep(1)
```

### Installation Progress

```python
from ezplog import Ezpl
import time

ezpl = Ezpl()
wizard = ezpl.get_printer().wizard

# Package installation with versions
packages = [
    ("rich", "13.7.0"),
    ("loguru", "0.7.2"),
    ("click", "8.1.7"),
    ("pytest", "7.4.3")
]

with wizard.package_install_progress(
    packages,
    description="Installing Dependencies"
) as (progress, task, package, version):
    progress.update(task, description=f"Installing {package}", version=version)
    progress.advance(task)
    time.sleep(1)
```

### Dynamic Layered Progress

```python
from ezplog import Ezpl
import time

ezpl = Ezpl()
wizard = ezpl.get_printer().wizard

# Multi-level progress with dynamic layers
stages = [
    {
        "name": "build",
        "type": "progress",
        "description": "Building project",
        "total": 100
    },
    {
        "name": "test",
        "type": "steps",
        "description": "Running tests",
        "steps": ["Unit tests", "Integration tests", "E2E tests"]
    },
    {
        "name": "deploy",
        "type": "spinner",
        "description": "Deploying to production"
    }
]

with wizard.dynamic_layered_progress(stages) as dlp:
    # Build stage
    for i in range(100):
        dlp.update_layer("build", progress=i+1)
        time.sleep(0.05)
    dlp.complete_layer("build")

    # Test stage
    for step in stages[1]["steps"]:
        dlp.update_layer("test", details=step)
        time.sleep(1)
    dlp.complete_layer("test")

    # Deploy stage
    dlp.update_layer("deploy", details="Uploading artifacts...")
    time.sleep(2)
    dlp.complete_layer("deploy")
```

## Indentation Management

### Manual Indentation

```python
from ezplog import Ezpl

ezpl = Ezpl()
printer = ezpl.get_printer()

printer.info("Starting main process")

# Increase indentation
printer.add_indent()
printer.info("Step 1: Initialize")
printer.info("Step 2: Load data")

# Further indentation
printer.add_indent()
printer.info("Substep 2.1: Validate")
printer.info("Substep 2.2: Process")

# Decrease indentation
printer.del_indent()
printer.info("Step 3: Finalize")

# Reset indentation
printer.reset_indent()
printer.success("Process complete")
```

**Output:**

```text
• INFO :: Starting main process
>>> • INFO :: Step 1: Initialize
>>> • INFO :: Step 2: Load data
>>>>>> • INFO :: Substep 2.1: Validate
>>>>>> • INFO :: Substep 2.2: Process
>>> • INFO :: Step 3: Finalize
• SUCCESS :: Process complete
```

### Context Manager

```python
from ezplog import Ezpl

ezpl = Ezpl()
printer = ezpl.get_printer()

printer.info("Main process")

with ezpl.manage_indent():
    printer.info("Indented step 1")
    printer.info("Indented step 2")

    with ezpl.manage_indent():
        printer.info("Double indented")
        printer.info("Double indented 2")

printer.info("Back to normal")
```

## Configuration

### Runtime Configuration

```python
from ezplog import Ezpl

# Initialize with configuration
ezpl = Ezpl(
    log_file="app.log",
    log_level="DEBUG",
    printer_level="INFO",
    file_logger_level="DEBUG",
    log_rotation="10 MB",
    log_retention="7 days",
    log_compression="zip"
)

# Reconfigure at runtime
ezpl.configure(
    printer_level="WARNING",
    logger_level="ERROR"
)

# Change levels
ezpl.set_level("DEBUG")
ezpl.set_printer_level("INFO")
ezpl.set_logger_level("DEBUG")

# Reload configuration from file/environment
ezpl.reload_config()
```

### Environment Variables

```python
import os
from ezplog import Ezpl

# Set environment variables
os.environ["EZPL_LOG_LEVEL"] = "DEBUG"
os.environ["EZPL_LOG_FILE"] = "app.log"
os.environ["EZPL_LOG_ROTATION"] = "10 MB"

# Initialize (will use environment variables)
ezpl = Ezpl()

# Get configuration
config = ezpl.get_config()
print(config.get_log_level())  # DEBUG
print(config.get_log_file())   # app.log
```

### Configuration File

Create `~/.ezpl/config.json`:

```json
{
  "log-level": "INFO",
  "log-file": "ezpl.log",
  "printer-level": "INFO",
  "file-logger-level": "DEBUG",
  "log-rotation": "10 MB",
  "log-retention": "7 days",
  "log-compression": "zip",
  "indent-step": 3,
  "indent-symbol": ">",
  "base-indent-symbol": "~"
}
```

```python
from ezplog import Ezpl

# Initialize (will use config file)
ezpl = Ezpl()
```

## Advanced Examples

### Complete Application Example

```python
from ezplog import Ezpl, Printer, Logger
from pathlib import Path
import time

def main():
    # Initialize with full configuration
    ezpl = Ezpl(
        log_file="myapp.log",
        log_level="DEBUG",
        log_rotation="10 MB",
        log_retention="30 days",
        log_compression="zip"
    )

    printer: Printer = ezpl.get_printer()
    logger: Logger = ezpl.get_logger()
    wizard = printer.wizard

    # Application start
    printer.system("Application starting...")
    logger.info("Application started")

    # Configuration
    wizard.success_panel("Configuration", "All settings loaded successfully")

    # Processing with progress
    with wizard.progress("[cyan]Processing data...", total=100) as (progress, task):
        for i in range(100):
            logger.debug(f"Processing item {i + 1}")
            time.sleep(0.05)
            progress.update(task, advance=1)

    # Results
    results = {
        "processed": 100,
        "errors": 0,
        "duration": "5.2s"
    }
    wizard.json(results, title="Processing Results")

    # Summary table
    summary = [
        {"Metric": "Total items", "Value": "100"},
        {"Metric": "Successful", "Value": "100"},
        {"Metric": "Failed", "Value": "0"},
        {"Metric": "Duration", "Value": "5.2s"}
    ]
    wizard.table(summary, title="Summary")

    # Completion
    printer.success("Application completed successfully")
    logger.info("Application completed")

if __name__ == "__main__":
    main()
```

### Error Handling Example

```python
from ezplog import Ezpl, ValidationError, LoggingError
import sys

def main():
    try:
        ezpl = Ezpl(log_file="app.log")
        printer = ezpl.get_printer()

        # Your application logic
        printer.info("Processing data...")

        # Simulate error
        raise ValueError("Invalid data format")

    except ValidationError as e:
        printer.error(f"Validation error: {e.message}")
        sys.exit(1)

    except LoggingError as e:
        printer.error(f"Logging error: {e.message}")
        sys.exit(1)

    except Exception as e:
        printer.error(f"Unexpected error: {str(e)}")
        sys.exit(1)

    finally:
        printer.info("Cleanup complete")

if __name__ == "__main__":
    main()
```

## See Also

- [Getting Started](../getting-started.md) - Basic usage and installation
- [API Reference](../api/index.md) - Complete API documentation
- [CLI Reference](../cli/index.md) - Command-line interface
- [User Guides](../guides/index.md) - In-depth guides

## Repository Examples

For more examples, check the `examples/` directory in the repository:

- [demo.py](https://github.com/neuraaak/ezplog/blob/main/examples/demo.py) - Complete feature demonstration
- [quick_test.py](https://github.com/neuraaak/ezplog/blob/main/examples/quick_test.py) - Interactive testing menu

## Need Help?

- **Issues**: [GitHub Issues](https://github.com/neuraaak/ezplog/issues)
- **Repository**: [https://github.com/neuraaak/ezplog](https://github.com/neuraaak/ezplog)
