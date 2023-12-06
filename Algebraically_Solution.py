import numpy as np
import scipy.optimize as opt

# Define the objective function
def f(x):
    return -10 * np.cos(np.pi * x - 2.2) + (x + 1.5) * x

# Initial guess for the minimizer
x0 = [-2]

# Set up minimizer options
minimizer_kwargs = {"method": "BFGS"}

# Use basinhopping optimization algorithm
optimization_algorithm = opt.basinhopping(f, x0, minimizer_kwargs=minimizer_kwargs, niter=200)

# Print information about the optimization result
print("1-D function")
print(optimization_algorithm.message[0])
optimized_x = optimization_algorithm.x
optimized_fun = optimization_algorithm.fun

# Display the optimized results
print("Optimized x: ", optimized_x)
print("Optimized function value: ", optimized_fun)
