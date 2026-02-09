# Configuration Guide

Comprehensive guide to configuring **Ezpl** logging framework.

## Overview

Ezpl provides flexible configuration management through multiple sources with a clear priority order:

1. **Direct arguments** to `Ezpl()`
2. **Environment variables** (`EZPL_*` prefix)
3. **Configuration file** (`~/.ezpl/config.json`)
4. **Default values**

## Configuration Sources

### 1. Direct Arguments (Highest Priority)

Pass configuration directly to the `Ezpl()` constructor:

```python
from ezpl import Ezpl

ezpl = Ezpl(
    log_file="app.log",
    log_level="DEBUG",
    printer_level="INFO",
    file_logger_level="DEBUG",
    log_rotation="10 MB",
    log_retention="7 days",
    log_compression="zip",
    indent_step=3,
    indent_symbol=">",
    base_indent_symbol="~"
)
```

**Available Parameters:**

| Parameter            | Type          | Description        | Default      |
| -------------------- | ------------- | ------------------ | ------------ |
| `log_file`           | `str \| Path` | Log file path      | `"ezpl.log"` |
| `log_level`          | `str`         | Global log level   | `"INFO"`     |
| `printer_level`      | `str`         | Console level      | `"INFO"`     |
| `file_logger_level`  | `str`         | File level         | `"INFO"`     |
| `log_rotation`       | `str`         | Rotation setting   | `None`       |
| `log_retention`      | `str`         | Retention period   | `None`       |
| `log_compression`    | `str`         | Compression format | `None`       |
| `indent_step`        | `int`         | Indentation step   | `3`          |
| `indent_symbol`      | `str`         | Indent symbol      | `">"`        |
| `base_indent_symbol` | `str`         | Base indent symbol | `"~"`        |

### 2. Environment Variables

Set environment variables with the `EZPL_` prefix:

**Unix/Linux/macOS:**

```bash
export EZPL_LOG_LEVEL=DEBUG
export EZPL_LOG_FILE=app.log
export EZPL_PRINTER_LEVEL=INFO
export EZPL_FILE_LOGGER_LEVEL=DEBUG
export EZPL_LOG_ROTATION="10 MB"
export EZPL_LOG_RETENTION="7 days"
export EZPL_LOG_COMPRESSION=zip
export EZPL_INDENT_STEP=3
export EZPL_INDENT_SYMBOL=">"
export EZPL_BASE_INDENT_SYMBOL="~"
```

**Windows:**

```bat
set EZPL_LOG_LEVEL=DEBUG
set EZPL_LOG_FILE=app.log
set EZPL_PRINTER_LEVEL=INFO
set EZPL_FILE_LOGGER_LEVEL=DEBUG
set EZPL_LOG_ROTATION=10 MB
set EZPL_LOG_RETENTION=7 days
set EZPL_LOG_COMPRESSION=zip
set EZPL_INDENT_STEP=3
set EZPL_INDENT_SYMBOL=>
set EZPL_BASE_INDENT_SYMBOL=~
```

**Using CLI:**

```bash
ezpl config set log_level DEBUG --env
ezpl config set log_rotation "10 MB" --env
```

**Available Environment Variables:**

| Variable                  | Description        | Default           |
| ------------------------- | ------------------ | ----------------- |
| `EZPL_LOG_LEVEL`          | Global log level   | `INFO`            |
| `EZPL_LOG_FILE`           | Log file name      | `ezpl.log`        |
| `EZPL_LOG_DIR`            | Log directory      | Current directory |
| `EZPL_PRINTER_LEVEL`      | Console level      | `INFO`            |
| `EZPL_FILE_LOGGER_LEVEL`  | File level         | `INFO`            |
| `EZPL_LOG_ROTATION`       | Rotation setting   | `None`            |
| `EZPL_LOG_RETENTION`      | Retention period   | `None`            |
| `EZPL_LOG_COMPRESSION`    | Compression format | `None`            |
| `EZPL_INDENT_STEP`        | Indentation step   | `3`               |
| `EZPL_INDENT_SYMBOL`      | Indent symbol      | `>`               |
| `EZPL_BASE_INDENT_SYMBOL` | Base indent symbol | `~`               |
| `EZPL_LOG_FORMAT`         | Log format string  | Default format    |

### 3. Configuration File

Create `~/.ezpl/config.json`:

```json
{
  "log_level": "INFO",
  "log_file": "ezpl.log",
  "printer_level": "INFO",
  "file_logger_level": "DEBUG",
  "log_rotation": "10 MB",
  "log_retention": "7 days",
  "log_compression": "zip",
  "indent_step": 3,
  "indent_symbol": ">",
  "base_indent_symbol": "~"
}
```

**Creating Configuration:**

```python
from ezpl import Ezpl

# Initialize with desired settings
ezpl = Ezpl(
    log_level="DEBUG",
    log_rotation="10 MB"
)

# Save to configuration file
config = ezpl.get_config()
config.save()
```

**Or using CLI:**

```bash
ezpl config set log_level DEBUG
ezpl config set log_rotation "10 MB"
```

### 4. Default Values

If no configuration is provided, Ezpl uses these defaults:

```python
DEFAULT_LOG_LEVEL = "INFO"
DEFAULT_LOG_FILE = "ezpl.log"
DEFAULT_PRINTER_LEVEL = "INFO"
DEFAULT_FILE_LOGGER_LEVEL = "INFO"
DEFAULT_INDENT_STEP = 3
DEFAULT_INDENT_SYMBOL = ">"
DEFAULT_BASE_INDENT_SYMBOL = "~"
```

## Log Levels

Available log levels (case-insensitive):

| Level      | Usage                  | Console Color  |
| ---------- | ---------------------- | -------------- |
| `DEBUG`    | Debugging information  | Cyan           |
| `INFO`     | Informational messages | Blue           |
| `SUCCESS`  | Success operations     | Green          |
| `WARNING`  | Warning messages       | Yellow         |
| `ERROR`    | Error messages         | Red            |
| `CRITICAL` | Critical errors        | Magenta on red |

**Setting Levels:**

```python
from ezpl import Ezpl

ezpl = Ezpl()

# Global level (affects both)
ezpl.set_level("DEBUG")

# Specific levels
ezpl.set_printer_level("INFO")   # Console
ezpl.set_logger_level("DEBUG")   # File
```

## Log Rotation

Configure automatic log file rotation:

### Size-Based Rotation

```python
ezpl = Ezpl(log_rotation="10 MB")
ezpl = Ezpl(log_rotation="500 KB")
ezpl = Ezpl(log_rotation="1 GB")
```

### Time-Based Rotation

```python
# Daily at midnight
ezpl = Ezpl(log_rotation="00:00")

# Daily at specific time
ezpl = Ezpl(log_rotation="12:00")

# Every X hours/days/weeks
ezpl = Ezpl(log_rotation="12 hours")
ezpl = Ezpl(log_rotation="1 day")
ezpl = Ezpl(log_rotation="1 week")
```

### Rotation Examples

| Setting      | Behavior                        |
| ------------ | ------------------------------- |
| `"10 MB"`    | Rotate when file reaches 10 MB  |
| `"500 KB"`   | Rotate when file reaches 500 KB |
| `"1 GB"`     | Rotate when file reaches 1 GB   |
| `"00:00"`    | Rotate daily at midnight        |
| `"12:00"`    | Rotate daily at noon            |
| `"12 hours"` | Rotate every 12 hours           |
| `"1 day"`    | Rotate every day                |
| `"1 week"`   | Rotate every week               |

## Log Retention

Configure how long to keep rotated log files:

### Time-Based Retention

```python
ezpl = Ezpl(log_retention="7 days")
ezpl = Ezpl(log_retention="1 week")
ezpl = Ezpl(log_retention="1 month")
```

### Count-Based Retention

```python
ezpl = Ezpl(log_retention="10 files")
ezpl = Ezpl(log_retention="20 files")
```

### Retention Examples

| Setting      | Behavior                   |
| ------------ | -------------------------- |
| `"7 days"`   | Keep logs for 7 days       |
| `"1 week"`   | Keep logs for 1 week       |
| `"1 month"`  | Keep logs for 1 month      |
| `"30 days"`  | Keep logs for 30 days      |
| `"10 files"` | Keep last 10 rotated files |
| `"20 files"` | Keep last 20 rotated files |

## Log Compression

Compress rotated log files:

```python
# ZIP compression
ezpl = Ezpl(log_compression="zip")

# GZIP compression
ezpl = Ezpl(log_compression="gz")

# TAR.GZ compression
ezpl = Ezpl(log_compression="tar.gz")
```

**Compression Formats:**

| Format     | Extension | Compression |
| ---------- | --------- | ----------- |
| `"zip"`    | `.zip`    | ZIP         |
| `"gz"`     | `.gz`     | GZIP        |
| `"tar.gz"` | `.tar.gz` | TAR + GZIP  |

## Complete Configuration Example

```python
from ezpl import Ezpl

# Production configuration
ezpl = Ezpl(
    log_file="/var/log/myapp/app.log",
    log_level="INFO",
    printer_level="WARNING",      # Less verbose console
    file_logger_level="DEBUG",    # Detailed file logs
    log_rotation="10 MB",          # Rotate at 10 MB
    log_retention="30 days",       # Keep 30 days
    log_compression="gz"           # GZIP compress old logs
)
```

## Runtime Reconfiguration

### Using configure()

```python
from ezpl import Ezpl

ezpl = Ezpl()

# Reconfigure at runtime
ezpl.configure(
    printer_level="DEBUG",
    logger_level="INFO",
    log_rotation="5 MB"
)
```

### Using set_level()

```python
ezpl = Ezpl()

# Change levels dynamically
ezpl.set_level("DEBUG")
ezpl.set_printer_level("INFO")
ezpl.set_logger_level("ERROR")
```

### Reloading Configuration

```python
ezpl = Ezpl()

# Reload from file and environment
ezpl.reload_config()
```

## Configuration Manager

Access the configuration manager directly:

```python
from ezpl import Ezpl

ezpl = Ezpl()
config = ezpl.get_config()

# Get values
log_level = config.get_log_level()
log_file = config.get_log_file()

# Set values
config.set("log_level", "DEBUG")
config.set("log_rotation", "10 MB")

# Save to file
config.save()

# Get all configuration
all_config = config.get_all()

# Reset to defaults
config.reset_to_defaults()
```

## Configuration Locking

Prevent configuration changes (useful for libraries):

```python
from ezpl import Ezpl

ezpl = Ezpl(log_level="INFO")

# Lock configuration
ezpl.lock_config()

# This will emit warning and have no effect
ezpl.set_level("DEBUG")

# Force change (bypasses lock)
ezpl.set_level("DEBUG", force=True)

# Unlock configuration
ezpl.unlock_config()
```

## Environment-Specific Configuration

### Development

```python
import os

if os.getenv("ENV") == "development":
    ezpl = Ezpl(
        log_level="DEBUG",
        printer_level="DEBUG",
        file_logger_level="DEBUG"
    )
else:
    ezpl = Ezpl(
        log_level="INFO",
        printer_level="WARNING",
        file_logger_level="INFO"
    )
```

### Using Environment Variables

```bash
# Development
export ENV=development
export EZPL_LOG_LEVEL=DEBUG

# Production
export ENV=production
export EZPL_LOG_LEVEL=INFO
export EZPL_PRINTER_LEVEL=WARNING
```

## Configuration Export

Export configuration as environment variables script:

```python
from ezpl import Ezpl

ezpl = Ezpl(log_level="DEBUG", log_rotation="10 MB")
config = ezpl.get_config()

# Export for Unix
config.export_to_script("env.sh", platform="unix")

# Export for Windows
config.export_to_script("env.bat", platform="windows")
```

**Or using CLI:**

```bash
ezpl config export --output env.sh --platform unix
ezpl config export --output env.bat --platform windows
```

**Generated scripts:**

```bash
# env.sh (Unix)
export EZPL_LOG_LEVEL="DEBUG"
export EZPL_LOG_FILE="ezpl.log"
export EZPL_LOG_ROTATION="10 MB"
```

```bat
# env.bat (Windows)
set EZPL_LOG_LEVEL=DEBUG
set EZPL_LOG_FILE=ezpl.log
set EZPL_LOG_ROTATION=10 MB
```

## Best Practices

### 1. Use Configuration File for Defaults

Create `~/.ezpl/config.json` with sensible defaults for your environment.

### 2. Use Environment Variables for Environment-Specific Settings

Set environment variables in your deployment environment (development, staging, production).

### 3. Use Direct Arguments for Application-Specific Settings

Pass specific configuration when initializing Ezpl in your application.

### 4. Separate Console and File Levels

```python
ezpl = Ezpl(
    printer_level="WARNING",   # Less verbose console
    file_logger_level="DEBUG"  # Detailed file logs
)
```

### 5. Configure Rotation and Retention

```python
ezpl = Ezpl(
    log_rotation="10 MB",
    log_retention="30 days",
    log_compression="gz"
)
```

### 6. Use Configuration Locking in Libraries

```python
# In library code
ezpl = Ezpl()
ezpl.lock_config()  # Prevent application from changing library's log level
```

### 7. Document Your Configuration

```python
# config.json with comments (use JSON5 if available)
{
  // Global log level for both console and file
  "log_level": "INFO",

  // Rotate logs at 10 MB
  "log_rotation": "10 MB",

  // Keep logs for 30 days
  "log_retention": "30 days",

  // Compress old logs with GZIP
  "log_compression": "gz"
}
```

## Troubleshooting

### Configuration Not Applied

1. Check configuration priority order
2. Verify environment variables are set
3. Check config file location (`~/.ezpl/config.json`)
4. Use `ezpl config show` to see current configuration

### Environment Variables Not Working

```bash
# Verify variables are set
echo $EZPL_LOG_LEVEL  # Unix
echo %EZPL_LOG_LEVEL%  # Windows

# Check in Python
import os
print(os.getenv("EZPL_LOG_LEVEL"))
```

### Configuration File Not Found

```python
from pathlib import Path

config_path = Path.home() / ".ezpl" / "config.json"
print(f"Config file: {config_path}")
print(f"Exists: {config_path.exists()}")
```

### Rotation Not Working

Verify rotation setting format:

```python
# Correct
ezpl = Ezpl(log_rotation="10 MB")

# Incorrect
ezpl = Ezpl(log_rotation="10MB")  # Missing space
```

## See Also

- [Getting Started](../getting-started.md) - Basic usage
- [CLI Reference](../cli/index.md) - CLI configuration commands
- [API Reference](../api/index.md) - Configuration API
- [Examples](../examples/index.md) - Configuration examples

## Need Help?

- **Issues**: [GitHub Issues](https://github.com/neuraaak/ezplog/issues)
- **Repository**: [https://github.com/neuraaak/ezplog](https://github.com/neuraaak/ezplog)
