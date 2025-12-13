@echo off
echo ===============================================
echo  Desinstallation du hook Git post-commit
echo  Projet: Enelog
echo ===============================================
echo.

if not exist ".git\hooks\post-commit" (
    echo → Aucun hook post-commit installe
    goto :end
)

echo Suppression du hook post-commit...
del ".git\hooks\post-commit"

if exist ".git\hooks\post-commit.backup" (
    echo.
    set /p restore="Restaurer l'ancien hook depuis la sauvegarde ? (o/N): "
    if /i "!restore!"=="o" (
        copy ".git\hooks\post-commit.backup" ".git\hooks\post-commit" >nul
        echo ✅ Ancien hook restaure
        del ".git\hooks\post-commit.backup"
    ) else (
        echo → Sauvegarde conservee: .git\hooks\post-commit.backup
    )
) else (
    echo ✅ Hook post-commit desinstalle
)

:end
echo.
pause
