#Example: State-Space Analysis of a Multivariable System

import numpy as np
from scipy.signal import ss2tf, lti, step
import matplotlib.pyplot as plt

# Define the state-space matrices
A = np.array([[0, 1], [-2, -3]])
B = np.array([[0], [1]])
C = np.array([[1, 0], [0, 1]])
D = np.array([[0], [0]])

# Convert to transfer function
num, den = ss2tf(A, B, C, D)
system = lti(num, den)

# Time vector
t = np.linspace(0, 10, 1000)

# Step response
t, y = step(system, T=t)

# Plot the step response
plt.plot(t, y)
plt.title('Step Response of Multivariable System')
plt.xlabel('Time (s)')
plt.ylabel('Output')
plt.grid()
plt.show()


'''
/home/dora/.local/lib/python3.12/site-packages/scipy/signal/_ltisys.py:599: BadCoefficients: Badly conditioned filter coefficients (numerator): the results may be meaningless
  self.num, self.den = normalize(*system)

'''