# -*- coding: utf-8 -*-
# ///////////////////////////////////////////////////////////////
# EZPL - Tests unitaires Exceptions
# Project: ezpl
# ///////////////////////////////////////////////////////////////

"""
Unit tests for custom exceptions.

Tests cover:
- All exception types
- Exception messages
- Exception attributes
- Exception hierarchy
- Error codes
"""

# IMPORT BASE
# ///////////////////////////////////////////////////////////////
import pytest

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from ezpl.core.exceptions import (
    ConfigurationError,
    EzplError,
    FileOperationError,
    HandlerError,
    InitializationError,
    LoggingError,
    ValidationError,
)

# IMPORT SPECS
# ///////////////////////////////////////////////////////////////


## ==> TESTS
# ///////////////////////////////////////////////////////////////


class TestEzplError:
    """Tests for base EzplError exception."""

    def test_ezpl_error_basic(self) -> None:
        """Test basic EzplError creation."""
        error = EzplError("Test error message")
        assert str(error) == "Test error message"
        assert error.message == "Test error message"
        assert error.error_code is None

    def test_ezpl_error_with_code(self) -> None:
        """Test EzplError with error code."""
        error = EzplError("Test error", "TEST_CODE")
        assert error.error_code == "TEST_CODE"
        assert "[TEST_CODE]" in str(error)

    def test_ezpl_error_str_representation(self) -> None:
        """Test string representation of EzplError."""
        error = EzplError("Test message", "CODE")
        error_str = str(error)
        assert "CODE" in error_str
        assert "Test message" in error_str

    def test_ezpl_error_inheritance(self) -> None:
        """Test that EzplError inherits from Exception."""
        error = EzplError("Test")
        assert isinstance(error, Exception)


class TestConfigurationError:
    """Tests for ConfigurationError exception."""

    def test_configuration_error_basic(self) -> None:
        """Test basic ConfigurationError creation."""
        error = ConfigurationError("Config error")
        assert str(error) == "[CONFIG_ERROR] Config error"
        assert error.error_code == "CONFIG_ERROR"
        assert error.config_key is None

    def test_configuration_error_with_key(self) -> None:
        """Test ConfigurationError with config key."""
        error = ConfigurationError("Invalid config", "log-level")
        assert error.config_key == "log-level"

    def test_configuration_error_inheritance(self) -> None:
        """Test that ConfigurationError inherits from EzplError."""
        error = ConfigurationError("Test")
        assert isinstance(error, EzplError)
        assert isinstance(error, Exception)


class TestLoggingError:
    """Tests for LoggingError exception."""

    def test_logging_error_basic(self) -> None:
        """Test basic LoggingError creation."""
        error = LoggingError("Logging error")
        assert str(error) == "[LOGGING_ERROR] Logging error"
        assert error.error_code == "LOGGING_ERROR"
        assert error.handler_type is None

    def test_logging_error_with_handler_type(self) -> None:
        """Test LoggingError with handler type."""
        error = LoggingError("Handler error", "file")
        assert error.handler_type == "file"

    def test_logging_error_inheritance(self) -> None:
        """Test that LoggingError inherits from EzplError."""
        error = LoggingError("Test")
        assert isinstance(error, EzplError)
        assert isinstance(error, Exception)


class TestValidationError:
    """Tests for ValidationError exception."""

    def test_validation_error_basic(self) -> None:
        """Test basic ValidationError creation."""
        error = ValidationError("Validation error")
        assert str(error) == "[VALIDATION_ERROR] Validation error"
        assert error.error_code == "VALIDATION_ERROR"
        assert error.field_name is None
        assert error.value is None

    def test_validation_error_with_field(self) -> None:
        """Test ValidationError with field name."""
        error = ValidationError("Invalid value", "level", "INVALID")
        assert error.field_name == "level"
        assert error.value == "INVALID"

    def test_validation_error_inheritance(self) -> None:
        """Test that ValidationError inherits from EzplError."""
        error = ValidationError("Test")
        assert isinstance(error, EzplError)
        assert isinstance(error, Exception)


class TestInitializationError:
    """Tests for InitializationError exception."""

    def test_initialization_error_basic(self) -> None:
        """Test basic InitializationError creation."""
        error = InitializationError("Init error")
        assert str(error) == "[INIT_ERROR] Init error"
        assert error.error_code == "INIT_ERROR"
        assert error.component is None

    def test_initialization_error_with_component(self) -> None:
        """Test InitializationError with component."""
        error = InitializationError("Failed to init", "printer")
        assert error.component == "printer"

    def test_initialization_error_inheritance(self) -> None:
        """Test that InitializationError inherits from EzplError."""
        error = InitializationError("Test")
        assert isinstance(error, EzplError)
        assert isinstance(error, Exception)


class TestFileOperationError:
    """Tests for FileOperationError exception."""

    def test_file_operation_error_basic(self) -> None:
        """Test basic FileOperationError creation."""
        error = FileOperationError("File error")
        assert str(error) == "[FILE_ERROR] File error"
        assert error.error_code == "FILE_ERROR"
        assert error.file_path is None
        assert error.operation is None

    def test_file_operation_error_with_path(self) -> None:
        """Test FileOperationError with file path."""
        error = FileOperationError("Cannot write", "/path/to/file.log", "write")
        assert error.file_path == "/path/to/file.log"
        assert error.operation == "write"

    def test_file_operation_error_inheritance(self) -> None:
        """Test that FileOperationError inherits from EzplError."""
        error = FileOperationError("Test")
        assert isinstance(error, EzplError)
        assert isinstance(error, Exception)


class TestHandlerError:
    """Tests for HandlerError exception."""

    def test_handler_error_basic(self) -> None:
        """Test basic HandlerError creation."""
        error = HandlerError("Handler error")
        assert str(error) == "[HANDLER_ERROR] Handler error"
        assert error.error_code == "HANDLER_ERROR"
        assert error.handler_name is None

    def test_handler_error_with_name(self) -> None:
        """Test HandlerError with handler name."""
        error = HandlerError("Handler failed", "console")
        assert error.handler_name == "console"

    def test_handler_error_inheritance(self) -> None:
        """Test that HandlerError inherits from EzplError."""
        error = HandlerError("Test")
        assert isinstance(error, EzplError)
        assert isinstance(error, Exception)


class TestExceptionHierarchy:
    """Tests for exception hierarchy."""

    def test_all_exceptions_inherit_from_ezpl_error(self) -> None:
        """Test that all custom exceptions inherit from EzplError."""
        exceptions = [
            ConfigurationError("Test"),
            LoggingError("Test"),
            ValidationError("Test"),
            InitializationError("Test"),
            FileOperationError("Test"),
            HandlerError("Test"),
        ]

        for exc in exceptions:
            assert isinstance(exc, EzplError)
            assert isinstance(exc, Exception)

    def test_all_exceptions_have_error_codes(self) -> None:
        """Test that all exceptions have error codes."""
        exceptions = [
            (ConfigurationError("Test"), "CONFIG_ERROR"),
            (LoggingError("Test"), "LOGGING_ERROR"),
            (ValidationError("Test"), "VALIDATION_ERROR"),
            (InitializationError("Test"), "INIT_ERROR"),
            (FileOperationError("Test"), "FILE_ERROR"),
            (HandlerError("Test"), "HANDLER_ERROR"),
        ]

        for exc, expected_code in exceptions:
            assert exc.error_code == expected_code


class TestExceptionRaising:
    """Tests for exception raising scenarios."""

    def test_raise_configuration_error(self) -> None:
        """Test raising ConfigurationError."""
        with pytest.raises(ConfigurationError) as exc_info:
            raise ConfigurationError("Config test", "test-key")
        assert exc_info.value.config_key == "test-key"

    def test_raise_validation_error(self) -> None:
        """Test raising ValidationError."""
        with pytest.raises(ValidationError) as exc_info:
            raise ValidationError("Validation test", "field", "value")
        assert exc_info.value.field_name == "field"
        assert exc_info.value.value == "value"

    def test_raise_file_operation_error(self) -> None:
        """Test raising FileOperationError."""
        with pytest.raises(FileOperationError) as exc_info:
            raise FileOperationError("File test", "/path/file", "read")
        assert exc_info.value.file_path == "/path/file"
        assert exc_info.value.operation == "read"
