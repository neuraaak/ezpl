@echo off
REM Installation script for Git hooks (Windows)
REM Project: Ezpl
REM Usage: install.bat

echo Installing Git hooks for Ezpl project...
echo.

REM Get project root (parent of .hooks directory)
cd /d "%~dp0\.."

REM Check if we're in a git repository
git rev-parse --git-dir >nul 2>&1
if errorlevel 1 (
    echo Error: Not a Git repository
    echo Please run this script from the root of a Git repository
    exit /b 1
)

REM Configure Git to use .hooks directory
echo Configuring Git to use .hooks directory...
git config core.hooksPath .hooks
if errorlevel 1 (
    echo Failed to configure Git hooks path
    exit /b 1
)
echo Git hooks path configured: .hooks

REM Verify configuration
git config core.hooksPath >nul 2>&1
if errorlevel 1 (
    echo Warning: Configuration may not be correct
) else (
    echo Configuration verified: core.hooksPath = .hooks
)

echo.
echo Git hooks installation completed!
echo.
echo Summary:
echo    - Git hooks path: .hooks
echo    - Pre-commit hook: Format code before commit
echo    - Post-commit hook: Auto-create version tags
echo.
echo To test hooks manually:
echo    .hooks\pre-commit
echo    .hooks\post-commit
echo.
echo To uninstall:
echo    git config --unset core.hooksPath

