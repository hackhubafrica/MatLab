import numpy as np
from scipy.optimize import minimize

# Define the cost function for power generation
def cost_function(p):
    return p[0]**2 + p[1]**2 + p[2]**2

# Constraints (e.g., power demand and generation limits)
constraints = (
    {'type': 'eq', 'fun': lambda p: p[0] + p[1] + p[2] - 100},  # Power demand
    {'type': 'ineq', 'fun': lambda p: p[0] - 10},  # Min generation for plant 1
    {'type': 'ineq', 'fun': lambda p: p[1] - 20},  # Min generation for plant 2
    {'type': 'ineq', 'fun': lambda p: p[2] - 30},  # Min generation for plant 3
)

# Initial guess
p0 = [33, 33, 34]

# Perform the optimization
result = minimize(cost_function, p0, constraints=constraints)

# Output the results
print(f"Optimal Power Generation: {result.x}")
print(f"Minimum Cost: {result.fun}")
