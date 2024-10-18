import numpy as np

# Define matrices A and B
# Define matrices A and B
A = np.array([[-9, -18],
              [2, 4]])

B = np.array([[2, 3, 1],
              [-1, -6, 7],
              [4, 5, -1]])

# Compute determinants
det_A = np.linalg.det(A)
det_B = np.linalg.det(B)

print("\nExample 3:")
print("Matrix A:")
print(A)
print(f"Determinant of A: {det_A}")
print("Matrix B:")
print(B)
print(f"Determinant of B: {det_B}")