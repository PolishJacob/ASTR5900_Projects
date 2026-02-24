import numpy as np

# Differential equation of interest. The true f(x) from this diff eq is f(x) = tan(x)
def dydx(y):
    return y**2 + 1

# Euler Method Numerical Integration. Takes some initial x and final x, along with an integer to divide xf - xi by
# to determine the step size. Iteratively calculates the integral of a given function (Here, a hard-coded function above).
# Returns the y value from the evaluation
def euler_method(initialx, finalx, delta):
    # Initialize variables
    yi = dydx(initialx)
    deltax = (finalx - initialx) / delta
    xi1 = initialx + deltax
    yi1 = yi + (deltax * dydx(yi))
    print("xi =", xi1, "yi =", yi, "deltax * f(xi, yi) =", deltax * dydx(yi), "True tan(x) =", np.tan(xi1))

    # Iterate until finalx is reached
    while xi1 < finalx:
        xi1 = xi1 + deltax
        yi = dydx(xi1)
        yi1 = yi + (deltax * dydx(yi))
        print("xi =", xi1, "yi =", yi, "deltax * f(xi, yi) =", deltax * dydx(yi), "True tan(x) =", np.tan(xi1))

    return yi1

# RK2 Runge-Kutta Numerical Integration. 
def runge_kutta_2():
    yi1 = 0

    return yi1

# Test functions
initial = 0
final = 1
steps = 5

print("Euler Method Numerical Integration")
solution = euler_method(initial, final, steps)
print("Function solution: f(x) =", solution, "True solution: tan(x) =", np.tan(final))