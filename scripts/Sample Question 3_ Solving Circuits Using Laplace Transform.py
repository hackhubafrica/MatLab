'''
Sample Question 3: Solving Circuits Using Laplace Transform.py
Question: For an RC circuit with 
𝑅=1𝑘Ω and 𝐶=1𝜇F, solve for the output voltage 
𝑉𝑜𝑢𝑡(𝑡) when a step input of 10V is applied at 𝑡=0

'''

import sympy as sp

# Define the Laplace variable and time variable
s, t = sp.symbols('s t')
V_out = sp.Function('V_out')(s)
V_in = 10 / s  # Laplace transform of the step input (10V step input)

# Circuit parameters
R = 1e3  # Resistance in ohms
C = 1e-6  # Capacitance in farads

# Define the circuit equation in Laplace domain
Z_R = R
Z_C = 1 / (s * C)
Z_total = Z_R + Z_C

# Using voltage divider rule
V_out_s = V_in * (Z_C / Z_total)

# Perform the inverse Laplace transform to find v_out(t)
v_out_t = sp.inverse_laplace_transform(V_out_s, s, t)

# Output the result
print(f"Output Voltage v_out(t): {v_out_t}")


'''
Output Voltage v_out(t): 10.0*Heaviside(t) - 10.0*exp(-1000.0*t)*Heaviside(t)
[Finished in 571ms]

'''

#Visualization
import numpy as np
import matplotlib.pyplot as plt

# Time vector
t = np.linspace(0, 0.01, 1000)  # Short time interval due to rapid transient

# Output voltage
v_out = 10.0 - 10.0 * np.exp(-1000.0 * t)

# Plot the response
plt.figure()
plt.plot(t, v_out)
plt.title('Output Voltage v_out(t)')
plt.xlabel('Time (s)')
plt.ylabel('v_out(t)')
plt.grid()
plt.show()
