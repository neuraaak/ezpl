# 📦 GitHub Actions Workflow - Publish to PyPI

## Overview

The `publish-pypi.yml` workflow automatically publishes the **ezplog** package to PyPI with strict validations to ensure quality and security of publications.

## 🎯 Triggers

The workflow can be triggered in two ways:

### 1. Automatically (Tag push on main)
```bash
git checkout main
git tag v1.4.0
git push origin v1.4.0
```
- Triggers when a tag matching `v*.*.*` format is pushed (e.g., v1.4.0, v2.0.1)
- **⚠️ IMPORTANT**: The tag must point to a commit on the `main` branch
- If the tag is on another branch, the workflow will fail and no publication will occur
- Publishes **automatically to PyPI production** after validation

### 2. Manually (Workflow Dispatch)
- From GitHub interface: Actions → Publish to PyPI → Run workflow
- `skip_tests` option available (not recommended)
- Main branch check is ignored in manual mode
- Publishes directly to PyPI production

## 🔄 Workflow Architecture

The workflow is divided into **two jobs** for better separation of responsibilities:

### Job `validate` - Validation and Tests

1. **Checkout code** - Retrieves source code with all tags and branches
2. **Set up Python** - Installs Python 3.11 with pip cache
3. **Fetch all branches and tags** - Fetches all remote branches and tags
4. **Extract version from tag** - Extracts version from Git tag
5. **Extract version from pyproject.toml** - Extracts version from `pyproject.toml`
6. **Check version consistency** - Verifies that versions match
7. **Check if tag is on main branch** - ⚠️ **Verifies that the tag is on the main branch**
8. **Install dependencies** - Installs development dependencies
9. **Run linting** - Runs `ruff check`, `ruff format --check`, and `mypy`
10. **Run tests** - Runs complete test suite with `pytest`

### Job `publish` - Build and Publication

The `publish` job only runs **if**:
- ✅ Version validation succeeded
- ✅ Tag is on main branch (or manual trigger)
- ✅ Tests and linting succeeded (unless `skip_tests=true`)

Steps:
1. **Checkout code** - Retrieves source code
2. **Set up Python** - Installs Python 3.11 with pip cache
3. **Clean previous builds** - Cleans previous build artifacts
4. **Install build dependencies** - Installs `build` and `twine`
5. **Build package** - Builds the package (.whl and .tar.gz)
6. **Check package** - Validates package with `twine check`
7. **Verify package installation** - Tests package installation and import
8. **Publish to PyPI** - Publishes to PyPI production
9. **Show publish info** - Displays publication information

## 🔐 Required Secret

You must configure the following secret in your GitHub repository settings:

### For PyPI Production
1. Create an account on https://pypi.org
2. Generate an API token in Account Settings
3. Add the `PYPI_API_TOKEN` secret in GitHub

**Secret configuration:**
```
GitHub Repository → Settings → Secrets and variables → Actions → New repository secret
```

## 📋 Usage

### Production publication (PyPI)

**Method 1: Via tag on main (recommended)**
```bash
# Make sure you're on main
git checkout main
git pull origin main

# Update version in pyproject.toml
# (or use the update_version.py script)

# Create and push the tag
git tag v1.4.0
git push origin v1.4.0
```

**⚠️ Important**: If you create a tag on another branch, the workflow will trigger but fail at the main branch check step. No publication will occur.

**Method 2: Via GitHub interface**
1. Go to Actions
2. Select "Publish to PyPI"
3. Click "Run workflow"
4. Select the branch (usually `main`)
5. Optionally, check `skip_tests` (not recommended)
6. Click "Run workflow"

**Method 3: Via gh CLI**
```bash
gh workflow run publish-pypi.yml
```

## ✅ Validations Performed

The workflow performs several validations before publication:

### 1. Version Validation
- ✅ Verifies that the tag version matches the one in `pyproject.toml`
- ✅ Fails if versions don't match

### 2. Branch Validation
- ✅ Verifies that the tag points to a commit on the `main` branch
- ✅ Uses `git branch --contains` and `git merge-base --is-ancestor`
- ✅ Fails if the tag is on another branch
- ⚠️ Ignored in `workflow_dispatch` mode (manual publication)

### 3. Quality Validation
- ✅ Linting with `ruff check` and `ruff format --check`
- ✅ Type checking with `mypy`
- ✅ Complete test suite execution

### 4. Package Validation
- ✅ Package validity check with `twine check`
- ✅ Package installation test
- ✅ Verifies that the package can be imported

## ✅ Post-Publication Verification

After publication, the workflow displays:
- ✅ Success status
- 📦 Package name (ezplog)
- 🏷️ Published version
- 🔗 Package URL on PyPI
- 📋 Direct link to the published version

## 🚀 Complete Release Workflow

1. **Development**: Work on your feature branch
2. **Local tests**: Ensure all tests pass locally
3. **Merge to main**: Merge your branch into `main`
4. **Local test**: Use `.scripts/build/upload_to_pypi.py test` to test on Test PyPI
5. **Version update**: 
   - Modify version in `ezpl/__init__.py`
   - Run `python .scripts/dev/update_version.py` to synchronize
   - Or modify `pyproject.toml` directly
6. **Commit & Push**: Commit and push changes to `main`
7. **Tag & Push**: Create and push the tag from `main` for production publication
   ```bash
   git checkout main
   git pull origin main
   git tag v1.4.0
   git push origin v1.4.0
   ```
8. **Verification**: Check on https://pypi.org/project/ezplog/

## 🧪 Pre-Publication Testing

To test your package before publishing to PyPI, use the local script:

```bash
# Build the package
python .scripts/build/build_package.py build

# Check the package
python .scripts/build/build_package.py check

# Test on Test PyPI (via local script)
python .scripts/build/upload_to_pypi.py test

# Publish to PyPI production (via GitHub workflow or local script)
python .scripts/build/upload_to_pypi.py prod
```

## 🚨 Security and Protection

### Protection against accidental publications

The workflow includes several protections:

1. **Tag on main only**: Only tags on `main` trigger automatic publication
2. **Version validation**: Tag version must match `pyproject.toml`
3. **Mandatory tests**: Tests must pass (except in manual mode with `skip_tests=true`)
4. **Mandatory linting**: Code must conform to standards
5. **Installation verification**: Package must be installable and importable

### Protection scenarios

**Scenario 1: Tag on feature branch**
```bash
git checkout feature-branch
git tag v1.5.0
git push origin v1.5.0
```
→ ❌ Workflow fails: "Tag is NOT on main branch"
→ ✅ No publication on PyPI

**Scenario 2: Tag on main**
```bash
git checkout main
git tag v1.5.0
git push origin v1.5.0
```
→ ✅ Workflow succeeds
→ ✅ Publication on PyPI

**Scenario 3: Inconsistent version**
```bash
# pyproject.toml contains version = "1.4.0"
git tag v1.5.0
git push origin v1.5.0
```
→ ❌ Workflow fails: "Version mismatch"
→ ✅ No publication on PyPI

## 📝 Important Notes

- The workflow does NOT build the package locally before push
- Build is done in the GitHub Actions environment
- Distribution files are NOT committed to the repository
- Make sure the version in `pyproject.toml` is up to date before publication
- Once published on PyPI, a package CANNOT be deleted (only "yanked")
- **Important**: Always test on Test PyPI with the local script before publishing to production
- **Security**: Only tags on `main` trigger automatic publication
- **Tests**: Tests are automatically executed before publication (unless `skip_tests=true`)

## 🔧 Troubleshooting

### Workflow fails with "Tag is NOT on main branch"

**Cause**: The tag was created on a branch other than `main`.

**Solution**:
1. Check which branch you're on: `git branch`
2. If necessary, merge your branch into `main`
3. Create the tag from `main`:
   ```bash
   git checkout main
   git pull origin main
   git tag v1.4.0
   git push origin v1.4.0
   ```

### Workflow fails with "Version mismatch"

**Cause**: The tag version doesn't match the one in `pyproject.toml`.

**Solution**:
1. Check the version in `pyproject.toml`
2. Use the synchronization script:
   ```bash
   python .scripts/dev/update_version.py
   ```
3. Or manually modify `pyproject.toml` to match the tag
4. Commit and push the changes
5. Recreate the tag if necessary

### Tests fail

**Cause**: Tests are failing in the test suite.

**Solution**:
1. Run tests locally: `pytest tests/`
2. Fix identified issues
3. Commit and push corrections
4. Rerun the workflow
