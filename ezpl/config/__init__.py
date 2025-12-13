# -*- coding: utf-8 -*-
# ///////////////////////////////////////////////////////////////
# EZPL - Configuration module
# Project: ezpl
# ///////////////////////////////////////////////////////////////

"""
Configuration module for Ezpl logging framework.

This module handles all configuration management.
"""

from .manager import ConfigurationManager
from .defaults import DefaultConfiguration

__all__ = ["ConfigurationManager", "DefaultConfiguration"]
