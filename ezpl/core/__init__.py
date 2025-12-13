# -*- coding: utf-8 -*-
# ///////////////////////////////////////////////////////////////
# EZPL - Core module
# Project: ezpl
# ///////////////////////////////////////////////////////////////

"""
Core module for Ezpl logging framework.

This module contains the core business logic and interfaces.
"""

from .interfaces import (
    LoggingHandler, 
    IndentationManager, 
    ConfigurationManager,
    EzplCore
)
from .exceptions import (
    EzplError,
    ConfigurationError,
    LoggingError,
    ValidationError,
    InitializationError,
    FileOperationError,
    HandlerError
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
    "HandlerError"
]
