import numpy as np

# Define matrices A and B
# Define matrix A
A = np.array([[2, 1, 1],
              [-5, -3, 0],
              [1, 1, -1]])

# Compute inverse if it exists
try:
    A_inv = np.linalg.inv(A)
    print("\nExample 4:")
    print("Matrix A:")
    print(A)
    print("Inverse of A:")
    print(A_inv)
except np.linalg.LinAlgError:
    print("\nExample 4:")
    print("Matrix A:")
    print(A)
    print("Inverse does not exist.")