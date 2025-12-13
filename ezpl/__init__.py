# -*- coding: utf-8 -*-
# ///////////////////////////////////////////////////////////////
# EZPL - Main Package
# Project: ezpl
# ///////////////////////////////////////////////////////////////

"""
Ezpl - Modern Python logging framework.

Ezpl is a modern Python library for advanced log management, using **Rich**
for console output and **loguru** for file logging, with a simple and typed API,
suitable for professional and industrial applications.

**Main Features:**
    - Singleton pattern for global logging instance
    - Rich-based console output with colors and formatting
    - Loguru-based file logging with rotation support
    - Contextual indentation management
    - Pattern-based logging (SUCCESS, ERROR, WARN, TIP, etc.)
    - JSON display support
    - Robust error handling

**Quick Start:**
    >>> from ezpl import Ezpl
    >>> ezpl = Ezpl()
    >>> printer = ezpl.get_printer()
    >>> logger = ezpl.get_logger()
    >>> printer.info("Hello, Ezpl!")
    >>> logger.info("Logged to file")
"""

# IMPORT BASE
# ///////////////////////////////////////////////////////////////
from __future__ import annotations

# IMPORT SPECS
# ///////////////////////////////////////////////////////////////

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from .ezpl import Ezpl
from .handlers import (
    EzPrinter,
    EzLogger,
    ConsolePrinter,
    FileLogger,
    RichWizard,
)
from .handlers.console import ConsolePrinterWrapper
from .config import ConfigurationManager
from .types import (
    LogLevel,
    Pattern,
    PATTERN_COLORS,
    get_pattern_color,
    get_pattern_color_by_name,
)
from .core.exceptions import (
    EzplError,
    ConfigurationError,
    LoggingError,
    ValidationError,
    InitializationError,
    FileOperationError,
    HandlerError,
)

## ==> TYPE ALIASES
# ///////////////////////////////////////////////////////////////

# Type aliases for better IDE support and type checking
# These aliases make it easier to type hint variables in user code

# Re-export ConsolePrinterWrapper as Printer for convenience
Printer = ConsolePrinterWrapper
"""Type alias for ConsolePrinterWrapper.
Use this type hint when you want to indicate that a variable holds a printer instance.

Example:
    >>> from ezpl import Ezpl, Printer
    >>> ezpl = Ezpl()
    >>> printer: Printer = ezpl.get_printer()
    >>> printer.info("Hello!")
    >>> printer.success("Done!")
    >>> printer.print_json({"key": "value"})
"""

# Note: For the logger, users should import Logger directly from loguru
# Example: from loguru import Logger
#          logger: Logger = ezpl.get_logger()

## ==> METADATA
# ///////////////////////////////////////////////////////////////

__version__ = "1.0.0"
__author__ = "Neuraaak"
__maintainer__ = "Neuraaak"
__license__ = "MIT"
__description__ = "A module for easier logging"
__keywords__ = ["logging", "rich", "loguru", "console", "file"]
__url__ = "https://github.com/neuraaak/ezpl"
__repository__ = "https://github.com/neuraaak/ezpl"

## ==> EXPORTS
# ///////////////////////////////////////////////////////////////

__all__ = [
    # Main class
    "Ezpl",
    # Handlers
    "EzPrinter",
    "EzLogger",
    "ConsolePrinter",
    "FileLogger",
    "ConsolePrinterWrapper",
    "RichWizard",
    # Configuration
    "ConfigurationManager",
    # Type aliases
    "Printer",
    # Types
    "LogLevel",
    "Pattern",
    "PATTERN_COLORS",
    "get_pattern_color",
    "get_pattern_color_by_name",
    # Exceptions
    "EzplError",
    "ConfigurationError",
    "LoggingError",
    "ValidationError",
    "InitializationError",
    "FileOperationError",
    "HandlerError",
    # Metadata
    "__version__",
    "__author__",
    "__maintainer__",
    "__license__",
    "__description__",
    "__keywords__",
    "__url__",
    "__repository__",
]
