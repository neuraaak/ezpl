# Examples Documentation – Ezpl

## Overview

This folder contains comprehensive examples and usage demonstrations for the **Ezpl** logging framework. These examples showcase all features including console logging, file logging, Rich display capabilities, configuration management, and advanced progress bars.

## Documentation Structure

### 📋 Main Documentation

- **EXAMPLES.md** (this file) – Complete examples guide
  - Script descriptions and usage
  - Code examples for all features
  - Best practices and common patterns

---

## Available Example Scripts

### 1. `demo.py` – Complete Demonstration

A comprehensive script demonstrating all Ezpl features.

**Location:** `examples/demo.py`

**Usage:**

```bash
python examples/demo.py
```

**Sections Covered:**

1. **Log Levels** – All standard log levels (DEBUG, INFO, SUCCESS, WARNING, ERROR, CRITICAL)
2. **Pattern Methods** – Contextual patterns (TIP, SYSTEM, INSTALL, DETECT, CONFIG, DEPS)
3. **Rich Features – Panels** – Info, success, error, warning, installation panels
4. **Rich Features – Tables** – Generic, status, dependency, and command tables
5. **Rich Features – JSON** – Syntax-highlighted JSON display
6. **Progress Bars** – Simple, spinner, download, file download, dependency, step progress
7. **Indentation** – Nested indentation management
8. **Configuration** – Runtime configuration and settings
9. **File Logging** – Structured file logging with separators
10. **Dynamic Layered Progress** – Multi-level progress bars with automatic layer management

**Example Output:**

```
================================================================================
SECTION 1: NIVEAUX DE LOG
================================================================================

• DEBUG   :: Message de debug - pour le développement
• INFO    :: Message d'information - opération normale
• SUCCESS :: Message de succès - opération réussie
...
```

### 2. `quick_test.py` – Interactive Testing

An interactive script with a menu to test features one by one.

**Location:** `examples/quick_test.py`

**Usage:**

```bash
python examples/quick_test.py
```

**Interactive Menu:**

- **1.** Test log levels
- **2.** Test patterns
- **3.** Test panels
- **4.** Test tables
- **5.** Test JSON
- **6.** Test progress bars
- **7.** Test indentation
- **8.** Test file logging
- **9.** Show configuration
- **0.** Exit

**Use Case:**

Perfect for exploring Ezpl features interactively or debugging specific functionality.

---

## Usage Examples

### Basic Logging

**Console and File Logging:**

```python
from ezpl import Ezpl
from pathlib import Path

# Initialize
ezpl = Ezpl(log_file="app.log", log_level="DEBUG")
printer = ezpl.get_printer()
logger = ezpl.get_logger()

# Console output (Rich formatting with pattern)
printer.info("Information message")
printer.success("Operation completed!")
printer.warning("Warning message")
printer.error("Error detected")

# File logging (structured format)
logger.info("Logged to file")
logger.debug("Debug information")
logger.warning("Warning in file")
```

**Output:**

- **Console:** `• INFO    :: Information message`
- **File:** `2024-01-15 10:30:45 | INFO       | __main__:main:10 - Logged to file`

### Pattern Methods

**Contextual Patterns:**

```python
from ezpl import Ezpl

ezpl = Ezpl()
printer = ezpl.get_printer()

# Contextual patterns
printer.tip("Pro tip: Use type hints for better code")
printer.system("System check completed")
printer.install("Installing dependency 'requests'...")
printer.detect("Detected Python 3.11.3")
printer.config("Configuration loaded from ~/.ezpl/config.json")
printer.deps("Checking dependencies: rich, loguru, click")
```

### RichWizard Features

**Panels:**

```python
from ezpl import Ezpl

ezpl = Ezpl()
wizard = ezpl.get_printer().wizard

# Simple panel
wizard.panel("Panel content", title="Simple Panel", style="blue")

# Status panels
wizard.info_panel("Information", "This is an info message")
wizard.success_panel("Success", "Operation completed successfully!")
wizard.error_panel("Error", "An error occurred")
wizard.warning_panel("Warning", "Attention required")

# Installation panel
wizard.installation_panel(
    "Installation",
    "Installing ezpl...",
    status="in_progress"
)
```

**Tables:**

```python
from ezpl import Ezpl

ezpl = Ezpl()
wizard = ezpl.get_printer().wizard

# Generic table
data = [
    {"Name": "Alice", "Age": 30, "City": "Paris"},
    {"Name": "Bob", "Age": 25, "City": "Lyon"},
]
wizard.table(data, title="Users")

# Status table (title is first parameter)
status_data = [
    {"Service": "API", "Status": "Active", "Uptime": "99.9%"},
    {"Service": "DB", "Status": "Active", "Uptime": "99.8%"},
]
wizard.status_table("Service Status", status_data, status_column="Status")

# Dependency table (takes a dict)
deps = {
    "requests": "2.31.0",
    "click": "8.1.0",
    "rich": "13.7.0",
}
wizard.dependency_table(deps)

# Command table
commands = [
    {"command": "python demo.py", "description": "Run demo", "category": "demo"},
    {"command": "pytest tests/", "description": "Run tests", "category": "test"},
]
wizard.command_table(commands)
```

**JSON Display:**

```python
from ezpl import Ezpl

ezpl = Ezpl()
wizard = ezpl.get_printer().wizard

# JSON from dict
config = {
    "app_name": "ezpl",
    "version": "1.0.0",
    "features": ["logging", "rich", "cli"],
    "settings": {
        "log_level": "INFO",
        "log_rotation": "10 MB"
    }
}
wizard.json(config, title="Configuration")

# JSON from list
data_list = [
    {"id": 1, "name": "Item 1", "active": True},
    {"id": 2, "name": "Item 2", "active": False},
]
wizard.json(data_list, title="Items")
```

### Progress Bars

**Simple Progress:**

```python
from ezpl import Ezpl
import time

ezpl = Ezpl()
wizard = ezpl.get_printer().wizard

with wizard.progress("Processing...", total=100) as (progress, task):
    for i in range(100):
        progress.update(task, advance=1)
        time.sleep(0.01)
```

**Spinner:**

```python
from ezpl import Ezpl
import time

ezpl = Ezpl()
wizard = ezpl.get_printer().wizard

with wizard.spinner("Loading...") as (progress, task):
    time.sleep(2)
```

**Download Progress:**

```python
from ezpl import Ezpl
import time

ezpl = Ezpl()
wizard = ezpl.get_printer().wizard

with wizard.download_progress("Downloading file.zip") as (progress, task):
    for i in range(0, 100, 10):
        progress.update(task, advance=10, total=100)
        time.sleep(0.1)
```

**Dependency Progress:**

```python
from ezpl import Ezpl
import time

ezpl = Ezpl()
wizard = ezpl.get_printer().wizard

dependencies = ["requests", "click", "rich"]
gen = wizard.dependency_progress(dependencies)
first_yield = gen.__enter__()
progress, task, dep = first_yield
progress.advance(task)
try:
    while True:
        progress, task, dep = next(gen.gen)
        progress.advance(task)
        time.sleep(0.1)
except (StopIteration, AttributeError):
    pass
gen.__exit__(None, None, None)
```

**Dynamic Layered Progress:**

```python
from ezpl import Ezpl
import time

ezpl = Ezpl()
wizard = ezpl.get_printer().wizard

stages = [
    {
        "name": "main",
        "type": "main",
        "description": "Overall progress",
        "steps": ["Step 1", "Step 2", "Step 3"]
    },
    {
        "name": "download",
        "type": "download",
        "description": "Downloading",
        "total_size": 1024000,
        "filename": "file.zip"
    },
    {
        "name": "process",
        "type": "progress",
        "description": "Processing",
        "total": 100
    }
]

with wizard.dynamic_layered_progress(stages, show_time=True) as progress:
    # Update main layer
    progress.update_layer("main", 0, "Starting...")
    time.sleep(0.5)

    # Update download
    progress.update_layer("download", 512000, "Downloading...")
    time.sleep(0.5)

    # Update process
    progress.update_layer("process", 50, "Processing at 50%")
    time.sleep(0.5)

    # Complete layers
    progress.complete_layer("download")
    progress.complete_layer("process")
    progress.complete_layer("main")
```

### Indentation Management

**Nested Indentation:**

```python
from ezpl import Ezpl

ezpl = Ezpl()
printer = ezpl.get_printer()

printer.info("Level 0")
with ezpl.manage_indent():
    printer.info("Level 1")
    with ezpl.manage_indent():
        printer.info("Level 2")
        with ezpl.manage_indent():
            printer.info("Level 3")
    printer.info("Back to level 1")
printer.info("Back to level 0")
```

**Output:**

```
• INFO    :: Level 0
• INFO    ::    > Level 1
• INFO    ::       > Level 2
• INFO    ::          > Level 3
• INFO    ::    > Back to level 1
• INFO    :: Back to level 0
```

### Configuration Management

**Initialization with Configuration:**

```python
from ezpl import Ezpl
from pathlib import Path

# Initialize with configuration
ezpl = Ezpl(
    log_file=Path("app.log"),
    log_level="DEBUG",
    log_rotation="10 MB",
    log_retention="7 days",
    log_compression="zip",
    indent_step=3,
    indent_symbol=">",
    base_indent_symbol="~"
)
```

**Runtime Configuration:**

```python
from ezpl import Ezpl

ezpl = Ezpl()

# Modify configuration
ezpl.configure(printer_level="WARNING")
printer = ezpl.get_printer()
printer.info("This won't appear (level too low)")
printer.warning("This will appear")

# Get current configuration
config = ezpl.get_config()
print(f"Log level: {config.get('log-level')}")
print(f"Printer level: {config.get('printer-level')}")
print(f"Log file: {ezpl.get_log_file()}")
```

**Reload Configuration:**

```python
from ezpl import Ezpl

ezpl = Ezpl()

# Reload from file and environment variables
ezpl.reload_config()
```

### File Logging

**Structured File Logging:**

```python
from ezpl import Ezpl
from pathlib import Path

ezpl = Ezpl(
    log_file=Path("app.log"),
    log_rotation="10 MB",
    log_retention="7 days",
    log_compression="zip"
)

logger = ezpl.get_logger()

# Log messages
logger.info("Information message")
logger.debug("Debug message")
logger.warning("Warning message")
logger.error("Error message")

# Add separator
ezpl.add_separator()

logger.info("Message after separator")

# Get log file path
print(f"Log file: {ezpl.get_log_file()}")
```

---

## Best Practices

### 1. Import Path Setup

For examples in the `examples/` directory, add the parent directory to `sys.path`:

```python
import sys
from pathlib import Path

# Add parent directory to path for ezpl import
sys.path.insert(0, str(Path(__file__).parent.parent))

from ezpl import Ezpl
```

### 2. Log File Management

- Use `Path` objects for log file paths
- Configure rotation for production applications
- Use retention policies to manage disk space
- Enable compression for archived logs

### 3. Error Handling

Ezpl is designed to never crash, but you can still handle errors gracefully:

```python
from ezpl import Ezpl
from ezpl import ValidationError

try:
    ezpl = Ezpl()
    ezpl.set_level("INVALID_LEVEL")
except ValidationError as e:
    print(f"Validation error: {e}")
```

### 4. Configuration Priority

Remember the priority order:

1. **Arguments** (highest priority)
2. **Environment variables** (`EZPL_*`)
3. **Configuration file** (`~/.ezpl/config.json`)
4. **Default values** (lowest priority)

### 5. Singleton Pattern

Configure Ezpl **before** importing libraries that use it:

```python
# In root project (project_test/main.py)
from ezpl import Ezpl

# Configure BEFORE importing libraries
ezpl = Ezpl(log_level="DEBUG", log_rotation="10 MB")

# Now import libraries - they will use the same configuration
import lib_a  # Uses the configured Ezpl instance
import lib_b  # Uses the same configured Ezpl instance
```

---

## Known Issues

### Unicode Encoding on Windows

On Windows, progress bars with Unicode characters may cause encoding errors if the console is not configured for UTF-8.

**Solution 1: Configure Console Encoding**

```python
import sys
import io

# Configure stdout for UTF-8
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

from ezpl import Ezpl
```

**Solution 2: Use PowerShell with UTF-8**

```powershell
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
python examples/demo.py
```

**Solution 3: Avoid Progress Bars**

If encoding issues persist, avoid progress bars (other features work normally).

### Table Method Signatures

- `status_table(title: str, data: List[Dict], status_column: str = "Status")` – `title` is the first parameter
- `dependency_table(dependencies: Dict[str, str])` – takes a dictionary, not a list
- `command_table(commands: List[Dict[str, str]])` – takes a list of dictionaries with keys `command`, `description`, `category`

---

## Running Examples

### Prerequisites

```bash
# Install in development mode
pip install -e .

# Or install dependencies
pip install rich loguru click
```

### Execute Examples

```bash
# Complete demonstration
python examples/demo.py

# Interactive testing
python examples/quick_test.py
```

### Log Files

Example scripts create log files in the current directory:

- `demo.log` – Log file from `demo.py`
- `quick_test.log` – Log file from `quick_test.py`

---

## Additional Resources

- **[API Documentation](docs/api/API_DOCUMENTATION.md)** – Complete API reference
- **[CLI Documentation](docs/cli/CLI_DOCUMENTATION.md)** – Command-line interface guide
- **[Configuration Guide](docs/cli/CONFIG_GUIDE.md)** – Configuration management

---

**Ezpl** – Modern, typed, robust and beautiful logging for Python. 🚀
