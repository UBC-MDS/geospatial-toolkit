# Note: Google Gemini AI was used to write the docstrings for the haversine_distance function

import math

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
    if not (isinstance(origin, tuple) and isinstance(destination, tuple)):
        raise TypeError("Origin and destination must be tuples.")
    
    if len(origin) != 2 or len(destination) != 2:
        raise ValueError("Origin and destination must have a length 2.")

    try:
        lat1, lon1 = map(float, origin)
        lat2, lon2 = map(float, destination)
    except (ValueError, TypeError):
        raise TypeError("Coordinates must contain numeric values.")

    if not (-90 <= lat1 <= 90 and -90 <= lat2 <= 90):
        raise ValueError("Latitude is not between -90 and 90.")
    
    if not (-180 <= lon1 <= 180 and -180 <= lon2 <= 180):
        raise ValueError("Longitude is not between -180 and 180.")
    
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    r = 6371.0 
    distance = c * r

    if unit == 'km':
        return distance
    elif unit == 'm':
        return distance * 1000
    elif unit == 'miles':
        return distance * 0.621371
    else:
        raise ValueError("Unit must be one of {'km', 'm', 'miles'}")