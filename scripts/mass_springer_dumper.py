from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

# Define the differential equation (mass-spring-damper)
def mass_spring_damper(y, t, k, m, c):
    x, v = y
    dydt = [v, -(c/m)*v - (k/m)*x]
    return dydt

# Initial conditions and parameters
y0 = [1.0, 0.0]  # Initial displacement and velocity
t = np.linspace(0, 10, 100)
k, m, c = 5.0, 1.0, 0.5  # Spring constant, mass, damping coefficient

# Solve the system of equations
solution = odeint(mass_spring_damper, y0, t, args=(k, m, c))

# Plot the results
plt.plot(t, solution[:, 0])
plt.xlabel('Time')
plt.ylabel('Displacement')
plt.title('Mass-Spring-Damper System')
plt.show()
