# API Reference (Auto-Generated)

Complete API reference generated from source code docstrings using [mkdocstrings](https://mkdocstrings.github.io/).

## Classes

| Class                                    | Description                                                |
| ---------------------------------------- | ---------------------------------------------------------- |
| [Ezpl](ezpl.md)                          | Thread-safe singleton — the single entry point for logging |
| [EzPrinter](printer.md)                  | Rich-based console output with pattern formatting          |
| [EzLogger](logger.md)                    | loguru-based file logging with rotation support            |
| [RichWizard](wizard.md)                  | Advanced Rich display: panels, tables, JSON, progress bars |
| [ConfigurationManager](configuration.md) | Configuration from args, env vars, file, and defaults      |

## Types and Exceptions

| Page                        | Description                                                                                |
| --------------------------- | ------------------------------------------------------------------------------------------ |
| [Types and Enums](types.md) | `LogLevel`, `Pattern`, `PATTERN_COLORS`, `PrinterProtocol`, `LoggerProtocol`, type aliases |
| [Exceptions](exceptions.md) | Full exception hierarchy rooted at `EzplError`                                             |

## Lib Mode Functions

For library authors — passive proxies that stay silent until the host application initializes `Ezpl`:

```python
from ezplog.lib_mode import get_logger, get_printer
# or equivalently:
from ezplog import get_logger, get_printer

log = get_logger(__name__)   # stdlib Logger with NullHandler
printer = get_printer()      # _LazyPrinter proxy
```

See [App Mode vs Lib Mode](../../explanations/dual-mode.md) for the full explanation.
