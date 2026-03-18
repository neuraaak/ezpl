# EzPrinter

Rich-based console output handler with pattern formatting, indentation management, and access to advanced display features.

## Overview

`EzPrinter` (alias: `Printer`) renders all console output via Rich. Every message uses the format `• PATTERN :: message`, where the pattern determines the color. Indentation is inserted between `::` and the message text.

`EzPrinter` is normally obtained through `Ezpl.get_printer()`. You can also use it standalone or inject a custom subclass via `Ezpl.set_printer_class()`.

`EzPrinter` does **not** write to files. For file output, use `EzLogger`.

## Usage

```python
from ezplog import Ezpl

ezpl = Ezpl()
printer = ezpl.get_printer()

# Standard log levels
printer.debug("Entering handler")
printer.info("Request received")
printer.success("Order processed")
printer.warning("Response time above threshold")
printer.error("Database unavailable")
printer.critical("Out of memory — halting")

# Semantic patterns
printer.tip("Enable caching to improve performance")
printer.system("Detected OS: Linux")
printer.install("Installing requests==2.31.0")
printer.detect("Found .env at /home/user/project")
printer.config("Using profile: production")
printer.deps("Checking numpy >= 1.26")

# Generic pattern dispatch
from ezplog import Pattern
printer.print_pattern(Pattern.SUCCESS, "Build passed", level="INFO")

# JSON display
printer.print_json({"host": "localhost", "port": 5432}, title="DB config")

# Table display
printer.print_table(
    [{"Package": "rich", "Version": "13.7"}, {"Package": "loguru", "Version": "0.7"}],
    title="Installed packages",
)

# Panel display
printer.print_panel("All systems operational.", title="Status", style="green")

# Access RichWizard for advanced features
printer.wizard.success_panel("Build complete", "4 targets built in 2.3s")
printer.wizard.table([{"File": "main.py", "Lines": 120}], title="Changed files")
```

## Indentation

```python
from ezplog import Ezpl

ezpl = Ezpl()
printer = ezpl.get_printer()

printer.info("Starting migration")

with printer.manage_indent():          # enters indent level 1
    printer.info("Applying schema v3")
    with printer.manage_indent():      # enters indent level 2
        printer.success("Table users updated")
        printer.success("Table orders updated")
    printer.info("Verifying integrity")

printer.success("Migration complete")
```

The context manager is re-entrant: nesting `manage_indent()` calls stacks indentation levels up to a maximum of 10.

## Class Reference

::: ezplog.handlers.console.EzPrinter
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

## Pattern Reference

| Method       | Pattern   | Color          |
| ------------ | --------- | -------------- |
| `info()`     | `INFO`    | bright_blue    |
| `debug()`    | `DEBUG`   | dim white      |
| `success()`  | `SUCCESS` | bright_green   |
| `warning()`  | `WARN`    | bright_yellow  |
| `error()`    | `ERROR`   | bright_red     |
| `critical()` | `ERROR`   | bright_red     |
| `tip()`      | `TIP`     | bright_magenta |
| `system()`   | `SYSTEM`  | bright_blue    |
| `install()`  | `INSTALL` | bright_green   |
| `detect()`   | `DETECT`  | bright_blue    |
| `config()`   | `CONFIG`  | bright_green   |
| `deps()`     | `DEPS`    | bright_cyan    |

!!! note
`critical()` reuses the `ERROR` pattern and color. The distinction between `error` and `critical` is filtered by the log level numeric value, not by the visual pattern.
