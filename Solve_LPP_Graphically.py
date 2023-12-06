import pulp
import matplotlib.pyplot as plt
import numpy as np

# Create a linear programming problem for graphical representation
lp_problem = pulp.LpProblem("Graphical_LPP", pulp.LpMaximize)

# Define decision variables
x = pulp.LpVariable("x", lowBound=0)
y = pulp.LpVariable("y", lowBound=0)

# Define the objective function to maximize
lp_problem += 3*x + 2*y, "Z"

# Define the constraints
lp_problem += 3*x + y <= 20
lp_problem += 4*x - 5*y >= -15
lp_problem += x + y <= 15

# Choose the solver and suppress solver messages
solver = pulp.LpSolverDefault
solver.msg = 0

# Solve the linear programming problem
lp_problem.solve(solver)

# Display the results
print("Status:", pulp.LpStatus[lp_problem.status])
print("Optimal values:")
print("x =", pulp.value(x))
print("y =", pulp.value(y))
print("Optimal objective function value (Z) =", pulp.value(lp_problem.objective))

# Generate x values for plotting
x_values = np.linspace(0, 10, 100)

# Compute y values for each constraint
y1_values = (20 - 3*x_values)
y2_values = (4*x_values + 15) / 5
y3_values = (15 - x_values)

# Plot the constraints
plt.plot(x_values, y1_values, label="3x + y <= 20")
plt.plot(x_values, y2_values, label="4x - 5y >= -15")
plt.plot(x_values, y3_values, label="x + y <= 15")

# Fill the feasible region
plt.fill_between(x_values, 0, np.minimum(np.minimum(y1_values, y2_values), y3_values), 
                 where=(y1_values >= 0) & (y2_values >= 0) & (y3_values >= 0), 
                 interpolate=True, color='gray', alpha=0.5)

# Set plot labels and title
plt.xlabel("x")
plt.ylabel("y")
plt.title("Feasible Region")
plt.legend()
plt.grid(True)
plt.show()