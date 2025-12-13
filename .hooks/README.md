# Git Hooks

Ce dossier contient les hooks Git pour le projet **Ezpl**.

## Hooks Disponibles

### `pre-commit`
- **Objectif** : Formatage automatique du code avant commit
- **Actions** :
  - Exécute `black` pour le formatage du code
  - Exécute `isort` pour l'organisation des imports
  - Exécute `ruff format` pour le formatage supplémentaire
  - Ajoute automatiquement les fichiers formatés au staging area
  - Bloque le commit si des erreurs de formatage sont détectées

### `post-commit`
- **Objectif** : Création automatique de tags après commit réussi
- **Actions** :
  - Lit la version depuis `pyproject.toml`
  - Crée ou met à jour le tag de version (ex: `v1.0.0`)
  - Crée ou met à jour le tag "latest" pour la version majeure (ex: `v1-latest`)
  - Construit le package localement
  - Push les tags vers le dépôt distant

## Installation

### Méthode recommandée : Script d'installation

**Utilisez le script d'installation** pour configurer automatiquement les hooks :

**Linux/macOS :**
```bash
chmod +x .hooks/install.sh
./.hooks/install.sh
```

**Windows :**
```cmd
.hooks\install.bat
```

### Méthode manuelle : `git config core.hooksPath`

**Cette méthode est recommandée** car elle permet de versionner les hooks dans le dépôt Git :

```bash
# Configurer Git pour utiliser les hooks du répertoire .hooks
git config core.hooksPath .hooks

# Vérifier la configuration
git config core.hooksPath
# Devrait afficher: .hooks
```

**Avantages :**
- Les hooks sont versionnés dans le dépôt
- Tous les contributeurs utilisent les mêmes hooks
- Pas besoin de copier manuellement les fichiers
- Configuration partagée via Git

### Méthode alternative : Copie manuelle

Si vous préférez copier les hooks dans `.git/hooks/` :

```bash
# Rendre les hooks exécutables
chmod +x .hooks/pre-commit
chmod +x .hooks/post-commit

# Copier vers .git/hooks/
cp .hooks/pre-commit .git/hooks/pre-commit
cp .hooks/post-commit .git/hooks/post-commit
```

**Note :** Cette méthode n'est pas recommandée car les hooks ne sont pas versionnés et doivent être recopiés après chaque clonage.

## Vérification

Vérifiez que les hooks sont bien installés :

```bash
# Vérifier la configuration
git config core.hooksPath

# Tester les hooks manuellement
.hooks/pre-commit
.hooks/post-commit
```

## Désinstallation

Pour désactiver les hooks :

```bash
# Retirer la configuration
git config --unset core.hooksPath

# Ou utiliser les hooks par défaut
git config core.hooksPath .git/hooks
```

## Développement

### Ajouter un nouveau hook

1. Créez le fichier dans `.hooks/` (ex: `.hooks/pre-push`)
2. Rendez-le exécutable : `chmod +x .hooks/pre-push`
3. Documentez-le dans ce README

### Tests

Testez un hook manuellement :

```bash
# Test pre-commit
.hooks/pre-commit

# Test post-commit
.hooks/post-commit
```

## Extensions Futures

- `pre-push` : Tests avant push
- `commit-msg` : Validation du message de commit
- `post-merge` : Actions après merge
- `pre-rebase` : Vérifications avant rebase
