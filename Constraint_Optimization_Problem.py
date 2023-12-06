import numpy as np
import scipy.optimize as opt

# Define the objective function to minimize
def f(x):
   return (x[0] - 3)**2 + (x[1] + 2)**2

# Define the constraint function
def constraint(x):
   return x[0]**2 + x[1]**2 - 50

# Set up the equality constraint
cons = ({'type': 'eq', 'fun': constraint})

# Initial guess for the minimizer
x0 = np.array([3, -5])

# Use the minimize function to find the minimum subject to the constraint
result = opt.minimize(f, x0, constraints=cons)

# Print information about the optimization result
print("Objective function to minimize: (x1 - 3)**2 + (x2 + 2)**2")
print("\nSubject to constraints :")
print("x1**2 + x2**2 - 50 = 0\n")

# Display the optimization result
print(result.message)
print("Optimal values:")
print("x1:", result.x[0])
print("x2:", result.x[1])