# Test Documentation – Ezpl

## Overview

This document provides comprehensive documentation for the **Ezpl** test suite. The test suite ensures reliability, robustness, and correctness of all Ezpl components through unit tests, integration tests, and robustness tests.

## General Overview

The Ezpl test suite is organized into three main categories:

- **Unit Tests** – Individual component testing with isolated test cases
- **Integration Tests** – Component interaction and integration scenarios
- **Robustness Tests** – Edge cases, error handling, and special character scenarios

## Test Structure

### Directory Organization

```
tests/
├── conftest.py          # Shared fixtures and pytest configuration
├── pytest.ini          # Pytest configuration and markers
├── run_tests.py        # Test runner script
├── unit/               # Unit tests
│   ├── test_ezpl.py
│   ├── test_printer.py
│   ├── test_logger.py
│   ├── test_wizard.py
│   ├── test_config.py
│   ├── test_types.py
│   ├── test_exceptions.py
│   └── test_utils.py
├── integration/        # Integration tests
│   ├── test_ezpl_integration.py
│   ├── test_config_integration.py
│   └── test_cli_integration.py
└── robustness/         # Robustness tests
    ├── test_special_chars.py
    ├── test_error_handling.py
    └── test_edge_cases.py
```

---

## Unit Tests

### `test_ezpl.py` – Ezpl Core Tests

**Location:** `tests/unit/test_ezpl.py`

**Test Classes:**

#### `TestSingleton`

- `test_singleton_returns_same_instance` – Verifies singleton pattern
- `test_reset_creates_new_instance` – Verifies reset functionality

#### `TestInitialization`

- `test_initialization_with_defaults` – Default initialization
- `test_initialization_with_log_file` – Custom log file
- `test_initialization_with_log_level` – Global log level
- `test_initialization_with_printer_level` – Printer-specific level
- `test_initialization_with_file_logger_level` – Logger-specific level
- `test_initialization_with_all_parameters` – All parameters

#### `TestConfigurationPriority`

- `test_argument_priority` – Arguments override defaults
- `test_environment_priority` – Environment variables priority
- `test_file_priority` – Config file priority
- `test_default_priority` – Default values fallback

#### `TestLevelManagement`

- `test_set_level` – Global level setting
- `test_set_printer_level` – Printer level setting
- `test_set_logger_level` – Logger level setting
- `test_invalid_level` – Invalid level handling

#### `TestFileOperations`

- `test_set_log_file` – Change log file
- `test_get_log_file` – Get log file path
- `test_add_separator` – Add separator to log file

#### `TestIndentation`

- `test_manage_indent` – Context manager indentation
- `test_nested_indent` – Nested indentation levels

#### `TestConfiguration`

- `test_get_config` – Get configuration manager
- `test_configure` – Runtime configuration
- `test_reload_config` – Reload from file/env

#### `TestGetters`

- `test_get_printer` – Get printer instance
- `test_get_logger` – Get logger instance

#### `TestErrorHandling`

- `test_invalid_log_level` – Invalid level error
- `test_invalid_config_key` – Invalid config key
- `test_invalid_file_path` – Invalid file path

### `test_printer.py` – ConsolePrinter Tests

**Location:** `tests/unit/test_printer.py`

**Test Classes:**

#### `TestLogLevels`

- All log level methods (debug, info, success, warning, error, critical)

#### `TestPatternMethods`

- Pattern methods (tip, system, install, detect, config, deps, print_pattern)

#### `TestIndentation`

- Indentation management (get_indent, add_indent, del_indent, reset_indent, manage_indent)
- Maximum indent limit
- Indentation with messages

#### `TestRichFeatures`

- `print_table` – Table display
- `print_panel` – Panel display
- `print_json` – JSON display
- `wizard` property – RichWizard access

#### `TestSpecialCharacters`

- Windows paths
- Braces and tags
- Unicode characters
- ANSI escape sequences

#### `TestTypeConversion`

- Dict, int, list, exception, None, custom objects as messages

### `test_logger.py` – FileLogger Tests

**Location:** `tests/unit/test_logger.py`

**Test Classes:**

#### `TestLogLevels`

- All log levels (debug, info, warning, error, critical, set_level)

#### `TestFileRotation`

- `rotation_by_size` – Size-based rotation
- `rotation_by_time` – Time-based rotation
- `rotation_by_date` – Date-based rotation
- `rotation_at_time` – Time-of-day rotation

#### `TestRetention`

- `retention_by_duration` – Duration-based retention
- `retention_by_count` – Count-based retention

#### `TestCompression`

- `compression_zip` – ZIP compression
- `compression_gz` – GZ compression
- `compression_tar_gz` – TAR.GZ compression

#### `TestSeparators`

- `add_separator` – Add separator to log file
- `separator_with_ezpl` – Separator with Ezpl integration

#### `TestFileOperations`

- `get_log_file` – Get log file path
- `get_file_size` – Get file size
- `get_file_size_empty_file` – Empty file size

#### `TestSpecialCharacters`

- Unicode characters
- Control characters
- HTML tags

#### `TestTypeConversion`

- Exception messages
- Dict messages
- List messages

#### `TestErrorHandling`

- Invalid directory permissions
- File write errors

#### `TestDirectoryCreation`

- Creating parent directories
- Handling existing directories

### `test_wizard.py` – RichWizard Tests

**Location:** `tests/unit/test_wizard.py`

**Test Classes:**

#### `TestPanels`

- `panel` – Generic panel
- `info_panel` – Info panel
- `success_panel` – Success panel
- `error_panel` – Error panel
- `warning_panel` – Warning panel
- `installation_panel` – Installation panel with different statuses

#### `TestTables`

- `table` – Generic table
- `table_from_columns` – Table from columns
- `status_table` – Status table
- `dependency_table` – Dependency table
- `command_table` – Command table
- Empty data handling

#### `TestJSON`

- `json` with dict, list, string
- Title, indent, highlight options
- Invalid JSON string handling

#### `TestProgressBars`

- `progress` – Simple progress bar
- `spinner` – Spinner progress
- `spinner_with_status` – Spinner with status
- `download_progress` – Download progress
- `file_download_progress` – File download progress
- `dependency_progress` – Dependency installation progress
- `package_install_progress` – Package installation progress
- `step_progress` – Step-based progress
- `file_copy_progress` – File copy progress
- `installation_progress` – Installation progress
- `build_progress` – Build progress
- `deployment_progress` – Deployment progress
- `layered_progress` – Layered progress

#### `TestDynamicProgress`

- `dynamic_layered_progress` – Basic usage
- Main layer progress
- Download layer progress
- Spinner layer progress
- Error handling
- Emergency stop
- Without time display

#### `TestErrorHandling`

- Panel with invalid data
- Table with invalid data
- JSON with invalid data

### `test_config.py` – ConfigurationManager Tests

**Location:** `tests/unit/test_config.py`

**Test Classes:**

#### `TestInitialization`

- Default config file
- Custom config file

#### `TestGetSetUpdate`

- `get` – Get configuration value
- `set` – Set configuration value
- `update` – Update multiple values
- `get_all` – Get all configuration

#### `TestSaveLoad`

- `save` – Save to file
- `load` – Load from file
- `reload` – Reload configuration
- `reset_to_defaults` – Reset to defaults

#### `TestPriorityOrder`

- Argument priority
- Environment variable priority
- File priority
- Default priority

#### `TestGetters`

- All specific getter methods (get_log_level, get_printer_level, etc.)

#### `TestExport`

- `export_to_script` – Export to shell script (Unix and Windows)

#### `TestErrorHandling`

- File operation errors (permission, invalid JSON)

### `test_types.py` – Type Tests

**Location:** `tests/unit/test_types.py`

**Test Classes:**

#### `TestLogLevel`

- Level existence and attributes
- `get_label`, `get_no`, `get_fgcolor`, `get_bgcolor`, `get_attribute`
- `is_valid_level`, `get_all_levels`, `get_rich_style`
- Level comparison
- String representations

#### `TestPattern`

- Pattern existence and values
- Enum access

#### `TestPatternColors`

- `PATTERN_COLORS` dictionary
- `get_pattern_color`, `get_pattern_color_by_name`
- Case-insensitivity
- Invalid patterns

#### `TestValidation`

- Validating log levels
- Pattern access

### `test_exceptions.py` – Exception Tests

**Location:** `tests/unit/test_exceptions.py`

**Test Classes:**

#### `TestEzplError`

- Base exception class

#### `TestConfigurationError`

- Configuration-specific errors

#### `TestLoggingError`

- Logging-specific errors

#### `TestValidationError`

- Validation errors

#### `TestInitializationError`

- Initialization errors

#### `TestFileOperationError`

- File operation errors

#### `TestHandlerError`

- Handler-specific errors

### `test_utils.py` – Utility Function Tests

**Location:** `tests/unit/test_utils.py`

**Test Classes:**

#### `TestSafeStrConvert`

- String, int, float, dict, list, None, bool conversion
- Exception conversion
- Custom objects
- Objects without `__str__` or `__repr__`

#### `TestSanitizeForFile`

- Normal strings
- Null bytes
- ANSI escape sequences
- HTML tags
- Control characters
- Preserving newlines/tabs
- Unicode characters
- Non-string inputs

#### `TestSanitizeForConsole`

- Similar to file sanitization (Rich handles ANSI sequences)

#### `TestEdgeCases`

- Empty strings
- Very long strings
- Mixed types in lists
- Nested structures

---

## Integration Tests

### `test_ezpl_integration.py` – Ezpl Integration

**Location:** `tests/integration/test_ezpl_integration.py`

**Test Classes:**

#### `TestEzplPrinterLoggerIntegration`

- `ezpl_provides_both_printer_and_logger` – Both handlers available
- `shared_indentation` – Shared indentation between printer and logger
- `global_level_affects_both` – Global level affects both handlers
- `printer_level_independent` – Printer level independent
- `logger_level_independent` – Logger level independent
- `singleton_propagation` – Singleton propagation
- `file_rotation_with_active_logging` – File rotation with active logging

#### `TestConfigurationIntegration`

- `config_via_args` – Configuration via arguments
- `config_via_configure` – Configuration via configure method
- `config_reload` – Configuration reload

#### `TestWizardIntegration`

- `wizard_accessible_via_printer` – Wizard accessible via printer
- `wizard_with_printer_and_logger` – Wizard with printer and logger

### `test_config_integration.py` – Configuration Integration

**Location:** `tests/integration/test_config_integration.py`

**Test Classes:**

#### `TestConfigManagerEzplIntegration`

- `ezpl_uses_config_manager` – Ezpl uses ConfigurationManager
- `config_changes_reflect_in_ezpl` – Config changes reflect in Ezpl
- `env_and_file_config_integration` – Environment and file config integration
- `config_save_and_reload` – Save and reload configuration
- `config_export_integration` – Configuration export integration

### `test_cli_integration.py` – CLI Integration

**Location:** `tests/integration/test_cli_integration.py`

**Test Classes:**

- CLI command integration tests
- CLI with Ezpl instance
- CLI configuration management

---

## Robustness Tests

### `test_special_chars.py` – Special Character Handling

**Location:** `tests/robustness/test_special_chars.py`

**Test Classes:**

#### `TestPrinterSpecialChars`

- Unicode characters
- Control characters
- ANSI escape sequences
- HTML/XML tags
- Windows paths
- Very long messages

#### `TestLoggerSpecialChars`

- Similar to printer tests
- File content verification

### `test_error_handling.py` – Error Handling

**Location:** `tests/robustness/test_error_handling.py`

**Test Classes:**

#### `TestExceptionMessages`

- ValueError, KeyError, nested exceptions
- With printer and logger

#### `TestComplexObjects`

- Nested dicts
- Lists of objects
- Custom objects
- Objects without `__str__`

#### `TestFileOperationErrors`

- Permission errors
- Disk full simulation
- Read-only file systems

#### `TestInvalidInputs`

- Invalid log levels
- Invalid file paths
- Invalid config values

#### `TestConcurrentOperations`

- Rapid logging
- Simulated concurrent file access

### `test_edge_cases.py` – Edge Cases

**Location:** `tests/robustness/test_edge_cases.py`

**Test Classes:**

#### `TestSingletonEdgeCases`

- `singleton_thread_safety` – Thread-safe singleton
- `reset_during_use` – Reset during active use

#### `TestLargeFiles`

- `large_log_file_creation` – Large log file creation
- `rotation_with_large_file` – Rotation with large file

#### `TestInvalidConfiguration`

- Invalid rotation formats
- Invalid retention formats
- Invalid compression formats
- Negative indent step

#### `TestInvalidPaths`

- Paths with invalid characters
- Too long paths
- Nonexistent parent directories

#### `TestInvalidLogLevels`

- Empty log levels
- None log levels
- Numeric log levels

#### `TestExcessiveIndentation`

- `excessive_indent_adds` – Excessive indent additions
- `excessive_nested_indent` – Excessive nested indentation

#### `TestRotationEdgeCases`

- `rotation_with_compression` – Rotation with compression
- `rotation_at_exact_size` – Rotation at exact size

---

## Test Configuration

### `conftest.py` – Shared Fixtures

**Location:** `tests/conftest.py`

**Fixtures:**

- `reset_ezpl` (autouse) – Automatically reset Ezpl singleton
- `temp_dir` – Temporary directory for test files
- `temp_log_file` – Temporary log file
- `temp_config_file` – Temporary configuration file
- `clean_env` – Clear environment variables
- `mock_console` – Mock Rich Console
- `ezpl_instance` – Clean Ezpl instance

**Pytest Hooks:**

- `pytest_runtest_teardown` – Handle Windows file locking
- `pytest_runtest_makereport` – Suppress teardown errors
- `pytest_runtest_logreport` – Suppress Windows file lock errors

### `pytest.ini` – Pytest Configuration

**Location:** `tests/pytest.ini`

**Configuration:**

- Strict markers and config
- Custom markers (slow, integration, robustness, unit, wizard, config, cli)
- Coverage configuration
- Test paths and Python path

### `run_tests.py` – Test Runner

**Location:** `tests/run_tests.py`

**Features:**

- Test type selection (unit, integration, robustness, all)
- Coverage reporting
- Verbose mode
- Fast mode (exclude slow tests)
- Parallel execution
- Marker filtering

**Usage:**

```bash
python tests/run_tests.py --type unit --coverage --verbose
```

---

## Running Tests

### Using pytest

```bash
# All tests
pytest tests/

# Specific directory
pytest tests/unit/
pytest tests/integration/
pytest tests/robustness/

# Specific marker
pytest -m wizard
pytest -m "not slow"

# With coverage
pytest --cov=ezpl --cov-report=html tests/
```

### Using run_tests.py

```bash
# Unit tests
python tests/run_tests.py --type unit

# Integration tests
python tests/run_tests.py --type integration

# Robustness tests
python tests/run_tests.py --type robustness

# All tests with coverage
python tests/run_tests.py --type all --coverage

# Parallel execution
python tests/run_tests.py --parallel

# Verbose mode
python tests/run_tests.py --verbose

# Filter by marker
python tests/run_tests.py --marker wizard
```

### Coverage Reports

```bash
# Terminal report
pytest --cov=ezpl --cov-report=term-missing tests/

# HTML report
pytest --cov=ezpl --cov-report=html:htmlcov tests/
# Open htmlcov/index.html in browser
```

---

## Test Markers

Custom pytest markers for test categorization:

- `@pytest.mark.unit` – Unit tests (default)
- `@pytest.mark.integration` – Integration tests
- `@pytest.mark.robustness` – Robustness tests
- `@pytest.mark.slow` – Slow tests (exclude with `-m "not slow"`)
- `@pytest.mark.wizard` – RichWizard-related tests
- `@pytest.mark.config` – Configuration-related tests
- `@pytest.mark.cli` – CLI-related tests

**Usage:**

```bash
# Run only wizard tests
pytest -m wizard

# Run all except slow tests
pytest -m "not slow"

# Run integration and robustness tests
pytest -m "integration or robustness"
```

---

## Best Practices

### 1. Test Isolation

Each test is independent. The `reset_ezpl` fixture automatically resets the Ezpl singleton before and after each test.

### 2. Use Fixtures

Use shared fixtures from `conftest.py` for common setup:

```python
def test_example(temp_dir, ezpl_instance):
    log_file = temp_dir / "test.log"
    ezpl = Ezpl(log_file=log_file)
    # Test code
```

### 3. Use Appropriate Markers

Mark tests with appropriate markers for categorization:

```python
@pytest.mark.unit
def test_something():
    pass

@pytest.mark.integration
@pytest.mark.slow
def test_integration():
    pass
```

### 4. Coverage Goals

Aim for >90% code coverage. Use coverage reports to identify untested code.

### 5. Windows Compatibility

Tests handle Windows-specific file locking issues through pytest hooks in `conftest.py`.

---

## Known Issues and Solutions

### Windows File Locking

On Windows, loguru can keep file handles open, causing `PermissionError` during test teardown. This is handled by:

- Explicit `close()` method in `FileLogger`
- Garbage collection and delays in fixtures
- Pytest hooks to suppress non-critical teardown errors

### Progress Bar Generators

Some progress bar context managers yield multiple times. Tests use the correct pattern:

```python
gen = wizard.dependency_progress(deps)
first_yield = gen.__enter__()
progress, task, dep = first_yield
# Iterate over subsequent yields
```

---

## Additional Resources

- **[Test Summary](SUMMARY.md)** – Quick test overview
- **[API Documentation](../api/API_DOCUMENTATION.md)** – API reference
- **[Examples Documentation](../examples/EXAMPLES.md)** – Usage examples

---

**Ezpl** – Comprehensive test suite for reliable logging. 🧪
