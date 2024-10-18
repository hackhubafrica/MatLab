import numpy as np
# Generate a complex matrix

'''
Singular Value Decomposition (SVD)
SVD decomposes a matrix into three simpler matrices: 
𝐴=𝑈Σ𝑉 , where U and 𝑉 are unitary matrices and 
Σ is a diagonal matrix of singular values.
'''
A = np.array([[1+2j, 3-1j], [4j, 2]])

# Perform SVD
U, S, Vh = np.linalg.svd(A)

print("\nSingular Values:")
print(S)

print("\nLeft Singular Vectors (U):")
print(U)

print("\nRight Singular Vectors (V conjugate transpose):")
print(Vh)