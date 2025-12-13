# Test Suite Summary

**Ezpl** – Comprehensive test suite documentation.

## 📖 Complete Documentation

For detailed test documentation, see **[TEST_DOCUMENTATION.md](TEST_DOCUMENTATION.md)**.

---

## Quick Overview

### Test Structure

The Ezpl test suite is organized into three main categories:

- **Unit Tests** (`tests/unit/`) – Individual component testing
- **Integration Tests** (`tests/integration/`) – Component interaction testing
- **Robustness Tests** (`tests/robustness/`) – Edge cases and error handling

### Test Coverage

- **Unit Tests**: 8 test files covering all core components
- **Integration Tests**: 3 test files for component integration
- **Robustness Tests**: 3 test files for edge cases and error scenarios
- **Total**: 200+ test cases

### Quick Start

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run all tests
pytest tests/

# Run specific test type
python tests/run_tests.py --type unit
python tests/run_tests.py --type integration
python tests/run_tests.py --type robustness

# With coverage
python tests/run_tests.py --coverage

# Parallel execution
python tests/run_tests.py --parallel
```

### Test Types

**Unit Tests:**

- `test_ezpl.py` – Ezpl singleton, initialization, configuration
- `test_printer.py` – ConsolePrinter, log levels, patterns, Rich features
- `test_logger.py` – FileLogger, rotation, retention, compression
- `test_wizard.py` – RichWizard panels, tables, JSON, progress bars
- `test_config.py` – ConfigurationManager operations
- `test_types.py` – LogLevel and Pattern enumerations
- `test_exceptions.py` – Custom exception classes
- `test_utils.py` – Utility functions

**Integration Tests:**

- `test_ezpl_integration.py` – Ezpl with Printer and Logger integration
- `test_config_integration.py` – ConfigurationManager with Ezpl integration
- `test_cli_integration.py` – CLI command integration

**Robustness Tests:**

- `test_special_chars.py` – Special character handling
- `test_error_handling.py` – Error scenarios and exception handling
- `test_edge_cases.py` – Edge cases, thread safety, large files

### Test Markers

Custom pytest markers for filtering:

- `@pytest.mark.unit` – Unit tests (default)
- `@pytest.mark.integration` – Integration tests
- `@pytest.mark.robustness` – Robustness tests
- `@pytest.mark.slow` – Slow tests (exclude with `-m "not slow"`)
- `@pytest.mark.wizard` – RichWizard-related tests
- `@pytest.mark.config` – Configuration-related tests
- `@pytest.mark.cli` – CLI-related tests

### Running Tests

**Using pytest directly:**

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

**Using run_tests.py:**

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

### Test Configuration

**pytest.ini:**

- Strict markers and config
- Custom markers defined
- Coverage configuration
- Test paths and Python path

**conftest.py:**

- Shared fixtures for all tests
- Ezpl singleton reset
- Temporary directories and files
- Mock console and configuration
- Windows-specific teardown handling

### Key Features Tested

**Ezpl:**

- Singleton pattern and thread safety
- Initialization with various parameters
- Configuration priority (arg > env > file > default)
- Level management (global, printer, logger)
- File operations (set, get, separators)
- Indentation management
- Configuration reload

**ConsolePrinter:**

- All log levels (DEBUG, INFO, SUCCESS, WARNING, ERROR, CRITICAL)
- Pattern methods (TIP, SYSTEM, INSTALL, DETECT, CONFIG, DEPS)
- Indentation management
- Rich features (tables, panels, JSON)
- Special character handling
- Type conversion

**FileLogger:**

- All log levels
- File rotation (by size, time, date, at time)
- Retention (by duration, count)
- Compression (zip, gz, tar.gz)
- Separators
- File operations (size, path)
- Special character handling
- Error handling

**RichWizard:**

- Panels (info, success, error, warning, installation)
- Tables (generic, status, dependency, command)
- JSON display
- Progress bars (simple, spinner, download, dependency, step)
- Dynamic layered progress
- Error handling

**ConfigurationManager:**

- Get/set/update operations
- Save/load from file
- Priority order
- Specific getters
- Export to script
- Error handling

### Best Practices

1. **Test Isolation**: Each test is independent (Ezpl singleton is reset)
2. **Fixtures**: Use shared fixtures from `conftest.py`
3. **Markers**: Use appropriate markers for test categorization
4. **Coverage**: Aim for >90% code coverage
5. **Windows Compatibility**: Tests handle Windows-specific file locking issues

---

## Additional Resources

- **[Complete Test Documentation](TEST_DOCUMENTATION.md)** – Detailed test documentation
- **[API Documentation](../api/API_DOCUMENTATION.md)** – API reference
- **[Examples Documentation](../examples/EXAMPLES.md)** – Usage examples

---

**Ezpl** – Comprehensive test suite for reliable logging. 🧪
