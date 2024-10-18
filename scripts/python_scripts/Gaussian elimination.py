import numpy as np

def gaussian_elimination(aug_matrix):
    """
    Perform Gaussian elimination on the augmented matrix.
    
    Parameters:
    - aug_matrix: numpy array, augmented matrix of shape (n, n+1)
    
    Returns:
    - solution: numpy array, vector of solutions if a unique solution exists
    - 'No solution' string if there's no solution
    - 'Infinite solutions' string if there are infinitely many solutions
    """
    n = aug_matrix.shape[0]
    
    # Forward elimination phase
    for i in range(n):
        # Find pivot row (maximum absolute value in the current column)
        max_row = i
        for k in range(i + 1, n):
            if abs(aug_matrix[k, i]) > abs(aug_matrix[max_row, i]):
                max_row = k
        
        # Swap rows if necessary (to avoid division by zero)
        if max_row != i:
            aug_matrix[[i, max_row]] = aug_matrix[[max_row, i]]
        
        # Check if the matrix is singular (no pivot element in this column)
        if aug_matrix[i, i] == 0:
            if aug_matrix[i, n] != 0:
                return 'No solution'
            continue
        
        # Eliminate below the current row
        for k in range(i + 1, n):
            factor = aug_matrix[k, i] / aug_matrix[i, i]
            aug_matrix[k, i:] -= factor * aug_matrix[i, i:]
    
    # Back substitution phase
    solution = np.zeros(n)
    for i in range(n - 1, -1, -1):
        if aug_matrix[i, i] == 0:
            continue
        
        solution[i] = (aug_matrix[i, n] - np.dot(aug_matrix[i, i+1:n], solution[i+1:])) / aug_matrix[i, i]
    
    # Check for infinite solutions
    if np.any(np.isnan(solution)):
        return 'Infinite solutions'
    
    return solution

# Example 2: Solve the system of equations
aug_matrix_example2 = np.array([
    [1, -2, 3, -2],
    [-1, 1, -2, 3],
    [2, -1, 3, 1]
], dtype=float)

print("Example 2:")
print("Augmented Matrix:")
print(aug_matrix_example2)
print()

solution_example2 = gaussian_elimination(aug_matrix_example2)

if isinstance(solution_example2, str):
    print(solution_example2)
else:
    print("Solution:")
    print(solution_example2)

# Example 3: Solve the system of equations
aug_matrix_example3 = np.array([
    [1, -2, 3, -2],
    [-1, 1, -2, 3],
    [2, -1, 3, -7]
], dtype=float)

print("\nExample 3:")
print("Augmented Matrix:")
print(aug_matrix_example3)
print()

solution_example3 = gaussian_elimination(aug_matrix_example3)

if isinstance(solution_example3, str):
    print(solution_example3)
else:
    print("Solution:")
    print(solution_example3)



'''
Explanation:
gaussian_elimination Function:

Forward Elimination Phase: Iterates through each row to perform row operations (partial pivoting if necessary) to eliminate below the current row.
Back Substitution Phase: Solves the resulting upper triangular system to find the solution vector.
Checking for Solutions: Handles cases where the system is singular (no solution) or where there are infinitely many solutions (dependent equations).
Examples (Example 2 and Example 3):

Each example provides its augmented matrix as input to the gaussian_elimination function.
It prints the augmented matrix and the solution or the respective message indicating no solution or infinite solutions.
'''