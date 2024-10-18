import numpy as np
import matplotlib.pyplot as plt

# Parameters
dt = 0.1  # Sample time
total_time = 10  # Total simulation time
t = np.arange(0, total_time + dt, dt)  # Time vector

# Predefine the size of the input/output vectors
ud = np.zeros_like(t)  # First derivative of input
y = np.zeros_like(t)   # Output (position)
yd = np.zeros_like(t)  # First derivative of output (velocity)
ydd = np.zeros_like(t) # Second derivative of output (acceleration)

# Initial conditions
y[0] = 2   # Initial position
yd[0] = 4  # Initial velocity
ud[0] = 6  # Initial input

# Step through time and solve the differential equation
for i in range(1, len(t)):
    # Input: Here you can define how your input changes over time
    ud[i] = 6  # Keep input constant (for simplicity)

    # Calculate the second derivative (acceleration) using the differential equation
    ydd[i] = ud[i] + 2 * ud[i] - yd[i-1] - 2 * y[i-1]  # Differential equation

    # Update the first derivative (velocity) using the previous value
    yd[i] = yd[i-1] + dt * ydd[i-1]  # yd = integral of ydd with respect to time

    # Update the output (position) using the previous value
    y[i] = y[i-1] + dt * yd[i-1]  # y = integral of yd with respect to time

# Plot the results
plt.figure()
plt.scatter(t, y, s=3, label='Position y(t)')  # Scatter plot for position
plt.plot(t, yd, 'r', label='Velocity yd(t)')  # Line plot for velocity
plt.legend()
plt.title('Numerical Solution of Second-Order Differential Equation')
plt.xlabel('Time (s)')
plt.ylabel('Response')
plt.grid()
plt.show()
