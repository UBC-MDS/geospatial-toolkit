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

## [1.0.0] - (2026-01-17)

### Added

- **Core Functions Implementation**
  - `haversine_distance()`: Calculate great-circle distance between two geographic points
    - Supports km, miles, and meters output units
    - Comprehensive input validation for coordinates
  - `get_antipode()`: Find the diametrically opposite point on Earth
    - Supports both string (place names) and tuple (coordinates) inputs
    - Includes `_identify_ocean()` helper for ocean identification when reverse geocoding fails
    - Forward and reverse geocoding via geopy-Nominatim
  - `standardize_latlong()`: Convert coordinate formats to decimal degrees
    - Supports decimal degrees, DMS (degrees/minutes/seconds), and DDM (degrees/decimal minutes)
    - Handles N/S/E/W directional suffixes
  - `point_to_city()`: Identify which city polygon contains a coordinate
    - Point-in-polygon test using Shapely geometry
    - Requires pandas DataFrame with geometry and city_name columns

- **Test Suite**
  - `test_calc_antipode.py`: 15+ test cases for get_antipode function
    - Tests for GeocoderServiceError, GeocoderTimedOut exceptions
    - Edge cases for ocean identification and reverse geocoding
    - Coverage increased from 67.5% to 87.5%
  - `test_haversine_distance.py`: Tests for distance calculation accuracy
    - Input type validation tests
    - Coordinate range validation tests
  - `test_standardize_latlong.py`: Tests for coordinate parsing
    - Tests for all supported input formats
    - Out-of-range coordinate tests
  - `test_point-to-city.py`: Tests for point-in-polygon functionality
    - Tests with Vancouver and Burnaby polygons
    - None result tests for points outside all polygons

- **Dependencies**
  - Added `geopy>=2.4.0` for geocoding functionality
  - Added `shapely>=2.0.1` for geometric operations
  - Added `pandas>=2.0.0` for DataFrame support
  - Added `environment.yml` for conda environment setup

### Changed

- Renamed `point-to-city.py` to `point_to_city.py` (Python naming convention)
- Updated `pyproject.toml` with correct UBC-MDS organization URLs
- Enhanced docstrings with numpy-style documentation
- Added GenAI attribution comments to all function modules
- Removed `test_example.py` placeholder file

### Fixed

- Fixed project URLs in `pyproject.toml` (changed from PAT0216 to UBC-MDS)
- Added `_identify_ocean()` docstring clarification about approximate boundaries

