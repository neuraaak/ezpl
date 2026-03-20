# CLI Reference

Command-line interface documentation for **Ezpl** logging framework.

## Overview

The Ezpl CLI provides comprehensive tools for managing configuration, viewing logs, and performing various operations from the command line.

## Features

- **📊 Log Management**: View, search, tail, export, and clean log files
- **⚙️ Configuration**: Get, set, and reset configuration values
- **🔍 Statistics**: Analyze log statistics with temporal distribution
- **📤 Export**: Export logs to JSON, CSV, or TXT formats
- **🌍 Environment**: Manage environment variables

## Quick Start

### Installation

The CLI is automatically available when Ezpl is installed:

```bash
pip install ezplog
```

### Basic Usage

```bash
# Display help
ezpl --help

# View logs
ezpl logs view --lines 50

# Search logs
ezpl logs search --pattern "error" --level ERROR

# Get configuration
ezpl config show

# Set configuration
ezpl config set log_level DEBUG

# Display version
ezpl version
```

## Command Categories

| Category                              | Commands                                       | Description              |
| ------------------------------------- | ---------------------------------------------- | ------------------------ |
| **[Logs](#logs-commands)**            | view, search, stats, tail, list, clean, export | Log file operations      |
| **[Config](#configuration-commands)** | show, set, reset, export                       | Configuration management |
| **[Info](#utility-commands)**         | version, info                                  | Package information      |

## Logs Commands

### `ezpl logs view`

View log file contents with optional filtering.

```bash
ezpl logs view [OPTIONS]
```

**Options:**

- `--file, -f PATH`: Path to log file (default: from config)
- `--lines, -n N`: Number of lines to display (default: 50)
- `--level, -l LEVEL`: Filter by log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- `--follow, -F`: Follow log file (like `tail -f`)

**Examples:**

```bash
# View last 100 lines
ezpl logs view --lines 100

# View errors only and follow
ezpl logs view --level ERROR --follow

# View specific file
ezpl logs view --file /path/to/app.log
```

### `ezpl logs search`

Search log entries using regex patterns.

```bash
ezpl logs search --pattern PATTERN [OPTIONS]
```

**Options:**

- `--pattern, -p PATTERN`: Search pattern (regex supported) **[required]**
- `--file, -f PATH`: Path to log file (default: from config)
- `--level, -l LEVEL`: Filter by log level
- `--case-sensitive, -c`: Case-sensitive search

**Examples:**

```bash
# Search for errors or exceptions
ezpl logs search --pattern "error|exception"

# Case-sensitive search in ERROR level
ezpl logs search --pattern "Database" --level ERROR --case-sensitive
```

### `ezpl logs stats`

Display statistics about log files.

```bash
ezpl logs stats [OPTIONS]
```

**Options:**

- `--file, -f PATH`: Path to log file (default: from config)
- `--format, -F FORMAT`: Output format: `table` (default) or `json`

**Examples:**

```bash
# Display stats in table format
ezpl logs stats

# Export stats as JSON
ezpl logs stats --format json > stats.json
```

**Output includes:**

- Total lines
- Log level distribution
- File size
- Date range
- Error rate

### `ezpl logs tail`

Display the last lines of a log file.

```bash
ezpl logs tail [OPTIONS]
```

**Options:**

- `--file, -f PATH`: Path to log file (default: from config)
- `--lines, -n N`: Number of lines to display (default: 20)
- `--follow, -F`: Follow log file continuously

**Examples:**

```bash
# Tail last 20 lines
ezpl logs tail

# Follow log file
ezpl logs tail --lines 50 --follow
```

### `ezpl logs list`

List available log files.

```bash
ezpl logs list [OPTIONS]
```

**Options:**

- `--dir, -d PATH`: Directory to search (default: from config)

**Examples:**

```bash
# List log files in default directory
ezpl logs list

# List log files in specific directory
ezpl logs list --dir /var/log/myapp
```

### `ezpl logs clean`

Clean old or large log files.

```bash
ezpl logs clean [OPTIONS]
```

**Options:**

- `--file, -f PATH`: Specific file to clean
- `--days, -d N`: Delete files older than N days
- `--size, -s SIZE`: Delete files larger than SIZE (e.g., '100MB')
- `--confirm, -y`: Skip confirmation prompt

**Examples:**

```bash
# Clean files older than 30 days
ezpl logs clean --days 30

# Clean files larger than 500MB (no confirmation)
ezpl logs clean --size 500MB --confirm
```

### `ezpl logs export`

Export log file to different formats.

```bash
ezpl logs export [OPTIONS]
```

**Options:**

- `--file, -f PATH`: Path to log file (default: from config)
- `--format, -F FORMAT`: Export format: `json` (default), `csv`, or `txt`
- `--output, -o PATH`: Output file path (default: stdout)

**Examples:**

```bash
# Export to JSON
ezpl logs export --format json --output logs.json

# Export to CSV
ezpl logs export --format csv --output logs.csv

# Export to stdout
ezpl logs export --format json
```

## Configuration Commands

### `ezpl config show`

Display current configuration.

```bash
ezpl config show [OPTIONS]
```

**Options:**

- `--env, -e`: Also show environment variables

**Examples:**

```bash
# Show current configuration
ezpl config show

# Show with environment variables
ezpl config show --env
```

### `ezpl config set`

Set a configuration value.

```bash
ezpl config set KEY VALUE [OPTIONS]
```

**Options:**

- `KEY`: Configuration key
- `VALUE`: Configuration value
- `--env, -e`: Also set as environment variable

**Available Keys:**

- `log_level`: Global log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- `log_file`: Log file name
- `printer_level`: Console output level
- `file_logger_level`: File logging level
- `log_rotation`: Rotation setting (e.g., "10 MB", "1 day")
- `log_retention`: Retention period (e.g., "7 days")
- `log_compression`: Compression format (e.g., "zip", "gz")
- `indent_step`: Indentation step size
- `indent_symbol`: Symbol for indentation
- `base_indent_symbol`: Base indentation symbol

**Examples:**

```bash
# Set log level
ezpl config set log_level DEBUG

# Set with environment variable
ezpl config set log_level DEBUG --env

# Set rotation
ezpl config set log_rotation "10 MB"
```

### `ezpl config reset`

Reset configuration to default values.

```bash
ezpl config reset [OPTIONS]
```

**Options:**

- `--confirm, -y`: Skip confirmation prompt

**Examples:**

```bash
# Reset with confirmation
ezpl config reset

# Reset without confirmation
ezpl config reset --confirm
```

### `ezpl config export`

Export configuration as environment variables script.

```bash
ezpl config export [OPTIONS]
```

**Options:**

- `--output, -o PATH`: Output file path
- `--platform, -p PLATFORM`: Platform (unix, windows)

**Examples:**

```bash
# Export for Unix
ezpl config export --output env.sh --platform unix

# Export for Windows
ezpl config export --output env.bat --platform windows
```

**Generated script:**

```bash
# Unix (env.sh)
export EZPL_LOG_LEVEL="INFO"
export EZPL_LOG_FILE="ezpl.log"
# ...

# Windows (env.bat)
set EZPL_LOG_LEVEL=INFO
set EZPL_LOG_FILE=ezpl.log
```

## Utility Commands

### `ezpl version`

Display version information.

```bash
ezpl version [OPTIONS]
```

**Options:**

- `--full, -f`: Display full version information

**Examples:**

```bash
# Simple version
ezpl version
# Output: 2.0.1

# Full version info
ezpl version --full
# Output:
# ezplog version 2.0.1
# Python 3.11.0
# Platform: linux
```

### `ezpl info`

Display package information.

```bash
ezpl info
```

Shows detailed information including:

- Package version
- Installation location
- Configuration paths
- Python version
- Core dependencies

**Example output:**

```text
ezplog Package Information
==========================
Version: 2.0.1
Location: /usr/local/lib/python3.11/site-packages/ezplog
Config Dir: /home/user/.ezpl
Python: 3.11.0

Dependencies:
- loguru: 0.7.2
- rich: 13.7.0
- click: 8.1.7
```

## Environment Variables

Ezpl supports the following environment variables:

| Variable                  | Description        | Default           |
| ------------------------- | ------------------ | ----------------- |
| `EZPL_LOG_LEVEL`          | Global log level   | `INFO`            |
| `EZPL_LOG_FILE`           | Log file name      | `ezpl.log`        |
| `EZPL_LOG_DIR`            | Log directory      | Platform-specific |
| `EZPL_PRINTER_LEVEL`      | Console level      | `INFO`            |
| `EZPL_FILE_LOGGER_LEVEL`  | File level         | `INFO`            |
| `EZPL_LOG_ROTATION`       | Rotation setting   | `None`            |
| `EZPL_LOG_RETENTION`      | Retention period   | `None`            |
| `EZPL_LOG_COMPRESSION`    | Compression format | `None`            |
| `EZPL_INDENT_STEP`        | Indentation step   | `3`               |
| `EZPL_INDENT_SYMBOL`      | Indent symbol      | `>`               |
| `EZPL_BASE_INDENT_SYMBOL` | Base indent symbol | `~`               |

### Setting Environment Variables

**Unix/Linux/macOS:**

```bash
export EZPL_LOG_LEVEL=DEBUG
export EZPL_LOG_FILE=app.log
export EZPL_LOG_ROTATION="10 MB"
```

**Windows:**

```bat
set EZPL_LOG_LEVEL=DEBUG
set EZPL_LOG_FILE=app.log
set EZPL_LOG_ROTATION=10 MB
```

**Using CLI:**

```bash
ezpl config set log_level DEBUG --env
```

## Best Practices

### Configuration Management

1. **Use environment variables for environment-specific settings:**

   ```bash
   # Development
   export EZPL_LOG_LEVEL=DEBUG

   # Production
   export EZPL_LOG_LEVEL=ERROR
   ```

2. **Check configuration before setting:**

   ```bash
   ezpl config show
   ezpl config set log_level DEBUG
   ```

3. **Export configuration for team sharing:**

   ```bash
   ezpl config export --output team-env.sh
   ```

### Log Management

1. **Use tail --follow for real-time monitoring:**

   ```bash
   ezpl logs tail --follow
   ```

2. **Export logs before cleaning:**

   ```bash
   ezpl logs export --format json --output backup.json
   ezpl logs clean --days 30 --confirm
   ```

3. **Use search with level filtering:**

   ```bash
   ezpl logs search --pattern "error" --level ERROR
   ```

4. **Check statistics regularly:**

   ```bash
   ezpl logs stats
   ```

### Automation

**Example: Daily log backup script (Unix):**

```bash
#!/bin/bash
DATE=$(date +%Y%m%d)
ezpl logs export --format json --output "backup-$DATE.json"
ezpl logs clean --days 7 --confirm
ezpl logs stats --format json > "stats-$DATE.json"
```

**Example: Log monitoring script:**

```bash
#!/bin/bash
while true; do
    ezpl logs search --pattern "error|exception" --level ERROR
    sleep 60
done
```

## Configuration File

Configuration is stored in `~/.ezpl/config.json`:

```json
{
  "log-level": "INFO",
  "log-file": "ezpl.log",
  "printer-level": "INFO",
  "file-logger-level": "DEBUG",
  "log-rotation": "10 MB",
  "log-retention": "7 days",
  "log-compression": "zip",
  "indent-step": 3,
  "indent-symbol": ">",
  "base-indent-symbol": "~"
}
```

## See Also

- [Getting Started](../getting-started.md) - Basic usage guide
- [User Guides](../guides/index.md) - Complete guides of project
- [API Reference](../api/index.md) - Complete API documentation
- [Examples](../examples/index.md) - Practical examples

## Need Help?

- **Issues**: [GitHub Issues](https://github.com/neuraaak/ezplog/issues)
- **Repository**: [https://github.com/neuraaak/ezplog](https://github.com/neuraaak/ezplog)
