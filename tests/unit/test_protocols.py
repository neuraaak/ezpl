# ///////////////////////////////////////////////////////////////
# EZPL - Tests unitaires Protocols
# Project: ezpl
# ///////////////////////////////////////////////////////////////

"""
Unit tests for Protocol type checking.

Tests cover:
- PrinterProtocol conformance
- LoggerProtocol conformance
- Runtime validation with isinstance()
- Type annotations
- Protocol method signatures
"""

from __future__ import annotations

# ///////////////////////////////////////////////////////////////
# IMPORTS
# ///////////////////////////////////////////////////////////////
# Local imports
from ezpl import Ezpl
from ezpl.types.protocols import LoggerProtocol, PrinterProtocol

# ///////////////////////////////////////////////////////////////
# TESTS
# ///////////////////////////////////////////////////////////////


class TestPrinterProtocol:
    """Tests for PrinterProtocol conformance."""

    def test_printer_implements_protocol(self) -> None:
        """Test that get_printer() returns a PrinterProtocol-conforming object."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()

        # Runtime check
        assert isinstance(printer, PrinterProtocol)

    def test_printer_has_core_methods(self) -> None:
        """Test that printer has all core logging methods."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()

        # Check method existence
        assert hasattr(printer, "info")
        assert hasattr(printer, "debug")
        assert hasattr(printer, "success")
        assert hasattr(printer, "warning")
        assert hasattr(printer, "error")
        assert hasattr(printer, "critical")

        # Check they are callable
        assert callable(printer.info)
        assert callable(printer.debug)
        assert callable(printer.success)

    def test_printer_has_pattern_methods(self) -> None:
        """Test that printer has all pattern methods."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()

        assert hasattr(printer, "tip")
        assert hasattr(printer, "system")
        assert hasattr(printer, "install")
        assert hasattr(printer, "detect")
        assert hasattr(printer, "config")
        assert hasattr(printer, "deps")

    def test_printer_has_indentation_methods(self) -> None:
        """Test that printer has indentation management methods."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()

        assert hasattr(printer, "add_indent")
        assert hasattr(printer, "del_indent")
        assert hasattr(printer, "reset_indent")
        assert hasattr(printer, "manage_indent")

    def test_printer_has_wizard_property(self) -> None:
        """Test that printer has wizard property."""
        ezpl = Ezpl()
        printer = ezpl.get_printer()

        assert hasattr(printer, "wizard")
        wizard = printer.wizard
        assert wizard is not None


class TestLoggerProtocol:
    """Tests for LoggerProtocol conformance."""

    def test_logger_implements_protocol(self) -> None:
        """Test that get_logger() returns a LoggerProtocol-conforming object."""
        ezpl = Ezpl()
        logger = ezpl.get_logger()

        # Runtime check
        assert isinstance(logger, LoggerProtocol)

    def test_logger_has_core_methods(self) -> None:
        """Test that logger has all core logging methods."""
        ezpl = Ezpl()
        logger = ezpl.get_logger()

        # Check method existence
        assert hasattr(logger, "trace")
        assert hasattr(logger, "debug")
        assert hasattr(logger, "info")
        assert hasattr(logger, "success")
        assert hasattr(logger, "warning")
        assert hasattr(logger, "error")
        assert hasattr(logger, "critical")
        assert hasattr(logger, "exception")

        # Check they are callable
        assert callable(logger.info)
        assert callable(logger.debug)
        assert callable(logger.error)

    def test_logger_has_loguru_methods(self) -> None:
        """Test that logger has loguru-specific methods."""
        ezpl = Ezpl()
        logger = ezpl.get_logger()

        assert hasattr(logger, "bind")
        assert hasattr(logger, "opt")
        assert hasattr(logger, "patch")

    def test_logger_has_ezpl_methods(self) -> None:
        """Test that logger has Ezpl-specific methods."""
        ezpl = Ezpl()
        logger = ezpl.get_logger()

        assert hasattr(logger, "set_level")
        assert hasattr(logger, "log")
        assert hasattr(logger, "add_separator")
        assert hasattr(logger, "get_log_file")
        assert hasattr(logger, "close")

    def test_logger_methods_work(self) -> None:
        """Test that logger methods actually work."""
        ezpl = Ezpl()
        logger = ezpl.get_logger()

        # These should not raise exceptions
        logger.info("Test info")
        logger.debug("Test debug")
        logger.success("Test success")
        logger.error("Test error")


class TestProtocolTypeAnnotations:
    """Tests for type annotations with protocols."""

    def test_function_with_printer_protocol_annotation(self) -> None:
        """Test function accepting PrinterProtocol."""

        def process(printer: PrinterProtocol) -> None:
            printer.info("Processing")
            printer.success("Done")

        ezpl = Ezpl()
        # Should work without type errors
        process(ezpl.get_printer())

    def test_function_with_logger_protocol_annotation(self) -> None:
        """Test function accepting LoggerProtocol."""

        def log_process(logger: LoggerProtocol) -> None:
            logger.info("Starting")
            logger.success("Completed")

        ezpl = Ezpl()
        # Should work without type errors
        log_process(ezpl.get_logger())

    def test_both_protocols_together(self) -> None:
        """Test function accepting both protocols."""

        def dual_log(printer: PrinterProtocol, logger: LoggerProtocol) -> None:
            printer.info("Console message")
            logger.info("File message")

        ezpl = Ezpl()
        dual_log(ezpl.get_printer(), ezpl.get_logger())


class TestProtocolInheritance:
    """Tests for protocol inheritance and extension."""

    def test_printer_protocol_extensible(self) -> None:
        """Test that protocols can be used for custom implementations."""
        # This test verifies that the protocol is properly defined
        # and can be used to validate custom implementations

        ezpl = Ezpl()
        printer = ezpl.get_printer()

        # Should conform to protocol
        assert isinstance(printer, PrinterProtocol)

        # Should have all required methods
        required_methods = [
            "info",
            "debug",
            "success",
            "warning",
            "error",
            "critical",
            "tip",
            "system",
            "install",
            "detect",
            "config",
            "deps",
            "print_pattern",
            "print_json",
            "add_indent",
            "del_indent",
            "reset_indent",
            "manage_indent",
        ]

        for method in required_methods:
            assert hasattr(printer, method), f"Missing method: {method}"
            assert callable(getattr(printer, method)), f"Method not callable: {method}"

    def test_logger_protocol_extensible(self) -> None:
        """Test that LoggerProtocol can validate custom implementations."""
        ezpl = Ezpl()
        logger = ezpl.get_logger()

        # Should conform to protocol
        assert isinstance(logger, LoggerProtocol)

        # Should have all required methods
        required_methods = [
            "trace",
            "debug",
            "info",
            "success",
            "warning",
            "error",
            "critical",
            "exception",
            "bind",
            "opt",
            "patch",
            "set_level",
            "log",
            "add_separator",
            "get_log_file",
            "close",
        ]

        for method in required_methods:
            assert hasattr(logger, method), f"Missing method: {method}"
            assert callable(getattr(logger, method)), f"Method not callable: {method}"
