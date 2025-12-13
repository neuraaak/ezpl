# -*- coding: utf-8 -*-
# ///////////////////////////////////////////////////////////////
# EZPL - Tests d'intégration Configuration
# Project: ezpl
# ///////////////////////////////////////////////////////////////

"""
Integration tests for ConfigurationManager with Ezpl.

Tests cover:
- ConfigurationManager + Ezpl integration
- Environment variables + config file
- Save and reload configuration
- Export configuration to script
"""

import json
import os
from pathlib import Path

# IMPORT BASE
# ///////////////////////////////////////////////////////////////
import pytest

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from ezpl import Ezpl
from ezpl.config import ConfigurationManager

# IMPORT SPECS
# ///////////////////////////////////////////////////////////////


## ==> TESTS
# ///////////////////////////////////////////////////////////////


class TestConfigManagerEzplIntegration:
    """Tests for ConfigurationManager + Ezpl integration."""

    def test_ezpl_uses_config_manager(self, temp_log_file: Path) -> None:
        """Test that Ezpl uses ConfigurationManager."""
        ezpl = Ezpl(log_file=temp_log_file)
        config = ezpl.get_config()

        assert isinstance(config, ConfigurationManager)
        assert config is not None

    def test_config_changes_reflect_in_ezpl(
        self, temp_log_file: Path, temp_config_file: Path
    ) -> None:
        """Test that config changes reflect in Ezpl."""
        ezpl = Ezpl(log_file=temp_log_file)
        ezpl.get_config()

        # Change config directly using configure() method which applies changes immediately
        ezpl.configure(printer_level="WARNING")

        # Verify change is applied to printer immediately
        assert ezpl.get_printer()._level == "WARNING"
        # Logger level should remain unchanged (we only changed printer-level)
        # The default logger level should still be there
        assert ezpl._logger._level is not None

    def test_env_and_file_config_integration(
        self, temp_config_file: Path, temp_log_file: Path, clean_env: None
    ) -> None:
        """Test integration of environment variables and config file."""
        # Set config file
        config_data = {"log-level": "INFO"}
        temp_config_file.parent.mkdir(parents=True, exist_ok=True)
        temp_config_file.write_text(json.dumps(config_data), encoding="utf-8")

        # Set environment variable
        os.environ["EZPL_LOG_LEVEL"] = "ERROR"

        # Mock config file path
        with pytest.MonkeyPatch().context() as m:
            m.setattr(
                "ezpl.config.manager.DefaultConfiguration.CONFIG_FILE", temp_config_file
            )
            _ = Ezpl(log_file=temp_log_file)
            # Environment should override file
            # Note: This tests the integration, actual priority is tested in unit tests

    def test_config_save_and_reload(
        self, temp_config_file: Path, temp_log_file: Path
    ) -> None:
        """Test saving and reloading configuration."""
        # Create a new ConfigurationManager with the temp config file
        config = ConfigurationManager(config_file=temp_config_file)

        # Modify config
        config.set("log-level", "DEBUG")
        config.save()

        # Verify file was saved
        assert temp_config_file.exists()
        content = temp_config_file.read_text(encoding="utf-8")
        assert "log-level" in content

        # Reload
        config.reload()
        assert config.get("log-level") == "DEBUG"

    def test_config_export_integration(
        self, temp_dir: Path, temp_log_file: Path
    ) -> None:
        """Test exporting configuration to script."""
        ezpl = Ezpl(log_file=temp_log_file)
        config = ezpl.get_config()

        output_file = temp_dir / "export.sh"
        config.export_to_script(output_file, platform="unix")

        assert output_file.exists()
        content = output_file.read_text(encoding="utf-8")
        assert "export" in content or "#!/bin/bash" in content
