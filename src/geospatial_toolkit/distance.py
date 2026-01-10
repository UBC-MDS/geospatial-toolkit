# Note: Google Gemini AI was used to write the docstrings for the haversine_distance function

def haversine_distance(origin, destination, unit='km'):
    """
    Calculate the great-circle distance between two points on Earth 
    using the haversine formula.

    Parameters
    ----------
    origin : tuple of float
        A tuple representing the (latitude, longitude) of the starting point
        in decimal degrees.
    destination : tuple of float
        A tuple representing the (latitude, longitude) of the end point
        in decimal degrees.
    unit : {'km', 'miles', 'm'}, optional
        The unit of distance to return. Default is 'km'.

    Returns
    -------
    float
        The distance between the two points in the specified units.

    Raises
    ------
    TypeError
        If origin or destination are not tuples or contains non-numeric values.
    ValueError
        If latitude is not between -90 and 90, or longitude not between -180 and 180.

    Examples
    --------
    >>> point_a = (49.2827, -123.1207) # Vancouver
    >>> point_b = (45.5017, -73.5673)  # Montreal
    >>> haversine_distance(point_a, point_b)
    3684.41
    """

    pass