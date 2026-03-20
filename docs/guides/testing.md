# Testing Guide

Comprehensive guide to the **Ezpl** test suite and testing practices.

## Overview

Ezpl includes a comprehensive test suite with **377 tests** covering unit, integration, and robustness scenarios with **65% code coverage**.

The project uses a `src/` layout (`src/ezplog`). The test suite adds `src/` to the import path in `tests/conftest.py`, so tests can run without a separate install step.

## Test Statistics

| Metric      | Value                         |
| ----------- | ----------------------------- |
| Total tests | 377                           |
| Passing     | 377 (100%)                    |
| Coverage    | 65%                           |
| Test types  | Unit, Integration, Robustness |

## Test Structure

```text
tests/
├── conftest.py              # Fixtures, hooks, Windows teardown handling
├── run_tests.py             # CLI test runner with options
├── unit/                    # 10 test files - individual components
│   ├── test_ezpl.py
│   ├── test_printer.py
│   ├── test_logger.py
│   ├── test_wizard.py
│   ├── test_configuration.py
│   ├── test_log_level.py
│   ├── test_patterns.py
│   ├── test_exceptions.py
│   ├── test_cli_commands.py
│   └── test_cli_utils.py
├── integration/             # 3 test files - cross-module interactions
│   ├── test_integration.py
│   ├── test_config_integration.py
│   └── test_cli_integration.py
└── robustness/              # 3 test files - edge cases, error handling
    ├── test_error_handling.py
    ├── test_edge_cases.py
    └── test_windows_compatibility.py
```

## Key Fixtures

### Common Fixtures (conftest.py)

| Fixture            | Scope                 | Purpose                                 |
| ------------------ | --------------------- | --------------------------------------- |
| `reset_ezpl`       | function, **autouse** | Resets singleton before/after each test |
| `temp_dir`         | function              | Temporary directory for test files      |
| `temp_log_file`    | function              | Temporary log file path                 |
| `temp_config_file` | function              | Temporary config file path              |
| `mock_console`     | function              | Mock Rich Console                       |
| `ezpl_instance`    | function              | Fresh Ezpl with temp log file           |
| `config_manager`   | function              | ConfigurationManager with temp config   |
| `clean_env`        | function              | Cleans `EZPL_*` env vars                |
| `sample_log_data`  | function              | Sample log entries for testing          |

### Fixture Examples

```python
@pytest.fixture
def ezpl_instance(temp_log_file, reset_ezpl):
    """Provide a fresh Ezpl instance with temporary log file."""
    ezpl = Ezpl(log_file=temp_log_file)
    return ezpl

@pytest.fixture
def mock_console(mocker):
    """Provide a mocked Rich Console."""
    mock = mocker.Mock(spec=Console)
    return mock
```

## Test Naming Convention

Tests follow the pattern:

```python
def test_should_<expected_behavior>_when_<condition>():
    """Test description."""
    # Test implementation
```

**Examples:**

```python
def test_should_create_singleton_when_first_call():
    """Test that Ezpl creates singleton on first call."""

def test_should_log_message_when_printer_info_called():
    """Test that printer logs info message correctly."""

def test_should_raise_error_when_invalid_level_provided():
    """Test that invalid level raises ValidationError."""
```

## Test Markers

Use pytest markers to categorize tests:

```python
@pytest.mark.unit
def test_basic_functionality():
    ...

@pytest.mark.integration
def test_cross_module_interaction():
    ...

@pytest.mark.robustness
def test_edge_case():
    ...

@pytest.mark.slow
def test_time_consuming_operation():
    ...

@pytest.mark.wizard
def test_rich_wizard_feature():
    ...

@pytest.mark.cli
def test_cli_command():
    ...
```

### Available Markers

- `@pytest.mark.unit` - Unit tests (default)
- `@pytest.mark.integration` - Integration tests
- `@pytest.mark.robustness` - Robustness and edge cases
- `@pytest.mark.slow` - Slow tests (exclude with `-m "not slow"`)
- `@pytest.mark.wizard` - RichWizard tests
- `@pytest.mark.config` - Configuration tests
- `@pytest.mark.cli` - CLI tests

## Running Tests

### Using CLI Test Runner

```bash
# Unit tests only
python tests/run_tests.py --type unit

# Integration tests
python tests/run_tests.py --type integration

# Robustness tests
python tests/run_tests.py --type robustness

# All tests
python tests/run_tests.py --type all

# With coverage
python tests/run_tests.py --type all --coverage

# Exclude slow tests
python tests/run_tests.py --fast

# Parallel execution
python tests/run_tests.py --parallel

# Specific marker
python tests/run_tests.py --marker wizard

# Verbose output
python tests/run_tests.py --verbose
```

### Using pytest Directly

```bash
# All tests
pytest tests/ -v

# Unit tests only
pytest tests/unit/ -v

# With coverage
pytest tests/ --cov=src/ezplog --cov-report=html --cov-report=term

# Specific test file
pytest tests/unit/test_ezpl.py -v

# Specific test function
pytest tests/unit/test_ezpl.py::test_should_create_singleton_when_first_call -v

# With markers
pytest tests/ -m unit -v
pytest tests/ -m "not slow" -v
pytest tests/ -m "wizard and unit" -v

# Parallel execution
pytest tests/ -n auto

# Stop on first failure
pytest tests/ -x

# Show local variables on failure
pytest tests/ -l

# Show full diff
pytest tests/ --tb=long
```

## Writing Tests

### Basic Test Structure

```python
import pytest
from ezplog import Ezpl

def test_should_initialize_ezpl_when_called():
    """Test Ezpl initialization."""
    # Arrange
    log_file = "test.log"

    # Act
    ezpl = Ezpl(log_file=log_file)

    # Assert
    assert ezpl is not None
    assert ezpl.get_printer() is not None
    assert ezpl.get_logger() is not None
```

### Using Fixtures

```python
def test_should_log_message_when_info_called(ezpl_instance):
    """Test printer info logging."""
    # Arrange
    printer = ezpl_instance.get_printer()

    # Act
    printer.info("Test message")

    # Assert - check log file or mock
    # ...
```

### Testing Exceptions

```python
import pytest
from ezplog import Ezpl, ValidationError

def test_should_raise_validation_error_when_invalid_level():
    """Test that invalid level raises ValidationError."""
    ezpl = Ezpl()

    with pytest.raises(ValidationError) as exc_info:
        ezpl.set_level("INVALID")

    assert "Invalid log level" in str(exc_info.value)
```

### Mocking

```python
def test_should_call_console_print_when_info_logged(mocker, ezpl_instance):
    """Test that console.print is called."""
    # Arrange
    printer = ezpl_instance.get_printer()
    mock_print = mocker.patch.object(printer._console, 'print')

    # Act
    printer.info("Test message")

    # Assert
    mock_print.assert_called_once()
```

### Parametrized Tests

```python
@pytest.mark.parametrize("level,expected", [
    ("DEBUG", LogLevel.DEBUG),
    ("INFO", LogLevel.INFO),
    ("WARNING", LogLevel.WARNING),
    ("ERROR", LogLevel.ERROR),
])
def test_should_set_level_when_valid_level_provided(level, expected):
    """Test setting various log levels."""
    ezpl = Ezpl()
    ezpl.set_level(level)
    # Assert level is set correctly
```

### Testing File Operations

```python
def test_should_create_log_file_when_logging(temp_log_file, ezpl_instance):
    """Test that log file is created."""
    # Arrange
    logger = ezpl_instance.get_logger()

    # Act
    logger.info("Test log entry")

    # Assert
    assert temp_log_file.exists()
    assert temp_log_file.read_text().count("Test log entry") > 0
```

### Testing CLI Commands

```python
import ezplog
from click.testing import CliRunner
from ezplog.cli.main import cli

def test_should_display_version_when_version_command_run():
    """Test version command."""
    # Arrange
    runner = CliRunner()

    # Act
    result = runner.invoke(cli, ['version'])

    # Assert
    assert result.exit_code == 0
    assert ezplog.__version__ in result.output
```

## Test Categories

### Unit Tests

Test individual components in isolation:

```python
def test_should_format_pattern_when_print_pattern_called():
    """Test pattern formatting."""
    from ezplog.handlers.console import EzPrinter

    printer = EzPrinter(level="INFO")
    # Test pattern formatting logic
```

### Integration Tests

Test interactions between components:

```python
def test_should_log_to_both_console_and_file_when_configured():
    """Test console and file logging integration."""
    ezpl = Ezpl(log_file="test.log", log_level="DEBUG")
    printer = ezpl.get_printer()
    logger = ezpl.get_logger()

    # Test that both handlers work together
    printer.info("Console message")
    logger.info("File message")
```

### Robustness Tests

Test edge cases and error handling:

```python
def test_should_handle_unicode_when_special_chars_logged():
    """Test handling of unicode characters."""
    ezpl = Ezpl()
    printer = ezpl.get_printer()

    # Should not crash with unicode
    printer.info("Unicode: 你好世界 🚀 ñ é")

def test_should_convert_non_string_when_logging():
    """Test automatic type conversion."""
    ezpl = Ezpl()
    printer = ezpl.get_printer()

    # Should convert to string automatically
    printer.info(12345)
    printer.info({"key": "value"})
    printer.info([1, 2, 3])
```

## Windows-Specific Testing

### File Locking Handling

```python
@pytest.fixture(autouse=True)
def reset_ezpl():
    """Reset Ezpl singleton before and after each test."""
    # Before test
    Ezpl.reset()
    yield
    # After test (Windows compatibility)
    Ezpl.reset()
    if platform.system() == "Windows":
        gc.collect()  # Force garbage collection
        time.sleep(0.15)  # Allow file handles to release
```

### Teardown Error Suppression

```python
def pytest_runtest_makereport(item, call):
    """Suppress teardown errors on Windows."""
    if call.when == "teardown" and call.excinfo:
        if platform.system() == "Windows":
            # Suppress file-related teardown errors
            call.excinfo = None
```

## Coverage

### Running with Coverage

```bash
# HTML report
pytest tests/ --cov=src/ezplog --cov-report=html

# Terminal report
pytest tests/ --cov=src/ezplog --cov-report=term-missing

# XML report (for CI)
pytest tests/ --cov=src/ezplog --cov-report=xml

# All reports
pytest tests/ --cov=src/ezplog --cov-report=html --cov-report=term-missing --cov-report=xml
```

### Coverage Configuration

```toml
# pyproject.toml
[tool.coverage.run]
source = ["src/ezplog"]
branch = true
omit = [
    "*/tests/*",
    "*/__pycache__/*",
]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "raise NotImplementedError",
    "if __name__ == .__main__.:",
]
show_missing = true
precision = 2
```

### Coverage Requirements

- **Minimum threshold**: 60%
- **Target**: 65%+
- **Critical modules**: 80%+

### Viewing Coverage Report

```bash
# Generate HTML report
pytest tests/ --cov=src/ezplog --cov-report=html

# Open in browser
# Windows
start htmlcov/index.html

# macOS
open htmlcov/index.html

# Linux
xdg-open htmlcov/index.html
```

## Continuous Integration

### GitHub Actions

Tests run automatically on:

- Push to main branch
- Pull request creation
- Pull request updates

```yaml
# Example workflow
- name: Run tests
  run: |
    pytest tests/ -v --tb=short --cov=src/ezplog
```

### Pre-commit Hooks

Tests can run in pre-commit:

```yaml
# .pre-commit-config.yaml
- repo: local
  hooks:
    - id: pytest
      name: pytest
      entry: pytest
      language: system
      pass_filenames: false
      always_run: true
```

## Best Practices

### Test Organization

1. **One test file per module**
2. **Group related tests in classes** (optional)
3. **Use descriptive test names**
4. **Keep tests focused and simple**
5. **Test one thing per test**

### Test Quality

1. **Follow AAA pattern** (Arrange, Act, Assert)
2. **Use fixtures** for common setup
3. **Mock external dependencies**
4. **Test both success and failure paths**
5. **Include edge cases**

### Performance

1. **Mark slow tests** with `@pytest.mark.slow`
2. **Use parallel execution** for large test suites
3. **Avoid unnecessary file I/O**
4. **Clean up resources** in fixtures

### Maintenance

1. **Keep tests up to date** with code changes
2. **Remove obsolete tests**
3. **Refactor duplicate test code** into fixtures
4. **Document complex test logic**

## Troubleshooting

### Common Issues

#### Tests Fail on Windows

```python
# Add Windows-specific handling
if platform.system() == "Windows":
    gc.collect()
    time.sleep(0.15)
```

#### Singleton Not Reset

```python
# Ensure reset fixture is used
@pytest.fixture(autouse=True)
def reset():
    Ezpl.reset()
    yield
    Ezpl.reset()
```

#### Mock Not Working

```python
# Use mocker fixture from pytest-mock
def test_example(mocker):
    mock = mocker.patch('ezplog.handlers.console.Console')
    # ...
```

#### Coverage Too Low

```bash
# Check which lines are missing
pytest tests/ --cov=src/ezplog --cov-report=term-missing

# View detailed HTML report
pytest tests/ --cov=src/ezplog --cov-report=html
```

## Resources

### Internal Documentation

- `tests/conftest.py` - Fixtures and hooks
- `tests/run_tests.py` - Test runner
- `.github/instructions/` - Testing guidelines

### External Resources

- [pytest Documentation](https://docs.pytest.org/)
- [pytest-cov Documentation](https://pytest-cov.readthedocs.io/)
- [pytest-mock Documentation](https://pytest-mock.readthedocs.io/)
- [pytest-xdist Documentation](https://pytest-xdist.readthedocs.io/)

## See Also

- [Development Guide](development.md) - Development workflow
- [API Reference](../api/index.md) - API documentation
- [Examples](../examples/index.md) - Usage examples

## Need Help?

- **Issues**: [GitHub Issues](https://github.com/neuraaak/ezplog/issues)
- **Repository**: [https://github.com/neuraaak/ezplog](https://github.com/neuraaak/ezplog)
