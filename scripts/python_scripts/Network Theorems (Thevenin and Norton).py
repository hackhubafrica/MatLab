#Example: Thevenin Equivalent Circuit


import numpy as np

# Define the circuit parameters
V1 = 12  # Voltage source 1 in volts
R1 = 10  # Resistance 1 in ohms
R2 = 5  # Resistance 2 in ohms
R3 = 15  # Resistance 3 in ohms

# Find Thevenin equivalent resistance (R_th)
R_th = (R1 * R2) / (R1 + R2) + R3

# Find Thevenin equivalent voltage (V_th)
V_th = V1 * (R2 / (R1 + R2))

# Output the results
print(f"Thevenin Equivalent Resistance: {R_th:.2f} ohms")
print(f"Thevenin Equivalent Voltage: {V_th:.2f} volts")