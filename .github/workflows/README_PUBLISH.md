# 📦 Workflow GitHub Actions - Publish to PyPI

## Vue d'ensemble

Le workflow `publish-pypi.yml` permet de publier automatiquement le package **ezplog** sur PyPI.

## 🎯 Déclencheurs

Le workflow peut être déclenché de deux façons :

### 1. Automatiquement (Push de tag)
```bash
git tag v1.4.0
git push origin v1.4.0
```
- Se déclenche quand un tag au format `v*.*.*` est poussé (ex: v1.4.0, v2.0.1)
- Publie **automatiquement sur PyPI production**

### 2. Manuellement (Workflow Dispatch)
- Depuis l'interface GitHub : Actions → Publish to PyPI → Run workflow
- Publie directement sur PyPI production

## 🔄 Étapes du Workflow

1. **Checkout code** - Récupère le code source
2. **Set up Python** - Installe Python 3.11
3. **Install build dependencies** - Installe `build` et `twine`
4. **Build package** - Construit le package (.whl et .tar.gz)
5. **Check package** - Vérifie la validité du package
6. **Publish to PyPI** - Publie sur PyPI production
7. **Show publish info** - Affiche les informations de publication

## 🔐 Secret Requis

Vous devez configurer le secret suivant dans les paramètres GitHub du repository :

### Pour PyPI Production
1. Créez un compte sur https://pypi.org
2. Générez un API token dans Account Settings
3. Ajoutez le secret `PYPI_API_TOKEN` dans GitHub

**Configuration du secret :**
```
GitHub Repository → Settings → Secrets and variables → Actions → New repository secret
```

## 📋 Utilisation

### Publication production (PyPI)

**Méthode 1: Via tag (recommandé)**
```bash
git tag v1.4.0
git push origin v1.4.0
```

**Méthode 2: Via l'interface GitHub**
1. Allez dans Actions
2. Sélectionnez "Publish to PyPI"
3. Cliquez sur "Run workflow"
4. Sélectionnez la branche
5. Cliquez sur "Run workflow"

**Méthode 3: Via gh CLI**
```bash
gh workflow run publish-pypi.yml
```

## ✅ Vérification

Après publication, le workflow affiche :
- ✅ Status de succès
- 📦 Nom du package (ezplog)
- 🏷️ Version publiée
- 🔗 URL du package sur PyPI

## 🚀 Workflow de Release Complet

1. **Développement** : Travaillez sur votre branche
2. **Tests** : Assurez-vous que tous les tests passent
3. **Test local** : Utilisez `.scripts/build/upload_to_pypi.py test` pour tester sur Test PyPI
4. **Mise à jour version** : Modifiez la version dans `pyproject.toml`
5. **Commit & Push** : Commitez les changements
6. **Tag & Push** : Créez et poussez le tag pour publication production
7. **Vérification** : Vérifiez sur https://pypi.org/project/ezplog/

## 🧪 Tests avant Publication

Pour tester votre package avant la publication sur PyPI, utilisez le script local :

```bash
# Construire le package
python .scripts/build/build_package.py build

# Vérifier le package
python .scripts/build/build_package.py check

# Tester sur Test PyPI (via script local)
python .scripts/build/upload_to_pypi.py test

# Publier sur PyPI production (via workflow GitHub ou script local)
python .scripts/build/upload_to_pypi.py prod
```

## 📝 Notes Importantes

- Le workflow ne construit PAS le package localement avant le push
- Le build est fait dans l'environnement GitHub Actions
- Les fichiers de distribution ne sont PAS commités dans le repository
- Assurez-vous que la version dans `pyproject.toml` est à jour avant la publication
- Une fois publié sur PyPI, un package ne peut PAS être supprimé (seulement "yanked")
- **Important** : Testez toujours sur Test PyPI avec le script local avant de publier en production
