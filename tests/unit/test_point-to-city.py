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







