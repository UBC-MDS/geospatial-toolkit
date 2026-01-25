# Used GenAI (Gemini-3-pro) to modify the docstring into numpy style, and create examples.
# Used GenAI (Gemini-3-pr) to ensure modularity in functions, ideate the structure of the code, and handle the exception cases/ errors gracefully.

from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError


def _identify_ocean(lat, lon):
    """
    Identify which ocean a coordinate point is located in using simplified boundaries.
    Boundaries are approximate and intended only as a fallback when reverse geocoding fails.

    Parameters
    ----------
    lat : float
        Latitude in decimal degrees.
    lon : float
        Longitude in decimal degrees.

    Returns
    -------
    str
        Name of the ocean (Pacific, Atlantic, Indian, Arctic, or Southern).
    """
    if lat < -60:
        return "Southern(Antarctic) Ocean"
    if lat > 66.5:
        return "Arctic Ocean"
    if lon < -70:
        return "Pacific Ocean"
    if lon < 20:
        return "Atlantic Ocean"
    if lon < 100:
        return "Indian Ocean"
    # lon >= 100: transition zone between Indian and Pacific
    if lon < 145 and lat < -10:
        return "Indian Ocean"
    return "Pacific Ocean"


def get_antipode(location, resolve_names=True):
    """
    Calculate the antipode (opposite point on Earth) for a given location and
    identify its geographical description.

    Parameters
    ----------
    location : str or tuple of float
        The starting location.
        - If str: A query string for a place name (e.g., "Vancouver, Canada").
        - If tuple: Coordinates in (latitude, longitude) format.
    resolve_names : bool, optional
        Whether to reverse geocode the antipodal coordinates. Default is True.

    Returns
    -------
    antipode_coords : tuple of float
        The coordinates of the antipode in (latitude, longitude) format.
    antipode_desc : str or None
        Human-readable description of the antipode location.
        Returns None if `resolve_names` is False.

    Raises
    ------
    ValueError
        If the location string cannot be geocoded or coordinates are out of range.
    TypeError
        If location is not a string or tuple of floats.

    Examples
    --------
    >>> coords, desc = get_antipode("Madrid, Spain")
    >>> print(coords)
    (-40.4168, 176.2962)

    >>> coords, desc = get_antipode((49.2827, -123.1207))
    >>> print(desc)
    "French Southern and Antarctic Lands"
    """
    geolocator = Nominatim(user_agent="geospatial_toolkit")

    # Parse input to get lat/lon
    if isinstance(location, str):
        try:
            geo_result = geolocator.geocode(location)
        except (GeocoderTimedOut, GeocoderServiceError) as e:
            raise ValueError(f"Geocoding service error: {e}")

        if geo_result is None:
            raise ValueError(f"Could not geocode location: '{location}'")
        lat, lon = geo_result.latitude, geo_result.longitude

    elif isinstance(location, tuple):
        if len(location) != 2:
            raise TypeError(
                f"Coordinate tuple must have exactly 2 elements, got {len(location)}"
            )
        lat, lon = location
        if not isinstance(lat, (int, float)) or not isinstance(lon, (int, float)):
            raise TypeError("Coordinate values must be numeric (int or float)")
    else:
        raise TypeError(
            f"location must be a string or tuple of floats, got {type(location).__name__}"
        )

    # Validate coordinates
    if not (-90 <= lat <= 90):
        raise ValueError(f"Latitude must be between -90 and 90 degrees. Got {lat}.")
    if not (-180 <= lon <= 180):
        raise ValueError(f"Longitude must be between -180 and 180 degrees. Got {lon}.")

    # Calculate antipode
    antipode_lat = round(-lat, 4)
    antipode_lon = round(lon - 180 if lon >= 0 else lon + 180, 4)
    antipode_coords = (antipode_lat, antipode_lon)

    if not resolve_names:
        return antipode_coords, None

    # Reverse geocode the antipode
    try:
        reverse_result = geolocator.reverse(
            f"{antipode_lat}, {antipode_lon}", language="en"
        )
    except (GeocoderTimedOut, GeocoderServiceError):
        return antipode_coords, "Unknown (geocoding service unavailable)"

    if reverse_result is None:
        antipode_desc = _identify_ocean(antipode_lat, antipode_lon)
    else:
        antipode_desc = reverse_result.address

    return antipode_coords, antipode_desc
