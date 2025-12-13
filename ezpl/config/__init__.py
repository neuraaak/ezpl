# -*- coding: utf-8 -*-
# ///////////////////////////////////////////////////////////////
# EZPL - Configuration module
# Project: ezpl
# ///////////////////////////////////////////////////////////////

"""
Configuration module for Ezpl logging framework.

This module handles all configuration management.
"""

from .defaults import DefaultConfiguration
from .manager import ConfigurationManager

__all__ = ["ConfigurationManager", "DefaultConfiguration"]
