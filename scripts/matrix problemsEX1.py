import numpy as np

# Define matrices A and B
A = np.array([[3, -2],
              [-9, 1]])

B = np.array([[-4, 1],
              [0, -5]])

# Compute A - 5B
result = A - 5 * B

print("Example 1:")
print("Matrix A:")
print(A)
print("Matrix B:")
print(B)
print("A - 5B:")
print(result)