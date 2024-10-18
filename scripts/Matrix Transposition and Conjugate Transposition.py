import numpy as np

# Define a complex matrix
A = np.array([[1+2j, 3-1j], [4j, 2]])

# Transposition
A_transpose = A.T
print("Matrix Transposition:")
print(A_transpose)

# Conjugate Transposition
A_conjugate_transpose = A.conj().T
print("\nMatrix Conjugate Transposition:")
print(A_conjugate_transpose)