import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the function that represents the system of ODEs
def model(z, t):
    y, dydt = z
    dzdt = [dydt, np.sin(t) - 2*y*dydt**2]
    return dzdt

# Initial conditions
y0 = 0.0
dydt0 = 0.0

# Time points for which to solve the ODE (0 to 10 in steps of 0.01)
t = np.arange(0, 10, 0.01)

# Solve the ODE using odeint
z0 = [y0, dydt0]
z = odeint(model, z0, t)

# Extract y(t) from the solution
y = z[:, 0]

# Plot the solution
plt.figure(figsize=(8, 6))
plt.plot(t, y, label='y(t)')
plt.title('Solution of d^2y/dt^2 + 2y(dy/dt)^2 = sin(t)')
plt.xlabel('t')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()