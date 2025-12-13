# -*- coding: utf-8 -*-
# ///////////////////////////////////////////////////////////////
# EZPL - Log Statistics Utility
# Project: ezpl
# ///////////////////////////////////////////////////////////////

"""
Log statistics utility for CLI operations.

This module provides functionality to calculate statistics from log files.
"""

# IMPORT BASE
# ///////////////////////////////////////////////////////////////
from ezpl.cli.utils.log_parser import LogEntry


from pathlib import Path
from typing import Dict, Any, List, Optional
from collections import Counter, defaultdict

# IMPORT SPECS
# ///////////////////////////////////////////////////////////////

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from .log_parser import LogParser

## ==> CLASSES
# ///////////////////////////////////////////////////////////////


class LogStatistics:
    """
    Calculate and store statistics from log files.
    """

    # ///////////////////////////////////////////////////////////////
    # INIT
    # ///////////////////////////////////////////////////////////////

    def __init__(self, log_file: Path) -> None:
        """
        Initialize log statistics calculator.

        Args:
            log_file: Path to the log file
        """
        self.log_file = Path(log_file)
        self.parser = LogParser(self.log_file)
        self._entries: Optional[List[LogEntry]] = None

    # ---
    # PRIVATE HELPER METHODS
    # ---

    def _get_entries(self) -> List[LogEntry]:
        """Get all log entries (cached)."""
        if self._entries is None:
            self._entries = list[LogEntry](self.parser.parse())
        return self._entries

    # ///////////////////////////////////////////////////////////////
    # STATISTICS METHODS
    # ///////////////////////////////////////////////////////////////

    def get_level_counts(self) -> Dict[str, int]:
        """
        Get count of messages by level.

        Returns:
            Dictionary mapping level names to counts
        """
        entries = self._get_entries()
        counter = Counter(entry.level for entry in entries)
        return dict(counter)

    def get_file_info(self) -> Dict[str, Any]:
        """
        Get basic file information.

        Returns:
            Dictionary with file size, line count, etc.
        """
        try:
            size = self.log_file.stat().st_size if self.log_file.exists() else 0
            entries = self._get_entries()
            line_count = len(entries)

            # Get date range
            timestamps = [
                entry.timestamp for entry in entries if entry.timestamp is not None
            ]
            date_range = None
            if timestamps:
                date_range = {
                    "first": min(timestamps),
                    "last": max(timestamps),
                }

            return {
                "file_path": str(self.log_file),
                "size_bytes": size,
                "size_mb": round(size / (1024 * 1024), 2),
                "line_count": line_count,
                "date_range": date_range,
            }
        except Exception:
            return {
                "file_path": str(self.log_file),
                "size_bytes": 0,
                "size_mb": 0,
                "line_count": 0,
                "date_range": None,
            }

    def get_temporal_distribution(self, period: str = "hour") -> Dict[str, int]:
        """
        Get distribution of logs over time.

        Args:
            period: Time period ('hour' or 'day')

        Returns:
            Dictionary mapping time periods to log counts
        """
        entries = self._get_entries()
        distribution: Dict[str, int] = defaultdict(int)

        for entry in entries:
            if entry.timestamp is None:
                continue

            if period == "hour":
                key = entry.timestamp.strftime("%Y-%m-%d %H:00")
            elif period == "day":
                key = entry.timestamp.strftime("%Y-%m-%d")
            else:
                key = entry.timestamp.strftime("%Y-%m-%d %H:%M")

            distribution[key] += 1

        return dict(distribution)

    def get_all_stats(self) -> Dict[str, Any]:
        """
        Get all statistics in a single dictionary.

        Returns:
            Dictionary containing all statistics
        """
        return {
            "file_info": self.get_file_info(),
            "level_counts": self.get_level_counts(),
            "temporal_distribution_hour": self.get_temporal_distribution("hour"),
            "temporal_distribution_day": self.get_temporal_distribution("day"),
        }
