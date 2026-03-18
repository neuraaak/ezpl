# ///////////////////////////////////////////////////////////////
# EZPL - Compatibility Shim
# Re-exports the public API from ezplog for backward compatibility.
# ///////////////////////////////////////////////////////////////

"""
Compatibility shim — re-exports the public API from ezplog.

This package exists for backward compatibility with projects that import
``from ezpl import ...`` or ``import ezpl``. New projects should import
from ``ezplog`` directly.

    >>> from ezpl import Ezpl       # legacy — still works
    >>> from ezplog import Ezpl     # preferred
"""

from __future__ import annotations

from ezplog import (
    PATTERN_COLORS,
    ConfigurationError,
    ConfigurationManager,
    EzLogger,
    Ezpl,
    EzplError,
    EzPrinter,
    FileOperationError,
    HandlerError,
    InitializationError,
    InterceptHandler,
    Logger,
    LoggerProtocol,
    LoggingError,
    LogLevel,
    Pattern,
    Printer,
    PrinterProtocol,
    RichWizard,
    ValidationError,
    get_logger,
    get_pattern_color,
    get_pattern_color_by_name,
    get_printer,
)

__all__ = [
    # Main class
    "Ezpl",
    # App mode
    "InterceptHandler",
    # Lib mode
    "get_logger",
    "get_printer",
    # Handlers
    "EzPrinter",
    "EzLogger",
    "RichWizard",
    # Configuration
    "ConfigurationManager",
    # Type aliases
    "Printer",
    "Logger",
    # Types & patterns
    "LogLevel",
    "Pattern",
    "PATTERN_COLORS",
    "get_pattern_color",
    "get_pattern_color_by_name",
    # Protocols
    "PrinterProtocol",
    "LoggerProtocol",
    # Exceptions
    "EzplError",
    "ConfigurationError",
    "LoggingError",
    "ValidationError",
    "InitializationError",
    "FileOperationError",
    "HandlerError",
]
