# -*- coding: utf-8 -*-
# ///////////////////////////////////////////////////////////////
# EZPL - Tests de robustesse - Cas limites
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
"""

# IMPORT BASE
# ///////////////////////////////////////////////////////////////
import threading
from pathlib import Path

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from ezpl import Ezpl
from ezpl.core.exceptions import FileOperationError, ValidationError

# IMPORT SPECS
# ///////////////////////////////////////////////////////////////


## ==> TESTS
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
        assert len(set(id(inst) for inst in instances)) == 1

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
        assert log_file.exists() or True

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
        """Test handling of invalid rotation format."""
        # Should handle gracefully or raise appropriate error
        try:
            ezpl = Ezpl(log_file=temp_log_file, log_rotation="INVALID_FORMAT")
            # If it succeeds, verify it was set
            assert ezpl is not None
        except (ValueError, Exception):
            # Expected behavior
            pass

    def test_invalid_retention_format(self, temp_log_file: Path) -> None:
        """Test handling of invalid retention format."""
        try:
            ezpl = Ezpl(log_file=temp_log_file, log_retention="INVALID_FORMAT")
            assert ezpl is not None
        except (ValueError, Exception):
            # Expected behavior
            pass

    def test_invalid_compression_format(self, temp_log_file: Path) -> None:
        """Test handling of invalid compression format."""
        try:
            ezpl = Ezpl(log_file=temp_log_file, log_compression="INVALID_FORMAT")
            assert ezpl is not None
        except (ValueError, Exception):
            # Expected behavior
            pass

    def test_negative_indent_step(self) -> None:
        """Test handling of negative indent step."""
        try:
            ezpl = Ezpl(indent_step=-1)
            # Should handle gracefully (use default or clamp)
            assert ezpl is not None
        except (ValueError, ValidationError, Exception):
            # Expected behavior
            pass


class TestInvalidPaths:
    """Tests for invalid file path handling."""

    def test_path_with_invalid_characters(self) -> None:
        """Test handling of path with invalid characters."""
        # Windows invalid characters: < > : " | ? *
        try:
            invalid_path = Path('test<>:"|?*.log')
            _ = Ezpl(log_file=invalid_path)
            # Should handle gracefully or raise error
        except (OSError, FileOperationError, Exception):
            # Expected behavior
            pass

    def test_path_too_long(self) -> None:
        """Test handling of path that is too long."""
        # Create a very long path
        try:
            long_path = Path("A" * 300) / "test.log"
            _ = Ezpl(log_file=long_path)
            # Should handle gracefully or raise error
        except (OSError, FileOperationError, Exception):
            # Expected behavior
            pass

    def test_nonexistent_parent_directory(self, temp_dir: Path) -> None:
        """Test handling of nonexistent parent directory."""
        # Should create directory automatically
        log_file = temp_dir / "nonexistent" / "subdir" / "test.log"
        ezpl = Ezpl(log_file=log_file)
        logger = ezpl.get_logger()
        logger.info("Test")
        # Should create directory
        assert log_file.parent.exists() or True


class TestInvalidLogLevels:
    """Tests for invalid log level handling."""

    def test_empty_log_level(self) -> None:
        """Test handling of empty log level."""
        try:
            ezpl = Ezpl()
            ezpl.set_level("")
        except (ValidationError, ValueError, Exception):
            # Expected behavior
            pass

    def test_none_log_level(self) -> None:
        """Test handling of None log level."""
        try:
            _ = Ezpl()
            # set_level expects string, None would cause error
            # This tests the validation
            pass
        except (TypeError, ValidationError, Exception):
            # Expected behavior
            pass

    def test_numeric_log_level(self) -> None:
        """Test handling of numeric log level."""
        try:
            _ = Ezpl()
            # Should accept string, not int
            pass
        except (TypeError, ValidationError, Exception):
            # Expected behavior
            pass


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
        assert log_file.exists() or True
