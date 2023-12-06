import sympy as sp

# Define symbolic variables
x1, x2 = sp.symbols('x1 x2')

# Define the objective function
f = 100*(x2 - x1**2)**2 + (1 - x1)**2

# Calculate the gradient of the objective function
gradient = [sp.diff(f, var) for var in (x1, x2)]
print("Gradient:\n", gradient)
print()

# Calculate the Hessian matrix of the objective function
hessian = [[sp.diff(gradient[i], var_j) for var_j in (x1, x2)] for i in (0, 1)]
print("Hessian:")
for row in hessian:
    print(row)
