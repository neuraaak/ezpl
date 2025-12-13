@echo off
setlocal enabledelayedexpansion
echo ===============================================
echo  Installation du hook Git post-commit
echo  Projet: Enelog - Creation auto de tags
echo ===============================================
echo.

REM Vérifier qu'on est dans un repo Git
if not exist ".git" (
    echo ❌ Erreur: Pas de repository Git detecte dans ce dossier
    echo    Executez ce script depuis la racine du projet Git
    pause
    exit /b 1
)

REM Vérifier que le hook source existe
if not exist ".hooks\post-commit" (
    echo ❌ Erreur: Fichier hook source introuvable
    echo    Attendu: .hooks\post-commit
    pause
    exit /b 1
)

REM Créer le dossier hooks s'il n'existe pas
if not exist ".git\hooks" mkdir ".git\hooks"

REM Backup de l'ancien hook s'il existe
if exist ".git\hooks\post-commit" (
    echo → Sauvegarde de l'ancien hook...
    copy ".git\hooks\post-commit" ".git\hooks\post-commit.backup" >nul
    echo   Sauvegarde: .git\hooks\post-commit.backup
)

REM Copier le nouveau hook
copy ".hooks\post-commit" ".git\hooks\post-commit" >nul
if errorlevel 1 (
    echo ❌ Erreur lors de la copie du hook
    pause
    exit /b 1
)

echo ✅ Hook post-commit installe avec succes !
echo.
echo 📋 Configuration:
echo    Source     : .hooks\post-commit
echo    Destination: .git\hooks\post-commit
echo    Type       : Bash script
echo.
echo 🔧 Fonctionnement:
echo    • A chaque commit, lit la version dans pyproject.toml
echo    • Cree automatiquement deux tags:
echo      - Tag de version: v{version} (ex: v3.1.6)
echo      - Tag latest: v{major}-latest (ex: v3-latest)
echo    • Affiche un message de confirmation
echo.
echo 📝 Push automatique:
echo    Les tags sont automatiquement pousses vers le repository distant
echo.
echo 🗑️  Desinstallation:
echo    Supprimez le fichier .git\hooks\post-commit
echo.

REM Test du hook sur la version actuelle
if exist "pyproject.toml" (
    echo 🧪 Test du hook sur la version actuelle:
    for /f "tokens=2 delims==" %%a in ('findstr /r "^version.*=" pyproject.toml') do (
        set "CURRENT_VERSION=%%a"
        set "CURRENT_VERSION=!CURRENT_VERSION: =!"
        set "CURRENT_VERSION=!CURRENT_VERSION:"=!"
        echo    Version detectee: !CURRENT_VERSION!
        echo    Tags qui seront crees au prochain commit:
        echo      - v!CURRENT_VERSION!
        for /f "tokens=1 delims=." %%b in ("!CURRENT_VERSION!") do (
            echo      - v%%b-latest
        )
    )
)

echo.
pause
