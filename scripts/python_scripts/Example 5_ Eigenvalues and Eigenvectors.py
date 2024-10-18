import numpy as np

# Define matrix D
D = np.array([[3, -1], [-1, 3]])

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(D)

print("Matrix D:")
print(D)
print("\nEigenvalues:")
print(eigenvalues)
print("\nEigenvectors:")
print(eigenvectors)
'''
Explanation:

Step 1: Define matrix D using a numpy array.
Step 2: Use np.linalg.eig to compute the eigenvalues and eigenvectors of matrix D.
Step 3: Print out the original matrix D, its eigenvalues, and corresponding eigenvectors
'''