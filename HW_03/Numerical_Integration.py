import numpy as np

# Differential equation of interest. The true f(x) from this diff eq is f(x) = tan(x)
def dydx(y):
    return y**2 + 1

# Euler Method Numerical Integration. Takes some initial and final x, an initial y, along with an integer to divide 
# xf - xi by to determine the step size h. Iteratively calculates the integral of a given function (here, a hard-coded 
# function above). Returns the y value from the evaluation.
def euler_method(initial_x, final_x, initial_y, steps):
    # Initialize variables
    h = (final_x - initial_x) / steps # Step size
    x_new = initial_x + h
    f = dydx(initial_y) # dy/dx evaluated at xi and yi
    y_new = initial_y + (h * f)
    print(f"x_i = {initial_x:.3f}, y_i = {initial_y:.3f}, f = {f:.3f}, h * f = {h * f:.3f}, true tan(x) = {np.tan(initial_x * 180 / np.pi):.3f}")
    print(f"x_new = {x_new:.3f}, y_new = {y_new:.3f}, f = {f:.3f}, dx * f = {h * f:.3f}, true tan(x) = {np.tan(x_new):.3f}")

    # Iterate by steps of x until final_x is reached
    while x_new < final_x:
        x_new = x_new + h
        f = dydx(y_new)
        y_new = y_new + (h * f)
        print(f"x_new = {x_new:.3f}, y_new = {y_new:.3f}, f = {f:.3f}, dx * f = {h * f:.3f}, true tan(x) = {np.tan(x_new):.3f}")

    return y_new

# RK2 Runge-Kutta Numerical Integration. 
def runge_kutta_2():
    yi1 = 0

    return yi1

# Test functions
x_i = 0.0
x_f = 1.0
y_i = 0.0
steps = 1000

print("Euler Method Numerical Integration")
solution = euler_method(x_i, x_f, y_i, steps)
print("Function solution: f(x) =", solution, "True solution: tan(x) =", np.tan(1))