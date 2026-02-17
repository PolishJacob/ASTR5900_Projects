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
def bisection_root(xleft, xright, err):
    # Initialize variables
    y = -999
    x_new = -999
    relErr = -999
    soln = -999
    iterations = 1

    # Verify the two guesses have a zero value between them
    if (f(xleft) > 0 and f(xright) > 0) or (f(xleft) < 0 and f(xright) < 0):
        print("Invalid set of guesses: Values do not cover a root.")
        return iterations, soln
    else:
        # Calculate first x_new
        x_new = (xleft + xright) / 2
        y = f(x_new)
        interations = iterations + 1
        if y < 0: # Calculate relErr from x_left and replace x_left
            relErr = abs((x_new - xleft) / x_new)
            xleft = x_new
        else: # Calculate relErr from x_right and replace x_right
            relErr = abs((x_new - xright) / x_new)
            xright = x_new

        while(relErr > err): # Use first relErr calculation to calculate while loop to desired error
            x_new = (xleft + xright) / 2
            y = f(x_new)
            iterations = iterations + 1
            if y < 0:
                relErr = abs((x_new - xleft) / x_new)
                xleft = x_new
            else:
                relErr = abs((x_new - xright) / x_new)
                xright = x_new

        return iterations, soln

# Newton_Raphson_root function takes one guess of the root of a given function and finds the x value
# associated with that root within some desired relative error using Newton-Raphson method. Derivative must be
# specified beforehand.
def newton_raphson_root(x0, err):
    # Initialize variables
    x1 = -999
    x_new = -999
    x_old = -999
    relErr = -999
    soln = -999
    iterations = 1

    # Calculate first iteration
    x1 = x0 - (f(x0) / derivf(x0))
    relErr = abs((x1 - x0) / x1)
    print("Iteration", iterations, ", x_new:", x1, ", relative error:", relErr)

    # See if x0 was a really good guess for x1
    if relErr < err:
        return iterations, x1
    else:
        x_old = x1
    
    # Keep calculating x_new until relative error is below the requested error
    while(relErr > err):
        x_new = x_old - (f(x_old) / derivf(x_old))
        relErr = abs((x_new - x_old) / x_new)
        iterations = iterations + 1
        print("Iteration", iterations, ", x_new:", x_new, ", relative error:", relErr)

        if (relErr < err):
            soln = x_new
        else:
            x_old = x_new

    return iterations, soln

# Test functions
its = -999
solution = -999
guess = 0.0
guess_left = 0.0
guess_right = 1.0
error = 0.01

its, solution = newton_raphson_root(guess, error)
print("Number of iterations:", its)
print("Solution:", solution)