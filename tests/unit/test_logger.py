# -*- coding: utf-8 -*-
# ///////////////////////////////////////////////////////////////
# EZPL - Tests unitaires FileLogger
# Project: ezpl
# ///////////////////////////////////////////////////////////////

from pathlib import Path
from ezpl import Ezpl
from time import time
from unittest.mock import patch


def wait_for_file(path, timeout=2.0) -> None:
    import time

    start = time.time()
    while not path.exists():
        if time.time() - start > timeout:
            raise FileNotFoundError(f"Timeout waiting for file: {path}")
        time.sleep(0.05)


def test_add_separator(tmp_path) -> None:
    Ezpl.reset()
    log_file = tmp_path / "test.log"
    log_file.parent.mkdir(parents=True, exist_ok=True)
    ezpl = Ezpl(log_file=log_file)
    ezpl.add_separator()
    # Écrire une ligne de log pour forcer la création du fichier
    ezpl.get_logger().info("force file creation")
    wait_for_file(log_file)
    content = log_file.read_text(encoding="utf-8")
    assert "==>" in content


def test_logger_with_strange_characters(tmp_path) -> None:
    import time

    Ezpl.reset()
    log_file = tmp_path / "strange.log"
    log_file.parent.mkdir(parents=True, exist_ok=True)
    ezpl = Ezpl(log_file=log_file)
    ezpl.add_separator()
    logger = ezpl.get_logger()
    # Écrire une ligne de log pour forcer la création du fichier
    logger.info("force file creation")
    strange_message = "Test spécial: éèàçô 漢字 🚀 \x00\x1b[31m"
    logger.info(strange_message)
    import time

    time.sleep(0.2)
    assert log_file.exists(), f"Fichier non créé: {log_file}"
    content = log_file.read_text(encoding="utf-8")
    assert "Test spécial" in content
    assert "漢字" in content
    assert "🚀" in content


def test_logger_with_exception_argument(tmp_path) -> None:
    import time as _time
    from unittest.mock import patch

    Ezpl.reset()
    log_file = tmp_path / "exception.log"
    ezpl = Ezpl(log_file=log_file)
    logger = ezpl.get_logger()
    try:
        {}[0]
    except Exception as exc:
        logger.error(exc)
        logger.error(f"Exception: {exc}")
    # Mock time.sleep pour accélérer le test
    with patch("time.sleep", return_value=None):
        _time.sleep(0.01)
    assert log_file.exists(), f"Fichier non créé: {log_file}"
    content = log_file.read_text(encoding="utf-8")
    assert "Exception" in content


def test_logger_handles_file_write_error(tmp_path) -> None:
    Ezpl.reset()
    log_file = tmp_path / "test.log"
    ezpl = Ezpl(log_file=log_file)

    with patch("builtins.open", side_effect=OSError("Write error")):
        logger = ezpl.get_logger()
        try:
            logger.info("Test message")
        except OSError as e:
            assert str(e) == "Write error"


def test_logger_with_mocked_sleep(tmp_path) -> None:
    from unittest.mock import patch

    Ezpl.reset()
    log_file = tmp_path / "mocked_sleep.log"
    ezpl = Ezpl(log_file=log_file)

    with patch("time.sleep", return_value=None):
        ezpl.get_logger().info("Test message with mocked sleep")
        assert log_file.exists()


def test_logger_file_rotation(tmp_path) -> None:
    """Test file rotation feature."""
    Ezpl.reset()
    log_file = tmp_path / "rotation.log"
    
    from ezpl.handlers import FileLogger
    logger_handler = FileLogger(
        log_file,
        level="INFO",
        rotation="1 KB",  # Rotation à 1 KB pour test
        retention="1 day",
        compression="zip"
    )
    
    logger = logger_handler.get_logger()
    # Écrire assez de données pour déclencher la rotation
    for i in range(100):
        logger.info(f"Test message {i} " * 10)  # Messages assez longs
    
    # Vérifier que le fichier existe
    assert log_file.exists() or any(log_file.parent.glob("rotation.log.*"))


def test_logger_get_file_size(tmp_path) -> None:
    """Test get_file_size method."""
    Ezpl.reset()
    log_file = tmp_path / "size_test.log"
    
    from ezpl.handlers import FileLogger
    logger_handler = FileLogger(log_file, level="INFO")
    logger = logger_handler.get_logger()
    
    # Écrire quelques messages
    logger.info("Test message 1")
    logger.info("Test message 2")
    
    # Vérifier que get_file_size retourne une valeur > 0
    size = logger_handler.get_file_size()
    assert size > 0
