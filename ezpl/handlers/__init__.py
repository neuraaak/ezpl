# -*- coding: utf-8 -*-
# ///////////////////////////////////////////////////////////////
# EZPL - Handlers module
# Project: ezpl
# ///////////////////////////////////////////////////////////////

"""
Handlers module for Ezpl logging framework.

This module contains concrete implementations of logging handlers.
"""

from .console import ConsolePrinter, ConsolePrinterWrapper
from .file import FileLogger
from .wizard import RichWizard

# Alias pour rétrocompatibilité
EzPrinter = ConsolePrinter
EzLogger = FileLogger

__all__ = [
    "ConsolePrinter",
    "ConsolePrinterWrapper",
    "FileLogger",
    "RichWizard",
    "EzPrinter",  # Alias pour compatibilité
    "EzLogger",  # Alias pour compatibilité
]
