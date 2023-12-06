import numpy as np
import scipy.optimize as opt
import seaborn as sns
import matplotlib.pyplot as plt

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

# Plot the function and the optimized point
sns.set_theme()

X = np.arange(-10, 10, 0.2)
y = [f(x) for x in X]

# Plot the function
plt.plot(X, y, label='Objective Function')

# Highlight the optimized point on the plot
plt.vlines(x=optimized_x, ymin=-10, ymax=125, colors='red', label='Optimized x')
plt.hlines(y=optimized_fun, xmin=-10, xmax=10, colors='red', label='Optimized function value')
plt.plot(optimized_x, optimized_fun, 'o', color="black", label='Optimized Point')

# Set plot labels and title
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Optimization of 1-D Function")
plt.legend()
plt.show()
