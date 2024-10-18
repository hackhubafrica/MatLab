'''
Example 3: Resonant Frequency Calculation.py
Question: Calculate the resonant frequency and bandwidth of an RLC circuit with 
𝑅=10Ω, 𝐿=0.1H, and 𝐶=10𝜇F
'''

import numpy as np

# Circuit parameters
R = 10  # Resistance in ohms
L = 0.1  # Inductance in henrys
C = 10e-6  # Capacitance in farads

# Resonant frequency
omega_0 = 1 / np.sqrt(L * C)
f_0 = omega_0 / (2 * np.pi)
print(f"Resonant Frequency: {f_0:.2f} Hz")

# Bandwidth
bandwidth = R / (2 * np.pi * L)
print(f"Bandwidth: {bandwidth:.2f} Hz")