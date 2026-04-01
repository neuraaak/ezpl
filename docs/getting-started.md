# Getting started

Build a working ezplog setup in less than 5 minutes.

## 🔧 Prerequisites

- Python 3.11 or higher
- A project where you can run Python scripts

## 📝 Steps

1. Install ezplog.

```bash
pip install ezplog
```

1. Initialize app mode once.

```python
from ezplog import Ezpl

ezpl = Ezpl(
    log_file="app.log",
    hook_logger=True,
    hook_printer=True,
)

ezpl.info("Application started")
ezpl.get_printer().success("Ready")
ezpl.get_logger().info("Written to app.log")
```

1. Verify library compatibility.

```python
from ezplog.lib_mode import get_logger, get_printer

library_logger = get_logger("demo.library")
library_printer = get_printer()

library_logger.info("Library logger message")
library_printer.success("Library printer message")
```

## ✅ Result

You now have one app-level logging configuration with unified console and file output.
Library loggers and printers are routed through explicit compatibility hooks.

## ➡️ Next steps

- [How to configure compatibility hooks](guides/configuration.md)
- [How to contribute changes locally](guides/development.md)
- [How to run and extend tests](guides/testing.md)
- [App mode vs lib mode](explanations/dual-mode.md)
- [Ezpl API](api/reference/ezpl.md)
