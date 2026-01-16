"""
Updated point-to-city function.

Note: 
ChatGPT and VSCode GenAI was used to help write the docstring.
ChatGPT was used to confirm the usecases, viability and potential errors of the function.
"""

def point_to_city(lat, lon, cities_df):
    """
    Determine which city polygon contains the given geographic coordinate.

    This function performs a point-in-polygon test to identify the city
    that the latitude/longitude coordinate falls within. It assumes that
    all geometries are provided in geographic coordinates (latitude and
    longitude) are using EPSG:4326. 
    No map projection or distance calculations are being performed.
    
    Parameters
    ----------
    lat : float
        Latitude of the point in decimal degrees.
    lon : float
        Longitude of the point in decimal degrees.
    cities_df : pandas.DataFrame
        A DataFrame containing city boundary geometries. The DataFrame
        must include a column named 'geometry' with Shapely Polygon
        or MultiPolygon objects, and a column named 'city_name' that
        identifies each city.
    
    Returns
    -------
    str or None
        The name of the city that contains the input point. Returns
        'None' if the point does not fall within any city polygon 
        OR if the point lies exactly on a city boundary. 
    
    Raises
    ------
    TypeError
        If `lat` or `lon` are not numeric, or if `cities_df` is not a
        pandas.DataFrame.
    ValueError
        If `lat` is not in the range [-90, 90] or if `lon` is not in the
        range [-180, 180].
    KeyError
        If `cities_df` does not contain the required columns
        'geometry' and 'city_name'.

    Notes
    ------
    - This function uses a topological point in polygon test and does not
      account for distance, area, or projection related distortions.
    - If a point lies exactly on a city boundary, this function returns None.
    - The accuracy of the result depends on the quality and resolution
      of the input city boundary dataset.
    
    Examples
    --------
    >>> lat = 49.2827
    >>> lon = -123.1207
    >>> point_to_city(lat, lon, cities_df)
        'Vancouver'
    """

    # Type Checks
    if not isinstance(cities_df, pd.DataFrame):
        raise TypeError("cities_df must be a pandas.DataFrame")

    if not isinstance(lat, (int, float)) or not isinstance(lon, (int, float)):
        raise TypeError("lat and lon must be numeric (int or float)")


    # Range validation 
    if not (-90 <= lat <= 90):
        raise ValueError("lat must be in the range [-90, 90]")

    if not (-180 <= lon <= 180):
        raise ValueError("lon must be in the range [-180, 180]")

    
    # Must Have Columns
    required_cols = {"geometry", "city_name"}
    if not required_cols.issubset(set(cities_df.columns)):
        raise KeyError("cities_df must contain 'geometry' and 'city_name' columns")
    



    
