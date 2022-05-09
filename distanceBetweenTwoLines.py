# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 05:47:10 2022

@author: glick
"""
import numpy as np
from numpy import linalg as LA
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

def distance_from_two_lines(e1, e2, r1, r2):
    # e1, e2 = Direction vector
    # r1, r2 = Point where the line passes through

    # Find the unit vector perpendicular to both lines
    n = np.cross(e1, e2)
    n /= np.linalg.norm(n)

    # Calculate distance
    d = np.dot(n, r1 - r2)

    return d


x11 = np.array([0,0,0])
x12 = np.array([0,0,50])

r1 = x11
t1 = LA.norm(x11-x12)
e1 = (x12-x11)/t1

x21 = np.array([20,0,0])
x22 = np.array([30,40,50])

r2 = x21
t2 = LA.norm(x21-x22)
e2 = (x22-x21)/t2

d = distance_from_two_lines(e1, e2, r1, r2)

