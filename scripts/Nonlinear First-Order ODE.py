import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the function that represents the ODE
def model(y, t):
    dydt = y**2 - t
    return dydt

# Initial condition
y0 = 0.5

# Time points for which to solve the ODE (0 to 2 in steps of 0.01)
t = np.arange(0, 2, 0.01)

# Solve the ODE using odeint
y = odeint(model, y0, t)

# Plot the solution
plt.figure(figsize=(8, 6))
plt.plot(t, y, label='y(t)')
plt.title('Solution of dy/dt = y^2 - t')
plt.xlabel('t')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()