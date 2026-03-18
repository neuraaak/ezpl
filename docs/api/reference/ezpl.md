# Ezpl

The thread-safe singleton that is the single entry point for all logging in an ezplog-based application.

## Overview

`Ezpl` manages one `EzPrinter` (console) and one `EzLogger` (file) for the lifetime of the process. The first call to `Ezpl(...)` creates and configures the instance; every subsequent call returns the same object and ignores all arguments.

`Ezpl` does **not** replace stdlib `logging` by default. Pass `intercept_stdlib=True` to capture records from libraries that use `logging.getLogger(__name__)`.

## Usage

```python
from ezplog import Ezpl

# App-level initialization — do this once, at startup
ezpl = Ezpl(
    log_file="app.log",
    log_level="INFO",
    log_rotation="10 MB",
    log_retention="7 days",
    intercept_stdlib=True,
    lock_config=True,
)

# Facade shortcuts (console only)
ezpl.info("Application started")
ezpl.success("Ready")
ezpl.warning("High memory usage")
ezpl.error("Connection refused")

# Access handlers directly for full API
printer = ezpl.get_printer()
logger = ezpl.get_logger()

printer.tip("Use --debug for verbose output")
logger.debug("Detailed trace saved to file")

# Contextual indentation
with ezpl.manage_indent():
    ezpl.info("Indented step")
```

## Class Reference

::: ezplog.ezpl.Ezpl
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

## Configuration Lock

The configuration lock prevents library code from overriding your application's logging setup after startup.

```python
from ezplog import Ezpl

# Option 1: lock during initialization (recommended)
ezpl = Ezpl(log_file="app.log", lock_config=True)
token = Ezpl._config_lock_token

# Option 2: lock manually
ezpl = Ezpl(log_file="app.log")
token = Ezpl.lock_config()

# Unlock when needed
success = Ezpl.unlock_config(token)  # True if token matches
```

When locked, calls to `configure()`, `set_level()`, `set_printer_level()`, and `set_logger_level()` emit a `UserWarning` and return without applying changes.

## Custom Handlers

Replace the default `EzPrinter` or `EzLogger` with a custom subclass:

```python
from ezplog import Ezpl, EzPrinter

class TimestampPrinter(EzPrinter):
    def info(self, message):
        from datetime import datetime
        super().info(f"[{datetime.now():%H:%M:%S}] {message}")

ezpl = Ezpl()
ezpl.set_printer_class(TimestampPrinter, level="DEBUG")
ezpl.get_printer().info("Hello")
# • INFO     :: [10:00:00] Hello
```

`set_printer_class()` and `set_logger_class()` accept either a class (which will be instantiated with current configuration values) or a pre-built instance.
