# CLI Documentation – Ezpl

## Overview

This folder contains the complete documentation of the **CLI** (Command Line Interface) for the **Ezpl** logging framework. The CLI provides comprehensive tools for managing configuration, viewing logs, and performing various operations.

## General Overview

The Ezpl CLI provides tools to:

- **Manage configuration** with support for user environment variables
- **View and search logs** with advanced filtering and formatting
- **Analyze log statistics** with temporal distribution
- **Export logs** to multiple formats (JSON, CSV, TXT)
- **Clean and maintain** log files

## Documentation Structure

### 📋 Main Documentation

- **README.md** (this file) – Overview of CLI commands
  - Presentation of available commands
  - Parameters, options, usage examples
  - Best practices

### 🛠️ Configuration Guide

- **CONFIG_GUIDE.md** – CLI integration and configuration guide
  - Usage with different environments
  - Configuration examples
  - Environment variables management

## Quick Start

### Installation

The CLI is automatically available when Ezpl is installed:

```bash
pip install ezpl
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
ezpl config get

# Set configuration with environment variable
ezpl config set log-level DEBUG --env
```

## Commands Reference

### 📊 Logs Commands

#### `ezpl logs view`

View log file contents with optional filtering.

```bash
ezpl logs view [--file PATH] [--lines N] [--level LEVEL] [--follow]
```

**Options:**

- `--file, -f`: Path to log file (default: from config)
- `--lines, -n`: Number of lines to display (default: 50)
- `--level, -l`: Filter by log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- `--follow, -F`: Follow log file (like `tail -f`)

**Examples:**

```bash
ezpl logs view --lines 100
ezpl logs view --level ERROR --follow
ezpl logs view --file /path/to/app.log
```

#### `ezpl logs search`

Search log entries using regex patterns.

```bash
ezpl logs search --pattern PATTERN [--file PATH] [--level LEVEL] [--case-sensitive]
```

**Options:**

- `--pattern, -p`: Search pattern (regex supported) **[required]**
- `--file, -f`: Path to log file (default: from config)
- `--level, -l`: Filter by log level
- `--case-sensitive, -c`: Case-sensitive search

**Examples:**

```bash
ezpl logs search --pattern "error|exception"
ezpl logs search --pattern "database" --level ERROR --case-sensitive
```

#### `ezpl logs stats`

Display statistics about log files.

```bash
ezpl logs stats [--file PATH] [--format json|table]
```

**Options:**

- `--file, -f`: Path to log file (default: from config)
- `--format, -F`: Output format: `table` (default) or `json`

**Examples:**

```bash
ezpl logs stats
ezpl logs stats --format json
```

#### `ezpl logs tail`

Display the last lines of a log file.

```bash
ezpl logs tail [--file PATH] [--lines N] [--follow]
```

**Options:**

- `--file, -f`: Path to log file (default: from config)
- `--lines, -n`: Number of lines to display (default: 20)
- `--follow, -F`: Follow log file (like `tail -f`)

**Examples:**

```bash
ezpl logs tail
ezpl logs tail --lines 50 --follow
```

#### `ezpl logs list`

List available log files.

```bash
ezpl logs list [--dir PATH]
```

**Options:**

- `--dir, -d`: Directory to search (default: from config)

**Examples:**

```bash
ezpl logs list
ezpl logs list --dir /path/to/logs
```

#### `ezpl logs clean`

Clean old or large log files.

```bash
ezpl logs clean [--file PATH] [--days N] [--size SIZE] [--confirm]
```

**Options:**

- `--file, -f`: Specific file to clean
- `--days, -d`: Delete files older than N days
- `--size, -s`: Delete files larger than SIZE (e.g., '100MB')
- `--confirm, -y`: Skip confirmation prompt

**Examples:**

```bash
ezpl logs clean --days 30
ezpl logs clean --size 500MB --confirm
```

#### `ezpl logs export`

Export log file to different formats.

```bash
ezpl logs export [--file PATH] [--format json|csv|txt] [--output OUTPUT]
```

**Options:**

- `--file, -f`: Path to log file (default: from config)
- `--format, -F`: Export format: `json` (default), `csv`, or `txt`
- `--output, -o`: Output file path (default: stdout)

**Examples:**

```bash
ezpl logs export --format json --output logs.json
ezpl logs export --format csv --output logs.csv
```

### ⚙️ Configuration Commands

#### `ezpl config get`

Get configuration value(s).

```bash
ezpl config get [KEY] [--show-env]
```

**Options:**

- `KEY`: Configuration key (optional, shows all if omitted)
- `--show-env, -e`: Show environment variable names for each key

**Examples:**

```bash
ezpl config get
ezpl config get log-level
ezpl config get --show-env
```

#### `ezpl config set`

Set a configuration value.

```bash
ezpl config set KEY VALUE [--env]
```

**Options:**

- `KEY`: Configuration key (must be predefined)
- `VALUE`: Configuration value
- `--env, -e`: Also set as user environment variable (uses predefined variable name)

**Available Keys:**

- `log-level`: Global log level
- `log-file`: Log file name
- `log-dir`: Log directory path
- `printer-level`: Printer log level
- `file-logger-level`: File logger level
- `indent-step`: Indentation step size
- `indent-symbol`: Symbol for indentation
- `base-indent-symbol`: Base indentation symbol
- `log-format`: Log format string
- `log-rotation`: Rotation setting (e.g., "10 MB", "1 day")
- `log-retention`: Retention period (e.g., "7 days")
- `log-compression`: Compression format (e.g., "zip", "gz")

**Examples:**

```bash
ezpl config set log-level DEBUG
ezpl config set log-level DEBUG --env
ezpl config set log-rotation "10 MB"
```

#### `ezpl config reset`

Reset configuration to default values.

```bash
ezpl config reset [--confirm]
```

**Options:**

- `--confirm, -y`: Skip confirmation prompt

**Note:** This will also remove all user environment variables created by Ezpl.

**Examples:**

```bash
ezpl config reset
ezpl config reset --confirm
```

### 🛠️ Utility Commands

#### `ezpl version`

Display version information.

```bash
ezpl version [--full]
```

**Options:**

- `--full, -f`: Display full version information

**Examples:**

```bash
ezpl version
ezpl version --full
```

#### `ezpl info`

Display package information.

```bash
ezpl info
```

Shows detailed information about the Ezpl package including version, location, configuration paths, and dependencies.

## Best Practices

### Configuration Management

1. **Use environment variables for sensitive or environment-specific settings:**

   ```bash
   ezpl config set log-level DEBUG --env
   ```

2. **Check available keys before setting:**

   ```bash
   ezpl config get --show-env
   ```

3. **Reset configuration when switching projects:**
   ```bash
   ezpl config reset --confirm
   ```

### Log Management

1. **Use `tail --follow` for real-time monitoring:**

   ```bash
   ezpl logs tail --follow
   ```

2. **Export logs before cleaning:**

   ```bash
   ezpl logs export --format json --output backup.json
   ezpl logs clean --days 30 --confirm
   ```

3. **Use search with level filtering for focused analysis:**

   ```bash
   ezpl logs search --pattern "error" --level ERROR
   ```

4. **Check statistics before cleaning:**
   ```bash
   ezpl logs stats
   ```

## Environment Variables

When using `--env` with `config set`, Ezpl automatically creates user environment variables with predefined names:

- `EZPL_LOG_LEVEL`
- `EZPL_LOG_FILE`
- `EZPL_LOG_DIR`
- `EZPL_PRINTER_LEVEL`
- `EZPL_FILE_LOGGER_LEVEL`
- `EZPL_LOG_ROTATION`
- `EZPL_LOG_RETENTION`
- `EZPL_LOG_COMPRESSION`
- And more...

These variables are stored in `~/.ezpl/.env` (or `%USERPROFILE%\.ezpl\.env` on Windows).

## Useful Links

### 📖 General Documentation

- **[../api/SUMMARY.md](../api/SUMMARY.md)** – API summary
- **[../api/API_DOCUMENTATION.md](../api/API_DOCUMENTATION.md)** – Complete API documentation

### 🛠️ Configuration

- **[CONFIG_GUIDE.md](CONFIG_GUIDE.md)** – Detailed configuration guide

### 🔗 External Resources

- **Source code**: `../../ezpl/cli/` – CLI implementation
- **Examples**: See API documentation for usage examples

---

**Ezpl CLI Documentation** – Complete guide to leverage the Ezpl CLI in your projects.
