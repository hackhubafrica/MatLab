import numpy as np

# Define matrices A and B
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Addition of matrices A and B
C = A + B
print("Matrix Addition:")
print(C)

# Subtraction of matrices A and B
D = A - B
print("\nMatrix Subtraction:")
print(D)

# Multiplication of matrices A and B (element-wise)
E = A * B
print("\nElement-wise Multiplication:")
print(E)

# Matrix multiplication of A and B
F = np.dot(A, B)
print("\nMatrix Multiplication:")
print(F)
