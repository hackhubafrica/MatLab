#Example: Short Circuit Analysis

import numpy as np

# Define the system parameters
V_base = 11e3  # Base voltage in volts
S_base = 100e6  # Base power in VA

print('V_base =',V_base)
print('S_base =',S_base)
# Impedances (per unit)
Z_th = 0.1 + 0.2j  # Thevenin impedance
print('Z_th =',Z_th)

# Fault current calculation for a three-phase fault
I_fault = V_base / (np.sqrt(3) * Z_th)
print('I_fault =',I_fault)


# Output the results
print(f"Fault Current: {I_fault:.2f} A")