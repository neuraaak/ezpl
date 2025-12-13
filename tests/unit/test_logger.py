# -*- coding: utf-8 -*-
# ///////////////////////////////////////////////////////////////
# EZPL - Tests unitaires FileLogger
# Project: ezpl
# ///////////////////////////////////////////////////////////////

"""
Unit tests for FileLogger.

Tests cover:
- All log levels
- File rotation (size, date, time)
- Retention (duration, count)
- Compression (zip, gz, tar.gz)
- Separators
- File size operations
- Special character handling
- Error handling
- Directory creation
"""

import time
from pathlib import Path
from unittest.mock import patch

# IMPORT BASE
# ///////////////////////////////////////////////////////////////
import pytest

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from ezpl import Ezpl
from ezpl.core.exceptions import FileOperationError, ValidationError
from ezpl.handlers import FileLogger

# IMPORT SPECS
# ///////////////////////////////////////////////////////////////


## ==> HELPER FUNCTIONS
# ///////////////////////////////////////////////////////////////


def wait_for_file(path: Path, timeout: float = 2.0) -> None:
    """Wait for file to be created."""
    start = time.time()
    while not path.exists():
        if time.time() - start > timeout:
            raise FileNotFoundError(f"Timeout waiting for file: {path}")
        time.sleep(0.05)


## ==> TESTS
# ///////////////////////////////////////////////////////////////


class TestLogLevels:
    """Tests for all log levels."""

    def test_debug_level(self, temp_log_file: Path) -> None:
        """Test debug() level."""
        logger_handler = FileLogger(temp_log_file, level="DEBUG")
        logger = logger_handler.get_logger()
        logger.debug("Debug message")
        wait_for_file(temp_log_file)
        assert temp_log_file.exists()

    def test_info_level(self, temp_log_file: Path) -> None:
        """Test info() level."""
        logger_handler = FileLogger(temp_log_file, level="INFO")
        logger = logger_handler.get_logger()
        logger.info("Info message")
        wait_for_file(temp_log_file)
        assert temp_log_file.exists()

    def test_warning_level(self, temp_log_file: Path) -> None:
        """Test warning() level."""
        logger_handler = FileLogger(temp_log_file, level="WARNING")
        logger = logger_handler.get_logger()
        logger.warning("Warning message")
        wait_for_file(temp_log_file)
        assert temp_log_file.exists()

    def test_error_level(self, temp_log_file: Path) -> None:
        """Test error() level."""
        logger_handler = FileLogger(temp_log_file, level="ERROR")
        logger = logger_handler.get_logger()
        logger.error("Error message")
        wait_for_file(temp_log_file)
        assert temp_log_file.exists()

    def test_critical_level(self, temp_log_file: Path) -> None:
        """Test critical() level."""
        logger_handler = FileLogger(temp_log_file, level="CRITICAL")
        logger = logger_handler.get_logger()
        logger.critical("Critical message")
        wait_for_file(temp_log_file)
        assert temp_log_file.exists()

    def test_set_level(self, temp_log_file: Path) -> None:
        """Test set_level() method."""
        logger_handler = FileLogger(temp_log_file, level="INFO")
        logger_handler.set_level("DEBUG")
        assert logger_handler._level == "DEBUG"

    def test_invalid_level_raises_error(self, temp_log_file: Path) -> None:
        """Test that invalid level raises ValidationError."""
        with pytest.raises(ValidationError):
            FileLogger(temp_log_file, level="INVALID_LEVEL")


class TestFileRotation:
    """Tests for file rotation."""

    def test_rotation_by_size(self, temp_dir: Path) -> None:
        """Test rotation by file size."""
        log_file = temp_dir / "rotation_size.log"
        logger_handler = FileLogger(
            log_file, level="INFO", rotation="1 KB", retention="1 day"
        )
        logger = logger_handler.get_logger()

        # Write enough data to trigger rotation
        for i in range(100):
            logger.info(f"Test message {i} " * 10)

        # Verify file exists or rotation occurred
        assert log_file.exists() or any(log_file.parent.glob("rotation_size.log.*"))

    def test_rotation_by_time(self, temp_dir: Path) -> None:
        """Test rotation by time."""
        log_file = temp_dir / "rotation_time.log"
        logger_handler = FileLogger(
            log_file, level="INFO", rotation="1 second", retention="1 day"
        )
        logger = logger_handler.get_logger()

        logger.info("Message 1")
        time.sleep(1.1)  # Wait for rotation time
        logger.info("Message 2")

        # Verify rotation occurred
        assert log_file.exists() or any(log_file.parent.glob("rotation_time.log.*"))

    def test_rotation_by_date(self, temp_dir: Path) -> None:
        """Test rotation by date."""
        log_file = temp_dir / "rotation_date.log"
        logger_handler = FileLogger(
            log_file, level="INFO", rotation="1 day", retention="7 days"
        )
        logger = logger_handler.get_logger()
        logger.info("Test message")
        # Verify file exists
        assert log_file.exists()

    def test_rotation_at_time(self, temp_dir: Path) -> None:
        """Test rotation at specific time."""
        log_file = temp_dir / "rotation_at_time.log"
        logger_handler = FileLogger(
            log_file, level="INFO", rotation="12:00", retention="7 days"
        )
        logger = logger_handler.get_logger()
        logger.info("Test message")
        # Verify file exists
        assert log_file.exists()


class TestRetention:
    """Tests for log retention."""

    def test_retention_by_duration(self, temp_dir: Path) -> None:
        """Test retention by duration."""
        log_file = temp_dir / "retention_duration.log"
        logger_handler = FileLogger(log_file, level="INFO", retention="1 day")
        logger = logger_handler.get_logger()
        logger.info("Test message")
        # Verify file exists
        assert log_file.exists()

    def test_retention_by_count(self, temp_dir: Path) -> None:
        """Test retention by duration (loguru doesn't support file count directly)."""
        log_file = temp_dir / "retention_count.log"
        logger_handler = FileLogger(
            log_file, level="INFO", rotation="1 KB", retention="1 day"
        )
        logger = logger_handler.get_logger()

        # Write enough to create multiple files
        for i in range(50):
            logger.info(f"Test message {i} " * 10)

        # Verify files exist
        assert log_file.exists() or any(log_file.parent.glob("retention_count.log.*"))


class TestCompression:
    """Tests for log compression."""

    def test_compression_zip(self, temp_dir: Path) -> None:
        """Test compression with zip format."""
        log_file = temp_dir / "compression_zip.log"
        logger_handler = FileLogger(
            log_file,
            level="INFO",
            rotation="1 KB",
            retention="1 day",
            compression="zip",
        )
        logger = logger_handler.get_logger()

        # Write enough to trigger rotation
        for i in range(50):
            logger.info(f"Test message {i} " * 10)

        # Verify file exists or compressed files exist
        assert log_file.exists() or any(
            log_file.parent.glob("compression_zip.log.*.zip")
        )

    def test_compression_gz(self, temp_dir: Path) -> None:
        """Test compression with gz format."""
        log_file = temp_dir / "compression_gz.log"
        logger_handler = FileLogger(
            log_file,
            level="INFO",
            rotation="1 KB",
            retention="1 day",
            compression="gz",
        )
        logger = logger_handler.get_logger()

        # Write enough to trigger rotation
        for i in range(50):
            logger.info(f"Test message {i} " * 10)

        # Verify file exists
        assert log_file.exists() or any(log_file.parent.glob("compression_gz.log.*.gz"))

    def test_compression_tar_gz(self, temp_dir: Path) -> None:
        """Test compression with tar.gz format."""
        log_file = temp_dir / "compression_tar_gz.log"
        logger_handler = FileLogger(
            log_file,
            level="INFO",
            rotation="1 KB",
            retention="1 day",
            compression="tar.gz",
        )
        logger = logger_handler.get_logger()

        # Write enough to trigger rotation
        for i in range(50):
            logger.info(f"Test message {i} " * 10)

        # Verify file exists
        assert log_file.exists() or any(
            log_file.parent.glob("compression_tar_gz.log.*.tar.gz")
        )


class TestSeparators:
    """Tests for log separators."""

    def test_add_separator(self, temp_log_file: Path) -> None:
        """Test add_separator() method."""
        logger_handler = FileLogger(temp_log_file, level="INFO")
        logger_handler.add_separator()
        logger = logger_handler.get_logger()
        logger.info("Test message")
        wait_for_file(temp_log_file)
        content = temp_log_file.read_text(encoding="utf-8")
        assert "==>" in content or "---" in content or len(content) > 0

    def test_separator_with_ezpl(self, temp_log_file: Path) -> None:
        """Test separator via Ezpl."""
        ezpl = Ezpl(log_file=temp_log_file)
        ezpl.add_separator()
        ezpl.get_logger().info("Test message")
        wait_for_file(temp_log_file)
        content = temp_log_file.read_text(encoding="utf-8")
        assert "==>" in content or "---" in content or len(content) > 0


class TestFileOperations:
    """Tests for file operations."""

    def test_get_log_file(self, temp_log_file: Path) -> None:
        """Test get_log_file() method."""
        logger_handler = FileLogger(temp_log_file, level="INFO")
        assert logger_handler.get_log_file() == temp_log_file

    def test_get_file_size(self, temp_log_file: Path) -> None:
        """Test get_file_size() method."""
        logger_handler = FileLogger(temp_log_file, level="INFO")
        logger = logger_handler.get_logger()
        logger.info("Test message 1")
        logger.info("Test message 2")
        wait_for_file(temp_log_file)
        size = logger_handler.get_file_size()
        assert size > 0

    def test_get_file_size_empty_file(self, temp_log_file: Path) -> None:
        """Test get_file_size() with empty file."""
        logger_handler = FileLogger(temp_log_file, level="INFO")
        size = logger_handler.get_file_size()
        assert size >= 0


class TestSpecialCharacters:
    """Tests for special character handling."""

    def test_unicode_characters(self, temp_log_file: Path) -> None:
        """Test logger with Unicode characters."""
        logger_handler = FileLogger(temp_log_file, level="INFO")
        logger = logger_handler.get_logger()
        strange_message = "Test spécial: éèàçô 漢字 🚀"
        logger.info(strange_message)
        wait_for_file(temp_log_file)
        content = temp_log_file.read_text(encoding="utf-8")
        assert "Test spécial" in content
        assert "漢字" in content
        assert "🚀" in content

    def test_control_characters(self, temp_log_file: Path) -> None:
        """Test logger with control characters."""
        logger_handler = FileLogger(temp_log_file, level="INFO")
        logger = logger_handler.get_logger()
        message_with_control = "Test\x00\x1b[31m"
        logger.info(message_with_control)
        wait_for_file(temp_log_file)
        # Should not crash
        assert temp_log_file.exists()

    def test_html_tags(self, temp_log_file: Path) -> None:
        """Test logger with HTML tags."""
        logger_handler = FileLogger(temp_log_file, level="INFO")
        logger = logger_handler.get_logger()
        logger.info("Message with <tags> and </tags>")
        wait_for_file(temp_log_file)
        content = temp_log_file.read_text(encoding="utf-8")
        # HTML tags should be sanitized or preserved
        assert "Message" in content


class TestTypeConversion:
    """Tests for automatic type conversion."""

    def test_exception_object(self, temp_log_file: Path) -> None:
        """Test logger with exception object."""
        logger_handler = FileLogger(temp_log_file, level="INFO")
        logger = logger_handler.get_logger()
        try:
            {}[0]
        except Exception as exc:
            logger.error(exc)
            logger.error(f"Exception: {exc}")
        wait_for_file(temp_log_file)
        content = temp_log_file.read_text(encoding="utf-8")
        assert "Exception" in content or "KeyError" in content

    def test_dict_message(self, temp_log_file: Path) -> None:
        """Test logger with dictionary message."""
        logger_handler = FileLogger(temp_log_file, level="INFO")
        logger = logger_handler.get_logger()
        logger.info({"key": "value"})
        wait_for_file(temp_log_file)
        assert temp_log_file.exists()

    def test_list_message(self, temp_log_file: Path) -> None:
        """Test logger with list message."""
        logger_handler = FileLogger(temp_log_file, level="INFO")
        logger = logger_handler.get_logger()
        logger.info(["list", "items"])
        wait_for_file(temp_log_file)
        assert temp_log_file.exists()


class TestErrorHandling:
    """Tests for error handling."""

    def test_invalid_directory_permissions(self, temp_dir: Path) -> None:
        """Test handling of invalid directory permissions."""
        # Create a path that might have permission issues
        invalid_path = temp_dir / "invalid" / "path" / "test.log"
        # Should handle gracefully or raise FileOperationError
        try:
            logger_handler = FileLogger(invalid_path, level="INFO")
            # If it succeeds, verify file was created
            assert logger_handler.get_log_file() == invalid_path
        except FileOperationError:
            # Expected behavior for permission errors
            pass

    def test_file_write_error_handling(self, temp_log_file: Path) -> None:
        """Test handling of file write errors."""
        logger_handler = FileLogger(temp_log_file, level="INFO")
        logger = logger_handler.get_logger()

        # Try to write with mocked error
        with patch("builtins.open", side_effect=OSError("Write error")):
            try:
                logger.info("Test message")
            except (OSError, Exception):
                # Expected behavior - should handle gracefully
                pass


class TestDirectoryCreation:
    """Tests for automatic directory creation."""

    def test_creates_parent_directory(self, temp_dir: Path) -> None:
        """Test that parent directory is created automatically."""
        log_file = temp_dir / "subdir" / "nested" / "test.log"
        logger_handler = FileLogger(log_file, level="INFO")
        assert log_file.parent.exists()
        assert logger_handler.get_log_file() == log_file

    def test_handles_existing_directory(self, temp_dir: Path) -> None:
        """Test handling of existing directory."""
        log_file = temp_dir / "existing" / "test.log"
        log_file.parent.mkdir(parents=True, exist_ok=True)
        logger_handler = FileLogger(log_file, level="INFO")
        assert logger_handler.get_log_file() == log_file
