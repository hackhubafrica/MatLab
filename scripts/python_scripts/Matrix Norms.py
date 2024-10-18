import numpy as np
from scipy.linalg import expm

# Define matrices A and B
A = np.array([[1+1j, 2], [3, 4-2j]])
B = np.array([[5-3j, 7], [8j, 9]])

# Solve for X in AX = B
X = np.linalg.solve(A, B)
print("\nSolution X for AX = B:")
print(X)
'''
Matrix norms quantify the size of a matrix.
Examples include the Frobenius norm and the spectral norm.
'''
# Compute Frobenius norm
norm_frobenius = np.linalg.norm(A)
print("\nFrobenius Norm of A:", norm_frobenius)

# Compute spectral norm
norm_spectral = np.linalg.norm(A, ord=2)
print("\nSpectral Norm of A:", norm_spectral)