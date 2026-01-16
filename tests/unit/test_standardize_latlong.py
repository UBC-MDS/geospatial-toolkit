import pytest
from geospatial_toolkit.latlong import standardize_latlong  

# Test decimal degree inputs (floats and strings)

@pytest.mark.parametrize("lat, lon, expected", [
    (34.0522, -118.2437, (34.0522, -118.2437)),
    ("34.0522", "-118.2437", (34.0522, -118.2437)),
    (90.0, 180.0, (90.0, 180.0)),
    (-90.0, -180.0, (-90.0, -180.0)),
])
def test_standardize_latlong_decimal_degrees(lat, lon, expected):
    """
    Test that decimal degree inputs are returned correctly.
    """
    assert standardize_latlong(lat, lon) == expected

# Test degrees, minutes, seconds (DMS) inputs

@pytest.mark.parametrize("lat, lon, expected", [
    ("34°3'8\"N", "118°14'37\"W", (34.052222, -118.243611)),
    ("34°3'8\"S", "118°14'37\"E", (-34.052222, 118.243611)),
    ("0°0'0\"N", "0°0'0\"E", (0.0, 0.0)),
    ("90°0'0\"S", "180°0'0\"W", (-90.0, -180.0)),
])
def test_standardize_latlong_dms(lat, lon, expected):
    """
    Test that degrees, minutes, seconds inputs are converted correctly.
    """
    result_lat, result_lon = standardize_latlong(lat, lon)

    assert result_lat == pytest.approx(expected[0], abs=1e-6)
    assert result_lon == pytest.approx(expected[1], abs=1e-6)

# Test degrees and decimal minutes (DDM) inputs

@pytest.mark.parametrize("lat, lon, expected", [
    ("34°3.133'N", "118°14.617'W", (34.052217, -118.243617)),
    ("34°3.133'S", "118°14.617'E", (-34.052217, 118.243617)),
])
def test_standardize_latlong_ddm(lat, lon, expected):
    """
    Test that degrees and decimal minutes inputs are converted correctly.
    """
    result_lat, result_lon = standardize_latlong(lat, lon)

    assert result_lat == pytest.approx(expected[0], abs=1e-6)
    assert result_lon == pytest.approx(expected[1], abs=1e-6)

# Test out of range inputs

@pytest.mark.parametrize("lat, lon", [
    (91.0, 0.0),
    (0.0, -181.0),
])
def test_standardize_latlong_out_of_range(lat, lon):
    """
    Test that out of range latitude/longitude raises ValueError.
    """
    with pytest.raises(ValueError, match="Latitude must be between -90 and 90 and longitude between -180 and 180"):
        standardize_latlong(lat, lon)

# Test invalid format inputs

@pytest.mark.parametrize("lat, lon", [
    ("invalid_lat", "118°14'37\"W"),
    ("34°3'8\"N", "invalid_lon"),
    ("34 degrees north", "118 degrees west"),
    ("34°3'8\"Q", "118°14'37\"Z"),
])
def test_standardize_latlong_invalid_format(lat, lon):
    """
    Test that invalid format latitude/longitude raises ValueError.
    """
    with pytest.raises(ValueError):
        standardize_latlong(lat, lon)