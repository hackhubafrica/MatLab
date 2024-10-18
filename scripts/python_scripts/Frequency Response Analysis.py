#Example: Frequency Response of a Circuit

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

# Define the circuit components (e.g., RLC circuit)
R = 1  # Resistance in ohms
L = 1e-3  # Inductance in henrys
C = 1e-6  # Capacitance in farads

# Transfer function H(s) = 1 / (LCs^2 + RCs + 1)
num = [1]
den = [L*C, R*C, 1]

# Frequency response
w, h = freqz(num, den, worN=8000)

# Plot the frequency response
plt.plot(0.5 * 8000 * w / np.pi, np.abs(h), 'b')
plt.title('Frequency Response')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain')
plt.grid()
plt.show()