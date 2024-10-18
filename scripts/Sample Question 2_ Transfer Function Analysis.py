'''
Sample Question 2: Transfer Function Analysis.py
Question: Determine the transfer function 
𝐻(𝑠) of an RLC series circuit with 
𝑅=1𝑘Ω, 𝐿=100𝑚𝐻, and 𝐶=10𝜇F, and plot its step response.
'''
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lti, step

# Circuit parameters
R = 1e3  # Resistance in ohms
L = 100e-3  # Inductance in henrys
C = 10e-6  # Capacitance in farads

# Transfer function H(s) = 1 / (LCs^2 + RCs + 1)
num = [1]
den = [L * C, R * C, 1]
system = lti(num, den)

# Time vector
t = np.linspace(0, 0.1, 1000)

# Step response
t, y = step(system, T=t)

# Plot the step response
plt.plot(t, y)
plt.title('Step Response of RLC Series Circuit')
plt.xlabel('Time (s)')
plt.ylabel('Output Voltage (V)')
plt.grid()
plt.show()