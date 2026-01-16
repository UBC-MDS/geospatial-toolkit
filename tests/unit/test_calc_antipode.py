"""
Test module for calc_antipode.py

Tests the get_antipode() function and _identify_ocean() helper.
"""

import pytest
from unittest.mock import patch, MagicMock
from geospatial_toolkit.calc_antipode import get_antipode, _identify_ocean


@pytest.fixture
def mock_geolocator():
    """Mock Nominatim geocoder to avoid real API calls."""
    with patch('geospatial_toolkit.calc_antipode.Nominatim') as mock:
        yield mock.return_value


class TestGetAntipode:
    """Unit tests for get_antipode() - 5 edge cases."""
    
    def test_valid_tuple_coordinates(self, mock_geolocator):
        """Test valid coordinate tuple returns correct antipode."""
        mock_geolocator.reverse.return_value = MagicMock(
            address="Kerguelen Islands, French Southern Territories"
        )
        coords, desc = get_antipode((49.2827, -123.1207))
        
        assert coords == (-49.2827, 56.8793)
        assert desc == "Kerguelen Islands, French Southern Territories"
    
    def test_north_pole_antipode(self, mock_geolocator):
        """Test North Pole (lat=90) returns South Pole."""
        mock_geolocator.reverse.return_value = None
        coords, desc = get_antipode((90, 0))
        
        assert coords[0] == -90
        assert desc == "Southern(Antarctic) Ocean"
    
    def test_international_date_line(self, mock_geolocator):
        """Test longitude wrapping near date line (lon=179)."""
        mock_geolocator.reverse.return_value = None
        coords, _ = get_antipode((0, 179))
        
        assert coords == (0, -1)
    
    def test_invalid_input_type_raises_typeerror(self):
        """Test non-tuple/string input raises TypeError."""
        with pytest.raises(TypeError) as exc:
            get_antipode([40.0, 100.0])
        assert "must be a string or tuple" in str(exc.value)
    
    def test_out_of_range_latitude_raises_valueerror(self):
        """Test latitude > 90 raises ValueError."""
        with pytest.raises(ValueError) as exc:
            get_antipode((91, 0))
        assert "Latitude must be between -90 and 90" in str(exc.value)


class TestIdentifyOcean:
    """Unit tests for _identify_ocean() - 5 major oceans."""
    
    def test_pacific_ocean(self):
        """Eastern Pacific: (0, -120)"""
        assert _identify_ocean(0, -120) == "Pacific Ocean"
    
    def test_atlantic_ocean(self):
        """North Atlantic: (30, -40)"""
        assert _identify_ocean(30, -40) == "Atlantic Ocean"
    
    def test_indian_ocean(self):
        """Central Indian: (-20, 70)"""
        assert _identify_ocean(-20, 70) == "Indian Ocean"
    
    def test_arctic_ocean(self):
        """High Arctic: (80, 0)"""
        assert _identify_ocean(80, 0) == "Arctic Ocean"
    
    def test_southern_ocean(self):
        """Antarctic waters: (-65, 0)"""
        assert _identify_ocean(-65, 0) == "Southern(Antarctic) Ocean"
