from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.8  # Gravitational acceleration (m/s^2)
C1 = 10  # Initial velocity (m/s)
C2 = 50  # Initial position (m)

# Time array
t_span = (0, 10)  # Time from 0 to 10 seconds
t_eval = np.linspace(0, 10, 500)  # Points at which to evaluate the solution

# Define the system of differential equations
def equations(t, y):
    # y[0] is position, y[1] is velocity
    dydt = [y[1], -g]  # Velocity and acceleration (second derivative)
    return dydt

# Initial conditions [y(0) = C2, v(0) = C1]
y0 = [C2, C1]

# Solve the differential equation
sol = solve_ivp(equations, t_span, y0, t_eval=t_eval)

# Extract position and time
y = sol.y[0]
t = sol.t

# Plot the results
plt.figure(figsize=(8, 6))
plt.plot(t, y, label='Position y(t)', color='b')
plt.title('Position of an Object Under Gravity Over Time (Runge-Kutta methods)', fontsize=16)
plt.xlabel('Time (seconds)', fontsize=14)
plt.ylabel('Position (meters)', fontsize=14)
plt.grid(True)
plt.legend()
plt.show()
