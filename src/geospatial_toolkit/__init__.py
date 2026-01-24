# MIT License
#
# Copyright (c) 2026 Athul, Bala, Prabuddha, Shreya
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice (including the next
# paragraph) shall be included in all copies or substantial portions of the
# Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
Geospatial Toolkit: A modular Python library for common spatial utilities.

This package provides lightweight functions for standardizing coordinates, 
calculating distances, finding antipodes, and performing point-in-polygon 
searches for city locations. It is designed to be accessible for GIS 
analysts and data scientists without requiring heavy GIS software.

Available functions:
- haversine_distance: Calculate great-circle distance between two points.
- get_antipode: Find the diametrically opposite point on Earth.
- standardize_latlong: Convert various coordinate formats to decimal degrees.
- point_to_city: Identify which city contains a given coordinate pair.
"""

from geospatial_toolkit.distance import haversine_distance
from geospatial_toolkit.calc_antipode import get_antipode
from geospatial_toolkit.latlong import standardize_latlong
from geospatial_toolkit.point_to_city import point_to_city

# This defines what is available when someone does 'from geospatial_toolkit import *'
__all__ = [
    "haversine_distance",
    "get_antipode",
    "standardize_latlong",
    "point_to_city",
]