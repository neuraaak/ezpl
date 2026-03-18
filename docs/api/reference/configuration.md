# ConfigurationManager

Centralized configuration store that merges values from defaults, a JSON file, environment variables, and runtime updates.

## Overview

`ConfigurationManager` handles all configuration for ezplog. It is created automatically by `Ezpl` during initialization and is accessible via `Ezpl.get_config()`.

The manager tracks which keys were explicitly set (from file, environment, or runtime) versus which are simply falling back to defaults. This distinction is used by `Ezpl.reload_config()` to apply priority rules correctly.

You rarely need to use `ConfigurationManager` directly. Prefer `Ezpl.configure()` for runtime changes and environment variables for deployment-time configuration.

## Usage

```python
from ezplog import Ezpl

ezpl = Ezpl(log_file="app.log")
config = ezpl.get_config()

# Read current values
print(config.get_log_level())        # "INFO"
print(config.get_log_file())         # Path("app.log")
print(config.get_printer_level())    # "INFO"

# Check if a key was explicitly set (not just a default)
print(config.has_key("log-rotation"))  # False if not set explicitly

# Update at runtime
config.set("log-level", "DEBUG")
config.update({"printer-level": "WARNING", "indent-step": 4})

# Persist to ~/.ezpl/config.json
config.save()

# Reset to defaults (in-memory only)
config.reset_to_defaults()

# Export as environment variable script
config.export_to_script("export_env.sh", platform="unix")
config.export_to_script("export_env.bat", platform="windows")
```

### Runtime Configuration via Ezpl

For most use cases, prefer `Ezpl.configure()` which applies changes to the live handlers:

```python
from ezplog import Ezpl

ezpl = Ezpl(log_file="app.log")

# In-memory update (applies immediately to printer and logger)
ezpl.configure(printer_level="DEBUG", log_rotation="5 MB")

# Persist to disk
ezpl.configure(printer_level="DEBUG", persist=True)

# Change log file (reinitializes the logger)
ezpl.set_log_file("logs/app-v2.log")
```

## Configuration Keys Reference

All configuration keys in the JSON file and in `ConfigurationManager` use hyphen-separated names.

| Key                  | Type        | Default           | Description                                                                        |
| -------------------- | ----------- | ----------------- | ---------------------------------------------------------------------------------- |
| `log-level`          | str         | `"INFO"`          | Global level — applied to both printer and logger when specific levels are not set |
| `log-file`           | str         | `"ezpl.log"`      | Log file name (relative to `log-dir` if not absolute)                              |
| `log-dir`            | str         | platform-specific | Base directory for relative log file paths                                         |
| `printer-level`      | str         | `"INFO"`          | Console output minimum level                                                       |
| `file-logger-level`  | str         | `"INFO"`          | File output minimum level                                                          |
| `indent-step`        | int         | `3`               | Spaces per indentation level                                                       |
| `indent-symbol`      | str         | `">"`             | Symbol appended to indented lines                                                  |
| `base-indent-symbol` | str         | `"~"`             | Symbol shown at indent level 0                                                     |
| `log-rotation`       | str or null | `null`            | Rotation trigger: `"10 MB"`, `"1 day"`, `"12:00"`                                  |
| `log-retention`      | str or null | `null`            | Retention period: `"7 days"`, `"1 month"`                                          |
| `log-compression`    | str or null | `null`            | Compression format: `"zip"`, `"gz"`, `"tar.gz"`                                    |

## Class Reference

::: ezplog.config.manager.ConfigurationManager
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
