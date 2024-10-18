import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the function that represents the system of ODEs
def model(z, t):
    x, y = z
    dxdt = x - y**2
    dydt = -x**2 + y
    return [dxdt, dydt]

# Initial conditions
x0 = 1.0
y0 = 1.0

# Time points for which to solve the ODE (0 to 10 in steps of 0.01)
t = np.arange(0, 10, 0.01)

# Solve the ODE using odeint
z0 = [x0, y0]
z = odeint(model, z0, t)

# Extract x(t) and y(t) from the solution
x = z[:, 0]
y = z[:, 1]

# Plot the solution
plt.figure(figsize=(8, 6))
plt.plot(t, x, label='x(t)')
plt.plot(t, y, label='y(t)')
plt.title('Solution of Nonlinear System of ODEs')
plt.xlabel('t')
plt.ylabel('Variables')
plt.grid(True)
plt.legend()
plt.show()