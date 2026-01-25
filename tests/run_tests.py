#!/usr/bin/env python
# ///////////////////////////////////////////////////////////////
# EZPL - Test Runner Script
# Project: ezpl
# ///////////////////////////////////////////////////////////////

"""
Test runner script for Ezpl logging framework.

This script provides a convenient way to run tests with various options:
- Unit, integration, or robustness tests
- Coverage reports
- Parallel execution
- Custom markers
"""

from __future__ import annotations

# ///////////////////////////////////////////////////////////////
# IMPORTS
# ///////////////////////////////////////////////////////////////
# Standard library imports
import argparse
import subprocess
import sys
from pathlib import Path

# ///////////////////////////////////////////////////////////////
# FUNCTIONS
# ///////////////////////////////////////////////////////////////


def run_command(cmd, description) -> bool:
    print(f"\n{'=' * 60}")
    print(f"🚀 {description}")
    print(f"{'=' * 60}")
    try:
        # Use subprocess.run without capture_output to stream output in real-time
        # This prevents blocking when output is large (e.g., with --coverage)
        result = subprocess.run(cmd, shell=True, check=False)  # noqa: S602
        return result.returncode == 0
    except KeyboardInterrupt:
        print("\n⚠️  Interruption utilisateur (Ctrl+C)")
        return False
    except Exception as e:
        print(f"❌ Erreur lors de l'exécution: {e}")
        return False


def main() -> None:
    parser = argparse.ArgumentParser(description="Lanceur de tests pour Ezpl")
    parser.add_argument(
        "--type",
        choices=["unit", "integration", "robustness", "all"],
        default="unit",
        help="Type de tests à exécuter",
    )
    parser.add_argument(
        "--coverage", action="store_true", help="Générer un rapport de couverture"
    )
    parser.add_argument("--verbose", action="store_true", help="Mode verbeux")
    parser.add_argument("--fast", action="store_true", help="Exclure les tests lents")
    parser.add_argument(
        "--parallel",
        action="store_true",
        help="Exécuter les tests en parallèle (pytest-xdist)",
    )
    parser.add_argument(
        "--marker",
        type=str,
        help="Exécuter uniquement les tests avec ce marker (ex: wizard, config)",
    )
    args = parser.parse_args()

    if not Path("pyproject.toml").exists():
        print(
            "❌ Erreur: pyproject.toml non trouvé. Exécutez ce script depuis la racine du projet."
        )
        sys.exit(1)

    cmd_parts = [sys.executable, "-m", "pytest"]
    if args.verbose:
        cmd_parts.append("-v")
    if args.fast:
        cmd_parts.extend(["-m", "not slow"])
    if args.marker:
        cmd_parts.extend(["-m", args.marker])
    if args.parallel:
        cmd_parts.extend(["-n", "auto"])
    if args.type == "unit":
        cmd_parts.append("tests/unit/")
    elif args.type == "integration":
        cmd_parts.append("tests/integration/")
    elif args.type == "robustness":
        cmd_parts.append("tests/robustness/")
    else:
        cmd_parts.append("tests/")
    if args.coverage:
        cmd_parts.extend(
            ["--cov=ezpl", "--cov-report=term-missing", "--cov-report=html:htmlcov"]
        )
    cmd = " ".join(cmd_parts)
    success = run_command(cmd, f"Exécution des tests {args.type}")
    if success:
        print("\n✅ Tests exécutés avec succès!")
        if args.coverage:
            print("\n📊 Rapport de couverture généré dans htmlcov/")
            print("   Ouvrez htmlcov/index.html dans votre navigateur")
    else:
        print("\n❌ Échec des tests")
        sys.exit(1)


if __name__ == "__main__":
    main()
