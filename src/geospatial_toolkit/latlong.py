# ChatGPT and VSCode GenAI was used to help write the docstring such as latitude/longitude values and examples.

def standardize_latlong(lat_value, lon_value):
    """
    Convert various latitude/longitude formats to a standardized decimal degree format.
    
    Parameters
    ----------
    lat_value : str or float
        Latitude value in various formats.
    lon_value : str or float
        Longitude value in various formats.
    Supported formats:
        - Decimal degrees (e.g., 34.0522, -118.2437)
        - Degrees, minutes, seconds (e.g., 34°3'8"N, 118°14'37"W)
        - Degrees and decimal minutes (e.g., 34°3.133'N, 118°14.617'W)

    Returns
    -------
    tuple
        A tuple containing standardized latitude and longitude in decimal degrees.
    
    Raises
    ------
    ValueError
        If the input format is not recognized or invalid.
        Valid ranges:
            - Latitude must be between -90 and 90
            - Longitude must be between -180 and 180
    
    Examples
    --------
    >>> standardize_latlong("34°3'8\"N", "118°14'37\"W")
    (34.052222, -118.243611)
    >>> standardize_latlong(34.0522, -118.2437)
    (34.0522, -118.2437)
    """
    pass