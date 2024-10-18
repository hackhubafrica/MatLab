import numpy as np
import matplotlib.pyplot as plt


# Differential Equation: 𝑑𝑦/𝑑𝑥 = 𝑥+1
# Particular Solution: 𝑦=𝑥^2/2 + 𝑥 + 1/2

# Define the function for the solution
def f(x):
    return (x**2) / 2 + x + 1 / 2

# Create a range of x values
x = np.linspace(0, 3, 100)  # From x = 0 to x = 3

# Calculate corresponding y values using the function
y = f(x)

# Plot the results
plt.figure(figsize=(8, 6))
plt.plot(x, y, 'b-', linewidth=2, label='y = (x^2)/2 + x + 1/2')
plt.plot(1, 2, 'ro', markersize=8)  # Initial condition point
plt.text(1, 2, ' (1, 2)', verticalalignment='bottom', horizontalalignment='right')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solution of the Differential Equation dy/dx = x + 1')
plt.grid()
plt.legend()
plt.show()