# How to configure compatibility hooks

Configure ezplog so application logs and library logs follow one consistent policy.

## 🔧 Prerequisites

- ezplog installed
- A single application entrypoint where `Ezpl` is initialized

## 📝 Steps

1. Initialize `Ezpl` once with explicit hook settings.

    ```python
    from ezplog import Ezpl

    ezpl = Ezpl(
        log_file="app.log",
        log_level="INFO",
        hook_logger=True,
        hook_printer=True,
    )
    ```

    ??? note "Why explicit hooks"
        Keeping compatibility settings explicit at startup makes runtime behavior predictable
        and easier to test.

2. Narrow stdlib interception when you only want selected namespaces.

    ```python
    ezpl.set_compatibility_hooks(
        hook_logger=True,
        hook_printer=True,
        logger_names=["vendor.payment", "vendor.auth"],
    )
    ```

3. Lock runtime configuration after bootstrap.

    ```python
    from ezplog import Ezpl

    token = Ezpl.lock_config()

    # Later, if required
    Ezpl.unlock_config(token)
    ```

4. Persist intentional runtime updates.

    ```python
    ezpl.configure(
        file_logger_level="DEBUG",
        log_rotation="10 MB",
        log_retention="14 days",
        persist=True,
    )
    ```

## ⚙️ Variations

Use environment variables for deployment-only overrides.

=== "Bash / Zsh"

    ```bash
    export EZPL_LOG_LEVEL=INFO
    export EZPL_FILE_LOGGER_LEVEL=DEBUG
    export EZPL_LOG_ROTATION="10 MB"
    ```

=== "PowerShell"

    ```powershell
    $env:EZPL_LOG_LEVEL = "INFO"
    $env:EZPL_FILE_LOGGER_LEVEL = "DEBUG"
    $env:EZPL_LOG_ROTATION = "10 MB"
    ```

Use a local configuration file for stable defaults.

```json
{
  "log-level": "INFO",
  "file-logger-level": "DEBUG",
  "log-rotation": "10 MB",
  "log-retention": "14 days"
}
```

## ✅ Result

The application owns logging policy, while libraries stay passive and compatible.
Hook behavior is explicit, testable, and can be scoped to specific logger names.
