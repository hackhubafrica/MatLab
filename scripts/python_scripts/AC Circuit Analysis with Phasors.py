#Example: Solving AC Circuits Using Phasors


import numpy as np

# Define the circuit components
V_source = 230  # Voltage source in volts
f = 50  # Frequency in Hz
omega = 2 * np.pi * f

# Impedances
Z_R = 10  # Resistance in ohms
Z_L = 1j * omega * 0.1  # Inductance in henrys
Z_C = 1 / (1j * omega * 100e-6)  # Capacitance in farads

# Total impedance
Z_total = Z_R + Z_L + Z_C

# Source current (phasor form)
I = V_source / Z_total

# Voltage drops across each component (phasor form)
V_R = I * Z_R
V_L = I * Z_L
V_C = I * Z_C

# Output the results
print(f"Source Current: {I:.2f} A")
print(f"Voltage Drop across R: {V_R:.2f} V")
print(f"Voltage Drop across L: {V_L:.2f} V")
print(f"Voltage Drop across C: {V_C:.2f} V")