# Git Hooks - Enelog

Ce dossier contient les hooks Git personnalisés pour le projet Enelog.

## Hook post-commit - Création automatique de tags

### 🎯 Objectif
Créer automatiquement **deux tags Git** à chaque commit lorsque la version change dans `pyproject.toml` :

1. **Tag de version classique** : `v3.1.6` (version complète)
2. **Tag "latest" de version majeure** : `v3-latest` (dernière version de la branche majeure)

### 📦 Contenu
- `post-commit` - Hook PowerShell principal
- `install-hook.bat` - Script d'installation
- `uninstall-hook.bat` - Script de désinstallation
- `README.md` - Cette documentation

### 🚀 Installation

1. **Exécuter l'installation :**
   ```cmd
   cd c:\Dev\__Outils\__PY\.lib\enelog
   .hooks\install-hook.bat
   ```

2. **Vérification :**
   - Le hook est copié dans `.git/hooks/post-commit`
   - Un backup de l'ancien hook est créé si nécessaire

### 🔧 Fonctionnement

**Déclenchement :** À chaque `git commit`

**Logique :**
1. Lit la version dans `pyproject.toml` (priorité)
2. Fallback vers `setup.py` si nécessaire
3. Extrait le numéro de version majeure
4. Crée/met à jour **deux tags** :
   - `v{version}` (ex: `v3.1.6`)
   - `v{major}-latest` (ex: `v3-latest`)

**Exemple :**
```cmd
# Modifier la version
echo 'version = "3.1.6"' >> pyproject.toml

# Committer
git add pyproject.toml
git commit -m "Bump version to 3.1.6"

# → Le hook s'exécute automatiquement
# ✓ [AUTO-TAG] Créé: v3.1.6
# ✓ [AUTO-TAG] Créé: v3-latest
```

### 🏷️ Types de tags créés

| Version | Tag classique | Tag latest |
|---------|---------------|------------|
| `3.1.6` | `v3.1.6` | `v3-latest` |
| `3.2.0` | `v3.2.0` | `v3-latest` |
| `4.0.0` | `v4.0.0` | `v4-latest` |

**Avantages :**
- **Tag classique** : Point de référence stable pour chaque version
- **Tag latest** : Pointe toujours vers la dernière version de la branche majeure

### ⚙️ Configuration

**Push automatique des tags :**
Pour pousser automatiquement les tags vers le distant (avec force pour les mises à jour), éditez `.git/hooks/post-commit` et décommentez :
```powershell
& git push origin "$tagName" --force 2>$null
& git push origin "$latestTagName" --force 2>$null
```

### 🗑️ Désinstallation

```cmd
.hooks\uninstall-hook.bat
```

### 📋 Messages du hook

- `✓ [AUTO-TAG] Créé: v3.1.6` - Nouveau tag de version créé
- `✓ [AUTO-TAG] Créé: v3-latest` - Nouveau tag latest créé
- `✓ [AUTO-TAG] Mis à jour: v3.1.6` - Tag de version mis à jour
- `✓ [AUTO-TAG] Mis à jour: v3-latest` - Tag latest mis à jour
- `→ [AUTO-TAG] Aucune version trouvée` - Pas de version détectée
- `❌ [AUTO-TAG] Erreur création/mise à jour` - Erreur lors de l'opération

### 🔍 Dépannage

**Le hook ne s'exécute pas :**
- Vérifier que le fichier `.git/hooks/post-commit` existe
- Vérifier les permissions du fichier

**Version non détectée :**
- Vérifier le format dans `pyproject.toml` : `version = "x.y.z"`
- Vérifier la syntaxe du fichier

**Tag non créé :**
- Vérifier que vous êtes dans un repository Git
- Vérifier que le tag n'existe pas déjà : `git tag -l`

**Tag latest non créé :**
- Vérifier que la version suit le format `x.y.z` (au moins 2 points)
- Le numéro de version majeure doit être extrait correctement

### 📁 Structure

```
.hooks/
├── post-commit           # Hook PowerShell principal
├── install-hook.bat      # Installation automatique
├── uninstall-hook.bat    # Désinstallation
└── README.md             # Documentation
```

---

**Auteur :** GitHub Copilot  
**Projet :** Enelog  
**Date :** 19 août 2025
