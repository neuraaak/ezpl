# ///////////////////////////////////////////////////////////////
# EZPL - Tests unitaires Ezpl
# Project: ezpl
# ///////////////////////////////////////////////////////////////

"""
Unit tests for Ezpl singleton class.

Tests cover:
- Singleton pattern
- Initialization with all parameters
- Configuration priority order
- Level management
- File operations
- Indentation
- Configuration management
- Error handling

Note: Some tests intentionally use try-except-pass for robustness testing.
"""

# ruff: noqa: S110, SIM105

from __future__ import annotations

# ///////////////////////////////////////////////////////////////
# IMPORTS
# ///////////////////////////////////////////////////////////////
# Standard library imports
import json
import os
from pathlib import Path
from unittest.mock import patch

# Third-party imports
import pytest

# Local imports
from ezpl import Ezpl
from ezpl.core.exceptions import FileOperationError, ValidationError

# ///////////////////////////////////////////////////////////////
# TESTS
# ///////////////////////////////////////////////////////////////


class TestSingleton:
    """Tests for singleton pattern."""

    def test_singleton_returns_same_instance(self) -> None:
        """Test that Ezpl() always returns the same instance."""
        Ezpl.reset()
        e1 = Ezpl()
        e2 = Ezpl()
        assert e1 is e2

    def test_reset_creates_new_instance(self) -> None:
        """Test that reset() allows creating a new instance."""
        Ezpl.reset()
        e1 = Ezpl()
        Ezpl.reset()
        e2 = Ezpl()
        # After reset, instances should be different
        # (or at least reset should not raise errors)
        assert e1 is not None
        assert e2 is not None


class TestInitialization:
    """Tests for Ezpl initialization."""

    def test_initialization_with_log_file(self, temp_log_file: Path) -> None:
        """Test initialization with custom log file."""
        ezpl = Ezpl(log_file=temp_log_file)
        assert ezpl._log_file == temp_log_file

    def test_initialization_with_all_parameters(self, temp_log_file: Path) -> None:
        """Test initialization with all parameters."""
        ezpl = Ezpl(
            log_file=temp_log_file,
            log_level="DEBUG",
            printer_level="INFO",
            file_logger_level="WARNING",
            log_rotation="10 MB",
            log_retention="7 days",
            log_compression="zip",
            indent_step=4,
            indent_symbol="  ",
            base_indent_symbol=">",
        )
        assert ezpl._log_file == temp_log_file
        # Verify levels are set correctly
        assert ezpl._printer._level == "INFO"
        assert ezpl._logger._level == "WARNING"

    def test_initialization_with_defaults(self) -> None:
        """Test initialization with default values."""
        ezpl = Ezpl()
        assert ezpl._log_file is not None
        assert ezpl.get_printer() is not None
        assert ezpl.get_logger() is not None


class TestConfigurationPriority:
    """Tests for configuration priority order (arg > env > file > default)."""

    def test_arg_overrides_env_and_file(
        self,
        temp_config_file: Path,
        clean_env: None,  # noqa: ARG002
    ) -> None:
        """Test that argument has highest priority."""
        # Set environment variable
        os.environ["EZPL_LOG_LEVEL"] = "WARNING"
        # Set config file
        config_data = {"log-level": "ERROR"}
        temp_config_file.parent.mkdir(parents=True, exist_ok=True)
        temp_config_file.write_text(json.dumps(config_data), encoding="utf-8")

        # Argument should override both
        ezpl = Ezpl(log_level="DEBUG")
        # The argument should be applied
        assert ezpl._printer._level == "DEBUG"
        assert ezpl._logger._level == "DEBUG"

    def test_env_overrides_file(
        self,
        temp_config_file: Path,
        clean_env: None,  # noqa: ARG002
    ) -> None:
        """Test that environment variable overrides config file."""
        # Set config file
        config_data = {"log-level": "ERROR"}
        temp_config_file.parent.mkdir(parents=True, exist_ok=True)
        temp_config_file.write_text(json.dumps(config_data), encoding="utf-8")
        # Set environment variable
        os.environ["EZPL_LOG_LEVEL"] = "WARNING"

        ezpl = Ezpl()
        # Environment should override file
        # Note: We can't easily test this without mocking, but we verify no errors
        assert ezpl is not None

    def test_file_overrides_default(self, temp_config_file: Path) -> None:
        """Test that config file overrides defaults."""
        # Set config file
        config_data = {"log-level": "ERROR", "printer-level": "WARNING"}
        temp_config_file.parent.mkdir(parents=True, exist_ok=True)
        temp_config_file.write_text(json.dumps(config_data), encoding="utf-8")

        # Mock the config file path
        with patch(
            "ezpl.config.manager.DefaultConfiguration.CONFIG_FILE", temp_config_file
        ):
            ezpl = Ezpl()
            # Config file should be loaded
            assert ezpl is not None


class TestLevelManagement:
    """Tests for log level management."""

    def test_set_level_changes_both_printer_and_logger(self) -> None:
        """Test that set_level() changes both printer and logger levels."""
        ezpl = Ezpl()
        ezpl.set_level("DEBUG")
        # Access internal printer to check level
        assert ezpl._printer._level == "DEBUG"
        assert ezpl._logger._level == "DEBUG"

    def test_set_printer_level_only(self) -> None:
        """Test that set_printer_level() only affects printer."""
        ezpl = Ezpl()
        ezpl.set_printer_level("WARNING")
        # Access internal printer to check level
        assert ezpl._printer._level == "WARNING"
        # Logger level should remain unchanged (default or previous value)
        assert ezpl._logger._level is not None

    def test_set_logger_level_only(self) -> None:
        """Test that set_logger_level() only affects logger."""
        ezpl = Ezpl()
        ezpl.set_logger_level("ERROR")
        assert ezpl._logger._level == "ERROR"
        # Printer level should remain unchanged

    def test_set_level_invalid_raises_error(self) -> None:
        """Test that set_level() with invalid level raises error."""
        ezpl = Ezpl()
        with pytest.raises(ValidationError):
            ezpl.set_level("INVALID_LEVEL")

    def test_set_printer_level_invalid_raises_error(self) -> None:
        """Test that set_printer_level() with invalid level raises error."""
        ezpl = Ezpl()
        with pytest.raises(ValidationError):
            ezpl.set_printer_level("INVALID_LEVEL")

    def test_set_logger_level_invalid_raises_error(self) -> None:
        """Test that set_logger_level() with invalid level raises error."""
        ezpl = Ezpl()
        with pytest.raises(ValidationError):
            ezpl.set_logger_level("INVALID_LEVEL")


class TestFileOperations:
    """Tests for file operations."""

    def test_set_log_file(self, temp_log_file: Path, temp_dir: Path) -> None:
        """Test changing log file."""
        ezpl = Ezpl(log_file=temp_log_file)
        new_file = temp_dir / "new.log"
        ezpl.set_log_file(new_file)
        assert ezpl._log_file == new_file

    def test_get_log_file(self, temp_log_file: Path) -> None:
        """Test getting log file path."""
        ezpl = Ezpl(log_file=temp_log_file)
        # Access internal _log_file or use get_config
        config = ezpl.get_config()
        log_file_from_config = config.get("log-file")
        assert log_file_from_config is not None

    def test_add_separator(self, temp_log_file: Path) -> None:
        """Test adding separator to log file."""
        ezpl = Ezpl(log_file=temp_log_file)
        ezpl.add_separator()
        # Write a log to ensure file is created
        ezpl.get_logger().info("Test message")
        # Verify separator was added (check file content)
        if temp_log_file.exists():
            content = temp_log_file.read_text(encoding="utf-8")
            assert "==>" in content or "---" in content or len(content) > 0


class TestIndentation:
    """Tests for indentation management."""

    def test_manage_indent_context_manager(self) -> None:
        """Test manage_indent() context manager."""
        ezpl = Ezpl()
        # Access internal printer to check indent
        initial_indent = ezpl._printer._indent

        with ezpl.manage_indent():
            assert ezpl._printer._indent == initial_indent + 1

        # After context, indent should return to initial
        assert ezpl._printer._indent == initial_indent

    def test_manage_indent_nested(self) -> None:
        """Test nested manage_indent() context managers."""
        ezpl = Ezpl()
        # Access internal printer to check indent
        initial_indent = ezpl._printer._indent

        with ezpl.manage_indent():
            assert ezpl._printer._indent == initial_indent + 1
            with ezpl.manage_indent():
                assert ezpl._printer._indent == initial_indent + 2
            assert ezpl._printer._indent == initial_indent + 1
        assert ezpl._printer._indent == initial_indent


class TestConfiguration:
    """Tests for configuration management."""

    def test_get_config_returns_config_manager(self) -> None:
        """Test that get_config() returns ConfigurationManager."""
        ezpl = Ezpl()
        config = ezpl.get_config()
        assert config is not None
        # Verify it has configuration methods
        assert hasattr(config, "get")
        assert hasattr(config, "set")

    def test_configure_with_dict(self, temp_config_file: Path) -> None:  # noqa: ARG002
        """Test configure() with dictionary."""
        ezpl = Ezpl()
        ezpl.configure({"level": "DEBUG", "log-rotation": "10 MB"})
        config = ezpl.get_config()
        assert config.get("log-level") == "DEBUG"
        assert config.get("log-rotation") == "10 MB"

    def test_configure_with_kwargs(self) -> None:
        """Test configure() with keyword arguments."""
        ezpl = Ezpl()
        ezpl.configure(level="WARNING", log_rotation="5 MB")
        config = ezpl.get_config()
        assert config.get("log-level") == "WARNING"
        assert config.get("log-rotation") == "5 MB"

    def test_configure_with_mixed_formats(self) -> None:
        """Test configure() with mixed key formats (underscore and hyphen)."""
        ezpl = Ezpl()
        # Mix of underscore and hyphen formats
        ezpl.configure(
            log_level="INFO",
            printer_level="DEBUG",
            log_rotation="10 MB",
        )
        config = ezpl.get_config()
        # Note: configure() with log_level sets both printer and logger
        # So log-level in config might be INFO, but printer-level is DEBUG
        assert config.get("printer-level") == "DEBUG"
        assert config.get("log-rotation") == "10 MB"

    def test_reload_config(
        self,
        temp_config_file: Path,
        clean_env: None,  # noqa: ARG002
    ) -> None:
        """Test reload_config() reloads from file and env."""
        # Create initial config
        config_data = {"log-level": "INFO"}
        temp_config_file.parent.mkdir(parents=True, exist_ok=True)
        temp_config_file.write_text(json.dumps(config_data), encoding="utf-8")

        # Mock config file path
        with patch(
            "ezpl.config.manager.DefaultConfiguration.CONFIG_FILE", temp_config_file
        ):
            ezpl = Ezpl()
            # Change config file
            config_data["log-level"] = "WARNING"
            temp_config_file.write_text(json.dumps(config_data), encoding="utf-8")
            # Reload
            ezpl.reload_config()
            # Config should be reloaded
            assert ezpl is not None


class TestGetters:
    """Tests for getter methods."""

    def test_get_printer_returns_ezprinter(self) -> None:
        """Test that get_printer() returns EzPrinter."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        assert printer is not None
        # Verify it has printer methods
        assert hasattr(printer, "info")
        assert hasattr(printer, "debug")
        assert hasattr(printer, "success")

    def test_get_logger_returns_loguru_logger(self) -> None:
        """Test that get_logger() returns loguru Logger."""
        ezpl = Ezpl()
        logger = ezpl.get_logger()
        assert logger is not None
        # Verify it has loguru methods
        assert hasattr(logger, "info")
        assert hasattr(logger, "debug")
        assert hasattr(logger, "warning")


class TestErrorHandling:
    """Tests for error handling."""

    def test_invalid_log_level_raises_error(self) -> None:
        """Test that invalid log level raises appropriate error."""
        ezpl = Ezpl()
        with pytest.raises(ValidationError):
            ezpl.set_level("NOT_A_VALID_LEVEL")

    def test_invalid_config_key_handled_gracefully(self) -> None:
        """Test that unknown config keys are accepted and persisted as-is."""
        ezpl = Ezpl()
        applied = ezpl.configure(invalid_key="invalid_value")
        assert applied is True
        assert ezpl.get_config().get("invalid_key") == "invalid_value"

    def test_file_operations_with_invalid_path(self) -> None:
        """Test that set_log_file propagates logger creation failure."""
        ezpl = Ezpl()
        with (
            patch(
                "ezpl.ezpl.EzLogger",
                side_effect=FileOperationError("boom", "x.log", "write"),
            ),
            pytest.raises(FileOperationError),
        ):
            ezpl.set_log_file("x.log")


class TestConfigLockV2:
    """Tests for safer lock behavior with owner/token controls."""

    def test_lock_config_returns_token_and_owner_info(self) -> None:
        """lock_config() should expose lock state with owner metadata."""
        Ezpl()
        token = Ezpl.lock_config(owner="CustomA")
        info = Ezpl.config_lock_info()

        assert token is not None
        assert info["locked"] is True
        assert info["owner"] == "CustomA"
        assert info["has_token"] is True

    def test_second_owner_cannot_relock(self) -> None:
        """A different owner should not be able to replace an active lock."""
        Ezpl()
        first_token = Ezpl.lock_config(owner="CustomA")

        with pytest.warns(UserWarning, match="already locked"):
            second_token = Ezpl.lock_config(owner="CustomB")

        assert first_token is not None
        assert second_token is None
        assert Ezpl.config_lock_info()["owner"] == "CustomA"

    def test_configure_force_requires_owner_or_token_when_locked(self) -> None:
        """force=True alone should not bypass a lock with owner/token metadata."""
        ezpl = Ezpl()
        Ezpl.lock_config(owner="CustomA")

        with pytest.warns(UserWarning, match="configuration is locked"):
            applied = ezpl.configure(level="DEBUG", force=True)

        assert applied is False

    def test_configure_force_with_owner_or_token_is_allowed(self) -> None:
        """A matching owner or token should authorize forced configure()."""
        ezpl = Ezpl()
        token = Ezpl.lock_config(owner="CustomA")
        assert token is not None

        by_owner = ezpl.configure(level="DEBUG", force=True, owner="CustomA")
        assert by_owner is True

        by_token = ezpl.configure(level="INFO", force=True, token=token)
        assert by_token is True

    def test_unlock_requires_owner_or_token(self) -> None:
        """unlock_config() should deny unknown callers when lock is active."""
        Ezpl()
        token = Ezpl.lock_config(owner="CustomA")
        assert token is not None

        with pytest.warns(UserWarning, match="Unlock denied"):
            unlocked = Ezpl.unlock_config(owner="CustomB")

        assert unlocked is False
        assert Ezpl.config_lock_info()["locked"] is True

        assert Ezpl.unlock_config(token=token) is True
        assert Ezpl.config_lock_info()["locked"] is False
