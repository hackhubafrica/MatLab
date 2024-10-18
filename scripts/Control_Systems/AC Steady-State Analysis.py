import numpy as np

# Define circuit parameters
V_rms = 230  # RMS voltage in volts
f = 50  # Frequency in Hz
R = 10  # Resistance in ohms
L = 0.1  # Inductance in henrys
C = 100e-6  # Capacitance in farads

# Angular frequency
omega = 2 * np.pi * f

# Impedances
Z_R = R
Z_L = 1j * omega * L
Z_C = 1 / (1j * omega * C)

# Total impedance
Z_total = Z_R + Z_L + Z_C

# Current in the circuit
I_rms = V_rms / Z_total

# Output the results
print(f"Total Impedance: {Z_total}")
print(f"RMS Current: {I_rms}")
