import numpy as np

# Define matrices A and B
A = np.array([[1, 2], [3, 4]])
B = np.array([[-1, 0], [0, 1]])

# Matrix multiplication
C = np.dot(A, B)

print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)
print("\nResult of A * B:")
print(C)

'''
Explanation:

Step 1: Define matrices A and B using numpy arrays.
Step 2: Use np.dot function to perform matrix multiplication (A * B).
Step 3: Print out the original matrices A and B, as well as the resulting matrix C.
'''