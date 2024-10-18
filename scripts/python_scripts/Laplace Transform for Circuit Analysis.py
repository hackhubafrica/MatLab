#Example: Solving Circuits Using Laplace Transform

import sympy as sp

# Define the Laplace variable and time variable
s, t = sp.symbols('s t')

# Define the circuit parameters
R = 1  # Resistance in ohms
L = 1e-3  # Inductance in henrys
C = 100e-6  # Capacitance in farads

# Define the input voltage as a function of time
V_in_t = 10 * sp.Heaviside(t)

# Laplace transform of the input voltage
V_in_s = sp.laplace_transform(V_in_t, t, s)[0]

# Define the impedance in the s-domain
Z_R = R
Z_L = s * L
Z_C = 1 / (s * C)

# Total impedance
Z_total = Z_R + Z_L + Z_C

# Solve for the output voltage in the s-domain
V_out_s = V_in_s / Z_total

# Inverse Laplace transform to get the time domain response
V_out_t = sp.inverse_laplace_transform(V_out_s, s, t)

# Output the results
print(f"Output Voltage (time domain): {V_out_t}")