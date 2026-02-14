# ///////////////////////////////////////////////////////////////
# EZPL - Tests unitaires CLI Utils
# Project: ezpl
# ///////////////////////////////////////////////////////////////

"""
Unit tests for CLI utility modules.

Tests cover:
- UserEnvManager behavior and error paths
- LogStatistics aggregation and fallback behavior
"""

from __future__ import annotations

# ///////////////////////////////////////////////////////////////
# IMPORTS
# ///////////////////////////////////////////////////////////////
# Standard library imports
from pathlib import Path
from unittest.mock import patch

# Local imports
from ezpl.cli.utils.env_manager import UserEnvManager
from ezpl.cli.utils.log_stats import LogStatistics

# ///////////////////////////////////////////////////////////////
# TESTS
# ///////////////////////////////////////////////////////////////


class TestUserEnvManager:
    """Tests for UserEnvManager."""

    def test_set_get_remove_cycle(self, temp_dir: Path) -> None:
        """Set, read, then remove a managed environment variable."""
        manager = UserEnvManager()
        manager.env_file = temp_dir / ".env"

        assert manager.set_user_env("log-level", "DEBUG") is True
        assert manager.get_user_env("log-level") == "DEBUG"

        assert manager.remove_user_env("log-level") is True
        assert manager.get_user_env("log-level") is None

    def test_set_user_env_returns_false_on_save_error(self, temp_dir: Path) -> None:
        """set_user_env should return False on I/O errors."""
        manager = UserEnvManager()
        manager.env_file = temp_dir / ".env"

        with patch.object(manager, "_save_env_file", side_effect=OSError("write")):
            assert manager.set_user_env("log-level", "INFO") is False

    def test_remove_all_user_env_returns_false_on_load_error(self) -> None:
        """remove_all_user_env should return False when loading fails."""
        manager = UserEnvManager()

        with patch.object(manager, "_load_env_file", side_effect=ValueError("bad")):
            assert manager.remove_all_user_env() is False


class TestLogStatistics:
    """Tests for LogStatistics."""

    def test_level_counts_and_file_info(self, temp_dir: Path) -> None:
        """Compute counts and basic file information from a valid log file."""
        log_file = temp_dir / "stats.log"
        log_file.write_text(
            "2026-02-14 10:00:00 | INFO      | app:main:10 - Hello\n"
            "2026-02-14 10:01:00 | ERROR     | app:main:11 - Boom\n",
            encoding="utf-8",
        )

        stats = LogStatistics(log_file)

        level_counts = stats.get_level_counts()
        assert level_counts.get("INFO") == 1
        assert level_counts.get("ERROR") == 1

        file_info = stats.get_file_info()
        assert file_info["line_count"] == 2
        assert file_info["size_bytes"] > 0

    def test_get_file_info_fallback_on_internal_error(self, temp_dir: Path) -> None:
        """Return fallback file info structure when stats computation fails."""
        log_file = temp_dir / "stats_error.log"
        log_file.write_text(
            "2026-02-14 10:00:00 | INFO      | app:main:10 - Hello\n",
            encoding="utf-8",
        )

        stats = LogStatistics(log_file)
        with patch.object(stats, "_get_entries", side_effect=ValueError("broken")):
            file_info = stats.get_file_info()

        assert file_info["line_count"] == 0
        assert file_info["date_range"] is None
