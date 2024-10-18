import numpy as np
import matplotlib.pyplot as plt

# Define the admittance matrix Y and current vector I
Y = np.array([[10, -5, 0], [-5, 15, -5], [0, -5, 10]])
I = np.array([10, 0, 0])

print('admittance matrix Y:')
print(Y)
print('current vector I')
print(I)
# Solve for node voltages V
V = np.linalg.solve(Y, I)
print(f"Node Voltages: {V}")
