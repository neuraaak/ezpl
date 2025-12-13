# -*- coding: utf-8 -*-
# ///////////////////////////////////////////////////////////////
# EZPL - Script de démonstration
# Project: ezpl
# ///////////////////////////////////////////////////////////////

"""
Script de démonstration pour tester les fonctionnalités d'Ezpl.

Ce script montre comment utiliser :
- Les différents niveaux de log
- Les méthodes de pattern
- Les fonctionnalités Rich (panels, tables, JSON)
- Les progress bars
- L'indentation
- La configuration
"""

# IMPORT BASE
# ///////////////////////////////////////////////////////////////
import sys
import time
from pathlib import Path

# Ajouter le répertoire parent au path pour importer ezpl
sys.path.insert(0, str(Path(__file__).parent.parent))

from ezpl import Ezpl

## ==> INITIALISATION
# ///////////////////////////////////////////////////////////////

# Créer un fichier de log temporaire pour la démo
log_file = Path("demo.log")

# Initialiser Ezpl
ezpl = Ezpl(log_file=log_file, log_level="DEBUG")
printer = ezpl.get_printer()
logger = ezpl.get_logger()

## ==> SECTION 1: NIVEAUX DE LOG
# ///////////////////////////////////////////////////////////////

print("\n" + "=" * 80)
print("SECTION 1: NIVEAUX DE LOG")
print("=" * 80 + "\n")

printer.debug("Message de debug - pour le développement")
printer.info("Message d'information - opération normale")
printer.success("Message de succès - opération réussie")
printer.warning("Message d'avertissement - attention requise")
printer.error("Message d'erreur - problème détecté")
printer.critical("Message critique - erreur grave")

# Logs dans le fichier
logger.debug("Debug dans le fichier")
logger.info("Info dans le fichier")
logger.warning("Warning dans le fichier")
logger.error("Error dans le fichier")

## ==> SECTION 2: MÉTHODES DE PATTERN
# ///////////////////////////////////////////////////////////////

print("\n" + "=" * 80)
print("SECTION 2: MÉTHODES DE PATTERN")
print("=" * 80 + "\n")

printer.tip("Astuce: Utilisez les type hints pour améliorer votre code")
printer.system("Vérification du système en cours...")
printer.install("Installation de la dépendance 'requests'...")
printer.detect("Détection de Python 3.11.3")
printer.config("Configuration chargée depuis ~/.ezpl/config.json")
printer.deps("Vérification des dépendances: rich, loguru, click")

## ==> SECTION 3: RICH FEATURES - PANELS
# ///////////////////////////////////////////////////////////////

print("\n" + "=" * 80)
print("SECTION 3: RICH FEATURES - PANELS")
print("=" * 80 + "\n")

wizard = printer.wizard

# Panel simple
wizard.panel("Contenu du panel", title="Panel Simple", style="blue")

# Panels avec statut
wizard.info_panel("Information", "Ceci est un message d'information")
wizard.success_panel("Succès", "Opération terminée avec succès!")
wizard.error_panel("Erreur", "Une erreur s'est produite")
wizard.warning_panel("Avertissement", "Attention: vérifiez la configuration")

# Panel d'installation
wizard.installation_panel(
    "Installation", "Installation de ezpl en cours...", status="in_progress"
)

## ==> SECTION 4: RICH FEATURES - TABLES
# ///////////////////////////////////////////////////////////////

print("\n" + "=" * 80)
print("SECTION 4: RICH FEATURES - TABLES")
print("=" * 80 + "\n")

# Table simple
data = [
    {"Nom": "Alice", "Âge": 30, "Ville": "Paris"},
    {"Nom": "Bob", "Âge": 25, "Ville": "Lyon"},
    {"Nom": "Charlie", "Âge": 35, "Ville": "Marseille"},
]
wizard.table(data, title="Liste des utilisateurs")

# Table de statut (title est le premier paramètre)
status_data = [
    {"Service": "API", "Statut": "✅ Actif", "Uptime": "99.9%"},
    {"Service": "DB", "Statut": "✅ Actif", "Uptime": "99.8%"},
    {"Service": "Cache", "Statut": "⚠️ Dégradé", "Uptime": "95.2%"},
]
wizard.status_table("Statut des services", status_data, status_column="Statut")

# Table de dépendances (prend un dict, pas une liste)
deps_dict = {
    "requests": "2.31.0",
    "click": "8.1.0",
    "rich": "13.7.0",
}
wizard.dependency_table(deps_dict)

# Table de commandes (pas de paramètre title)
commands = [
    {"command": "python demo.py", "description": "Lancer la démo"},
    {"command": "pytest tests/", "description": "Lancer les tests"},
    {"command": "ezpl logs view", "description": "Voir les logs"},
]
wizard.command_table(commands)

## ==> SECTION 5: RICH FEATURES - JSON
# ///////////////////////////////////////////////////////////////

print("\n" + "=" * 80)
print("SECTION 5: RICH FEATURES - JSON")
print("=" * 80 + "\n")

# JSON simple
config_dict = {
    "app_name": "ezpl",
    "version": "1.0.0",
    "features": ["logging", "rich", "cli"],
    "settings": {
        "log_level": "INFO",
        "log_rotation": "10 MB",
        "log_retention": "7 days",
    },
}
wizard.json(config_dict, title="Configuration")

# JSON avec liste
data_list = [
    {"id": 1, "name": "Item 1", "active": True},
    {"id": 2, "name": "Item 2", "active": False},
    {"id": 3, "name": "Item 3", "active": True},
]
wizard.json(data_list, title="Liste d'éléments")

## ==> SECTION 6: PROGRESS BARS
# ///////////////////////////////////////////////////////////////

print("\n" + "=" * 80)
print("SECTION 6: PROGRESS BARS")
print("=" * 80 + "\n")

# Progress bar simple
print("Progress bar simple:")
with wizard.progress("Traitement en cours...", total=100) as (progress, task):
    for i in range(100):
        progress.update(task, advance=1)
        time.sleep(0.01)

# Spinner
print("\nSpinner:")
with wizard.spinner("Chargement...") as (progress, task):
    time.sleep(2)

# Download progress
print("\nDownload progress:")
with wizard.download_progress("Téléchargement de fichier.zip") as (progress, task):
    for i in range(0, 100, 10):
        progress.update(task, advance=10, total=100)
        time.sleep(0.1)

# File download progress
print("\nFile download progress:")
with wizard.file_download_progress("large_file.zip", 1024000) as (progress, task):
    for i in range(0, 1024000, 102400):
        progress.update(task, advance=102400)
        time.sleep(0.1)

# Dependency progress
print("\nDependency progress:")
dependencies = ["requests", "click", "rich", "loguru"]
gen = wizard.dependency_progress(dependencies)
first_yield = gen.__enter__()
progress, task, dep = first_yield
progress.advance(task)
try:
    while True:
        progress, task, dep = next(gen.gen)
        progress.advance(task)
        time.sleep(0.1)
except (StopIteration, AttributeError):
    pass
gen.__exit__(None, None, None)

# Step progress
print("\nStep progress:")
steps = [("Init", "Initialisation"), ("Process", "Traitement"), ("Done", "Terminé")]
with wizard.step_progress(steps) as (progress, task, steps_list):
    for i in range(len(steps)):
        progress.advance(task)
        time.sleep(0.2)

## ==> SECTION 7: INDENTATION
# ///////////////////////////////////////////////////////////////

print("\n" + "=" * 80)
print("SECTION 7: INDENTATION")
print("=" * 80 + "\n")

printer.info("Message au niveau 0")
with ezpl.manage_indent():
    printer.info("Message au niveau 1")
    with ezpl.manage_indent():
        printer.info("Message au niveau 2")
        with ezpl.manage_indent():
            printer.info("Message au niveau 3")
    printer.info("Retour au niveau 1")
printer.info("Retour au niveau 0")

## ==> SECTION 8: CONFIGURATION
# ///////////////////////////////////////////////////////////////

print("\n" + "=" * 80)
print("SECTION 8: CONFIGURATION")
print("=" * 80 + "\n")

# Afficher la configuration actuelle
config = ezpl.get_config()
printer.info(f"Niveau de log: {config.get('log-level')}")
printer.info(f"Niveau du printer: {config.get('printer-level')}")
printer.info(f"Niveau du logger: {config.get('file-logger-level')}")

# Modifier la configuration
ezpl.configure(printer_level="WARNING")
printer.info("Après configuration - ce message devrait apparaître")
printer.warning("Message d'avertissement - devrait apparaître")

# Remettre en INFO
ezpl.configure(printer_level="INFO")
printer.info("Retour au niveau INFO")

## ==> SECTION 9: LOGGING DANS LE FICHIER
# ///////////////////////////////////////////////////////////////

print("\n" + "=" * 80)
print("SECTION 9: LOGGING DANS LE FICHIER")
print("=" * 80 + "\n")

logger.info("Message d'information dans le fichier")
logger.debug("Message de debug dans le fichier")
logger.warning("Message d'avertissement dans le fichier")
logger.error("Message d'erreur dans le fichier")

# Ajouter un séparateur
ezpl.add_separator()

logger.info("Message après le séparateur")

# Afficher le chemin du fichier de log
printer.info(f"Fichier de log: {ezpl.get_log_file()}")

## ==> SECTION 10: DYNAMIC LAYERED PROGRESS
# ///////////////////////////////////////////////////////////////

print("\n" + "=" * 80)
print("SECTION 10: DYNAMIC LAYERED PROGRESS")
print("=" * 80 + "\n")

stages = [
    {
        "name": "main",
        "type": "main",
        "description": "Progression principale",
        "steps": ["Étape 1", "Étape 2", "Étape 3"],
    },
    {
        "name": "download",
        "type": "download",
        "description": "Téléchargement",
        "total_size": 1024000,
        "filename": "file.zip",
    },
    {"name": "process", "type": "progress", "description": "Traitement", "total": 100},
]

with wizard.dynamic_layered_progress(stages, show_time=True) as progress:
    # Mettre à jour la couche principale
    progress.update_layer("main", 0, "Démarrage...")
    time.sleep(0.5)

    # Mettre à jour le téléchargement
    progress.update_layer("download", 512000, "Téléchargement en cours...")
    time.sleep(0.5)

    # Mettre à jour le traitement
    progress.update_layer("process", 50, "Traitement à 50%")
    time.sleep(0.5)

    # Compléter les couches
    progress.complete_layer("download")
    progress.complete_layer("process")
    progress.complete_layer("main")

## ==> FIN
# ///////////////////////////////////////////////////////////////

print("\n" + "=" * 80)
print("DÉMONSTRATION TERMINÉE")
print("=" * 80 + "\n")

printer.success("Tous les exemples ont été exécutés avec succès!")
printer.info(f"Consultez le fichier de log: {log_file}")
