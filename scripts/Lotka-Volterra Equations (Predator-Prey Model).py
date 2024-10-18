import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

'''
Another classic example of a nonlinear system is the 
Lotka-Volterra equations, which describe the interaction 
between predator and prey populations:
'''

# Define the function that represents the Lotka-Volterra equations
def lotka_volterra(z, t, alpha, beta, delta, gamma):
    x, y = z
    dxdt = alpha*x - beta*x*y
    dydt = delta*x*y - gamma*y
    return [dxdt, dydt]

# Parameters
alpha = 1.0
beta = 0.5
delta = 0.5
gamma = 1.0

# Initial conditions
x0 = 2.0
y0 = 1.0

# Time points for which to solve the ODE (0 to 10 in steps of 0.01)
t = np.arange(0, 10, 0.01)

# Solve the ODE using odeint
z0 = [x0, y0]
z = odeint(lotka_volterra, z0, t, args=(alpha, beta, delta, gamma))

# Extract x(t) and y(t) from the solution
x = z[:, 0]
y = z[:, 1]

# Plot the solution
plt.figure(figsize=(8, 6))
plt.plot(t, x, label='Prey (x)')
plt.plot(t, y, label='Predator (y)')
plt.title('Lotka-Volterra Equations (Predator-Prey Model)')
plt.xlabel('Time')
plt.ylabel('Population')
plt.grid(True)
plt.legend()
plt.show()