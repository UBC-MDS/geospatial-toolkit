import pytest
from geospatial_toolkit.distance import haversine_distance

def test_haversine_input_types():
    """
    Test that the function raises TypeError for non-tuple or non-numeric inputs.
    """
    # Test empty tuple
    with pytest.raises(TypeError, match="length 2"):
        haversine_distance((), (45.5, -73.5))

    # Test tuple with only 1 item
    with pytest.raises(TypeError, match="length 2"):
        haversine_distance((49.2,), (45.5, -73.5))
    
    # Test tuple with more than 2 items
    with pytest.raises(TypeError, match="length 2"):
        haversine_distance((49.2, -123.1, 500), (45.5, -73.5))

    # Test non-tuple input
    with pytest.raises(TypeError):
        haversine_distance([49.2, -123.1], (45.5, -73.5))
    
    # Test non-numeric values inside the tuple
    with pytest.raises(TypeError):
        haversine_distance(("string", -123.1), (45.5, -73.5))

def test_haversine_input_ranges():
    """
    Test that the function raises ValueError for coordinates outside Earth's bounds.
    """
    # Latitude > 90
    with pytest.raises(ValueError, match="latitude"):
        haversine_distance((91, 0), (0, 0))
    
    # Longitude < -180
    with pytest.raises(ValueError, match="longitude"):
        haversine_distance((0, -181), (0, 0))

def test_haversine_invalid_units():
    """
    Test that the function raises ValueError for unsupported distance units.
    """
    with pytest.raises(ValueError):
         haversine_distance((0, 0), (1, 1), unit='lightyears')
