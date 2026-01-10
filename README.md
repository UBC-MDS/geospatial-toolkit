# Welcome to Geospatial Toolkit

|        |        |
|--------|--------|
| Package | [![Latest PyPI Version](https://img.shields.io/pypi/v/geospatial-toolkit.svg)](https://pypi.org/project/geospatial-toolkit/) [![Supported Python Versions](https://img.shields.io/pypi/pyversions/geospatial-toolkit.svg)](https://pypi.org/project/geospatial-toolkit/)  |
| Meta   | [![Code of Conduct](https://img.shields.io/badge/Contributor%20Covenant-v2.0%20adopted-ff69b4.svg)](CODE_OF_CONDUCT.md) |

*TODO: the above badges that indicate python version and package version will only work if your package is on PyPI.
If you don't plan to publish to PyPI, you can remove them.*

## Project Summary
Geospatial Toolkit is a Python package designed to simplify and standardize common geospatial tasks. It provides utilities for handling latitude/longitude data, distance calculations, and basic geospatial visualizations. The toolkit is intended for GIS analysts, data scientists, students and researchers who need reliable and simple tools for spatial data analysis.


## Functions

- **standardize_latlong(lat, long)**: Converts latitude and longitude from various formats (degrees minutes seconds, decimal degrees) to a standardized decimal degree format.

- **haversine_distance(coord1, coord2)**: Calculates the great-circle distance between two points on the Earth's surface given their latitude and longitude using the Haversine formula.

## Place in the Python Ecosystem
There are several existing Python packages for geospatial analysis, including:

- [`geopandas`](https://geopandas.org/): advanced GIS operations and geodataframes  
- [`shapely`](https://shapely.readthedocs.io/): geometric operations  
- [`pyproj`](https://pyproj4.github.io/): CRS transformations and projections  

The Geospatial Toolkit complements these by offering small, modular functions for everyday tasks in geospatial analysis. For instance, `standardize_latlong` simplifies input standardization before further analysis.

## Get started

You can install this package into your preferred Python environment using pip:

```bash
$ pip install geospatial-toolkit
```

To use geospatial-toolkit in your code:

```python
>>> import geospatial-toolkit as gst
>>> geospatial-toolkit.standardize_latlong("34°3'8\"N", "118°14'37\"W")
(34.0522, -118.2436)
```

## Contributors
- Athul Sasidharan
- Prabuddha Tamhane
- Shrabanti Bala Joya
- Shreya Kakachery

## Copyright

- Copyright © 2026 Athul, Bala, Prabuddha, Shreya.
- Free software distributed under the [MIT License](./LICENSE).
