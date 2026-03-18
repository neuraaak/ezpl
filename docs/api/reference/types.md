# Types and Enums

Type definitions, enumerations, and protocols exported from `ezplog`.

## LogLevel

`LogLevel` maps log level names to their numeric priority and display colors. Use it when you need to compare levels programmatically or pass a typed level value.

```python
from ezplog import LogLevel

# Access a level
level = LogLevel.INFO
print(level.label)   # "INFO"
print(level.no)      # 20

# Validate user input
if not LogLevel.is_valid_level("VERBOSE"):
    print("Unknown level")

# Get all available levels
print(LogLevel.get_all_levels())
# ['DEBUG', 'INFO', 'SUCCESS', 'WARNING', 'ERROR', 'CRITICAL']
```

### Level Reference

| Name       | Numeric | Rich Style          |
| ---------- | ------- | ------------------- |
| `DEBUG`    | 10      | cyan                |
| `INFO`     | 20      | blue                |
| `SUCCESS`  | 25      | bold green          |
| `WARNING`  | 30      | bold yellow         |
| `ERROR`    | 40      | bold red            |
| `CRITICAL` | 50      | bold magenta on red |

::: ezplog.types.enums.log_level.LogLevel
options:
show_source: false
show_root_heading: true
show_root_full_path: false
show_symbol_type_heading: true
members_order: source
show_if_no_docstring: false
show_signature_annotations: true
separate_signature: true
docstring_style: google
docstring_section_style: table

---

## Pattern

`Pattern` provides semantic meaning beyond log levels. Each pattern maps to a fixed Rich color string used by `EzPrinter.print_pattern()`.

```python
from ezplog import Ezpl, Pattern

ezpl = Ezpl()
printer = ezpl.get_printer()

# Use a pattern enum directly
printer.print_pattern(Pattern.TIP, "Enable caching for better performance")
printer.print_pattern(Pattern.INSTALL, "Installing dependency: requests")
```

### Pattern Reference

| Name      | Output label | Color          |
| --------- | ------------ | -------------- |
| `SUCCESS` | SUCCESS      | bright_green   |
| `ERROR`   | ERROR        | bright_red     |
| `WARN`    | WARN         | bright_yellow  |
| `TIP`     | TIP          | bright_magenta |
| `DEBUG`   | DEBUG        | dim white      |
| `INFO`    | INFO         | bright_blue    |
| `SYSTEM`  | SYSTEM       | bright_blue    |
| `INSTALL` | INSTALL      | bright_green   |
| `DETECT`  | DETECT       | bright_blue    |
| `CONFIG`  | CONFIG       | bright_green   |
| `DEPS`    | DEPS         | bright_cyan    |

::: ezplog.types.enums.patterns.Pattern
options:
show_source: false
show_root_heading: true
show_root_full_path: false
show_symbol_type_heading: true
members_order: source
show_if_no_docstring: false
show_signature_annotations: true
separate_signature: true
docstring_style: google
docstring_section_style: table

---

## Pattern Color Utilities

::: ezplog.types.enums.patterns.get_pattern_color
options:
show_source: false
show_root_heading: true
show_signature_annotations: true
separate_signature: true
docstring_style: google
docstring_section_style: table

::: ezplog.types.enums.patterns.get_pattern_color_by_name
options:
show_source: false
show_root_heading: true
show_signature_annotations: true
separate_signature: true
docstring_style: google
docstring_section_style: table

---

## Protocols

Protocols allow type-safe use of ezplog components without importing the concrete classes. Useful in library code or when injecting custom implementations.

```python
from ezplog import PrinterProtocol, LoggerProtocol

def setup_reporting(printer: PrinterProtocol, logger: LoggerProtocol) -> None:
    printer.info("Report started")
    logger.info("Report started")
```

::: ezplog.types.protocols.printer_protocol.PrinterProtocol
options:
show_source: false
show_root_heading: true
show_root_full_path: false
show_symbol_type_heading: true
members_order: source
show_if_no_docstring: false
show_signature_annotations: true
separate_signature: true
docstring_style: google
docstring_section_style: table

::: ezplog.types.protocols.logger_protocol.LoggerProtocol
options:
show_source: false
show_root_heading: true
show_root_full_path: false
show_symbol_type_heading: true
members_order: source
show_if_no_docstring: false
show_signature_annotations: true
separate_signature: true
docstring_style: google
docstring_section_style: table

---

## Type Aliases

```python
from ezplog import Printer, Logger
```

| Alias     | Resolves to | Use                                   |
| --------- | ----------- | ------------------------------------- |
| `Printer` | `EzPrinter` | Type annotation for printer variables |
| `Logger`  | `EzLogger`  | Type annotation for logger variables  |

```python
from ezplog import Ezpl, Printer, Logger

ezpl = Ezpl()
printer: Printer = ezpl.get_printer()
logger: Logger = ezpl.get_logger()
```
