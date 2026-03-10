# ///////////////////////////////////////////////////////////////
# EZPL - Robustness Tests - Error Handling
# Project: ezpl
# ///////////////////////////////////////////////////////////////

"""
Robustness tests for error handling.

Tests cover:
- Exceptions passed as messages
- Complex objects (dict, list, custom)
- File operation errors
- Network errors (if applicable)
- Timeouts
- Memory errors (if applicable)

Note: This file intentionally uses try-except-pass for robustness testing.
"""

# ruff: noqa: S110, SIM105

from __future__ import annotations

# ///////////////////////////////////////////////////////////////
# IMPORTS
# ///////////////////////////////////////////////////////////////
# Standard library imports
from pathlib import Path
from unittest.mock import patch

# Third-party imports
import pytest

# Local imports
from ezpl import Ezpl
from ezpl.core.exceptions import FileOperationError, ValidationError

pytestmark = pytest.mark.robustness

# ///////////////////////////////////////////////////////////////
# TESTS
# ///////////////////////////////////////////////////////////////


class TestExceptionMessages:
    """Tests for exceptions passed as messages."""

    def test_value_error_as_message_printer(self) -> None:
        """Test printer with ValueError exception."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        try:
            raise ValueError("Test error")
        except Exception as exc:
            printer.error(exc)
            # Should not crash

    def test_value_error_as_message_logger(self, temp_log_file: Path) -> None:
        """Test logger with ValueError exception."""
        ezpl = Ezpl(log_file=temp_log_file)
        logger = ezpl.get_logger()
        try:
            raise ValueError("Test error")
        except Exception as exc:
            logger.error(exc)
            # Should not crash

    def test_key_error_as_message(self) -> None:
        """Test with KeyError exception."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        try:
            {}["missing"]
        except Exception as exc:
            printer.error(exc)
            # Should not crash

    def test_nested_exception(self) -> None:
        """Test with nested exception."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        try:
            try:
                raise ValueError("Inner error")
            except ValueError:
                raise RuntimeError("Outer error") from None
        except Exception as exc:
            printer.error(exc)
            # Should not crash


class TestComplexObjects:
    """Tests for complex objects as messages."""

    def test_nested_dict_printer(self) -> None:
        """Test printer with nested dictionary."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        nested = {"level1": {"level2": {"level3": "value"}}}
        printer.info(nested)
        # Should not crash

    def test_nested_dict_logger(self, temp_log_file: Path) -> None:
        """Test logger with nested dictionary."""
        ezpl = Ezpl(log_file=temp_log_file)
        logger = ezpl.get_logger()
        nested = {"level1": {"level2": {"level3": "value"}}}
        logger.info(nested)
        # Should not crash

    def test_list_of_objects_printer(self) -> None:
        """Test printer with list of objects."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        complex_list = [
            {"key": "value"},
            [1, 2, 3],
            "string",
            123,
            None,
        ]
        printer.info(complex_list)
        # Should not crash

    def test_custom_object_printer(self) -> None:
        """Test printer with custom object."""

        class CustomObject:
            def __init__(self):
                self.data = "test"

            def __str__(self):
                return f"CustomObject(data={self.data})"

        ezpl = Ezpl()
        printer = ezpl.get_printer()
        custom = CustomObject()
        printer.info(custom)
        # Should not crash

    def test_object_without_str(self) -> None:
        """Test with object without __str__ method."""

        class NoStrObject:
            def __repr__(self):
                return "NoStrObject()"

        ezpl = Ezpl()
        printer = ezpl.get_printer()
        obj = NoStrObject()
        printer.info(obj)
        # Should not crash


class TestFileOperationErrors:
    """Tests for file operation error handling."""

    def test_permission_error_handling(self, temp_dir: Path) -> None:
        """Test handling of permission errors."""
        # Create a path that might have permission issues
        invalid_path = temp_dir / "invalid" / "path" / "test.log"

        # Should handle gracefully or raise FileOperationError
        try:
            ezpl = Ezpl(log_file=invalid_path)
            # If it succeeds, verify file was created
            assert ezpl._log_file == invalid_path
        except (FileOperationError, OSError, PermissionError):
            # Expected behavior for permission errors
            pass

    def test_disk_full_simulation(self, temp_log_file: Path) -> None:
        """Test handling of disk full scenario (simulated)."""
        ezpl = Ezpl(log_file=temp_log_file)
        logger = ezpl.get_logger()

        # Simulate disk full error
        with patch("builtins.open", side_effect=OSError("No space left on device")):
            try:
                logger.info("Test message")
            except OSError:
                pass

    def test_read_only_file_system(self, temp_log_file: Path) -> None:
        """Test handling of read-only file system (simulated)."""
        ezpl = Ezpl(log_file=temp_log_file)
        logger = ezpl.get_logger()

        # Simulate read-only error
        with patch(
            "builtins.open", side_effect=PermissionError("Read-only file system")
        ):
            try:
                logger.info("Test message")
            except PermissionError:
                pass


class TestInvalidInputs:
    """Tests for invalid input handling."""

    def test_invalid_log_level_handling(self) -> None:
        """Invalid log level string should raise ValidationError."""
        ezpl = Ezpl()
        with pytest.raises(ValidationError):
            ezpl.set_level("INVALID_LEVEL")

    def test_invalid_file_path_handling(self) -> None:
        """Invalid path characters should raise FileOperationError or OSError."""
        invalid_path = Path('<>:"|?*')  # Invalid Windows characters
        with pytest.raises((OSError, FileOperationError)):
            _ = Ezpl(log_file=invalid_path)

    def test_invalid_config_value_handling(self) -> None:
        """ConfigurationManager.set() accepts any value — should not raise."""
        ezpl = Ezpl()
        config = ezpl.get_config()
        config.set("log-level", 12345)  # Stores value as-is, no validation here


class TestConcurrentOperations:
    """Tests for concurrent operation handling."""

    def test_rapid_logging(self, temp_log_file: Path) -> None:
        """Test rapid logging operations."""
        ezpl = Ezpl(log_file=temp_log_file)
        logger = ezpl.get_logger()
        printer = ezpl.get_printer()

        # Rapid logging
        for i in range(100):
            logger.info(f"Message {i}")
            printer.info(f"Message {i}")

        # Should not crash
        assert temp_log_file.exists()

    def test_concurrent_file_access(self, temp_log_file: Path) -> None:
        """Test concurrent file access (simulated)."""
        ezpl = Ezpl(log_file=temp_log_file)
        logger = ezpl.get_logger()

        # Simulate concurrent writes
        for i in range(50):
            logger.info(f"Concurrent message {i}")

        # Should not crash
        assert temp_log_file.exists()
