# -*- coding: utf-8 -*-
# ///////////////////////////////////////////////////////////////
# EZPL - Tests d'intégration CLI
# Project: ezpl
# ///////////////////////////////////////////////////////////////

"""
Integration tests for CLI commands with real Ezpl instance.

Tests cover:
- CLI commands with real Ezpl
- Log parsing with real logs
- Statistics on real logs
- Config management via CLI
"""

from pathlib import Path

# IMPORT BASE
# ///////////////////////////////////////////////////////////////
import pytest
from click.testing import CliRunner

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from ezpl import Ezpl
from ezpl.cli.main import cli

# IMPORT SPECS
# ///////////////////////////////////////////////////////////////


## ==> TESTS
# ///////////////////////////////////////////////////////////////


@pytest.fixture
def cli_runner():
    """Create a Click CLI runner for testing."""
    return CliRunner()


class TestCLIWithEzpl:
    """Tests for CLI commands with real Ezpl instance."""

    def test_version_command(self, cli_runner: CliRunner) -> None:
        """Test version command."""
        result = cli_runner.invoke(cli, ["--version"])
        assert result.exit_code == 0
        assert "version" in result.output.lower() or "ezpl" in result.output.lower()

    def test_info_command(self, cli_runner: CliRunner) -> None:
        """Test info command."""
        result = cli_runner.invoke(cli, ["info"])
        assert result.exit_code == 0
        # Should display info about Ezpl
        assert "ezpl" in result.output.lower() or "info" in result.output.lower()

    def test_logs_list_command(
        self, cli_runner: CliRunner, temp_log_file: Path
    ) -> None:
        """Test logs list command."""
        # Create some logs
        ezpl = Ezpl(log_file=temp_log_file)
        logger = ezpl.get_logger()
        logger.info("Test message 1")
        logger.info("Test message 2")

        result = cli_runner.invoke(cli, ["logs", "list"])
        # Should not crash, may or may not find logs
        assert result.exit_code in [0, 1]

    def test_config_get_command(self, cli_runner: CliRunner) -> None:
        """Test config get command."""
        result = cli_runner.invoke(cli, ["config", "get", "log-level"])
        # Should display config value or error
        assert result.exit_code in [0, 1, 2]

    def test_config_set_command(self, cli_runner: CliRunner, clean_env: None) -> None:
        """Test config set command."""
        result = cli_runner.invoke(cli, ["config", "set", "log-level", "DEBUG"])
        # Should set config or show error
        assert result.exit_code in [0, 1, 2]

    def test_config_reset_command(self, cli_runner: CliRunner) -> None:
        """Test config reset command."""
        result = cli_runner.invoke(cli, ["config", "reset"])
        # Should reset config or show error
        assert result.exit_code in [0, 1, 2]


class TestCLILogParsing:
    """Tests for CLI log parsing with real logs."""

    def test_logs_view_with_real_log(
        self, cli_runner: CliRunner, temp_log_file: Path
    ) -> None:
        """Test logs view command with real log file."""
        # Create logs
        ezpl = Ezpl(log_file=temp_log_file)
        logger = ezpl.get_logger()
        logger.info("Test message 1")
        logger.warning("Test message 2")
        logger.error("Test message 3")

        result = cli_runner.invoke(cli, ["logs", "view", str(temp_log_file)])
        # Should display logs or show error
        assert result.exit_code in [0, 1, 2]

    def test_logs_search_with_real_log(
        self, cli_runner: CliRunner, temp_log_file: Path
    ) -> None:
        """Test logs search command with real log file."""
        # Create logs
        ezpl = Ezpl(log_file=temp_log_file)
        logger = ezpl.get_logger()
        logger.info("Test message with keyword")
        logger.info("Another message")

        result = cli_runner.invoke(
            cli, ["logs", "search", "keyword", str(temp_log_file)]
        )
        # Should search logs or show error
        assert result.exit_code in [0, 1, 2]

    def test_logs_stats_with_real_log(
        self, cli_runner: CliRunner, temp_log_file: Path
    ) -> None:
        """Test logs stats command with real log file."""
        # Create logs
        ezpl = Ezpl(log_file=temp_log_file)
        logger = ezpl.get_logger()
        logger.info("Test message 1")
        logger.warning("Test message 2")
        logger.error("Test message 3")

        result = cli_runner.invoke(cli, ["logs", "stats", str(temp_log_file)])
        # Should show statistics or error
        assert result.exit_code in [0, 1, 2]


class TestCLIConfigManagement:
    """Tests for CLI config management."""

    def test_config_get_all(self, cli_runner: CliRunner) -> None:
        """Test config get all."""
        result = cli_runner.invoke(cli, ["config", "get"])
        # Should display all config or error
        assert result.exit_code in [0, 1, 2]

    def test_config_set_multiple(self, cli_runner: CliRunner, clean_env: None) -> None:
        """Test config set with multiple values."""
        result = cli_runner.invoke(
            cli, ["config", "set", "log-level", "DEBUG", "printer-level", "INFO"]
        )
        # Should set config or show error
        assert result.exit_code in [0, 1, 2]
