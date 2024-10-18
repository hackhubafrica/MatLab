#Example: Transient Analysis of an RC Circuit

import numpy as np
import matplotlib.pyplot as plt

# Circuit parameters
R = 1e3  # Resistance in ohms
C = 1e-6  # Capacitance in farads
V_in = 5  # Input voltage in volts

# Time vector
t = np.linspace(0, 0.01, 1000)

# Transient response
V_out = V_in * (1 - np.exp(-t / (R * C)))

# Plot the transient response
plt.plot(t, V_out, 'b')
plt.title('Transient Response of an RC Circuit')
plt.xlabel('Time (s)')
plt.ylabel('Output Voltage (V)')
plt.grid()
plt.show()