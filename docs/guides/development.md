# Development Guide

Comprehensive guide for developing and contributing to **Ezpl**.

## Prerequisites

- Python 3.10 or higher
- Git
- Understanding of Python logging, Rich, and loguru

## Development Setup

### 1. Clone the Repository

```bash
git clone https://github.com/neuraaak/ezplog.git
cd ezplog
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate

# Activate (Unix/Linux/macOS)
source .venv/bin/activate
```

### 3. Install Development Dependencies

```bash
# Install in editable mode with dev dependencies
pip install -e ".[dev]"
```

This installs:

- **Development tools**: black, isort, ruff, pyright
- **Testing**: pytest, pytest-cov, pytest-mock, pytest-xdist
- **Build**: build, twine
- **Security**: bandit

### 4. Install Git Hooks

```bash
# Activate custom hooks
git config core.hooksPath .hooks

# Or use pre-commit (alternative)
pre-commit install
```

## Project Structure

```text
ezplog/
├── .github/
│   ├── instructions/      # Development instructions
│   └── workflows/         # CI/CD workflows
├── .hooks/                # Custom Git hooks
├── docs/                  # Documentation (mkdocs)
├── ezpl/                  # Source code
│   ├── cli/              # CLI commands
│   ├── config/           # Configuration management
│   ├── core/             # Core interfaces and exceptions
│   ├── handlers/         # Printer and logger handlers
│   │   └── wizard/       # RichWizard components
│   ├── types/            # Type definitions and enums
│   └── utils/            # Utilities
├── tests/                # Test suite
│   ├── unit/            # Unit tests
│   ├── integration/     # Integration tests
│   └── robustness/      # Robustness tests
├── examples/            # Example scripts
├── pyproject.toml       # Project configuration
└── mkdocs.yml          # Documentation configuration
```

## Coding Standards

### Python Style

Follow the project's coding standards defined in `.github/instructions/`:

- **PEP 8** compliance
- **Line length**: 88 characters (Black default)
- **Type hints**: Required for all public APIs
- **Docstrings**: Google style
- **Imports**: Standard library → Third-party → Local

### Type Hints

```python
from __future__ import annotations

# Use modern type syntax
def process(data: list[str]) -> dict[str, int]:
    ...

# Prefer | over Union
def get_value(key: str) -> str | None:
    ...

# Use collections.abc
from collections.abc import Sequence

def handle_items(items: Sequence[str]) -> None:
    ...
```

### Docstrings

```python
def example_function(param1: str, param2: int | None = None) -> bool:
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
        >>> result = example_function("test", 42)
        >>> print(result)
        True
    """
```

## Development Workflow

### 1. Create a Feature Branch

```bash
git checkout -b feature/your-feature-name
```

### 2. Make Changes

Follow the coding standards and add tests for new features.

### 3. Run Code Quality Tools

```bash
# Format code
black ezpl/
isort ezpl/

# Lint
ruff check ezpl/ --fix
ruff format ezpl/

# Type check
pyright ezpl/

# Security scan
bandit -r ezpl/
```

### 4. Run Tests

```bash
# All tests
pytest tests/

# With coverage
pytest tests/ --cov=ezpl --cov-report=html

# Specific test type
pytest tests/unit/
pytest tests/integration/
pytest tests/robustness/

# Parallel execution
pytest tests/ -n auto
```

### 5. Commit Changes

```bash
# Add files
git add .

# Commit (hooks will run automatically)
git commit -m "feat: add new feature"
```

The pre-commit hook will automatically:

- Format code with black, isort, ruff
- Run linting checks
- Update version badge in README
- Auto-stage reformatted files

### 6. Push and Create PR

```bash
git push origin feature/your-feature-name
```

Then create a Pull Request on GitHub.

## Git Hooks

### Pre-commit Hook

Runs before each commit:

1. **Lint & Format**: Black + isort + Ruff
2. **Update Version Badge**: In README.md
3. **Auto-stage**: Reformatted files

### Post-commit Hook

Runs after each commit:

1. **Read Version**: From pyproject.toml
2. **Create/Update Tags**: `v<version>` and `v<major>-latest`
3. **Build Package**: Via build script

### Pre-commit Framework

Additional hooks via `.pre-commit-config.yaml`:

- File hygiene checks
- YAML/TOML validation
- Security checks
- Debug statement detection

## Testing

### Test Structure

```text
tests/
├── conftest.py              # Fixtures and hooks
├── run_tests.py             # CLI test runner
├── unit/                    # 10 test files
├── integration/             # 3 test files
└── robustness/              # 3 test files
```

### Writing Tests

```python
import pytest
from ezpl import Ezpl

def test_should_create_singleton_when_first_call():
    """Test that Ezpl creates singleton on first call."""
    ezpl1 = Ezpl()
    ezpl2 = Ezpl()
    assert ezpl1 is ezpl2

def test_should_log_message_when_info_called(ezpl_instance):
    """Test that printer logs info message."""
    printer = ezpl_instance.get_printer()
    printer.info("Test message")
    # Assertions...
```

### Test Naming Convention

```python
def test_should_<expected_behavior>_when_<condition>():
    ...
```

### Running Tests

```bash
# All tests
python tests/run_tests.py --type all

# Unit tests only
python tests/run_tests.py --type unit

# With coverage
python tests/run_tests.py --type all --coverage

# Parallel execution
python tests/run_tests.py --parallel

# Exclude slow tests
python tests/run_tests.py --fast

# Specific marker
python tests/run_tests.py --marker wizard
```

### Test Markers

- `@pytest.mark.unit` - Unit tests
- `@pytest.mark.integration` - Integration tests
- `@pytest.mark.robustness` - Robustness tests
- `@pytest.mark.slow` - Slow tests
- `@pytest.mark.wizard` - RichWizard tests
- `@pytest.mark.config` - Configuration tests
- `@pytest.mark.cli` - CLI tests

## Building

### Build Package

```bash
# Clean previous builds
rm -rf build/ dist/ *.egg-info/

# Build
python -m build

# Check package
twine check dist/*
```

### Test Installation

```bash
# Install from wheel
pip install dist/*.whl --force-reinstall

# Test import
python -c "import ezpl; print(ezpl.__version__)"
```

## Documentation

### Building Docs Locally

```bash
# Install docs dependencies
pip install -e ".[docs]"

# Serve docs locally
mkdocs serve

# Build docs
mkdocs build
```

### Deploying Docs

Docs are automatically deployed via GitHub Actions on push to main:

```yaml
# .github/workflows/docs.yml
on:
  push:
    branches: [main]
    paths:
      - "docs/**"
      - "mkdocs.yml"
      - "ezpl/**"
```

## CI/CD

### GitHub Actions Workflows

#### PyPI Publication

Triggered on version tag push (`v*.*.*`):

1. **Validate**: Version consistency, tag on main branch
2. **Test**: Run full test suite
3. **Build**: Create wheel and source distribution
4. **Publish**: Upload to PyPI

#### Documentation Deployment

Triggered on docs changes:

1. **Install**: Package with docs dependencies
2. **Build**: Generate documentation with mkdocs
3. **Deploy**: Deploy to GitHub Pages

## Release Process

### 1. Update Version

```toml
# pyproject.toml
[project]
version = "1.5.2"
```

```python
# ezpl/__init__.py
__version__ = "1.5.2"
```

### 2. Update CHANGELOG

Document changes in CHANGELOG.md (if exists).

### 3. Commit and Push

```bash
git add pyproject.toml ezpl/__init__.py
git commit -m "chore: bump version to 1.5.2"
git push origin main
```

The post-commit hook will automatically:

- Create tag `v1.5.2`
- Create/update tag `v1-latest`
- Build package

### 4. Verify and Push Tags

```bash
# Verify tags
git tag -l

# Push tags (triggers PyPI workflow)
git push origin v1.5.2
git push origin v1-latest --force
```

## Troubleshooting

### Common Issues

#### Import Errors in Tests

```bash
# Reinstall in editable mode
pip install -e ".[dev]"
```

#### Type Check Failures

```bash
# Run pyright with verbose output
pyright ezpl/ --verbose
```

#### Test Failures on Windows

Some tests may fail on Windows due to file locking:

- The test suite includes Windows-specific teardown handling
- Use `gc.collect()` and delays in fixtures

#### Git Hooks Not Running

```bash
# Verify hooks path
git config core.hooksPath

# Set hooks path
git config core.hooksPath .hooks

# Make hooks executable (Unix)
chmod +x .hooks/*
```

## Best Practices

### Code Quality

1. **Always run tests** before committing
2. **Use type hints** for all public APIs
3. **Write docstrings** for all public functions/classes
4. **Keep functions small** (max complexity: 10)
5. **Avoid global state** (except singleton)

### Test Practices

1. **Test behavior, not implementation**
2. **Use descriptive test names**
3. **Include edge cases**
4. **Mock external dependencies**
5. **Maintain high coverage** (target: 65%+)

### Git Commits

Follow conventional commits:

- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `chore:` - Maintenance tasks
- `refactor:` - Code refactoring
- `test:` - Test changes
- `style:` - Code style changes

### Pull Requests

1. **Clear title and description**
2. **Reference issues** (#123)
3. **Include tests** for new features
4. **Update documentation** if needed
5. **Ensure CI passes**

## Contributing Guidelines

### Before Contributing

1. Check existing issues and PRs
2. Discuss major changes in an issue first
3. Read `.github/instructions/` for project guidelines

### Contribution Process

1. Fork the repository
2. Create a feature branch
3. Make changes following coding standards
4. Add tests for new features
5. Run full test suite
6. Submit Pull Request

### Code Review

- Be respectful and constructive
- Address all review comments
- Keep discussions focused on code
- Be patient during the review process

## Resources

### Internal Documentation

- `.github/instructions/README.md` - Project instructions
- `.github/instructions/core/` - Core principles
- `.github/instructions/languages/python/` - Python standards
- `CLAUDE.md` - Claude-specific instructions

### External Resources

- [Black Documentation](https://black.readthedocs.io/)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [pytest Documentation](https://docs.pytest.org/)
- [mkdocs Documentation](https://www.mkdocs.org/)
- [Rich Documentation](https://rich.readthedocs.io/)
- [loguru Documentation](https://loguru.readthedocs.io/)

## Need Help?

- **Issues**: [GitHub Issues](https://github.com/neuraaak/ezplog/issues)
- **Discussions**: [GitHub Discussions](https://github.com/neuraaak/ezplog/discussions)
- **Repository**: [https://github.com/neuraaak/ezplog](https://github.com/neuraaak/ezplog)
