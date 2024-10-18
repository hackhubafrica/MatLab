import numpy as np
# Define matrix A
A2 = np.array([[1, -1, 4],
               [9, -1, 3]])

# Compute eigenvalues and eigenvectors
eigenvalues2, eigenvectors2 = np.linalg.eig(A2)

print("\nExample 2:")
print("Matrix A:")
print(A2)
print("Eigenvalues:", eigenvalues2)
print("Eigenvectors:")
for i in range(len(eigenvectors2)):
    print(f"Eigenvalue {i+1}: {eigenvectors2[:,i]}")