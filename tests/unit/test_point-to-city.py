"""
Tests for the point-to-city function.

Note: ChatGPT was used to suggest additional edge cases, 
validate the structure and confirm the usecases of these unit tests.
"""

import pandas as pd
import pytest
from shapely.geometry import Polygon

from geospatial_toolkit.point_to_city import point_to_city

@pytest.fixture
def cities_df():
    """
    Create a simple cities DataFrame for unit testing.

    Using two adjacent square polygons (EPSG:4326 style lat/lon values):
      - Vancouver: lon [-124, -123], lat [49, 50]
      - Burnaby:   lon [-123, -122], lat [49, 50]
    """

    vancouver_poly = Polygon( [(-124, 49), (-123, 49), (-123, 50), (-124, 50)] )

    burnaby_poly = Polygon( [(-123, 49), (-122, 49), (-122, 50), (-123, 50)] )

    return pd.DataFrame(
        {
            "city_name": ["Vancouver", "Burnaby"],
            "geometry": [vancouver_poly, burnaby_poly],
        }
    )



def test_point_inside_vancouver_returns_vancouver(cities_df):
    lat, lon = 49.5, -123.5
    assert point_to_city(lat, lon, cities_df) == "Vancouver"


def test_point_inside_burnaby_returns_burnaby(cities_df):
    lat, lon = 49.6, -122.5
    assert point_to_city(lat, lon, cities_df) == "Burnaby"


def test_point_outside_all_polygons_returns_none(cities_df):
    lat, lon = 48.5, -123.5
    assert point_to_city(lat, lon, cities_df) is None


def test_point_on_boundary_returns_none(cities_df):
    """
    Point lies exactly on the shared boundary between the two polygons.
    With shapely `contains()` function, we consider boundary points are NOT included inside,
    so the expected result will be None for boundary points.
    """
    lat, lon = 49.5, -123.0
    assert point_to_city(lat, lon, cities_df) is None


def test_missing_required_columns_raises_keyerror(cities_df):
    """
    cities_df must contain both 'geometry' and 'city_name' as columns.
    """
    bad_df = cities_df.drop(columns=["city_name"])
    with pytest.raises(KeyError):
        point_to_city(49.5, -123.5, bad_df)


def test_non_numeric_lat_lon_raises_typeerror(cities_df):
    """
    lat/lon must be numeric. Strings should raise TypeError.
    """
    with pytest.raises(TypeError):
        point_to_city("49.5", -123.5, cities_df)

    with pytest.raises(TypeError):
        point_to_city(49.5, "-123.5", cities_df)

