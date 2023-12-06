from numpy import arange
from scipy.optimize import line_search
from matplotlib import pyplot

# Define the objective function
def objective(x):
    return (-8.0 + x) ** 2.0

# Define the gradient of the objective function
def gradient(x):
    return 3.0 * (-5.0 + x)

# Initial point and direction for line search
point = -5.0
direction = 100.0
print('start=%.1f, direction=%.lf' % (point, direction))

# Perform line search to find the step size (alpha)
result = line_search(objective, gradient, point, direction)
alpha = result[0]
print('Alpha: %.3f' % alpha)
print('Function evaluations: %d' % result[1])

# Calculate the end point based on the step size
end = point + alpha * direction

# Print the value of the objective function at the end point
print('f(end) = f(%.3f) = %.3f' % (end, objective(end)))

# Plotting the objective function, initial point, and end point
r_min, r_max = -25.0, 40.0
inputs = arange(r_min, r_max, 0.1)
targets = [objective(x) for x in inputs]
pyplot.plot(inputs, targets, '--', label='objective')
pyplot.plot([point], [objective(point)], 's', color='g', label='start point')
pyplot.plot([end], [objective(end)], 's', color='r', label='end point')
pyplot.legend()
pyplot.show()