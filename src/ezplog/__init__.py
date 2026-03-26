# ///////////////////////////////////////////////////////////////
# EZPL - Main Module
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

**Two usage modes:**

*App mode* — configure once at application level:

    >>> from ezplog import Ezpl
    >>> ezpl = Ezpl(log_file="app.log", intercept_stdlib=True, lock_config=True)
    >>> ezpl.info("Application started")           # direct facade
    >>> ezpl.get_printer().success("Ready")        # advanced usage

*Lib mode* — passive proxies for library authors:

    >>> from ezplog.lib_mode import get_logger, get_printer
    >>> log = get_logger(__name__)
    >>> printer = get_printer()
    >>> log.info("Library initialized")            # silent without host config
    >>> printer.success("Library initialized")     # silent without host config
"""

from __future__ import annotations

# ///////////////////////////////////////////////////////////////
# IMPORTS
# ///////////////////////////////////////////////////////////////
# Standard library imports
import sys

# Local imports
from .app_mode import InterceptHandler
from .config import ConfigurationManager
from .core.exceptions import (
    ConfigurationError,
    EzplError,
    FileOperationError,
    HandlerError,
    InitializationError,
    LoggingError,
    ValidationError,
)
from .ezpl import Ezpl
from .handlers import EzLogger, EzPrinter, RichWizard
from .handlers.wizard.dynamic import DynamicLayeredProgress, StageConfig
from .lib_mode import get_logger, get_printer
from .types import (
    PATTERN_COLORS,
    LoggerProtocol,
    LogLevel,
    Pattern,
    PrinterProtocol,
    get_pattern_color,
    get_pattern_color_by_name,
)
from .version import __version__

# ///////////////////////////////////////////////////////////////
# META INFORMATIONS
# ///////////////////////////////////////////////////////////////

__author__ = "Neuraaak"
__maintainer__ = "Neuraaak"
__description__ = "A module for easier logging"
__python_requires__ = ">=3.11"
__keywords__ = ["logging", "rich", "loguru", "console", "file"]
__url__ = "https://github.com/neuraaak/ezplog"
__repository__ = "https://github.com/neuraaak/ezplog"

# ///////////////////////////////////////////////////////////////
# PYTHON VERSION CHECK
# ///////////////////////////////////////////////////////////////

if sys.version_info < (3, 11):  # noqa: UP036
    raise RuntimeError(
        f"Ezpl {__version__} requires Python 3.11 or higher. "
        f"Current version: {sys.version}"
    )

# ///////////////////////////////////////////////////////////////
# TYPE ALIASES
# ///////////////////////////////////////////////////////////////

Printer = EzPrinter
"""Type alias for EzPrinter (console printer handler).
Use this type when you want to annotate a variable that represents a printer.

Example:
    >>> from ezplog import Ezpl, Printer
    >>> ezpl = Ezpl()
    >>> printer: Printer = ezpl.get_printer()
    >>> printer.info("Hello!")
    >>> printer.success("Done!")
    >>> printer.print_json({"key": "value"})
"""

Logger = EzLogger
"""Type alias for EzLogger (file logger handler).
Use this type when you want to annotate a variable that represents a logger.

Example:
    >>> from ezplog import Ezpl, Logger
    >>> ezpl = Ezpl()
    >>> logger: Logger = ezpl.get_logger()
    >>> logger.info("Logged to file")
"""

# ///////////////////////////////////////////////////////////////
# PUBLIC API
# ///////////////////////////////////////////////////////////////

__all__ = [
    # Main class exports
    "Ezpl",
    # App mode — stdlib interception
    "InterceptHandler",
    # Lib mode — passive proxies for library authors
    "get_logger",
    "get_printer",
    # Handler class exports
    "EzPrinter",
    "EzLogger",
    "RichWizard",
    "DynamicLayeredProgress",
    "StageConfig",
    # Configuration exports
    "ConfigurationManager",
    # Type aliases exports
    "Printer",
    "Logger",
    # Type & pattern exports
    "LogLevel",
    "Pattern",
    "PATTERN_COLORS",
    "get_pattern_color",
    "get_pattern_color_by_name",
    # Protocol exports
    "PrinterProtocol",
    "LoggerProtocol",
    # Exception exports
    "EzplError",
    "ConfigurationError",
    "LoggingError",
    "ValidationError",
    "InitializationError",
    "FileOperationError",
    "HandlerError",
]
