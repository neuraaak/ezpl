# -*- coding: utf-8 -*-
# ///////////////////////////////////////////////////////////////
# EZPL - Test rapide interactif
# Project: ezpl
# ///////////////////////////////////////////////////////////////

"""
Script interactif pour tester rapidement les fonctionnalités d'Ezpl.

Usage:
    python examples/quick_test.py
"""

import sys
from pathlib import Path

# Ajouter le répertoire parent au path pour importer ezpl
sys.path.insert(0, str(Path(__file__).parent.parent))

from ezpl import Ezpl


def main():
    """Fonction principale pour les tests interactifs."""

    # Initialiser Ezpl
    log_file = Path("quick_test.log")
    ezpl = Ezpl(log_file=log_file, log_level="DEBUG")
    printer = ezpl.get_printer()
    logger = ezpl.get_logger()
    wizard = printer.wizard

    print("\n" + "=" * 80)
    print("EZPL - TEST RAPIDE INTERACTIF")
    print("=" * 80)

    # Menu
    while True:
        print("\nOptions disponibles:")
        print("1. Tester les niveaux de log")
        print("2. Tester les patterns")
        print("3. Tester les panels")
        print("4. Tester les tables")
        print("5. Tester le JSON")
        print("6. Tester les progress bars")
        print("7. Tester l'indentation")
        print("8. Tester le logging fichier")
        print("9. Afficher la configuration")
        print("0. Quitter")

        choice = input("\nVotre choix: ").strip()

        if choice == "0":
            break
        elif choice == "1":
            test_log_levels(printer)
        elif choice == "2":
            test_patterns(printer)
        elif choice == "3":
            test_panels(wizard)
        elif choice == "4":
            test_tables(wizard)
        elif choice == "5":
            test_json(wizard)
        elif choice == "6":
            test_progress_bars(wizard)
        elif choice == "7":
            test_indentation(ezpl, printer)
        elif choice == "8":
            test_file_logging(logger, ezpl)
        elif choice == "9":
            show_config(ezpl)
        else:
            print("Choix invalide!")

    print("\n✅ Tests terminés!")
    print(f"Consultez le fichier de log: {log_file}")


def test_log_levels(printer):
    """Tester les niveaux de log."""
    print("\n--- Test des niveaux de log ---")
    printer.debug("Message DEBUG")
    printer.info("Message INFO")
    printer.success("Message SUCCESS")
    printer.warning("Message WARNING")
    printer.error("Message ERROR")
    printer.critical("Message CRITICAL")


def test_patterns(printer):
    """Tester les patterns."""
    print("\n--- Test des patterns ---")
    printer.tip("Astuce: Utilisez les type hints")
    printer.system("Message système")
    printer.install("Installation en cours")
    printer.detect("Détection effectuée")
    printer.config("Configuration chargée")
    printer.deps("Dépendances vérifiées")


def test_panels(wizard):
    """Tester les panels."""
    print("\n--- Test des panels ---")
    wizard.info_panel("Info", "Message d'information")
    wizard.success_panel("Succès", "Opération réussie")
    wizard.error_panel("Erreur", "Une erreur s'est produite")
    wizard.warning_panel("Avertissement", "Attention requise")


def test_tables(wizard):
    """Tester les tables."""
    print("\n--- Test des tables ---")
    data = [
        {"Nom": "Alice", "Âge": 30},
        {"Nom": "Bob", "Âge": 25},
    ]
    wizard.table(data, title="Utilisateurs")


def test_json(wizard):
    """Tester le JSON."""
    print("\n--- Test du JSON ---")
    data = {"app": "ezpl", "version": "1.0.0", "features": ["logging", "rich"]}
    wizard.json(data, title="Configuration")


def test_progress_bars(wizard):
    """Tester les progress bars."""
    print("\n--- Test des progress bars ---")
    import time

    with wizard.progress("Traitement...", total=50) as (progress, task):
        for i in range(50):
            progress.update(task, advance=1)
            time.sleep(0.02)


def test_indentation(ezpl, printer):
    """Tester l'indentation."""
    print("\n--- Test de l'indentation ---")
    printer.info("Niveau 0")
    with ezpl.manage_indent():
        printer.info("Niveau 1")
        with ezpl.manage_indent():
            printer.info("Niveau 2")
        printer.info("Retour niveau 1")
    printer.info("Retour niveau 0")


def test_file_logging(logger, ezpl):
    """Tester le logging fichier."""
    print("\n--- Test du logging fichier ---")
    logger.info("Message INFO dans le fichier")
    logger.debug("Message DEBUG dans le fichier")
    logger.warning("Message WARNING dans le fichier")
    logger.error("Message ERROR dans le fichier")
    print(f"Fichier de log: {ezpl.get_log_file()}")


def show_config(ezpl):
    """Afficher la configuration."""
    print("\n--- Configuration actuelle ---")
    config = ezpl.get_config()
    print(f"Log level: {config.get('log-level')}")
    print(f"Printer level: {config.get('printer-level')}")
    print(f"Logger level: {config.get('file-logger-level')}")
    print(f"Log file: {ezpl.get_log_file()}")


if __name__ == "__main__":
    main()
