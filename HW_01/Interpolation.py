# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import math

# Define linear interpolation function
# This function finds the y value for a given x within the given range of x_pnts using linear interpolation.
# Function assumes that the provided x_pnts and y_pnts are pre-sorted from lowest to highest
# Resolution can be increased by giving how many n points are desired between points in the given data set.
def lin_interpolate(x_pnts, y_pnts, x, n):
    if(x >= x_pnts[0] and x <= x_pnts[-1]):
        for i in range(0, len(x_pnts)):
            if(x >= x_pnts[i] and x <= x_pnts[i+1]):
                xi = x_pnts[i]
                xi1 = x_pnts[i+1]
                yi = y_pnts[i]
                yi1 = y_pnts[i+1]
                print("x =", x, "falls between x =", xi, "and x =", xi1)
                break
            else:
                print("Error in finding given point range.")
        a = (yi1 - yi) / (xi1 - xi)
        b = yi
        g = a * (x - xi) + b
    else:
        print("x =", x, "falls outside of the given data range.")
    return g

# Data array
xpoints = [2, 3, 4, 9, 15]
ypoints = [2, 6, 7, 12, 16]
pnt = 9
g_val = lin_interpolate(xpoints, ypoints, pnt, 1)
print("The y value at x =", pnt, "is", g_val)