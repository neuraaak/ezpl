# -*- coding: utf-8 -*-
# ///////////////////////////////////////////////////////////////

# -*- coding: utf-8 -*-
# ///////////////////////////////////////////////////////////////
# EZPL - Utils module
# Project: ezpl
# ///////////////////////////////////////////////////////////////

"""
Utils module for Ezpl logging framework.

This module provides compatibility imports for the handlers module.
"""

# Imports de compatibilité - les classes ont été déplacées vers handlers
from ..handlers import ConsolePrinter as EzPrinter
from ..handlers import FileLogger as EzLogger

__all__ = ["EzPrinter", "EzLogger"]
