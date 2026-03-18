# RichWizard

Advanced Rich display capabilities: panels, tables, JSON, and progress bars.

## Overview

`RichWizard` provides methods for structured visual output beyond plain log lines. It is always accessed through `EzPrinter.wizard` — it shares the same `Console` instance as the printer and should not be instantiated directly.

`RichWizard` does **not** perform log-level filtering. Its methods always produce output when called. To suppress output, control the `EzPrinter` level instead.

## Usage

```python
from ezplog import Ezpl

ezpl = Ezpl()
wizard = ezpl.get_printer().wizard

# Panels
wizard.success_panel("Deployment complete", "3 services healthy, 0 warnings.")
wizard.error_panel("Build failed", "Step 4 returned exit code 1.")
wizard.info_panel("Release notes", "Version 2.0 — breaking changes in the API.")

# Tables
wizard.table(
    [
        {"Service": "api-gateway", "Status": "UP", "Latency": "12ms"},
        {"Service": "auth-service", "Status": "UP", "Latency": "8ms"},
        {"Service": "worker", "Status": "DOWN", "Latency": "—"},
    ],
    title="Service Status",
)

# JSON
wizard.json(
    {"database": {"host": "localhost", "port": 5432}, "cache": {"ttl": 300}},
    title="Active configuration",
)

# Progress bar
import time

with wizard.progress("Uploading artifacts", total=50) as (progress, task):
    for _ in range(50):
        time.sleep(0.05)
        progress.update(task, advance=1)
```

## Via EzPrinter Convenience Methods

`EzPrinter` exposes three shortcut methods that delegate to `wizard`:

```python
from ezplog import Ezpl

ezpl = Ezpl()
printer = ezpl.get_printer()

# Equivalent to printer.wizard.table(...)
printer.print_table(
    [{"Name": "Alice", "Role": "admin"}],
    title="Users",
)

# Equivalent to printer.wizard.panel(...)
printer.print_panel("Hello world", title="Message", style="blue")

# Equivalent to printer.wizard.json(...)
printer.print_json({"key": "value"}, title="Config")
```

## Class Reference

::: ezplog.handlers.wizard.core.RichWizard
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
