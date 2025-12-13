# -*- coding: utf-8 -*-
# ///////////////////////////////////////////////////////////////
# EZPL - Tests unitaires RichWizard
# Project: ezpl
# ///////////////////////////////////////////////////////////////

"""
Unit tests for RichWizard.

Tests cover:
- Panel methods (all types)
- Table methods (all types)
- JSON display
- Progress bars (all types)
- Dynamic layered progress
- Error handling
"""

import time

# IMPORT BASE
# ///////////////////////////////////////////////////////////////
import pytest

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from ezpl import Ezpl

# IMPORT SPECS
# ///////////////////////////////////////////////////////////////


## ==> TESTS
# ///////////////////////////////////////////////////////////////


@pytest.fixture
def wizard():
    """Create a RichWizard instance for testing."""
    ezpl = Ezpl()
    return ezpl.get_printer().wizard


class TestPanels:
    """Tests for panel methods."""

    def test_panel_basic(self, wizard) -> None:
        """Test basic panel() method."""
        wizard.panel("Test content")
        # Verify no exception raised

    def test_panel_with_title(self, wizard) -> None:
        """Test panel() with title."""
        wizard.panel("Test content", title="Test Title")
        # Verify no exception raised

    def test_info_panel(self, wizard) -> None:
        """Test info_panel() method."""
        wizard.info_panel("Info Title", "Info content")
        # Verify no exception raised

    def test_success_panel(self, wizard) -> None:
        """Test success_panel() method."""
        wizard.success_panel("Success Title", "Success content")
        # Verify no exception raised

    def test_error_panel(self, wizard) -> None:
        """Test error_panel() method."""
        wizard.error_panel("Error Title", "Error content")
        # Verify no exception raised

    def test_warning_panel(self, wizard) -> None:
        """Test warning_panel() method."""
        wizard.warning_panel("Warning Title", "Warning content")
        # Verify no exception raised

    def test_installation_panel_pending(self, wizard) -> None:
        """Test installation_panel() with pending status."""
        wizard.installation_panel("Step 1", "Installing...", status="pending")
        # Verify no exception raised

    def test_installation_panel_success(self, wizard) -> None:
        """Test installation_panel() with success status."""
        wizard.installation_panel("Step 1", "Installed", status="success")
        # Verify no exception raised

    def test_installation_panel_error(self, wizard) -> None:
        """Test installation_panel() with error status."""
        wizard.installation_panel("Step 1", "Failed", status="error")
        # Verify no exception raised

    def test_panel_with_custom_style(self, wizard) -> None:
        """Test panel() with custom style."""
        wizard.panel("Content", border_style="red", width=50)
        # Verify no exception raised


class TestTables:
    """Tests for table methods."""

    def test_table_basic(self, wizard) -> None:
        """Test basic table() method."""
        data = [{"Name": "Alice", "Age": 30}, {"Name": "Bob", "Age": 25}]
        wizard.table(data)
        # Verify no exception raised

    def test_table_with_title(self, wizard) -> None:
        """Test table() with title."""
        data = [{"Name": "Alice", "Age": 30}]
        wizard.table(data, title="Users")
        # Verify no exception raised

    def test_table_from_columns(self, wizard) -> None:
        """Test table_from_columns() method."""
        columns = ["Name", "Age"]
        rows = [["Alice", "30"], ["Bob", "25"]]
        wizard.table_from_columns("Users", columns, rows)
        # Verify no exception raised

    def test_status_table(self, wizard) -> None:
        """Test status_table() method."""
        data = [
            {"Service": "API", "Status": "success"},
            {"Service": "DB", "Status": "error"},
        ]
        wizard.status_table("Services", data)
        # Verify no exception raised

    def test_dependency_table(self, wizard) -> None:
        """Test dependency_table() method."""
        deps = {"requests": "2.31.0", "click": "8.1.0", "missing": ""}
        wizard.dependency_table(deps)
        # Verify no exception raised

    def test_command_table(self, wizard) -> None:
        """Test command_table() method."""
        commands = [
            {
                "command": "install",
                "description": "Install package",
                "category": "Package",
            },
            {
                "command": "update",
                "description": "Update package",
                "category": "Package",
            },
        ]
        wizard.command_table(commands)
        # Verify no exception raised

    def test_table_empty_data(self, wizard) -> None:
        """Test table() with empty data."""
        wizard.table([])
        # Should not raise error, just return early
        # Verify no exception raised


class TestJSON:
    """Tests for JSON display."""

    def test_json_with_dict(self, wizard) -> None:
        """Test json() with dictionary."""
        wizard.json({"name": "Alice", "age": 30})
        # Verify no exception raised

    def test_json_with_list(self, wizard) -> None:
        """Test json() with list."""
        wizard.json([1, 2, 3, {"nested": "value"}])
        # Verify no exception raised

    def test_json_with_string(self, wizard) -> None:
        """Test json() with JSON string."""
        wizard.json('{"key": "value"}')
        # Verify no exception raised

    def test_json_with_title(self, wizard) -> None:
        """Test json() with title."""
        wizard.json({"key": "value"}, title="Config")
        # Verify no exception raised

    def test_json_with_indent(self, wizard) -> None:
        """Test json() with custom indent."""
        wizard.json({"key": "value"}, indent=4)
        # Verify no exception raised

    def test_json_without_highlight(self, wizard) -> None:
        """Test json() without highlighting."""
        wizard.json({"key": "value"}, highlight=False)
        # Verify no exception raised

    def test_json_invalid_string(self, wizard) -> None:
        """Test json() with invalid JSON string."""
        wizard.json("{invalid json}")
        # Should handle gracefully
        # Verify no exception raised


class TestProgressBars:
    """Tests for progress bar methods."""

    def test_progress_basic(self, wizard) -> None:
        """Test basic progress() method."""
        with wizard.progress("Processing...", total=100) as (progress, task):
            progress.update(task, advance=50)
        # Verify no exception raised

    def test_progress_indeterminate(self, wizard) -> None:
        """Test progress() with indeterminate total."""
        with wizard.progress("Processing...", total=None) as (progress, task):
            progress.update(task)
        # Verify no exception raised

    def test_spinner(self, wizard) -> None:
        """Test spinner() method."""
        with wizard.spinner("Loading...") as (progress, task):
            time.sleep(0.1)
        # Verify no exception raised

    def test_spinner_with_status(self, wizard) -> None:
        """Test spinner_with_status() method."""
        with wizard.spinner_with_status("Processing...") as (progress, task):
            progress.update(task, status="Step 1/3")
        # Verify no exception raised

    def test_download_progress(self, wizard) -> None:
        """Test download_progress() method."""
        with wizard.download_progress("Downloading...") as (progress, task):
            progress.update(task, advance=50, total=100)
        # Verify no exception raised

    def test_file_download_progress(self, wizard) -> None:
        """Test file_download_progress() method."""
        with wizard.file_download_progress("file.zip", 1024000) as (progress, task):
            progress.update(task, advance=512000)
        # Verify no exception raised

    def test_dependency_progress(self, wizard) -> None:
        """Test dependency_progress() method."""
        deps = ["requests", "click", "rich"]
        # dependency_progress is a context manager that yields multiple times
        gen = wizard.dependency_progress(deps)
        # Get the first yield
        first_yield = gen.__enter__()
        progress, task, dep = first_yield
        progress.advance(task)
        # Consume all remaining yields to allow the generator to complete
        try:
            while True:
                progress, task, dep = next(gen.gen)
                progress.advance(task)
        except (StopIteration, AttributeError):
            pass
        # Exit the context manager
        gen.__exit__(None, None, None)
        # Verify no exception raised

    def test_package_install_progress(self, wizard) -> None:
        """Test package_install_progress() method."""
        packages = [("requests", "2.31.0"), ("click", "8.1.0")]
        # package_install_progress is a context manager that yields multiple times
        gen = wizard.package_install_progress(packages)
        first_yield = gen.__enter__()
        progress, task, pkg, ver = first_yield
        progress.advance(task)
        # Consume all remaining yields
        try:
            while True:
                progress, task, pkg, ver = next(gen.gen)
                progress.advance(task)
        except (StopIteration, AttributeError):
            pass
        gen.__exit__(None, None, None)
        # Verify no exception raised

    def test_step_progress(self, wizard) -> None:
        """Test step_progress() method."""
        steps = [("Init", "Initializing"), ("Install", "Installing")]
        with wizard.step_progress(steps) as (progress, task, steps_list):
            for i in range(len(steps)):
                progress.advance(task)
        # Verify no exception raised

    def test_file_copy_progress(self, wizard) -> None:
        """Test file_copy_progress() method."""
        files = ["file1.txt", "file2.txt", "file3.txt"]
        with wizard.file_copy_progress(files) as (progress, task, files_list):
            for i in range(len(files)):
                progress.advance(task)
        # Verify no exception raised

    def test_installation_progress(self, wizard) -> None:
        """Test installation_progress() method."""
        steps = [("Init", "Initializing"), ("Install", "Installing")]
        # installation_progress is a context manager that yields multiple times
        gen = wizard.installation_progress(steps)
        first_yield = gen.__enter__()
        progress, task, name, desc = first_yield
        progress.advance(task)
        # Consume all remaining yields
        try:
            while True:
                progress, task, name, desc = next(gen.gen)
                progress.advance(task)
        except (StopIteration, AttributeError):
            pass
        gen.__exit__(None, None, None)
        # Verify no exception raised

    def test_build_progress(self, wizard) -> None:
        """Test build_progress() method."""
        phases = [("Compile", 50), ("Test", 30), ("Package", 20)]
        # build_progress is a context manager that yields multiple times
        gen = wizard.build_progress(phases)
        first_yield = gen.__enter__()
        progress, task, phase, weight = first_yield
        progress.update(task, completed=progress.tasks[task].completed + weight)
        # Consume all remaining yields
        try:
            while True:
                progress, task, phase, weight = next(gen.gen)
                progress.update(task, completed=progress.tasks[task].completed + weight)
        except (StopIteration, AttributeError):
            pass
        gen.__exit__(None, None, None)
        # Verify no exception raised

    def test_deployment_progress(self, wizard) -> None:
        """Test deployment_progress() method."""
        stages = ["Prepare", "Deploy", "Verify"]
        # deployment_progress is a context manager that yields multiple times
        gen = wizard.deployment_progress(stages)
        first_yield = gen.__enter__()
        progress, task, stage = first_yield
        progress.advance(task)
        # Consume all remaining yields
        try:
            while True:
                progress, task, stage = next(gen.gen)
                progress.advance(task)
        except (StopIteration, AttributeError):
            pass
        gen.__exit__(None, None, None)
        # Verify no exception raised

    def test_layered_progress(self, wizard) -> None:
        """Test layered_progress() method."""
        layers = [
            {"name": "Layer1", "total": 100},
            {"name": "Layer2", "total": 50},
        ]
        with wizard.layered_progress(layers) as (progress, task_ids):
            for layer_name, task_id in task_ids.items():
                progress.update(task_id, advance=50)
        # Verify no exception raised


class TestDynamicProgress:
    """Tests for dynamic layered progress."""

    def test_dynamic_layered_progress_basic(self, wizard) -> None:
        """Test basic dynamic_layered_progress()."""
        stages = [
            {
                "name": "step1",
                "type": "progress",
                "description": "Step 1",
                "total": 100,
            },
        ]
        with wizard.dynamic_layered_progress(stages) as progress:
            progress.update_layer("step1", 50, "Processing...")
            progress.complete_layer("step1")
        # Verify no exception raised

    def test_dynamic_layered_progress_with_main(self, wizard) -> None:
        """Test dynamic_layered_progress() with main layer."""
        stages = [
            {"name": "main", "type": "main", "description": "Overall Progress"},
            {
                "name": "step1",
                "type": "progress",
                "description": "Step 1",
                "total": 100,
            },
            {
                "name": "step2",
                "type": "steps",
                "description": "Step 2",
                "steps": ["A", "B"],
            },
        ]
        with wizard.dynamic_layered_progress(stages) as progress:
            progress.update_layer("step1", 50)
            progress.complete_layer("step1")
            progress.update_layer("step2", 1)
            progress.complete_layer("step2")
        # Verify no exception raised

    def test_dynamic_layered_progress_with_download(self, wizard) -> None:
        """Test dynamic_layered_progress() with download layer."""
        stages = [
            {
                "name": "download",
                "type": "download",
                "description": "Downloading",
                "total_size": 1024000,
                "filename": "file.zip",
            },
        ]
        with wizard.dynamic_layered_progress(stages) as progress:
            progress.update_layer("download", 512000, "Downloading...")
            progress.complete_layer("download")
        # Verify no exception raised

    def test_dynamic_layered_progress_with_spinner(self, wizard) -> None:
        """Test dynamic_layered_progress() with spinner layer."""
        stages = [
            {"name": "spinner", "type": "spinner", "description": "Processing..."},
        ]
        with wizard.dynamic_layered_progress(stages) as progress:
            progress.update_layer("spinner", 0, "Working...")
            progress.complete_layer("spinner")
        # Verify no exception raised

    def test_dynamic_layered_progress_error_handling(self, wizard) -> None:
        """Test dynamic_layered_progress() error handling."""
        stages = [
            {
                "name": "step1",
                "type": "progress",
                "description": "Step 1",
                "total": 100,
            },
        ]
        with wizard.dynamic_layered_progress(stages) as progress:
            progress.handle_error("step1", "Test error")
        # Verify no exception raised

    def test_dynamic_layered_progress_emergency_stop(self, wizard) -> None:
        """Test dynamic_layered_progress() emergency stop."""
        stages = [
            {
                "name": "step1",
                "type": "progress",
                "description": "Step 1",
                "total": 100,
            },
        ]
        with wizard.dynamic_layered_progress(stages) as progress:
            progress.emergency_stop("Critical error")
        # Verify no exception raised

    def test_dynamic_layered_progress_without_time(self, wizard) -> None:
        """Test dynamic_layered_progress() without time display."""
        stages = [
            {
                "name": "step1",
                "type": "progress",
                "description": "Step 1",
                "total": 100,
            },
        ]
        with wizard.dynamic_layered_progress(stages, show_time=False) as progress:
            progress.update_layer("step1", 50)
            progress.complete_layer("step1")
        # Verify no exception raised


class TestErrorHandling:
    """Tests for error handling in wizard methods."""

    def test_panel_with_invalid_content(self, wizard) -> None:
        """Test panel() with invalid content type."""
        # Should handle gracefully
        wizard.panel(None)
        # Verify no exception raised

    def test_table_with_invalid_data(self, wizard) -> None:
        """Test table() with invalid data structure."""
        # Should handle gracefully
        wizard.table([{"key": "value"}, "invalid"])
        # Verify no exception raised

    def test_json_with_invalid_data(self, wizard) -> None:
        """Test json() with invalid JSON."""
        # Should handle gracefully
        wizard.json("{invalid json}")
        # Verify no exception raised
