# ///////////////////////////////////////////////////////////////
# EZPL - CLI Commands Module
# Project: ezpl
# ///////////////////////////////////////////////////////////////

"""
CLI Commands module for Ezpl logging framework.

This module contains all CLI command implementations.
"""

from __future__ import annotations

# ///////////////////////////////////////////////////////////////
# IMPORTS
# ///////////////////////////////////////////////////////////////
# Local imports
from ._config import config_group
from ._docs import docs_command
from ._info import info_command
from ._logs import logs_group
from ._version import version_command

# ///////////////////////////////////////////////////////////////
# PUBLIC API
# ///////////////////////////////////////////////////////////////

__all__ = [
    # CLI command groups
    "logs_group",
    "config_group",
    "version_command",
    "info_command",
    "docs_command",
]
