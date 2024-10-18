import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# Define the transfer function for the system
num = [1]  # Numerator coefficients (dy/dx = x + 1)
den = [1, 0]  # Denominator coefficients (y is an integral of the right-hand side)
system = ctrl.TransferFunction(num, den)

# Time vector
t = np.linspace(1, 3, 100)

# Step response of the system
t, y = ctrl.forced_response(system, T=t, U=t + 1)

# Plot the results
plt.figure(figsize=(8, 6))
plt.plot(t, y, 'b-', linewidth=2, label='Response of the system')
plt.plot(1, 2, 'ro', markersize=8)  # Initial condition point
plt.text(1, 2, ' (1, 2)', verticalalignment='bottom', horizontalalignment='right')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Control System Response for dy/dx = x + 1')
plt.grid()
plt.legend()
plt.show()