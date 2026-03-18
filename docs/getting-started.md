# Getting Started

Install ezplog and get your first log messages in under 5 minutes.

## Installation

=== "pip"
`bash
    pip install ezplog
    `

=== "uv"
`bash
    uv add ezplog
    `

=== "From source"
`bash
    git clone https://github.com/neuraaak/ezplog.git
    cd ezplog
    pip install .
    `

**Requirements**: Python 3.11 or higher.

## Quickstart — App Mode

Use app mode when you are writing an **application** (script, service, CLI tool). Initialize `Ezpl` once at startup.

```python
from ezplog import Ezpl

# Initialize once. Subsequent Ezpl() calls return the same instance.
ezpl = Ezpl(log_file="app.log")

# Facade shortcuts — delegates to EzPrinter
ezpl.info("Application started")
ezpl.success("Ready")
ezpl.warning("Low memory")
ezpl.error("Connection refused")

# Access the console printer directly for more options
printer = ezpl.get_printer()
printer.tip("Use --debug for verbose output")
printer.system("Detected platform: Linux")

# Access the file logger
logger = ezpl.get_logger()
logger.info("Saved to file")
logger.debug("Detailed trace")
```

The console output uses the format `• PATTERN :: message`. The file uses structured lines:
`2026-03-18 10:00:00 | INFO       | module:function:42 - message`.

## Quickstart — Lib Mode

Use lib mode when you are writing a **library** that will be consumed by other applications. Your logger and printer stay silent until the host app initializes `Ezpl`.

```python
# my_library/core.py
from ezplog.lib_mode import get_logger, get_printer

log = get_logger(__name__)       # stdlib Logger with NullHandler
printer = get_printer()          # lazy proxy, silent by default

def process(items: list[str]) -> None:
    log.info("Processing %d items", len(items))       # silent without host config
    printer.success("Processing complete")             # silent without host config
```

When the host application calls `Ezpl(intercept_stdlib=True)`, all `log.*` calls are forwarded automatically. See [App Mode vs Lib Mode](explanations/dual-mode.md) for the full explanation.

## Configuration

### Constructor Arguments

All parameters are optional. Any parameter you omit is resolved from environment variables, the config file, or built-in defaults.

```python
from ezplog import Ezpl

ezpl = Ezpl(
    log_file="app.log",
    log_level="DEBUG",              # applies to both printer and logger
    printer_level="INFO",           # console only — overrides log_level
    file_logger_level="DEBUG",      # file only — overrides log_level
    log_rotation="10 MB",           # rotate when file reaches 10 MB
    log_retention="7 days",         # keep rotated files for 7 days
    log_compression="zip",          # compress rotated files
    indent_step=4,
    indent_symbol=">",
    base_indent_symbol="~",
    lock_config=True,               # prevent libraries from reconfiguring
    intercept_stdlib=True,          # capture stdlib logging.getLogger() calls
)
```

### Environment Variables

Set `EZPL_*` variables before your process starts.

| Variable                  | Purpose               | Default    |
| ------------------------- | --------------------- | ---------- |
| `EZPL_LOG_LEVEL`          | Global log level      | `INFO`     |
| `EZPL_LOG_FILE`           | Log file path         | `ezpl.log` |
| `EZPL_PRINTER_LEVEL`      | Console output level  | `INFO`     |
| `EZPL_FILE_LOGGER_LEVEL`  | File logger level     | `INFO`     |
| `EZPL_LOG_ROTATION`       | Rotation setting      | none       |
| `EZPL_LOG_RETENTION`      | Retention period      | none       |
| `EZPL_LOG_COMPRESSION`    | Compression format    | none       |
| `EZPL_INDENT_STEP`        | Indentation step size | `3`        |
| `EZPL_INDENT_SYMBOL`      | Indentation symbol    | `>`        |
| `EZPL_BASE_INDENT_SYMBOL` | Base indent symbol    | `~`        |

=== "Linux / macOS"
`bash
    export EZPL_LOG_LEVEL=DEBUG
    export EZPL_LOG_FILE=app.log
    export EZPL_LOG_ROTATION="10 MB"
    `

=== "Windows"
`bat
    set EZPL_LOG_LEVEL=DEBUG
    set EZPL_LOG_FILE=app.log
    set EZPL_LOG_ROTATION=10 MB
    `

### Configuration File

Create `~/.ezpl/config.json` with hyphenated keys:

```json
{
  "log-level": "INFO",
  "log-file": "app.log",
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

!!! warning "Key format"
Configuration file keys use hyphens (`log-level`), not underscores. Environment variables use underscores with the `EZPL_` prefix (`EZPL_LOG_LEVEL`).

### Priority Order

When the same setting is defined in multiple places, the resolution order is:

1. Constructor argument (highest priority)
2. Environment variable (`EZPL_*`)
3. Configuration file (`~/.ezpl/config.json`)
4. Built-in default (lowest priority)

## Pattern-Based Logging

`EzPrinter` supports semantic patterns beyond standard log levels. Each pattern maps to a fixed color in the console.

```python
from ezplog import Ezpl

ezpl = Ezpl()
printer = ezpl.get_printer()

printer.success("Operation completed")      # bright_green
printer.error("Connection failed")          # bright_red
printer.warning("Disk almost full")         # bright_yellow
printer.tip("Pass --verbose for details")   # bright_magenta
printer.system("Restarting service")        # bright_blue
printer.install("Installing dependency")    # bright_green
printer.detect("Found config at /etc/app")  # bright_blue
printer.config("Applied user settings")     # bright_green
printer.deps("Checking requirements")       # bright_cyan
```

## Indentation

Use indentation to visually group related log messages.

```python
from ezplog import Ezpl

ezpl = Ezpl()
printer = ezpl.get_printer()

printer.info("Starting deployment")

with ezpl.manage_indent():
    printer.info("Building image")
    with ezpl.manage_indent():
        printer.success("Layers cached")
    printer.info("Pushing to registry")

printer.success("Deployment complete")
```

The `manage_indent()` context manager increments the indentation level on entry and restores it on exit, even if an exception is raised.

## Advanced Display

### Panels

```python
from ezplog import Ezpl

ezpl = Ezpl()
printer = ezpl.get_printer()

printer.wizard.success_panel("Deployment complete", "All 3 services are healthy.")
printer.wizard.error_panel("Build failed", "Step 4 returned exit code 1.")
printer.wizard.info_panel("Release notes", "Version 2.0 — see changelog for details.")
```

### Tables

```python
from ezplog import Ezpl

ezpl = Ezpl()
printer = ezpl.get_printer()

services = [
    {"Service": "api-gateway", "Status": "healthy", "Uptime": "14d"},
    {"Service": "auth-service", "Status": "healthy", "Uptime": "14d"},
    {"Service": "worker", "Status": "degraded", "Uptime": "2h"},
]
printer.wizard.table(services, title="Service Status")
```

### JSON

```python
from ezplog import Ezpl

ezpl = Ezpl()
printer = ezpl.get_printer()

config = {
    "database": {"host": "localhost", "port": 5432},
    "cache": {"ttl": 300},
}
printer.print_json(config, title="Active configuration")
```

### Progress Bars

```python
import time
from ezplog import Ezpl

ezpl = Ezpl()
printer = ezpl.get_printer()

with printer.wizard.progress("Uploading artifacts", total=100) as (progress, task):
    for _ in range(100):
        time.sleep(0.02)
        progress.update(task, advance=1)
```

## Config Lock

To prevent any library from reconfiguring `Ezpl` after your application has initialized it:

```python
from ezplog import Ezpl

# lock_config=True locks configuration immediately after init
ezpl = Ezpl(log_file="app.log", lock_config=True)

# The token is stored on the class if you need to unlock later
token = Ezpl._config_lock_token

# To unlock (e.g., for testing or controlled reconfiguration)
Ezpl.unlock_config(token)
```

Any call to `configure()`, `set_level()`, or similar methods while locked produces a `UserWarning` and is silently ignored.

## Next Steps

- [App Mode vs Lib Mode](explanations/dual-mode.md) — understand when to use each
- [API Reference](api/index.md) — complete method reference for all classes
- [CLI Reference](cli/index.md) — use the `ezplog` command-line tool
- [Configuration Guide](guides/configuration.md) — full configuration reference
