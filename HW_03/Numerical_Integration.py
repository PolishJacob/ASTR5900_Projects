import numpy as np
import matplotlib.pyplot as plt

# Differential equation of interest. The true f(x) from this diff eq is f(x) = tan(x)
def dydx(y):
    return y**2 + 1

# Maxwell-Boltzmann Velocity Distribution
def f(v):
    m = 1.67e-27
    k = 1.38e-23
    T = 10000

    f = ((m / (2 * np.pi * k * T))**(3/2)) * (4 * np.pi * v**2) * np.exp(-(m * v**2) / (2 * k * T))
    return f

# Euler Method Numerical Integration. Takes a differential equation, some initial and final x, an initial y, 
# along with an integer to divide xf - xi by to determine the step size h. Iteratively calculates the integral 
# of a given function (here, a hard-coded function above). Returns an array for the x values, y values, 
# true values, and the final y value.
def euler_method(fxn, initial_x, final_x, initial_y, steps):
    # Initialize variables
    x_arr = np.array([])
    y_arr = np.array([])
    true_arr = np.array([])
    x_arr = np.append(x_arr, initial_x) # Place first element of x
    y_arr = np.append(y_arr, initial_y) # Place first element of y
    true_arr = np.append(true_arr, np.tan(initial_x)) # Place first element of true

    # First calculations
    h = (final_x - initial_x) / steps # Step size
    x_new = initial_x + h
    x_arr = np.append(x_arr, x_new)
    true_arr = np.append(true_arr, np.tan(x_new))
    f = fxn(initial_y) # dy/dx evaluated at xi and yi
    y_new = initial_y + (h * f)
    y_arr = np.append(y_arr, y_new)

    # Print initial inputs and first calculations
    print(f"x_i = {initial_x:.3f}, y_i = {initial_y:.3f}, f = {f:.3f}, h * f = {h * f:.3f}, true tan(x) = {np.tan(initial_x * 180 / np.pi):.3f}")
    print(f"x_new = {x_new:.3f}, y_new = {y_new:.3f}, f = {f:.3f}, dx * f = {h * f:.3f}, true tan(x) = {np.tan(x_new):.3f}")

    # Iterate by steps of x until final_x is reached. Print the variables in each step
    while x_new < final_x:
        x_new = x_new + h
        x_arr = np.append(x_arr, x_new)
        true_arr = np.append(true_arr, np.tan(x_new))
        f = fxn(y_new)
        y_new = y_new + (h * f)
        y_arr = np.append(y_arr, y_new)

        print(f"x_new = {x_new:.3f}, y_new = {y_new:.3f}, f = {f:.3f}, dx * f = {h * f:.3f}, true tan(x) = {np.tan(x_new):.3f}")

    return x_arr, y_arr, true_arr, y_new

# RK2 Runge-Kutta Numerical Integration. Uses the Modified Euler Method value of b = 1/2. Takes a differential equation, 
# some initial and final x, an initial y, along with an integer to divide xf - xi by to determine the step size h. 
# Iteratively calculates the integral of a given function (here, a hard-coded function above). 
# Returns an array for the x values, y values, true values, and the final y value.
def runge_kutta_2(fxn, initial_x, final_x, initial_y, steps):
    # Initialize variables
    x_arr = np.array([])
    y_arr = np.array([])
    true_arr = np.array([])
    x_arr = np.append(x_arr, initial_x) # Place first element of x
    y_arr = np.append(y_arr, initial_y) # Place first element of y
    true_arr = np.append(true_arr, np.tan(initial_x)) # Place first element of true

    # First calculations
    h = (final_x - initial_x) / steps # Step size
    x_new = initial_x + h
    x_arr = np.append(x_arr, x_new)
    true_arr = np.append(true_arr, np.tan(x_new))
    K1 = fxn(initial_y)
    K2 = fxn(initial_y + (h * K1))
    y_new = initial_y + ((h * (K1 + K2)) / 2)
    y_arr = np.append(y_arr, y_new)

    # Print initial inputs and first calculations
    print(f"x_i = {initial_x:.3f}, y_i = {initial_y:.3f}, true tan(x) = {np.tan(initial_x * 180 / np.pi):.3f}")
    print(f"x_new = {x_new:.3f}, y_new = {y_new:.3f}, true tan(x) = {np.tan(x_new):.3f}")

    # Iterate by steps of x until final_x is reached. Print the variables in each step
    while x_new < final_x:
        x_new = x_new + h
        x_arr = np.append(x_arr, x_new)
        true_arr = np.append(true_arr, np.tan(x_new))
        K1 = fxn(y_new)
        K2 = fxn(y_new + (h * K1))
        y_new = y_new + ((h * (K1 + K2)) / 2)
        y_arr = np.append(y_arr, y_new)

        print(f"x_new = {x_new:.3f}, y_new = {y_new:.3f}, true tan(x) = {np.tan(x_new):.3f}")

    return x_arr, y_arr, true_arr, y_new

# Initialize variables
x_i = 0.0
x_f = 1
y_i = 0.0
steps = 100
euler_x = np.array([])
euler_y = np.array([])
euler_true = np.array([])
euler_solution = -999
rk_x = np.array([])
rk_y = np.array([])
rk_true = np.array([])
rk_solution = -999

# Calculate with both methods and print
print("Euler Method Numerical Integration")
euler_x, euler_y, euler_true, euler_solution = euler_method(dydx, x_i, x_f, y_i, steps)
print("Function solution: f(x) =", euler_solution, "True solution: tan(x) =", np.tan(x_f))

print("Runge-Kutta RK2 Numerical Integration")
rk_x, rk_y, rk_true, rk_solution = runge_kutta_2(dydx, x_i, x_f, y_i, steps)
print("Function solution: f(x) =", rk_solution, "True solution: tan(x) =", np.tan(x_f))

# Plot convergence study of both methods
# log_x = np.logspace(euler_x[0], euler_x[-1], steps)
# print(log_x, len(log_x))
# plt.scatter(log_x, np.log(np.abs(euler_y - euler_true)), s= 1)
# plt.show()

# Maxwell-Boltzmann Velocity Distribution Plot
mb_x = np.linspace(0, 40000, 40000) # Range of velocities
mb_y = f(mb_x) # Probabilities
plt.scatter(mb_x, mb_y, s = 10)
plt.show()

# Use RK2 for Maxwell-Boltzmann integration
