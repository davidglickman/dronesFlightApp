# -*- coding: utf-8 -*-
"""
Created on Mon May  9 20:38:51 2022

@author: glick
"""

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

point = Point(0.5, 0.5)
polygon = Polygon([(0, 0), (0, 1), (1, 1), (1, 0)])
print(polygon.contains(point))