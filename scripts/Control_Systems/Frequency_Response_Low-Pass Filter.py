'''
Example 4: Frequency Response of a Low-Pass Filter.py
Question: Analyze the frequency response of a first-order low-pass filter with 
𝑅=1𝑘Ω  and 𝐶=1𝜇F.
'''

import numpy as np
import matplotlib.pyplot as plt

# Circuit parameters
R = 1e3  # Resistance in ohms
C = 1e-6  # Capacitance in farads

# Frequency range
frequencies = np.logspace(1, 6, 1000)
omega = 2 * np.pi * frequencies

# Transfer function H(s) = 1 / (RCs + 1)
H = 1 / (1 + 1j * omega * R * C)

# Magnitude and phase
magnitude = 20 * np.log10(np.abs(H))
phase = np.angle(H, deg=True)

# Plot the frequency response
plt.figure()
plt.subplot(2, 1, 1)
plt.semilogx(frequencies, magnitude)
plt.title('Frequency Response of a First-Order Low-Pass Filter')
plt.ylabel('Magnitude (dB)')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.semilogx(frequencies, phase)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase (degrees)')
plt.grid(True)

plt.show()