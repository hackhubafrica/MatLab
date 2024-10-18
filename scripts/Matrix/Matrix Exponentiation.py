import numpy as np
from scipy.linalg import expm

# Define a complex matrix A
A = np.array([[-1+2j, 2-3j], [4j, -2]])

# Compute matrix exponential
A_exp = expm(A)
print("\nMatrix Exponential:")
print(A_exp)
