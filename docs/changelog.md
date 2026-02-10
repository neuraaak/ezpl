# Changelog

Toutes les modifications notables de ce projet sont documentées ici.

Ce changelog est généré automatiquement à partir des [Conventional Commits](https://www.conventionalcommits.org/).

## [Unreleased](https://github.com/neuraaak/ezplog/compare/v1.5.3...HEAD)

### Features

- Ajouter des options pour le workflow de publication et améliorer les hooks de commit ([c7fdb17](https://github.com/neuraaak/ezplog/commit/c7fdb1795a5cdafc9bbc2a9f1aaa0aa20063c1c4))

### Corrections

- Update tag pattern in publish workflow and improve post-commit hook for tag creation ([fc3ff56](https://github.com/neuraaak/ezplog/commit/fc3ff56f33fba083cb54cc1f7f0d4a36ebc9bd6f))
- Update tag pattern in workflows to use "v\*-latest" for versioning ([a29d15a](https://github.com/neuraaak/ezplog/commit/a29d15a56fddb6ec944951cafdcb277fbe38c9eb))

### Maintenance

- Update project documentation and bump version to 1.5.3 ([3299396](https://github.com/neuraaak/ezplog/commit/32993968c6e36e2f0e7dfe23f466b02858ef5124))
- Updating workflows, hooks and doc ([924bf9c](https://github.com/neuraaak/ezplog/commit/924bf9c701a83afe4341f45cf3aa9260a16b0aa0))

## [1.5.3](https://github.com/neuraaak/ezplog/releases/tag/v1.5.3) — 2026-02-10

### Corrections

- Update tag pattern in publish workflow and improve post-commit hook for tag creation ([1764da1](https://github.com/neuraaak/ezplog/commit/1764da192d7b33a52748b9e68b3dc3948bb1963b))

## [1.5.2](https://github.com/neuraaak/ezplog/releases/tag/v1.5.2) — 2026-02-09

### Corrections

- Ajouter l'exclusion de la sortie de build MkDocs ([d48f904](https://github.com/neuraaak/ezplog/commit/d48f90492e72def07a99bdc24bf295ed792b3fc8))
- Add missing type annotations for griffe validation ([32e256a](https://github.com/neuraaak/ezplog/commit/32e256a57cef2a3170579b7803b70776bab694aa))

## [1.5.1](https://github.com/neuraaak/ezplog/releases/tag/v1.5.1) — 2026-02-08

### Features

- Personalize build message to include project name ([c7286e3](https://github.com/neuraaak/ezplog/commit/c7286e3af205d2429fd7ba35ce27e9ed363972ef))
- Add level protection mechanisms and level property accessors ([4c8a76d](https://github.com/neuraaak/ezplog/commit/4c8a76d756e0b32e7eb6c9c4a527db970a486ae6))

### Corrections

- Improve main branch reference handling and add debug info for tag verification ([d1f0a45](https://github.com/neuraaak/ezplog/commit/d1f0a45d9d4cee5e4db2781d490f3ddd12826555))

## [1.5.0](https://github.com/neuraaak/ezplog/releases/tag/v1.5.0) — 2026-01-31

### Refactoring

- Major architectural cleanup for v1.5.0 ([2c79fb9](https://github.com/neuraaak/ezplog/commit/2c79fb9f23e66da197c9f1c29465d9261bf85ac0))

## [1.4.3](https://github.com/neuraaak/ezplog/releases/tag/v1.4.3) — 2026-01-26

### Corrections

- Correct package name in installation verification step of GitHub Actions workflow ([1a5068c](https://github.com/neuraaak/ezplog/commit/1a5068c5e7b0a82055b13ec1020d9196350be11e))

### Maintenance

- Update .gitignore and pre-commit configuration for improved file management ([f6c5ac1](https://github.com/neuraaak/ezplog/commit/f6c5ac1fe58e7f873f59d31befe6b01f837af97e))
- Replaced mypy with ty and pyright ([a549394](https://github.com/neuraaak/ezplog/commit/a549394890ed11a88d645c8c4502f8eccd8e8933))

## [1.4.2](https://github.com/neuraaak/ezplog/releases/tag/v1.4.2) — 2026-01-25

### Maintenance

- Simplify package installation verification in GitHub Actions workflow ([d389a1d](https://github.com/neuraaak/ezplog/commit/d389a1d9a0975125ac8bebcac78845ce929e805a))
- Remove linting step from GitHub Actions workflow ([7554bd7](https://github.com/neuraaak/ezplog/commit/7554bd73d915ec4df444ba4bcbe87e5a39bdb43f))
- Update requirements and improve GitHub Actions workflow ([374e290](https://github.com/neuraaak/ezplog/commit/374e2906ca0fa8e977c37dea93f1d03bbc696329))
- Bump version to 1.4.2 ([ed37c95](https://github.com/neuraaak/ezplog/commit/ed37c95575127e9060c7539137d5122ab92916f8))

## [1.4.1](https://github.com/neuraaak/ezplog/releases/tag/v1.4.1) — 2026-01-25

### Maintenance

- Add development requirements and update GitHub Actions workflow ([f90f62e](https://github.com/neuraaak/ezplog/commit/f90f62eb7ccdcf8047cec0c4131e29c0da318435))

## [1.4.0](https://github.com/neuraaak/ezplog/releases/tag/v1.4.0) — 2026-01-18

### Maintenance

- Update json printing + setting github actions + cleaned ruff warnings in tests ([d5bea2b](https://github.com/neuraaak/ezplog/commit/d5bea2bd705f7ab8d3c0fc47204ca0b5a94248a9))

## [1.3.0](https://github.com/neuraaak/ezplog/releases/tag/v1.3.0) — 2026-01-08

### Maintenance

- Added printer/logger customization methods ([5a8d180](https://github.com/neuraaak/ezplog/commit/5a8d180c8e899383d48b906929d7c5c551600a3b))

## [1.2.1](https://github.com/neuraaak/ezplog/releases/tag/v1.2.1) — 2026-01-05

### Corrections

- Update PyPI badge in README.md to reflect correct project name ([c0a2906](https://github.com/neuraaak/ezplog/commit/c0a29062d873fc99a9d92d9ee81d0bcd963a53ee))

### Maintenance

- Update .gitignore to exclude temporary files ([49569d1](https://github.com/neuraaak/ezplog/commit/49569d1d977125a06774c70c341fd9e860e96cb0))
- Bump version to 1.2.1 and update project URLs ([4f84679](https://github.com/neuraaak/ezplog/commit/4f84679d4d49390b3905da6b38ee447240797498))

## [1.2.0](https://github.com/neuraaak/ezplog/releases/tag/v1.2.0) — 2025-12-23

### Maintenance

- Rename project from ezpl to ezplog in pyproject.toml ([99b01f0](https://github.com/neuraaak/ezplog/commit/99b01f0170f5114e29c4a50c92f825755c350c7d))
- Bump version to 1.2.0 and update configuration ([5ec5c8b](https://github.com/neuraaak/ezplog/commit/5ec5c8b02e6c50525ab8bc53d9b227de80656faf))

## [1.1.4](https://github.com/neuraaak/ezplog/releases/tag/v1.1.4) — 2025-12-16

### Maintenance

- Update Python compatibility and documentation ([c233e72](https://github.com/neuraaak/ezplog/commit/c233e720c5cdba9e25a86f41a4415d0e08b7f14b))
- Bump version to 1.1.4 and update related documentation ([4b82c43](https://github.com/neuraaak/ezplog/commit/4b82c43a53b6c69fa68c00c65410cc3179f28972))

## [1.1.3](https://github.com/neuraaak/ezplog/releases/tag/v1.1.3) — 2025-12-15

### Corrections

- Enhance logger management to prevent duplicate handlers ([d59d1be](https://github.com/neuraaak/ezplog/commit/d59d1bec6d247b52868446a99091826997e0f32a))

### Maintenance

- Bump version to 1.1.3 and update related documentation ([450f61b](https://github.com/neuraaak/ezplog/commit/450f61b1560a71235890c6ba7d9252daa79ae908))

## [1.1.2](https://github.com/neuraaak/ezplog/releases/tag/v1.1.2) — 2025-12-15

### Corrections

- Streamline type hints in progress.py ([82d8bf0](https://github.com/neuraaak/ezplog/commit/82d8bf0a8a5dcd7bf21f0b51b6551f9829ff5134))

### Maintenance

- Update version to 1.1.2 and change development status ([5da8d25](https://github.com/neuraaak/ezplog/commit/5da8d25d985fc7cd8ad3fe081d8e6b7ce0c92430))
- Minor enhancements - v1.1.1 ([648a472](https://github.com/neuraaak/ezplog/commit/648a4728b72aa139d7022da9f19be43b6725af08))

## [1.1.0](https://github.com/neuraaak/ezplog/releases/tag/v1.1.0) — 2025-12-13

### Features

- Add comprehensive documentation, test suite, and development tooling - v1.1.0 ([e4d78d8](https://github.com/neuraaak/ezplog/commit/e4d78d836d38d51be3044a79e27c3b3b34f7f8e6))

---

_Généré automatiquement par [git-cliff](https://git-cliff.org/)_
