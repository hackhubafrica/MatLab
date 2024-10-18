import numpy as np

# Parameters
R = 0.5  # Resistance per unit length in ohms/m
L = 2e-6  # Inductance per unit length in henrys/m
G = 0  # Conductance per unit length in siemens/m
C = 100e-12  # Capacitance per unit length in farads/m

# Angular frequency
omega = 2 * np.pi * 1e6  # 1 MHz

# Characteristic impedance
Z0 = np.sqrt((R + 1j * omega * L) / (G + 1j * omega * C))

# Propagation constant
gamma = np.sqrt((R + 1j * omega * L) * (G + 1j * omega * C))

# Output the results
print(f"Characteristic Impedance: {Z0}")
print(f"Propagation Constant: {gamma}")
