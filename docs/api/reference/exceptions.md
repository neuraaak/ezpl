# Exceptions

Exception hierarchy for structured error handling in ezplog.

## Overview

All ezplog exceptions inherit from `EzplError`. Each exception carries a `message` (human-readable) and an `error_code` (machine-readable category). Subclasses add context-specific attributes to help identify the source of the error.

```python
from ezplog import EzplError, ValidationError, ConfigurationError

try:
    from ezplog import Ezpl
    ezpl = Ezpl(log_level="INVALID")
except ValidationError as exc:
    print(exc)              # [VALIDATION_ERROR] Invalid log level: INVALID
    print(exc.field_name)   # "level"
    print(exc.value)        # "INVALID"
except EzplError as exc:
    print(exc.error_code)   # fallback for any other ezplog error
```

## Hierarchy

```text
EzplError (base)
├── ConfigurationError   CONFIG_ERROR   — config load / validation failure
├── LoggingError         LOGGING_ERROR  — file write / handler init failure
├── ValidationError      VALIDATION_ERROR — invalid input (levels, patterns)
├── InitializationError  INIT_ERROR     — component startup failure
├── FileOperationError   FILE_ERROR     — read / write / create failure
└── HandlerError         HANDLER_ERROR  — handler operation failure
```

## Base Exception

::: ezplog.core.exceptions.EzplError
options:
show_source: false
show_root_heading: true
show_root_full_path: false
show_symbol_type_heading: true
members_order: source
show_if_no_docstring: false
show_signature_annotations: true
separate_signature: true
merge_init_into_class: true
docstring_style: google
docstring_section_style: table

## Specific Exceptions

### ConfigurationError

Raised when configuration loading or validation fails (e.g., corrupted `config.json`). The optional `config_key` attribute names the problematic configuration key.

::: ezplog.core.exceptions.ConfigurationError
options:
show_source: false
show_root_heading: false
members_order: source
show_signature_annotations: true
separate_signature: true
merge_init_into_class: true
docstring_style: google
docstring_section_style: table

### LoggingError

Raised when a log write or handler initialization fails. The optional `handler_type` attribute is `"file"` or `"console"`.

::: ezplog.core.exceptions.LoggingError
options:
show_source: false
show_root_heading: false
members_order: source
show_signature_annotations: true
separate_signature: true
merge_init_into_class: true
docstring_style: google
docstring_section_style: table

### ValidationError

Raised when a caller passes an invalid value (e.g., an unrecognized log level string). The `field_name` and `value` attributes identify what failed validation.

::: ezplog.core.exceptions.ValidationError
options:
show_source: false
show_root_heading: false
members_order: source
show_signature_annotations: true
separate_signature: true
merge_init_into_class: true
docstring_style: google
docstring_section_style: table

### InitializationError

Raised when a component fails to start. The `component` attribute names the component (`"printer"`, `"logger"`, `"config"`).

::: ezplog.core.exceptions.InitializationError
options:
show_source: false
show_root_heading: false
members_order: source
show_signature_annotations: true
separate_signature: true
merge_init_into_class: true
docstring_style: google
docstring_section_style: table

### FileOperationError

Raised when a file cannot be read, written, or created. The `file_path` and `operation` attributes identify which file and operation failed.

::: ezplog.core.exceptions.FileOperationError
options:
show_source: false
show_root_heading: false
members_order: source
show_signature_annotations: true
separate_signature: true
merge_init_into_class: true
docstring_style: google
docstring_section_style: table

### HandlerError

Raised when a handler operation fails outside of normal logging flow. The `handler_name` attribute identifies the handler (`"EzPrinter"`, `"EzLogger"`).

::: ezplog.core.exceptions.HandlerError
options:
show_source: false
show_root_heading: false
members_order: source
show_signature_annotations: true
separate_signature: true
merge_init_into_class: true
docstring_style: google
docstring_section_style: table
