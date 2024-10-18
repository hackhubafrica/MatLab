'''
Sample Question 1: AC Circuit Analysis
Question: Given an AC circuit with a voltage source 
𝑉𝑠𝑜𝑢𝑟𝑐𝑒=230 at 50Hz a resistor 𝑅=10Ω an inductor 𝐿=0.1H and a capacitor 𝐶=100𝜇F in series, 
calculate the current in the circuit and the voltage drops across each component.
'''

import numpy as np

# Circuit parameters
V_source = 230  # Voltage source in volts
f = 50  # Frequency in Hz
omega = 2 * np.pi * f
print('omega =',omega)
# Impedances
Z_R = 10  # Resistance in ohms
Z_L = 1j * omega * 0.1  # Inductance in henrys
Z_C = 1 / (1j * omega * 100e-6)  # Capacitance in farads
print('Z_R =',Z_R)
print('Z_L =',Z_L)
print('Z_C =',Z_C)



# Total impedance
Z_total = Z_R + Z_L + Z_C

print(f"Total Impedance: {Z_total:.2f} Ω")

# Source current (phasor form)
I = V_source / Z_total
print('I =',I)
# Voltage drops across each component (phasor form)
V_R = I * Z_R
V_L = I * Z_L
V_C = I * Z_C

# Output the results
print(f"Source Current: {I:.2f} A")
print(f"Voltage Drop across R: {V_R:.2f} V")
print(f"Voltage Drop across L: {V_L:.2f} V")
print(f"Voltage Drop across C: {V_C:.2f} V")