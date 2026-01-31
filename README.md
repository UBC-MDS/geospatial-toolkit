# Welcome to Geospatial Toolkit

|        |        |
|--------|--------|
| Package | [![Latest PyPI Version](https://img.shields.io/pypi/v/geospatial-toolkit.svg)](https://pypi.org/project/geospatial-toolkit/) [![Supported Python Versions](https://img.shields.io/pypi/pyversions/geospatial-toolkit.svg)](https://pypi.org/project/geospatial-toolkit/)  |
| Meta   | [![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md) |

## Project Summary

Geospatial Toolkit is a lightweight Python package designed to simplify and standardize common geospatial tasks. It provides small, modular utilities for coordinate standardization, distance calculations, and spatial search without requiring heavy GIS dependencies.

The toolkit is intended for GIS analysts, data scientists, students, and researchers who need reliable and easy-to-use functions for everyday spatial analysis and prototyping.

## Functions

- **standardize_latlong(lat, lon):** Converts latitude and longitude values from various common formats (e.g., decimal degrees, degrees minutes seconds) into a standardized decimal degree representation. The function validates coordinate ranges to ensure correctness before further analysis.

- **haversine_distance(origin, destination, unit='km'):** Calculates the great-circle distance between two geographic points using the haversine formula. Distances can be returned in kilometers, meters, or miles. Calculations are performed directly on latitude/longitude coordinates.

- **get_antipode(location, resolve_names=True):** Computes the antipodal point (the opposite location on Earth) for a given input location. The input may be a place name or a coordinate pair. Optionally performs reverse geocoding to return a human readable description of the antipode (e.g., land location or open ocean).

- **point_to_city(lat, lon, cities_df):** Determines which city polygon contains a given latitude/longitude coordinate using a point-in-polygon test. The function assumes all geometries are provided in geographic coordinates (EPSG:4326) and does not perform any projection or distance based calculations.

## Place in the Python Ecosystem

There are several existing Python packages for geospatial analysis, including:

- [`geopandas`](https://geopandas.org/): advanced GIS operations and geodataframes  
- [`shapely`](https://shapely.readthedocs.io/): geometric operations  
- [`pyproj`](https://pyproj4.github.io/): CRS transformations and projections
- [`geopy`](https://geopy.readthedocs.io/): geocoding and distance calculations
- [`haversine`](https://pypi.org/project/haversine/): distance calculations using the haversine formula
- [`astropy`](https://www.astropy.org/): astronomy and geospatial calculations

Among the four main functions in Geospatial Toolkit, some overlap with existing Python packages while others provide unique functionality. The `standardize_latlong` function partially overlaps with packages like `geopy` and `astropy`. The `haversine_distance` function has equivalents in the `haversine` package and `geopy.distance`. The `get_antipode` function is unique as it combines antipode calculation with optional reverse geocoding. This functionality not readily available in other packages. Finally, `point_to_city` partially overlaps with `geopandas` and `shapely` point-in-polygon operations, but is simplified.

## Get started

### Installation

You can install the latest version of the package from [TestPyPI](https://test.pypi.org/):

```bash
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ geospatial-toolkit
```

To use geospatial-toolkit in your code, start a Python session:

```bash
python
```

Then run:

```python
import geospatial_toolkit as gst
import pandas as pd
from shapely.geometry import Polygon

# 1. Standardize latitude and longitude
# 'd' stands for degree
gst.standardize_latlong('34d3\'8"N', '118d14\'37"W')

# 2. Calculate Great-Circle distance
point_a = (49.2827, -123.1207) # Vancouver
point_b = (45.5017, -73.5673)  # Montreal
gst.haversine_distance(point_a, point_b)

# 3. Get the antipode of a location
gst.get_antipode((49.2827, -123.1207))

# 4. Find which city contains a given point (using a reference DataFrame)
data = {
    'city_name': ['Vancouver', 'Port-aux-Français'],
    'geometry': [
        Polygon([(-124, 48), (-122, 48), (-122, 50), (-124, 50)]), 
        Polygon([(69, -50), (71, -50), (71, -48), (69, -48)])
    ]
}
cities_df = pd.DataFrame(data)

gst.point_to_city(49.2827, -123.1207, cities_df)
```

To exit the Python session:

```python
exit()
```

## Development Environment

### Prerequisites

- Python 3.11 or higher
- [Conda](https://docs.conda.io/en/latest/miniconda.html) or Mamba package manager

To set up the development environment, navigate to your local folder of choice and follow the instructions below

1. Clone the repository:

Using HTTPS:

```bash
git clone https://github.com/UBC-MDS/geospatial-toolkit.git
```

Or, using SSH:

```bash
git clone git@github.com:UBC-MDS/geospatial-toolkit.git
```

Navigate to the project root:

```bash
cd geospatial-toolkit
```

Create and activate the project Conda environment:

```bash
conda env create -f environment.yml
conda activate geospatial
```

Install the package in editable mode

```bash
pip install -e .
```

(Recommended) Install development dependencies

This project uses optional dependency groups for development, testing, documentation, and packaging.

Install all development-related dependencies with:

```bash
pip install -e ".[all]"
```

Alternatively, you can install specific groups:

```bash
pip install -e ".[dev]"
pip install -e ".[tests]"
pip install -e ".[docs]"
```

## Running Tests

To run the full test suite, ensure the development environment is activated and the package is installed in editable mode with testing dependencies.

In terminal, from the project root directory, run:

```bash
pytest
```

To run tests with coverage, run:

```bash
pytest --cov=geospatial_toolkit
```

## Building Documentation

This project uses quartodoc and Quarto to generate its documentation.

Note on Dependencies: Building the documentation requires `nbformat` to execute Python code blocks. This is included in the `environment.yml` file.

Ensure the development environment is activated and the package is installed in editable mode with documentation dependencies:

```bash
pip install -e ".[docs]"
```

Generate the API reference:

```bash
quartodoc build
```

Preview the site locally:

```bash
quarto preview
```

## Contributors

- Athul Sasidharan
- Prabuddha Tamhane
- Shrabanti Bala Joya
- Shreya Kakachery

## How to cite

If you use this package in coursework, reports, or research, please cite the GitHub repository:

Geospatial Toolkit contributors. (2026). *geospatial_toolkit* (Version 3.0.0) [Software]. GitHub. https://github.com/UBC-MDS/geospatial-toolkit

## Copyright

- Copyright © 2026 Athul, Bala, Prabuddha, Shreya.
- Free software distributed under the [MIT License](./LICENSE).

## Attribution

Gen AI tools (Google Gemini, OpenAI ChatGPT, and GitHub Copilot) were used to assist in the creation of this package, including code generation and documentation drafting. All generated content was reviewed and edited by the human authors to ensure accuracy and quality.
