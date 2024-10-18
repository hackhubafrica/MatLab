import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np

def model2(Y, x):
    y, dy = Y  # y is the first element, dy is the second
    d2y = 3 * x**2  # The second derivative
    return [dy, d2y]  # Return the derivatives

# Create an array of x values (from 1 to 3 for this example)
x = np.linspace(1, 3, 100)


# Initial conditions
Y0 = [0, 0]  # y(0) = 0, y'(0) = 0

# Solve the ODE
y = odeint(model2, Y0, x)

# Plot the results
plt.figure()
plt.plot(x, y[:, 0])  # Plotting y
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solution of ODE: y\'\' = 3x^2')
plt.grid()
plt.show()