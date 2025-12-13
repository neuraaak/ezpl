# Configuration Guide – Ezpl CLI

## Overview

This guide provides instructions for configuring and using the **Ezpl CLI** with environment variables and configuration files.

## Configuration Sources

Ezpl CLI uses a priority order for configuration:

1. **Environment variables** (highest priority)
2. **Configuration file** (`~/.ezpl/config.json`)
3. **Default values** (lowest priority)

## Configuration File

### Location

- **Windows**: `%USERPROFILE%\.ezpl\config.json`
- **Linux/macOS**: `~/.ezpl/config.json`

### Format

The configuration file is a JSON file with the following structure:

```json
{
  "log-level": "INFO",
  "log-file": "ezpl.log",
  "log-dir": "/path/to/logs",
  "printer-level": "INFO",
  "file-logger-level": "INFO",
  "indent-step": 3,
  "indent-symbol": ">",
  "base-indent-symbol": "~",
  "log-format": "{time:YYYY-MM-DD HH:mm:ss} | {level:<10} | {module}:{function}:{line} - {message}",
  "log-rotation": null,
  "log-retention": null,
  "log-compression": null
}
```

### Managing Configuration

Use the CLI commands to manage configuration:

```bash
# View all configuration
ezpl config get

# View specific key
ezpl config get log-level

# Set configuration
ezpl config set log-level DEBUG

# Reset to defaults
ezpl config reset --confirm
```

## Environment Variables

### User Environment Variables

Ezpl can create user environment variables that persist across sessions. These are stored in:

- **Windows**: `%USERPROFILE%\.ezpl\.env`
- **Linux/macOS**: `~/.ezpl/.env`

### Setting Environment Variables

Use the `--env` flag when setting configuration:

```bash
# Set configuration and create environment variable
ezpl config set log-level DEBUG --env
```

This creates `EZPL_LOG_LEVEL=DEBUG` in the user environment file.

### Available Environment Variables

All environment variables are prefixed with `EZPL_`:

- `EZPL_LOG_LEVEL`: Global log level
- `EZPL_LOG_FILE`: Log file name
- `EZPL_LOG_DIR`: Log directory path
- `EZPL_PRINTER_LEVEL`: Printer log level
- `EZPL_FILE_LOGGER_LEVEL`: File logger level
- `EZPL_INDENT_STEP`: Indentation step size
- `EZPL_INDENT_SYMBOL`: Symbol for indentation
- `EZPL_BASE_INDENT_SYMBOL`: Base indentation symbol
- `EZPL_LOG_FORMAT`: Log format string
- `EZPL_LOG_ROTATION`: Rotation setting (e.g., "10 MB", "1 day")
- `EZPL_LOG_RETENTION`: Retention period (e.g., "7 days")
- `EZPL_LOG_COMPRESSION`: Compression format (e.g., "zip", "gz")

### Viewing Environment Variables

```bash
# Show configuration with environment variable names
ezpl config get --show-env
```

### Removing Environment Variables

```bash
# Reset configuration (removes all user environment variables)
ezpl config reset --confirm
```

## Configuration Examples

### Basic Setup

```bash
# Set log level
ezpl config set log-level INFO

# Set log directory
ezpl config set log-dir ~/logs

# View configuration
ezpl config get
```

### Advanced Setup with Environment Variables

```bash
# Set multiple configurations with environment variables
ezpl config set log-level DEBUG --env
ezpl config set printer-level INFO --env
ezpl config set log-rotation "10 MB" --env
ezpl config set log-retention "7 days" --env

# Verify
ezpl config get --show-env
```

### Project-Specific Configuration

For different projects, you can:

1. **Use different configuration files:**

   ```bash
   # Set environment variable before running
   export EZPL_LOG_DIR=/path/to/project1/logs
   ezpl logs view
   ```

2. **Reset configuration between projects:**

   ```bash
   # Project 1
   ezpl config set log-dir ~/project1/logs

   # Switch to Project 2
   ezpl config reset --confirm
   ezpl config set log-dir ~/project2/logs
   ```

## Log File Configuration

### Default Log Location

By default, logs are stored in:

- **Windows**: `%APPDATA%\ezpl\logs\ezpl.log`
- **Linux**: `~/.local/share/ezpl/logs/ezpl.log`
- **macOS**: `~/Library/Application Support/ezpl/logs/ezpl.log`

### Custom Log Location

```bash
# Set custom log directory
ezpl config set log-dir /path/to/custom/logs

# Set custom log file name
ezpl config set log-file myapp.log
```

### Log Rotation

Configure automatic log rotation:

```bash
# Rotate by size
ezpl config set log-rotation "10 MB"

# Rotate by time
ezpl config set log-rotation "1 day"

# Rotate at specific time
ezpl config set log-rotation "12:00"

# Disable rotation
ezpl config set log-rotation null
```

### Log Retention

Configure log retention:

```bash
# Keep logs for 7 days
ezpl config set log-retention "7 days"

# Keep last 10 files
ezpl config set log-retention "10 files"

# Disable retention
ezpl config set log-retention null
```

### Log Compression

Configure log compression:

```bash
# Compress with gzip
ezpl config set log-compression "gz"

# Compress with zip
ezpl config set log-compression "zip"

# Disable compression
ezpl config set log-compression null
```

## Troubleshooting

### Configuration Not Applied

1. **Check configuration file:**

   ```bash
   ezpl config get
   ```

2. **Check environment variables:**

   ```bash
   ezpl config get --show-env
   ```

3. **Verify file permissions:**
   - Ensure you have write access to `~/.ezpl/`
   - Check that the configuration file is not corrupted

### Environment Variables Not Working

1. **Verify environment variables are set:**

   ```bash
   # On Linux/macOS
   cat ~/.ezpl/.env

   # On Windows
   type %USERPROFILE%\.ezpl\.env
   ```

2. **Reload environment:**
   - Restart your terminal/shell
   - Or source the `.env` file manually

### Reset Everything

If you encounter issues, reset to defaults:

```bash
ezpl config reset --confirm
```

This will:

- Reset all configuration to defaults
- Remove all user environment variables
- Keep the configuration file structure

## Best Practices

1. **Use environment variables for sensitive settings:**

   ```bash
   ezpl config set log-level DEBUG --env
   ```

2. **Document your configuration:**

   - Keep a record of custom settings
   - Use version control for project-specific configs

3. **Regular cleanup:**

   ```bash
   # Check log statistics
   ezpl logs stats

   # Clean old logs
   ezpl logs clean --days 30 --confirm
   ```

4. **Project isolation:**
   - Use different log directories for different projects
   - Reset configuration when switching projects

---

**Ezpl Configuration Guide** – Your reference for configuring the Ezpl CLI.
