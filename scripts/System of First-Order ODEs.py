import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the system of differential equations
def system_of_odes(u, t):
    x, y = u
    dxdt = -x + 2*y
    dydt = x - y
    return [dxdt, dydt]

# Initial conditions
u0 = [1, 0]  # x(0) = 1, y(0) = 0

# Time points to solve for
t = np.linspace(0, 10, 100)

# Solve the differential equations
sol = odeint(system_of_odes, u0, t)

# Extract solutions for x(t) and y(t)
x = sol[:, 0]
y = sol[:, 1]

# Plot the solutions
plt.figure(figsize=(8, 6))
plt.plot(t, x, label='x(t)')
plt.plot(t, y, label='y(t)')
plt.title('Solution of System of ODEs')
plt.xlabel('Time (t)')
plt.ylabel('Values')
plt.grid(True)
plt.legend()
plt.show()