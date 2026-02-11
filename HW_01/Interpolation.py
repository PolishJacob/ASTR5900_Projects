# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import math

# Define linear interpolation function
# This function finds the y value for a given x within the given range of x_pnts using linear interpolation.
# Function assumes that the provided x_pnts and y_pnts are pre-sorted from lowest to highest
# Resolution can be increased by giving how many n points are desired between points in the given data set.
def lin_interpolate(x_pnts, y_pnts, x, n = 1):
    if(len(x_pnts) != len(y_pnts)): #Check to see if given x array and y array are equal length, otherwise exit
        print("Error: Length of x_pnts and y_pnts do not match. Values returned.")
        return x, x_pnts, y_pnts
    
    x_array = np.array([]) # Initialize output x array
    y_array = np.array([]) # Initialize output y array

    if(n == 1): # If resolution is default value, output the given arrays
        x_array = x_pnts
        y_array = y_pnts
    else:
        for i in range(0, len(x_pnts) - 1):
            xarr = np.array([])
            yarr = np.array([])
            xi = x_pnts[i]
            xi1 = x_pnts[i+1]
            yi = y_pnts[i]
            yi1 = y_pnts[i+1]

            xarr = np.linspace(xi, xi1, n)
            x_array = np.append(x_array, xarr)

            a = (yi1 - yi) / (xi1 - xi)
            b = yi - (a * xi)
            yarr = (a * xarr) + b
            y_array = np.append(y_array, yarr)

    if(x >= x_pnts[0] and x <= x_pnts[-1]): # Check if requested x is within the given x range
        for i in range(0, len(x_pnts)): # Find which two given points the requested x is between
            if(x >= x_pnts[i] and x <= x_pnts[i+1]):
                xi = x_pnts[i]
                xi1 = x_pnts[i+1]
                yi = y_pnts[i]
                yi1 = y_pnts[i+1]
                print("x =", x, "falls between x =", xi, "and x =", xi1)
                break
        a = (yi1 - yi) / (xi1 - xi)
        b = yi
        g = a * (x - xi) + b # Calculate y on line between the two given points the requested x is between


    else:
        print("x =", x, "falls outside of the given data range. Values returned.")
        return x, x_array, y_array
    return g, x_array, y_array

# Read data from HW_01.txt
xpoints, ypoints = np.loadtxt('HW01_data.txt', skiprows=1, usecols=(0, 1), unpack=True)
print("x array:", xpoints)
print("y array:", ypoints)
pnt = 2.5
num = 10
g_val, highResX, highResY = lin_interpolate(xpoints, ypoints, pnt, num)
print("The y value at x =", pnt, "is", g_val)
print("The interpolation x array is:", highResX)
print("The interpolation y array is:", highResY)
print("Length of interpolated x array:", len(highResX))
print("Length of interpolated y array:", len(highResY))

plt.scatter(xpoints, ypoints)
plt.scatter(pnt, g_val)
plt.scatter(highResX, highResY, s = 3)
plt.show()