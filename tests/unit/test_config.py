# -*- coding: utf-8 -*-
# ///////////////////////////////////////////////////////////////
# EZPL - Tests unitaires ConfigurationManager
# Project: ezpl
# ///////////////////////////////////////////////////////////////

"""
Unit tests for ConfigurationManager.

Tests cover:
- Initialization
- Get/Set/Update operations
- Save/Load operations
- Priority order (env > file > default)
- Getters for specific values
- Reset to defaults
- Export to script
- Error handling
"""

import json
import os
from pathlib import Path
from unittest.mock import patch

# IMPORT BASE
# ///////////////////////////////////////////////////////////////
import pytest

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from ezpl.config import ConfigurationManager
from ezpl.core.exceptions import FileOperationError

# IMPORT SPECS
# ///////////////////////////////////////////////////////////////


## ==> TESTS
# ///////////////////////////////////////////////////////////////


class TestInitialization:
    """Tests for ConfigurationManager initialization."""

    def test_init_with_default_config_file(self) -> None:
        """Test initialization with default config file."""
        config = ConfigurationManager()
        assert config._config_file is not None

    def test_init_with_custom_config_file(self, temp_config_file: Path) -> None:
        """Test initialization with custom config file."""
        config = ConfigurationManager(config_file=temp_config_file)
        assert config._config_file == temp_config_file

    def test_init_loads_defaults(self, temp_config_file: Path) -> None:
        """Test that initialization loads default values."""
        config = ConfigurationManager(config_file=temp_config_file)
        all_config = config.get_all()
        assert len(all_config) > 0
        # Verify some default keys exist
        assert "log-level" in all_config or "printer-level" in all_config

    def test_init_loads_from_file(self, temp_config_file: Path) -> None:
        """Test that initialization loads from config file."""
        config_data = {"log-level": "DEBUG", "printer-level": "WARNING"}
        temp_config_file.parent.mkdir(parents=True, exist_ok=True)
        temp_config_file.write_text(json.dumps(config_data), encoding="utf-8")

        config = ConfigurationManager(config_file=temp_config_file)
        assert config.get("log-level") == "DEBUG"
        assert config.get("printer-level") == "WARNING"

    def test_init_loads_from_env(self, temp_config_file: Path, clean_env: None) -> None:
        """Test that initialization loads from environment variables."""
        os.environ["EZPL_LOG_LEVEL"] = "ERROR"
        os.environ["EZPL_PRINTER_LEVEL"] = "DEBUG"

        config = ConfigurationManager(config_file=temp_config_file)
        # Environment should override defaults
        assert config.get("log-level") == "ERROR"
        assert config.get("printer-level") == "DEBUG"

    def test_init_handles_invalid_json(self, temp_config_file: Path) -> None:
        """Test that initialization handles invalid JSON gracefully."""
        temp_config_file.parent.mkdir(parents=True, exist_ok=True)
        temp_config_file.write_text("{invalid json}", encoding="utf-8")

        # Should not raise error, should use defaults
        config = ConfigurationManager(config_file=temp_config_file)
        assert config is not None


class TestGetSetUpdate:
    """Tests for get, set, and update operations."""

    def test_get_existing_key(self, config_manager: ConfigurationManager) -> None:
        """Test get() with existing key."""
        config_manager.set("test-key", "test-value")
        assert config_manager.get("test-key") == "test-value"

    def test_get_non_existing_key(self, config_manager: ConfigurationManager) -> None:
        """Test get() with non-existing key."""
        assert config_manager.get("non-existing-key") is None
        assert config_manager.get("non-existing-key", "default") == "default"

    def test_set_key_value(self, config_manager: ConfigurationManager) -> None:
        """Test set() method."""
        config_manager.set("test-key", "test-value")
        assert config_manager.get("test-key") == "test-value"

    def test_update_multiple_keys(self, config_manager: ConfigurationManager) -> None:
        """Test update() with multiple keys."""
        config_manager.update({"key1": "value1", "key2": "value2"})
        assert config_manager.get("key1") == "value1"
        assert config_manager.get("key2") == "value2"

    def test_get_all(self, config_manager: ConfigurationManager) -> None:
        """Test get_all() method."""
        config_manager.set("test-key", "test-value")
        all_config = config_manager.get_all()
        assert isinstance(all_config, dict)
        assert "test-key" in all_config


class TestGetters:
    """Tests for specific getter methods."""

    def test_get_log_level(self, config_manager: ConfigurationManager) -> None:
        """Test get_log_level() method."""
        level = config_manager.get_log_level()
        assert isinstance(level, str)
        assert level in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

    def test_get_log_file(self, config_manager: ConfigurationManager) -> None:
        """Test get_log_file() method."""
        log_file = config_manager.get_log_file()
        assert isinstance(log_file, Path)

    def test_get_printer_level(self, config_manager: ConfigurationManager) -> None:
        """Test get_printer_level() method."""
        level = config_manager.get_printer_level()
        assert isinstance(level, str)

    def test_get_file_logger_level(self, config_manager: ConfigurationManager) -> None:
        """Test get_file_logger_level() method."""
        level = config_manager.get_file_logger_level()
        assert isinstance(level, str)

    def test_get_indent_step(self, config_manager: ConfigurationManager) -> None:
        """Test get_indent_step() method."""
        step = config_manager.get_indent_step()
        assert isinstance(step, int)
        assert step > 0

    def test_get_indent_symbol(self, config_manager: ConfigurationManager) -> None:
        """Test get_indent_symbol() method."""
        symbol = config_manager.get_indent_symbol()
        assert isinstance(symbol, str)

    def test_get_base_indent_symbol(self, config_manager: ConfigurationManager) -> None:
        """Test get_base_indent_symbol() method."""
        symbol = config_manager.get_base_indent_symbol()
        assert isinstance(symbol, str)

    def test_get_log_rotation(self, config_manager: ConfigurationManager) -> None:
        """Test get_log_rotation() method."""
        rotation = config_manager.get_log_rotation()
        # Can be None or a string
        assert rotation is None or isinstance(rotation, str)

    def test_get_log_retention(self, config_manager: ConfigurationManager) -> None:
        """Test get_log_retention() method."""
        retention = config_manager.get_log_retention()
        # Can be None or a string
        assert retention is None or isinstance(retention, str)

    def test_get_log_compression(self, config_manager: ConfigurationManager) -> None:
        """Test get_log_compression() method."""
        compression = config_manager.get_log_compression()
        # Can be None or a string
        assert compression is None or isinstance(compression, str)


class TestFileOperations:
    """Tests for file operations."""

    def test_save_config(self, temp_config_file: Path) -> None:
        """Test save() method."""
        config = ConfigurationManager(config_file=temp_config_file)
        config.set("test-key", "test-value")
        config.save()

        # Verify file was created and contains the value
        assert temp_config_file.exists()
        content = temp_config_file.read_text(encoding="utf-8")
        assert "test-key" in content
        assert "test-value" in content

    def test_save_creates_directory(self, temp_dir: Path) -> None:
        """Test that save() creates directory if it doesn't exist."""
        config_file = temp_dir / "subdir" / "config.json"
        config = ConfigurationManager(config_file=config_file)
        config.save()
        assert config_file.exists()

    def test_save_handles_permission_error(self, temp_config_file: Path) -> None:
        """Test that save() handles permission errors."""
        config = ConfigurationManager(config_file=temp_config_file)
        config.set("test-key", "test-value")

        with patch("builtins.open", side_effect=PermissionError("Permission denied")):
            with pytest.raises(FileOperationError):
                config.save()

    def test_reset_to_defaults(self, config_manager: ConfigurationManager) -> None:
        """Test reset_to_defaults() method."""
        config_manager.set("custom-key", "custom-value")
        config_manager.reset_to_defaults()
        # Custom key should be removed
        assert config_manager.get("custom-key") is None

    def test_reload(self, temp_config_file: Path) -> None:
        """Test reload() method."""
        # Create initial config
        config_data = {"log-level": "INFO"}
        temp_config_file.parent.mkdir(parents=True, exist_ok=True)
        temp_config_file.write_text(json.dumps(config_data), encoding="utf-8")

        config = ConfigurationManager(config_file=temp_config_file)
        assert config.get("log-level") == "INFO"

        # Modify config file
        config_data["log-level"] = "DEBUG"
        temp_config_file.write_text(json.dumps(config_data), encoding="utf-8")

        # Reload
        config.reload()
        assert config.get("log-level") == "DEBUG"


class TestPriorityOrder:
    """Tests for configuration priority order."""

    def test_env_overrides_file(self, temp_config_file: Path, clean_env: None) -> None:
        """Test that environment variables override config file."""
        # Set config file
        config_data = {"log-level": "INFO"}
        temp_config_file.parent.mkdir(parents=True, exist_ok=True)
        temp_config_file.write_text(json.dumps(config_data), encoding="utf-8")

        # Set environment variable
        os.environ["EZPL_LOG_LEVEL"] = "ERROR"

        config = ConfigurationManager(config_file=temp_config_file)
        # Environment should override file
        assert config.get("log-level") == "ERROR"

    def test_file_overrides_default(self, temp_config_file: Path) -> None:
        """Test that config file overrides defaults."""
        config_data = {"log-level": "WARNING"}
        temp_config_file.parent.mkdir(parents=True, exist_ok=True)
        temp_config_file.write_text(json.dumps(config_data), encoding="utf-8")

        config = ConfigurationManager(config_file=temp_config_file)
        # File should override default
        assert config.get("log-level") == "WARNING"


class TestExport:
    """Tests for export operations."""

    def test_export_to_script_windows(self, temp_dir: Path) -> None:
        """Test export_to_script() for Windows."""
        config = ConfigurationManager()
        config.set("test-key", "test-value")
        output_file = temp_dir / "config.bat"

        with patch("sys.platform", "win32"):
            config.export_to_script(output_file, platform="windows")

        assert output_file.exists()
        content = output_file.read_text(encoding="utf-8")
        assert "set" in content.lower()

    def test_export_to_script_unix(self, temp_dir: Path) -> None:
        """Test export_to_script() for Unix."""
        config = ConfigurationManager()
        config.set("test-key", "test-value")
        output_file = temp_dir / "config.sh"

        with patch("sys.platform", "linux"):
            config.export_to_script(output_file, platform="unix")

        assert output_file.exists()
        content = output_file.read_text(encoding="utf-8")
        assert "export" in content or "#!/bin/bash" in content

    def test_export_handles_io_error(self, temp_dir: Path) -> None:
        """Test that export handles IO errors."""
        config = ConfigurationManager()
        invalid_path = temp_dir / "invalid" / "path" / "script.sh"

        with patch("builtins.open", side_effect=IOError("Permission denied")):
            with pytest.raises(FileOperationError):
                config.export_to_script(invalid_path)


class TestErrorHandling:
    """Tests for error handling."""

    def test_handles_missing_config_file(self, temp_dir: Path) -> None:
        """Test handling of missing config file."""
        config_file = temp_dir / "nonexistent" / "config.json"
        config = ConfigurationManager(config_file=config_file)
        # Should use defaults
        assert config is not None

    def test_handles_corrupted_config_file(self, temp_config_file: Path) -> None:
        """Test handling of corrupted config file."""
        temp_config_file.parent.mkdir(parents=True, exist_ok=True)
        temp_config_file.write_text("{invalid json}", encoding="utf-8")

        # Should not raise error, should use defaults
        config = ConfigurationManager(config_file=temp_config_file)
        assert config is not None
