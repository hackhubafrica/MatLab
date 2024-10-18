#Example: State Space Representation and Response

import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt

# State-space matrices
A = np.array([[0, 1], [-1, -1]])
B = np.array([[0], [1]])
C = np.array([[1, 0]])
D = np.array([[0]])

# Initial conditions
x0 = np.array([[1], [0]])

# Time vector
t = np.linspace(0, 10, 100)

# State response
def state_response(A, B, C, D, x0, t):
    x = la.expm(A * t[:, None, None]) @ x0
    y = C @ x
    return y.flatten()

y = state_response(A, B, C, D, x0, t)

# Plot the response
plt.plot(t, y, 'b')
plt.title('State Space Response')
plt.xlabel('Time (s)')
plt.ylabel('Output')
plt.grid()
plt.show()