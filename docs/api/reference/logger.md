# EzLogger

loguru-based file logging handler with rotation, retention, compression, and structured output.

## Overview

`EzLogger` (alias: `Logger`) writes structured log lines to a file using loguru as the backend. Each line includes a timestamp, level label, source location, and message.

Log format:

```text
2026-03-18 10:00:00 | INFO       | module:function:42 - message
```

`EzLogger` is normally obtained through `Ezpl.get_logger()`. It does **not** write to the console. For console output, use `EzPrinter`.

The parent directory for the log file is created automatically on initialization.

## Usage

```python
from ezplog import Ezpl

ezpl = Ezpl(
    log_file="logs/app.log",
    file_logger_level="DEBUG",
    log_rotation="10 MB",
    log_retention="30 days",
    log_compression="zip",
)
logger = ezpl.get_logger()

# Standard log levels
logger.debug("Cache miss for key: user-42")
logger.info("Request processed in 42ms")
logger.success("Order #1234 confirmed")
logger.warning("Retry attempt 2 of 3")
logger.error("Failed to connect to database")
logger.critical("Out of disk space")

# Exception with traceback
try:
    result = 1 / 0
except ZeroDivisionError:
    logger.exception("Unexpected division error")

# Session separator — visual marker in the log file
logger.add_separator()
```

### Rotation Settings

```python
from ezplog import Ezpl

# Rotate by size
ezpl = Ezpl(log_file="app.log", log_rotation="10 MB")

# Rotate by time
ezpl = Ezpl(log_file="app.log", log_rotation="1 day")

# Rotate at a specific time
ezpl = Ezpl(log_file="app.log", log_rotation="12:00")
```

### Advanced loguru Features

Access the underlying loguru logger for structured logging or log binding:

```python
from ezplog import Ezpl

ezpl = Ezpl(log_file="app.log")
logger = ezpl.get_logger()

# Bind context variables to all subsequent records
bound_logger = logger.bind(request_id="abc-123", user="alice")
bound_logger.info("Processing request")

# Access raw loguru for opt() / patch()
loguru_logger = logger.get_loguru()
loguru_logger.opt(exception=True).error("Caught exception")
```

## Class Reference

::: ezplog.handlers.file.EzLogger
options:
show_source: false
show_root_heading: true
show_root_full_path: false
show_symbol_type_heading: true
show_symbol_type_toc: true
members_order: source
group_by_category: true
show_category_heading: true
show_if_no_docstring: false
show_signature_annotations: true
separate_signature: true
signature_crossrefs: true
merge_init_into_class: true
docstring_style: google
docstring_section_style: table

## Default Log Location

When no `log_file` argument is given to `Ezpl()`, the log file path is resolved as follows:

| Platform | Default path                                       |
| -------- | -------------------------------------------------- |
| Windows  | `%APPDATA%\ezpl\logs\ezpl.log`                     |
| macOS    | `~/Library/Application Support/ezpl/logs/ezpl.log` |
| Linux    | `~/.local/share/ezpl/logs/ezpl.log`                |

Pass an explicit path to `Ezpl(log_file=...)` or set `EZPL_LOG_FILE` to override.
