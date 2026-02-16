import numpy as np

# Global function of interest to use for demonstration of the two root-finding methods
def f(x):
    y = (x**3) - (7 * x**2) + (14 * x) - 5
    return y

# Derivative of global function of interest to use in Newton-Raphson
def derivf(x):
    y = (3 * x**2) - (14 * x) + 14
    return y

# Bisection_root function takes two guesses on either side of the root of a given function and finds the x value
# associated with that root within some desired relative error using the Bisection method.
def bisection_root(x0, x1, err):
    if (f(x0) > 0 and f(x1) > 0) or (f(x0) < 0 and f(x1) < 0): # Verify the two guesses have a zero value between then
        print("Invalid set of guesses: Values do not cover a root.")
        return -1, -1
    else:
        
        return iterations, soln

# Newton_Raphson_root function takes one guess of the root of a given function and finds the x value
# associated with that root within some desired relative error using Newton-Raphson method. The function will
# calculate the derivative of the function.
def newton_raphson_root(x0, err):
    soln = -1

    x1 = x0 - (f(x0) / derivf(x0))
    relErr = abs((x1 - x0) / x1)
    iterations = 1

    if relErr < err: # See if x0 was a really good guess for x1
        return iterations, x1
    else:
        x_old = x1
    
    while(relErr > err): # Keep calculating x_new until relative error is below the requested error
        x_new = x_old - (f(x_old) / derivf(x_old))
        relErr = abs((x_new - x_old) / x_new)
        if (relErr < err):
            x_new = soln
        else:
            x_old = x_new
        iterations = iterations + 1
    return iterations, soln