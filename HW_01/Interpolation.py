# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import math

# Define linear interpolation function
# This function finds the y value for a given x within the given range of x_pnts using linear interpolation.
# Resolution can be increased by giving how many n points are desired between points in the given data set.
def lin_interpolate(x_pnts, y_pnts, x, n):
    if(x >= x_pnts[0] and x <= x_pnts[-1]):
        print("x =", x, "falls within the data range.")
    else:
        print("x =", x, "falls outside of the given data range.")
    return

# Data array
xpoints = [2, 5, 6, 8, 10]
ypoints = [3, 4, 5, 8, 9]
lin_interpolate(xpoints, ypoints, 11, 1)