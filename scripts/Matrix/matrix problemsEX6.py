import numpy as np
# Define vectors x1, x2, x3 for Example 6 and Example 7
x1 = np.array([1, -3, 5])
x2 = np.array([-2, 1, 4])
x3_example6 = np.array([6, -2, 1])
x3_example7 = np.array([2, -1, 4])

# Stack vectors into matrix X
X_example6 = np.vstack((x1, x2, x3_example6))
X_example7 = np.vstack((x1, x2, x3_example7))

# Compute the rank of matrix X to determine linear independence
rank_example6 = np.linalg.matrix_rank(X_example6)
rank_example7 = np.linalg.matrix_rank(X_example7)

print("\nExample 6:")
print("Vectors x1, x2, x3:")
print("x1:", x1)
print("x2:", x2)
print("x3:", x3_example6)
if rank_example6 < 3:
    print("Vectors are linearly dependent.")
    # Find the linear relationship if they are dependent
    coeff = np.linalg.solve(X_example6[:, :2], -X_example6[:, 2])
    print("Linear relationship (x3 in terms of x1 and x2):", coeff)
else:
    print("Vectors are linearly independent.")

print("\nExample 7:")
print("Vectors x1, x2, x3:")
print("x1:", x1)
print("x2:", x2)
print("x3:", x3_example7)
if rank_example7 < 3:
    print("Vectors are linearly dependent.")
    # Find the linear relationship if they are dependent
    coeff = np.linalg.solve(X_example7[:, :2], -X_example7[:, 2])
    print("Linear relationship (x3 in terms of x1 and x2):", coeff)
else:
    print("Vectors are linearly independent.")