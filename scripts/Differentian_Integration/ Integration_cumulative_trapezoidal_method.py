import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumtrapz

# Define constants
g = 9.8  # Gravitational acceleration (m/s^2)
C1 = 10  # Initial velocity (m/s)
C2 = 50  # Initial position (m)

# Define the time array
t = np.linspace(0, 10, 500)  # Time from 0 to 10 seconds, 500 points

# Acceleration array (constant)
a = -g * np.ones_like(t)

# Integrate acceleration to get velocity
v = cumtrapz(a, t, initial=C1)  # Integrate a to get v with initial velocity C1

# Integrate velocity to get position
y = cumtrapz(v, t, initial=C2)  # Integrate v to get y with initial position C2

# Plot position vs time
plt.figure(figsize=(8, 6))
plt.plot(t, y, label=f'Position y(t)', color='b')
plt.title('Position of an Object Under Gravity Over Time (Numerical Integration)', fontsize=16)
plt.xlabel('Time (seconds)', fontsize=14)
plt.ylabel('Position (meters)', fontsize=14)
plt.grid(True)
plt.legend()
plt.show()