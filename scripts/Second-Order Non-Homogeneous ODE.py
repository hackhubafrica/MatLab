import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the differential equation function
def second_order_ode(y, t):
    y1, y2 = y
    dydt = [y2, 2*y2 - y1 + np.exp(2*t)]
    return dydt

# Initial conditions
y0 = [0, 1]  # y(0) = 0, y'(0) = 1

# Time points to solve for
t = np.linspace(0, 5, 100)

# Solve the differential equation
sol = odeint(second_order_ode, y0, t)

# Extract solution for y(t)
y = sol[:, 0]

# Plot the solution
plt.figure(figsize=(8, 6))
plt.plot(t, y, label='y(t)')
plt.title('Solution of Second-Order ODE: y\'\' - 2y\' + y = e^(2t)')
plt.xlabel('Time (t)')
plt.ylabel('y(t)')
plt.grid(True)
plt.legend()
plt.show()