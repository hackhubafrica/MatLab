'''
Example 5: Frequency Response of a Second-Order Band-Pass Filter.py
Question: Analyze the frequency response of a second-order band-pass filter with 
𝑅=1𝑘Ω,𝐿=10𝑚𝐻, and 𝐶=100𝑛𝐹

'''
import numpy as np
import matplotlib.pyplot as plt

# Circuit parameters
R = 1e3  # Resistance in ohms
L = 10e-3  # Inductance in henrys
C = 100e-9  # Capacitance in farads

# Frequency range
frequencies = np.logspace(1, 6, 1000)
omega = 2 * np.pi * frequencies

# Transfer function H(s) = (sL/R) / (s^2 + sR/L + 1/LC)
H = (1j * omega * L / R) / (1j * omega**2 * L * C + 1j * omega * R * C + 1)

# Magnitude and phase
magnitude = 20 * np.log10(np.abs(H))
phase = np.angle(H, deg=True)

# Plot the frequency response
plt.figure()
plt.subplot(2, 1, 1)
plt.semilogx(frequencies, magnitude)
plt.title('Frequency Response of a Second-Order Band-Pass Filter')
plt.ylabel('Magnitude (dB)')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.semilogx(frequencies, phase)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase (degrees)')
plt.grid(True)

plt.show()