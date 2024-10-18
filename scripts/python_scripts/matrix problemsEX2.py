import numpy as np

# Define matrices A and B
# Define matrices A and B
A = np.array([[2, -1, 0],
              [-3, 6, 1]])

B = np.array([[1, 0, -1],
              [2, -4, 3],
              [1, 0, 0]])

# Compute AB
result = np.dot(A, B)

print("\nExample 2:")
print("Matrix A:")
print(A)
print("Matrix B:")
print(B)
print("AB:")
print(result)
