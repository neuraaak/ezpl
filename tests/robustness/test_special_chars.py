# -*- coding: utf-8 -*-
# ///////////////////////////////////////////////////////////////
# EZPL - Tests de robustesse - Caractères spéciaux
# Project: ezpl
# ///////////////////////////////////////////////////////////////

"""
Robustness tests for special character handling.

Tests cover:
- Unicode characters
- Control characters
- ANSI escape sequences
- HTML/XML tags
- Windows paths with backslashes
- Very long messages
- Empty or None messages
"""

# IMPORT BASE
# ///////////////////////////////////////////////////////////////
import time
from pathlib import Path

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from ezpl import Ezpl

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


class TestUnicodeCharacters:
    """Tests for Unicode character handling."""

    def test_complex_unicode_printer(self) -> None:
        """Test printer with complex Unicode characters."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()

        # Various Unicode characters
        unicode_messages = [
            "éèàçô",
            "漢字",
            "🚀",
            "αβγ",
            "АБВ",
            "مرحبا",
            "नमस्ते",
        ]

        for msg in unicode_messages:
            printer.info(msg)
            # Verify no exception raised

    def test_complex_unicode_logger(self, temp_log_file: Path) -> None:
        """Test logger with complex Unicode characters."""
        ezpl = Ezpl(log_file=temp_log_file)
        logger = ezpl.get_logger()

        unicode_messages = [
            "éèàçô",
            "漢字",
            "🚀",
            "αβγ",
            "АБВ",
        ]

        for msg in unicode_messages:
            logger.info(msg)

        wait_for_file(temp_log_file)
        content = temp_log_file.read_text(encoding="utf-8")
        # Verify Unicode is preserved or handled
        assert len(content) > 0


class TestControlCharacters:
    """Tests for control character handling."""

    def test_null_bytes_printer(self) -> None:
        """Test printer with null bytes."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        printer.error("Message\x00with\x00nulls")
        # Should not crash

    def test_null_bytes_logger(self, temp_log_file: Path) -> None:
        """Test logger with null bytes."""
        ezpl = Ezpl(log_file=temp_log_file)
        logger = ezpl.get_logger()
        logger.info("Message\x00with\x00nulls")
        wait_for_file(temp_log_file)
        # Should not crash, null bytes should be removed

    def test_other_control_chars_printer(self) -> None:
        """Test printer with other control characters."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        printer.error("Message\x01\x02\x03")
        # Should not crash

    def test_other_control_chars_logger(self, temp_log_file: Path) -> None:
        """Test logger with other control characters."""
        ezpl = Ezpl(log_file=temp_log_file)
        logger = ezpl.get_logger()
        logger.info("Message\x01\x02\x03")
        wait_for_file(temp_log_file)
        # Should not crash


class TestANSIEscapeSequences:
    """Tests for ANSI escape sequence handling."""

    def test_ansi_sequences_printer(self) -> None:
        """Test printer with ANSI escape sequences."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        printer.error("Message\x1b[31mRed\x1b[0m")
        # Should not crash (Rich handles ANSI)

    def test_ansi_sequences_logger(self, temp_log_file: Path) -> None:
        """Test logger with ANSI escape sequences."""
        ezpl = Ezpl(log_file=temp_log_file)
        logger = ezpl.get_logger()
        logger.info("Message\x1b[31mRed\x1b[0m")
        wait_for_file(temp_log_file)
        # Should not crash, ANSI should be removed from file


class TestHTMLXMLTags:
    """Tests for HTML/XML tag handling."""

    def test_html_tags_printer(self) -> None:
        """Test printer with HTML tags."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        printer.error("Message <tag>content</tag>")
        # Should not crash

    def test_html_tags_logger(self, temp_log_file: Path) -> None:
        """Test logger with HTML tags."""
        ezpl = Ezpl(log_file=temp_log_file)
        logger = ezpl.get_logger()
        logger.info("Message <tag>content</tag>")
        wait_for_file(temp_log_file)
        # Should not crash, tags should be sanitized


class TestWindowsPaths:
    """Tests for Windows path handling."""

    def test_windows_path_printer(self) -> None:
        """Test printer with Windows path."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        printer.error("Path: C:\\Users\\Test\\file.txt")
        # Should not crash

    def test_windows_path_logger(self, temp_log_file: Path) -> None:
        """Test logger with Windows path."""
        ezpl = Ezpl(log_file=temp_log_file)
        logger = ezpl.get_logger()
        logger.info("Path: C:\\Users\\Test\\file.txt")
        wait_for_file(temp_log_file)
        # Should not crash


class TestLongMessages:
    """Tests for very long message handling."""

    def test_very_long_message_printer(self) -> None:
        """Test printer with very long message."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        long_message = "A" * 10000
        printer.info(long_message)
        # Should not crash

    def test_very_long_message_logger(self, temp_log_file: Path) -> None:
        """Test logger with very long message."""
        ezpl = Ezpl(log_file=temp_log_file)
        logger = ezpl.get_logger()
        long_message = "A" * 10000
        logger.info(long_message)
        wait_for_file(temp_log_file)
        # Should not crash

    def test_extremely_long_message(self, temp_log_file: Path) -> None:
        """Test with extremely long message (>100KB)."""
        ezpl = Ezpl(log_file=temp_log_file)
        logger = ezpl.get_logger()
        extremely_long = "A" * 200000  # 200KB
        logger.info(extremely_long)
        wait_for_file(temp_log_file)
        # Should not crash


class TestEmptyNoneMessages:
    """Tests for empty or None message handling."""

    def test_empty_string_printer(self) -> None:
        """Test printer with empty string."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        printer.info("")
        # Should not crash

    def test_empty_string_logger(self, temp_log_file: Path) -> None:
        """Test logger with empty string."""
        ezpl = Ezpl(log_file=temp_log_file)
        logger = ezpl.get_logger()
        logger.info("")
        wait_for_file(temp_log_file)
        # Should not crash

    def test_none_message_printer(self) -> None:
        """Test printer with None message."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        printer.info(None)
        # Should not crash, should convert to "None"

    def test_none_message_logger(self, temp_log_file: Path) -> None:
        """Test logger with None message."""
        ezpl = Ezpl(log_file=temp_log_file)
        logger = ezpl.get_logger()
        logger.info(None)
        wait_for_file(temp_log_file)
        # Should not crash


class TestMixedSpecialCharacters:
    """Tests for mixed special characters."""

    def test_mixed_special_chars_printer(self) -> None:
        """Test printer with mixed special characters."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        mixed = "Unicode: éèàçô 漢字 🚀\x00\x1b[31m<tag>Path: C:\\Users\\file.txt</tag>"
        printer.error(mixed)
        # Should not crash

    def test_mixed_special_chars_logger(self, temp_log_file: Path) -> None:
        """Test logger with mixed special characters."""
        ezpl = Ezpl(log_file=temp_log_file)
        logger = ezpl.get_logger()
        mixed = "Unicode: éèàçô 漢字 🚀\x00\x1b[31m<tag>Path: C:\\Users\\file.txt</tag>"
        logger.info(mixed)
        wait_for_file(temp_log_file)
        # Should not crash
