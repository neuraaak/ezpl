# -*- coding: utf-8 -*-
# ///////////////////////////////////////////////////////////////
# EZPL - Tests unitaires Printer
# Project: ezpl
# ///////////////////////////////////////////////////////////////

from ezpl import Ezpl
from unittest.mock import patch


def test_manage_indent_changes_indent() -> None:
    Ezpl.reset()
    ezpl = Ezpl()
    printer = ezpl.get_printer()
    with ezpl.manage_indent():
        printer.info("Indented message")
    # No assert: just check no exception


def test_printer_with_special_characters() -> None:
    """Test printer with special characters (Rich should handle them better)."""
    Ezpl.reset()
    ezpl = Ezpl()
    printer = ezpl.get_printer()
    
    # Test avec caractères spéciaux qui causaient des problèmes avant
    printer.error("Path: C:\\Users\\Test\\file.txt")
    printer.error("Message with {braces} and <tags>")
    printer.error("Unicode: éèàçô 漢字 🚀")
    # Pas d'assert : juste vérifier qu'aucune exception n'est levée


def test_printer_with_exception_argument() -> None:
    """Test printer with exception objects."""
    Ezpl.reset()
    ezpl = Ezpl()
    printer = ezpl.get_printer()
    try:
        1 / 0
    except Exception as exc:
        # On passe l'exception directement au printer (devrait convertir en string)
        printer.error(exc)
        printer.error(f"Exception: {exc}")


def test_printer_with_non_string_messages() -> None:
    """Test printer with non-string messages (should auto-convert)."""
    Ezpl.reset()
    ezpl = Ezpl()
    printer = ezpl.get_printer()
    
    # Test avec différents types
    printer.info({"key": "value"})  # Dict
    printer.info(12345)  # Int
    printer.info(["list", "items"])  # List
    # Pas d'assert : juste vérifier qu'aucune exception n'est levée


def test_printer_all_levels() -> None:
    """Test all printer log levels."""
    Ezpl.reset()
    ezpl = Ezpl()
    printer = ezpl.get_printer()
    
    printer.debug("Debug message")
    printer.info("Info message")
    printer.success("Success message")
    printer.warning("Warning message")
    printer.error("Error message")
    printer.critical("Critical message")
    # Pas d'assert : juste vérifier qu'aucune exception n'est levée


def test_printer_indentation() -> None:
    """Test printer indentation."""
    Ezpl.reset()
    ezpl = Ezpl()
    printer = ezpl.get_printer()
    
    printer.info("Level 0")
    with ezpl.manage_indent():
        printer.info("Level 1")
        with ezpl.manage_indent():
            printer.info("Level 2")
    printer.info("Back to level 0")
    # Pas d'assert : juste vérifier qu'aucune exception n'est levée


def test_printer_max_indent() -> None:
    """Test that indentation is limited to MAX_INDENT."""
    Ezpl.reset()
    ezpl = Ezpl()
    printer = ezpl.get_printer()
    
    # Essayer d'ajouter beaucoup d'indentation
    for _ in range(20):
        printer.add_indent()
    
    # L'indentation devrait être limitée à MAX_INDENT (10)
    indent = printer.get_indent()
    # Vérifier que l'indentation ne dépasse pas MAX_INDENT
    assert printer._indent <= 10


def test_printer_rich_features() -> None:
    """Test Rich-specific features."""
    Ezpl.reset()
    ezpl = Ezpl()
    printer = ezpl.get_printer()
    
    # Test print_table
    printer.print_table([
        {"Name": "Alice", "Age": 30},
        {"Name": "Bob", "Age": 25}
    ])
    
    # Test print_panel
    printer.print_panel("Important message", title="Alert")
    
    # Pas d'assert : juste vérifier qu'aucune exception n'est levée
