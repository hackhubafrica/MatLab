import numpy as np

# Define matrix A
A1 = np.array([[2, 7],
               [-1, -6]])

# Compute eigenvalues and eigenvectors
eigenvalues1, eigenvectors1 = np.linalg.eig(A1)

print("Example 1:")
print("Matrix A:")
print(A1)
print("Eigenvalues:", eigenvalues1)
print("Eigenvectors:")
for i in range(len(eigenvectors1)):
    print(f"Eigenvalue {i+1}: {eigenvectors1[:,i]}")