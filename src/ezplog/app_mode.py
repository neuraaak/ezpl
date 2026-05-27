# ///////////////////////////////////////////////////////////////
# APP_MODE - Stdlib logging bridge for application-level interception
# Project: ezpl
# ///////////////////////////////////////////////////////////////

"""
InterceptHandler: bridge from stdlib logging to loguru.

Install this handler on the root stdlib logger to automatically capture
log records emitted by any library using logging.getLogger(__name__) —
including those using ezpl.lib_mode.get_logger() — and route them through
the loguru pipeline (and thus through EzLogger if configured).

Simplest usage via Ezpl (recommended):

    ezpl = Ezpl(log_file="app.log", hook_logger=True)

Manual installation (for fine-grained control):

    import logging
    from ezpl import InterceptHandler

    logging.basicConfig(handlers=[InterceptHandler()], level=logging.DEBUG, force=True)
"""

from __future__ import annotations

# ///////////////////////////////////////////////////////////////
# IMPORTS
# ///////////////////////////////////////////////////////////////
# Standard library imports
import inspect
import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import types

# Third-party imports
from loguru import logger

# ///////////////////////////////////////////////////////////////
# CLASSES
# ///////////////////////////////////////////////////////////////


class InterceptHandler(logging.Handler):
    """
    Redirect stdlib logging records to loguru.

    This handler bridges the stdlib logging system and loguru, allowing
    libraries that use logging.getLogger(__name__) to have their output
    captured by the loguru pipeline configured by ezpl.

    The caller frame is resolved by walking up the call stack past logging
    internals, so the log records appear with the correct source location
    in loguru output.

    Example:
        >>> import logging
        >>> from ezpl import Ezpl, InterceptHandler
        >>> # Option 1 — automatic via Ezpl
        >>> ezpl = Ezpl(log_file="app.log", hook_logger=True)
        >>> # Option 2 — manual installation
        >>> logging.basicConfig(handlers=[InterceptHandler()], level=0, force=True)
    """

    def emit(self, record: logging.LogRecord) -> None:
        """
        Forward a stdlib LogRecord to loguru.

        Args:
            record: The log record emitted by a stdlib logger.
        """
        # Map stdlib level name to a loguru level; fall back to numeric level
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = str(record.levelno)

        # Walk up the call stack to find the actual caller — skip both
        # `emit` itself and all stdlib `logging` machinery (handlers, Logger._log,
        # callHandlers, etc.). This is loguru's canonical InterceptHandler recipe:
        # start at the current frame (depth=0) and keep walking while we're
        # either still in `emit` or inside the stdlib logging module.
        frame: types.FrameType | None = inspect.currentframe()
        depth = 0
        while frame is not None and (
            depth == 0 or frame.f_code.co_filename == logging.__file__
        ):
            frame = frame.f_back
            depth += 1

        # Bind task="logger" so records pass EzLogger's file sink filter.
        # NOTE: brace escaping (`{` -> `{{`) is handled centrally by EzLogger's
        # custom formatter, which is the single source of truth for all entry
        # paths (intercept, direct calls, third-party binds). Do not escape
        # here or braces would be doubled in the final output.
        logger.bind(task="logger").opt(
            depth=depth,
            exception=record.exc_info,
        ).log(level, record.getMessage())


# ///////////////////////////////////////////////////////////////
# PUBLIC API
# ///////////////////////////////////////////////////////////////

__all__ = [
    "InterceptHandler",
]
