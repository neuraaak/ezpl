# Examples

Runnable ezplog scenarios for common integration patterns.

## 🚀 Basic application setup

```python
from ezplog import Ezpl

ezpl = Ezpl(log_file="app.log", hook_logger=True, hook_printer=True)

printer = ezpl.get_printer()
logger = ezpl.get_logger()

printer.info("Service started")
logger.info("Service started")
```

## 💡 Selective stdlib logger hooking

```python
import logging
from ezplog import Ezpl

ezpl = Ezpl(log_file="app.log", hook_logger=False, hook_printer=False)
ezpl.set_compatibility_hooks(hook_logger=True, logger_names=["vendor.payments"])

vendor_logger = logging.getLogger("vendor.payments")
vendor_logger.setLevel(logging.INFO)
vendor_logger.info("Payment flow initialized")
```

## 💡 Library-side passive mode

```python
from ezplog import get_logger, get_printer

logger = get_logger("my_library.module")
printer = get_printer()

logger.info("Library operation started")
printer.success("Library operation completed")
```

## 💡 Runtime update with persistence

```python
from ezplog import Ezpl

ezpl = Ezpl(log_file="app.log", hook_logger=True)
ezpl.configure(
    file_logger_level="DEBUG",
    log_rotation="10 MB",
    log_retention="7 days",
    persist=True,
)

ezpl.get_logger().debug("Runtime configuration persisted")
```
