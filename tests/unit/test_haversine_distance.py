"""
Tests for the haversine_distance function.

Note: Google Gemini AI was used to suggest additional edge cases 
and validate the structure of these unit tests.
"""

import pytest
from geospatial_toolkit.distance import haversine_distance

def test_haversine_input_types():
    """
    Test that the function raises TypeError for non-tuple or non-numeric inputs.
    """
    # Test empty tuple
    with pytest.raises(ValueError, match="length 2"):
        haversine_distance((), (45.5, -73.5))

    # Test tuple with only 1 item
    with pytest.raises(ValueError, match="length 2"):
        haversine_distance((49.2,), (45.5, -73.5))
    
    # Test tuple with more than 2 items
    with pytest.raises(ValueError, match="length 2"):
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

def test_haversine_output_non_negative():
    """
    Test that the distance is always a positive number or zero.
    """
    vancouver = (49.2827, -123.1207)
    montreal = (45.5017, -73.5673)
    
    assert haversine_distance(vancouver, montreal) >= 0
    assert haversine_distance(vancouver, vancouver) == 0

def test_haversine_calculation_accuracy():
    """
    Test the mathematical accuracy of the function using known distances.
    """
    vancouver = (49.2827, -123.1207)
    montreal = (45.5017, -73.5673)
    
    assert haversine_distance(vancouver, montreal, unit='km') == pytest.approx(3684.41, abs=1)

def test_haversine_unit_conversion():
    """
    Test that switching units produces the correct relative values.
    """
    point_a = (45.0, -75.0)
    point_b = (46.0, -76.0)
    
    dist_km = haversine_distance(point_a, point_b, unit='km')
    dist_m = haversine_distance(point_a, point_b, unit='m')
    dist_miles = haversine_distance(point_a, point_b, unit='miles')
    
    assert dist_m == pytest.approx(dist_km * 1000, rel=1e-3)
    assert dist_miles == pytest.approx(dist_km * 0.621371, rel=1e-3)
