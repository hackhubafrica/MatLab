import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Define system parameters
num = [1, 2]  # Numerator: s + 2
den = [1, 1, 2]  # Denominator: s^2 + s + 2

# Create a transfer function for step response
system = signal.TransferFunction(num, den)

# Time vector
dt = 0.01  # Sample time
total_time = 10  # Total time for simulation
time = np.arange(0, total_time + dt, dt)  # Time vector

# Get step response
time_step, response_step = signal.step(system, T=time)

# Plot step response
plt.figure()
plt.plot(time_step, response_step, label='Step Response (Continuous)')
plt.xlabel('Time (s)')
plt.ylabel('Response')
plt.title('Step Response of the System')
plt.grid(True)
plt.legend()
plt.show()

# Define initial conditions and system dynamics for numerical solution
y = np.zeros_like(time)   # Position (output)
yd = np.zeros_like(time)  # Velocity (first derivative of y)
u = np.ones_like(time) * 6  # Input (constant step input for now)

# Initial conditions
y[0] = 0  # Initial position
yd[0] = 0  # Initial velocity

# Coefficients from the system equation (a1 * ydd + a2 * yd + a3 * y = u)
a1 = 1  # Coefficient of ydd (s^2)
a2 = 1  # Coefficient of yd (s)
a3 = 2  # Coefficient of y (constant term)

# Numerical solution using for-else loop
for i in range(1, len(time)):
    if i == 1:
        # First step: solve using initial conditions
        ydd = (u[i-1] - a2 * yd[i-1] - a3 * y[i-1]) / a1  # Second derivative (acceleration)
    else:
        # Solve for subsequent time steps
        ydd = (u[i-1] - a2 * yd[i-1] - a3 * y[i-1]) / a1  # Acceleration
        yd[i] = yd[i-1] + ydd * dt  # Update velocity
        y[i] = y[i-1] + yd[i-1] * dt  # Update position using velocity (integral of yd)

# Plot results
plt.figure()
plt.plot(time, y, label='Numerical Solution (Position)')
plt.plot(time, yd, label='Numerical Solution (Velocity)')
plt.xlabel('Time (s)')
plt.ylabel('Response')
plt.title('Numerical Solution of Second-Order Differential Equation')
plt.grid(True)
plt.legend()
plt.show()
