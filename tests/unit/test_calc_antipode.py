"""
Test module for calc_antipode.py

Tests the get_antipode() function and _identify_ocean() helper.
"""

# Used GenAI (Gemini-3-pro) to create test cases that aren't obvious to increase coverage, such as Timeout error, service error, International Date Line, and more.

import pytest
from unittest.mock import patch, MagicMock
from geospatial_toolkit.calc_antipode import get_antipode, _identify_ocean
from geopy.exc import GeocoderServiceError, GeocoderTimedOut


@pytest.fixture
def mock_geolocator():
    # Mock Nominatim geocoder to avoid real API calls.
    with patch("geospatial_toolkit.calc_antipode.Nominatim") as mock:
        yield mock.return_value


class TestGetAntipode:
    # Unit tests for get_antipode().

    def test_valid_tuple_coordinates(self, mock_geolocator):
        # Test valid coordinate tuple returns correct antipode.
        mock_geolocator.reverse.return_value = MagicMock(
            address="Kerguelen Islands, French Southern Territories"
        )
        coords, desc = get_antipode((49.2827, -123.1207))

        assert coords == (-49.2827, 56.8793)
        assert desc == "Kerguelen Islands, French Southern Territories"

    def test_north_pole_antipode(self, mock_geolocator):
        # Test North Pole (lat=90) returns South Pole.
        mock_geolocator.reverse.return_value = None
        coords, desc = get_antipode((90, 0))

        assert coords[0] == -90
        assert desc == "Southern(Antarctic) Ocean"

    def test_international_date_line(self, mock_geolocator):
        # Test longitude wrapping near date line (lon=179).
        mock_geolocator.reverse.return_value = None
        coords, _ = get_antipode((0, 179))

        assert coords == (0, -1)

    def test_invalid_input_type_raises_typeerror(self):
        # Test non-tuple/string input raises TypeError.
        with pytest.raises(TypeError) as exc:
            get_antipode([40.0, 100.0])
        assert "must be a string or tuple" in str(exc.value)

    def test_out_of_range_latitude_raises_valueerror(self):
        # Test latitude > 90 raises ValueError.
        with pytest.raises(ValueError) as exc:
            get_antipode((91, 0))
        assert "Latitude must be between -90 and 90" in str(exc.value)

    def test_string_location_success(self, mock_geolocator):
        # Test valid string location returns antipode and fallback ocean.
        # Mock geocode response for "Some Place" -> (10.0, 20.0)
        mock_geolocator.geocode.return_value = MagicMock(latitude=10.0, longitude=20.0)
        # Mock reverse response as None (Ocean)
        mock_geolocator.reverse.return_value = None

        coords, desc = get_antipode("Some Place")

        # Antipode calculation:
        # Lat: -10.0
        # Lon: 20.0 - 180 = -160.0
        assert coords == (-10.0, -160.0)

        # Ocean identification for (-10, -160) [Pacific is lon < -70]
        assert desc == "Pacific Ocean"

    def test_string_location_not_found(self, mock_geolocator):
        # Test geocode returns None raises ValueError.
        mock_geolocator.geocode.return_value = None
        with pytest.raises(ValueError):
            get_antipode("Nowhere Land")

    def test_geocode_service_error(self, mock_geolocator):
        # Test geocode raises GeocoderServiceError.
        mock_geolocator.geocode.side_effect = GeocoderServiceError("boom")
        with pytest.raises(ValueError):
            get_antipode("Error Place")

    def test_reverse_geocode_timeout(self, mock_geolocator):
        # Test reverse geocode timeout returns unknown description.
        mock_geolocator.reverse.side_effect = GeocoderTimedOut("timeout")
        # Use simple tuple input that is valid (0,0) -> Antipode (0, -180)
        coords, desc = get_antipode((0, 0))
        assert desc == "Unknown (geocoding service unavailable)"

    def test_tuple_wrong_length(self):
        # Test tuple with wrong length raises TypeError.
        with pytest.raises(TypeError):
            get_antipode((10,))

    def test_longitude_out_of_range(self):
        # Test longitude > 180 raises ValueError.
        with pytest.raises(ValueError):
            get_antipode((0, 181))


class TestIdentifyOcean:
    # Unit tests for _identify_ocean() - 5 major oceans.

    def test_pacific_ocean(self):
        # Eastern Pacific: (0, -120)
        assert _identify_ocean(0, -120) == "Pacific Ocean"

    def test_atlantic_ocean(self):
        # North Atlantic: (30, -40)
        assert _identify_ocean(30, -40) == "Atlantic Ocean"

    def test_indian_ocean(self):
        # Central Indian: (-20, 70)
        assert _identify_ocean(-20, 70) == "Indian Ocean"

    def test_arctic_ocean(self):
        # High Arctic: (80, 0)
        assert _identify_ocean(80, 0) == "Arctic Ocean"

    def test_southern_ocean(self):
        # Antarctic waters: (-65, 0)
        assert _identify_ocean(-65, 0) == "Southern(Antarctic) Ocean"
