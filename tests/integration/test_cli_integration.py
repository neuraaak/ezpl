# ///////////////////////////////////////////////////////////////
# EZPL - CLI Integration Tests
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

from __future__ import annotations

# ///////////////////////////////////////////////////////////////
# IMPORTS
# ///////////////////////////////////////////////////////////////
# Standard library imports
from pathlib import Path

# Third-party imports
import pytest
from click.testing import CliRunner

# Local imports
from ezplog import Ezpl
from ezplog.cli.main import cli

pytestmark = [pytest.mark.integration, pytest.mark.cli]

# ///////////////////////////////////////////////////////////////
# TESTS
# ///////////////////////////////////////////////////////////////


@pytest.fixture
def cli_runner():
    """Create a Click CLI runner for testing."""
    return CliRunner()


class TestCLIWithEzpl:
    """Tests for CLI commands with real Ezpl instance."""

    def test_should_display_version_when_version_flag_is_given(
        self, cli_runner: CliRunner
    ) -> None:
        """Test version command."""
        result = cli_runner.invoke(cli, ["--version"])
        assert result.exit_code == 0
        assert "version" in result.output.lower() or "ezpl" in result.output.lower()

    def test_should_display_info_when_info_command_is_invoked(
        self, cli_runner: CliRunner
    ) -> None:
        """Test info command."""
        result = cli_runner.invoke(cli, ["info"])
        assert result.exit_code == 0
        # Should display info about Ezpl
        assert "ezpl" in result.output.lower() or "info" in result.output.lower()

    def test_should_list_log_files_when_logs_list_command_is_invoked(
        self, cli_runner: CliRunner, temp_log_file: Path
    ) -> None:
        """Test logs list command."""
        # Create some logs
        ezpl = Ezpl(log_file=temp_log_file)
        logger = ezpl.get_logger()
        logger.info("Test message 1")
        logger.info("Test message 2")

        result = cli_runner.invoke(
            cli,
            ["logs", "list", "--dir", str(temp_log_file.parent)],
        )
        assert result.exit_code == 0

    def test_should_return_config_value_when_config_get_command_is_invoked(
        self, cli_runner: CliRunner
    ) -> None:
        """Test config get command."""
        result = cli_runner.invoke(cli, ["config", "get", "log-level"])
        assert result.exit_code == 0

    def test_should_set_config_value_when_config_set_command_is_invoked(
        self,
        cli_runner: CliRunner,
        clean_env: None,  # noqa: ARG002
    ) -> None:
        """Test config set command."""
        result = cli_runner.invoke(cli, ["config", "set", "log-level", "DEBUG"])
        assert result.exit_code == 0

    def test_should_reset_config_when_reset_command_is_confirmed(
        self, cli_runner: CliRunner
    ) -> None:
        """Test config reset command."""
        result = cli_runner.invoke(cli, ["config", "reset", "--confirm"])
        assert result.exit_code == 0


class TestCLILogParsing:
    """Tests for CLI log parsing with real logs."""

    def test_should_view_log_entries_when_log_file_contains_real_logs(
        self, cli_runner: CliRunner, temp_log_file: Path
    ) -> None:
        """Test logs view command with real log file."""
        # Create logs
        ezpl = Ezpl(log_file=temp_log_file)
        logger = ezpl.get_logger()
        logger.info("Test message 1")
        logger.warning("Test message 2")
        logger.error("Test message 3")

        result = cli_runner.invoke(
            cli,
            ["logs", "view", "--file", str(temp_log_file)],
        )
        assert result.exit_code == 0

    def test_should_search_log_entries_when_keyword_pattern_is_given(
        self, cli_runner: CliRunner, temp_log_file: Path
    ) -> None:
        """Test logs search command with real log file."""
        # Create logs
        ezpl = Ezpl(log_file=temp_log_file)
        logger = ezpl.get_logger()
        logger.info("Test message with keyword")
        logger.info("Another message")

        result = cli_runner.invoke(
            cli,
            [
                "logs",
                "search",
                "--pattern",
                "keyword",
                "--file",
                str(temp_log_file),
            ],
        )
        assert result.exit_code == 0

    def test_should_display_log_statistics_when_log_file_contains_real_logs(
        self, cli_runner: CliRunner, temp_log_file: Path
    ) -> None:
        """Test logs stats command with real log file."""
        # Create logs
        ezpl = Ezpl(log_file=temp_log_file)
        logger = ezpl.get_logger()
        logger.info("Test message 1")
        logger.warning("Test message 2")
        logger.error("Test message 3")

        result = cli_runner.invoke(
            cli,
            ["logs", "stats", "--file", str(temp_log_file)],
        )
        assert result.exit_code == 0


class TestCLIConfigManagement:
    """Tests for CLI config management."""

    def test_should_display_all_config_when_no_key_is_specified(
        self, cli_runner: CliRunner
    ) -> None:
        """Test config get all."""
        result = cli_runner.invoke(cli, ["config", "get"])
        assert result.exit_code == 0

    def test_should_reject_extra_arguments_when_config_set_receives_too_many_args(
        self,
        cli_runner: CliRunner,
        clean_env: None,  # noqa: ARG002  # pyright: ignore[reportUnusedVariable]
    ) -> None:
        """Test config set rejects unexpected extra arguments."""
        result = cli_runner.invoke(
            cli, ["config", "set", "log-level", "DEBUG", "printer-level", "INFO"]
        )
        assert result.exit_code != 0
