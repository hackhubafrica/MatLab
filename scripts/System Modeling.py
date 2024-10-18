import numpy as np

# Define system matrices (example: DC motor)
A = np.array([[0, 1], [-1, -0.1]])
B = np.array([[0], [1]])
C = np.array([[1, 0]])
D = np.array([[0]])