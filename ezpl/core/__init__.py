# -*- coding: utf-8 -*-
# ///////////////////////////////////////////////////////////////
# EZPL - Core module
# Project: ezpl
# ///////////////////////////////////////////////////////////////

"""
Core module for Ezpl logging framework.

This module contains the core business logic and interfaces.
"""

from .exceptions import (
    ConfigurationError,
    EzplError,
    FileOperationError,
    HandlerError,
    InitializationError,
    LoggingError,
    ValidationError,
)
from .interfaces import (
    ConfigurationManager,
    EzplCore,
    IndentationManager,
    LoggingHandler,
)

__all__ = [
    # Interfaces
    "LoggingHandler",
    "IndentationManager",
    "ConfigurationManager",
    "EzplCore",
    # Exceptions
    "EzplError",
    "ConfigurationError",
    "LoggingError",
    "ValidationError",
    "InitializationError",
    "FileOperationError",
    "HandlerError",
]
