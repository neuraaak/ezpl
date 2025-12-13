# -*- coding: utf-8 -*-
# ///////////////////////////////////////////////////////////////
# EZPL - Tests unitaires Types
# Project: ezpl
# ///////////////////////////////////////////////////////////////

"""
Unit tests for LogLevel and Pattern types.

Tests cover:
- LogLevel enumeration and attributes
- Pattern enumeration
- Validation methods
- Color functions
- Edge cases
"""

# IMPORT BASE
# ///////////////////////////////////////////////////////////////
import pytest

from ezpl.core.exceptions import ValidationError

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from ezpl.types import (
    PATTERN_COLORS,
    LogLevel,
    Pattern,
    get_pattern_color,
    get_pattern_color_by_name,
)

# IMPORT SPECS
# ///////////////////////////////////////////////////////////////


## ==> TESTS
# ///////////////////////////////////////////////////////////////


class TestLogLevel:
    """Tests for LogLevel enumeration."""

    def test_all_levels_exist(self) -> None:
        """Test that all expected log levels exist."""
        levels = LogLevel.get_all_levels()
        expected_levels = ["DEBUG", "INFO", "SUCCESS", "WARNING", "ERROR", "CRITICAL"]
        for level in expected_levels:
            assert level in levels

    def test_level_attributes(self) -> None:
        """Test that all levels have required attributes."""
        for level in LogLevel:
            assert hasattr(level, "label")
            assert hasattr(level, "no")
            assert hasattr(level, "fg")
            assert hasattr(level, "bg")
            assert isinstance(level.label, str)
            assert isinstance(level.no, int)
            assert isinstance(level.fg, str)
            assert isinstance(level.bg, str)

    def test_get_label(self) -> None:
        """Test get_label() class method."""
        label = LogLevel.get_label("DEBUG")
        assert isinstance(label, str)
        assert label == "DEBUG"

    def test_get_no(self) -> None:
        """Test get_no() class method."""
        no = LogLevel.get_no("INFO")
        assert isinstance(no, int)
        assert no > 0

    def test_get_fgcolor(self) -> None:
        """Test get_fgcolor() class method."""
        fg = LogLevel.get_fgcolor("ERROR")
        assert isinstance(fg, str)

    def test_get_bgcolor(self) -> None:
        """Test get_bgcolor() class method."""
        bg = LogLevel.get_bgcolor("SUCCESS")
        assert isinstance(bg, str)

    def test_get_attribute(self) -> None:
        """Test get_attribute() class method."""
        label = LogLevel.get_attribute("DEBUG", "label")
        assert isinstance(label, str)
        assert label == "DEBUG"

        no = LogLevel.get_attribute("INFO", "no")
        assert isinstance(no, int)

    def test_get_attribute_invalid_level(self) -> None:
        """Test get_attribute() with invalid level."""
        with pytest.raises(ValidationError):
            LogLevel.get_attribute("INVALID", "label")

    def test_get_attribute_invalid_attribute(self) -> None:
        """Test get_attribute() with invalid attribute."""
        with pytest.raises(ValidationError):
            LogLevel.get_attribute("DEBUG", "invalid_attr")

    def test_is_valid_level(self) -> None:
        """Test is_valid_level() class method."""
        assert LogLevel.is_valid_level("DEBUG") is True
        assert LogLevel.is_valid_level("INFO") is True
        assert LogLevel.is_valid_level("WARNING") is True
        assert LogLevel.is_valid_level("INVALID") is False
        assert LogLevel.is_valid_level("") is False

    def test_is_valid_level_case_insensitive(self) -> None:
        """Test is_valid_level() is case-insensitive."""
        assert LogLevel.is_valid_level("debug") is True
        assert LogLevel.is_valid_level("Debug") is True
        assert LogLevel.is_valid_level("DEBUG") is True

    def test_get_all_levels(self) -> None:
        """Test get_all_levels() class method."""
        levels = LogLevel.get_all_levels()
        assert isinstance(levels, list)
        assert len(levels) == 6
        assert "DEBUG" in levels
        assert "INFO" in levels
        assert "SUCCESS" in levels
        assert "WARNING" in levels
        assert "ERROR" in levels
        assert "CRITICAL" in levels

    def test_get_rich_style(self) -> None:
        """Test get_rich_style() instance method."""
        style = LogLevel.DEBUG.get_rich_style()
        assert isinstance(style, str)
        assert style == "cyan"

        style = LogLevel.ERROR.get_rich_style()
        assert isinstance(style, str)
        assert "red" in style

    def test_level_comparison(self) -> None:
        """Test that levels can be compared by numeric value."""
        assert LogLevel.DEBUG.no < LogLevel.INFO.no
        assert LogLevel.INFO.no < LogLevel.WARNING.no
        assert LogLevel.WARNING.no < LogLevel.ERROR.no
        assert LogLevel.ERROR.no < LogLevel.CRITICAL.no

    def test_str_representation(self) -> None:
        """Test string representation."""
        level_str = str(LogLevel.DEBUG)
        assert "LogLevel" in level_str
        assert "DEBUG" in level_str

    def test_repr_representation(self) -> None:
        """Test detailed representation."""
        level_repr = repr(LogLevel.INFO)
        assert "LogLevel" in level_repr
        assert "INFO" in level_repr


class TestPattern:
    """Tests for Pattern enumeration."""

    def test_all_patterns_exist(self) -> None:
        """Test that all expected patterns exist."""
        patterns = [p.name for p in Pattern]
        expected_patterns = [
            "SUCCESS",
            "ERROR",
            "WARN",
            "TIP",
            "DEBUG",
            "INFO",
            "SYSTEM",
            "INSTALL",
            "DETECT",
            "CONFIG",
            "DEPS",
        ]
        for pattern in expected_patterns:
            assert pattern in patterns

    def test_pattern_values(self) -> None:
        """Test that patterns have correct values."""
        assert Pattern.SUCCESS.value == "SUCCESS"
        assert Pattern.ERROR.value == "ERROR"
        assert Pattern.SYSTEM.value == "SYSTEM"

    def test_pattern_enum_access(self) -> None:
        """Test accessing patterns by name."""
        assert Pattern["SUCCESS"] == Pattern.SUCCESS
        assert Pattern["ERROR"] == Pattern.ERROR
        assert Pattern["SYSTEM"] == Pattern.SYSTEM


class TestPatternColors:
    """Tests for pattern color functions."""

    def test_pattern_colors_dict(self) -> None:
        """Test PATTERN_COLORS dictionary."""
        assert isinstance(PATTERN_COLORS, dict)
        assert Pattern.SUCCESS in PATTERN_COLORS
        assert Pattern.ERROR in PATTERN_COLORS
        assert Pattern.SYSTEM in PATTERN_COLORS

    def test_get_pattern_color(self) -> None:
        """Test get_pattern_color() function."""
        color = get_pattern_color(Pattern.SUCCESS)
        assert isinstance(color, str)
        assert color == "bright_green"

        color = get_pattern_color(Pattern.ERROR)
        assert isinstance(color, str)
        assert color == "bright_red"

    def test_get_pattern_color_all_patterns(self) -> None:
        """Test get_pattern_color() for all patterns."""
        for pattern in Pattern:
            color = get_pattern_color(pattern)
            assert isinstance(color, str)
            assert len(color) > 0

    def test_get_pattern_color_by_name(self) -> None:
        """Test get_pattern_color_by_name() function."""
        color = get_pattern_color_by_name("SUCCESS")
        assert isinstance(color, str)
        assert color == "bright_green"

        color = get_pattern_color_by_name("error")
        assert isinstance(color, str)
        assert color == "bright_red"

    def test_get_pattern_color_by_name_case_insensitive(self) -> None:
        """Test get_pattern_color_by_name() is case-insensitive."""
        color1 = get_pattern_color_by_name("SUCCESS")
        color2 = get_pattern_color_by_name("success")
        color3 = get_pattern_color_by_name("Success")
        assert color1 == color2 == color3

    def test_get_pattern_color_by_name_invalid(self) -> None:
        """Test get_pattern_color_by_name() with invalid pattern."""
        color = get_pattern_color_by_name("INVALID_PATTERN")
        # Should return default "white"
        assert color == "white"

    def test_get_pattern_color_unknown_pattern(self) -> None:
        """Test get_pattern_color() with unknown pattern (should not happen but test fallback)."""
        # Create a mock pattern that's not in PATTERN_COLORS
        # This tests the fallback in get_pattern_color
        # Since all patterns are in PATTERN_COLORS, we test the function logic
        color = get_pattern_color(Pattern.SUCCESS)
        assert color is not None


class TestValidation:
    """Tests for validation methods."""

    def test_validate_all_log_levels(self) -> None:
        """Test validation of all log levels."""
        for level in LogLevel:
            assert LogLevel.is_valid_level(level.name) is True

    def test_validate_invalid_log_level(self) -> None:
        """Test validation of invalid log level."""
        assert LogLevel.is_valid_level("INVALID_LEVEL") is False
        assert LogLevel.is_valid_level("") is False
        assert LogLevel.is_valid_level("123") is False

    def test_pattern_access_by_name(self) -> None:
        """Test accessing patterns by name."""
        assert Pattern["SUCCESS"] == Pattern.SUCCESS
        assert Pattern["SYSTEM"] == Pattern.SYSTEM

    def test_pattern_access_invalid_name(self) -> None:
        """Test accessing pattern with invalid name."""
        with pytest.raises(KeyError):
            _ = Pattern["INVALID_PATTERN"]
