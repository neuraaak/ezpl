# Project Instructions — ezpl (ezplog)

This file is the **primary reference** for any AI assistant or developer working on this project.
It must be consulted **before any development task**.

---

## Instruction Hierarchy

Priority order when multiple instructions exist:

1. **This file** (`.github/instructions/README.md`) — Project context and overrides
2. **Domain-specific files** in `.github/instructions/` — Detailed standards
3. **`CLAUDE.md`** — Claude-specific preferences
4. **General conventions** — Only when not covered above

### Available Instruction Files

| File                                                            | Scope                                                |
| --------------------------------------------------------------- | ---------------------------------------------------- |
| `core/advanced-cognitive-conduct.instructions.md`               | Reasoning framework and senior colleague approach    |
| `languages/python/python-development-standards.instructions.md` | Python development practices and optimization        |
| `languages/python/python-formatting-standards.instructions.md`  | Code formatting, section markers, docstrings         |
| `languages/python/pyproject-standards.instructions.md`          | `pyproject.toml` organization and tool configuration |

---

## Project Overview

**ezpl** is a modern Python logging framework combining **Rich** console output with **loguru** file logging.

| Attribute            | Value                                |
| -------------------- | ------------------------------------ |
| Package name (PyPI)  | `ezplog`                             |
| Module name (import) | `ezpl`                               |
| Python               | `>=3.10`                             |
| License              | MIT                                  |
| Author               | Neuraaak                             |
| Status               | Production/Stable                    |
| Repository           | <https://github.com/neuraaak/ezplog> |

### Core Dependencies

| Library         | Purpose                                                      |
| --------------- | ------------------------------------------------------------ |
| `loguru>=0.7.2` | File logging with rotation, retention, compression           |
| `rich>=13.0.0`  | Console rendering with colors, panels, tables, progress bars |
| `click>=8.0.0`  | CLI framework                                                |

---

## Architecture

### Singleton Pattern

The central class `Ezpl` implements a **thread-safe Singleton** with double-checked locking.
A single global instance manages both console and file logging.

```text
Ezpl (Singleton)
├── EzPrinter (alias: Printer) — Rich-based console output
│   └── RichWizard — Advanced display (panels, tables, JSON, progress)
├── EzLogger (alias: Logger) — loguru-based file logging
└── ConfigurationManager — Centralized configuration
```

### Configuration Priority

Resolution order (highest to lowest):

1. **Arguments** passed directly to `Ezpl()`
2. **Environment variables** (`EZPL_*` prefix)
3. **Configuration file** (`~/.ezpl/config.json`)
4. **Default values** (defined in `ezpl/config/defaults.py`)

### Environment Variables

| Variable                  | Purpose               | Default    |
| ------------------------- | --------------------- | ---------- |
| `EZPL_LOG_LEVEL`          | Global log level      | `INFO`     |
| `EZPL_LOG_FILE`           | Log file path         | `ezpl.log` |
| `EZPL_PRINTER_LEVEL`      | Console output level  | `INFO`     |
| `EZPL_FILE_LOGGER_LEVEL`  | File logger level     | `INFO`     |
| `EZPL_LOG_ROTATION`       | Rotation setting      | `None`     |
| `EZPL_LOG_RETENTION`      | Retention period      | `None`     |
| `EZPL_LOG_COMPRESSION`    | Compression format    | `None`     |
| `EZPL_INDENT_STEP`        | Indentation step size | `3`        |
| `EZPL_INDENT_SYMBOL`      | Indentation symbol    | `>`        |
| `EZPL_BASE_INDENT_SYMBOL` | Base indent symbol    | `~`        |

---

## Module Structure

```text
ezpl/
├── __init__.py              # Public API, exports, version
├── ezpl.py                  # Singleton class (core)
├── cli/                     # CLI (Click-based)
│   ├── main.py              # Entry point: ezpl command
│   ├── commands/            # Subcommands: config, info, logs, version
│   └── utils/               # CLI utilities: env_manager, log_parser, log_stats
├── config/
│   ├── manager.py           # ConfigurationManager
│   └── defaults.py          # Default values and cross-platform paths
├── core/
│   ├── exceptions.py        # Exception hierarchy (EzplError base)
│   ├── interfaces.py        # ABCs (LoggingHandler, IndentationManager) + Protocols
│   └── __init__.py
├── handlers/
│   ├── console.py           # EzPrinter (Rich console output)
│   ├── file.py              # EzLogger (loguru file logging)
│   ├── utils.py             # Handler utilities
│   └── wizard/              # RichWizard advanced display
│       ├── core.py          # Core wizard functionality
│       ├── dynamic.py       # Dynamic progress bars
│       ├── json.py          # JSON display
│       ├── panels.py        # Panel rendering
│       ├── progress.py      # Progress bars and spinners
│       └── tables.py        # Table rendering
├── types/
│   ├── enums/
│   │   ├── log_level.py     # LogLevel: DEBUG, INFO, SUCCESS, WARNING, ERROR, CRITICAL
│   │   └── patterns.py      # Pattern: SUCCESS, ERROR, WARN, TIP, SYSTEM, INSTALL, etc.
│   └── protocols/
│       ├── logger_protocol.py   # LoggerProtocol
│       └── printer_protocol.py  # PrinterProtocol
└── utils/                   # Shared utility functions
```

---

## Public API

### Exported Classes

| Class                  | Alias     | Purpose                                  |
| ---------------------- | --------- | ---------------------------------------- |
| `Ezpl`                 | —         | Main singleton, manages printer + logger |
| `EzPrinter`            | `Printer` | Console output with pattern formatting   |
| `EzLogger`             | `Logger`  | File logging with rotation support       |
| `RichWizard`           | —         | Advanced Rich display capabilities       |
| `ConfigurationManager` | —         | Configuration management                 |

### Exception Hierarchy

All exceptions inherit from `EzplError` which carries a `message` and optional `error_code`.

```text
EzplError (base)
├── ConfigurationError      # CONFIG_ERROR — config loading/validation
├── LoggingError            # LOGGING_ERROR — file writing, handler init
├── ValidationError         # VALIDATION_ERROR — input validation
├── InitializationError     # INIT_ERROR — component initialization
├── FileOperationError      # FILE_ERROR — file read/write/create
└── HandlerError            # HANDLER_ERROR — handler operations
```

### Type Exports

| Export            | Type     | Purpose                                        |
| ----------------- | -------- | ---------------------------------------------- |
| `LogLevel`        | Enum     | DEBUG, INFO, SUCCESS, WARNING, ERROR, CRITICAL |
| `Pattern`         | Enum     | Contextual patterns with color mapping         |
| `PATTERN_COLORS`  | dict     | Pattern-to-color mapping                       |
| `PrinterProtocol` | Protocol | Interface for printer implementations          |
| `LoggerProtocol`  | Protocol | Interface for logger implementations           |

---

## Type System & Design Patterns

### Type Conventions

- **Union syntax**: `int | str` (not `Union[int, str]`)
- **Built-in generics**: `list[str]`, `dict[str, int]`, `tuple[int, str]`
- **Imports**: `collections.abc` over `typing` for `Sequence`, `Mapping`, `Callable`
- **Protocols**: Structural typing for flexible implementations
- **Future annotations**: `from __future__ import annotations` in every file
- **Type aliases**: `Printer = EzPrinter`, `Logger = EzLogger`

### Design Patterns Used

| Pattern                | Location                                    | Purpose                        |
| ---------------------- | ------------------------------------------- | ------------------------------ |
| Singleton              | `Ezpl.__new__()`                            | Single global logging instance |
| Double-checked locking | `Ezpl._lock`                                | Thread-safe singleton init     |
| Handler                | `EzPrinter`, `EzLogger`                     | Separate console/file concerns |
| Protocol               | `PrinterProtocol`, `LoggerProtocol`         | Structural typing interfaces   |
| ABC                    | `LoggingHandler`, `IndentationManager`      | Abstract base contracts        |
| Context Manager        | `manage_indent()`                           | Indentation scope management   |
| Factory                | `set_printer_class()`, `set_logger_class()` | Custom handler injection       |
| Configuration locking  | `lock_config()`, `unlock_config()`          | Prevent library interference   |

---

## Code Formatting Standards

### Section Markers

Main sections use forward-slash separators:

```python
# ///////////////////////////////////////////////////////////////
# SECTION NAME
# ///////////////////////////////////////////////////////////////
```

Subsections within classes use dash separators:

```python
# ------------------------------------------------
# SUBSECTION NAME
# ------------------------------------------------
```

### File Layout Order

1. Module header comment (`# ///` block with module name)
2. Module docstring
3. `# IMPORTS` — Standard library → Third-party → Local
4. `# CONSTANTS`
5. `# CLASSES`
6. `# FUNCTIONS`
7. `# PUBLIC API` — `__all__` exports

### Naming Conventions

| Element           | Convention         | Example                             |
| ----------------- | ------------------ | ----------------------------------- |
| Classes           | PascalCase         | `EzPrinter`, `RichWizard`           |
| Methods/functions | snake_case         | `get_printer()`, `set_level()`      |
| Constants         | UPPER_SNAKE_CASE   | `LOG_LEVEL`, `CONFIG_DIR`           |
| Private members   | Leading underscore | `_instance`, `_printer`             |
| Enum members      | UPPER_SNAKE_CASE   | `LogLevel.DEBUG`, `Pattern.SUCCESS` |

### Docstrings

Google style with `Args`, `Returns`, `Raises`, `Example` sections:

```python
def example(param1: str, param2: int | None = None) -> bool:
    """Brief description.

    Detailed explanation of behavior.

    Args:
        param1: Description of param1
        param2: Description of param2

    Returns:
        bool: Description of return value

    Raises:
        ValidationError: When validation fails

    Example:
        >>> result = example("test", 42)
        >>> print(result)
        True
    """
```

### Comments

- Written in **English** by default
- Explain the **why**, not the **what**
- No comments on obvious operations
- No meta-comments about refactoring or code history

---

## Code Quality Tools

### Tool Chain

| Tool    | Purpose                        | Line Length | Target              |
| ------- | ------------------------------ | ----------- | ------------------- |
| Black   | Code formatting                | 88          | py310, py311, py312 |
| isort   | Import sorting (black profile) | 88          | —                   |
| Ruff    | Linting (12 rule sets)         | 88          | py310               |
| Pyright | Type checking (basic mode)     | —           | 3.10                |
| ty      | Minimal type checking          | —           | 3.10                |
| Bandit  | Security scanning              | —           | —                   |

### Ruff Rules Enabled

```text
E    — pycodestyle errors          S    — bandit security
W    — pycodestyle warnings        T20  — flake8-print
F    — pyflakes                    ARG  — flake8-unused-arguments
I    — isort                       PIE  — flake8-pie
B    — flake8-bugbear              SIM  — flake8-simplify
C4   — flake8-comprehensions       UP   — pyupgrade
```

Maximum cyclomatic complexity: **10**

### Per-File Exceptions

| Path            | Allowed                         |
| --------------- | ------------------------------- |
| `tests/**/*`    | `S101` (assert), `S311`, `E501` |
| `examples/**/*` | `T201` (print), `E501`          |
| `ezpl/cli/**/*` | `T201` (print), `E501`          |

---

## Testing

### Structure

```text
tests/
├── conftest.py              # Fixtures, hooks, Windows teardown handling
├── run_tests.py             # CLI test runner with options
├── unit/                    # 10 test files — individual components
├── integration/             # 3 test files — cross-module interactions
└── robustness/              # 3 test files — edge cases, error handling
```

### Key Fixtures (conftest.py)

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

### Test Naming Convention

```python
def test_should_<expected_behavior>_when_<condition>():
```

### Test Markers

| Marker                     | Purpose                                   |
| -------------------------- | ----------------------------------------- |
| `@pytest.mark.unit`        | Unit tests (default)                      |
| `@pytest.mark.integration` | Integration tests                         |
| `@pytest.mark.robustness`  | Robustness and edge cases                 |
| `@pytest.mark.slow`        | Slow tests (exclude with `-m "not slow"`) |
| `@pytest.mark.wizard`      | RichWizard tests                          |
| `@pytest.mark.config`      | Configuration tests                       |
| `@pytest.mark.cli`         | CLI tests                                 |

### Running Tests

```bash
# Unit tests only
python tests/run_tests.py --type unit

# All tests with coverage
python tests/run_tests.py --type all --coverage

# Exclude slow tests
python tests/run_tests.py --fast

# Parallel execution
python tests/run_tests.py --parallel

# Specific marker
python tests/run_tests.py --marker wizard

# Direct pytest
pytest tests/ -v --tb=short
```

### Coverage Requirements

- **Minimum threshold**: 60%
- **Source**: `ezpl/` package
- **Branch coverage**: enabled
- **Reports**: terminal (missing lines), HTML, XML

### Windows-Specific Handling

- `gc.collect()` + 0.15s delay in `reset_ezpl` for file handle release
- Teardown error suppression hooks for Windows file locking issues

---

## Git Hooks & Automation

### Pre-commit Hook (`.hooks/pre-commit`)

Runs automatically before each commit:

1. **Lint & format** via `.scripts/dev/lint.py` (fallback: Black + isort + Ruff)
2. **Update version badge** in README via `.scripts/dev/update_version.py`
3. **Auto-stage** all reformatted files

### Post-commit Hook (`.hooks/post-commit`)

Runs automatically after each commit:

1. **Read version** from `pyproject.toml`
2. **Create/update tag**: `v<version>` (e.g., `v1.5.1`)
3. **Create/update latest tag**: `v<major>-latest` (e.g., `v1-latest`)
4. **Build package** via `.scripts/build/build_package.py`

### Pre-commit Framework (`.pre-commit-config.yaml`)

Execution order:

1. File hygiene (trailing whitespace, EOF, YAML/TOML validation, merge conflicts, large files, debug statements, private keys)
2. Ruff format
3. Black
4. isort
5. Ruff check (with `--fix`)
6. Bandit security scan

### Activating Hooks

```bash
git config core.hooksPath .hooks
```

---

## CI/CD — PyPI Publication

Workflow: `.github/workflows/publish-pypi.yml`

### Trigger

- Push of version tag (`v*.*.*`)
- Manual dispatch

### Pipeline Steps

1. **Version validation** — tag must match `pyproject.toml` version
2. **Branch verification** — tag must be on `main`
3. **Test suite** — full test execution
4. **Build** — wheel and source distribution
5. **Publish** — PyPI via `pypa/gh-action-pypi-publish`

---

## Environment Constraints

| Constraint   | Detail                                    |
| ------------ | ----------------------------------------- |
| Platform     | Windows-based development                 |
| Proxy        | Required for external requests            |
| Dependencies | Wheel files (`.whl`) preferred            |
| PyPI access  | Limited — assume local package management |
| Build        | `cx_Freeze` for executables               |

---

## Prohibited Practices

- **No `print()`** for logging — use the logging framework
- **No global variables** — use configuration or class attributes
- **No commented-out code** in commits
- **No hard-coded credentials** or file paths
- **No silent failures** — always raise or log errors
- **No `os.path`** — use `pathlib.Path`
- **No `Union[X, Y]`** — use `X | Y`
- **No `List[str]`** — use `list[str]`

---

## Quick Reference — Development Workflow

```bash
# 1. Activate virtual environment
.venv\Scripts\activate          # Windows
source .venv/bin/activate       # Unix

# 2. Install dev dependencies
python -m pip install -e ".[dev]"

# 3. Activate git hooks
git config core.hooksPath .hooks

# 4. Run tests
python tests/run_tests.py --type all --coverage

# 5. Lint manually
ruff check ezpl/ --fix
ruff format ezpl/
black ezpl/
isort ezpl/

# 6. Type check
pyright ezpl/

# 7. Security scan
bandit -r ezpl/ -f json

# 8. Build package
python -m build
```
