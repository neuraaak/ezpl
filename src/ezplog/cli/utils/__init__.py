# ///////////////////////////////////////////////////////////////
# EZPL - CLI Utils Module
# Project: ezpl
# ///////////////////////////////////////////////////////////////

"""
CLI utilities module for Ezpl logging framework.

This module contains utility functions and classes for CLI operations:
- Log parsing and analysis
- Statistics calculation
- User environment variable management
"""

from __future__ import annotations

# ///////////////////////////////////////////////////////////////
# IMPORTS
# ///////////////////////////////////////////////////////////////
# Local imports
from ._env_manager import UserEnvManager
from ._log_parser import LogEntry, LogParser
from ._log_stats import LogStatistics

# ///////////////////////////////////////////////////////////////
# PUBLIC API
# ///////////////////////////////////////////////////////////////

__all__ = [
    # Log utilities exports
    "LogParser",
    "LogEntry",
    "LogStatistics",
    # Environment utilities exports
    "UserEnvManager",
]
