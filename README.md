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

You can install this package into your preferred Python environment using pip:

```bash
pip install geospatial-toolkit
```

To use geospatial-toolkit in your code:

```python
import geospatial_toolkit as gst
gst.standardize_latlong("34°3'8\"N", "118°14'37\"W")
```
## Development Environment

To set up the development environment, navigate to your local folder of choice and follow the instructions below

1. Clone the repository:

Using HTTPS:
```
git clone https://github.com/UBC-MDS/geospatial-toolkit.git
```

Or, using SSH:
```
git clone git@github.com:UBC-MDS/geospatial-toolkit.git
```

Navigate to the project root:
```
cd geospatial-toolkit
```

2. Create project Conda environment:
```
conda env create -f environment.yml
```

3. Activate the Conda environment:
```
conda activate geospatial
```

4. Install the package in editable mode
```
pip install -e .
```

## Running Tests

To run the full test suite, ensure the development environment is activated and the package is installed in editable mode.

In terminal, from the project root directory, run: 
```
pytest
```
To run tests with coverage, run:
```
pytest --cov=geospatial_toolkit
```

## Developer Guide: Building Documentation

1. Install the package in editable mode: `pip install -e .`
2. Generate the API reference: `PYTHONPATH=src quartodoc build`
3. Preview the site locally: `quarto preview`

## Contributors
- Athul Sasidharan
- Prabuddha Tamhane
- Shrabanti Bala Joya
- Shreya Kakachery

## Copyright

- Copyright © 2026 Athul, Bala, Prabuddha, Shreya.
- Free software distributed under the [MIT License](./LICENSE).

## Atribution

Gen AI tools were used to assist in the creation of this package, including code generation and documentation drafting. All generated content was reviewed and edited by the human authors to ensure accuracy and quality.

