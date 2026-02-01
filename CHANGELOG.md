# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [3.0.0] - (2026-02-02)

### Added
- Added a full user installation guide and expanded README setup instructions. (PR #102)
- Added “How to cite” guidance in the README. (PR #96)
- Added contributor names/emails to `pyproject.toml`. (PR #96)
- Added a contributors section to `CONDUCT.md`. (PR #96)
- Added retrospective documentation content (charts/metrics + sections). (PR #92)
- Added `hatch-vcs` for dynamic versioning from Git tags. (PR #76)
- Added Netlify deployment for PR preview builds. (PR #78)

### Changed
- Updated README examples and formatting, including fixing escape characters in the `standardize_latlong` example. (PR #102)
- Updated installation link / TestPyPI install instructions in README. (PR #102)
- Added/clarified the `d` notation in latitude/longitude instructions and demo notes. (PR #94, PR #102)
- Updated harassment reporting email in the Code of Conduct. (PR #96)

### Removed
- Removed `.github/dependabot.yml`. (PR #91)

### Fixed
- Fixed TOML/dependency issues that were causing docs/build workflow failures. (PR #97)

### Peer Review Feedback

Addressed the following Peer/TA Feedback:

- Feedback : Add how to cite section (maybe in contributing? please look up other matured repos) (Norton's review)
- Updated : Added cite section to the README file and added contents. 

- Feedback : Add link to documentation website (Norton's review)
- Update: Added the link as instructed. 

- Feedback : Add a small data frame in demo (Mara's review)
- Update : Added, verified and test the data frame along with the functions in demo.

- Feedback : Update latlong function demo (Based on Limor and Mara's reviews) 
- Update : Updated, added dataframes, tested and verified the contents.

- Feedback : Align Python versions across workflows - Different workflows use different Python versions (3.10 vs 3.11 vs 3.13) in CI, docs, and release workflows. (Limor's review, also good to keep things consistent) 
- Update : Changed the versioning to semantic, so automatically updates the versions. 

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

## [0.0.1] - (2026-01-10)

### Added

- **Initial Project Structure**
  - Created project from copier template
  - Set up `pyproject.toml` with hatchling build system
  - MIT License
  - Basic `README.md` with project description and function specifications

- **Function Specifications (Docstrings Only)**
  - `haversine_distance`: Initial docstring for great-circle distance calculation
  - `get_antipode`: Initial docstring for antipode calculation
  - `standardize_latlong`: Initial docstring for coordinate format conversion
  - `point-to-city`: Initial docstring for point-in-polygon city lookup

- **Documentation**
  - `CODE_OF_CONDUCT.md` renamed to `CONDUCT.md` with updated content
  - `CONTRIBUTING.md` with contribution guidelines and GenAI attribution requirements

### Changed

- Updated `README.md` with function descriptions and attributions

### Removed

- Removed `example.py` placeholder script

---
