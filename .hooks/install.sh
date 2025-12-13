#!/bin/bash
# Installation script for Git hooks
# Project: Ezpl
# Usage: ./install.sh

set -e

echo "🔧 Installing Git hooks for Ezpl project..."
echo ""

# Get project root (parent of .hooks directory)
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_ROOT"

# Check if we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "❌ Error: Not a Git repository"
    echo "   Please run this script from the root of a Git repository"
    exit 1
fi

# Configure Git to use .hooks directory
echo "📝 Configuring Git to use .hooks directory..."
if git config core.hooksPath .hooks; then
    echo "✅ Git hooks path configured: .hooks"
else
    echo "❌ Failed to configure Git hooks path"
    exit 1
fi

# Verify configuration
HOOKS_PATH=$(git config core.hooksPath)
if [ "$HOOKS_PATH" = ".hooks" ]; then
    echo "✅ Configuration verified: core.hooksPath = .hooks"
else
    echo "⚠️  Warning: Configuration may not be correct"
    echo "   Expected: .hooks"
    echo "   Got: $HOOKS_PATH"
fi

# Make hooks executable
echo ""
echo "🔐 Making hooks executable..."
if [ -f ".hooks/pre-commit" ]; then
    chmod +x .hooks/pre-commit
    echo "✅ pre-commit is executable"
else
    echo "⚠️  Warning: .hooks/pre-commit not found"
fi

if [ -f ".hooks/post-commit" ]; then
    chmod +x .hooks/post-commit
    echo "✅ post-commit is executable"
else
    echo "⚠️  Warning: .hooks/post-commit not found"
fi

echo ""
echo "✅ Git hooks installation completed!"
echo ""
echo "📋 Summary:"
echo "   - Git hooks path: .hooks"
echo "   - Pre-commit hook: Format code before commit"
echo "   - Post-commit hook: Auto-create version tags"
echo ""
echo "💡 To test hooks manually:"
echo "   .hooks/pre-commit"
echo "   .hooks/post-commit"
echo ""
echo "💡 To uninstall:"
echo "   git config --unset core.hooksPath"

