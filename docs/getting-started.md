# Getting started

Build a working ezplog setup in less than 5 minutes.

## 🔧 Prerequisites

- Python 3.11 or higher
- A project where you can run Python scripts

## 📝 Steps

### 1. Install ezplog

=== "pip"

    ```bash
    pip install ezplog
    ```

=== "uv"

    ```bash
    uv add ezplog
    ```

### 2. Initialize app mode once

```python
from ezplog import Ezpl

ezpl = Ezpl(
    log_file="app.log",  # (1)!
    hook_logger=True,  # (2)!
    hook_printer=True,  # (3)!
)

ezpl.info("Application started")
ezpl.get_printer().success("Ready")
ezpl.get_logger().info("Written to app.log")
```

1. Creates the file sink destination.
2. Routes stdlib loggers into the unified pipeline.
3. Allows lazy library printers to delegate to the active `EzPrinter`.

### 3. Verify library compatibility

=== "Host app already initialized"

    ```python
    from ezplog.lib_mode import get_logger, get_printer

    library_logger = get_logger("demo.library")
    library_printer = get_printer()

    library_logger.info("Library logger message")
    library_printer.success("Library printer message")
    ```

=== "Library package only"

    ```python
    from ezplog.lib_mode import get_logger

    logger = get_logger("demo.library")
    logger.info("Silent by default until host app initializes Ezpl")
    ```

??? tip "✅ Success check"
    You should see one console message and one log entry in `app.log`.

## ✅ What you built

You now have one app-level logging configuration with unified console and file output.
Library loggers and printers are routed through explicit compatibility hooks.

## ➡️ Next steps

- [How to configure compatibility hooks](guides/configuration.md)
- [How to contribute changes locally](guides/development.md)
- [How to run and extend tests](guides/testing.md)
- [App mode vs lib mode](concepts/dual-mode.md)
- [Ezpl API](api/reference/ezpl.md)
