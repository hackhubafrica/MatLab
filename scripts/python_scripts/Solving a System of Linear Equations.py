import numpy as np

# Coefficients matrix A and constants vector b
A = np.array([[2, 1, -1], [3, 4, 2], [1, -5, 3]])
b = np.array([6, 8, 4])

# Solve for x: Ax = b
x = np.linalg.solve(A, b)
print("Solution for x:")
print(x)

'''
Solution for x:
[ 4.  1. -1.]
'''