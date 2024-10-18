import numpy as np

# Define matrix C
C = np.array([[2, -1], [-3, 4]])

# Calculate the inverse of C
C_inv = np.linalg.inv(C)

print("Matrix C:")
print(C)
print("\nInverse of C:")
print(C_inv)