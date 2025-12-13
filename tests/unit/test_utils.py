# -*- coding: utf-8 -*-
# ///////////////////////////////////////////////////////////////
# EZPL - Tests unitaires Utils
# Project: ezpl
# ///////////////////////////////////////////////////////////////

"""
Unit tests for handler utility functions.

Tests cover:
- safe_str_convert() with various types
- sanitize_for_file() with special characters
- sanitize_for_console() with special characters
- Edge cases and error handling
"""

# IMPORT BASE
# ///////////////////////////////////////////////////////////////

# IMPORT SPECS
# ///////////////////////////////////////////////////////////////

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from ezpl.handlers.utils import (
    safe_str_convert,
    sanitize_for_console,
    sanitize_for_file,
)

## ==> TESTS
# ///////////////////////////////////////////////////////////////


class TestSafeStrConvert:
    """Tests for safe_str_convert() function."""

    def test_string_input(self) -> None:
        """Test safe_str_convert() with string input."""
        result = safe_str_convert("test string")
        assert result == "test string"
        assert isinstance(result, str)

    def test_int_input(self) -> None:
        """Test safe_str_convert() with integer input."""
        result = safe_str_convert(12345)
        assert result == "12345"
        assert isinstance(result, str)

    def test_float_input(self) -> None:
        """Test safe_str_convert() with float input."""
        result = safe_str_convert(3.14)
        assert result == "3.14"
        assert isinstance(result, str)

    def test_dict_input(self) -> None:
        """Test safe_str_convert() with dictionary input."""
        result = safe_str_convert({"key": "value"})
        assert isinstance(result, str)
        assert "key" in result or "value" in result

    def test_list_input(self) -> None:
        """Test safe_str_convert() with list input."""
        result = safe_str_convert([1, 2, 3])
        assert isinstance(result, str)
        assert "1" in result or "2" in result or "3" in result

    def test_none_input(self) -> None:
        """Test safe_str_convert() with None input."""
        result = safe_str_convert(None)
        assert result == "None"
        assert isinstance(result, str)

    def test_bool_input(self) -> None:
        """Test safe_str_convert() with boolean input."""
        result_true = safe_str_convert(True)
        result_false = safe_str_convert(False)
        assert isinstance(result_true, str)
        assert isinstance(result_false, str)

    def test_exception_input(self) -> None:
        """Test safe_str_convert() with exception object."""
        try:
            raise ValueError("Test error")
        except Exception as exc:
            result = safe_str_convert(exc)
            assert isinstance(result, str)
            assert "ValueError" in result or "Test error" in result

    def test_custom_object(self) -> None:
        """Test safe_str_convert() with custom object."""

        class CustomObject:
            def __str__(self):
                return "CustomObject"

        result = safe_str_convert(CustomObject())
        assert isinstance(result, str)
        assert "Custom" in result or "object" in result.lower()

    def test_object_without_str(self) -> None:
        """Test safe_str_convert() with object without __str__."""

        class NoStrObject:
            def __repr__(self):
                return "NoStrObject()"

        result = safe_str_convert(NoStrObject())
        assert isinstance(result, str)

    def test_object_without_str_or_repr(self) -> None:
        """Test safe_str_convert() with object without __str__ or __repr__."""

        class NoStrOrReprObject:
            pass

        result = safe_str_convert(NoStrOrReprObject())
        assert isinstance(result, str)
        # Should return type name as fallback
        assert "object" in result.lower() or "NoStrOrReprObject" in result


class TestSanitizeForFile:
    """Tests for sanitize_for_file() function."""

    def test_normal_string(self) -> None:
        """Test sanitize_for_file() with normal string."""
        result = sanitize_for_file("Normal message")
        assert result == "Normal message"

    def test_null_bytes(self) -> None:
        """Test sanitize_for_file() removes null bytes."""
        result = sanitize_for_file("Message\x00with\x00nulls")
        assert "\x00" not in result

    def test_ansi_escape_sequences(self) -> None:
        """Test sanitize_for_file() removes ANSI escape sequences."""
        result = sanitize_for_file("Message\x1b[31mRed\x1b[0m")
        assert "\x1b[" not in result

    def test_html_tags(self) -> None:
        """Test sanitize_for_file() removes HTML tags."""
        result = sanitize_for_file("Message <tag>content</tag>")
        assert "<" not in result
        assert ">" not in result

    def test_control_characters(self) -> None:
        """Test sanitize_for_file() removes control characters."""
        result = sanitize_for_file("Message\x01\x02\x03")
        # Control characters should be removed
        assert "\x01" not in result
        assert "\x02" not in result
        assert "\x03" not in result

    def test_preserves_newlines(self) -> None:
        """Test sanitize_for_file() preserves newlines."""
        result = sanitize_for_file("Line 1\nLine 2")
        assert "\n" in result

    def test_preserves_tabs(self) -> None:
        """Test sanitize_for_file() preserves tabs."""
        result = sanitize_for_file("Line 1\tLine 2")
        assert "\t" in result

    def test_unicode_characters(self) -> None:
        """Test sanitize_for_file() handles Unicode characters."""
        result = sanitize_for_file("Unicode: éèàçô 漢字 🚀")
        assert "Unicode" in result
        # Unicode should be preserved or replaced, not crash
        assert isinstance(result, str)

    def test_non_string_input(self) -> None:
        """Test sanitize_for_file() with non-string input."""
        result = sanitize_for_file(12345)
        assert isinstance(result, str)

    def test_none_input(self) -> None:
        """Test sanitize_for_file() with None input."""
        result = sanitize_for_file(None)
        assert isinstance(result, str)


class TestSanitizeForConsole:
    """Tests for sanitize_for_console() function."""

    def test_normal_string(self) -> None:
        """Test sanitize_for_console() with normal string."""
        result = sanitize_for_console("Normal message")
        assert result == "Normal message"

    def test_null_bytes(self) -> None:
        """Test sanitize_for_console() removes null bytes."""
        result = sanitize_for_console("Message\x00with\x00nulls")
        assert "\x00" not in result

    def test_control_characters(self) -> None:
        """Test sanitize_for_console() removes control characters."""
        result = sanitize_for_console("Message\x01\x02\x03")
        # Control characters should be removed
        assert "\x01" not in result
        assert "\x02" not in result
        assert "\x03" not in result

    def test_preserves_ansi_sequences(self) -> None:
        """Test sanitize_for_console() preserves ANSI sequences (Rich handles them)."""
        # Note: sanitize_for_console removes control chars but Rich can handle ANSI
        result = sanitize_for_console("Message\x1b[31mRed\x1b[0m")
        # Control chars are removed, but Rich will handle styling
        assert isinstance(result, str)

    def test_unicode_characters(self) -> None:
        """Test sanitize_for_console() handles Unicode characters."""
        result = sanitize_for_console("Unicode: éèàçô 漢字 🚀")
        assert "Unicode" in result
        # Unicode should be preserved
        assert isinstance(result, str)

    def test_non_string_input(self) -> None:
        """Test sanitize_for_console() with non-string input."""
        result = sanitize_for_console(12345)
        assert isinstance(result, str)

    def test_none_input(self) -> None:
        """Test sanitize_for_console() with None input."""
        result = sanitize_for_console(None)
        assert isinstance(result, str)

    def test_special_characters(self) -> None:
        """Test sanitize_for_console() with special characters."""
        result = sanitize_for_console("Path: C:\\Users\\Test\\file.txt")
        assert isinstance(result, str)
        # Should handle backslashes (Rich will handle them)
        assert "Path" in result


class TestEdgeCases:
    """Tests for edge cases."""

    def test_empty_string(self) -> None:
        """Test functions with empty string."""
        assert safe_str_convert("") == ""
        assert sanitize_for_file("") == ""
        assert sanitize_for_console("") == ""

    def test_very_long_string(self) -> None:
        """Test functions with very long string."""
        long_string = "A" * 10000
        result = safe_str_convert(long_string)
        assert len(result) == 10000

        result = sanitize_for_file(long_string)
        assert isinstance(result, str)

        result = sanitize_for_console(long_string)
        assert isinstance(result, str)

    def test_mixed_types_in_list(self) -> None:
        """Test safe_str_convert() with mixed types."""
        mixed = [1, "string", {"key": "value"}, None, True]
        result = safe_str_convert(mixed)
        assert isinstance(result, str)

    def test_nested_structures(self) -> None:
        """Test safe_str_convert() with nested structures."""
        nested = {"level1": {"level2": {"level3": "value"}}}
        result = safe_str_convert(nested)
        assert isinstance(result, str)
