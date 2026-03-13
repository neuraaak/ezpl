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

from __future__ import annotations

# ///////////////////////////////////////////////////////////////
# IMPORTS
# ///////////////////////////////////////////////////////////////
# Third-party imports
import pytest

# Local imports
from ezpl.core.exceptions import (
    ConfigurationError,
    EzplError,
    FileOperationError,
    HandlerError,
    InitializationError,
    LoggingError,
    ValidationError,
)

# ///////////////////////////////////////////////////////////////
# TESTS
# ///////////////////////////////////////////////////////////////


class TestEzplError:
    """Tests for base EzplError exception."""

    def test_should_set_message_when_created_with_message_only(self) -> None:
        """Test basic EzplError creation."""
        error = EzplError("Test error message")
        assert str(error) == "Test error message"
        assert error.message == "Test error message"
        assert error.error_code is None

    def test_should_include_code_in_str_when_error_code_is_provided(self) -> None:
        """Test EzplError with error code."""
        error = EzplError("Test error", "TEST_CODE")
        assert error.error_code == "TEST_CODE"
        assert "[TEST_CODE]" in str(error)

    def test_should_include_both_code_and_message_when_str_is_called(self) -> None:
        """Test string representation of EzplError."""
        error = EzplError("Test message", "CODE")
        error_str = str(error)
        assert "CODE" in error_str
        assert "Test message" in error_str

    def test_should_be_instance_of_exception_when_ezpl_error_is_created(self) -> None:
        """Test that EzplError inherits from Exception."""
        error = EzplError("Test")
        assert isinstance(error, Exception)


class TestConfigurationError:
    """Tests for ConfigurationError exception."""

    def test_should_set_config_error_code_when_created_without_key(self) -> None:
        """Test basic ConfigurationError creation."""
        error = ConfigurationError("Config error")
        assert str(error) == "[CONFIG_ERROR] Config error"
        assert error.error_code == "CONFIG_ERROR"
        assert error.config_key is None

    def test_should_store_config_key_when_key_is_provided(self) -> None:
        """Test ConfigurationError with config key."""
        error = ConfigurationError("Invalid config", "log-level")
        assert error.config_key == "log-level"

    def test_should_be_instance_of_ezpl_error_when_configuration_error_is_created(
        self,
    ) -> None:
        """Test that ConfigurationError inherits from EzplError."""
        error = ConfigurationError("Test")
        assert isinstance(error, EzplError)
        assert isinstance(error, Exception)


class TestLoggingError:
    """Tests for LoggingError exception."""

    def test_should_set_logging_error_code_when_created_without_handler_type(
        self,
    ) -> None:
        """Test basic LoggingError creation."""
        error = LoggingError("Logging error")
        assert str(error) == "[LOGGING_ERROR] Logging error"
        assert error.error_code == "LOGGING_ERROR"
        assert error.handler_type is None

    def test_should_store_handler_type_when_handler_type_is_provided(self) -> None:
        """Test LoggingError with handler type."""
        error = LoggingError("Handler error", "file")
        assert error.handler_type == "file"

    def test_should_be_instance_of_ezpl_error_when_logging_error_is_created(
        self,
    ) -> None:
        """Test that LoggingError inherits from EzplError."""
        error = LoggingError("Test")
        assert isinstance(error, EzplError)
        assert isinstance(error, Exception)


class TestValidationError:
    """Tests for ValidationError exception."""

    def test_should_set_validation_error_code_when_created_without_field(self) -> None:
        """Test basic ValidationError creation."""
        error = ValidationError("Validation error")
        assert str(error) == "[VALIDATION_ERROR] Validation error"
        assert error.error_code == "VALIDATION_ERROR"
        assert error.field_name is None
        assert error.value is None

    def test_should_store_field_name_and_value_when_field_and_value_are_provided(
        self,
    ) -> None:
        """Test ValidationError with field name."""
        error = ValidationError("Invalid value", "level", "INVALID")
        assert error.field_name == "level"
        assert error.value == "INVALID"

    def test_should_be_instance_of_ezpl_error_when_validation_error_is_created(
        self,
    ) -> None:
        """Test that ValidationError inherits from EzplError."""
        error = ValidationError("Test")
        assert isinstance(error, EzplError)
        assert isinstance(error, Exception)


class TestInitializationError:
    """Tests for InitializationError exception."""

    def test_should_set_init_error_code_when_created_without_component(self) -> None:
        """Test basic InitializationError creation."""
        error = InitializationError("Init error")
        assert str(error) == "[INIT_ERROR] Init error"
        assert error.error_code == "INIT_ERROR"
        assert error.component is None

    def test_should_store_component_name_when_component_is_provided(self) -> None:
        """Test InitializationError with component."""
        error = InitializationError("Failed to init", "printer")
        assert error.component == "printer"

    def test_should_be_instance_of_ezpl_error_when_initialization_error_is_created(
        self,
    ) -> None:
        """Test that InitializationError inherits from EzplError."""
        error = InitializationError("Test")
        assert isinstance(error, EzplError)
        assert isinstance(error, Exception)


class TestFileOperationError:
    """Tests for FileOperationError exception."""

    def test_should_set_file_error_code_when_created_without_path(self) -> None:
        """Test basic FileOperationError creation."""
        error = FileOperationError("File error")
        assert str(error) == "[FILE_ERROR] File error"
        assert error.error_code == "FILE_ERROR"
        assert error.file_path is None
        assert error.operation is None

    def test_should_store_path_and_operation_when_path_and_operation_are_provided(
        self,
    ) -> None:
        """Test FileOperationError with file path."""
        error = FileOperationError("Cannot write", "/path/to/file.log", "write")
        assert error.file_path == "/path/to/file.log"
        assert error.operation == "write"

    def test_should_be_instance_of_ezpl_error_when_file_operation_error_is_created(
        self,
    ) -> None:
        """Test that FileOperationError inherits from EzplError."""
        error = FileOperationError("Test")
        assert isinstance(error, EzplError)
        assert isinstance(error, Exception)


class TestHandlerError:
    """Tests for HandlerError exception."""

    def test_should_set_handler_error_code_when_created_without_handler_name(
        self,
    ) -> None:
        """Test basic HandlerError creation."""
        error = HandlerError("Handler error")
        assert str(error) == "[HANDLER_ERROR] Handler error"
        assert error.error_code == "HANDLER_ERROR"
        assert error.handler_name is None

    def test_should_store_handler_name_when_handler_name_is_provided(self) -> None:
        """Test HandlerError with handler name."""
        error = HandlerError("Handler failed", "console")
        assert error.handler_name == "console"

    def test_should_be_instance_of_ezpl_error_when_handler_error_is_created(
        self,
    ) -> None:
        """Test that HandlerError inherits from EzplError."""
        error = HandlerError("Test")
        assert isinstance(error, EzplError)
        assert isinstance(error, Exception)


class TestExceptionHierarchy:
    """Tests for exception hierarchy."""

    def test_should_all_be_instances_of_ezpl_error_when_any_exception_is_instantiated(
        self,
    ) -> None:
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

    def test_should_all_have_expected_error_codes_when_any_exception_is_instantiated(
        self,
    ) -> None:
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

    def test_should_expose_config_key_attribute_when_configuration_error_is_raised(
        self,
    ) -> None:
        """Test raising ConfigurationError."""
        with pytest.raises(ConfigurationError) as exc_info:
            raise ConfigurationError("Config test", "test-key")
        assert exc_info.value.config_key == "test-key"

    def test_should_expose_field_name_and_value_when_validation_error_is_raised(
        self,
    ) -> None:
        """Test raising ValidationError."""
        with pytest.raises(ValidationError) as exc_info:
            raise ValidationError("Validation test", "field", "value")
        assert exc_info.value.field_name == "field"
        assert exc_info.value.value == "value"

    def test_should_expose_file_path_and_operation_when_file_operation_error_is_raised(
        self,
    ) -> None:
        """Test raising FileOperationError."""
        with pytest.raises(FileOperationError) as exc_info:
            raise FileOperationError("File test", "/path/file", "read")
        assert exc_info.value.file_path == "/path/file"
        assert exc_info.value.operation == "read"
