# ///////////////////////////////////////////////////////////////
# EZPL - Robustness Tests - Edge Cases
# Project: ezpl
# ///////////////////////////////////////////////////////////////

"""
Robustness tests for edge cases.

Tests cover:
- Singleton with threads (if applicable)
- Very large log files
- Rotation with compression
- Invalid configuration
- Invalid file paths
- Invalid log levels
- Excessive indentation

Note: This file intentionally uses try-except-pass for robustness testing.
"""

# ruff: noqa: S110, SIM105

from __future__ import annotations

# ///////////////////////////////////////////////////////////////
# IMPORTS
# ///////////////////////////////////////////////////////////////
# Standard library imports
import threading
from pathlib import Path

# Third-party imports
import pytest

# Local imports
from ezpl import Ezpl
from ezpl.core.exceptions import FileOperationError, LoggingError, ValidationError

pytestmark = pytest.mark.robustness

# ///////////////////////////////////////////////////////////////
# TESTS
# ///////////////////////////////////////////////////////////////


class TestSingletonEdgeCases:
    """Tests for singleton edge cases."""

    def test_singleton_thread_safety(self) -> None:
        """Test singleton behavior with multiple threads."""
        instances = []

        def get_instance():
            instances.append(Ezpl())

        threads = [threading.Thread(target=get_instance) for _ in range(5)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

        # All instances should be the same
        assert len({id(inst) for inst in instances}) == 1

    def test_reset_during_use(self) -> None:
        """Test reset() while instance is in use."""
        ezpl1 = Ezpl()
        printer1 = ezpl1.get_printer()

        # Reset while using
        Ezpl.reset()

        # Create new instance
        ezpl2 = Ezpl()
        printer2 = ezpl2.get_printer()

        # Should not crash
        assert printer1 is not None
        assert printer2 is not None


class TestLargeFiles:
    """Tests for very large log files."""

    def test_large_log_file_creation(self, temp_dir: Path) -> None:
        """Test creating a large log file."""
        log_file = temp_dir / "large.log"
        ezpl = Ezpl(log_file=log_file)
        logger = ezpl.get_logger()

        # Write many messages
        for i in range(1000):
            logger.info(f"Message {i} " * 10)

        # Should not crash
        assert log_file.exists()

    def test_rotation_with_large_file(self, temp_dir: Path) -> None:
        """Test rotation with large file."""
        log_file = temp_dir / "large_rotation.log"
        ezpl = Ezpl(
            log_file=log_file,
            log_rotation="1 KB",
            log_retention="1 day",
        )
        logger = ezpl.get_logger()

        # Write enough to trigger multiple rotations
        for i in range(200):
            logger.info(f"Message {i} " * 10)

        # Should not crash
        assert log_file.exists() or any(log_file.parent.glob("large_rotation.log.*"))


class TestInvalidConfiguration:
    """Tests for invalid configuration handling."""

    def test_invalid_rotation_format(self, temp_log_file: Path) -> None:
        """Loguru validates rotation at init — should raise LoggingError."""
        with pytest.raises(LoggingError):
            Ezpl(log_file=temp_log_file, log_rotation="INVALID_FORMAT")

    def test_invalid_retention_format(self, temp_log_file: Path) -> None:
        """Loguru validates retention at init — should raise LoggingError."""
        with pytest.raises(LoggingError):
            Ezpl(log_file=temp_log_file, log_retention="INVALID_FORMAT")

    def test_invalid_compression_format(self, temp_log_file: Path) -> None:
        """Loguru validates compression at init — should raise LoggingError."""
        with pytest.raises(LoggingError):
            Ezpl(log_file=temp_log_file, log_compression="INVALID_FORMAT")

    def test_negative_indent_step(self) -> None:
        """EzPrinter does not validate indent_step — Ezpl init should succeed."""
        ezpl = Ezpl(indent_step=-1)
        assert ezpl is not None


class TestInvalidPaths:
    """Tests for invalid file path handling."""

    def test_path_with_invalid_characters(self) -> None:
        """Invalid path characters should raise FileOperationError or OSError."""
        invalid_path = Path('test<>:"|?*.log')
        with pytest.raises((OSError, FileOperationError)):
            _ = Ezpl(log_file=invalid_path)

    def test_path_too_long(self) -> None:
        """Excessively long paths should raise FileOperationError or OSError."""
        long_path = Path("A" * 300) / "test.log"
        with pytest.raises((OSError, FileOperationError)):
            _ = Ezpl(log_file=long_path)

    def test_nonexistent_parent_directory(self, temp_dir: Path) -> None:
        """Test handling of nonexistent parent directory."""
        # Should create directory automatically
        log_file = temp_dir / "nonexistent" / "subdir" / "test.log"
        ezpl = Ezpl(log_file=log_file)
        logger = ezpl.get_logger()
        logger.info("Test")
        # Directory should have been created automatically
        assert log_file.parent.exists()


class TestInvalidLogLevels:
    """Tests for invalid log level handling."""

    def test_empty_log_level(self) -> None:
        """Empty string is not a valid log level — should raise ValidationError."""
        ezpl = Ezpl()
        with pytest.raises(ValidationError):
            ezpl.set_level("")

    def test_none_log_level(self) -> None:
        """None is not a valid log level — should raise AttributeError or ValidationError."""
        ezpl = Ezpl()
        with pytest.raises((AttributeError, ValidationError)):
            ezpl.set_level(None)  # type: ignore[arg-type]

    def test_numeric_log_level(self) -> None:
        """Integer is not a valid log level — should raise AttributeError or ValidationError."""
        ezpl = Ezpl()
        with pytest.raises((AttributeError, ValidationError)):
            ezpl.set_level(42)  # type: ignore[arg-type]


class TestExcessiveIndentation:
    """Tests for excessive indentation handling."""

    def test_excessive_indent_adds(self) -> None:
        """Test that excessive indent adds are limited."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()

        # Try to add way more than MAX_INDENT
        for _ in range(100):
            printer.add_indent()

        # Should be limited to MAX_INDENT (10)
        assert printer._indent <= 10

    def test_excessive_nested_indent(self) -> None:
        """Test excessive nested indentation."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()

        # Try deeply nested context managers
        for _ in range(20):
            with ezpl.manage_indent():
                pass

        # Should be limited
        assert printer._indent <= 10


class TestRotationEdgeCases:
    """Tests for rotation edge cases."""

    def test_rotation_with_compression(self, temp_dir: Path) -> None:
        """Test rotation with compression enabled."""
        log_file = temp_dir / "rotation_compressed.log"
        ezpl = Ezpl(
            log_file=log_file,
            log_rotation="1 KB",
            log_retention="1 day",
            log_compression="zip",
        )
        logger = ezpl.get_logger()

        # Write enough to trigger rotation
        for i in range(100):
            logger.info(f"Message {i} " * 10)

        # Should not crash
        assert log_file.exists() or any(
            log_file.parent.glob("rotation_compressed.log.*.zip")
        )

    def test_rotation_at_exact_size(self, temp_dir: Path) -> None:
        """Test rotation at exact size threshold."""
        log_file = temp_dir / "exact_size.log"
        ezpl = Ezpl(
            log_file=log_file,
            log_rotation="1 KB",
            log_retention="1 day",
        )
        logger = ezpl.get_logger()

        # Write exactly 1 KB
        message = "A" * 1024
        logger.info(message)

        # Should not crash
        assert log_file.exists()
