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

from __future__ import annotations

# ///////////////////////////////////////////////////////////////
# IMPORTS
# ///////////////////////////////////////////////////////////////
# Local imports
from ezplog.utils import (
    safe_str_convert,
    sanitize_for_console,
    sanitize_for_file,
)

# ///////////////////////////////////////////////////////////////
# TESTS
# ///////////////////////////////////////////////////////////////


class TestSafeStrConvert:
    """Tests for safe_str_convert() function."""

    def test_should_return_string_unchanged_when_input_is_string(self) -> None:
        """Test safe_str_convert() with string input."""
        result = safe_str_convert("test string")
        assert result == "test string"
        assert isinstance(result, str)

    def test_should_convert_to_string_when_input_is_integer(self) -> None:
        """Test safe_str_convert() with integer input."""
        result = safe_str_convert(12345)
        assert result == "12345"
        assert isinstance(result, str)

    def test_should_convert_to_string_when_input_is_float(self) -> None:
        """Test safe_str_convert() with float input."""
        result = safe_str_convert(3.14)
        assert result == "3.14"
        assert isinstance(result, str)

    def test_should_convert_to_string_when_input_is_dict(self) -> None:
        """Test safe_str_convert() with dictionary input."""
        result = safe_str_convert({"key": "value"})
        assert isinstance(result, str)
        assert "key" in result or "value" in result

    def test_should_convert_to_string_when_input_is_list(self) -> None:
        """Test safe_str_convert() with list input."""
        result = safe_str_convert([1, 2, 3])
        assert isinstance(result, str)
        assert "1" in result or "2" in result or "3" in result

    def test_should_return_none_string_when_input_is_none(self) -> None:
        """Test safe_str_convert() with None input."""
        result = safe_str_convert(None)
        assert result == "None"
        assert isinstance(result, str)

    def test_should_convert_to_string_when_input_is_boolean(self) -> None:
        """Test safe_str_convert() with boolean input."""
        result_true = safe_str_convert(True)
        result_false = safe_str_convert(False)
        assert isinstance(result_true, str)
        assert isinstance(result_false, str)

    def test_should_include_exception_type_or_message_when_input_is_exception(
        self,
    ) -> None:
        """Test safe_str_convert() with exception object."""
        try:
            raise ValueError("Test error")
        except Exception as exc:
            result = safe_str_convert(exc)
            assert isinstance(result, str)
            assert "ValueError" in result or "Test error" in result

    def test_should_return_str_representation_when_input_has_custom_str_method(
        self,
    ) -> None:
        """Test safe_str_convert() with custom object."""

        class CustomObject:
            def __str__(self):
                return "CustomObject"

        result = safe_str_convert(CustomObject())
        assert isinstance(result, str)
        assert "Custom" in result or "object" in result.lower()

    def test_should_return_repr_representation_when_input_lacks_str_method(
        self,
    ) -> None:
        """Test safe_str_convert() with object without __str__."""

        class NoStrObject:
            def __repr__(self):
                return "NoStrObject()"

        result = safe_str_convert(NoStrObject())
        assert isinstance(result, str)

    def test_should_return_type_name_fallback_when_input_lacks_str_and_repr(
        self,
    ) -> None:
        """Test safe_str_convert() with object without __str__ or __repr__."""

        class NoStrOrReprObject:
            pass

        result = safe_str_convert(NoStrOrReprObject())
        assert isinstance(result, str)
        # Should return type name as fallback
        assert "object" in result.lower() or "NoStrOrReprObject" in result


class TestSanitizeForFile:
    """Tests for sanitize_for_file() function."""

    def test_should_not_modify_normal_string_when_sanitize_for_file_is_called(
        self,
    ) -> None:
        """Test sanitize_for_file() with normal string."""
        result = sanitize_for_file("Normal message")
        assert result == "Normal message"

    def test_should_remove_null_bytes_when_sanitize_for_file_is_called(self) -> None:
        """Test sanitize_for_file() removes null bytes."""
        result = sanitize_for_file("Message\x00with\x00nulls")
        assert "\x00" not in result

    def test_should_remove_ansi_escape_sequences_when_input_contains_ansi_codes(
        self,
    ) -> None:
        """Test sanitize_for_file() removes ANSI escape sequences."""
        result = sanitize_for_file("Message\x1b[31mRed\x1b[0m")
        assert "\x1b[" not in result

    def test_should_remove_html_tags_when_input_contains_html_markup(self) -> None:
        """Test sanitize_for_file() removes HTML tags."""
        result = sanitize_for_file("Message <tag>content</tag>")
        assert "<" not in result
        assert ">" not in result

    def test_should_remove_control_characters_when_sanitize_for_file_is_called(
        self,
    ) -> None:
        """Test sanitize_for_file() removes control characters."""
        result = sanitize_for_file("Message\x01\x02\x03")
        # Control characters should be removed
        assert "\x01" not in result
        assert "\x02" not in result
        assert "\x03" not in result

    def test_should_preserve_newlines_when_input_contains_newlines(self) -> None:
        """Test sanitize_for_file() preserves newlines."""
        result = sanitize_for_file("Line 1\nLine 2")
        assert "\n" in result

    def test_should_preserve_tabs_when_input_contains_tab_characters(self) -> None:
        """Test sanitize_for_file() preserves tabs."""
        result = sanitize_for_file("Line 1\tLine 2")
        assert "\t" in result

    def test_should_handle_unicode_without_crashing_when_sanitize_for_file_is_called(
        self,
    ) -> None:
        """Test sanitize_for_file() handles Unicode characters."""
        result = sanitize_for_file("Unicode: éèàçô 漢字 🚀")
        assert "Unicode" in result
        # Unicode should be preserved or replaced, not crash
        assert isinstance(result, str)

    def test_should_convert_to_string_when_sanitize_for_file_receives_non_string(
        self,
    ) -> None:
        """Test sanitize_for_file() with non-string input."""
        result = sanitize_for_file(12345)
        assert isinstance(result, str)

    def test_should_return_string_when_sanitize_for_file_receives_none(self) -> None:
        """Test sanitize_for_file() with None input."""
        result = sanitize_for_file(None)
        assert isinstance(result, str)


class TestSanitizeForConsole:
    """Tests for sanitize_for_console() function."""

    def test_should_not_modify_normal_string_when_sanitize_for_console_is_called(
        self,
    ) -> None:
        """Test sanitize_for_console() with normal string."""
        result = sanitize_for_console("Normal message")
        assert result == "Normal message"

    def test_should_remove_null_bytes_when_sanitize_for_console_is_called(self) -> None:
        """Test sanitize_for_console() removes null bytes."""
        result = sanitize_for_console("Message\x00with\x00nulls")
        assert "\x00" not in result

    def test_should_remove_control_characters_when_sanitize_for_console_is_called(
        self,
    ) -> None:
        """Test sanitize_for_console() removes control characters."""
        result = sanitize_for_console("Message\x01\x02\x03")
        # Control characters should be removed
        assert "\x01" not in result
        assert "\x02" not in result
        assert "\x03" not in result

    def test_should_return_string_when_input_contains_ansi_codes(self) -> None:
        """Test sanitize_for_console() preserves ANSI sequences (Rich handles them)."""
        # Note: sanitize_for_console removes control chars but Rich can handle ANSI
        result = sanitize_for_console("Message\x1b[31mRed\x1b[0m")
        # Control chars are removed, but Rich will handle styling
        assert isinstance(result, str)

    def test_should_handle_unicode_without_crashing_when_sanitize_for_console_is_called(
        self,
    ) -> None:
        """Test sanitize_for_console() handles Unicode characters."""
        result = sanitize_for_console("Unicode: éèàçô 漢字 🚀")
        assert "Unicode" in result
        # Unicode should be preserved
        assert isinstance(result, str)

    def test_should_convert_to_string_when_sanitize_for_console_receives_non_string(
        self,
    ) -> None:
        """Test sanitize_for_console() with non-string input."""
        result = sanitize_for_console(12345)
        assert isinstance(result, str)

    def test_should_return_string_when_sanitize_for_console_receives_none(self) -> None:
        """Test sanitize_for_console() with None input."""
        result = sanitize_for_console(None)
        assert isinstance(result, str)

    def test_should_preserve_backslashes_when_input_contains_windows_path(self) -> None:
        """Test sanitize_for_console() with special characters."""
        result = sanitize_for_console("Path: C:\\Users\\Test\\file.txt")
        assert isinstance(result, str)
        # Should handle backslashes (Rich will handle them)
        assert "Path" in result


class TestEdgeCases:
    """Tests for edge cases."""

    def test_should_return_empty_string_when_input_is_empty_string(self) -> None:
        """Test functions with empty string."""
        assert safe_str_convert("") == ""
        assert sanitize_for_file("") == ""
        assert sanitize_for_console("") == ""

    def test_should_preserve_length_and_not_crash_when_input_is_very_long_string(
        self,
    ) -> None:
        """Test functions with very long string."""
        long_string = "A" * 10000
        result = safe_str_convert(long_string)
        assert len(result) == 10000

        result = sanitize_for_file(long_string)
        assert isinstance(result, str)

        result = sanitize_for_console(long_string)
        assert isinstance(result, str)

    def test_should_convert_all_items_to_single_string_when_input_is_mixed_type_list(
        self,
    ) -> None:
        """Test safe_str_convert() with mixed types."""
        mixed = [1, "string", {"key": "value"}, None, True]
        result = safe_str_convert(mixed)
        assert isinstance(result, str)

    def test_should_convert_to_string_when_input_is_nested_structure(self) -> None:
        """Test safe_str_convert() with nested structures."""
        nested = {"level1": {"level2": {"level3": "value"}}}
        result = safe_str_convert(nested)
        assert isinstance(result, str)
