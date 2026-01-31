# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.0.0] - (2026-02-02)

### Peer Review Feedback

Addressed the following Peer/TA Feedback:

- <add_feedback_here>

### Added

- Added tutorial page (`tutorial.qmd`) and environment packages for rendering Python code
- Added retrospective documentation with team metrics sections and charts
- Added hatch-vcs for dynamic versioning from git tags
- Added Netlify deployment for PR preview builds

### Changed

- Switched documentation deployment to GitHub Actions Pages
- Added Python session startup instructions and replaced the degree symbol with `d` in latlong instructions

### Removed

- Deleted `.github/dependabot.yml` configuration

### Fixed

- Fixed Attribution typo and documented GenAI tools used

## [2.0.0] - (2026-01-25)

### Added

- CI/CD integration via GitHub Workflows
  - `build.yml` for continuous integration with multi-Python version testing
  - `deploy.yml` for Test PyPI deployment
  - `docs.yml` for documentation generation
  - `publish.yml` for package publishing
  - `release.yml` for release automation
- Quartodoc-based documentation system with Quarto rendering
  - `_quarto.yml` configuration file
  - Reference documentation pages for all four functions
  - `index.qmd` landing page
- Package namespace imports in `__init__.py` for direct function access
- Comprehensive package description docstring in `__init__.py`
- `__all__` export list defining public API

### Changed

- Migrated documentation from Sphinx to Quartodoc
- Replaced sphinx dependencies with `quartodoc>=0.7.0` and `griffe>=0.40.0`
- Updated `pyproject.toml` with expanded optional dependencies:
  - `dev`: hatch, pre-commit, ruff, black, quartodoc
  - `docs`: quartodoc
  - `build`: pip-audit, twine
  - `tests`: pytest, pytest-cov, pytest-raises, pytest-randomly, pytest-xdist
  - `all`: combined all optional dependencies
- Enhanced README.md with:
  - Developer setup instructions
  - Testing and documentation build instructions
  - Demo installation commands with developer dependencies
  - Function usage examples
- Reformatted all Python files with Black code formatter
- Replaced degree symbol (`°`) with `d` in `standardize_latlong()` docstring and regex patterns for better cross-platform compatibility
- Updated tests to account for degree symbol replacement in latlong module
- Added TypeError handling for non-numeric inputs across all functions
- Enhanced test coverage with additional edge case tests

### Fixed

- Fixed Quarto build issues by converting `latlong.qmd` to UTF-8 encoding
- Fixed CI workflow by adding Quarto setup action
- Fixed CD workflow to use direct build commands instead of hatch environment
- Fixed typo in latlong function