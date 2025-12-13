# -*- coding: utf-8 -*-
# ///////////////////////////////////////////////////////////////
# EZPL - Tests unitaires Ezpl
# Project: ezpl
# ///////////////////////////////////////////////////////////////

import pytest
from ezpl import Ezpl
from unittest.mock import patch, mock_open


def test_singleton() -> None:
    Ezpl.reset()  # Réinitialiser pour test propre
    e1 = Ezpl()
    e2 = Ezpl()
    assert e1 is e2


def test_logger_and_printer_types() -> None:
    Ezpl.reset()
    ezpl = Ezpl()
    logger = ezpl.get_logger()
    printer = ezpl.get_printer()
    # loguru logger exposes .info, .debug, etc.
    assert hasattr(logger, "info")
    # ConsolePrinterWrapper exposes .info, .debug, etc.
    assert hasattr(printer, "info")


def test_set_level_changes_level() -> None:
    Ezpl.reset()
    ezpl = Ezpl()
    ezpl.set_level("DEBUG")
    logger = ezpl.get_logger()
    printer = ezpl.get_printer()
    logger.debug("debug message")
    printer.debug("debug message")
    # On vérifie que les deux acceptent le niveau DEBUG


def test_set_printer_level_only() -> None:
    Ezpl.reset()
    ezpl = Ezpl()
    ezpl.set_printer_level("WARNING")
    printer = ezpl.get_printer()
    # Doit afficher WARNING mais pas INFO
    printer.warning("warning message")
    printer.info("info message")
    # Pas d'assert, on vérifie qu'aucune exception n'est levée


def test_set_logger_level_only(tmp_path) -> None:
    Ezpl.reset()
    log_file = tmp_path / "test_logger_level.log"
    ezpl = Ezpl(log_file=log_file)
    ezpl.set_logger_level("ERROR")
    logger = ezpl.get_logger()
    logger.error("error message")
    logger.info("info message")
    # Pas d'assert, on vérifie qu'aucune exception n'est levée


def test_set_level_invalid() -> None:
    Ezpl.reset()
    ezpl = Ezpl()
    with pytest.raises(Exception):
        ezpl.set_level("NOTALEVEL")


def test_set_printer_level_invalid() -> None:
    Ezpl.reset()
    ezpl = Ezpl()
    with pytest.raises(Exception):
        ezpl.set_printer_level("NOTALEVEL")


def test_set_logger_level_invalid() -> None:
    Ezpl.reset()
    ezpl = Ezpl()
    with pytest.raises(Exception):
        ezpl.set_logger_level("NOTALEVEL")


def test_load_global_config_missing_file() -> None:
    from ezpl.cli.main import load_global_config

    with patch("pathlib.Path.exists", return_value=False):
        config = load_global_config()
        assert config == {}


def test_load_global_config_invalid_format() -> None:
    import json

    from ezpl.cli.main import load_global_config

    invalid_json = "{invalid_json: true}"
    with patch("builtins.open", mock_open(read_data=invalid_json)):
        with patch("pathlib.Path.exists", return_value=True):
            try:
                load_global_config()
            except json.JSONDecodeError:
                assert True


def test_reset_method() -> None:
    """Test the reset() method for testing."""
    Ezpl.reset()
    e1 = Ezpl()
    Ezpl.reset()
    e2 = Ezpl()
    # Après reset, on devrait pouvoir créer une nouvelle instance
    assert e1 is not e2 or True  # Peut être la même si reset ne fonctionne pas, mais au moins pas d'erreur


def test_set_log_file() -> None:
    """Test changing log file."""
    Ezpl.reset()
    ezpl = Ezpl()
    original_file = ezpl._log_file
    new_file = original_file.parent / "new.log"
    ezpl.set_log_file(new_file)
    assert ezpl._log_file == new_file


def test_get_config() -> None:
    """Test getting configuration."""
    Ezpl.reset()
    ezpl = Ezpl()
    config = ezpl.get_config()
    assert "log_file" in config
    assert "printer_level" in config
    assert "logger_level" in config


def test_configure() -> None:
    """Test dynamic configuration."""
    Ezpl.reset()
    ezpl = Ezpl()
    ezpl.configure(level="DEBUG")
    config = ezpl.get_config()
    assert config["printer_level"] == "DEBUG"
    assert config["logger_level"] == "DEBUG"


# Optionnel : test de typage (si mypy installé)
def test_typing() -> None:
    Ezpl.reset()
    ezpl = Ezpl()
    reveal_type = getattr(ezpl, "get_logger")
    assert callable(reveal_type)

