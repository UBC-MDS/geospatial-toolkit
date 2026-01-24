# ChatGPT and VSCode GenAI was used to help write the docstring such as latitude/longitude values and examples.
# Gemini helped write the regex patterns and parsing logic.

import re


def standardize_latlong(lat, lon):
    """
    Convert various latitude/longitude formats to a standardized decimal degree format.

    Parameters
    ----------
    lat : str or float
        Latitude value in various formats.
    lon : str or float
        Longitude value in various formats.
    Supported formats:
        - Decimal degrees (e.g., 34.0522, -118.2437)
        - Degrees, minutes, seconds (e.g., 34°3'8"N, 118°14'37"W)
        - Degrees and decimal minutes (e.g., 34°3.133'N, 118°14.617'W)

    Returns
    -------
    tuple
        A tuple of floats containing standardized latitude and longitude in decimal degrees.

    Raises
    ------
    ValueError
        If the input format is not recognized or if the coordinates are out of valid geographic ranges
        (Latitude must be between -90 and 90 and longitude must be between -180 and 180).

    Examples
    --------
    >>> # Decimal Degrees
    >>> standardize_latlong(34.0522, -118.2437)
    (34.0522, -118.2437)

    >>> # Degrees, Minutes, Seconds (DMS)
    >>> standardize_latlong("34°3'8\"N", "118°14'37\"W")
    (34.05222222222222, -118.24361111111111)

    >>> # Degrees and Decimal Minutes (DDM)
    >>> standardize_latlong("34°3.133'N", "118°14.617'W")
    (34.05221666666667, -118.24361666666667)
    """

    def parse_coordinate(coord):
        """
        Parse a single coordinate (latitude or longitude) from various formats to decimal degrees.
        """
        try:
            return float(coord)
        except ValueError:
            pass

        if isinstance(coord, str):
            dms_pattern = re.match(r"(\d+)°(\d+)'(\d+(?:\.\d+)?)\"?([NSEW])", coord)
            ddm_pattern = re.match(r"(\d+)°(\d+(?:\.\d+)?)'?([NSEW])", coord)

            if dms_pattern:
                degrees, minutes, seconds, direction = dms_pattern.groups()
                value = float(degrees) + float(minutes) / 60 + float(seconds) / 3600
            elif ddm_pattern:
                degrees, minutes, direction = ddm_pattern.groups()
                value = float(degrees) + float(minutes) / 60
            else:
                raise ValueError("Input format not recognized or invalid")

            if direction in ["S", "W"]:
                value = -value
            return value

        raise ValueError("Input format not recognized or invalid")

    standard_lat = parse_coordinate(lat)
    standard_lon = parse_coordinate(lon)

    if not (-90 <= standard_lat <= 90) or not (-180 <= standard_lon <= 180):
        raise ValueError(
            "Latitude must be between -90 and 90 and longitude between -180 and 180"
        )

    return standard_lat, standard_lon
