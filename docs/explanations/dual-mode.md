# App Mode vs Lib Mode

This page answers one question: **which usage mode should I use for my code?**

## The Rule

> If your code is an **application** (a script, a service, a CLI tool, anything with a `main` entry point), use **app mode**.
>
> If your code is a **library** (a package consumed by other developers' applications), use **lib mode**.

The distinction matters because logging is a cross-cutting concern: when multiple libraries each configure their own logger independently, they conflict. Python's official recommendation is that libraries should never configure logging — they should only emit records and let the host application decide where those records go.

ezplog enforces this cleanly through its two modes.

## Comparison

|                           | App mode                  | Lib mode                                              |
| ------------------------- | ------------------------- | ----------------------------------------------------- |
| **Who uses it**           | Application authors       | Library authors                                       |
| **Entry point**           | `from ezplog import Ezpl` | `from ezplog.lib_mode import get_logger, get_printer` |
| **What it returns**       | Configured singleton      | Passive proxy / stdlib logger                         |
| **Silent by default**     | No — logs immediately     | Yes — no-op until app initializes `Ezpl`              |
| **Configures logging**    | Yes                       | Never                                                 |
| **Survives without host** | Yes                       | Yes (silently discards all output)                    |
| **Type**                  | `Ezpl` singleton          | `logging.Logger` + `_LazyPrinter` proxy               |

## App Mode — Full Example

An application configures `Ezpl` once at startup. All subsequent calls within the process return the same singleton.

```python
# my_app/main.py
from ezplog import Ezpl

def main() -> None:
    # Configure once. This is the single initialization point.
    ezpl = Ezpl(
        log_file="app.log",
        log_level="INFO",
        log_rotation="10 MB",
        log_retention="7 days",
        intercept_stdlib=True,   # capture library loggers automatically
        lock_config=True,        # prevent libraries from reconfiguring
    )

    ezpl.info("Application started")

    # From here on, any library using lib_mode will also produce output
    from my_app.services import DataService
    service = DataService()
    service.run()

if __name__ == "__main__":
    main()
```

### intercept_stdlib

When `intercept_stdlib=True`, ezplog installs an `InterceptHandler` on the root stdlib logger. This means any code — including third-party libraries — that uses `logging.getLogger(__name__)` will have its records forwarded to the loguru pipeline (and thus into `EzLogger`).

This is the recommended way to unify all log output in your application.

### lock_config

When `lock_config=True`, the configuration is locked immediately after `Ezpl()` returns. Any subsequent call to `configure()`, `set_level()`, or similar methods — including those originating from library code — issues a `UserWarning` and is silently ignored. The lock token is stored at `Ezpl._config_lock_token`.

```python
token = Ezpl._config_lock_token   # save if you need to unlock later
Ezpl.unlock_config(token)          # returns True on success
```

## Lib Mode — Full Example

A library never configures logging. It uses passive proxies that become active only when the host application has initialized `Ezpl`.

```python
# my_library/service.py
from ezplog.lib_mode import get_logger, get_printer

# Both of these are safe to call at module level — no side effects
log = get_logger(__name__)       # stdlib Logger with NullHandler attached
printer = get_printer()          # lazy EzPrinter proxy

class DataService:
    def run(self) -> None:
        log.info("DataService starting")          # forwarded if app uses intercept_stdlib=True
        printer.system("DataService ready")        # forwarded if app initialized Ezpl

        try:
            self._process()
        except Exception:
            log.exception("DataService failed")
            printer.error("DataService encountered a fatal error")
            raise

    def _process(self) -> None:
        log.debug("Processing records")
        printer.info("Processing...")
```

### What happens without a host app

If this library is imported in isolation (no `Ezpl` initialization by any caller):

- `log.info(...)` — silently discarded by the `NullHandler`
- `printer.system(...)` — silently discarded by the `_LazyPrinter` proxy

No output, no configuration, no errors. This matches the Python recommendation for library logging.

### What happens with a host app

If the host application calls `Ezpl(intercept_stdlib=True)` before calling library code:

- `log.info(...)` — captured by `InterceptHandler` and forwarded to loguru / `EzLogger`
- `printer.system(...)` — forwarded to the real `EzPrinter`

The library code requires zero changes.

## Limitations

### Silent failures are intentional

In lib mode, a missing `Ezpl` initialization produces no error and no output. This is by design: a library must not crash or print warnings if the host app does not use ezplog. Test your library code with an explicit `Ezpl()` call in your test fixtures to verify output.

### intercept_stdlib captures all stdlib loggers

When `intercept_stdlib=True`, the `InterceptHandler` is installed on the **root** stdlib logger. This captures records from every library that uses `logging.getLogger(__name__)`, not just those using ezplog's lib mode. If you need fine-grained control, install `InterceptHandler` manually on a specific logger:

```python
import logging
from ezplog import InterceptHandler

# Only intercept records from my_library, not everything
logging.getLogger("my_library").addHandler(InterceptHandler())
```

### Multiprocess environments

The `Ezpl` singleton is process-local. In a multiprocess setup (e.g., `multiprocessing`, `gunicorn` workers), each worker process must initialize `Ezpl` independently. File-based logging with rotation is handled by loguru and is safe for single-writer scenarios. For multi-writer scenarios, point each worker to a different log file or use a centralized log aggregator.

### The singleton cannot be re-initialized

Once `Ezpl()` has been called in a process, subsequent `Ezpl()` calls return the existing instance and ignore all arguments. To change configuration at runtime, use `ezpl.configure(...)` or `ezpl.set_log_file(...)` instead. To force a fresh initialization (tests only), call `Ezpl.reset()`.

```python
# In tests — reset between test cases
import pytest
from ezplog import Ezpl

@pytest.fixture(autouse=True)
def reset_ezpl():
    yield
    Ezpl.reset()
```
