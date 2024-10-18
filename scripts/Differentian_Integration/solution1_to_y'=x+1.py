import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define the differential equation
def model(y, x):
    return x + 1  # dy/dx = x + 1

# Initial condition
y0 = 2  # y(1) = 2

# Create an array of x values (from 1 to 3 for this example)
x = np.linspace(0, 3, 100)

# Use odeint to solve the differential equation
y = odeint(model, y0, x)

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
