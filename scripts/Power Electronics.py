#Example: Simulation of a Buck Converter

import numpy as np
import matplotlib.pyplot as plt

# Parameters
V_in = 12  # Input voltage in volts
V_out = 5  # Output voltage in volts
L = 10e-6  # Inductance in henrys
C = 100e-6  # Capacitance in farads
R = 10  # Load resistance in ohms
f = 100e3  # Switching frequency in Hz
D = V_out / V_in  # Duty cycle

# Time vector
t = np.linspace(0, 1 / f, 1000)

# Inductor current waveform (simplified)
I_L = (V_in - V_out) / L * (t % (1 / f) < D / f) * (t % (1 / f))

# Capacitor voltage waveform (simplified)
V_C = np.cumsum(I_L) / (C * f)

# Plot the waveforms
plt.subplot(2, 1, 1)
plt.plot(t, I_L, 'b')
plt.title('Inductor Current')
plt.xlabel('Time (s)')
plt.ylabel('Current (A)')
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(t, V_C, 'r')
plt.title('Capacitor Voltage')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.grid()

plt.tight_layout()
plt.show()