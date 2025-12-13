#!/usr/bin/env python3
"""
Build script for Ezpl PyPI package.
This script builds the package and optionally uploads it to PyPI.
"""

import glob
import os
import shutil
import subprocess
import sys


def run_command(command, description=""):
    """Run a command and return success status."""
    if description:
        print(f"🔄 {description}...")

    try:
        result = subprocess.run(  # noqa: S603
            command, check=True, capture_output=True, text=True
        )  # noqa: S603
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")
        if e.stderr:
            print(f"Error output: {e.stderr}")
        return False


def clean_build():
    """Clean previous build artifacts."""
    print("🧹 Cleaning previous build artifacts...")

    # Remove build directories
    paths_to_remove = ["build", "dist"]

    # Add egg-info directories (using glob for pattern matching)
    egg_info_patterns = glob.glob("*.egg-info")
    paths_to_remove.extend(egg_info_patterns)

    for path in paths_to_remove:
        if os.path.exists(path):
            if os.path.isdir(path):
                shutil.rmtree(path)
                print(f"   Removed directory: {path}")
            else:
                os.remove(path)
                print(f"   Removed file: {path}")

    print("✅ Build artifacts cleaned")


def build_package():
    """Build the package."""
    print("🔨 Building Ezpl package...")

    # Clean previous builds
    clean_build()

    # Build the package
    commands = [
        [sys.executable, "-m", "build", "--wheel"],
        [sys.executable, "-m", "build", "--sdist"],
    ]

    for command in commands:
        if not run_command(command, "Building package"):
            return False

    print("✅ Package built successfully")
    return True


def check_package():
    """Check the built package."""
    print("🔍 Checking package...")

    commands = [
        [sys.executable, "-m", "twine", "check", "dist/*"],
    ]

    for command in commands:
        if not run_command(command, "Checking package"):
            return False

    print("✅ Package check passed")
    return True


def upload_to_test_pypi():
    """Upload to Test PyPI."""
    print("🚀 Uploading to Test PyPI...")

    commands = [
        [sys.executable, "-m", "twine", "upload", "--repository", "testpypi", "dist/*"],
    ]

    for command in commands:
        if not run_command(command, "Uploading to Test PyPI"):
            print("❌ Upload to Test PyPI failed:")
            return False

    print("✅ Upload to Test PyPI successful!")
    return True


def upload_to_pypi():
    """Upload to PyPI."""
    print("🚀 Uploading to PyPI...")

    commands = [
        [sys.executable, "-m", "twine", "upload", "dist/*"],
    ]

    for command in commands:
        if not run_command(command, "Uploading to PyPI"):
            print("❌ Upload to PyPI failed:")
            return False

    print("✅ Upload to PyPI successful!")
    return True


def main():
    """Main function."""
    if len(sys.argv) < 2:
        print("Usage: python build_package.py [build|check|test-upload|upload]")
        print("  build        - Build the package")
        print("  check        - Check the built package")
        print("  test-upload  - Upload to Test PyPI")
        print("  upload       - Upload to PyPI")
        return

    action = sys.argv[1]

    if action == "build":
        if not build_package():
            sys.exit(1)

    elif action == "check":
        if not build_package():
            sys.exit(1)
        if not check_package():
            sys.exit(1)

    elif action == "test-upload":
        if not build_package():
            sys.exit(1)
        if not upload_to_test_pypi():
            sys.exit(1)

    elif action == "upload":
        if not build_package():
            sys.exit(1)
        if not upload_to_pypi():
            sys.exit(1)

    else:
        print(f"❌ Unknown action: {action}")
        sys.exit(1)


if __name__ == "__main__":
    main()
