# -*- coding: utf-8 -*-
# ///////////////////////////////////////////////////////////////
# EZPL - Tests unitaires Printer
# Project: ezpl
# ///////////////////////////////////////////////////////////////

"""
Unit tests for ConsolePrinter and ConsolePrinterWrapper.

Tests cover:
- All log levels
- All pattern methods
- Indentation management
- Rich features (tables, panels, JSON)
- Special character handling
- Type conversion
- Error handling
"""

# IMPORT BASE
# ///////////////////////////////////////////////////////////////

# IMPORT SPECS
# ///////////////////////////////////////////////////////////////

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from ezpl import Ezpl
from ezpl.types import Pattern

## ==> TESTS
# ///////////////////////////////////////////////////////////////


class TestLogLevels:
    """Tests for all log level methods."""

    def test_debug_level(self) -> None:
        """Test debug() method."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        printer.debug("Debug message")
        # Verify no exception raised

    def test_info_level(self) -> None:
        """Test info() method."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        printer.info("Info message")
        # Verify no exception raised

    def test_success_level(self) -> None:
        """Test success() method."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        printer.success("Success message")
        # Verify no exception raised

    def test_warning_level(self) -> None:
        """Test warning() method."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        printer.warning("Warning message")
        # Verify no exception raised

    def test_warn_alias(self) -> None:
        """Test warn() alias for warning()."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        printer.warn("Warn message")
        # Verify no exception raised

    def test_error_level(self) -> None:
        """Test error() method."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        printer.error("Error message")
        # Verify no exception raised

    def test_critical_level(self) -> None:
        """Test critical() method."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        printer.critical("Critical message")
        # Verify no exception raised

    def test_all_levels_in_sequence(self) -> None:
        """Test all log levels in sequence."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        printer.debug("Debug message")
        printer.info("Info message")
        printer.success("Success message")
        printer.warning("Warning message")
        printer.error("Error message")
        printer.critical("Critical message")
        # Verify no exception raised


class TestPatternMethods:
    """Tests for all pattern methods."""

    def test_tip_pattern(self) -> None:
        """Test tip() pattern method."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        printer.tip("Tip message")
        # Verify no exception raised

    def test_system_pattern(self) -> None:
        """Test system() pattern method."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        printer.system("System message")
        # Verify no exception raised

    def test_install_pattern(self) -> None:
        """Test install() pattern method."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        printer.install("Install message")
        # Verify no exception raised

    def test_detect_pattern(self) -> None:
        """Test detect() pattern method."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        printer.detect("Detect message")
        # Verify no exception raised

    def test_config_pattern(self) -> None:
        """Test config() pattern method."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        printer.config("Config message")
        # Verify no exception raised

    def test_deps_pattern(self) -> None:
        """Test deps() pattern method."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        printer.deps("Deps message")
        # Verify no exception raised

    def test_all_patterns_in_sequence(self) -> None:
        """Test all pattern methods in sequence."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        printer.tip("Tip")
        printer.system("System")
        printer.install("Install")
        printer.detect("Detect")
        printer.config("Config")
        printer.deps("Deps")
        # Verify no exception raised

    def test_print_pattern_with_string(self) -> None:
        """Test print_pattern() with string pattern."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        printer.print_pattern("SUCCESS", "Custom pattern message")
        # Verify no exception raised

    def test_print_pattern_with_enum(self) -> None:
        """Test print_pattern() with Pattern enum."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        printer.print_pattern(Pattern.SUCCESS, "Enum pattern message")
        # Verify no exception raised


class TestIndentation:
    """Tests for indentation management."""

    def test_get_indent_returns_string(self) -> None:
        """Test get_indent() returns indentation string."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        indent = printer.get_indent()
        assert isinstance(indent, str)

    def test_add_indent_increases_level(self) -> None:
        """Test add_indent() increases indentation level."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        initial_indent = printer._indent
        printer.add_indent()
        assert printer._indent == initial_indent + 1

    def test_del_indent_decreases_level(self) -> None:
        """Test del_indent() decreases indentation level."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        printer.add_indent()
        initial_indent = printer._indent
        printer.del_indent()
        assert printer._indent == initial_indent - 1

    def test_del_indent_does_not_go_below_zero(self) -> None:
        """Test del_indent() does not go below zero."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        printer.reset_indent()
        printer.del_indent()
        assert printer._indent >= 0

    def test_reset_indent_sets_to_zero(self) -> None:
        """Test reset_indent() sets indentation to zero."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        printer.add_indent()
        printer.add_indent()
        printer.reset_indent()
        assert printer._indent == 0

    def test_manage_indent_context_manager(self) -> None:
        """Test manage_indent() context manager."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        initial_indent = printer._indent

        with ezpl.manage_indent():
            assert printer._indent == initial_indent + 1

        assert printer._indent == initial_indent

    def test_manage_indent_nested(self) -> None:
        """Test nested manage_indent() context managers."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        initial_indent = printer._indent

        with ezpl.manage_indent():
            assert printer._indent == initial_indent + 1
            with ezpl.manage_indent():
                assert printer._indent == initial_indent + 2
            assert printer._indent == initial_indent + 1
        assert printer._indent == initial_indent

    def test_max_indent_limit(self) -> None:
        """Test that indentation is limited to MAX_INDENT."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        printer.reset_indent()

        # Try to add more than MAX_INDENT
        for _ in range(20):
            printer.add_indent()

        # Indentation should be limited to MAX_INDENT (10)
        assert printer._indent <= 10

    def test_indentation_with_messages(self) -> None:
        """Test indentation with actual messages."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        printer.info("Level 0")
        with ezpl.manage_indent():
            printer.info("Level 1")
            with ezpl.manage_indent():
                printer.info("Level 2")
        printer.info("Back to level 0")
        # Verify no exception raised


class TestRichFeatures:
    """Tests for Rich-specific features."""

    def test_print_table_with_dict_list(self) -> None:
        """Test print_table() with list of dictionaries."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        data = [
            {"Name": "Alice", "Age": 30},
            {"Name": "Bob", "Age": 25},
        ]
        printer.print_table(data)
        # Verify no exception raised

    def test_print_table_with_title(self) -> None:
        """Test print_table() with title."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        data = [{"Name": "Alice", "Age": 30}]
        printer.print_table(data, title="Users")
        # Verify no exception raised

    def test_print_panel_basic(self) -> None:
        """Test print_panel() basic usage."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        printer.print_panel("Important message")
        # Verify no exception raised

    def test_print_panel_with_title(self) -> None:
        """Test print_panel() with title."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        printer.print_panel("Important message", title="Alert")
        # Verify no exception raised

    def test_print_panel_with_style(self) -> None:
        """Test print_panel() with custom style."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        printer.print_panel("Important message", title="Alert", style="red")
        # Verify no exception raised

    def test_print_json_with_dict(self) -> None:
        """Test print_json() with dictionary."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        printer.print_json({"key": "value", "number": 42})
        # Verify no exception raised

    def test_print_json_with_list(self) -> None:
        """Test print_json() with list."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        printer.print_json([1, 2, 3, {"nested": "value"}])
        # Verify no exception raised

    def test_print_json_with_string(self) -> None:
        """Test print_json() with JSON string."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        printer.print_json('{"key": "value"}')
        # Verify no exception raised

    def test_print_json_with_title(self) -> None:
        """Test print_json() with title."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        printer.print_json({"key": "value"}, title="Config")
        # Verify no exception raised

    def test_print_json_with_indent(self) -> None:
        """Test print_json() with custom indent."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        printer.print_json({"key": "value"}, indent=4)
        # Verify no exception raised

    def test_wizard_property(self) -> None:
        """Test wizard property returns RichWizard instance."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        wizard = printer.wizard
        assert wizard is not None
        assert hasattr(wizard, "panel")
        assert hasattr(wizard, "table")
        assert hasattr(wizard, "json")


class TestSpecialCharacters:
    """Tests for special character handling."""

    def test_windows_path_with_backslashes(self) -> None:
        """Test printer with Windows path containing backslashes."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        printer.error("Path: C:\\Users\\Test\\file.txt")
        # Verify no exception raised

    def test_message_with_braces_and_tags(self) -> None:
        """Test printer with braces and tags."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        printer.error("Message with {braces} and <tags>")
        # Verify no exception raised

    def test_unicode_characters(self) -> None:
        """Test printer with Unicode characters."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        printer.error("Unicode: éèàçô 漢字 🚀")
        # Verify no exception raised

    def test_ansi_escape_sequences(self) -> None:
        """Test printer with ANSI escape sequences."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        printer.error("ANSI: \x1b[31mRed\x1b[0m")
        # Verify no exception raised


class TestTypeConversion:
    """Tests for automatic type conversion."""

    def test_dict_message(self) -> None:
        """Test printer with dictionary message."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        printer.info({"key": "value"})
        # Verify no exception raised

    def test_int_message(self) -> None:
        """Test printer with integer message."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        printer.info(12345)
        # Verify no exception raised

    def test_list_message(self) -> None:
        """Test printer with list message."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        printer.info(["list", "items"])
        # Verify no exception raised

    def test_exception_object(self) -> None:
        """Test printer with exception object."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        try:
            1 / 0
        except Exception as exc:
            printer.error(exc)
            printer.error(f"Exception: {exc}")
        # Verify no exception raised

    def test_none_message(self) -> None:
        """Test printer with None message."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()
        printer.info(None)
        # Verify no exception raised

    def test_custom_object(self) -> None:
        """Test printer with custom object."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()

        class CustomObject:
            def __str__(self):
                return "CustomObject"

        printer.info(CustomObject())
        # Verify no exception raised
