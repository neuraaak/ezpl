# -*- coding: utf-8 -*-
# ///////////////////////////////////////////////////////////////
# EZPL - Types module
# Project: ezpl
# ///////////////////////////////////////////////////////////////

"""
Types module for Ezpl logging framework.

This module contains type definitions and enumerations.
"""

from .log_level import LogLevel
from .patterns import (
    Pattern,
    PATTERN_COLORS,
    get_pattern_color,
    get_pattern_color_by_name,
)

__all__ = [
    "LogLevel",
    "Pattern",
    "PATTERN_COLORS",
    "get_pattern_color",
    "get_pattern_color_by_name",
]
