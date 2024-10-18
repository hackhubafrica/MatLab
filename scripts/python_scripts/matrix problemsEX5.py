import numpy as np

## Define matrix B
B = np.array([[1, -3],
              [-2, 6]])

# Compute inverse if it exists
try:
    B_inv = np.linalg.inv(B)
    print("\nExample 5:")
    print("Matrix B:")
    print(B)
    print("Inverse of B:")
    print(B_inv)
except np.linalg.LinAlgError:
    print("\nExample 5:")
    print("Matrix B:")
    print(B)
    print("Inverse does not exist.")